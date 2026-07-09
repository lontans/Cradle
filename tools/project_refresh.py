"""
One-command refresh: re-runs the existing analysis scripts against the
current Altium exports and every component card, and prints a consolidated
status. Doesn't replace reading the individual outputs -- it's the "what
should I look at first" entry point, not a substitute for them.

What it does NOT do, on purpose: doesn't call datasheet_index.py or
datasheet_quickstart.py (those are per-new-datasheet tools, not part of a
routine refresh loop -- rerunning them on every refresh would burn time
reprocessing PDFs that haven't changed). Doesn't write anything back into
component cards or the net registry -- that's still a human/Claude-reads-
the-output-and-decides step, same discipline as everywhere else in this
project. This script only aggregates what's already checkable
mechanically.

Usage:
    python project_refresh.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from netlist_parse import (  # noqa: E402
    parse_netlist, parse_bom, load_standard_parts, load_sheet_map,
    write_summary, freshness_line, classify_floating_nets,
)
from wiring_check import check_open_items, check_wiring  # noqa: E402
from card_lint import lint_card  # noqa: E402
from registry_check import check_registry, summarize  # noqa: E402

NETLIST_PATH = "docs/Altium/Netlist/Cradle.NET"
BOM_PATH = "docs/Altium/BOM/Cradle.csv"
NETLIST_PREFIX = "docs/Altium/Cradle"
REGISTRY_PATH = "docs/net-registry.md"
COMPONENTS_DIR = "docs/components"


def find_designator(card_path):
    text = Path(card_path).read_text(encoding="utf-8")
    for line in text.split("\n"):
        if line.strip().startswith("**Designator:**"):
            return line.split("**Designator:**")[1].strip()
    return None


def find_wiring_targets(card_path):
    """Parse '**Wiring targets:** U1/RK3576, U9/MAX98357' from card header."""
    targets = []
    for line in Path(card_path).read_text(encoding="utf-8").split("\n"):
        if not line.strip().startswith("**Wiring targets:**"):
            continue
        value = line.split("**Wiring targets:**", 1)[1].strip()
        if not value or value.startswith("<"):
            return []
        for part in value.split(","):
            part = part.strip()
            if "/" not in part:
                continue
            designator, name = part.split("/", 1)
            targets.append((designator.strip(), name.strip()))
        return targets
    return []


def is_component_card(path):
    return path.name.endswith(".md") and not path.name.startswith("_")


def main():
    print("=" * 70)
    print("PROJECT REFRESH")
    print("=" * 70)

    if not Path(NETLIST_PATH).exists() or not Path(BOM_PATH).exists():
        print(f"Missing {NETLIST_PATH} or {BOM_PATH} -- nothing to refresh.")
        return

    print(f"\nSOURCE FRESHNESS: {freshness_line(NETLIST_PATH, BOM_PATH)}")
    print("(If this looks old relative to your last Altium session, re-export before trusting anything below.)")

    components, nets = parse_netlist(NETLIST_PATH)
    bom = parse_bom(BOM_PATH)
    standard_parts = load_standard_parts()
    sheet_map = load_sheet_map()
    write_summary(NETLIST_PATH, components, bom, nets, NETLIST_PREFIX + ".netlist-summary.md", standard_parts, sheet_map)

    orphaned, staged, pending_port = classify_floating_nets(nets, standard_parts)
    print(f"\nNetlist: {len(components)} components, {len(nets)} nets -> {NETLIST_PREFIX}.netlist-summary.md")
    print(f"  {len(orphaned)} orphaned pins worth reviewing (excludes {len(staged)} on known staged parts, {len(pending_port)} pending-port nets)")

    if Path(REGISTRY_PATH).exists():
        print(f"\n{'-' * 70}")
        print("NET REGISTRY")
        print(f"{'-' * 70}")
        registry_results = check_registry(REGISTRY_PATH, NETLIST_PATH)
        total, missing, single = summarize(registry_results)
        print(f"  {total} row(s): {total - missing} present in netlist, {missing} missing, {single} single-member only")
        if missing:
            missing_nets = [r["net"] for r in registry_results if not r["in_netlist"]]
            print(f"  Missing: {', '.join(missing_nets)}")
        print(f"  -> run `python tools/registry_check.py {REGISTRY_PATH} {NETLIST_PATH}` for full table")
    else:
        print(f"\nNet registry: {REGISTRY_PATH} not found -- skipping.")

    print(f"\n{'-' * 70}")
    print("COMPONENT CARDS")
    print(f"{'-' * 70}")

    card_paths = sorted(
        p for p in Path(COMPONENTS_DIR).glob("*.md")
        if is_component_card(p)
    ) if Path(COMPONENTS_DIR).exists() else []
    if not card_paths:
        print(f"No cards found in {COMPONENTS_DIR}/.")

    for card_path in card_paths:
        card_str = str(card_path)
        print(f"\n{card_path.name}:")

        lint_findings = lint_card(card_str)
        if lint_findings:
            print(f"  LINT: {len(lint_findings)} finding(s) -- run `python tools/card_lint.py {card_str}` for detail")
        else:
            print("  LINT: clean")

        designator = find_designator(card_str)
        if not designator:
            print("  No Designator field -- skipping wiring checks (card_lint should have flagged this).")
            continue

        try:
            open_results = check_open_items(card_str, designator, NETLIST_PATH)
        except Exception as e:
            print(f"  Could not run open-items check: {e}")
            open_results = []

        still_open = [r for r in open_results if not r["has_net"]]
        if open_results:
            print(f"  OPEN ITEMS: {len(still_open)} of {len(open_results)} non-Decided pins still have no real connection")
            print(f"    -> run `python tools/wiring_check.py --open {card_str} {designator} {NETLIST_PATH}` for the full list")
        else:
            print("  OPEN ITEMS: none (every pin is marked Decided)")

        targets = find_wiring_targets(card_str)
        if not targets:
            print("  REACHABILITY: skipped (no **Wiring targets:** line)")
            continue

        for target_designator, target_name in targets:
            try:
                reach_results = check_wiring(
                    card_str, designator, target_designator, target_name, NETLIST_PATH
                )
            except Exception as e:
                print(f"  REACHABILITY ({target_name}): could not run -- {e}")
                continue

            unwired = [r for r in reach_results if not r["has_net"]]
            not_reaching = [r for r in reach_results if r["has_net"] and not r["reaches_target"]]
            print(
                f"  REACHABILITY ({target_name}/{target_designator}): "
                f"{len(unwired)} not wired on {designator}; "
                f"{len(not_reaching)} wired on {designator} but not reaching {target_designator} yet"
            )
            if unwired or not_reaching:
                print(
                    f"    -> run `python tools/wiring_check.py {card_str} {designator} "
                    f"{target_designator} {target_name} {NETLIST_PATH}` for the full list"
                )

    print(f"\n{'-' * 70}")
    print("Done. Re-export netlist/BOM from Altium if SOURCE FRESHNESS looks stale.")
    print(f"{'-' * 70}")


if __name__ == "__main__":
    main()
