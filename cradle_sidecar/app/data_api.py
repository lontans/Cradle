"""
Loaders (and a small set of writers) for the cradle_sidecar web UI.

Mostly read-only views of the same files agents use directly via
cradle_sidecar/tools/. The one write path is component cards
(write_card) -- the manual-card-authoring flow for parts whose datasheet
is missing or unusable for automated extraction. Does not run AI, does
not replace agent workflows.
"""

import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent.parent / "tools"
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from paths import (
    ARCHITECTURE_PATH,
    BOM_PATH,
    COMPONENTS_DIR,
    DATASHEETS_DIR,
    NETLIST_PATH,
    NET_REGISTRY_PATH,
    SCHEMATIC_STATUS_PATH,
    SHEET_MAP_PATH,
)
from card_lint import iter_pin_rows, lint_text
from card_note import VALID_TAGS, append_note
from netlist_parse import freshness_line, load_sheet_map, parse_bom, parse_netlist
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


def architecture_vision_md():
    """Verbatim contents of docs/architecture.md -- pulled in as-is, no
    summarizing or rephrasing, so this is a read-through of the one
    published source rather than a second copy that can drift from it.
    Only surfaced on sheet 1 (the top-level/block-diagram sheet), since
    that's the project-overview vantage point this doc is written for."""
    path = Path(ARCHITECTURE_PATH)
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


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
        "vision_md": architecture_vision_md() if str(bom_sheet) == "1" else None,
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


VALID_CARD_ORIGINS = ("Datasheet-derived", "Manually authored", "Mixed")


def parse_card_meta(path, text):
    """Shared header-field extraction so every card list/index agrees on the
    same reading of title/designator/origin instead of three copies drifting."""
    title = path.stem
    if text.startswith("# "):
        title = text.split("\n", 1)[0][2:].strip()
    designator = ""
    origin = ""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("**Designator:**") and not designator:
            designator = stripped.split("**Designator:**", 1)[1].strip()
        elif stripped.startswith("**Card origin:**") and not origin:
            origin = stripped.split("**Card origin:**", 1)[1].strip()
    return {"file": path.name, "title": title, "designator": designator, "origin": origin}


def load_card_index():
    """designator -> {file, title, origin}."""
    index = {}
    root = Path(COMPONENTS_DIR)
    if not root.exists():
        return index
    for path in sorted(root.glob("*.md")):
        if path.name.startswith("_"):
            continue
        meta = parse_card_meta(path, path.read_text(encoding="utf-8"))
        if meta["designator"]:
            index[meta["designator"]] = {"file": meta["file"], "title": meta["title"], "origin": meta["origin"]}
    return index


def list_cards():
    """Every card, plus whether its designator still resolves in the current
    BOM (an unresolved designator usually means a designator got renumbered
    in Altium after the card was written, or the card was authored ahead of
    schematic entry -- either way, worth surfacing rather than hiding)."""
    cards = []
    root = Path(COMPONENTS_DIR)
    if not root.exists():
        return cards
    bom = parse_bom(BOM_PATH) if Path(BOM_PATH).exists() else {}
    for path in sorted(root.glob("*.md")):
        if path.name.startswith("_"):
            continue
        meta = parse_card_meta(path, path.read_text(encoding="utf-8"))
        meta["designator_in_bom"] = bool(meta["designator"]) and meta["designator"] in bom
        cards.append(meta)
    return cards


def read_card(filename):
    path = Path(COMPONENTS_DIR) / filename
    if not path.exists() or path.name.startswith("_"):
        return None
    return path.read_text(encoding="utf-8")


def read_template():
    path = Path(COMPONENTS_DIR) / "_TEMPLATE.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def is_safe_card_filename(name):
    """New/edited card names stay a single markdown file directly inside
    COMPONENTS_DIR -- no path traversal, no overwriting the template."""
    if not name or "/" in name or "\\" in name or ".." in name:
        return False
    if not name.endswith(".md") or name.startswith("_"):
        return False
    return name == Path(name).name


def write_card(filename, content, overwrite):
    """Create or update a component card. Refuses to clobber an existing
    file unless overwrite=True, so a typo'd "new card" name can't silently
    erase another part's card -- the editor UI only sets overwrite=True when
    the user opened that exact file to edit it."""
    if not is_safe_card_filename(filename):
        return {"ok": False, "error": "invalid card filename"}
    root = Path(COMPONENTS_DIR)
    root.mkdir(parents=True, exist_ok=True)
    path = root / filename
    if path.exists() and not overwrite:
        return {"ok": False, "error": "card already exists"}
    path.write_text(content, encoding="utf-8")
    return {"ok": True, "file": filename}


def lint_card_text(text):
    """Same check as tools/card_lint.py, run on in-memory draft text so the
    editor UI can lint before saving -- not just after."""
    return [{"kind": kind, "line": line, "message": msg} for kind, line, msg in lint_text(text)]


def add_card_note(filename, text, tag, source=None, page=None):
    """The mechanical write-back half of card_note.py's split: an agent (or
    the UI) supplies already-reasoned text plus a provenance tag, this
    function guarantees the on-disk formatting is identical regardless of
    who called it or how carefully. Only operates on a card that already
    exists -- a note has nowhere to attach on a file that isn't there yet."""
    if not is_safe_card_filename(filename):
        return {"ok": False, "error": "invalid card filename"}
    path = Path(COMPONENTS_DIR) / filename
    if not path.exists():
        return {"ok": False, "error": "card does not exist"}
    if tag not in VALID_TAGS:
        return {"ok": False, "error": f"tag must be one of {VALID_TAGS}"}
    try:
        new_text = append_note(path.read_text(encoding="utf-8"), text, tag, source, page)
    except ValueError as e:
        return {"ok": False, "error": str(e)}
    path.write_text(new_text, encoding="utf-8")
    return {"ok": True, "file": filename, "markdown": new_text}


DATASHEET_MIME = {".pdf": "application/pdf"}


def read_datasheet(name):
    """Raw bytes + mimetype for inline embedding (an <iframe>/<embed> needs
    the real file streamed with the right Content-Type, not a JSON wrapper).
    Basename only, same traversal-safety shape as is_safe_card_filename."""
    if not name or "/" in name or "\\" in name or ".." in name:
        return None
    path = Path(DATASHEETS_DIR) / name
    if not path.is_file():
        return None
    mime = DATASHEET_MIME.get(path.suffix.lower())
    if not mime:
        return None
    return {"bytes": path.read_bytes(), "mime": mime}


def extract_datasheet_name(card_markdown):
    """Pulls the primary datasheet's basename directly out of a card's own
    **Datasheet:** header line -- self-contained (works whether the card
    came from a sheet's BOM-matched part or the standalone Cards view,
    unlike find_datasheet_assets() which needs a BOM part name to match
    against). Returns None if the line is missing or doesn't point at a PDF."""
    m = re.search(r"\*\*Datasheet:\*\*\s*`([^`]+\.pdf)`", card_markdown, re.IGNORECASE)
    if not m:
        return None
    return Path(m.group(1)).name


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


def aggregate_pin_status():
    """Walks every component card's pin table and tallies the Status
    column -- reuses card_lint.py's iter_pin_rows() (the exact row shape
    the lint already trusts) so this can never disagree with what the
    lint itself considers a valid row."""
    counts = {"Decided": 0, "Open": 0, "Not addressed": 0, "other": 0}
    root = Path(COMPONENTS_DIR)
    if not root.exists():
        return counts
    for path in root.glob("*.md"):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        for _, m in iter_pin_rows(text):
            status = m.group(6).strip()
            if status.startswith("Decided"):
                counts["Decided"] += 1
            elif status.startswith("Open"):
                counts["Open"] += 1
            elif status.startswith("Not addressed"):
                counts["Not addressed"] += 1
            else:
                counts["other"] += 1
    return counts


def homepage_stats():
    """Deterministic counts for the sidecar's home page -- every number
    here is computed fresh from the same real files project_refresh.py
    reads (BOM, netlist, component cards, datasheets/, net-registry.md),
    never cached or randomized. Recomputed on every /api/home call, so
    clicking Run project refresh and returning to Home always shows
    current numbers, same discipline as everything else in this module."""
    bom = parse_bom(BOM_PATH) if Path(BOM_PATH).exists() else {}
    components, nets = ({}, {})
    if Path(NETLIST_PATH).exists():
        components, nets = parse_netlist(NETLIST_PATH)
    datasheets_root = Path(DATASHEETS_DIR)
    datasheet_count = len(list(datasheets_root.glob("*.pdf"))) if datasheets_root.exists() else 0
    return {
        "bom_designators": len(bom),
        "netlist_components": len(components),
        "net_count": len(nets),
        "sheet_count": len(list_sheets()),
        "card_count": len(list_cards()),
        "datasheet_count": datasheet_count,
        "pin_status": aggregate_pin_status(),
        "registry_summary": registry_with_checks()["summary"],
        "freshness": freshness(),
    }


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


OPENABLE_SUFFIXES = (".md", ".pdf")


def is_safe_open_path(repo_root, rel_path):
    """Backs both the datasheet "open" buttons and clicking a markdown link
    inside rendered card/doc content (e.g. `[decisions-log.md](decisions-log.md)`
    in docs/architecture.md) -- those links point all over the repo
    (docs/, cradle_sidecar/data/, top-level CHANGELOG.md), not just
    cradle_sidecar/data/, so this isn't scoped to one subdirectory. This
    only ever triggers os.startfile() locally -- it never serves the
    file's bytes over HTTP -- so the actual risk to guard against is path
    traversal outside the repo, not which subdirectory inside it."""
    try:
        full = (repo_root / rel_path).resolve()
        repo_root = repo_root.resolve()
        if full != repo_root and repo_root not in full.parents:
            return False
        return full.is_file() and full.suffix.lower() in OPENABLE_SUFFIXES
    except (OSError, ValueError):
        return False
