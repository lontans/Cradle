# Schematic status

Sheet-by-sheet status of the Altium hierarchical schematic. Edit in place as sheets progress; log the *milestone* (sheet started/completed) in CHANGELOG.md.

Net naming convention: match Radxa naming where possible for cross-reference during debug. Hierarchical ports required on every net that crosses sheet boundaries — Radxa uses flat topology with inconsistent naming, which requires careful translation into Altium's hierarchical port system. Key nets: `VSYS`, `VDD_CPU`, `VDD_GPU`, `VDD_NPU`, `VDD_LOGIC`, `VCC_DDR`, `VCC_3V3`, `VCC_1V8`, `I2C_SCL`, `I2C_SDA`.

| # | Sheet | Status | Notes |
|---|---|---|---|
| 1 | Power — Charging | **Complete** | BQ25601, battery connector, USB1 CC resistors, VSYS output, TVS, reverse polarity protection, NTC thermistor, QON switch |
| 2 | Power — PMIC | **In progress** | RK806S-5, all 10 buck regulators (inductors + decoupling) done. Remaining: LDO outputs, PWRON, RESET_OUT, I2C interface, enable/fault pins |
| 3 | Compute — SoC | Not started | RK3576 pin assignments, power pins to named nets, clock, reset, boot mode resistors, JTAG pads. **Do this sheet last** — by then every net it connects to already has a name |
| 4 | Compute — Memory | Not started | LPDDR4X (K4UBE3D4AB-MGCL) and eMMC (EMMC04G-M627-Y02U), all decoupling |
| 5 | Wireless | **In progress** | AP6275S: SDIO (4-bit) to SoC, UART to SoC (BT HCI; PCM omitted), 2x Johanson 2450AT18A100E 2.4GHz chip antennas + matching networks, 37.4MHz crystal + load caps, 32.768kHz SiTime MEMS oscillator on LPO. 2.4GHz-only (5GHz dropped). Full pin-out now resolved including CBUCK/ABUCK inductor loops, SDIO no-pull-up wiring, and REG_ON/HOST_WAKE GPIO connections — ready to lay out in Altium. See docs/decisions-log.md |
| 6 | Storage and SD | Not started | MicroSD slot (TF-01A), card detect, decoupling |
| 7 | Interfaces — USB and HDMI | Not started | Both USB-C connectors, AP2141 load switch, CC resistors, ESD arrays, mini-HDMI, TMDS termination |
| 8 | Interfaces — FPC and Expansion | Not started | 30-pin CSI FPC, 20-pin expansion FPC, ESD protection, pull-ups, pin assignment documentation |
| 9 | Audio | **In progress** | MAX98357AEWL+T (U9): mono speaker, I2S Channel 0 (SD_MODE HIGH), GAIN NC (9dB), OUTP/OUTN to speaker JST-PH on Interfaces sheet. Both MEMS mics (MIC1 right/SELECT-GND, MIC2 left/SELECT-3V3) share CLK/DATA, split by rising/falling clock edge. RK3576's 2x PDM controllers + 5x SAI/I2S blocks handle both natively — no external codec (see docs/decisions-log.md) |
| 10 | System | Not started | Debug UART header, power/reset buttons, status LEDs, crystal oscillator, boot mode resistors |
