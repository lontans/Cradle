# cradle_sidecar

Live co-design operational layer for the Cradle board project — component knowledge, netlist/BOM exports, and the tooling that keeps them checked against each other. Physically separate from [`../docs/`](../docs/) on purpose: `docs/` is published narrative for anyone reading this repo on GitHub, this directory is the working database agents and (eventually) a human-facing UI both read and write. See [`co-design-workflow.md`](co-design-workflow.md) for the full reasoning, history, and every lesson learned building this — including the migration into this directory itself.

## Cold start

```
python cradle_sidecar/tools/project_refresh.py
```

Run from the repo root. Re-parses the current Altium exports, lints every component card, checks open items and cross-part reachability, and validates the net registry — one consolidated status. Then use [`workflow-cheatsheet.md`](workflow-cheatsheet.md) for task-specific commands (researching a new part, checking wiring, etc.).

## What's in here

- **`co-design-workflow.md`** — the spec and full history: why each layer of tooling exists, what was tried and rejected, every bug found and fixed, and the reasoning behind every non-obvious decision (including this directory's own existence). Read once for context.
- **`workflow-cheatsheet.md`** — task-to-command lookup for day-to-day work. Read this one repeatedly, not `co-design-workflow.md`.
- **`data/`** — the live truth this tooling operates on:
  - `components/` — curated per-part knowledge cards. Copy `_TEMPLATE.md` for a new one.
  - `net-registry.md` — cross-sheet net tracking, hand-maintained, mechanically checked against the netlist.
  - `altium/` — periodically re-exported Altium netlist (`Netlist/Cradle.NET`) + BOM (`BOM/Cradle.csv`), plus derived data (`sheet-map.md`, `standard-parts.md`) and generated summaries. **Always check the `SOURCE FRESHNESS` line any tool prints before trusting a "missing/not wired" finding** — that's indistinguishable from a stale export otherwise.
  - `datasheets/` — vendor PDFs plus generated `.index.md`/`.tables.md`/`.outline.md`/`.quickstart.md` per part.
- **`tools/`** — every script (`datasheet_index.py`, `datasheet_quickstart.py`, `netlist_parse.py`, `wiring_check.py`, `card_lint.py`, `registry_check.py`, `project_refresh.py`). `paths.py` is the single source of truth for every path they use — if this directory ever moves again, that's the one file that needs to change.

## What's NOT in here (descoped for now)

A localhost web UI (`cradle_sidecar/app/`) reading this same `data/` directory was a real design intent — sheet-aware navigation, rendered cards, PDF deep-links, check badges — but is **explicitly descoped**, not merely deferred. Schematic work and the knowledge layer (`data/`, tooling, write-back) deliver value today; with one component card and Wireless in progress, a UI would be a shell over sparse data. Revisit when Compute-SoC starts or daily cross-sheet navigation pain justifies it. See `co-design-workflow.md` for full reasoning.

## The one rule that makes any of this worth maintaining

Every script here only narrows where to look — none of them reason about what a signal does for Cradle specifically. That reasoning is still a human/Claude-in-conversation task every time, and the system only stays valuable if the outcome gets written back into `data/` as part of finishing the task, not left to live only in chat history.
