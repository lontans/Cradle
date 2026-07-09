"""
Read-only loaders for the cradle_sidecar web UI.

Does not write to data/, does not run AI, does not replace agent workflows.
Agents continue to use cradle_sidecar/tools/ directly; this module only
serves human-readable views of the same files.
"""

import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent.parent / "tools"
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from paths import (
    BOM_PATH,
    COMPONENTS_DIR,
    DATASHEETS_DIR,
    NETLIST_PATH,
    NET_REGISTRY_PATH,
    SCHEMATIC_STATUS_PATH,
    SHEET_MAP_PATH,
)
from netlist_parse import freshness_line, load_sheet_map, parse_bom
from registry_check import check_registry, summarize

# BOM sheet number -> schematic-status.md row number(s) (project-specific).
# Almost 1:1, except sheet 8: Altium has one "Cradle_Interfaces" sheet, but
# schematic-status.md tracks it as two rows (7=USB/HDMI, 8=FPC/Expansion) --
# a real gap found 2026-07-08 (single-row mapping silently hid row 8's notes
# from the UI whenever sheet 8 was viewed). List-valued so both rows show.
BOM_TO_SCHEMATIC_ROWS = {
    "1": [],
    "2": [1],
    "3": [2],
    "4": [3],
    "5": [4],
    "6": [5],
    "7": [6],
    "8": [7, 8],
    "9": [9],
}


def repo_root_from_here():
    """cradle_sidecar/app/ -> repo root."""
    return Path(__file__).resolve().parent.parent.parent


def parse_schematic_status():
    rows = {}
    for line in Path(SCHEMATIC_STATUS_PATH).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]*)\|\s*$", line)
        if not m:
            continue
        rows[int(m.group(1))] = {
            "num": int(m.group(1)),
            "name": m.group(2).strip(),
            "status": m.group(3).strip(),
            "notes": m.group(4).strip(),
        }
    return rows


def read_schematic_status_raw():
    return Path(SCHEMATIC_STATUS_PATH).read_text(encoding="utf-8")


def schematic_status_preamble():
    """Verbatim lines from docs/schematic-status.md before the status table."""
    lines = []
    for line in read_schematic_status_raw().splitlines():
        if line.strip().startswith("| #"):
            break
        lines.append(line)
    return "\n".join(lines).strip()


def net_registry_preamble():
    """Verbatim lines from net-registry.md before the registry table."""
    lines = []
    for line in Path(NET_REGISTRY_PATH).read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("| Net"):
            break
        if line.strip() and not line.startswith("# Net registry"):
            lines.append(line)
    return "\n".join(lines).strip()


def sheet_descriptor_markdown(bom_sheet):
    """Assembled from schematic-status.md row(s) + sheet-map — fields quoted, not
    paraphrased. A BOM sheet can map to more than one schematic-status row
    (sheet 8: Altium's one Interfaces sheet vs. schematic-status.md's two rows)
    -- render all of them, not just the first, or the rest silently disappear."""
    sheet_map = load_sheet_map(SHEET_MAP_PATH)
    schematic = parse_schematic_status()
    sch_rows = [schematic[n] for n in BOM_TO_SCHEMATIC_ROWS.get(str(bom_sheet), []) if n in schematic]
    altium = sheet_map.get(str(bom_sheet), "?")
    lines = ["*Source: `docs/schematic-status.md`, `cradle_sidecar/data/altium/sheet-map.md`*", ""]
    if sch_rows:
        title = " / ".join(s["name"] for s in sch_rows)
        lines.extend([f"## {title}", "", f"**Altium BOM `SheetNumber`:** {bom_sheet} — `{altium}`", ""])
        if len(sch_rows) > 1:
            lines.append(f"*Note: this Altium sheet covers {len(sch_rows)} schematic-status.md rows — shown separately below.*")
            lines.append("")
        for sch in sch_rows:
            lines.extend([
                f"### {sch['name']} (row {sch['num']})",
                "",
                f"**Status:** {sch['status']}",
                "",
                "**Notes (verbatim from schematic-status):**",
                "",
                sch["notes"],
                "",
            ])
    else:
        lines.extend([
            f"## BOM sheet {bom_sheet}",
            "",
            f"**Altium:** `{altium}`",
            "",
            "*(No row mapped in docs/schematic-status.md for this BOM sheet number.)*",
        ])
    return "\n".join(lines)


# Substrings that appear in net-registry.md driven_from / consumed_by cells (mechanical match only).
SHEET_CONTRACT_ALIASES = {
    "1": ["top-level", "Cradle (top-level"],
    "2": ["Charging", "Power_Charging"],
    "3": ["PMIC", "Power_PMIC", "RK806"],
    "4": ["Compute-SoC", "Compute_SOC", "SoC"],
    "5": ["Memory", "Compute_Memory", "LPDDR", "eMMC"],
    "6": ["Wireless", "AP6275S"],
    "7": ["Storage", "MicroSD"],
    "8": ["Interfaces", "USB", "HDMI", "FPC"],
    "9": ["Audio", "MAX98357", "MEMS"],
}


def _field_matches_aliases(text, aliases):
    low = text.lower()
    return any(a.lower() in low for a in aliases)


def sheet_contracts(bom_sheet, registry_rows):
    aliases = SHEET_CONTRACT_ALIASES.get(str(bom_sheet), [])
    sheet_map = load_sheet_map(SHEET_MAP_PATH)
    altium = sheet_map.get(str(bom_sheet), "")
    if altium and altium not in aliases:
        aliases = list(aliases) + [altium, altium.replace("Cradle_", "")]
    contracts = []
    for row in registry_rows:
        driven = row.get("driven_from", "")
        consumed = row.get("consumed_by", "")
        out = _field_matches_aliases(driven, aliases)
        inn = _field_matches_aliases(consumed, aliases)
        if not out and not inn:
            continue
        direction = []
        if out:
            direction.append("out")
        if inn:
            direction.append("in")
        contracts.append({**row, "direction": direction})
    return contracts


def sheet_detail(bom_sheet):
    card_index = load_card_index()
    parts = []
    for p in parts_on_sheet(bom_sheet):
        p = dict(p)
        p["card"] = card_index.get(p["designator"])
        p["datasheets"] = find_datasheet_assets(p["name"])
        parts.append(p)
    reg = registry_with_checks()
    sheets = list_sheets()
    meta = next((s for s in sheets if s["bom_sheet"] == str(bom_sheet)), {})
    return {
        "bom_sheet": str(bom_sheet),
        "meta": meta,
        "schematic_preamble_md": schematic_status_preamble(),
        "sheet_descriptor_md": sheet_descriptor_markdown(bom_sheet),
        "registry_preamble_md": net_registry_preamble(),
        "contracts": sheet_contracts(bom_sheet, reg["rows"]),
        "registry_summary": reg["summary"],
        "parts": parts,
    }


def list_sheets():
    """Summary row per BOM sheet for the nav list. Sheets mapping to more than
    one schematic-status.md row (see BOM_TO_SCHEMATIC_ROWS) get a combined
    name/status/notes here -- full per-row detail lives in
    sheet_descriptor_markdown(), not truncated here."""
    sheet_map = load_sheet_map(SHEET_MAP_PATH)
    schematic = parse_schematic_status()
    sheets = []
    for num in sorted(sheet_map, key=lambda x: int(x)):
        sch_rows = [schematic[n] for n in BOM_TO_SCHEMATIC_ROWS.get(num, []) if n in schematic]
        sheets.append({
            "bom_sheet": num,
            "altium_name": sheet_map[num],
            "design_name": " / ".join(s["name"] for s in sch_rows) if sch_rows else sheet_map[num],
            "status": " / ".join(s["status"] for s in sch_rows) if sch_rows else "",
            "notes": " || ".join(s["notes"] for s in sch_rows) if sch_rows else "",
        })
    return sheets


def parts_on_sheet(bom_sheet):
    bom = parse_bom(BOM_PATH)
    sheet_str = str(bom_sheet)
    parts = []
    for designator, info in sorted(bom.items()):
        s = info.get("sheet", "")
        if s == sheet_str:
            exact = True
        elif s.startswith("ambiguous(") and sheet_str in s:
            exact = False
        else:
            continue
        parts.append({
            "designator": designator,
            "name": info.get("name", ""),
            "description": info.get("description", ""),
            "sheet_resolution": "exact" if exact else "ambiguous",
        })
    return parts


def load_card_index():
    """designator -> {file, title, has_card}."""
    index = {}
    root = Path(COMPONENTS_DIR)
    if not root.exists():
        return index
    for path in sorted(root.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        title = path.stem
        if text.startswith("# "):
            title = text.split("\n", 1)[0][2:].strip()
        designator = None
        for line in text.splitlines():
            if line.strip().startswith("**Designator:**"):
                designator = line.split("**Designator:**", 1)[1].strip()
                break
        entry = {"file": path.name, "title": title}
        if designator:
            index[designator] = entry
    return index


def list_cards():
    cards = []
    root = Path(COMPONENTS_DIR)
    if not root.exists():
        return cards
    for path in sorted(root.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        title = path.stem
        designator = ""
        if text.startswith("# "):
            title = text.split("\n", 1)[0][2:].strip()
        for line in text.splitlines():
            if line.strip().startswith("**Designator:**"):
                designator = line.split("**Designator:**", 1)[1].strip()
                break
        cards.append({
            "file": path.name,
            "title": title,
            "designator": designator,
        })
    return cards


def read_card(filename):
    path = Path(COMPONENTS_DIR) / filename
    if not path.exists() or path.name.startswith("_"):
        return None
    return path.read_text(encoding="utf-8")


def parse_registry():
    rows = []
    text = Path(NET_REGISTRY_PATH).read_text(encoding="utf-8")
    row_re = re.compile(
        r"^\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*$"
    )
    for line in text.splitlines():
        m = row_re.match(line)
        if not m:
            continue
        rows.append({
            "net": m.group(1).strip(),
            "driven_from": m.group(2).strip(),
            "consumed_by": m.group(3).strip(),
            "soc_pin": m.group(7).strip(),
            "status": m.group(8).strip(),
        })
    return rows


def registry_with_checks():
    results = check_registry(NET_REGISTRY_PATH, NETLIST_PATH)
    total, missing, single = summarize(results)
    return {
        "summary": {
            "total": total,
            "present": total - missing,
            "missing": missing,
            "single_member": single,
        },
        "rows": results,
    }


def freshness():
    paths = [NETLIST_PATH, BOM_PATH, NET_REGISTRY_PATH]
    existing = [p for p in paths if Path(p).exists()]
    return freshness_line(*existing) if existing else "No export files found."


def find_datasheet_assets(part_name):
    """Best-effort match BOM part name to datasheet files in data/datasheets/."""
    if not part_name:
        return []
    root = Path(DATASHEETS_DIR)
    if not root.exists():
        return []
    key = part_name.upper().replace(" ", "")
    assets = []
    for path in sorted(root.iterdir()):
        if path.name.startswith("."):
            continue
        stem = path.stem.upper().replace(" ", "")
        if key in stem or stem.startswith(key[: min(8, len(key))]):
            assets.append({
                "name": path.name,
                "path": path.as_posix(),
                "kind": path.suffix.lower().lstrip("."),
            })
    return assets[:12]


def is_safe_open_path(repo_root, rel_path):
    """Only allow opening files under cradle_sidecar/data/."""
    try:
        full = (repo_root / rel_path).resolve()
        allowed = (repo_root / "cradle_sidecar" / "data").resolve()
        return full.is_file() and str(full).startswith(str(allowed))
    except (OSError, ValueError):
        return False
