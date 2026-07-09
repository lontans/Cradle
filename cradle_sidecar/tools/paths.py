"""
Single source of truth for every filesystem path this tooling touches.

Every script imports path constants from here instead of hardcoding path
strings directly. This is the module that made the 2026-07-08 physical move
into cradle_sidecar/ a one-file edit instead of a many-file find-and-replace
across every script -- see cradle_sidecar/co-design-workflow.md for the full
history (the sidecar proposal, why it was deferred, then adopted once the
migration was explicitly requested).

Paths are relative to the repo root. Every script in this project is
invoked from the repo root by convention (see
cradle_sidecar/workflow-cheatsheet.md, e.g.
`python cradle_sidecar/tools/project_refresh.py`) -- these constants match
that convention rather than trying to be independently robust to being
invoked from elsewhere.
"""

# --- Altium exports (live, periodically re-exported from the running project) ---
NETLIST_PATH = "cradle_sidecar/data/altium/Netlist/Cradle.NET"
BOM_PATH = "cradle_sidecar/data/altium/BOM/Cradle.csv"
NETLIST_SUMMARY_PREFIX = "cradle_sidecar/data/altium/Cradle"
SHEET_MAP_PATH = "cradle_sidecar/data/altium/sheet-map.md"
STANDARD_PARTS_PATH = "cradle_sidecar/data/altium/standard-parts.md"

# --- Live co-design knowledge (component cards, cross-sheet net tracking) ---
COMPONENTS_DIR = "cradle_sidecar/data/components"
NET_REGISTRY_PATH = "cradle_sidecar/data/net-registry.md"

# --- Vendor datasheets + generated per-part output (.index/.tables/.outline/.quickstart) ---
DATASHEETS_DIR = "cradle_sidecar/data/datasheets"

# --- Agent/operator manuals ---
WORKFLOW_CHEATSHEET_PATH = "cradle_sidecar/workflow-cheatsheet.md"
CODESIGN_WORKFLOW_PATH = "cradle_sidecar/co-design-workflow.md"

# --- Published narrative docs -- never machine-written, stay in docs/, listed
#     here only for completeness/cross-reference, not because tooling writes to them ---
ARCHITECTURE_PATH = "docs/architecture.md"
DECISIONS_LOG_PATH = "docs/decisions-log.md"
BOM_DOC_PATH = "docs/bom.md"
SCHEMATIC_STATUS_PATH = "docs/schematic-status.md"
