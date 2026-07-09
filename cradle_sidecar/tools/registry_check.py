"""
Mechanical net-registry validation — no interpretation of intent.

Parses cradle_sidecar/data/net-registry.md and checks each listed net name against the
current Altium Protel netlist export. Reports only structural facts:
whether the net name exists in the export, and how many pins are on it.

A missing net may mean stale export, an unconnected hierarchical port, or
a registry row that hasn't been wired yet — this script does not decide
which. See cradle_sidecar/co-design-workflow.md for that distinction.

Usage:
    python registry_check.py <net-registry.md> <netlist.NET>
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from netlist_parse import parse_netlist, freshness_line  # noqa: E402

REGISTRY_ROW_RE = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*$"
)


def parse_registry_rows(registry_path):
    rows = []
    for line in Path(registry_path).read_text(encoding="utf-8").split("\n"):
        m = REGISTRY_ROW_RE.match(line)
        if not m:
            continue
        net_name, driven, consumed, domain, pull, protocol, soc_pin, status = m.groups()
        rows.append({
            "net": net_name.strip(),
            "driven_from": driven.strip(),
            "consumed_by": consumed.strip(),
            "voltage_domain": domain.strip(),
            "pull_term": pull.strip(),
            "protocol": protocol.strip(),
            "soc_pin": soc_pin.strip(),
            "status": status.strip(),
        })
    return rows


def check_registry(registry_path, netlist_path):
    registry_rows = parse_registry_rows(registry_path)
    _, nets = parse_netlist(netlist_path)
    net_by_name = {n["name"]: n for n in nets}

    results = []
    for row in registry_rows:
        net = net_by_name.get(row["net"])
        if net is None:
            results.append({
                **row,
                "in_netlist": False,
                "member_count": 0,
                "single_member": False,
            })
        else:
            count = len(net["members"])
            results.append({
                **row,
                "in_netlist": True,
                "member_count": count,
                "single_member": count < 2,
            })
    return results


def format_report(results):
    lines = [
        "| Net | Registry status | In netlist? | Member count | Single-member? |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        in_nl = "yes" if r["in_netlist"] else "**NO**"
        single = "yes" if r["single_member"] else "no"
        if not r["in_netlist"]:
            single = "n/a"
        lines.append(
            f"| `{r['net']}` | {r['status']} | {in_nl} | {r['member_count']} | {single} |"
        )
    return "\n".join(lines)


def summarize(results):
    missing = [r for r in results if not r["in_netlist"]]
    single = [r for r in results if r["in_netlist"] and r["single_member"]]
    return len(results), len(missing), len(single)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python cradle_sidecar/tools/registry_check.py <net-registry.md> <netlist.NET>")
        sys.exit(1)

    registry_path, netlist_path = sys.argv[1:3]
    print(f"SOURCE FRESHNESS: {freshness_line(registry_path, netlist_path)}")
    print("Missing-net findings are indistinguishable from a stale export — re-export before trusting.\n")

    results = check_registry(registry_path, netlist_path)
    if not results:
        print(f"No registry rows parsed from {registry_path}.")
        sys.exit(1)

    print(format_report(results))
    total, missing, single = summarize(results)
    print(
        f"\n{total} registry row(s): "
        f"{total - missing} present in netlist, "
        f"{missing} missing, "
        f"{single} present but single-member only."
    )
