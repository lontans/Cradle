# Ported tables: EMMC04G-M627-Y02U Datasheet.pdf

Mechanically extracted pin tables and spec/parameter tables -- cell contents are verbatim from the PDF, not reworded or interpreted. Review before trusting (table detection can misparse merged cells or footnote markers) and fold the relevant parts into `cradle_sidecar/data/components/<PART>.md` by hand, including the Cradle Wiring and Status columns that only a real design decision can fill in.

## Page 12 -- spec/parameter table

| Symbol | Comment | Min | Max | Unit |
|---|---|---|---|---|
| tRSTW | RST_n_pulse_width | 1 |  | [us] |
| tRSCA | RST_n_to_Command_time | 2001 |  | [us] |
| tRSTH | RST_n_high_period_(interval_time) | 1 |  | [us] |
| Note1：74 cycles of clock signal required before issuing CMD1 or CMD0 with argument 0xFFFFFFFA |  |  |  |  |

## Page 24 -- spec/parameter table

| Parameter | Symbol | Min | Max. | Unit | Remark |
|---|---|---|---|---|---|
| Peak voltage on all lines |  | -0.5 | VCCQ + 0.5 | V |  |
| All Inputs |  |  |  |  |  |
| Input Leakage Current (before initialization sequence and/or the internal pull up resistors connected) |  | -100 | 100 | μA |  |
| Input Leakage Current (after initialization sequence and the internal pull up resistors disconnected) |  | -2 | 2 | μA |  |
| All Outputs |  |  |  |  |  |
| Output Leakage Current (before initialization sequence) |  | -100 | 100 | μA |  |
| Output Leakage Current (after initialization sequence) |  | -2 | 2 | μA |  |
| Note1：Initialization sequence is defined in section 10.1 |  |  |  |  |  |

## Page 25 -- spec/parameter table

| Parameter | Symbol | MIN | MAX | Unit | Remarks |
|---|---|---|---|---|---|
| Supply voltage (NAND) | V CC | 2.7 | 3.6 | V |  |
| Supply voltage (I/O) | V CCQ | 2.7 | 3.6 | V |  |
|  |  | 1.7 | 1.95 | V |  |
| Supply power-up for 3.3V | t PRUH |  | 35 | ms |  |
| Supply power-up for 1.8V | t PRUL |  | 25 | ms |  |

## Page 26 -- spec/parameter table

| Parameter | Symbol | Min | Max | Unit | Remark |
|---|---|---|---|---|---|
| Pull-up resistance for CMD | R CMD | 4.7 | 50 | Kohm | to prevent bus floating |
| Pull-up resistance for DAT0–7 | R DAT | 10 | 50 | Kohm | to prevent bus floating |
| Pull-up resistance for RST_n | R RSTn | 4.7 | 50 | Kohm | It is not necessary to put pull-up resistance on RST_n_(H/W_rest)_line if host does not use H/W reset. (Extended CSD register [162] = 0 b ) |
| Bus signal line capacitance | CL |  | 30 | pF | Single Device |
| Single Device capacitance | C BGA |  | 12 | pF |  |
| Maximum signal line inductance |  |  | 16 | nH |  |
| Impedance on CLK / CMD / DAT0~7 |  | 45 | 55 | ohm | Impedance match |
| Serial’s resistance on CLK line | SR CLK | 0 | 47 | ohm |  |
| Serial’s resistance on CMD / DAT0~7 line | SR CMD SR DAT0~7 | 0 | 47 | ohm |  |
| V decoupling capacitor CCQ |  | 2.2+0.1 | 4.7+0.22 | μF | It should be located as close as possible to the balls defined in order to minimize connection parasitic |
|  | CH1 | 1 | 2.2 |  | CH1 is only for HS200. It should be placed adjacent to VCCQ-VSSQ balls (#K6 and #K4 accordingly, next to DAT [7..0] balls). It should be located as close as possible to the balls defined in order to minimize connection parasitic. |
| VCC capacitor value |  | 1+0.1 | 4.7+0.22 | μF | It should be located as close as possible to the balls defined in order to minimize connection parasitic |
| V capacitor value DDi | C REG | 1 | 4.7+0.1 | μF | To stabilize regulator output to controller core logics. It should be located as close as possible to the balls defined in order to minimize connection parasitic |

## Page 28 -- spec/parameter table

| Parameter | Symbol | Min | Max. | Unit | Conditions |
|---|---|---|---|---|---|
| Output HIGH voltage | VOH | VDD – 0.2 |  | V | IOH = -100 μA |
| Output LOW voltage | VOL |  | 0.3 | V | IOL = 2 mA |

## Page 28 -- spec/parameter table

| Parameter | Symbol | Min | Max. | Unit | Conditions |
|---|---|---|---|---|---|
| Output HIGH voltage | VOH | 0.75 * VCCQ |  | V | IOH = -100 μA @ V min CCQ |
| Output LOW voltage | VOL |  | 0.125 * VCCQ | V | IOL = 100 μA @ V min CCQ |
| Input HIGH voltage | VIH | 0.625 * VCCQ | VCCQ + 0.3 | V |  |
| Input LOW voltage | VIL | VSS – 0.3 | 0.25 * VCCQ | V |  |

## Page 29 -- spec/parameter table

| Parameter | Symbol | Min | Max. | Unit | Conditions |
|---|---|---|---|---|---|
| Output HIGH voltage | VOH | V – 0.45V CCQ |  | V | IOH = -2mA |
| Output LOW voltage | VOL |  | 0.45V | V | IOL = 2mA |
| Input HIGH voltage | VIH | 0.65 * V CCQ 1 | V + 0.3 CCQ | V |  |
| Input LOW voltage | VIL | V – 0.3 SS | 0.35 * V DD2 | V |  |
| Note1：0.7 * V for MMC™4.3 and older revisions. |  |  |  |  |  |
| DD |  |  |  |  |  |
| Note2：0.3 * V for MMC™4.3 and older revisions. |  |  |  |  |  |
| DD |  |  |  |  |  |

## Page 30 -- spec/parameter table

| Parameter | Symbol | Min | Max. | Unit | Remark |
|---|---|---|---|---|---|
| Clock CLK1 |  |  |  |  |  |
| Clock frequency Data Transfer Mode (PP)2 | fPP | 0 | 523 | MHz | CL ≤ 30 pF Tolerance:+100KHz |
| Clock frequency Identification Mode (OD) | fOD | 0 | 400 | kHz | Tolerance: +20KHz |
| Clock high time | tWH | 6.5 |  | ns | CL ≤ 30 pF |
| Clock low time | tWL | 6.5 |  | ns | CL ≤ 30 pF |
| Clock rise time4 | tTLH |  | 3 | ns | CL ≤ 30 pF |
| Clock fall time | tTHL |  | 3 | ns | CL ≤ 30 pF |
| Inputs CMD, DAT (referenced to CLK) |  |  |  |  |  |
| Input set-up time | tISU | 3 |  | ns | CL ≤ 30 pF |
| Input hold time | tIH | 3 |  | ns | CL ≤ 30 pF |
| Outputs CMD, DAT (referenced to CLK) |  |  |  |  |  |
| Output delay time during data transfer | tODLY |  | 13.7 | ns | CL ≤ 30 pF |
| Output hold time | tOH | 2.5 |  | ns | CL ≤ 30 pF |
| Signal rise time5 | tRISE |  | 3 | ns | CL ≤ 30 pF |
| Signal fall time | tFALL |  | 3 | ns | CL ≤ 30 pF |
| Note1：CLK timing is measured at 50% of VDD. |  |  |  |  |  |
| Note2： eMMC™ shall support the full frequency range from 0-26Mhz or 0-52MHz |  |  |  |  |  |
| Note3：Device can operate as high-speed Device interface timing at 26 MHz clock frequency. |  |  |  |  |  |
| Note4：CLK rise and fall times are measured by min (VIH) and max (VIL). |  |  |  |  |  |
| Note5：Inputs CMD DAT rise and fall times are measured by min (VIH) and max (VIL) and outputs CMD DAT rise and |  |  |  |  |  |
| fall times are measured by min (VOH) and max (VOL). “ |  |  |  |  |  |

## Page 30 -- spec/parameter table

| Parameter | Symbol | Min | Max. | Unit | Remark1 |
|---|---|---|---|---|---|
| Clock CLK2 |  |  |  |  |  |
| Clock frequency Data Transfer Mode (PP)3 | fPP | 0 | 26 | MHz | CL ≤ 30 pF |
| Clock frequency Identification Mode (OD) | fOD | 0 | 400 | kHz |  |
| Clock high time | tWH | 10 |  |  | CL ≤ 30 pF |
| Clock low time | tWL | 10 |  | ns | CL ≤ 30 pF |
| Clock rise time4 | tTLH |  | 10 | ns | CL ≤ 30 pF |
| Clock fall time | tTHL |  | 10 | ns | CL ≤ 30 pF |
| Inputs CMD, DAT (referenced to CLK) |  |  |  |  |  |
| Input set-up time | tISU | 3 |  | ns | CL ≤ 30 pF |
| Input hold time | tIH | 3 |  | ns | CL ≤ 30 pF |
| Outputs CMD, DAT (referenced to CLK) |  |  |  |  |  |
| Output set-up time5 | tOSU | 11.7 |  | ns | CL ≤ 30 pF |
| Output hold time5 | tOH | 8.3 |  | ns | CL ≤ 30 pF |
| Note1：The Device must always start with the backward-compatible interface timing. The timing mode can be switched |  |  |  |  |  |
| to high-speed interface timing by the host sending the SWITCH command (CMD6) with the argument for high- |  |  |  |  |  |
| speed interface select. |  |  |  |  |  |
| Note2：CLK timing is measured at 50% of VDD. |  |  |  |  |  |

## Page 32 -- spec/parameter table

| Parameter | Symbol | Min | Max. | Unit | Remark |
|---|---|---|---|---|---|
| Input CLK1 |  |  |  |  |  |
| Clock duty cycle |  | 45 | 55 | % | Includes jitter, phase noise |
| Input DAT (referenced to CLK-DDR mode) |  |  |  |  |  |
| Input set-up time | tISUddr | 2.5 |  | ns | CL ≤ 20 pF |
| Input hold time | tIHddr | 2.5 |  | ns | CL ≤ 20 pF |
| Output DAT (referenced to CLK-DDR mode) |  |  |  |  |  |
| Output delay time during data transfer | tODLYddr | 1.5 | 7 | ns | CL ≤ 20 pF |
| Signal rise time (all signals)2 | tRISE |  | 2 | ns | CL ≤ 20 pF |
| Signal fall time (all signals) | tFALL |  | 2 | ns | CL ≤ 20 pF |
| Note1：CLK timing is measured at 50% of VDD. |  |  |  |  |  |
| Note2：Inputs CMD, DAT rise and fall times are measured by min (V ) and max (V ), and outputs CMD, DAT rise and |  |  |  |  |  |
| IH IL |  |  |  |  |  |
| fall times are measured by min (V ) and max (V ) |  |  |  |  |  |
| OH OL |  |  |  |  |  |

## Page 33 -- spec/parameter table

| Symbol | Min. | Max. | Unit | Remark |
|---|---|---|---|---|
| t PERIOD | 5 | - | ns | 200MHz (Max.), between rising edges |
| t , t TLH THL | - | 0.2* t PERIOD | ns | t , t < 1ns (max.) at 200MHz, C =12pF, The absolute TLH THL BGA maximum value of t , t is 10ns regardless of clock TLH THL frequency. |
| Duty Cycle | 30 | 70 | % |  |

## Page 33 -- spec/parameter table

| Symbol | Min. | Max. | Unit | Remark |
|---|---|---|---|---|
| t ISU | 1.4 | - | ns | C ≤ 6pF BGA |
| t IH | 0.8 |  | ns | C ≤ 6pF BGA |

## Page 34 -- spec/parameter table

| Symbol | Min. | Max. | Unit | Remark |
|---|---|---|---|---|
| t PH | 0 | 2 | UI | Device output momentary phase from CLK input to CMD or DAT lines output. Does not include a long term temperature drift. |
| ΔT PH | -350 (ΔT=-20°C) | +1550 (ΔT=90°C) | ps | Delay variation due to temperature change after tuning. Total allowable shift of output valid window (T ) from last system Tuning procedure ΔT is 2600ps for VW PH ΔT from -25°C to 125°C during operation. |
| T VW | 0.575 | - | UI | t =2.88ns at 200MHz Using test circuit in Figure 15 including skew among CMD VW and DAT lines created by the Device. Host path may add Signal Integrity induced noise, skews, etc. Expected T at Host input is larger than 0.475UI. VW |
| Note：Unit Interval (UI) is one bit nominal time. For example, UI=5ns at 200MHz. |  |  |  |  |

## Page 36 -- spec/parameter table

| Parameter | Symbol | Min | Max | Unit | Remark |
|---|---|---|---|---|---|
| Input CLK |  |  |  |  |  |
| Cycle time data transfer mode | tPERIOD | 5 |  |  | 200MHz(Max), between rising edges With respect to VT. |
| Slew rate | SR | 1.125 |  | V/ns | With respect to VIH/VIL. |
| Duty cycle distortion | tCKDCD | 0.0 | 0.3 | ns | Allowable deviation from an ideal 50% duty cycle. With respect to VT. Includes jitter, phase noise |
| Minimum pulse width | tCKMPW | 2.2 |  | ns | With respect to VT. |
| Input DAT (referenced to CLK) |  |  |  |  |  |
| Input set-up time | tISUddr | 0.4 |  | ns | CDevice ≤ 6pF With respect to VIH/VIL. |
| Input hold time | tIHddr | 0.4 |  | ns | CDevice ≤ 6pF With respect to VIH/VIL. |
| Slew rate | SR | 1.125 |  | V/ns | With respect to VIH/VIL. |

## Page 37 -- spec/parameter table

| Parameter | Symbol | Min | Max | Unit | Remark |
|---|---|---|---|---|---|
| Data Strobe |  |  |  |  |  |
| Cycle time data transfer mode | tPERIOD | 5 |  |  | 200MHz(Max), between rising edges With respect to VT |
| Slew rate | SR | 1.125 |  | V/ns | With respect to VOH/VOL and HS400 reference load |
| Duty cycle distortion | tDSDCD | 0.0 | 0.2 | ns | Allowable deviation from the input CLK duty cycle distortion (tCKDCD) With respect to VT Includes jitter, phase noise |
| Minimum pulse width | tDSMPW | 2.0 |  | ns | With respect to VT |
| Read pre-amble | tRPRE | 0.4 | - | tPERIOD | Max value is specified by manufacturer. Value up to infinite is valid |
| Read post-amble | tRPST | 0.4 | - | tPERIOD | Max value is specified by manufacturer. Value up to infinite is valid |
| Output DAT (referenced to Data Strobe) |  |  |  |  |  |
| Output skew | tRQ |  | 0.4 | ns | With respect to VOH/VOL and HS400 reference load |
| Output hold skew | tRQH |  | 0.4 | ns | With respect to VOH/VOL and HS400 reference load. |
| Slew rate | SR | 1.125 |  | V/ns | With respect to VOH/VOL and HS400 reference load |

## Page 38 -- spec/parameter table

| Parameter | Symbol | Min | Type | Max | Unit | Remark |
|---|---|---|---|---|---|---|
| Pull-up resistance for CMD | RCMD | 4.7 |  | 100(1) | Kohm |  |
| Pull-up resistance for DAT0-7 | RDAT | 10 |  | 100(1) | Kohm |  |
| Pull-down resistance for Data Strobe | RDS | 10 |  | 100(1) | Kohm |  |
| Internal pull up resistance DAT1- DAT7 | Rint | 10 |  | 150 | Kohm |  |
| Single Device capacitance | CDevice |  |  | 6 | pF |  |

## Page 42 -- spec/parameter table

|  | Parameter |  |  | Rating |  |  | Unit |  |  | Note |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Operating temperature |  |  | -25 ~ +85 |  |  | ℃ |  |  |  |  |  |
| Storage temperature |  |  | -55 ~ +125 |  |  | ℃ |  |  |  |  |  |

