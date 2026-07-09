# TF-01A — MicroSD (TF card) push-push connector

**Designator:** Card1

**Wiring targets:** U1/RK3576

**Vendor:** (LCSC/generic, C91145) **Datasheet:** `cradle_sidecar/data/datasheets/TF-01A Datasheet.pdf` — **1-page scanned image, no extractable text layer** `[VERIFIED — pulled raw PDF text via PyMuPDF 2026-07-09, returned empty string]`. `datasheet_index.py`/`datasheet_quickstart.py` both found zero structure for this reason — not a tool bug, the source PDF has nothing machine-readable in it. Pinout below is `[UNVERIFIED — user's visual read of the datasheet 2026-07-09]`, not independently confirmed against source text.

## High-level summary

- Standard 8-contact microSD card interface (SD-mode signal names; the datasheet also lists SPI-mode alternate names, unused here) plus a separate mechanical card-detect switch pin and shield/ground tabs.
- Cradle uses SD-mode wiring (matches the SDIO/SD-mode approach already used on the Wireless sheet), not SPI mode.
- **Two different "CD" signals exist on this part — do not conflate them:** pin 2 (`DAT3`/`CD`) is the SD-protocol electrical presence-detect built into the data bus; pin 9 (`CD`) is a bare mechanical switch contact, entirely separate from the SD bus, that closes when a card is physically inserted.

## Power domains

| Domain | Pin(s) | Range | Cradle rail |
|---|---|---|---|
| `VDD` | 4 | 2.7–3.6V (typ 3.3V, standard SD default bus voltage) | `STORAGE_3V3` |
| `VSS` | 6, 10-13 (shield/shell) | Ground | GND plane |

## Pin table

| # | Name | Type | Vendor function | Cradle wiring | Status |
|---|---|---|---|---|---|
| 1 | `DAT2` | I/O | SD data line 2 (4-bit mode only) | RK3576 SDMMC controller + 30kOhm pull-up (R48) to `STORAGE_3V3` | Decided (2026-07-09) |
| 2 | `DAT3`/`CD` | I/O | SD data line 3, also card's own electrical presence-detect (internal pull-up in the card per SD spec) | RK3576 SDMMC controller + 30kOhm pull-up (R49) to `STORAGE_3V3` | Decided (2026-07-09) |
| 3 | `CMD` | I/O | Command line, host<->card | RK3576 SDMMC controller + 30kOhm pull-up (R45) to `STORAGE_3V3` | Decided (2026-07-09) |
| 4 | `VDD` | P | Card power | `STORAGE_3V3` rail, local decoupling (C91, C92) | Decided |
| 5 | `CLK` | I | Clock, host-driven | RK3576 SDMMC controller, no pull-up (actively driven) | Decided |
| 6 | `VSS` | — | Ground | GND plane | Decided |
| 7 | `DAT0` | I/O | SD data line 0 (used in 1-bit and 4-bit mode) | RK3576 SDMMC controller + 30kOhm pull-up (R46) to `STORAGE_3V3` | Decided |
| 8 | `DAT1` | I/O | SD data line 1 (4-bit mode only) | RK3576 SDMMC controller + 30kOhm pull-up (R47) to `STORAGE_3V3` | Decided |
| 9 | `CD` | — | Mechanical card-detect switch (physical contact, not part of SD bus) | RK3576 GPIO input + 30kOhm pull-up (R50) to `STORAGE_3V3` — **voltage domain not yet checked, see Known Gaps** | Open |
| 10-13 | `GND` | — | Shield/shell ground tabs | GND plane | Decided |

## Known gaps (things the vendor datasheet does not specify)

- Datasheet PDF has no extractable text at all (single page, empty text layer) — pinout above came from the user's own visual read, not a tool-verified source. Worth re-sourcing a text-based version of this datasheet if one exists (e.g. from LCSC/JLCPCB part page) rather than relying on the image.
- **Real open risk, not yet resolved:** pin 9's mechanical card-detect switch pull-up is wired to `STORAGE_3V3` (3.3V) along with the rest of the SD bus. The SD bus pull-ups being 3.3V is correct (standard SD default bus voltage). But pin 9 goes to a plain RK3576 GPIO, not an SD-protocol pin — if that GPIO lands on a 1.8V-only bank (RK3576 has multiple IO voltage domains across its GPIO banks), a 3.3V pull-up would overvoltage it. Not checkable yet since Compute-SoC pin assignment hasn't happened — **flag this specifically when the SoC sheet picks a GPIO for pin 9**, don't let it default through silently.
- Pull-up value (30kOhm, matching the Wireless-sheet SDIO convention) hasn't been checked against RK3576's own SDMMC controller spec — carried over by convention, not derived from the RK3576 TRM.

## External validation (secondary sources, not the primary datasheet)

- None yet — standard SD-mode microSD pinout conventions used to interpret the user's visual read, not a specific third-party schematic.

## Net name map (card name -> real Altium net name)

| Card name (vendor pin name) | Pin | Real Altium net name |
|---|---|---|
| `VDD` | 4 | `STORAGE_3V3` |
| `CMD` | 3 | `STORAGE_CMD_7` |
| `CLK` | 5 | `STORAGE_CLK_7` |
| `DAT0` | 7 | `STORAGE_D0_7` |
| `DAT1` | 8 | `STORAGE_D1_7` |
| `DAT2` | 1 | `STORAGE_D2_7` |
| `DAT3`/`CD` | 2 | `STORAGE_CDD3_7` |
| `CD` (mechanical) | 9 | `STORAGE_CD_7` |

`VSS`(6) and the shield pins (10-13) stay out of this table — GND, no hierarchical port needed.

## Open questions

1. Voltage domain check for pin 9's host GPIO (see Known Gaps) — resolve when Compute-SoC assigns a pin.
2. Confirm 30kOhm pull-up value against RK3576 SDMMC requirements once the TRM/SoC sheet work starts.
3. eMMC (`U3`, `EMMC04G-M627-Y02U`) also lives on this sheet (per `docs/schematic-status.md`) — not yet covered by this card; needs its own section or a separate card once its pinout (currently only a figure/diagram in the datasheet, not machine-readable) gets read manually.
