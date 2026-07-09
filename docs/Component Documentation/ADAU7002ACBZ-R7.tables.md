# Ported tables: ADAU7002ACBZ-R7 Documentation.pdf

Mechanically extracted pin tables and spec/parameter tables -- cell contents are verbatim from the PDF, not reworded or interpreted. Review before trusting (table detection can misparse merged cells or footnote markers) and fold the relevant parts into `docs/components/<PART>.md` by hand, including the Cradle Wiring and Status columns that only a real design decision can fill in.

## Page 3 -- spec/parameter table

| Parameter | Test Conditions/Comments | Min Typ Max | Unit |
|---|---|---|---|
| DIGITAL INPUT/OUTPUT High Level Input Voltage (V ) IH Low Level Input Voltage (V ) IL Input Leakage, High (I ) IH Input Leakage, Low (I ) IL Input Capacitance SDATA PDM_CLK | BCLK and LRCLK pins BCLK and LRCLK pins | 0.7 × IOVDD 0.3 × IOVDD 1 1 5 4.5 9 | V V µA µA pF mA mA |
| PERFORMANCE Dynamic Range With A-Weighted Filter (RMS) Signal-to-Noise-Ratio Decimation Ratio Frequency Response Stop Band Stop-Band Attenuation Group Delay Gain Start-Up Time Bit Width Interchannel Phase | 20 Hz to 20 kHz, −60 dB input A-weighted, fourth-order input DC to 0.45 output f S 0.02 f input signal S PDM to PCM Internal and output | 110 110 64× −0.1 +0.01 0.566 60 3.31 0 48 20 0 | dB dB dB f S dB LRCLK cycles dB LRCLK cycles Bits Degrees |
| CLOCKING Output Sampling Rate BCLK Frequency | f LRCLK pulse rate S f BCLK | 4 48 96 0.256 3.072 24.576 | kHz MHz |
| POWER SUPPLIES Supply Voltage Range Supply Current Shutdown Current | IOVDD IOVDD = 1.8 V IOVDD = 3.3 V IOVDD = 1.8 V, 16 kHz output IOVDD = 3.3 V, 16 kHz output IOVDD , no input clocks SD | 1.62 3.6 0.67 1.33 0.21 0.41 1 | V mA mA mA mA µA |

## Page 5 -- pin table

| Pin No. | Mnemonic | Type | Description |
|---|---|---|---|
| A1 | PDM DAT_PDM CLK | Input | PDM Data Input |
| A2 | _ | Output | PDM Clock Output |
| B1 | SDATA | Output | Serial Data Output for I2S/TDM |
| B2 | BCLK | Input | Bit Clock for I2S/TDM |
| C1 | GND | Ground | Ground |
| C2 | LRCLK | Input | Left/Right Clock for I2S/Frame Sync for TDM |
| D1 | IOVDD | Supply | Input/Output and Digital Supply |
| D2 | CONFIG | Input | Configuration Pin |

## Page 10 -- spec/parameter table

| Parameter | Symbol | t MIN | t MAX | Unit |
|---|---|---|---|---|
| BCLK Pulse Width High BCLK Pulse Width Low LRCLK Setup Time LRCLK Hold Time Time from BCLK Falling | t BIH t BIL t LIS t LIH t SODM | 10 10 10 10 | 18 | ns ns ns ns ns |

