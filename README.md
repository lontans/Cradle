# Cradle

Compute platform integrating the RK3576 SoC — a credit-card sized (85mm x 54mm), battery-native edge AI board for voice AI, robotics, and wearable applications. See [Claude/cradle_context_brief.txt](Claude/cradle_context_brief.txt) for the full original design brief.

## Repo layout

- [`docs/architecture.md`](docs/architecture.md) — locked architecture (compute, power, wireless, interfaces, audio, PCB design, software target)
- [`docs/decisions-log.md`](docs/decisions-log.md) — engineering decisions with rationale, and corrections caught during design sessions
- [`docs/bom.md`](docs/bom.md) — bill of materials, living document
- [`docs/schematic-status.md`](docs/schematic-status.md) — sheet-by-sheet Altium schematic progress
- [`CHANGELOG.md`](CHANGELOG.md) — running dated log of what changed, across hardware and firmware
- [`hardware/`](hardware/README.md) — Altium project, fab outputs (once checked in)
- [`firmware/`](firmware/README.md) — bring-up and software work, with its own [firmware/LOG.md](firmware/LOG.md)

## Status

Schematic: Sheet 1 (Power — Charging) complete, Sheet 2 (Power — PMIC) in progress. See [docs/schematic-status.md](docs/schematic-status.md) for the full sheet list. Firmware work has not started.
