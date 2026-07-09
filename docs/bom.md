# Bill of materials

Living document — edit in place as parts are confirmed or swapped. Log the *reason* for any swap in [decisions-log.md](decisions-log.md), not here.

Last updated: 2026-07-08

## Confirmed / sourced

| Designator | Part Number | Description | LCSC/JLCPCB # | Qty |
|---|---|---|---|---|
| U1 | RK3576 | Main SoC, FCCSP-698L | C42388007 | 1 |
| U2 | AP6275S | WiFi 6 + BT 5.3 module, SDIO | C2918717 | 1 |
| U3 | HDMI-519S | Mini-HDMI Type C connector | C183605 | 1 |
| U4 | EMMC04G-M627-Y02U | 4GB eMMC 5.1 | (confirmed) | 1 |
| U5 | K4UBE3D4AB-MGCL | 4GB LPDDR4X, x32, 200-ball FBGA | C5827966 | 1 |
| U6 | RK806S-5 | PMIC for RK3576, QFN-68 | C49174044 | 1 |
| U7 | BQ25601RTWR | Charger IC, QFN-24 | (confirmed) | 1 |
| U8 | AP2141WG-7 | USB host VBUS load switch, SOT-25 | (confirmed) | 1 |
| U9 | MAX98357AEWL+T | Class D audio amp, BGA-9 | (confirmed) | 1 |
| USB1, USB2 | TYPE-C 16P QTWT | USB-C connectors (charge + host) | C5187472 | 2 |
| Card1 | TF-01A | MicroSD slot, push-push | C91145 | 1 |
| FPC1 | FC-05D30P11H20 | 30P FPC, 0.5mm, MIPI-CSI | C23398805 | 1 |
| FPC2 | FC-05D20P11H20 | 20P FPC, 0.5mm, expansion | C23398799 | 1 |
| MIC1, MIC2 | MMICT390200012 | PDM MEMS microphone, TDK | C3171752 | 2 |
| J1 | SM04B-GHS-TB(LF)(SN) | UART debug header, JST GH 4-pin | (confirmed) | 1 |
| D1 | PESD5V0S1BA,115 | TVS on USB1 VBUS, SOD-323 | (to confirm) | 1 |
| L_CHG | SWPA4030S1R0NT | 1µH charger inductor, 4x4mm | C42193 | 1 |
| L_BUCK x10 | WPN252012ER47MT | 0.47µH buck inductors, 1008 | C317620 | 10 |
| SW1 | KMR221GLFS | Power button (QON), tactile momentary | (confirmed) | 1 |
| BAT | JST-PH 2-pin | LiPo battery connector | C131337 | 1 |
| SPK | JST-PH 2-pin | Speaker output connector | C131337 | 1 |
| NTC1 | 103AT-series | 10kΩ NTC thermistor, B=3435K | (to source) | 1 |

## Still needed (not yet sourced)

- L_WL1, L_WL2: 2.2-4.7uH inductors (**exact value not yet picked** — both evidence-backed from independent production schematics, see AP6275S.md open questions), 3030/1210 package, >=1A rated, DCR <=80mOhm — for AP6275S `CBUCK_0P9`/`CSR_VLX` and `ASR_VLX`/`ABUCK_1P12` internal buck loops (see decisions-log.md, 2026-07-07 entry)
- R_SDIO x5: 30kOhm pull-ups (R0402) on SDIO CMD/D0/D1/D2/D3, returned to 1.8V VDDIO rail, per AMPAK EVB manual (see decisions-log.md, 2026-07-07 entry)
- Crystal oscillator (24MHz for RK3576)
- Status LEDs (0402) + current limiting resistors
- Reset button (tactile SMD)
- ESD arrays for USB2 (D+/D-), mini-HDMI, FPC interfaces
- Reverse polarity protection MOSFET (DMP2035U or similar)
- U.FL antenna connector (optional-populate)
- Boot mode resistors
- I2C pull-up resistors
- All per-rail decoupling caps and passives (defined during schematic, ~40-60 components)
- Ferrite beads for analog/RF power isolation

## Sourcing watch list

Parts flagged as volatile-stock or single-source at time of selection — recheck before placing a fab/assembly order.

- **U5 (K4UBE3D4AB-MGCL)**: stock was volatile at selection. Footprint-compatible fallback is K4U6E3S4AA-MGCL (2GB, same 200-ball FBGA) if unavailable.
