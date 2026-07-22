# Netlist summary: Cradle.NET

**Source freshness:** Cradle.NET: exported 2026-07-21 23:42:13

Auto-generated. Deterministic parse of the Protel netlist + BOM -- no interpretation of intent, just what's actually wired. `floating` = single-pin net (rare, usually a real error). `unlabeled` = Altium auto-generated name, no manual net label placed (common on in-progress sheets, not necessarily wrong). Neither flag catches a pin with *no* net entry at all -- that requires comparing against a component's full pin table separately; see get_designator_pins() in netlist_parse.py. **A 'net doesn't exist' or 'pin has no connection' finding is indistinguishable from a stale export** -- re-export before trusting a missing-net report, and treat hierarchical port resolution (does a net label actually reach a matching Sheet Entry) as something only Altium's own ERC/Compile output can confirm, not this parser.

Components: 261. Nets: 548.

Single-pin nets: 392 total -- 335 deliberately named (`pending-port`: a real hierarchical port net, expected to be single-pin until the far sheet exists -- not a problem by itself), 36 on known staged/standard parts (`cradle_sidecar/data/altium/standard-parts.md` -- expected, excluded from review below), and 21 genuinely unexplained auto-named orphans -- these are the real candidates for review/No Connect.

## Orphaned pins (auto-named, no label, connects to nothing, not a known staged part -- review these)

| Net | Pin | Part | Sheet |
|---|---|---|---|
| NetANT1_2 | ANT1-2 | 2450AT18A100E | Cradle_Wireless |
| NetANT2_2 | ANT2-2 | 2450AT18A100E | Cradle_Wireless |
| NetJ1_5 | J1-5 | SM04B-GHS-TB(LF)(SN) | Cradle_Interfaces |
| NetJ1_6 | J1-6 | SM04B-GHS-TB(LF)(SN) | Cradle_Interfaces |
| NetSW1_5 | SW1-5 | JLC_KMR221GLFS | Cradle_Power_Charging |
| NetU10_10 | U10-10 | BQ25601RTWR | Cradle_Power_Charging |
| NetU10_8 | U10-8 | BQ25601RTWR | Cradle_Power_Charging |
| NetU2_12 | U2-12 | AP6275S | Cradle_Wireless |
| NetU2_24 | U2-24 | AP6275S | Cradle_Wireless |
| NetU2_37 | U2-37 | AP6275S | Cradle_Wireless |
| NetU2_44 | U2-44 | AP6275S | Cradle_Wireless |
| NetU2_45 | U2-45 | AP6275S | Cradle_Wireless |
| NetU2_46 | U2-46 | AP6275S | Cradle_Wireless |
| NetU2_47 | U2-47 | AP6275S | Cradle_Wireless |
| NetU2_48 | U2-48 | AP6275S | Cradle_Wireless |
| NetU6_2 | U6-2 | RK806S-5 | Cradle_Power_PMIC |
| NetU6_21 | U6-21 | RK806S-5 | Cradle_Power_PMIC |
| NetU6_3 | U6-3 | RK806S-5 | Cradle_Power_PMIC |
| NetU6_38 | U6-38 | RK806S-5 | Cradle_Power_PMIC |
| NetU6_48 | U6-48 | RK806S-5 | Cradle_Power_PMIC |
| NetU8_17 | U8-17 | HDMI-519S | Cradle_Interfaces |

## Pending-port nets (named, single-pin, waiting on a far sheet -- expected)

| Net | Pin | Sheet |
|---|---|---|
| WIRELESS_WL_REG_ON | U2-15 | Cradle_Wireless |
| WIRELESS_WL_HOST_WAKE | U2-16 | Cradle_Wireless |
| WIRELESS_WL_GPIO_11 | U2-35 | Cradle_Wireless |
| WIRELESS_WL_GPIO_10 | U2-33 | Cradle_Wireless |
| WIRELESS_BT_UART_TXD | U2-40 | Cradle_Wireless |
| WIRELESS_BT_UART_RXD | U2-41 | Cradle_Wireless |
| WIRELESS_BT_UART_RTS_N | U2-42 | Cradle_Wireless |
| WIRELESS_BT_UART_CTS_N | U2-43 | Cradle_Wireless |
| WIRELESS_BT_REG_ON | U2-38 | Cradle_Wireless |
| WIRELESS_BT_HOST_WAKE | U2-50 | Cradle_Wireless |
| WIRELESS_3V3 | U2-36 | Cradle_Wireless |
| VDU_CPU_BIG_3 | U6-49 | Cradle_Power_PMIC |
| USB2_D_8_P | D8-1 | Cradle_Interfaces |
| USB2_D_8_N | D8-2 | Cradle_Interfaces |
| USB1_D_8_P | D1-1 | Cradle_Interfaces |
| USB1_D_8_N | D1-2 | Cradle_Interfaces |
| SPK_SD_MODE | U9-A1 | Cradle_Audio |
| SPK_OUTP_8 | P2-1 | ambiguous(Cradle_Power_Charging, Cradle_Interfaces) |
| SPK_OUTP | U9-A3 | Cradle_Audio |
| SPK_OUTN_8 | P2-2 | ambiguous(Cradle_Power_Charging, Cradle_Interfaces) |
| SPK_OUTN | U9-B3 | Cradle_Audio |
| SPK_LRCLK | U9-C3 | Cradle_Audio |
| SPK_DIN | U9-B1 | Cradle_Audio |
| SPK_BCLK | U9-C1 | Cradle_Audio |
| SD_CLK | Card1-5 | Cradle_Storage |
| RESET_L | U6-40 | Cradle_Power_PMIC |
| PWRON_L | R13-1 | Cradle_Power_PMIC |
| PMIC_PWR_CTRL_2 | U6-61 | Cradle_Power_PMIC |
| PMIC_PWR_CTRL_1 | U6-62 | Cradle_Power_PMIC |
| PMIC_INT_L | U6-19 | Cradle_Power_PMIC |
| PMIC_EXT_EN_OUT | U6-39 | Cradle_Power_PMIC |
| NetUSB2_B8 | USB2-B8 | Cradle_Interfaces |
| NetUSB2_A8 | USB2-A8 | Cradle_Interfaces |
| NetUSB1_B8 | USB1-B8 | Cradle_Interfaces |
| NetUSB1_A8 | USB1-A8 | Cradle_Interfaces |
| NetU9_B2 | U9-B2 | Cradle_Audio |
| NetU5_K12 | U5-K12 | Cradle_Compute_Memory |
| NetU5_K10 | U5-K10 | Cradle_Compute_Memory |
| NetU5_K8 | U5-K8 | Cradle_Compute_Memory |
| NetU5_K5 | U5-K5 | Cradle_Compute_Memory |
| NetU5_K3 | U5-K3 | Cradle_Compute_Memory |
| NetU5_K1 | U5-K1 | Cradle_Compute_Memory |
| NetU5_J11 | U5-J11 | Cradle_Compute_Memory |
| NetU5_J9 | U5-J9 | Cradle_Compute_Memory |
| NetU5_J8 | U5-J8 | Cradle_Compute_Memory |
| NetU5_J5 | U5-J5 | Cradle_Compute_Memory |
| NetU5_J4 | U5-J4 | Cradle_Compute_Memory |
| NetU5_J2 | U5-J2 | Cradle_Compute_Memory |
| NetU5_H12 | U5-H12 | Cradle_Compute_Memory |
| NetU5_H11 | U5-H11 | Cradle_Compute_Memory |
| NetU5_H10 | U5-H10 | Cradle_Compute_Memory |
| NetU5_H9 | U5-H9 | Cradle_Compute_Memory |
| NetU5_H8 | U5-H8 | Cradle_Compute_Memory |
| NetU5_H5 | U5-H5 | Cradle_Compute_Memory |
| NetU5_H4 | U5-H4 | Cradle_Compute_Memory |
| NetU5_H3 | U5-H3 | Cradle_Compute_Memory |
| NetU5_H2 | U5-H2 | Cradle_Compute_Memory |
| NetU5_H1 | U5-H1 | Cradle_Compute_Memory |
| NetU5_G11 | U5-G11 | Cradle_Compute_Memory |
| NetU5_G9 | U5-G9 | Cradle_Compute_Memory |
| NetU5_G4 | U5-G4 | Cradle_Compute_Memory |
| NetU5_G2 | U5-G2 | Cradle_Compute_Memory |
| NetU5_F12 | U5-F12 | Cradle_Compute_Memory |
| NetU5_F11 | U5-F11 | Cradle_Compute_Memory |
| NetU5_F10 | U5-F10 | Cradle_Compute_Memory |
| NetU5_F9 | U5-F9 | Cradle_Compute_Memory |
| NetU5_F8 | U5-F8 | Cradle_Compute_Memory |
| NetU5_F5 | U5-F5 | Cradle_Compute_Memory |
| NetU5_F4 | U5-F4 | Cradle_Compute_Memory |
| NetU5_F3 | U5-F3 | Cradle_Compute_Memory |
| NetU5_F2 | U5-F2 | Cradle_Compute_Memory |
| NetU5_F1 | U5-F1 | Cradle_Compute_Memory |
| NetU5_E11 | U5-E11 | Cradle_Compute_Memory |
| NetU5_E10 | U5-E10 | Cradle_Compute_Memory |
| NetU5_E9 | U5-E9 | Cradle_Compute_Memory |
| NetU5_E4 | U5-E4 | Cradle_Compute_Memory |
| NetU5_E3 | U5-E3 | Cradle_Compute_Memory |
| NetU5_E2 | U5-E2 | Cradle_Compute_Memory |
| NetU5_D12 | U5-D12 | Cradle_Compute_Memory |
| NetU5_D10 | U5-D10 | Cradle_Compute_Memory |
| NetU5_D8 | U5-D8 | Cradle_Compute_Memory |
| NetU5_D5 | U5-D5 | Cradle_Compute_Memory |
| NetU5_D3 | U5-D3 | Cradle_Compute_Memory |
| NetU5_D1 | U5-D1 | Cradle_Compute_Memory |
| NetU5_C11 | U5-C11 | Cradle_Compute_Memory |
| NetU5_C10 | U5-C10 | Cradle_Compute_Memory |
| NetU5_C9 | U5-C9 | Cradle_Compute_Memory |
| NetU5_C4 | U5-C4 | Cradle_Compute_Memory |
| NetU5_C3 | U5-C3 | Cradle_Compute_Memory |
| NetU5_C2 | U5-C2 | Cradle_Compute_Memory |
| NetU5_B12 | U5-B12 | Cradle_Compute_Memory |
| NetU5_B11 | U5-B11 | Cradle_Compute_Memory |
| NetU5_B10 | U5-B10 | Cradle_Compute_Memory |
| NetU5_B9 | U5-B9 | Cradle_Compute_Memory |
| NetU5_B8 | U5-B8 | Cradle_Compute_Memory |
| NetU5_B5 | U5-B5 | Cradle_Compute_Memory |
| NetU5_B4 | U5-B4 | Cradle_Compute_Memory |
| NetU5_B3 | U5-B3 | Cradle_Compute_Memory |
| NetU5_B2 | U5-B2 | Cradle_Compute_Memory |
| NetU5_B1 | U5-B1 | Cradle_Compute_Memory |
| NetU5_A12 | U5-A12 | Cradle_Compute_Memory |
| NetU5_A11 | U5-A11 | Cradle_Compute_Memory |
| NetU5_A9 | U5-A9 | Cradle_Compute_Memory |
| NetU5_A8 | U5-A8 | Cradle_Compute_Memory |
| NetU5_A5 | U5-A5 | Cradle_Compute_Memory |
| NetU5_A4 | U5-A4 | Cradle_Compute_Memory |
| NetU5_A2 | U5-A2 | Cradle_Compute_Memory |
| NetU5_A1 | U5-A1 | Cradle_Compute_Memory |
| NetU3_P14 | U3-P14 | Cradle_Storage |
| NetU3_P13 | U3-P13 | Cradle_Storage |
| NetU3_P12 | U3-P12 | Cradle_Storage |
| NetU3_P11 | U3-P11 | Cradle_Storage |
| NetU3_P10 | U3-P10 | Cradle_Storage |
| NetU3_P9 | U3-P9 | Cradle_Storage |
| NetU3_P8 | U3-P8 | Cradle_Storage |
| NetU3_P7 | U3-P7 | Cradle_Storage |
| NetU3_P2 | U3-P2 | Cradle_Storage |
| NetU3_P1 | U3-P1 | Cradle_Storage |
| NetU3_N14 | U3-N14 | Cradle_Storage |
| NetU3_N13 | U3-N13 | Cradle_Storage |
| NetU3_N12 | U3-N12 | Cradle_Storage |
| NetU3_N11 | U3-N11 | Cradle_Storage |
| NetU3_N10 | U3-N10 | Cradle_Storage |
| NetU3_N9 | U3-N9 | Cradle_Storage |
| NetU3_N8 | U3-N8 | Cradle_Storage |
| NetU3_N7 | U3-N7 | Cradle_Storage |
| NetU3_N6 | U3-N6 | Cradle_Storage |
| NetU3_N3 | U3-N3 | Cradle_Storage |
| NetU3_N1 | U3-N1 | Cradle_Storage |
| NetU3_M14 | U3-M14 | Cradle_Storage |
| NetU3_M13 | U3-M13 | Cradle_Storage |
| NetU3_M12 | U3-M12 | Cradle_Storage |
| NetU3_M11 | U3-M11 | Cradle_Storage |
| NetU3_M10 | U3-M10 | Cradle_Storage |
| NetU3_M9 | U3-M9 | Cradle_Storage |
| NetU3_M8 | U3-M8 | Cradle_Storage |
| NetU3_M7 | U3-M7 | Cradle_Storage |
| NetU3_M3 | U3-M3 | Cradle_Storage |
| NetU3_M2 | U3-M2 | Cradle_Storage |
| NetU3_M1 | U3-M1 | Cradle_Storage |
| NetU3_L14 | U3-L14 | Cradle_Storage |
| NetU3_L13 | U3-L13 | Cradle_Storage |
| NetU3_L12 | U3-L12 | Cradle_Storage |
| NetU3_L3 | U3-L3 | Cradle_Storage |
| NetU3_L2 | U3-L2 | Cradle_Storage |
| NetU3_L1 | U3-L1 | Cradle_Storage |
| NetU3_K14 | U3-K14 | Cradle_Storage |
| NetU3_K13 | U3-K13 | Cradle_Storage |
| NetU3_K12 | U3-K12 | Cradle_Storage |
| NetU3_K10 | U3-K10 | Cradle_Storage |
| NetU3_K7 | U3-K7 | Cradle_Storage |
| NetU3_K6 | U3-K6 | Cradle_Storage |
| NetU3_K3 | U3-K3 | Cradle_Storage |
| NetU3_K2 | U3-K2 | Cradle_Storage |
| NetU3_K1 | U3-K1 | Cradle_Storage |
| NetU3_J14 | U3-J14 | Cradle_Storage |
| NetU3_J13 | U3-J13 | Cradle_Storage |
| NetU3_J12 | U3-J12 | Cradle_Storage |
| NetU3_J3 | U3-J3 | Cradle_Storage |
| NetU3_J2 | U3-J2 | Cradle_Storage |
| NetU3_J1 | U3-J1 | Cradle_Storage |
| NetU3_H14 | U3-H14 | Cradle_Storage |
| NetU3_H13 | U3-H13 | Cradle_Storage |
| NetU3_H12 | U3-H12 | Cradle_Storage |
| NetU3_H3 | U3-H3 | Cradle_Storage |
| NetU3_H2 | U3-H2 | Cradle_Storage |
| NetU3_H1 | U3-H1 | Cradle_Storage |
| NetU3_G14 | U3-G14 | Cradle_Storage |
| NetU3_G13 | U3-G13 | Cradle_Storage |
| NetU3_G12 | U3-G12 | Cradle_Storage |
| NetU3_G10 | U3-G10 | Cradle_Storage |
| NetU3_G3 | U3-G3 | Cradle_Storage |
| NetU3_G2 | U3-G2 | Cradle_Storage |
| NetU3_G1 | U3-G1 | Cradle_Storage |
| NetU3_F14 | U3-F14 | Cradle_Storage |
| NetU3_F13 | U3-F13 | Cradle_Storage |
| NetU3_F12 | U3-F12 | Cradle_Storage |
| NetU3_F10 | U3-F10 | Cradle_Storage |
| NetU3_F3 | U3-F3 | Cradle_Storage |
| NetU3_F2 | U3-F2 | Cradle_Storage |
| NetU3_F1 | U3-F1 | Cradle_Storage |
| NetU3_E14 | U3-E14 | Cradle_Storage |
| NetU3_E13 | U3-E13 | Cradle_Storage |
| NetU3_E12 | U3-E12 | Cradle_Storage |
| NetU3_E10 | U3-E10 | Cradle_Storage |
| NetU3_E9 | U3-E9 | Cradle_Storage |
| NetU3_E8 | U3-E8 | Cradle_Storage |
| NetU3_E5 | U3-E5 | Cradle_Storage |
| NetU3_E3 | U3-E3 | Cradle_Storage |
| NetU3_E2 | U3-E2 | Cradle_Storage |
| NetU3_E1 | U3-E1 | Cradle_Storage |
| NetU3_D14 | U3-D14 | Cradle_Storage |
| NetU3_D13 | U3-D13 | Cradle_Storage |
| NetU3_D12 | U3-D12 | Cradle_Storage |
| NetU3_D4 | U3-D4 | Cradle_Storage |
| NetU3_D3 | U3-D3 | Cradle_Storage |
| NetU3_D2 | U3-D2 | Cradle_Storage |
| NetU3_D1 | U3-D1 | Cradle_Storage |
| NetU3_C14 | U3-C14 | Cradle_Storage |
| NetU3_C13 | U3-C13 | Cradle_Storage |
| NetU3_C12 | U3-C12 | Cradle_Storage |
| NetU3_C11 | U3-C11 | Cradle_Storage |
| NetU3_C10 | U3-C10 | Cradle_Storage |
| NetU3_C9 | U3-C9 | Cradle_Storage |
| NetU3_C8 | U3-C8 | Cradle_Storage |
| NetU3_C7 | U3-C7 | Cradle_Storage |
| NetU3_C5 | U3-C5 | Cradle_Storage |
| NetU3_C3 | U3-C3 | Cradle_Storage |
| NetU3_C1 | U3-C1 | Cradle_Storage |
| NetU3_B14 | U3-B14 | Cradle_Storage |
| NetU3_B13 | U3-B13 | Cradle_Storage |
| NetU3_B12 | U3-B12 | Cradle_Storage |
| NetU3_B11 | U3-B11 | Cradle_Storage |
| NetU3_B10 | U3-B10 | Cradle_Storage |
| NetU3_B9 | U3-B9 | Cradle_Storage |
| NetU3_B8 | U3-B8 | Cradle_Storage |
| NetU3_B7 | U3-B7 | Cradle_Storage |
| NetU3_B1 | U3-B1 | Cradle_Storage |
| NetU3_A14 | U3-A14 | Cradle_Storage |
| NetU3_A13 | U3-A13 | Cradle_Storage |
| NetU3_A12 | U3-A12 | Cradle_Storage |
| NetU3_A11 | U3-A11 | Cradle_Storage |
| NetU3_A10 | U3-A10 | Cradle_Storage |
| NetU3_A9 | U3-A9 | Cradle_Storage |
| NetU3_A8 | U3-A8 | Cradle_Storage |
| NetU3_A7 | U3-A7 | Cradle_Storage |
| NetU3_A2 | U3-A2 | Cradle_Storage |
| NetU3_A1 | U3-A1 | Cradle_Storage |
| NetU1_N29 | U1-N29 | Cradle_Compute_SOC |
| NetU1_N28 | U1-N28 | Cradle_Compute_SOC |
| NetU1_N1 | U1-N1 | Cradle_Compute_SOC |
| NetU1_M29 | U1-M29 | Cradle_Compute_SOC |
| NetU1_M28 | U1-M28 | Cradle_Compute_SOC |
| NetU1_L29 | U1-L29 | Cradle_Compute_SOC |
| NetU1_L28 | U1-L28 | Cradle_Compute_SOC |
| NetU1_L1 | U1-L1 | Cradle_Compute_SOC |
| NetU1_K29 | U1-K29 | Cradle_Compute_SOC |
| NetU1_K28 | U1-K28 | Cradle_Compute_SOC |
| NetU1_K1 | U1-K1 | Cradle_Compute_SOC |
| NetU1_J29 | U1-J29 | Cradle_Compute_SOC |
| NetU1_J28 | U1-J28 | Cradle_Compute_SOC |
| NetU1_H29 | U1-H29 | Cradle_Compute_SOC |
| NetU1_H28 | U1-H28 | Cradle_Compute_SOC |
| NetU1_H1 | U1-H1 | Cradle_Compute_SOC |
| NetU1_G29 | U1-G29 | Cradle_Compute_SOC |
| NetU1_G28 | U1-G28 | Cradle_Compute_SOC |
| NetU1_G1 | U1-G1 | Cradle_Compute_SOC |
| NetU1_F28 | U1-F28 | Cradle_Compute_SOC |
| NetU1_E29 | U1-E29 | Cradle_Compute_SOC |
| NetU1_E28 | U1-E28 | Cradle_Compute_SOC |
| NetU1_E1 | U1-E1 | Cradle_Compute_SOC |
| NetU1_D28 | U1-D28 | Cradle_Compute_SOC |
| NetU1_D1 | U1-D1 | Cradle_Compute_SOC |
| NetU1_C29 | U1-C29 | Cradle_Compute_SOC |
| NetU1_C28 | U1-C28 | Cradle_Compute_SOC |
| NetU1_C1 | U1-C1 | Cradle_Compute_SOC |
| NetU1_B29 | U1-B29 | Cradle_Compute_SOC |
| NetU1_B28 | U1-B28 | Cradle_Compute_SOC |
| NetU1_B27 | U1-B27 | Cradle_Compute_SOC |
| NetU1_B26 | U1-B26 | Cradle_Compute_SOC |
| NetU1_B25 | U1-B25 | Cradle_Compute_SOC |
| NetU1_B24 | U1-B24 | Cradle_Compute_SOC |
| NetU1_B23 | U1-B23 | Cradle_Compute_SOC |
| NetU1_B22 | U1-B22 | Cradle_Compute_SOC |
| NetU1_B21 | U1-B21 | Cradle_Compute_SOC |
| NetU1_B20 | U1-B20 | Cradle_Compute_SOC |
| NetU1_B19 | U1-B19 | Cradle_Compute_SOC |
| NetU1_B18 | U1-B18 | Cradle_Compute_SOC |
| NetU1_B17 | U1-B17 | Cradle_Compute_SOC |
| NetU1_B16 | U1-B16 | Cradle_Compute_SOC |
| NetU1_B15 | U1-B15 | Cradle_Compute_SOC |
| NetU1_B14 | U1-B14 | Cradle_Compute_SOC |
| NetU1_B13 | U1-B13 | Cradle_Compute_SOC |
| NetU1_B12 | U1-B12 | Cradle_Compute_SOC |
| NetU1_B11 | U1-B11 | Cradle_Compute_SOC |
| NetU1_B10 | U1-B10 | Cradle_Compute_SOC |
| NetU1_B9 | U1-B9 | Cradle_Compute_SOC |
| NetU1_B8 | U1-B8 | Cradle_Compute_SOC |
| NetU1_B7 | U1-B7 | Cradle_Compute_SOC |
| NetU1_B6 | U1-B6 | Cradle_Compute_SOC |
| NetU1_B5 | U1-B5 | Cradle_Compute_SOC |
| NetU1_B4 | U1-B4 | Cradle_Compute_SOC |
| NetU1_B3 | U1-B3 | Cradle_Compute_SOC |
| NetU1_B2 | U1-B2 | Cradle_Compute_SOC |
| NetU1_B1 | U1-B1 | Cradle_Compute_SOC |
| NetU1_A29 | U1-A29 | Cradle_Compute_SOC |
| NetU1_A28 | U1-A28 | Cradle_Compute_SOC |
| NetU1_A27 | U1-A27 | Cradle_Compute_SOC |
| NetU1_A26 | U1-A26 | Cradle_Compute_SOC |
| NetU1_A25 | U1-A25 | Cradle_Compute_SOC |
| NetU1_A23 | U1-A23 | Cradle_Compute_SOC |
| NetU1_A21 | U1-A21 | Cradle_Compute_SOC |
| NetU1_A19 | U1-A19 | Cradle_Compute_SOC |
| NetU1_A17 | U1-A17 | Cradle_Compute_SOC |
| NetU1_A15 | U1-A15 | Cradle_Compute_SOC |
| NetU1_A13 | U1-A13 | Cradle_Compute_SOC |
| NetU1_A11 | U1-A11 | Cradle_Compute_SOC |
| NetU1_A9 | U1-A9 | Cradle_Compute_SOC |
| NetU1_A7 | U1-A7 | Cradle_Compute_SOC |
| NetU1_A5 | U1-A5 | Cradle_Compute_SOC |
| NetU1_A4 | U1-A4 | Cradle_Compute_SOC |
| NetU1_A3 | U1-A3 | Cradle_Compute_SOC |
| NetU1_A2 | U1-A2 | Cradle_Compute_SOC |
| NetU1_A1 | U1-A1 | Cradle_Compute_SOC |
| I2C1_SDA_M0_RK806 | U6-15 | Cradle_Power_PMIC |
| I2C1_SCL_M0_RK806 | U6-17 | Cradle_Power_PMIC |
| HDMI_D2_P | D5-1 | Cradle_Interfaces |
| HDMI_D2_N | D5-2 | Cradle_Interfaces |
| HDMI_D1_P | D4-1 | Cradle_Interfaces |
| HDMI_D1_N | D4-2 | Cradle_Interfaces |
| HDMI_D0_P | D6-1 | Cradle_Interfaces |
| HDMI_D0_N | D6-2 | Cradle_Interfaces |
| HDMI_CLK_P | D7-1 | Cradle_Interfaces |
| HDMI_CLK_N | D7-2 | Cradle_Interfaces |
| EXP_SPI_SCK | FPC1-11 | Cradle_Interfaces |
| EXP_SPI_MOSI | FPC1-12 | Cradle_Interfaces |
| EXP_SPI_MISO | FPC1-13 | Cradle_Interfaces |
| EXP_SPI_CSN | FPC1-14 | Cradle_Interfaces |
| EXP_GPIO10 | FPC1-27 | Cradle_Interfaces |
| EXP_GPIO9 | FPC1-26 | Cradle_Interfaces |
| EXP_GPIO8 | FPC1-22 | Cradle_Interfaces |
| EXP_GPIO7 | FPC1-21 | Cradle_Interfaces |
| EXP_GPIO6 | FPC1-20 | Cradle_Interfaces |
| EXP_GPIO5 | FPC1-19 | Cradle_Interfaces |
| EXP_GPIO4 | FPC1-6 | Cradle_Interfaces |
| EXP_GPIO3 | FPC1-5 | Cradle_Interfaces |
| EXP_GPIO2 | FPC1-4 | Cradle_Interfaces |
| EXP_GPIO1 | FPC1-3 | Cradle_Interfaces |
| EMMC_DS_TOGGLE | Q2-1 | ambiguous(Cradle_Storage, Cradle_Interfaces) |
| EMMC_CLK | U3-M6 | Cradle_Storage |
| DEBUG_TX | J1-2 | Cradle_Interfaces |
| DEBUG_RX | J1-3 | Cradle_Interfaces |
| CAM_PWDN | U15-2 | Cradle_Interfaces |
| BQ_PSEL | U10-2 | Cradle_Power_Charging |
| BQ_CE | U10-9 | Cradle_Power_Charging |

## All nets

| Net | Pins | Flags |
|---|---|---|
| AUDIO_3V3 | C76-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C79-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), MIC1-5(MMICT390200012@Cradle_Audio), MIC2-2(MMICT390200012@Cradle_Audio), MIC2-5(MMICT390200012@Cradle_Audio) | - |
| AUDIO_5V | C77-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C78-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), U9-A2(MAX98357AEWL+T@Cradle_Audio) | - |
| BQ_CE | U10-9(BQ25601RTWR@Cradle_Power_Charging) | pending-port |
| BQ_INT | R3-2(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U10-7(BQ25601RTWR@Cradle_Power_Charging) | - |
| BQ_PSEL | U10-2(BQ25601RTWR@Cradle_Power_Charging) | pending-port |
| BQ_SCL | R1-2(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U10-5(BQ25601RTWR@Cradle_Power_Charging) | - |
| BQ_SDA | R2-2(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U10-6(BQ25601RTWR@Cradle_Power_Charging) | - |
| BQ_VBUS | C1-1(GRM188C61E226ME01J@Cradle_Power_Charging), C2-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), D2-1(PESD5V0S1BA,115@Cradle_Power_Charging), U10-1(BQ25601RTWR@Cradle_Power_Charging), U10-24(BQ25601RTWR@Cradle_Power_Charging) | - |
| BQ_VREF | R1-1(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R2-1(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R3-1(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | - |
| CAM_MCLK | D20-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-5(JLC_05A20L22P@Cradle_Interfaces) | - |
| CAM_PWDN | U15-2(SN74LV1T125DCKR@Cradle_Interfaces) | pending-port |
| CAM_SCL | D21-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-3(JLC_05A20L22P@Cradle_Interfaces) | - |
| CAM_SDA | D22-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-2(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_CLK_N | D13-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-15(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_CLK_P | D14-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-14(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_D0_N | D15-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-12(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_D0_P | D16-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-11(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_D1_N | D17-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-9(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_D1_P | D18-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-8(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_D2_N | D9-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-21(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_D2_P | D10-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-20(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_D3_N | D11-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-18(JLC_05A20L22P@Cradle_Interfaces) | - |
| CSI0_D3_P | D12-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-17(JLC_05A20L22P@Cradle_Interfaces) | - |
| DEBUG_RX | J1-3(SM04B-GHS-TB(LF)(SN)@Cradle_Interfaces) | pending-port |
| DEBUG_TX | J1-2(SM04B-GHS-TB(LF)(SN)@Cradle_Interfaces) | pending-port |
| EMMC_CLK | U3-M6(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| EMMC_CMD | R51-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-M5(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_D0 | R52-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-A3(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_D1 | R53-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-A4(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_D2 | R54-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-A5(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_D3 | R55-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-B2(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_D4 | R56-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-B3(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_D5 | R57-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-B4(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_D6 | R58-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-B5(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_D7 | R59-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-B6(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_DS | R61-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-H5(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EMMC_DS_TOGGLE | Q2-1(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)) | pending-port |
| EMMC_RST_N | R60-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-K5(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| EXP_GPIO1 | FPC1-3(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO10 | FPC1-27(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO2 | FPC1-4(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO3 | FPC1-5(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO4 | FPC1-6(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO5 | FPC1-19(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO6 | FPC1-20(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO7 | FPC1-21(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO8 | FPC1-22(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_GPIO9 | FPC1-26(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_I2C_SCL | D23-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC1-8(FC-05D30P11H20@Cradle_Interfaces) | - |
| EXP_I2C_SDA | D24-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC1-9(FC-05D30P11H20@Cradle_Interfaces) | - |
| EXP_SPI_CSN | FPC1-14(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_SPI_MISO | FPC1-13(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_SPI_MOSI | FPC1-12(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_SPI_SCK | FPC1-11(FC-05D30P11H20@Cradle_Interfaces) | pending-port |
| EXP_UART_RX | D26-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC1-17(FC-05D30P11H20@Cradle_Interfaces) | - |
| EXP_UART_TX | D25-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC1-16(FC-05D30P11H20@Cradle_Interfaces) | - |
| GND | C1-2(GRM188C61E226ME01J@Cradle_Power_Charging), C2-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C3-2(885012106031@Cradle_Power_Charging), C4-2(CC0402MRX5R7BB475@Cradle_Power_Charging), C6-2(885012106031@Cradle_Power_Charging), C7-2(885012106031@Cradle_Power_Charging), C15-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C16-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C17-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C18-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C19-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C20-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C21-1(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C23-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C24-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C26-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C27-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C28-1(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C29-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C31-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C32-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C33-1(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C34-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C35-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C36-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C38-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C39-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C40-1(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C41-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C42-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C43-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C44-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C45-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C46-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C47-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C48-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C49-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C50-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C52-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C53-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C54-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C55-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C56-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C57-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C58-1(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C59-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C60-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C61-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C62-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C63-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C64-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C65-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C67-2(JLC_0402B102K500NT@Cradle_Power_PMIC), C68-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C70-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C71-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C72-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C74-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C75-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C76-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C77-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C78-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C79-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C81-1(JLC_30pF_0402CG300J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), C82-1(JLC_30pF_0402CG300J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), C86-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C87-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C89-2(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C90-2(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C91-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C92-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C93-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C94-2(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C95-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C96-2(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C97-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C98-2(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C99-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C100-2(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C101-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C102-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C103-2(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C104-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C105-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C106-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C107-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C108-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C109-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C110-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C111-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C112-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), Card1-6(TF-01A@Cradle_Storage), Card1-10(TF-01A@Cradle_Storage), Card1-11(TF-01A@Cradle_Storage), Card1-12(TF-01A@Cradle_Storage), Card1-13(TF-01A@Cradle_Storage), D2-2(PESD5V0S1BA,115@Cradle_Power_Charging), D3-2(JLC_SD103AX@Cradle_Power_PMIC), D9-C(ESD9L5.0ST5G@Cradle_Interfaces), D10-C(ESD9L5.0ST5G@Cradle_Interfaces), D11-C(ESD9L5.0ST5G@Cradle_Interfaces), D12-C(ESD9L5.0ST5G@Cradle_Interfaces), D13-C(ESD9L5.0ST5G@Cradle_Interfaces), D14-C(ESD9L5.0ST5G@Cradle_Interfaces), D15-C(ESD9L5.0ST5G@Cradle_Interfaces), D16-C(ESD9L5.0ST5G@Cradle_Interfaces), D17-C(ESD9L5.0ST5G@Cradle_Interfaces), D18-C(ESD9L5.0ST5G@Cradle_Interfaces), D19-C(ESD9L5.0ST5G@Cradle_Interfaces), D20-C(ESD9L5.0ST5G@Cradle_Interfaces), D21-C(ESD9L5.0ST5G@Cradle_Interfaces), D22-C(ESD9L5.0ST5G@Cradle_Interfaces), D23-C(ESD9L5.0ST5G@Cradle_Interfaces), D24-C(ESD9L5.0ST5G@Cradle_Interfaces), D25-C(ESD9L5.0ST5G@Cradle_Interfaces), D26-C(ESD9L5.0ST5G@Cradle_Interfaces), FPC1-1(FC-05D30P11H20@Cradle_Interfaces), FPC1-7(FC-05D30P11H20@Cradle_Interfaces), FPC1-10(FC-05D30P11H20@Cradle_Interfaces), FPC1-15(FC-05D30P11H20@Cradle_Interfaces), FPC1-18(FC-05D30P11H20@Cradle_Interfaces), FPC1-23(FC-05D30P11H20@Cradle_Interfaces), FPC1-25(FC-05D30P11H20@Cradle_Interfaces), FPC1-28(FC-05D30P11H20@Cradle_Interfaces), FPC1-29(FC-05D30P11H20@Cradle_Interfaces), FPC1-30(FC-05D30P11H20@Cradle_Interfaces), FPC1-31(FC-05D30P11H20@Cradle_Interfaces), FPC1-32(FC-05D30P11H20@Cradle_Interfaces), FPC2-4(JLC_05A20L22P@Cradle_Interfaces), FPC2-7(JLC_05A20L22P@Cradle_Interfaces), FPC2-10(JLC_05A20L22P@Cradle_Interfaces), FPC2-13(JLC_05A20L22P@Cradle_Interfaces), FPC2-16(JLC_05A20L22P@Cradle_Interfaces), FPC2-19(JLC_05A20L22P@Cradle_Interfaces), FPC2-22(JLC_05A20L22P@Cradle_Interfaces), FPC2-23(JLC_05A20L22P@Cradle_Interfaces), FPC2-24(JLC_05A20L22P@Cradle_Interfaces), J1-4(SM04B-GHS-TB(LF)(SN)@Cradle_Interfaces), MIC1-2(MMICT390200012@Cradle_Audio), MIC1-3(MMICT390200012@Cradle_Audio), MIC2-3(MMICT390200012@Cradle_Audio), P1-2(S2B-PH-K-S(LF)(SN)@ambiguous(Cradle_Power_Charging, Cradle_Interfaces)), Q1-1(DMP2035U-7@Cradle_Power_Charging), Q2-3(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), Q6-3(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R7-2(103AT-2@Cradle_Power_Charging), R8-2(RT0402FRE0730K1L@Cradle_Power_Charging), R11-2(AC0402JR-13100KL@Cradle_Power_PMIC), R18-2(AC0402JR-13100KL@Cradle_Power_PMIC), R20-2(CRG0402F200K@Cradle_Power_PMIC), R24-2(AC0402JR-13100KL@Cradle_Power_PMIC), R71-2(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), R72-2(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), R73-2(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), R74-2(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), SW1-3(JLC_KMR221GLFS@Cradle_Power_Charging), SW1-4(JLC_KMR221GLFS@Cradle_Power_Charging), U2-1(AP6275S@Cradle_Wireless), U2-3(AP6275S@Cradle_Wireless), U2-4(AP6275S@Cradle_Wireless), U2-5(AP6275S@Cradle_Wireless), U2-6(AP6275S@Cradle_Wireless), U2-7(AP6275S@Cradle_Wireless), U2-8(AP6275S@Cradle_Wireless), U2-10(AP6275S@Cradle_Wireless), U2-11(AP6275S@Cradle_Wireless), U2-23(AP6275S@Cradle_Wireless), U2-27(AP6275S@Cradle_Wireless), U2-30(AP6275S@Cradle_Wireless), U2-32(AP6275S@Cradle_Wireless), U2-39(AP6275S@Cradle_Wireless), U3-A6(EMMC04G-M627-Y02U@Cradle_Storage), U3-C4(EMMC04G-M627-Y02U@Cradle_Storage), U3-E7(EMMC04G-M627-Y02U@Cradle_Storage), U3-G5(EMMC04G-M627-Y02U@Cradle_Storage), U3-H10(EMMC04G-M627-Y02U@Cradle_Storage), U3-J5(EMMC04G-M627-Y02U@Cradle_Storage), U3-K8(EMMC04G-M627-Y02U@Cradle_Storage), U3-N2(EMMC04G-M627-Y02U@Cradle_Storage), U3-N5(EMMC04G-M627-Y02U@Cradle_Storage), U3-P4(EMMC04G-M627-Y02U@Cradle_Storage), U3-P6(EMMC04G-M627-Y02U@Cradle_Storage), U5-A3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-A10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-C1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-C5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-C8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-C12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-D2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-D4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-D9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-D11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-E1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-E5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-E8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-E12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-G1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-G3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-G5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-G8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-G10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-G12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-J1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-J3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-J10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-J12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-K2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-K4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-K9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U5-K11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory), U6-69(RK806S-5@Cradle_Power_PMIC), U8-1(HDMI-519S@Cradle_Interfaces), U8-4(HDMI-519S@Cradle_Interfaces), U8-7(HDMI-519S@Cradle_Interfaces), U8-10(HDMI-519S@Cradle_Interfaces), U8-13(HDMI-519S@Cradle_Interfaces), U8-20(HDMI-519S@Cradle_Interfaces), U8-21(HDMI-519S@Cradle_Interfaces), U8-22(HDMI-519S@Cradle_Interfaces), U8-23(HDMI-519S@Cradle_Interfaces), U9-C2(MAX98357AEWL+T@Cradle_Audio), U10-17(BQ25601RTWR@Cradle_Power_Charging), U10-18(BQ25601RTWR@Cradle_Power_Charging), U10-25(BQ25601RTWR@Cradle_Power_Charging), U14-1(JLC_32.768KHz_SIT1552AI-JF-DCC-32.768D@Cradle_Wireless), U14-4(JLC_32.768KHz_SIT1552AI-JF-DCC-32.768D@Cradle_Wireless), U15-1(SN74LV1T125DCKR@Cradle_Interfaces), U15-3(SN74LV1T125DCKR@Cradle_Interfaces), USB1-0(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB1-A1(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB1-A12(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB2-0(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB2-A1(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB2-A12(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), X1-2(JLC_37.4_MHz_7M37470001@Cradle_Wireless), X1-4(JLC_37.4_MHz_7M37470001@Cradle_Wireless) | - |
| HDMI_CEC | Q3-2(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R64-1(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)) | - |
| HDMI_CLK_N | D7-2(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| HDMI_CLK_P | D7-1(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| HDMI_CLK_PROC_8_N | D7-3(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), U8-12(HDMI-519S@Cradle_Interfaces) | - |
| HDMI_CLK_PROC_8_P | D7-4(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), U8-11(HDMI-519S@Cradle_Interfaces) | - |
| HDMI_D0_N | D6-2(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| HDMI_D0_P | D6-1(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| HDMI_D0_PROC_8_N | D6-3(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), U8-9(HDMI-519S@Cradle_Interfaces) | - |
| HDMI_D0_PROC_8_P | D6-4(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), U8-8(HDMI-519S@Cradle_Interfaces) | - |
| HDMI_D1_N | D4-2(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| HDMI_D1_P | D4-1(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| HDMI_D1_PROC_8_N | D4-3(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), U8-6(HDMI-519S@Cradle_Interfaces) | - |
| HDMI_D1_PROC_8_P | D4-4(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), U8-5(HDMI-519S@Cradle_Interfaces) | - |
| HDMI_D2_N | D5-2(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| HDMI_D2_P | D5-1(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| HDMI_D2_PROC_8_N | D5-3(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), U8-3(HDMI-519S@Cradle_Interfaces) | - |
| HDMI_D2_PROC_8_P | D5-4(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), U8-2(HDMI-519S@Cradle_Interfaces) | - |
| HDMI_HPD | Q6-2(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R69-1(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)) | - |
| HDMI_SCL | Q4-2(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R65-1(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)) | - |
| HDMI_SDA | Q5-2(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R68-1(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)) | - |
| I2C1_SCL_M0_RK806 | U6-17(RK806S-5@Cradle_Power_PMIC) | pending-port |
| I2C1_SDA_M0_RK806 | U6-15(RK806S-5@Cradle_Power_PMIC) | pending-port |
| INTERFACES_3V3 | C112-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), FPC1-2(FC-05D30P11H20@Cradle_Interfaces), FPC1-24(FC-05D30P11H20@Cradle_Interfaces), FPC2-1(JLC_05A20L22P@Cradle_Interfaces), J1-1(SM04B-GHS-TB(LF)(SN)@Cradle_Interfaces), Q3-1(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), Q4-1(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), Q5-1(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R64-2(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), R65-2(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), R68-2(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), R69-2(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), U15-5(SN74LV1T125DCKR@Cradle_Interfaces) | - |
| INTERFACES_5V | R63-2(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), R66-2(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), R67-2(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), U8-18(HDMI-519S@Cradle_Interfaces), USB1-A4(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB1-A9(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB2-A4(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB2-A9(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| MIC_CLK | MIC1-4(MMICT390200012@Cradle_Audio), MIC2-4(MMICT390200012@Cradle_Audio) | - |
| MIC_DATA | MIC1-1(MMICT390200012@Cradle_Audio), MIC2-1(MMICT390200012@Cradle_Audio) | - |
| NLDO1_3 | C42-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-14(RK806S-5@Cradle_Power_PMIC) | - |
| NLDO2_3 | C43-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-12(RK806S-5@Cradle_Power_PMIC) | - |
| NLDO3_3 | C44-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-11(RK806S-5@Cradle_Power_PMIC) | - |
| NLDO4_3 | C45-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-10(RK806S-5@Cradle_Power_PMIC) | - |
| NLDO5_3 | C46-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-8(RK806S-5@Cradle_Power_PMIC) | - |
| NetANT1_1 | ANT1-1(2450AT18A100E@Cradle_Wireless), C84-1(JLC_10pF_0402CG100J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | - |
| NetANT1_2 | ANT1-2(2450AT18A100E@Cradle_Wireless) | orphaned |
| NetANT2_1 | ANT2-1(2450AT18A100E@Cradle_Wireless), C85-1(JLC_10pF_0402CG100J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | - |
| NetANT2_2 | ANT2-2(2450AT18A100E@Cradle_Wireless) | orphaned |
| NetC10_1 | C10-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)) | orphaned |
| NetC10_2 | C10-2(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)) | orphaned |
| NetC11_1 | C11-1(JLC_10pF_0402CG100J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetC11_2 | C11-2(JLC_10pF_0402CG100J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetC12_1 | C12-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)) | orphaned |
| NetC12_2 | C12-2(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)) | orphaned |
| NetC13_1 | C13-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)) | orphaned |
| NetC13_2 | C13-2(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)) | orphaned |
| NetC23_1 | C23-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), R13-2(RMCF0402JT100R@Cradle_Power_PMIC), U6-4(RK806S-5@Cradle_Power_PMIC) | - |
| NetC3_1 | C3-1(885012106031@Cradle_Power_Charging), U10-23(BQ25601RTWR@Cradle_Power_Charging) | - |
| NetC5_1 | C5-1(CC0402KRX5R9BB473@Cradle_Power_Charging), L1-1(JLC_SWPA4030S1R0NT@Cradle_Power_Charging), U10-19(BQ25601RTWR@Cradle_Power_Charging), U10-20(BQ25601RTWR@Cradle_Power_Charging) | - |
| NetC5_2 | C5-2(CC0402KRX5R9BB473@Cradle_Power_Charging), U10-21(BQ25601RTWR@Cradle_Power_Charging) | - |
| NetC66_2 | C66-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), D3-1(JLC_SD103AX@Cradle_Power_PMIC), R19-2(CRG0402F200K@Cradle_Power_PMIC) | - |
| NetC7_1 | C7-1(885012106031@Cradle_Power_Charging), Q1-3(DMP2035U-7@Cradle_Power_Charging), U10-13(BQ25601RTWR@Cradle_Power_Charging), U10-14(BQ25601RTWR@Cradle_Power_Charging) | - |
| NetC80_1 | C80-1(JLC_30pF_0402CG300J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetC80_2 | C80-2(JLC_30pF_0402CG300J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetC81_2 | C81-2(JLC_30pF_0402CG300J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-14(AP6275S@Cradle_Wireless), X1-3(JLC_37.4_MHz_7M37470001@Cradle_Wireless) | - |
| NetC82_2 | C82-2(JLC_30pF_0402CG300J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-13(AP6275S@Cradle_Wireless), X1-1(JLC_37.4_MHz_7M37470001@Cradle_Wireless) | - |
| NetC83_1 | C83-1(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))) | orphaned |
| NetC83_2 | C83-2(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))) | orphaned |
| NetC84_2 | C84-2(JLC_10pF_0402CG100J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R30-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | - |
| NetC85_2 | C85-2(JLC_10pF_0402CG100J500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R31-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | - |
| NetC88_1 | C88-1(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | orphaned |
| NetC88_2 | C88-2(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | orphaned |
| NetC89_1 | C89-1(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), L10-2(SLS3D16S2R2NTT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-29(AP6275S@Cradle_Wireless) | - |
| NetC8_1 | C8-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)) | orphaned |
| NetC8_2 | C8-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)) | orphaned |
| NetC90_1 | C90-1(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), L11-1(SLS3D16S2R2NTT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-25(AP6275S@Cradle_Wireless) | - |
| NetC99_1 | C99-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U3-C2(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| NetC9_1 | C9-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)) | orphaned |
| NetC9_2 | C9-2(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)) | orphaned |
| NetD19_A | D19-A(ESD9L5.0ST5G@Cradle_Interfaces), FPC2-6(JLC_05A20L22P@Cradle_Interfaces), U15-4(SN74LV1T125DCKR@Cradle_Interfaces) | - |
| NetD1_3 | D1-3(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), USB1-A7(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB1-B7(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| NetD1_4 | D1-4(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), USB1-A6(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB1-B6(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| NetD8_3 | D8-3(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), USB2-A7(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB2-B7(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| NetD8_4 | D8-4(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces), USB2-A6(JLC_TYPE-C 16P QTWT@Cradle_Interfaces), USB2-B6(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| NetJ1_5 | J1-5(SM04B-GHS-TB(LF)(SN)@Cradle_Interfaces) | orphaned |
| NetJ1_6 | J1-6(SM04B-GHS-TB(LF)(SN)@Cradle_Interfaces) | orphaned |
| NetL10_1 | L10-1(SLS3D16S2R2NTT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-28(AP6275S@Cradle_Wireless) | - |
| NetL11_2 | L11-2(SLS3D16S2R2NTT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-26(AP6275S@Cradle_Wireless) | - |
| NetL2_1 | L2-1(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)) | orphaned |
| NetL2_2 | L2-2(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)) | orphaned |
| NetL9_1 | L9-1(SLS3D16S2R2NTT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetL9_2 | L9-2(SLS3D16S2R2NTT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetLED1_1 | LED1-1(JLC_XL-0603QYGC@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet))), R5-1(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | - |
| NetLED2_2 | LED2-2(JLC_KT-0603R@Cradle_Power_Charging), R4-1(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | - |
| NetLED3_1 | LED3-1(JLC_XL-0603QYGC@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet))) | orphaned |
| NetLED3_2 | LED3-2(JLC_XL-0603QYGC@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet))) | orphaned |
| NetP1_1 | P1-1(S2B-PH-K-S(LF)(SN)@ambiguous(Cradle_Power_Charging, Cradle_Interfaces)), Q1-2(DMP2035U-7@Cradle_Power_Charging) | - |
| NetQ2_2 | Q2-2(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R61-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| NetQ3_3 | Q3-3(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R63-1(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), U8-14(HDMI-519S@Cradle_Interfaces) | - |
| NetQ4_3 | Q4-3(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R66-1(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), U8-15(HDMI-519S@Cradle_Interfaces) | - |
| NetQ5_3 | Q5-3(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), R67-1(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), U8-16(HDMI-519S@Cradle_Interfaces) | - |
| NetQ6_1 | Q6-1(JLC_LBSS138LT1G@ambiguous(Cradle_Storage, Cradle_Interfaces)), U8-19(HDMI-519S@Cradle_Interfaces) | - |
| NetR12_2 | R12-2(RC0402JR-100RL@Cradle_Power_PMIC), U6-18(RK806S-5@Cradle_Power_PMIC) | - |
| NetR25_1 | R25-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | orphaned |
| NetR25_2 | R25-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | orphaned |
| NetR26_1 | R26-1(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetR26_2 | R26-2(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetR27_1 | R27-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetR27_2 | R27-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetR28_1 | R28-1(JLC_100_OHM_CR0402JF0101G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetR28_2 | R28-2(JLC_100_OHM_CR0402JF0101G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)) | orphaned |
| NetR30_2 | R30-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-2(AP6275S@Cradle_Wireless) | - |
| NetR31_2 | R31-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-9(AP6275S@Cradle_Wireless) | - |
| NetR32_2 | R32-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-17(AP6275S@Cradle_Wireless) | - |
| NetR33_2 | R33-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-18(AP6275S@Cradle_Wireless) | - |
| NetR34_2 | R34-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-19(AP6275S@Cradle_Wireless) | - |
| NetR35_2 | R35-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-20(AP6275S@Cradle_Wireless) | - |
| NetR36_1 | R36-1(JLC_100_OHM_CR0402JF0101G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-31(AP6275S@Cradle_Wireless) | - |
| NetR36_2 | R36-2(JLC_100_OHM_CR0402JF0101G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U14-2(JLC_32.768KHz_SIT1552AI-JF-DCC-32.768D@Cradle_Wireless) | - |
| NetR37_2 | R37-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-21(AP6275S@Cradle_Wireless) | - |
| NetR38_2 | R38-2(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-22(AP6275S@Cradle_Wireless) | - |
| NetR4_2 | R4-2(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U10-3(BQ25601RTWR@Cradle_Power_Charging) | - |
| NetR5_2 | R5-2(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U10-4(BQ25601RTWR@Cradle_Power_Charging) | - |
| NetR62_1 | R62-1(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)) | orphaned |
| NetR62_2 | R62-2(TFCR0603-10W-C-4701FT-1K@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)) | orphaned |
| NetR6_2 | R6-2(RMCF0402FT5K23@Cradle_Power_Charging), R7-1(103AT-2@Cradle_Power_Charging), R8-1(RT0402FRE0730K1L@Cradle_Power_Charging), U10-11(BQ25601RTWR@Cradle_Power_Charging) | - |
| NetR70_1 | R70-1(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)) | orphaned |
| NetR70_2 | R70-2(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)) | orphaned |
| NetR71_1 | R71-1(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), USB1-B5(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| NetR72_1 | R72-1(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), USB1-A5(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| NetR73_1 | R73-1(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), USB2-B5(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| NetR74_1 | R74-1(CRCW04025K10JNEE@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Interfaces)), USB2-A5(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | - |
| NetSW1_1 | SW1-1(JLC_KMR221GLFS@Cradle_Power_Charging), SW1-2(JLC_KMR221GLFS@Cradle_Power_Charging), U10-12(BQ25601RTWR@Cradle_Power_Charging) | - |
| NetSW1_5 | SW1-5(JLC_KMR221GLFS@Cradle_Power_Charging) | orphaned |
| NetTP1_1 | TP1-1(RH-5007@Cradle_Power_PMIC), U6-16(RK806S-5@Cradle_Power_PMIC) | - |
| NetU10_10 | U10-10(BQ25601RTWR@Cradle_Power_Charging) | orphaned |
| NetU10_8 | U10-8(BQ25601RTWR@Cradle_Power_Charging) | orphaned |
| NetU1_A1 | U1-A1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A11 | U1-A11(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A13 | U1-A13(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A15 | U1-A15(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A17 | U1-A17(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A19 | U1-A19(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A2 | U1-A2(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A21 | U1-A21(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A23 | U1-A23(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A25 | U1-A25(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A26 | U1-A26(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A27 | U1-A27(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A28 | U1-A28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A29 | U1-A29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A3 | U1-A3(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A4 | U1-A4(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A5 | U1-A5(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A7 | U1-A7(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_A9 | U1-A9(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B1 | U1-B1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B10 | U1-B10(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B11 | U1-B11(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B12 | U1-B12(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B13 | U1-B13(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B14 | U1-B14(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B15 | U1-B15(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B16 | U1-B16(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B17 | U1-B17(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B18 | U1-B18(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B19 | U1-B19(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B2 | U1-B2(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B20 | U1-B20(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B21 | U1-B21(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B22 | U1-B22(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B23 | U1-B23(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B24 | U1-B24(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B25 | U1-B25(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B26 | U1-B26(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B27 | U1-B27(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B28 | U1-B28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B29 | U1-B29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B3 | U1-B3(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B4 | U1-B4(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B5 | U1-B5(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B6 | U1-B6(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B7 | U1-B7(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B8 | U1-B8(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_B9 | U1-B9(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_C1 | U1-C1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_C28 | U1-C28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_C29 | U1-C29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_D1 | U1-D1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_D28 | U1-D28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_E1 | U1-E1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_E28 | U1-E28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_E29 | U1-E29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_F28 | U1-F28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_G1 | U1-G1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_G28 | U1-G28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_G29 | U1-G29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_H1 | U1-H1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_H28 | U1-H28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_H29 | U1-H29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_J28 | U1-J28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_J29 | U1-J29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_K1 | U1-K1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_K28 | U1-K28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_K29 | U1-K29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_L1 | U1-L1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_L28 | U1-L28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_L29 | U1-L29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_M28 | U1-M28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_M29 | U1-M29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_N1 | U1-N1(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_N28 | U1-N28(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU1_N29 | U1-N29(RK3576_C42388007@Cradle_Compute_SOC) | pending-port |
| NetU2_12 | U2-12(AP6275S@Cradle_Wireless) | orphaned |
| NetU2_24 | U2-24(AP6275S@Cradle_Wireless) | orphaned |
| NetU2_37 | U2-37(AP6275S@Cradle_Wireless) | orphaned |
| NetU2_44 | U2-44(AP6275S@Cradle_Wireless) | orphaned |
| NetU2_45 | U2-45(AP6275S@Cradle_Wireless) | orphaned |
| NetU2_46 | U2-46(AP6275S@Cradle_Wireless) | orphaned |
| NetU2_47 | U2-47(AP6275S@Cradle_Wireless) | orphaned |
| NetU2_48 | U2-48(AP6275S@Cradle_Wireless) | orphaned |
| NetU3_A1 | U3-A1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A10 | U3-A10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A11 | U3-A11(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A12 | U3-A12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A13 | U3-A13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A14 | U3-A14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A2 | U3-A2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A7 | U3-A7(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A8 | U3-A8(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_A9 | U3-A9(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B1 | U3-B1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B10 | U3-B10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B11 | U3-B11(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B12 | U3-B12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B13 | U3-B13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B14 | U3-B14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B7 | U3-B7(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B8 | U3-B8(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_B9 | U3-B9(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C1 | U3-C1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C10 | U3-C10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C11 | U3-C11(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C12 | U3-C12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C13 | U3-C13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C14 | U3-C14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C3 | U3-C3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C5 | U3-C5(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C7 | U3-C7(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C8 | U3-C8(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_C9 | U3-C9(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_D1 | U3-D1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_D12 | U3-D12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_D13 | U3-D13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_D14 | U3-D14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_D2 | U3-D2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_D3 | U3-D3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_D4 | U3-D4(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E1 | U3-E1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E10 | U3-E10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E12 | U3-E12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E13 | U3-E13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E14 | U3-E14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E2 | U3-E2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E3 | U3-E3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E5 | U3-E5(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E8 | U3-E8(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_E9 | U3-E9(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_F1 | U3-F1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_F10 | U3-F10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_F12 | U3-F12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_F13 | U3-F13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_F14 | U3-F14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_F2 | U3-F2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_F3 | U3-F3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_G1 | U3-G1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_G10 | U3-G10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_G12 | U3-G12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_G13 | U3-G13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_G14 | U3-G14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_G2 | U3-G2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_G3 | U3-G3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_H1 | U3-H1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_H12 | U3-H12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_H13 | U3-H13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_H14 | U3-H14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_H2 | U3-H2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_H3 | U3-H3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_J1 | U3-J1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_J12 | U3-J12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_J13 | U3-J13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_J14 | U3-J14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_J2 | U3-J2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_J3 | U3-J3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K1 | U3-K1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K10 | U3-K10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K12 | U3-K12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K13 | U3-K13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K14 | U3-K14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K2 | U3-K2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K3 | U3-K3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K6 | U3-K6(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_K7 | U3-K7(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_L1 | U3-L1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_L12 | U3-L12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_L13 | U3-L13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_L14 | U3-L14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_L2 | U3-L2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_L3 | U3-L3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M1 | U3-M1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M10 | U3-M10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M11 | U3-M11(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M12 | U3-M12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M13 | U3-M13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M14 | U3-M14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M2 | U3-M2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M3 | U3-M3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M7 | U3-M7(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M8 | U3-M8(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_M9 | U3-M9(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N1 | U3-N1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N10 | U3-N10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N11 | U3-N11(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N12 | U3-N12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N13 | U3-N13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N14 | U3-N14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N3 | U3-N3(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N6 | U3-N6(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N7 | U3-N7(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N8 | U3-N8(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_N9 | U3-N9(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P1 | U3-P1(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P10 | U3-P10(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P11 | U3-P11(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P12 | U3-P12(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P13 | U3-P13(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P14 | U3-P14(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P2 | U3-P2(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P7 | U3-P7(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P8 | U3-P8(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU3_P9 | U3-P9(EMMC04G-M627-Y02U@Cradle_Storage) | pending-port |
| NetU5_A1 | U5-A1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_A11 | U5-A11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_A12 | U5-A12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_A2 | U5-A2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_A4 | U5-A4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_A5 | U5-A5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_A8 | U5-A8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_A9 | U5-A9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B1 | U5-B1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B10 | U5-B10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B11 | U5-B11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B12 | U5-B12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B2 | U5-B2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B3 | U5-B3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B4 | U5-B4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B5 | U5-B5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B8 | U5-B8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_B9 | U5-B9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_C10 | U5-C10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_C11 | U5-C11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_C2 | U5-C2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_C3 | U5-C3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_C4 | U5-C4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_C9 | U5-C9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_D1 | U5-D1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_D10 | U5-D10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_D12 | U5-D12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_D3 | U5-D3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_D5 | U5-D5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_D8 | U5-D8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_E10 | U5-E10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_E11 | U5-E11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_E2 | U5-E2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_E3 | U5-E3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_E4 | U5-E4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_E9 | U5-E9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F1 | U5-F1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F10 | U5-F10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F11 | U5-F11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F12 | U5-F12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F2 | U5-F2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F3 | U5-F3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F4 | U5-F4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F5 | U5-F5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F8 | U5-F8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_F9 | U5-F9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_G11 | U5-G11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_G2 | U5-G2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_G4 | U5-G4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_G9 | U5-G9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H1 | U5-H1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H10 | U5-H10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H11 | U5-H11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H12 | U5-H12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H2 | U5-H2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H3 | U5-H3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H4 | U5-H4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H5 | U5-H5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H8 | U5-H8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_H9 | U5-H9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_J11 | U5-J11(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_J2 | U5-J2(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_J4 | U5-J4(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_J5 | U5-J5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_J8 | U5-J8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_J9 | U5-J9(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_K1 | U5-K1(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_K10 | U5-K10(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_K12 | U5-K12(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_K3 | U5-K3(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_K5 | U5-K5(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU5_K8 | U5-K8(JLC_K4UBE3D4AB-MGCL@Cradle_Compute_Memory) | pending-port |
| NetU6_2 | U6-2(RK806S-5@Cradle_Power_PMIC) | orphaned |
| NetU6_21 | U6-21(RK806S-5@Cradle_Power_PMIC) | orphaned |
| NetU6_3 | U6-3(RK806S-5@Cradle_Power_PMIC) | orphaned |
| NetU6_38 | U6-38(RK806S-5@Cradle_Power_PMIC) | orphaned |
| NetU6_48 | U6-48(RK806S-5@Cradle_Power_PMIC) | orphaned |
| NetU8_17 | U8-17(HDMI-519S@Cradle_Interfaces) | orphaned |
| NetU9_B2 | U9-B2(MAX98357AEWL+T@Cradle_Audio) | pending-port |
| NetUSB1_A8 | USB1-A8(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | pending-port |
| NetUSB1_B8 | USB1-B8(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | pending-port |
| NetUSB2_A8 | USB2-A8(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | pending-port |
| NetUSB2_B8 | USB2-B8(JLC_TYPE-C 16P QTWT@Cradle_Interfaces) | pending-port |
| PLDO1_3 | C59-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-60(RK806S-5@Cradle_Power_PMIC) | - |
| PLDO2_3 | C60-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-58(RK806S-5@Cradle_Power_PMIC) | - |
| PLDO3_3 | C61-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-57(RK806S-5@Cradle_Power_PMIC) | - |
| PLDO4_3 | C62-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-63(RK806S-5@Cradle_Power_PMIC) | - |
| PLDO5_3 | C63-1(JLC_1210B225K500NT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-65(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_EXT_EN_OUT | U6-39(RK806S-5@Cradle_Power_PMIC) | pending-port |
| PMIC_FB5_3 | R22-2(RC0402FR-07499KL@Cradle_Power_PMIC), R24-1(AC0402JR-13100KL@Cradle_Power_PMIC), U6-47(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_FB6_3 | C14-2(CAP 100pF 50V 0402(1005)@Cradle_Power_PMIC), R9-2(RN73R1ETTP2001F25@Cradle_Power_PMIC), R11-1(AC0402JR-13100KL@Cradle_Power_PMIC), U6-31(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_FB9_3 | C51-2(CAP 100pF 50V 0402(1005)@Cradle_Power_PMIC), R17-2(RK73H1ETTP1103F@Cradle_Power_PMIC), R18-1(AC0402JR-13100KL@Cradle_Power_PMIC), U6-66(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_INT_L | U6-19(RK806S-5@Cradle_Power_PMIC) | pending-port |
| PMIC_PWR_CTRL_1 | U6-62(RK806S-5@Cradle_Power_PMIC) | pending-port |
| PMIC_PWR_CTRL_2 | U6-61(RK806S-5@Cradle_Power_PMIC) | pending-port |
| PMIC_SW10_3 | L7-1(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), U6-26(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_SW1_3 | U6-50(RK806S-5@Cradle_Power_PMIC), U6-51(RK806S-5@Cradle_Power_PMIC), U7-1(JLC_FTC252012SR24MBCA@Cradle_Power_PMIC) | - |
| PMIC_SW2_3 | U6-35(RK806S-5@Cradle_Power_PMIC), U6-36(RK806S-5@Cradle_Power_PMIC), U11-1(JLC_FTC252012SR24MBCA@Cradle_Power_PMIC) | - |
| PMIC_SW3_3 | U6-55(RK806S-5@Cradle_Power_PMIC), U12-1(JLC_FTC252012SR24MBCA@Cradle_Power_PMIC) | - |
| PMIC_SW4_3 | U6-23(RK806S-5@Cradle_Power_PMIC), U13-1(JLC_FTC252012SR24MBCA@Cradle_Power_PMIC) | - |
| PMIC_SW5_3 | L8-1(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), U6-45(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_SW6_3 | L3-1(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), U6-29(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_SW7_3 | L4-1(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), U6-42(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_SW8_3 | L5-1(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), U6-6(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_SW9_3 | L6-1(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), U6-68(RK806S-5@Cradle_Power_PMIC) | - |
| PMIC_VDC | C67-1(JLC_0402B102K500NT@Cradle_Power_PMIC), R19-1(CRG0402F200K@Cradle_Power_PMIC), R20-1(CRG0402F200K@Cradle_Power_PMIC), U6-32(RK806S-5@Cradle_Power_PMIC) | - |
| PWRON_L | R13-1(RMCF0402JT100R@Cradle_Power_PMIC) | pending-port |
| REGN_2 | C4-1(CC0402MRX5R7BB475@Cradle_Power_Charging), R6-1(RMCF0402FT5K23@Cradle_Power_Charging), U10-22(BQ25601RTWR@Cradle_Power_Charging) | - |
| RESET_L | U6-40(RK806S-5@Cradle_Power_PMIC) | pending-port |
| SD_CD | Card1-9(TF-01A@Cradle_Storage), R50-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| SD_CDD3 | Card1-2(TF-01A@Cradle_Storage), R49-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| SD_CLK | Card1-5(TF-01A@Cradle_Storage) | pending-port |
| SD_CMD | Card1-3(TF-01A@Cradle_Storage), R45-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| SD_D0 | Card1-7(TF-01A@Cradle_Storage), R46-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| SD_D1 | Card1-8(TF-01A@Cradle_Storage), R47-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| SD_D2 | Card1-1(TF-01A@Cradle_Storage), R48-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| SPK_BCLK | U9-C1(MAX98357AEWL+T@Cradle_Audio) | pending-port |
| SPK_DIN | U9-B1(MAX98357AEWL+T@Cradle_Audio) | pending-port |
| SPK_LRCLK | U9-C3(MAX98357AEWL+T@Cradle_Audio) | pending-port |
| SPK_OUTN | U9-B3(MAX98357AEWL+T@Cradle_Audio) | pending-port |
| SPK_OUTN_8 | P2-2(S2B-PH-K-S(LF)(SN)@ambiguous(Cradle_Power_Charging, Cradle_Interfaces)) | pending-port |
| SPK_OUTP | U9-A3(MAX98357AEWL+T@Cradle_Audio) | pending-port |
| SPK_OUTP_8 | P2-1(S2B-PH-K-S(LF)(SN)@ambiguous(Cradle_Power_Charging, Cradle_Interfaces)) | pending-port |
| SPK_SD_MODE | U9-A1(MAX98357AEWL+T@Cradle_Audio) | pending-port |
| STORAGE_1V8 | C93-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C94-1(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C95-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C96-1(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C97-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C98-1(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C100-1(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), C101-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C102-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C103-1(CL10A475KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R51-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R52-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R53-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R54-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R55-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R56-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R57-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R58-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R59-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R60-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-C6(EMMC04G-M627-Y02U@Cradle_Storage), U3-M4(EMMC04G-M627-Y02U@Cradle_Storage), U3-N4(EMMC04G-M627-Y02U@Cradle_Storage), U3-P3(EMMC04G-M627-Y02U@Cradle_Storage), U3-P5(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| STORAGE_3V3 | C91-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C92-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C104-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C105-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C106-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C107-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C108-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C109-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C110-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C111-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), Card1-4(TF-01A@Cradle_Storage), R45-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R46-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R47-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R48-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R49-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R50-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U3-E6(EMMC04G-M627-Y02U@Cradle_Storage), U3-F5(EMMC04G-M627-Y02U@Cradle_Storage), U3-J10(EMMC04G-M627-Y02U@Cradle_Storage), U3-K9(EMMC04G-M627-Y02U@Cradle_Storage) | - |
| SYS | C6-1(885012106031@Cradle_Power_Charging), L1-2(JLC_SWPA4030S1R0NT@Cradle_Power_Charging), LED1-2(JLC_XL-0603QYGC@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet))), LED2-1(JLC_KT-0603R@Cradle_Power_Charging), U10-15(BQ25601RTWR@Cradle_Power_Charging), U10-16(BQ25601RTWR@Cradle_Power_Charging) | - |
| USB1_D_8_N | D1-2(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| USB1_D_8_P | D1-1(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| USB2_D_8_N | D8-2(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| USB2_D_8_P | D8-1(JLC_PRTR5V0U2X_C2827688@Cradle_Interfaces) | pending-port |
| VCCA1V8_PLDO6 | C64-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), U6-20(RK806S-5@Cradle_Power_PMIC) | - |
| VCC_1V1_NLDO | C17-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C21-2(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C28-2(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C33-2(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C34-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C40-2(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C47-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C48-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C49-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C50-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C54-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C58-2(JLC_22uF_0603_C1608X5R1A226MT000E@ambiguous(Cradle_Power_PMIC, Cradle (top-level/block-diagram sheet))), C65-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C66-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C71-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), C75-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), R12-1(RC0402JR-100RL@Cradle_Power_PMIC), U6-1(RK806S-5@Cradle_Power_PMIC), U6-7(RK806S-5@Cradle_Power_PMIC), U6-9(RK806S-5@Cradle_Power_PMIC), U6-13(RK806S-5@Cradle_Power_PMIC), U6-22(RK806S-5@Cradle_Power_PMIC), U6-27(RK806S-5@Cradle_Power_PMIC), U6-28(RK806S-5@Cradle_Power_PMIC), U6-33(RK806S-5@Cradle_Power_PMIC), U6-34(RK806S-5@Cradle_Power_PMIC), U6-43(RK806S-5@Cradle_Power_PMIC), U6-44(RK806S-5@Cradle_Power_PMIC), U6-52(RK806S-5@Cradle_Power_PMIC), U6-53(RK806S-5@Cradle_Power_PMIC), U6-54(RK806S-5@Cradle_Power_PMIC), U6-59(RK806S-5@Cradle_Power_PMIC), U6-64(RK806S-5@Cradle_Power_PMIC) | - |
| VCC_3V3 | C55-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C56-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C57-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), U6-24(RK806S-5@Cradle_Power_PMIC), U13-2(JLC_FTC252012SR24MBCA@Cradle_Power_PMIC) | - |
| VDD2_DDR | C51-1(CAP 100pF 50V 0402(1005)@Cradle_Power_PMIC), C52-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C53-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), L6-2(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), R17-1(RK73H1ETTP1103F@Cradle_Power_PMIC), U6-67(RK806S-5@Cradle_Power_PMIC) | - |
| VDDQ_DDR | C14-1(CAP 100pF 50V 0402(1005)@Cradle_Power_PMIC), C15-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C16-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), L3-2(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), R9-1(RN73R1ETTP2001F25@Cradle_Power_PMIC), U6-30(RK806S-5@Cradle_Power_PMIC) | - |
| VDD_1V8 | C36-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C41-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), L5-2(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), U6-5(RK806S-5@Cradle_Power_PMIC) | - |
| VDD_CPU_BIG | C18-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C19-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C20-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C22-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C22-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), R10-1(RMCF0402JT100R@Cradle_Power_PMIC), R10-2(RMCF0402JT100R@Cradle_Power_PMIC), U7-2(JLC_FTC252012SR24MBCA@Cradle_Power_PMIC) | - |
| VDD_CPU_LIT | C35-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C37-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C37-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C38-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C39-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), R16-1(RMCF0402JT100R@Cradle_Power_PMIC), R16-2(RMCF0402JT100R@Cradle_Power_PMIC), U6-56(RK806S-5@Cradle_Power_PMIC), U12-2(JLC_FTC252012SR24MBCA@Cradle_Power_PMIC) | - |
| VDD_DDR | C68-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C69-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C69-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C70-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), L7-2(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), R21-1(RMCF0402JT100R@Cradle_Power_PMIC), R21-2(RMCF0402JT100R@Cradle_Power_PMIC), U6-25(RK806S-5@Cradle_Power_PMIC) | - |
| VDD_GPU | C72-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C73-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C73-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C74-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), L8-2(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), R22-1(RC0402FR-07499KL@Cradle_Power_PMIC), R23-1(RMCF0402JT100R@Cradle_Power_PMIC), R23-2(RMCF0402JT100R@Cradle_Power_PMIC), U6-46(RK806S-5@Cradle_Power_PMIC) | - |
| VDD_LOGIC | C24-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C25-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C25-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C26-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C27-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), L4-2(JLC_WPN252012ER47MT@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), R14-1(RMCF0402JT100R@Cradle_Power_PMIC), R14-2(RMCF0402JT100R@Cradle_Power_PMIC), U6-41(RK806S-5@Cradle_Power_PMIC) | - |
| VDD_NPU | C29-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C30-1(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C30-2(CL05A105KP5NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Storage)), C31-1(JLC_C2012X5R1A476MTJ00E@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC)), C32-1(JLC_CL10A106KP8NNNC@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Storage)), R15-1(RMCF0402JT100R@Cradle_Power_PMIC), R15-2(RMCF0402JT100R@Cradle_Power_PMIC), U6-37(RK806S-5@Cradle_Power_PMIC), U11-2(JLC_FTC252012SR24MBCA@Cradle_Power_PMIC) | - |
| VDU_CPU_BIG_3 | U6-49(RK806S-5@Cradle_Power_PMIC) | pending-port |
| WIRELESS_1V8 | C86-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), C87-1(GRM155R61E104KA87D@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Power_PMIC, Cradle_Audio, Cradle_Wireless, Cradle_Storage, Cradle_Interfaces)), R29-1(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R39-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R40-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R41-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R42-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R43-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), R44-2(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)), U2-34(AP6275S@Cradle_Wireless), U14-3(JLC_32.768KHz_SIT1552AI-JF-DCC-32.768D@Cradle_Wireless) | - |
| WIRELESS_3V3 | U2-36(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_BT_HOST_WAKE | U2-50(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_BT_REG_ON | U2-38(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_BT_UART_CTS_N | U2-43(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_BT_UART_RTS_N | U2-42(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_BT_UART_RXD | U2-41(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_BT_UART_TXD | U2-40(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_BT_WAKE | R29-2(TNPW040210K0DEED@ambiguous(Cradle_Power_Charging, Cradle (top-level/block-diagram sheet), Cradle_Wireless)), U2-49(AP6275S@Cradle_Wireless) | - |
| WIRELESS_SD0 | R37-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R41-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| WIRELESS_SD1 | R38-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R42-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| WIRELESS_SD2 | R35-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R43-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| WIRELESS_SD3 | R34-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R44-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| WIRELESS_SDCLK | R33-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R40-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| WIRELESS_SDCMD | R32-1(JLC_0_OHM_0402_RC0402JR-070RL@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless)), R39-1(JLC_30K_CR0402FF3002G@ambiguous(Cradle (top-level/block-diagram sheet), Cradle_Wireless, Cradle_Storage)) | - |
| WIRELESS_WL_GPIO_10 | U2-33(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_WL_GPIO_11 | U2-35(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_WL_HOST_WAKE | U2-16(AP6275S@Cradle_Wireless) | pending-port |
| WIRELESS_WL_REG_ON | U2-15(AP6275S@Cradle_Wireless) | pending-port |
