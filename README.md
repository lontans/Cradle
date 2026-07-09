# Cradle

Compute platform integrating the RK3576 SoC — a credit-card sized (85mm x 54mm), battery-native edge AI board for voice AI, robotics, and wearable applications. See [Claude/cradle_context_brief.txt](Claude/cradle_context_brief.txt) for the full original design brief.

## Repo layout

- [`docs/architecture.md`](docs/architecture.md) — locked architecture (compute, power, wireless, interfaces, audio, PCB design, software target)
- [`docs/decisions-log.md`](docs/decisions-log.md) — engineering decisions with rationale, and corrections caught during design sessions
- [`docs/bom.md`](docs/bom.md) — bill of materials, living document
- [`docs/schematic-status.md`](docs/schematic-status.md) — sheet-by-sheet Altium schematic progress
- [`docs/workflow-cheatsheet.md`](docs/workflow-cheatsheet.md) — **start here if you're an agent picking up this repo cold**: run `python tools/project_refresh.py` first, then use this for task-specific commands
- [`docs/co-design-workflow.md`](docs/co-design-workflow.md) — why the tooling system exists, what's been tried and rejected, full bug/lesson history. **Status: partially built** — Layers 0–0.9 (datasheet index, netlist parse, wiring check, `project_refresh`, `card_lint`, `registry_check`) are real and tested; [`docs/net-registry.md`](docs/net-registry.md) is seeded (Wireless cross-sheet nets only); Layer 2 sheet contracts are still proposed, not built
- [`docs/net-registry.md`](docs/net-registry.md) — cross-sheet net table (Layer 3); hand-maintained, mechanically checked against netlist exports via `tools/registry_check.py`
- [`docs/components/`](docs/components/) — curated per-part knowledge cards (pinout + Cradle-specific wiring decisions). Copy [`docs/components/_TEMPLATE.md`](docs/components/_TEMPLATE.md) for new cards. Only one real card so far (`AP6275S.md`) — built incrementally as design work touches each part, not upfront for the whole BOM
- [`docs/Altium/`](docs/Altium/) — live netlist/BOM exports and derived data (sheet map, standard-parts list) feeding the `tools/` scripts. **Not the same thing as `hardware/`** — see `hardware/README.md` for the distinction
- [`CHANGELOG.md`](CHANGELOG.md) — running dated log of what changed, across hardware and firmware
- [`hardware/`](hardware/README.md) — Altium project, fab outputs (once checked in)
- [`firmware/`](firmware/README.md) — bring-up and software work, with its own [firmware/LOG.md](firmware/LOG.md)

## Status

Schematic: Sheet 1 (Power — Charging) complete, Sheet 2 (Power — PMIC) in progress. See [docs/schematic-status.md](docs/schematic-status.md) for the full sheet list. Firmware work has not started.
