# FC-05D30P11H20 — GPIO/expansion FPC header (30P + 2 shield)

**Designator:** FPC1

**Wiring targets:** U1/RK3576

**Card origin:** Manually authored — no vendor pin-function datasheet exists for this connector (generic 0.5mm-pitch FFC/FPC housing, mechanical-only part numbering); this pinout is a Cradle-specific design, not a vendor spec.

**Vendor:** generic FFC/FPC connector house (part `FC-05D30P11H20`) **Datasheet:** none usable — no pin-function content found for this part number; same class of gap as `HDMI-519S.md`'s connector. **Structural index:** n/a.

**Role corrected 2026-07-21** `[MANUAL — user, 2026-07-21]` — `FPC1` keeps its original `FC-05D30P11H20` (30P, slide-lock actuator) and takes the **GPIO/expansion role**; the CSI-camera role and the `05A20L22P` part swap belong on `FPC2` instead — see `FPC2.md`. An earlier draft of this card had the two reversed.

**Wired 2026-07-21** `[MANUAL — user, 2026-07-21]` — user wired this header in Altium and re-exported; confirmed against the fresh netlist below. Matches the proposed pinout almost exactly, with two differences: pins 26/27 (left "reserved" in the proposal) are now `EXP_GPIO9`/`EXP_GPIO10` instead of unused, and **no level-shifter was added** — the user decided to skip level-shifting for now (see High-level summary and Known gaps), so every signal here goes straight from the connector pin to a pending RK3576-side net with no buffer in between.

## High-level summary

- General-purpose GPIO/expansion header, deliberately kept separate from any display role: Cradle already has HDMI (`HDMI-519S.md`, U8) as its display output, so this connector doesn't need to carry MIPI DSI — confirmed with the user 2026-07-21 `[MANUAL — user, 2026-07-21]`. A local/attached-panel use case would flip this decision, but none exists currently.
- Netlist shows 32 physical pins (`FPC1-1` through `FPC1-32`) `[VERIFIED — Cradle.NET/Cradle.csv]` — the extra 2 beyond the "30P" BOM description are shield/frame ground tabs, same pattern as `FPC2.md`/`HDMI-519S.md`.
- **Signal mix and pin-order convention adapted from NVIDIA's Jetson Orin NX carrier board 40-pin GPIO expansion header** (`P3768-A04`, page 23), read via vector text extraction `[MANUAL — user-supplied reference schematic, 2026-07-21]`. Real findings from that reference:
  1. Jetson needs 3x `TXB0108` 8-bit auto-direction level-shifters between its SoC and header because **Jetson Orin NX's exposed GPIO bank is fixed at 1.8V, with no 3.3V option**. **RK3576 is different**: its `VCCIO1-6` banks are switchable between 1.8V and 3.3V `[VERIFIED — RK3576 datasheet V1.6.tables.md, GPIO power spec table]` — so Cradle can skip the level-shifter Jetson needed, **as long as the Compute-SoC sheet pinmux's this header onto a `VCCIO1-6` bank in 3.3V mode** (see the hard constraint below — decided 2026-07-21, not left as a bet).
  2. Jetson protects its 5V header pin with a reverse-power / "ideal diode" circuit (`Q23` P-FET + `Q24A`/`B` dual-BJT) so a peripheral with its own onboard supply can't back-feed the board if plugged in live. **Decided against for Cradle 2026-07-21** — see below; considered a reasonable simplification given this header's low current/low-risk use case rather than something worth the extra parts.
  3. Jetson's two direct-connect I2C buses get single-channel `LESD5VD8LCG-R` ESD diodes since they're the only signals reaching the header with no buffer chip's inherent protection. **Correction 2026-07-21** `[MANUAL — user, 2026-07-21]`: those are single-line shunt-to-GND diodes, one per line — not the same kind of part as Cradle's standardized `JLC_PRTR5V0U2X_C2827688`, which is a matched differential-pair array, wrong shape for single-ended GPIO/I2C/SPI/UART lines. If ESD protection is added here, it needs a genuinely single-line-appropriate part, not a reuse of the diff-pair part (see Known gaps).
  4. The reference header's signal *order* groups pins by bus (SPI block, UART block) with GND pins distributed throughout each group rather than only at the connector's edges — this is the actual justification for the pin order below, not an arbitrary choice. Cradle's version drops Jetson-specific extras (I2S/DAP audio-over-header, the ID-EEPROM auto-detect bus) since neither is a Cradle requirement.
- With 30 pins available (10 more than the 20-pin part originally considered for this role), the extra room went to more raw GPIO — **10 total** (`EXP_GPIO1`-`EXP_GPIO10`) once the user filled the 2 previously-reserved pins, rather than leaving them unused.
- **Level-shifting decided 2026-07-21** `[MANUAL — user, 2026-07-21]`: **no level-shifter for this header, for now.** Every signal (`GPIO1`-`10`, I2C, SPI, UART) connects straight from the connector pin to a pending RK3576-side net (`*` suffix, single-pin, awaiting the Compute-SoC sheet) with nothing in between.
- **HARD CONSTRAINT on the Compute-SoC sheet, set 2026-07-21** `[MANUAL — user, 2026-07-21]`: because there is no level-shifter here, **every signal on this header (`EXP_GPIO1`-`10`, `EXP_I2C_SCL`/`SDA`, `EXP_SPI_*`, `EXP_UART_*`) must be pinmux'd to a bank from RK3576's `VCCIO1-6` group, configured in 3.3V mode — `VCCIO0`/`PMUIO0` (1.8V-only) must not be used for any signal on this connector.** This is not a preference, it's a correctness requirement: without a level-shifter in the path, assigning a 1.8V-only bank here would drive/receive 3.3V directly against a 1.8V-only pad, risking exceeding absolute max on that pad. Whoever builds the Compute-SoC sheet needs to honor this constraint when choosing pinmux instances for this header — it isn't optional or a "nice to have," it's the thing that makes the no-level-shifter decision safe.
- **ESD protection added 2026-07-21** `[MANUAL — user, 2026-07-21]` for the two buses most likely to run an external cable: `EXP_I2C_SCL`/`SDA` (`D23`/`D24`) and `EXP_UART_TX`/`RX` (`D25`/`D26`), all `ESD9L5.0ST5G` (same single-line part proven in on `FPC2.md`'s camera lines). `EXP_GPIO*`/`EXP_SPI_*` remain unprotected — lower priority since they're more likely to stay board-to-board on a short ribbon than run to an external peripheral.
- **Reverse-power protection on `EXP_3V3` decided against, 2026-07-21** `[MANUAL — user, 2026-07-21]`: both power pins (2, 24) wire straight to `INTERFACES_3V3` with no ideal-diode/reverse-blocking circuit. This is an accepted, conscious simplification, not an oversight — if a peripheral with its own onboard supply is ever plugged in live, it could back-feed `INTERFACES_3V3`. Documented as a known, accepted risk rather than an open task.

## Power domains

| Domain | Pin(s) | Range | Cradle rail |
|---|---|---|---|
| Header power out | 2, 24 | 3.3V | `INTERFACES_3V3`, direct — no reverse-power protection (decided against 2026-07-21, accepted risk) |

## Pin table

Wired and confirmed against the 2026-07-21 22:45 netlist/BOM export. `Type` = direction relative to this connector part. All GPIO/I2C/SPI/UART signals are the connector-side net (`*` suffix = Cradle_Interfaces sheet-local); the RK3576-facing side of each is still a separate, single-pin net pending the Compute-SoC sheet.

| # | Name | Type | Vendor function | Cradle wiring | Status |
|---|---|---|---|---|---|
| 1 | GND | — | Ground | Ground plane | Decided |
| 2 | `EXP_3V3` | I | Power out to peripheral | `INTERFACES_3V3`, direct — no reverse-power protection (decided against, accepted risk) | Decided |
| 3 | `EXP_GPIO1` | I/O | Generic GPIO | `EXP_GPIO1` — pending Compute-SoC sheet (RK3576) | Decided |
| 4 | `EXP_GPIO2` | I/O | Generic GPIO | `EXP_GPIO2` — pending Compute-SoC sheet (RK3576) | Decided |
| 5 | `EXP_GPIO3` | I/O | Generic GPIO | `EXP_GPIO3` — pending Compute-SoC sheet (RK3576) | Decided |
| 6 | `EXP_GPIO4` | I/O | Generic GPIO | `EXP_GPIO4` — pending Compute-SoC sheet (RK3576) | Decided |
| 7 | GND | — | Ground | Ground plane | Decided |
| 8 | `EXP_I2C_SCL` | I/O | Expansion I2C bus, clock | `EXP_I2C_SCL`, no level-shifter (must land on a `VCCIO1-6` 3.3V-mode bank, see High-level summary), ESD diode `D23` (`ESD9L5.0ST5G`) — pending Compute-SoC sheet (RK3576) | Decided |
| 9 | `EXP_I2C_SDA` | I/O | Expansion I2C bus, data | `EXP_I2C_SDA`, no level-shifter, ESD diode `D24` (`ESD9L5.0ST5G`) — pending Compute-SoC sheet (RK3576) | Decided |
| 10 | GND | — | Ground | Ground plane | Decided |
| 11 | `EXP_SPI_SCK` | O | Expansion SPI bus, clock | `EXP_SPI_SCK` — pending Compute-SoC sheet (RK3576) | Decided |
| 12 | `EXP_SPI_MOSI` | O | Expansion SPI bus, host-out | `EXP_SPI_MOSI` — pending Compute-SoC sheet (RK3576) | Decided |
| 13 | `EXP_SPI_MISO` | I | Expansion SPI bus, host-in | `EXP_SPI_MISO` — pending Compute-SoC sheet (RK3576) | Decided |
| 14 | `EXP_SPI_CSN` | O | Expansion SPI bus, chip select | `EXP_SPI_CSN` — pending Compute-SoC sheet (RK3576) | Decided |
| 15 | GND | — | Ground | Ground plane | Decided |
| 16 | `EXP_UART_TX` | O | Expansion UART, transmit | `EXP_UART_TX`, ESD diode `D25` (`ESD9L5.0ST5G`) — pending Compute-SoC sheet (RK3576) | Decided |
| 17 | `EXP_UART_RX` | I | Expansion UART, receive | `EXP_UART_RX`, ESD diode `D26` (`ESD9L5.0ST5G`) — pending Compute-SoC sheet (RK3576) | Decided |
| 18 | GND | — | Ground | Ground plane | Decided |
| 19 | `EXP_GPIO5` | I/O | Generic GPIO | `EXP_GPIO5` — pending Compute-SoC sheet (RK3576) | Decided |
| 20 | `EXP_GPIO6` | I/O | Generic GPIO | `EXP_GPIO6` — pending Compute-SoC sheet (RK3576) | Decided |
| 21 | `EXP_GPIO7` | I/O | Generic GPIO | `EXP_GPIO7` — pending Compute-SoC sheet (RK3576) | Decided |
| 22 | `EXP_GPIO8` | I/O | Generic GPIO | `EXP_GPIO8` — pending Compute-SoC sheet (RK3576) | Decided |
| 23 | GND | — | Ground | Ground plane | Decided |
| 24 | `EXP_3V3` | I | Power out to peripheral (second pin, same rail as pin 2) | `INTERFACES_3V3` (confirmed same net as pin 2) | Decided |
| 25 | GND | — | Ground | Ground plane | Decided |
| 26 | `EXP_GPIO9` | I/O | Generic GPIO — filled in from the proposal's "reserved" pin | `EXP_GPIO9` — pending Compute-SoC sheet (RK3576) | Decided |
| 27 | `EXP_GPIO10` | I/O | Generic GPIO — filled in from the proposal's "reserved" pin | `EXP_GPIO10` — pending Compute-SoC sheet (RK3576) | Decided |
| 28 | GND | — | Ground | Ground plane | Decided |
| 29 | GND | — | Ground | Ground plane | Decided |
| 30 | GND | — | Ground | Ground plane | Decided |
| 31 | GND | — | Shield/frame tab (mechanical) | Ground plane | Decided |
| 32 | GND | — | Shield/frame tab (mechanical) | Ground plane | Decided |

## Known gaps (things the vendor datasheet does not specify)

- **No vendor datasheet at all for this connector**, same as `FPC2.md`.
- **HARD CONSTRAINT for the Compute-SoC sheet**: every signal on this header must land on a `VCCIO1-6` bank in 3.3V mode. There is no level-shifter here, so a `VCCIO0`/`PMUIO0` (1.8V-only) assignment would be a real absolute-max violation, not a cosmetic mismatch. See High-level summary.
- **`EXP_3V3` has no reverse-power protection** — decided 2026-07-21, an accepted risk given this header's low-current/low-stakes use case, not an oversight.
- **`EXP_GPIO*`/`EXP_SPI_*` have no ESD protection** — I2C and UART got it (`D23`-`D26`, `ESD9L5.0ST5G`) since those are the buses most likely to run an external cable; GPIO/SPI were left unprotected as lower priority.
- **Exact RK3576 GPIO/I2C/SPI/UART instance assignment not chosen** — any free instances work electrically, as long as they come from a `VCCIO1-6` bank in 3.3V mode; final choice depends on what else the Compute-SoC sheet allocates.

## External validation (secondary sources, not the primary datasheet)

- NVIDIA Jetson Orin NX Carrier Board, `P3768-A04`, `cradle_sidecar/data/datasheets/P3768_A04_OrCAD_schematics(base_version).pdf`, page 23 ("40PIN GPIO Expansion HDR") — real reference schematic, used to validate the signal mix, pin-order convention, and flag the level-shifting/reverse-power/ESD design questions above. `[MANUAL — user-supplied, 2026-07-21]`

## Net name map (card name -> real Altium net name)

Connector-side net labels match the card names 1:1 (e.g. `EXP_GPIO1` pin is literally net `EXP_GPIO1`) — no separate mapping needed. The RK3576-facing side of each signal remains a distinct, still-unconnected net pending the Compute-SoC sheet.

## Open questions

1. RK3576 pinmux instance/bank assignment for all GPIO/I2C/SPI/UART signals on this header — pending the Compute-SoC sheet (RK3576), which doesn't exist yet. **Must satisfy the hard constraint**: a `VCCIO1-6` bank in 3.3V mode, not `VCCIO0`/`PMUIO0`.
