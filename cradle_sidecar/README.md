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

## Sidecar web UI (v0)

Co-design companion while you work in Altium — read-only views of `data/`, plus **Run project refresh** (same as `cradle_sidecar/tools/project_refresh.py`). Does not edit cards, run AI, or replace the agent workflow.

```
python cradle_sidecar/app/server.py
```

Open http://127.0.0.1:8765/ (override port with `CRADLE_SIDECAR_PORT`). Sheet → parts → component card + open datasheet PDF. Net registry with mechanical check status. Agents still use CLI tools and update markdown directly.

## What's NOT in the UI yet

Altium sheet auto-sync, in-browser card/registry editing, `update_github_docs` publish. v0 is navigate, interpret, open PDFs, and refresh on demand.

## The one rule

Every script here only narrows where to look — none of them reason about what a signal does for Cradle specifically. That reasoning is still a human/Claude-in-conversation task every time, and the system only stays valuable if the outcome gets written back into `data/` as part of finishing the task, not left to live only in chat history.
