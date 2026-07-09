"""
Cross-reference a component card's pin table against the real Altium netlist
to answer "what's left to wire, and which direction is each signal."

Deterministic, no LLM: parses the markdown pin table (regex on the row shape
used in docs/components/<PART>.md -- # | Name | Type | Vendor function |
Cradle Wiring | Status), filters to rows whose Cradle Wiring mentions a
target designator (e.g. the RK3576 is U1 in the BOM), and reports per pin:
whether that pin has *any* net on the source part's side yet, and whether
that net actually reaches the target designator yet.

This directly answers the recurring question "what remaining signal wires
do I need to connect on <SoC>, as it stands" without re-deriving the pin
list from memory or re-reading the component card by hand each time.

Usage:
    python wiring_check.py <component_card.md> <source_designator> <target_designator> <target_name> <netlist.NET>

Example:
    python wiring_check.py docs/components/AP6275S.md U2 U1 RK3576 docs/Altium/Netlist/Cradle.NET
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from netlist_parse import parse_netlist, get_designator_pins, freshness_line  # noqa: E402


def get_really_wired_pins(nets, designator):
    """Like get_designator_pins(), but excludes pins whose only net has a
    single member -- Altium emits a net entry (auto-named NetXX_Y) even for
    a completely isolated pin, so 'appears in some net' is NOT the same as
    'connects to anything real'. Use this, not get_designator_pins(), for
    any check that means to answer 'is this pin actually wired to something
    else' -- see the CBUCK_0P9/CSR_VLX miss this was built to fix."""
    pin_re = re.compile(rf"^{re.escape(designator)}-(\S+)$")
    pins = set()
    for net in nets:
        if len(net["members"]) < 2:
            continue
        for m in net["members"]:
            match = pin_re.match(m)
            if match:
                pins.add(match.group(1))
    return pins

PIN_ROW_RE = re.compile(
    r"^\|\s*([\d,\-]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*$"
)
NOT_ROUTED_RE = re.compile(r"\bnot routed\b|\bno-connect\b|\bno connect\b", re.IGNORECASE)


def parse_pin_table(card_path):
    """Extract rows from the '## Pin table' section of a component card."""
    text = Path(card_path).read_text(encoding="utf-8")
    rows = []
    in_table = False
    for line in text.split("\n"):
        if line.strip().startswith("| #"):
            in_table = True
            continue
        if in_table:
            if not line.strip().startswith("|"):
                break
            if set(line.strip()) <= set("|-: "):
                continue
            m = PIN_ROW_RE.match(line)
            if m:
                pin_field, name, io_type, vendor_fn, cradle_wiring, status = m.groups()
                rows.append({
                    "pins": pin_field.strip(), "name": name.strip(),
                    "type": io_type.strip(), "cradle_wiring": cradle_wiring.strip(),
                    "status": status.strip(),
                })
    return rows


def expand_pin_field(pin_field):
    """'1,3-8,10' -> [1,3,4,5,6,7,8,10]. Handles the comma/range shorthand
    used for grouped GND/NC rows in component card pin tables."""
    pins = []
    for part in pin_field.split(","):
        part = part.strip()
        if "-" in part and part.replace("-", "").isdigit():
            lo, hi = part.split("-")
            pins.extend(range(int(lo), int(hi) + 1))
        elif part.isdigit():
            pins.append(int(part))
    return pins


def check_wiring(card_path, source_designator, target_designator, target_name, netlist_path):
    """target_name: how the target part is referred to in the component card's
    prose (e.g. 'RK3576') -- component cards describe parts by name, not by
    BOM designator, so matching needs both."""
    rows = parse_pin_table(card_path)
    _, nets = parse_netlist(netlist_path)
    wired_pins = get_designator_pins(nets, source_designator)

    results = []
    for row in rows:
        if target_name not in row["cradle_wiring"]:
            continue
        if NOT_ROUTED_RE.search(row["cradle_wiring"]):
            continue  # e.g. BT_PCM_* mentions RK3576 in its explanation but is explicitly not routed
        for pin in expand_pin_field(row["pins"]):
            has_net = str(pin) in wired_pins
            reaches_target = False
            if has_net:
                for net in nets:
                    members = net["members"]
                    if any(m == f"{source_designator}-{pin}" for m in members):
                        reaches_target = any(m.startswith(f"{target_designator}-") for m in members)
            results.append({
                "pin": pin, "name": row["name"], "type": row["type"],
                "status": row["status"], "has_net": has_net, "reaches_target": reaches_target,
            })
    return sorted(results, key=lambda r: r["pin"])


def check_open_items(card_path, source_designator, netlist_path):
    """Different check from check_wiring() above -- that one only covers
    signals meant to reach a *different* designator (e.g. RK3576). This
    covers the pattern that check missed entirely: a pin-table row marked
    Open/Not addressed that's actually a same-part loop (two pins on the
    source designator itself needing an external component bridging them,
    e.g. AP6275S's CBUCK/ABUCK buck loops) or any other still-unresolved
    row, regardless of what it mentions. Just reports current netlist
    connectivity for every non-Decided row so nothing needs a target name
    to be checked."""
    rows = parse_pin_table(card_path)
    _, nets = parse_netlist(netlist_path)
    # Cardinality-based on purpose: this check answers "is a real component
    # bridging/using this pin", not "is a port name waiting for a far sheet"
    # (that's check_wiring()'s job, where a single-pin named net is real
    # progress). A single-pin net here -- named or not -- means no real
    # component has been placed on it either way.
    wired_pins = get_really_wired_pins(nets, source_designator)

    results = []
    for row in rows:
        if row["status"].startswith("Decided"):
            continue
        for pin in expand_pin_field(row["pins"]):
            has_net = str(pin) in wired_pins
            results.append({
                "pin": pin, "name": row["name"], "type": row["type"],
                "status": row["status"], "has_net": has_net,
            })
    return sorted(results, key=lambda r: r["pin"])


def format_open_report(results, source_designator):
    lines = [
        f"| Pin | Signal | Dir | Card status | {source_designator}-side wired? |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        wired = "yes" if r["has_net"] else "**NO (still open)**"
        lines.append(f"| {r['pin']} | {r['name']} | {r['type']} | {r['status']} | {wired} |")
    return "\n".join(lines)


def format_report(results, source_designator, target_designator):
    lines = [
        f"| Pin | Signal | Dir | Card status | {source_designator}-side wired? | Reaches {target_designator} yet? |",
        "|---|---|---|---|---|---|",
    ]
    for r in results:
        wired = "yes" if r["has_net"] else "**NO (no net at all)**"
        reaches = "yes" if r["reaches_target"] else "no"
        lines.append(f"| {r['pin']} | {r['name']} | {r['type']} | {r['status']} | {wired} | {reaches} |")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) == 5 and sys.argv[1] == "--open":
        _, card_path, source, netlist_path = sys.argv[1:5]
        print(f"SOURCE FRESHNESS: {freshness_line(card_path, netlist_path)}")
        print(f"Checking every non-Decided row in {card_path} against current {source} netlist connectivity.")
        print("This does NOT require a target designator -- catches same-part loops "
              "(e.g. two pins needing an external bridging component) that check_wiring() "
              "structurally can't see, since those rows never mention a target part by name.\n")
        results = check_open_items(card_path, source, netlist_path)
        print(format_open_report(results, source))
        still_open = [r for r in results if not r["has_net"]]
        print(f"\n{len(still_open)} of {len(results)} non-Decided pin(s) still have no netlist connection at all.")
    elif len(sys.argv) >= 6:
        card_path, source, target, target_name, netlist_path = sys.argv[1:6]
        print(f"SOURCE FRESHNESS: {freshness_line(card_path, netlist_path)}")
        print("A 'not wired' finding below is indistinguishable from a stale netlist export -- re-export before trusting it.\n")
        results = check_wiring(card_path, source, target, target_name, netlist_path)
        print(format_report(results, source, target))

        unwired = [r for r in results if not r["has_net"]]
        not_reaching = [r for r in results if r["has_net"] and not r["reaches_target"]]
        print(f"\n{len(unwired)} signal(s) not wired at all on {source} side; "
              f"{len(not_reaching)} wired on {source} side but not yet reaching {target}.")
    else:
        print("Usage:")
        print("  python wiring_check.py <component_card.md> <source_designator> <target_designator> <target_name> <netlist.NET>")
        print("  python wiring_check.py --open <component_card.md> <source_designator> <netlist.NET>")
        sys.exit(1)
