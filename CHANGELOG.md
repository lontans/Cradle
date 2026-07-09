# Changelog

Running log of what changed and when. Short dated bullets — for the reasoning behind a change, link to the relevant doc ([docs/architecture.md](docs/architecture.md), [docs/decisions-log.md](docs/decisions-log.md), [docs/bom.md](docs/bom.md), [docs/schematic-status.md](docs/schematic-status.md), [firmware/LOG.md](firmware/LOG.md)) rather than restating it here.

## 2026-07-07
- Sheet 5 (Wireless): resolved AP6275S external wiring gaps not covered by AMPAK's datasheet — internal buck regulator pins (`CBUCK_0P9`/`CSR_VLX`, `ASR_VLX`/`ABUCK_1P12`) need external 4.7uH inductor + 4.7uF cap loops; confirmed no SDIO pull-up resistors needed for a soldered point-to-point design; confirmed `SDIO_VSEL` (pin 24) is no-connect. Sourced from a real production schematic (Geniatech CBD-3588) wiring the same module over SDIO — see decisions-log.md

## 2026-07-05
- Repo scaffolding populated: `docs/` (architecture, decisions log, BOM, schematic status), `hardware/` and `firmware/` placeholders
- Content migrated from `cradle_context_brief.txt` into structured docs; brief kept as-is for raw reference
- Schematic status at time of writing: Sheet 1 (Power — Charging) complete, Sheet 2 (Power — PMIC) in progress (buck stages done, LDO/PWRON/RESET_OUT/I2C pending)
- No firmware work started yet
- Sheet 9 (Audio) and Sheet 5 (Wireless) moved to in progress: MAX98357A channel/gain config and mono speaker output settled, PDM mic stereo clocking (MIC1/MIC2, rising/falling edge) settled, AP6275S antenna (2.4GHz-only) and both external clock parts (37.4MHz crystal, 32.768kHz MEMS oscillator) selected — see decisions-log.md for the run of entries dated today
