# Ported tables: SIT1552AI-JF-DCC-32.768D Documentation.pdf

Mechanically extracted pin tables and spec/parameter tables -- cell contents are verbatim from the PDF, not reworded or interpreted. Review before trusting (table detection can misparse merged cells or footnote markers) and fold the relevant parts into `docs/components/<PART>.md` by hand, including the Cradle Wiring and Status columns that only a real design decision can fill in.

## Page 1 -- spec/parameter table

| Parameter | Symbol | Min. | Typ. | Max. | Unit | Condition |
|---|---|---|---|---|---|---|
| Frequency and Stability |  |  |  |  |  |  |
| Output Frequency | Fout | 32.768 |  |  | kHz |  |
| Frequency Stability Over Temperature[1] |  | -5.0 |  | 5.0 | ppm | Stability part number code = E |
| (without Initial Offset[2]) | F_stab | -10 |  | 10 |  | Stability part number code = F |
|  |  | -20 |  | 20 |  | Stability part number code = 1 |
| Frequency Stability Over Temperature (with Initial Offset [2]) | F_stab | -10 |  | 10 | ppm | Stability part number code = E |
|  |  | -13 |  | 13 |  | Stability part number code = F |
|  |  | -22 |  | 22 |  | Stability part number code = 1 |
| Frequency Stability vs Voltage | F_vdd | -0.75 |  | 0.75 | ppm | 1.8 V ±10% |
|  |  | -1.5 |  | 1.5 | ppm | 1.5 V – 3.63 V |
| First Year Frequency Aging | F_aging | -1.0 |  | 1.0 | ppm | TA = 25°C, Vdd = 3.3 V |
| Jitter Performance (TA = over temp) |  |  |  |  |  |  |
| Long Term Jitter |  |  |  | 2.5 | µspp | 81920 cycles (2.5 sec), 100 samples |
| Period Jitter |  |  | 35 |  | nsRMS | Cycles = 10,000, T = 25°C, Vdd = 1.5 V – 3.63 V A |
| Supply Voltage and Current Consumption |  |  |  |  |  |  |
| Operating Supply Voltage | Vdd | 1.5 |  | 3.63 | V | TA = -40°C to +85°C |
| Core Supply Current [3] | Idd |  | 0.99 |  | μA | TA = 25°C, Vdd = 1.8 V, LVCMOS Output configuration, No Load |
|  |  |  |  | 1.52 |  | TA = -40°C to +85°C, Vdd = 1.5 V – 3.63 V, No Load |
| Power-Supply Ramp | t Vdd R_amp_ |  |  | 100 | ms | Vdd Ramp-Up 0 to 90% Vdd, TA = -40°C to +85°C |
| Start-up Time at Power-up | t_start |  | 180 | 300 | ms | TA = -40°C +60°C, valid output |
|  |  |  |  | 350 |  | TA = +60°C to +70°C, valid output |
|  |  |  |  | 380 |  | TA = +70°C to +85°C, valid output |

## Page 2 -- spec/parameter table

| Parameter | Symbol | Min. | Typ. | Max. | Unit | Condition |
|---|---|---|---|---|---|---|
| Operating Temperature Range |  |  |  |  |  |  |
| Commercial Temperature | Op_Temp | 0 |  | 70 | °C |  |
| Industrial Temperature |  | -40 |  | 85 | °C |  |
| LVCMOS Output |  |  |  |  |  |  |
| Output Rise/Fall Time | tr, tf |  | 100 | 200 | ns | 10-90% (Vdd), 15 pF Load |
|  |  |  |  | 50 |  | 10-90% (Vdd), 5 pF Load, Vdd ≥ 1.62 V |
| Output Clock Duty Cycle | DC | 48 |  | 52 | % |  |
| Output Voltage High | VOH | 90% |  |  | V | Vdd: 1.5 V – 3.63 V. IOH = -1 μA, 15 pF Load |
| Output Voltage Low | VOL |  |  | 10% | V | Vdd: 1.5 V – 3.63 V. IOL = 1 μA, 15 pF Load |
| NanoDrive™ Programmable, Reduced Swing Output |  |  |  |  |  |  |
| Output Rise/Fall Time | tf, tf |  |  | 200 | ns | 30-70% (VOL/VOH), 10 pF Load |
| Output Clock Duty Cycle | DC | 48 |  | 52 | % |  |
| AC-coupled Programmable Output Swing | V_sw |  | 0.20 to 0.80 |  | V | SiT1552 does not internally AC-couple. This output description is intended for a receiver that is AC-coupled. See Table 4 for acceptable NanoDrive swing options. Vdd: 1.5 V – 3.63 V, 10 pF Load, IOH / IOL = ±0.2 μA |
| DC-Biased Programmable Output Voltage High Range | VOH |  | 0.60 to 1.225 |  | V | Vdd: 1.5 V – 3.63 V. IOH = -0.2 μA, 10 pF Load. See Table 4 for acceptable VOH/VOL setting levels. |
| DC-Biased Programmable Output Voltage Low Range | VOL |  | 0.35 to 0.80 |  | V | Vdd: 1.5 V – 3.63 V. IOL = 0.2 μA, 10 pF Load. See Table 4 for acceptable VOH/VOL setting levels. |
| Programmable Output Voltage Swing Tolerance |  | -0.055 |  | 0.055 | V | TA = -40°C to +85°C, Vdd = 1.5 V to 3.63 V |

## Page 3 -- spec/parameter table

| Parameter | Test Condition | Value | Unit |
|---|---|---|---|
| Continuous Power Supply Voltage Range (Vdd) |  | -0.5 to 3.63 | V |
| Short Duration Maximum Power Supply Voltage (Vdd) | ≤30 minutes | 4.0 | V |
| Continuous Maximum Operating Temperature Range | Vdd = 1.5V - 3.63V | 105 | °C |
| Short Duration Maximum Operating Temperature Range | Vdd = 1.5V - 3.63V, ≤30 mins | 125 | °C |
| Human Body Model (HBM) ESD Protection | JESD22-A114 | 3000 | V |
| Charge-Device Model (CDM) ESD Protection | JESD22- C101 | 750 | V |
| Machine Model (MM) ESD Protection | JESD22- A115 | 300 | V |
| Latch-up Tolerance | JESD78 Compliant |  |  |
| Mechanical Shock Resistance | Mil 883, Method 2002 | 10,000 | g |
| Mechanical Vibration Resistance | Mil 883, Method 2007 | 70 | g |
| 1508 CSP Junction Temperature |  | 150 | °C |
| Storage Temperature |  | -65°C to 150°C |  |

