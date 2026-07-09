# Cradle

Compute platform integrating the RK3576 SoC — a credit-card sized (85mm x 54mm), battery-native edge AI board for voice AI, robotics, and wearable applications. See [Claude/cradle_context_brief.txt](Claude/cradle_context_brief.txt) for the full original design brief.

## Repo layout

`docs/` and [`cradle_sidecar/`](cradle_sidecar/) are physically separated on purpose (moved 2026-07-08 — see `cradle_sidecar/co-design-workflow.md` for the full reasoning and migration history): `docs/` is published narrative for anyone reading this repo, `cradle_sidecar/` is the live co-design operational layer — component knowledge, netlist/BOM exports, and the tooling that reads/writes them. Same split already proven at a smaller scale by `hardware/` (the eventual Altium project) vs. `cradle_sidecar/data/altium/` (frequent lightweight exports) — see `hardware/README.md`.

**`docs/` — published, human-owned narrative, never machine-written:**
- [`docs/architecture.md`](docs/architecture.md) — locked architecture (compute, power, wireless, interfaces, audio, PCB design, software target)
- [`docs/decisions-log.md`](docs/decisions-log.md) — engineering decisions with rationale, and corrections caught during design sessions
- [`docs/bom.md`](docs/bom.md) — bill of materials, living document (hand-edited; not currently generated from anything)
- [`docs/schematic-status.md`](docs/schematic-status.md) — sheet-by-sheet Altium schematic progress

**[`cradle_sidecar/`](cradle_sidecar/) — live co-design state + tooling, operational, agent-facing:**
- [`cradle_sidecar/workflow-cheatsheet.md`](cradle_sidecar/workflow-cheatsheet.md) — **start here if you're an agent picking up this repo cold**: run `python cradle_sidecar/tools/project_refresh.py` first, then use this for task-specific commands
- [`cradle_sidecar/co-design-workflow.md`](cradle_sidecar/co-design-workflow.md) — why the tooling system exists, what's been tried and rejected, full bug/lesson history, including the sidecar migration itself. **Status: partially built** — Layers 0–0.9 (datasheet index, netlist parse, wiring check, `project_refresh`, `card_lint`, `registry_check`) are real and tested; [`cradle_sidecar/data/net-registry.md`](cradle_sidecar/data/net-registry.md) is seeded (Wireless cross-sheet nets only); Layer 2 sheet contracts are still proposed, not built
- `cradle_sidecar/data/` — the actual live data: `net-registry.md` (cross-sheet nets), `components/` (curated per-part knowledge cards — copy `_TEMPLATE.md` for new ones; only one real card so far, `AP6275S.md`, built incrementally as design work touches each part), `altium/` (live netlist/BOM exports + derived data), `datasheets/` (vendor PDFs + generated `.index`/`.tables`/`.outline`/`.quickstart` per part)
- `cradle_sidecar/tools/` — every script above; `paths.py` centralizes every path they use, specifically so a future reorg (or this one) is a one-file change, not a many-file one
- `cradle_sidecar/app/` — **v0 localhost co-design UI** (`python cradle_sidecar/app/server.py` → http://127.0.0.1:8765/). Read-only views + refresh on click; agents still use CLI tools for everything else

**Repo-wide, not part of either group:**
- [`CHANGELOG.md`](CHANGELOG.md) — running dated log of what changed, across hardware and firmware
- [`hardware/`](hardware/README.md) — Altium project, fab outputs (once checked in)
- [`firmware/`](firmware/README.md) — bring-up and software work, with its own [firmware/LOG.md](firmware/LOG.md)

## Status

Schematic: Sheet 1 (Power — Charging) complete, Sheet 2 (Power — PMIC) in progress. See [docs/schematic-status.md](docs/schematic-status.md) for the full sheet list. Firmware work has not started.
