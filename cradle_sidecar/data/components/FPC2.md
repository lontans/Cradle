# 05A20L22P — MIPI CSI camera FPC connector (22P + 2 shield)

**Designator:** FPC2

**Wiring targets:** U1/RK3576

**Card origin:** Manually authored — no vendor pin-function datasheet exists for this connector (generic 0.5mm-pitch FFC/FPC housing, mechanical-only part numbering); this pinout is a Cradle-specific design, not a vendor spec.

**Vendor:** HanElectricity (part `05A20L22P`, JLCPCB `C22435644`) **Datasheet:** none usable — no pin-function content found anywhere for this part number; same class of gap as `HDMI-519S.md`'s connector, just without even a mechanical PDF on file. **Structural index:** n/a.

**Wired 2026-07-21** `[MANUAL — user, 2026-07-21]` — user placed `05A20L22P` on `FPC2` (confirmed in BOM: `FPC-SMD_22P-P0.50_05A20L22P`, 24 physical pins per the fresh netlist, confirming the +2 shield pattern seen elsewhere on this board) and wired the sheet; confirmed against the fresh export below. The CSI-camera role and this part belong on `FPC2`, not `FPC1` as an earlier draft had it — `FPC1` stays on `FC-05D30P11H20` (30P) as the GPIO/expansion header, see `FPC1.md`.

## High-level summary

- Connects a MIPI CSI camera module to RK3576's standalone `MIPI_DPHY_CSI0_RX` port. **Cross-block lane-combining question resolved 2026-07-21** `[MANUAL — user, 2026-07-21]`: the wiring originally kept Jetson's split `CSI0`/`CSI1` block naming, which raised a real open question about whether RK3576 supports combining lanes across two separate CSI PHY blocks the way Jetson's combo-PHY does. User renamed the net labels so all 4 data lanes + clock are now `CSI0_D0`-`D3`/`CLK` — a single, self-contained standalone `CSI0` interface, since RK3576's `CSI0` ballout already provides all 4 lanes + clock on its own dedicated balls (confirmed: `AK20`-`AL24`, no shared naming with `CSI1` anywhere) `[VERIFIED — RK3576 datasheet V1.6.tables.md, MIPI_DPHY_CSI0_RX_* rows]`. This sidesteps the unconfirmed cross-block trick entirely rather than needing to resolve it, and leaves `CSI1` free for a possible second camera later.
- **PWDN level-shift circuit is built and confirmed**: `U15` (`SN74LV1T125DCKR`, matches the Jetson reference part) — `VCC` on `INTERFACES_3V3` (pin 5), `OE*` tied to `GND` (pin 1, always enabled), `IN` from a pending RK3576-side net `CAM_PWDN` (pin 2), `OUT` (pin 4) through ESD diode `D19` to the connector. Exactly the circuit this card recommended.
- **MCLK confirmed direct, no buffer** — connector pin 5 (`CAM_MCLK`) goes straight to ESD diode `D20`, no chip in between, matching the Jetson reference's asymmetry (`PWDN` buffered, `MCLK` not).
- **ESD part corrected and now built with a genuinely single-line-appropriate part**: `ESD9L5.0ST5G` (SOD-923, single-channel TVS), not `JLC_PRTR5V0U2X_C2827688` as this card had proposed. Now 14 instances (`D9`-`D22`), one per individual signal line — matching Jetson's own per-line topology exactly. Protection now covers all 10 diff-pair lines, `PWDN_LS`, `MCLK`, *and* (added 2026-07-21) `CAM_SDA`/`CAM_SCL` — full coverage of every signal on the connector.
- **`CAM_SDA`/`CAM_SCL` ESD added 2026-07-21** `[MANUAL — user, 2026-07-21]`: `D21`/`D22` (`ESD9L5.0ST5G`), matching every other line. Note this is transient/surge protection only — it's a separate concern from the I2C bus's steady-state pull-up resistors, which are deliberately *not* placed on this sheet (see below).
- **Power pin decided**: pin 1 wired to `INTERFACES_3V3` (shared with the HDMI level-shifters and `FPC1`'s header power) rather than a dedicated `CAM_3V3` net — resolves the earlier open question.
- **No separate `RESET_N` or spare GPIO pins**, as planned — 22 signal pins doesn't leave room; design assumes a sensor satisfied with `PWDN` alone.
- **Connector-side ESD diode nets intentionally left auto-named** `[MANUAL — user, 2026-07-21]` — the still-unlabeled nets (e.g. `NetD19_A`) are Altium's own auto-generated names; the user is not manually relabeling them for cosmetic purposes. Documented as a final, accepted state, not an outstanding task.

## Why no I2C pull-up resistors on this sheet

`CAM_SDA`/`CAM_SCL` now have ESD/surge protection (`D21`/`D22`), but **no pull-up resistors** — this is deliberate, not a gap:

- I2C only needs *one* set of pull-ups per bus, sized against total bus capacitance and placed once, not duplicated at every device/connector. Adding pull-ups here would be guessing at a value before the bus's actual topology (what else might share it, total trace length) is known.
- The correct pull-up value depends on the bus's final operating voltage (1.8V vs 3.3V), which isn't decided yet — it depends on which RK3576 bank/pinmux instance ends up hosting this I2C controller, a Compute-SoC-sheet decision that doesn't exist yet.
- RK3576 (like most SoCs) may have configurable internal weak pull-ups on I2C-capable GPIO pads. Adding an external pull-up now, before knowing whether the internal one will be enabled, risks either double-pulling the bus or picking a value that fights the internal setting.
- **Conclusion**: pull-ups belong on the Compute-SoC sheet (or wherever the I2C bus's host-side configuration is finalized), not on the Interfaces sheet at the connector. Tracked as an open item below.

## Power domains

| Domain | Pin(s) | Range | Cradle rail |
|---|---|---|---|
| Camera module supply | 1 | 3.3V | `INTERFACES_3V3` |

No analog/1.2V rail provided on this connector, per the Jetson reference — revisit only if a chosen sensor needs bare rail access instead of self-regulation.

## Pin table

Wired and confirmed against the 2026-07-21 22:45 netlist/BOM export. `Type` = direction relative to this connector part — RK3576 is the actual CSI receiver, so the camera module's outputs are `O` and the connector's own control/power inputs are `I`.

| # | Name | Type | Vendor function | Cradle wiring | Status |
|---|---|---|---|---|---|
| 1 | `VDD_3V3` | I | Camera module power, single rail | `INTERFACES_3V3` | Decided |
| 2 | `CAM_SDA` | I/O | Sensor control bus, data | `CAM_SDA`, ESD diode `D22` (`ESD9L5.0ST5G`) — pull-up deliberately deferred to the Compute-SoC sheet (bus voltage/host pad config not decided yet) — pending Compute-SoC sheet (RK3576) | Decided |
| 3 | `CAM_SCL` | I/O | Sensor control bus, clock | `CAM_SCL`, ESD diode `D21` (`ESD9L5.0ST5G`) — pull-up deliberately deferred to the Compute-SoC sheet — pending Compute-SoC sheet (RK3576) | Decided |
| 4 | GND | — | Ground | Ground plane | Decided |
| 5 | `CAM_MCLK` | I | Reference clock to sensor, driven directly (no level shift) | `CAM_MCLK` via ESD diode `D20` (`ESD9L5.0ST5G`) — pending Compute-SoC sheet (RK3576) | Decided |
| 6 | `CAM_PWDN_LS` | I | Power-down/standby, level-shifted | `U15` (`SN74LV1T125DCKR`) output via ESD diode `D19` (`ESD9L5.0ST5G`); `U15` `IN` = pending `CAM_PWDN` (RK3576 GPIO), `VCC` = `INTERFACES_3V3`, `OE*` = `GND` (always enabled) | Decided |
| 7 | GND | — | Ground | Ground plane | Decided |
| 8 | `CSI0_D1_P` | O | RK3576 `MIPI_DPHY_CSI0_RX_D1P` lane, positive | ESD diode `D18` (`ESD9L5.0ST5G`) then pending RK3576-side net — pending Compute-SoC sheet (RK3576) | Decided |
| 9 | `CSI0_D1_N` | O | RK3576 `MIPI_DPHY_CSI0_RX_D1N` lane, negative | ESD diode `D17` then pending RK3576-side net | Decided |
| 10 | GND | — | Ground | Ground plane | Decided |
| 11 | `CSI0_D0_P` | O | RK3576 `MIPI_DPHY_CSI0_RX_D0P` lane, positive | ESD diode `D16` then pending RK3576-side net | Decided |
| 12 | `CSI0_D0_N` | O | RK3576 `MIPI_DPHY_CSI0_RX_D0N` lane, negative | ESD diode `D15` then pending RK3576-side net | Decided |
| 13 | GND | — | Ground | Ground plane | Decided |
| 14 | `CSI0_CLK_P` | O | RK3576 `MIPI_DPHY_CSI0_RX_CLKP`, positive | ESD diode `D14` then pending RK3576-side net | Decided |
| 15 | `CSI0_CLK_N` | O | RK3576 `MIPI_DPHY_CSI0_RX_CLKN`, negative | ESD diode `D13` then pending RK3576-side net | Decided |
| 16 | GND | — | Ground | Ground plane | Decided |
| 17 | `CSI0_D3_P` | O | RK3576 `MIPI_DPHY_CSI0_RX_D3P` lane, positive | ESD diode `D12` then pending RK3576-side net | Decided |
| 18 | `CSI0_D3_N` | O | RK3576 `MIPI_DPHY_CSI0_RX_D3N` lane, negative | ESD diode `D11` then pending RK3576-side net | Decided |
| 19 | GND | — | Ground | Ground plane | Decided |
| 20 | `CSI0_D2_P` | O | RK3576 `MIPI_DPHY_CSI0_RX_D2P` lane, positive | ESD diode `D10` then pending RK3576-side net | Decided |
| 21 | `CSI0_D2_N` | O | RK3576 `MIPI_DPHY_CSI0_RX_D2N` lane, negative | ESD diode `D9` then pending RK3576-side net | Decided |
| 22 | GND | — | Ground | Ground plane | Decided |
| 23 | GND | — | Shield/frame tab (mechanical) | Ground plane | Decided |
| 24 | GND | — | Shield/frame tab (mechanical) | Ground plane | Decided |

14 ESD diodes total (`D9`-`D22`), one per individual signal line (not per pair) — `ESD9L5.0ST5G`, single-channel, matching Jetson's own topology. Every signal on this connector now has ESD protection.

## Known gaps (things the vendor datasheet does not specify)

- **No vendor datasheet at all for this connector** — no pin-function content, not even a mechanical PDF.
- **I2C pull-up resistor values and placement not yet decided** — deliberately deferred to the Compute-SoC sheet, see "Why no I2C pull-up resistors" above. Not a gap in this sheet's design, but a real dependency that needs to land somewhere before the camera can actually be used.
- **Exact RK3576 pinmux instance/bank for `CAM_PWDN`, `CAM_MCLK`, I2C, and `CSI0` not chosen** — pending the Compute-SoC sheet (RK3576), which doesn't exist yet.
- **Camera module not yet chosen** — the "single 3.3V rail, self-regulated module" and "`PWDN` only, no `RESET_N`" assumptions should be re-checked once a specific sensor is spec'd.

## External validation (secondary sources, not the primary datasheet)

- NVIDIA Jetson Orin NX Carrier Board, `P3768-A04`, `cradle_sidecar/data/datasheets/P3768_A04_OrCAD_schematics(base_version).pdf`, page 18 ("CSI CAM CONNECTORS") — real reference schematic, used to validate the pin assignment, level-shifting, and ESD architecture. Re-verified twice (text extraction + high-res visual crop). `[MANUAL — user-supplied, 2026-07-21]`

## Net name map (card name -> real Altium net name)

| Card name | Pin | Real Altium net name |
|---|---|---|
| `VDD_3V3` | 1 | `INTERFACES_3V3` |
| `CAM_SDA` | 2 | `CAM_SDA` |
| `CAM_SCL` | 3 | `CAM_SCL` |
| `CAM_MCLK` | 5 | `CAM_MCLK` (connector side of `D20`) |
| `CAM_PWDN_LS` | 6 | connector side of `D19` — Altium-auto-named (e.g. `NetD19_A`), intentionally left as-is, see High-level summary; RK3576-facing side of `U15` is `CAM_PWDN` |
| `CSI0_D1_P`/`N` | 8/9 | connector side of `D18`/`D17` — Altium-auto-named, intentionally left as-is |
| `CSI0_D0_P`/`N` | 11/12 | connector side of `D16`/`D15` — Altium-auto-named, intentionally left as-is |
| `CSI0_CLK_P`/`N` | 14/15 | connector side of `D14`/`D13` — Altium-auto-named, intentionally left as-is |
| `CSI0_D3_P`/`N` | 17/18 | connector side of `D12`/`D11` — Altium-auto-named, intentionally left as-is |
| `CSI0_D2_P`/`N` | 20/21 | connector side of `D10`/`D9` — Altium-auto-named, intentionally left as-is |

## Open questions

1. RK3576 pinmux instance/bank assignment for `CAM_PWDN`, `CAM_MCLK`, the I2C bus, and `CSI0` — pending the Compute-SoC sheet (RK3576), which doesn't exist yet.
2. I2C pull-up resistor value and placement — deliberately deferred to the Compute-SoC sheet or wherever the bus's host-side config is finalized, see "Why no I2C pull-up resistors" above.
3. Camera module selection — pending; revisit the "single 3.3V, no analog rail" and "`PWDN` only, no `RESET_N`" assumptions once a specific sensor is spec'd.
