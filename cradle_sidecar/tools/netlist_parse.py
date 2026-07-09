"""
Altium Protel netlist + BOM parser.

Deterministic parsing only, same philosophy as datasheet_index.py -- no LLM,
no interpretation of what a net *should* be, just mechanical extraction of
what the netlist and BOM actually say. Two outputs:

1. <prefix>.netlist-summary.md -- every net, its member pins (resolved to
   part name/description via the BOM), and two cheap-but-real flags:
   - "floating": net has exactly one pin -- almost certainly an error, a
     single-ended net can't do anything (rare in practice since Altium
     usually doesn't emit a net for a truly disconnected pin at all -- see
     pin-coverage check below for the more common failure mode).
   - "unlabeled": Altium auto-generated the net name (NetR12_2 etc.) because
     no one placed a manual net label -- not necessarily wrong, but worth a
     glance since meaningful nets usually get named deliberately.

2. Programmatic access to per-designator pin coverage (which pin numbers on
   a given designator actually appear in *any* net) -- this is the
   important one. A pin with genuinely no connection doesn't show up as a
   floating net, it just never appears anywhere in the netlist at all
   (Altium only emits nets for pins that are actually wired to something).
   The only way to catch that is comparing against the *expected* pin count
   from a real pin table -- e.g. cradle_sidecar/data/components/<PART>.md -- which this
   script doesn't have built in (it doesn't know what a part's pins should
   be), but exposes get_designator_pins() so that comparison can be made
   wherever a component card already exists.

Usage:
    python netlist_parse.py <netlist.NET> <bom.csv> [output_prefix]
"""

import csv
import datetime
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paths import SHEET_MAP_PATH, STANDARD_PARTS_PATH  # noqa: E402


def freshness_line(*paths):
    """Every report from this script should visibly state when its source
    files were last exported -- a stale netlist reporting 'this net doesn't
    exist' looks identical to a fresh one, and that ambiguity is exactly
    what makes a missing-net finding untrustworthy without this. See
    cradle_sidecar/co-design-workflow.md, 2026-07-08 entry, for why this exists."""
    lines = []
    for p in paths:
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(p))
        lines.append(f"{Path(p).name}: exported {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
    return " | ".join(lines)

COMPONENT_BLOCK_RE = re.compile(r"\[\n(.*?)\n\]", re.DOTALL)
NET_BLOCK_RE = re.compile(r"\(\n(.*?)\n\)", re.DOTALL)
AUTO_NET_NAME_RE = re.compile(r"^Net[A-Z]+\d+_\d+$")


def parse_netlist(netlist_path):
    text = Path(netlist_path).read_text(encoding="utf-8", errors="replace")

    components = {}
    for block in COMPONENT_BLOCK_RE.findall(text):
        lines = block.split("\n")
        designator = lines[0].strip()
        footprint = lines[1].strip() if len(lines) > 1 else ""
        libref_or_value = lines[2].strip() if len(lines) > 2 else ""
        components[designator] = {"footprint": footprint, "value": libref_or_value}

    nets = []
    for block in NET_BLOCK_RE.findall(text):
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        if not lines:
            continue
        name, members = lines[0], lines[1:]
        nets.append({"name": name, "members": members})

    return components, nets


def parse_bom(bom_path):
    """Returns designator -> {name, description, sheet}. `sheet` is an exact
    single sheet number when the BOM row lists one designator, or a
    comma-joined *set* of sheet numbers (ambiguous, can't be resolved to a
    specific instance) when the row groups multiple designators sharing one
    part value -- see cradle_sidecar/data/altium/sheet-map.md for why."""
    designator_map = {}
    with open(bom_path, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("Designator"):
                continue
            name = row.get("Name", "")
            desc = row.get("Description", "")
            designators = [d.strip() for d in row["Designator"].split(",") if d.strip()]
            sheet_field = row.get("SheetNumber", "")
            is_ambiguous = len(designators) > 1 and "," in sheet_field
            sheet = sheet_field.strip() if not is_ambiguous else f"ambiguous({sheet_field.strip()})"
            for d in designators:
                designator_map[d] = {"name": name, "description": desc, "sheet": sheet}
    return designator_map


def load_sheet_map(path=SHEET_MAP_PATH):
    p = Path(path)
    if not p.exists():
        return {}
    mapping = {}
    for line in p.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*$", line)
        if m:
            mapping[m.group(1)] = m.group(2)
    return mapping


def resolve_sheet_name(sheet_value, sheet_map):
    """sheet_value may be a plain number, 'ambiguous(1, 2, 3)', or empty."""
    if not sheet_value:
        return "?"
    m = re.match(r"^ambiguous\((.+)\)$", sheet_value)
    if m:
        names = [sheet_map.get(s.strip(), s.strip()) for s in m.group(1).split(",")]
        return "ambiguous(" + ", ".join(names) + ")"
    return sheet_map.get(sheet_value, sheet_value)


def load_standard_parts(path=STANDARD_PARTS_PATH):
    """Designators the user holds as staged/generic stock, not yet placed
    into a real circuit role -- see that file for the discipline this
    depends on. Both pins of these designators are *expected* to be
    orphaned; excluded from the orphan review list so real problems aren't
    buried under known-staged parts."""
    p = Path(path)
    if not p.exists():
        return set()
    designators = set()
    for line in p.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\|\s*([A-Z]+\d+)\s*\|", line)
        if m:
            designators.add(m.group(1))
    return designators


def get_designator_pins(nets, designator):
    """All pin numbers of `designator` that appear anywhere in the netlist
    (i.e. are actually wired to something). Compare against a component
    card's full pin table to find pins with no connection at all."""
    pin_re = re.compile(rf"^{re.escape(designator)}-(\S+)$")
    pins = set()
    for net in nets:
        for m in net["members"]:
            match = pin_re.match(m)
            if match:
                pins.add(match.group(1))
    return pins


def classify_floating_nets(nets, standard_parts):
    """Single source of truth for the orphaned/staged/pending-port split --
    write_summary() and project_refresh.py both need this exact
    classification and must not reimplement it separately. A prior version
    of project_refresh.py did reimplement it (inline, wrong), producing 485
    'orphaned' pins where the real number was 118 -- see
    cradle_sidecar/co-design-workflow.md, 2026-07-08, for the fix."""
    floating = [n for n in nets if len(n["members"]) == 1]
    all_orphaned = [n for n in floating if AUTO_NET_NAME_RE.match(n["name"])]
    pending_port = [n for n in floating if not AUTO_NET_NAME_RE.match(n["name"])]

    def designator_of(n):
        return n["members"][0].split("-")[0]

    staged = [n for n in all_orphaned if designator_of(n) in standard_parts]
    orphaned = [n for n in all_orphaned if designator_of(n) not in standard_parts]
    return orphaned, staged, pending_port


def write_summary(netlist_path, components, bom, nets, out_path, standard_parts=None, sheet_map=None):
    standard_parts = standard_parts or set()
    sheet_map = sheet_map or {}
    designator_re = re.compile(r"^(\S+?)-(\S+)$")

    def sheet_of(designator):
        return resolve_sheet_name(bom.get(designator, {}).get("sheet", ""), sheet_map)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Netlist summary: {Path(netlist_path).name}\n\n")
        f.write(f"**Source freshness:** {freshness_line(netlist_path)}\n\n")
        f.write(
            "Auto-generated. Deterministic parse of the Protel netlist + BOM -- "
            "no interpretation of intent, just what's actually wired. "
            "`floating` = single-pin net (rare, usually a real error). "
            "`unlabeled` = Altium auto-generated name, no manual net label placed "
            "(common on in-progress sheets, not necessarily wrong). Neither flag "
            "catches a pin with *no* net entry at all -- that requires comparing "
            "against a component's full pin table separately; see "
            "get_designator_pins() in netlist_parse.py. **A 'net doesn't exist' or "
            "'pin has no connection' finding is indistinguishable from a stale "
            "export** -- re-export before trusting a missing-net report, and treat "
            "hierarchical port resolution (does a net label actually reach a "
            "matching Sheet Entry) as something only Altium's own ERC/Compile "
            "output can confirm, not this parser.\n\n"
        )
        f.write(f"Components: {len(components)}. Nets: {len(nets)}.\n\n")

        orphaned, staged, pending_port = classify_floating_nets(nets, standard_parts)
        floating = orphaned + staged + pending_port

        def designator_of(n):
            return n["members"][0].split("-")[0]

        f.write(
            f"Single-pin nets: {len(floating)} total -- {len(pending_port)} deliberately named "
            f"(`pending-port`: a real hierarchical port net, expected to be single-pin until the "
            f"far sheet exists -- not a problem by itself), {len(staged)} on known staged/standard "
            f"parts (`cradle_sidecar/data/altium/standard-parts.md` -- expected, excluded from review below), and "
            f"{len(orphaned)} genuinely unexplained auto-named orphans -- these are the real "
            f"candidates for review/No Connect.\n\n"
        )

        if orphaned:
            f.write("## Orphaned pins (auto-named, no label, connects to nothing, not a known staged part -- review these)\n\n")
            f.write("| Net | Pin | Part | Sheet |\n|---|---|---|---|\n")
            for n in sorted(orphaned, key=lambda n: n["members"][0]):
                d = designator_of(n)
                part = bom.get(d, {}).get("name", "?")
                f.write(f"| {n['name']} | {n['members'][0]} | {part} | {sheet_of(d)} |\n")
            f.write("\n")

        if pending_port:
            f.write("## Pending-port nets (named, single-pin, waiting on a far sheet -- expected)\n\n")
            f.write("| Net | Pin | Sheet |\n|---|---|---|\n")
            for n in pending_port:
                d = designator_of(n)
                f.write(f"| {n['name']} | {n['members'][0]} | {sheet_of(d)} |\n")
            f.write("\n")

        f.write("## All nets\n\n")
        f.write("| Net | Pins | Flags |\n|---|---|---|\n")
        for n in sorted(nets, key=lambda n: n["name"]):
            flags = []
            if len(n["members"]) == 1:
                flags.append("orphaned" if AUTO_NET_NAME_RE.match(n["name"]) else "pending-port")
            resolved = []
            for m in n["members"]:
                match = designator_re.match(m)
                if match:
                    d = match.group(1)
                    part = bom.get(d, {}).get("name", "?")
                    resolved.append(f"{m}({part}@{sheet_of(d)})")
                else:
                    resolved.append(m)
            f.write(f"| {n['name']} | {', '.join(resolved)} | {', '.join(flags) or '-'} |\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python cradle_sidecar/tools/netlist_parse.py <netlist.NET> <bom.csv> [output_prefix]")
        sys.exit(1)

    netlist_path, bom_path = sys.argv[1], sys.argv[2]
    prefix = sys.argv[3] if len(sys.argv) > 3 else str(Path(netlist_path).with_suffix(""))

    components, nets = parse_netlist(netlist_path)
    bom = parse_bom(bom_path)
    standard_parts = load_standard_parts()
    sheet_map = load_sheet_map()
    write_summary(netlist_path, components, bom, nets, prefix + ".netlist-summary.md", standard_parts, sheet_map)

    print(f"SOURCE FRESHNESS: {freshness_line(netlist_path, bom_path)}")
    print(f"Parsed {len(components)} components, {len(nets)} nets -> {prefix}.netlist-summary.md")
    if any(row.get("sheet") for row in bom.values()):
        print(f"Sheet resolution: active (cradle_sidecar/data/altium/sheet-map.md, {len(sheet_map)} sheets known).")
    else:
        print(f"Sheet resolution: BOM has no SheetNumber column -- add one in Altium's BOM template.")
