# Net registry — cross-sheet nets

Layer 3 from `cradle_sidecar/co-design-workflow.md`, seeded rather than left as "still proposed, not built." Scope: **only nets that cross a sheet boundary** (hierarchical ports). Pin-local facts (a pull resistor entirely within one sheet) belong in the relevant `cradle_sidecar/data/components/<PART>.md` instead — see that doc's Layer 1/Layer 3 split.

Seeded 2026-07-08 from the Wireless sheet only, using `AP6275S.md`'s net name map + the real netlist. Not exhaustive — PMIC/Charging/Audio/Storage/Interfaces cross-sheet nets aren't in here yet, add as those sheets get the same treatment.

**Format not fully decided** (see `cradle_sidecar/co-design-workflow.md` open question — markdown here for consistency with other sidecar data files, may move to CSV if row count grows past what's comfortably skimmable).

| Net (real Altium name) | Driven from | Consumed by | Voltage domain | Pull/term (owner sheet) | Protocol/speed | SoC pin | Status |
|---|---|---|---|---|---|---|---|
| `WIRELESS_3V3` | Power sheet (Charging or PMIC — not yet traced upstream) | Wireless (AP6275S VBAT) | 3.0-3.8V | none | — | n/a (power) | pending — source not yet confirmed |
| `WIRELESS_1V8` | Power sheet (PMIC, presumed) | Wireless (AP6275S VDDIO + SIT1552 VCC) | 1.68-1.98V | — | — | n/a (power) | pending — source not yet confirmed |
| `WIRELESS_WL_REG_ON` | Compute-SoC | Wireless (AP6275S pin 15) | 1.8V logic | none, must not float | GPIO | TBD | pending |
| `WIRELESS_WL_HOST_WAKE` | Wireless (AP6275S pin 16) | Compute-SoC | 1.8V logic | none | GPIO | TBD | pending |
| `WIRELESS_SDCMD` | Compute-SoC | Wireless (AP6275S pin 17) | 1.8V | 30kOhm pull-up (Wireless) | SDIO 3.0 | TBD | pending |
| `WIRELESS_SDCLK` | Compute-SoC | Wireless (AP6275S pin 18) | 1.8V | 0Ohm series (Wireless) — card recommends ~100Ohm, not yet updated to match | SDIO 3.0 | TBD | pending |
| `WIRELESS_SD0` | Compute-SoC | Wireless (AP6275S pin 21) | 1.8V | 30kOhm pull-up (Wireless) | SDIO 3.0 | TBD | pending |
| `WIRELESS_SD1` | Compute-SoC | Wireless (AP6275S pin 22) | 1.8V | 30kOhm pull-up (Wireless) | SDIO 3.0 | TBD | pending |
| `WIRELESS_SD2` | Compute-SoC | Wireless (AP6275S pin 20) | 1.8V | 30kOhm pull-up (Wireless) | SDIO 3.0 | TBD | pending |
| `WIRELESS_SD3` | Compute-SoC | Wireless (AP6275S pin 19) | 1.8V | 30kOhm pull-up (Wireless) | SDIO 3.0 | TBD | pending |
| `WIRELESS_BT_REG_ON` | Compute-SoC | Wireless (AP6275S pin 38) | 1.8V logic | none, must not float | GPIO | TBD | pending |
| `WIRELESS_BT_HOST_WAKE` | Wireless (AP6275S pin 50) | Compute-SoC | 1.8V logic | none | GPIO | TBD | pending |
| `WIRELESS_BT_WAKE` | Compute-SoC | Wireless (AP6275S pin 49) | 1.8V logic | 10kOhm pull-up (Wireless, R29) | GPIO | TBD | pending |
| `WIRELESS_BT_UART_TXD` | Wireless (AP6275S pin 40) | Compute-SoC | 1.8V | none | UART, up to 4Mbps | TBD, needs RTS/CTS-capable mux | pending |
| `WIRELESS_BT_UART_RXD` | Compute-SoC | Wireless (AP6275S pin 41) | 1.8V | none | UART | same instance as TXD | pending |
| `WIRELESS_BT_UART_RTS_N` | Wireless (AP6275S pin 42) | Compute-SoC | 1.8V | none | UART flow control | same instance as TXD | pending |
| `WIRELESS_BT_UART_CTS_N` | Compute-SoC | Wireless (AP6275S pin 43) | 1.8V | none | UART flow control | same instance as TXD | pending |
| `WIRELESS_WL_GPIO_10` | Wireless (AP6275S pin 33) | unassigned | 1.8V | none | GPIO | n/a — purpose not yet decided | not addressed |
| `WIRELESS_WL_GPIO_11` | Wireless (AP6275S pin 35) | unassigned | 1.8V | none | GPIO | n/a — purpose not yet decided | not addressed |

Filtering by `SoC pin = TBD` is the Compute-SoC sheet's checklist for what it owes Wireless, per the original Layer 3 design — 15 rows currently qualify.
