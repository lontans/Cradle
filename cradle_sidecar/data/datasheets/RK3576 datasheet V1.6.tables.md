# Ported tables: RK3576 datasheet V1.6.pdf

Mechanically extracted pin tables and spec/parameter tables -- cell contents are verbatim from the PDF, not reworded or interpreted. Review before trusting (table detection can misparse merged cells or footnote markers) and fold the relevant parts into `cradle_sidecar/data/components/<PART>.md` by hand, including the Cradle Wiring and Status columns that only a real design decision can fill in.

## Page 30 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VSS_0 |  |  | A1 |  |  | LP4 A1 A/LP4X A1 A/LP5 A1 A |  |  | 1N1 |  |  |
| LP4 DQ11 B/LP4X DQ11 B/LP5 DQ11 B |  |  | A2 |  |  | VSS_59 |  |  | 1N2 |  |  |
| LP4_DQS1P_B/LP4X_DQS1P_B/LP5_RDQS1P B |  |  | A3 |  |  | LP4_CKE0_A/LP4X_CKE0_A/LP5_CSN0 A |  |  | 1N3 |  |  |
| _ VSS_1 |  |  | A4 |  |  | _ VSS_60 |  |  | 1N4 |  |  |
| LP4 DQ6 B/LP4X DQ6 B/LP5 DQ6 B |  |  | A5 |  |  | LP4_CKE1_A/LP4X_CKE1_A/LP5_CSN1 A |  |  | 1N5 |  |  |
| SAI1 SDO0 M0/SAI4 SDI M0/SPI3 CLK M2 /PWM2 CH6 M0/GPIO4 A7 d |  |  | A7 |  |  | _ VSS_61 |  |  | 1N6 |  |  |
| _ _ _ _ VO_LCDC_D22/VO_EBC_GDSP/ETH0_MDIO M0/PDM1_SDI3_M2/DSMC_DATA15/FLEXBUS 0_D7/UART1_RTSN_M2/SPI2_CSN1_M2/PWM 1 CH1 M3/GPIO3 A5 d |  |  | A9 |  |  | AVSS1_20 |  |  | 1N20 |  |  |
| _ _ _ _ VO_LCDC_D16/VO_EBC_SDCE0/ETH0_TXCTL M0/PDM1_SDI0_M2/DSMC_DATA10/FLEXBU S0_D2/UART9_TX_M1/I2C8_SCL_M3/GPIO3 B3 d |  |  | A11 |  |  | AVSS1_21 |  |  | 1N21 |  |  |
| _ VO_LCDC_D17/VO_EBC_SDCE1/ETH0_RXD0 M0/PDM1_SDI1_M2/DSMC_DATA11/FLEXBU S0_D3/UART9_RX_M1/I2C8_SDA_M3/GPIO3 B2 d |  |  | A13 |  |  | PCIE0_REFCLKP |  |  | 1N22 |  |  |
| _ _ VI CIF D2/ETH1 TXD2 M0/SAI2 LRCK M1/ PDM1_SDI3_M0/UART11_RTSN_M1/SPI1_MI SO M1/PWM0 CH0 M2/GPIO2 C3 d |  |  | A15 |  |  | PCIE0_REFCLKN |  |  | 1N23 |  |  |
| _ _ _ _ _ VI CIF D5/ETH1 RXD2 M0/ETH0 PTP REFC LK_M1/PDM1_SDI1_M0/UART9_RX_M0/PWM 1 CH0 M2/GPIO2 C0 d |  |  | A17 |  |  | AVSS1_22 |  |  | 1N24 |  |  |
| _ _ _ _ VI_CIF_D9/SDMMC1_PWREN_M1/ETH0_TXD 2_M1/SAI0_SDI3_M0/PDM0_SDI0_M3/UART 7_CTSN_M0/SPI4_MOSI_M3/SATA0_ACTLED M0/GPIO2 B4 d |  |  | A19 |  |  | LP4 DQ2 A/LP4X DQ2 A/LP5 DQ2 A |  |  | 1P1 |  |  |
| _ _ _ VI CIF D7/ETH1 PTP REFCLK M1/ETH0 RX D3_M1/SAI0_SCLK_M0/UART7_TX_M0/UART 8 RTSN M1/I2C8 SCL M2/GPIO2 B6 d |  |  | A21 |  |  | VSS_62 |  |  | 1P2 |  |  |
| _ _ _ _ _ _ SDMMC0 D2/FSPI1 D2 M0/DSM AUD RP M 0/SAI3_LRCK_M3/JTAG_TCK_M0/UART5_RTS N M2/SPI0 CSN1 M1/CAN1 RX M0/I3C1 S CL M1/GPIO2 A2 d |  |  | A23 |  |  | VSS_63 |  |  | 1P3 |  |  |
| _ _ _ SARADC_IN0_BOOT |  |  | A25 |  |  | VSS_64 |  |  | 1P4 |  |  |
| ETH1_TXCTL_M1/FSPI1_D2_M1/PDM0_SDI0 M2/UART2_TX_M0/I2C8_SCL_M1/SATA_CPPO D/GPIO1 C6 d |  |  | A26 |  |  | LP4 A5 A/LP4X A5 A/LP5 A5 A |  |  | 1P5 |  |  |
| _ _ ETH1_TXD2_M1/SDMMC1_D3_M0/SAI3_SDI M1/UART3_RTSN_M2/SPI1_CSN0_M0/GPIO1 B7 d |  |  | A27 |  |  | VSS_65 |  |  | 1P6 |  |  |
| _ _ ETH1_RXD2_M1/SDMMC1_D0_M0/SAI3_SCL K M1/I2C9 SDA M1/SPI1 CLK M0/PCIE1 C LKREQN M1/PWM1 CH0 M1/GPIO1 B4 d |  |  | A28 |  |  | VSS_66 |  |  | 1P20 |  |  |
| _ _ _ _ _ VSS_2 |  |  | A29 |  |  | VSS_67 |  |  | 1P21 |  |  |
| LP4 DQ9 B/LP4X DQ9 B/LP5 DQ9 B |  |  | B1 |  |  | VSS_68 |  |  | 1P22 |  |  |
| LP4 DQ10 B/LP4X DQ10 B/LP5 DQ10 B |  |  | B2 |  |  | SPI2_MISO_M0/I2C0_SDA_M0/GPIO0 B1 z |  |  | 1P23 |  |  |
| LP4_DQS1N_B/LP4X_DQS1N_B/LP5_RDQS1N B |  |  | B3 |  |  | _ VSS_69 |  |  | 1P24 |  |  |
| _ LP4 DMI0 B/LP4X DMI0 B/LP5 DMI0 B |  |  | B4 |  |  | VSS_70 |  |  | 1R1 |  |  |
| VSS_3 |  |  | B5 |  |  | VSS_71 |  |  | 1R2 |  |  |
| SAI1_SDO3_M0/SAI1_SDI1_M0/PDM1_SDI1 M1/FLEXBUS1_D15_M1/SPI4_MISO_M2/MIP I TE M0/GPIO4 B2 d |  |  | B6 |  |  | LP4 A2 A/LP4X A2 A/LP5 A2 A |  |  | 1R3 |  |  |

## Page 31 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SAI1_SDO2_M0/SAI1_SDI2_M0/PDM1_SDI2 M1/FLEXBUS1_D14_M1/SPI4_MOSI_M2/UA RT5_RX_M1/UART6_CTSN_M0/UART2_CTSN M1/GPIO4 B1 d |  |  | B7 |  |  | LP4_CSN0_A/LP4X_CSN0_A |  |  | 1R4 |  |  |
| _ _ SPDIF_RX0_M0/FLEXBUS0_CSN_M4/UART2 RX_M1/I2C3_SDA_M0/CAN1_RX_M2/GPIO4 B4 d |  |  | B8 |  |  | LP5_A6_A |  |  | 1R5 |  |  |
| _ VO_LCDC_D9/VO_EBC_SDDO9/ETH0_TXD3 M0/SAI2_SCLK_M2/DSMC_INT1/FLEXBUS0 D9/UART11_RTSN_M0/SPI4_MISO_M1/I2C9 SCL M3/PWM2 CH0 M3/GPIO3 C2 d |  |  | B9 |  |  | ZQ_A |  |  | 1R6 |  |  |
| _ _ _ _ _ VO_LCDC_D15/VO_EBC_SDDO15/ETH0_TXD 1_M0/SPDIF_RX1_M0/DSMC_DATA9/FLEXBU S0_D1/UART9_RTSN_M1/PWM1_CH4_M3/GPI O3 B4 d |  |  | B10 |  |  | TSADC_CTRL_M0/TSADC_CTRL_ORG/G PIO0_A1_z |  |  | 1R24 |  |  |
| _ _ VO_LCDC_D13/VO_EBC_SDDO13/ETH0_TXC LK_M0/DSMC_DQS1/FLEXBUS0_CLK/SPI3_C SN0 M1/PWM0 CH1 M3/GPIO3 B6 d |  |  | B11 |  |  | LP4 DQ1 A/LP4X DQ1 A/LP5 DQ1 A |  |  | 1T1 |  |  |
| _ _ _ _ _ VO_LCDC_D0/VO_EBC_SDDO0/ETH0_RXD2 M0/SAI2_SDO_M2/DSMC_CSN0/FLEXBUS1 D2/UART2_CTSN_M2/I3C1_SCL_M2/PWM2_C H5 M3/GPIO3 D3 d |  |  | B12 |  |  | LP4 A3 A/LP4X A3 A/LP5 A3 A |  |  | 1T2 |  |  |
| _ _ _ VO_LCDC_D20/VO_EBC_VCOM/ETH0_RXCTL M0/PDM1_CLK1_M2/DSMC_DATA13/FLEXBU S0_D5/UART1_TX_M2/UART10_RTSN_M0/GP IO3 A7 d |  |  | B13 |  |  | VSS_72 |  |  | 1T3 |  |  |
| _ _ VO_LCDC_D19/VO_EBC_SDCE3/ETH0_MCLK M0/SAI4_MCLK_M1/DSMC_CSN1/FLEXBUS0 D8/UART10_RX_M0/SPI2_MOSI_M2/PWM0 CH0 M3/GPIO3 B0 d |  |  | B14 |  |  | LP4_CSN1_A/LP4X_CSN1_A |  |  | 1T4 |  |  |
| _ _ _ ETH1_TXD1_M0/SAI4_LRCK_M3/UART4_RTS N_M0/I2C5_SDA_M2/PWM0_CH1_M2/GPIO2 C7 d |  |  | B15 |  |  | VSS_73 |  |  | 1T5 |  |  |
| _ _ ETH1_TXCTL_M0/SAI4_SDI_M3/UART4_TX M0/I2C6_SCL_M2/PWM2_CH0_M2/GPIO2_D0 d |  |  | B16 |  |  | VSS_74 |  |  | 1T6 |  |  |
| _ CAM_CLK0_OUT_M1/ETH1_RXD1_M0/SAI4 MCLK_M3/UART6_TX_M1/I3C1_SCL_M0/PWM 2 CH2 M2/GPIO2 D2 d |  |  | B17 |  |  | VSS_75 |  |  | 1T20 |  |  |
| _ _ _ _ ETH1_RXCTL_M0/UART6_RX_M1/I3C1_SDA M0/PWM2 CH3 M2/GPIO2 D3 d |  |  | B18 |  |  | PMIC_INT/GPIO0_A6_u |  |  | 1T21 |  |  |
| _ _ _ _ VI CIF D13/SDMMC1 D2 M1/ETH0 TXD1 M 1/SAI0_SDI0_M0/PDM0_SDI3_M3/UART1_TX M1/GPIO2 B0 d |  |  | B19 |  |  | SPI2_CLK_M0/I2C1_SCL_M0/GPIO0_B 2_z |  |  | 1T22 |  |  |
| _ _ _ VI_CIF_D14/SDMMC1_D1_M1/ETH0_TXCTL M1/SAI0_SDO1_M0/UART8_RX_M1/I2C4_SD A M2/GPIO2 A7 d |  |  | B20 |  |  | SPI2_MOSI_M0/I2C1_SDA_M0/GPIO0 B3_z |  |  | 1T23 |  |  |
| _ _ _ VI CIF D6/ETH0 RXD2 M1/SAI0 LRCK M0/ UART7_RX_M0/UART8_CTSN_M1/I2C8_SDA M2/GPIO2 B7 d |  |  | B21 |  |  | PWR_CTRL2/GPIO0_A4_d |  |  | 1T24 |  |  |
| _ _ VI CIF D15/SDMMC1 D0 M1/ETH0 RXD0 M 1/SAI0_SDO0_M0/UART8_TX_M1/SPI4_CSN1 M3/I2C4 SCL M2/GPIO2 A6 d |  |  | B22 |  |  | LP4_DQS0P_A/LP4X_DQS0P_A/LP5_RD QS0P_A |  |  | 1U1 |  |  |
| _ _ _ _ _ SDMMC0 D3/FSPI1 D3 M0/DSM AUD RN M 0/SAI3_SDI_M3/JTAG_TMS_M0/UART5_CTSN M2/CAN1_TX_M0/I3C1_SDA_M1/GPIO2_A3 d |  |  | B23 |  |  | VSS_76 |  |  | 1U2 |  |  |
| _ SDMMC0 D0/FSPI1 D0 M0/DSM AUD LP M 0/UART0_RX_M1/UART7_RX_M2/I2C8_SCL M0/SPI0_MOSI_M1/CAN0_RX_M0/PWM2_CH 2 M0/GPIO2 A0 d |  |  | B24 |  |  | VSS_77 |  |  | 1U3 |  |  |
| _ _ _ SDMMC0 D1/FSPI1 D1 M0/DSM AUD LN M 0/SAI3_MCLK_M3/UART0_TX_M1/UART7_TX M2/I2C8_SDA_M0/SPI0_MISO_M1/CAN0_T X M0/PWM2 CH3 M0/GPIO2 A1 d |  |  | B25 |  |  | VSS_78 |  |  | 1U4 |  |  |

## Page 32 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH1_TXD3_M1/SDMMC1_CMD_M0/PDM0_S DI2_M2/UART3_TX_M2/SPI1_CSN1_M0/PWM 0 CH0 M1/GPIO1 C0 d |  |  | B26 |  |  | LP4_RESET/LP4X_RESET/LP5_RESET |  |  | 1U5 |  |  |
| _ _ _ _ ETH1_RXD3_M1/SDMMC1_D1_M0/SAI3_LRC K_M1/I2C9_SCL_M1/SPI1_MOSI_M0/PWM1 CH1 M1/GPIO1 B5 d |  |  | B27 |  |  | VSS_79 |  |  | 1U6 |  |  |
| _ _ _ ETH1 TXD1 M1/FSPI1 D1 M1/UART4 RX M 1/UART2_CTSN_M0/SPI2_MISO_M1/PCIE1_B UTTONRSTN/GPIO1 C5 d |  |  | B28 |  |  | PMUIO1_VCC |  |  | 1U20 |  |  |
| _ _ ETH1_PPSCLK_M1/SDMMC1_PWREN_M0/FSP I1_RSTN_M1/FSPI1_CSN1_M1/UART4_RTSN M1/I2C6_SCL_M1/SPI2_CSN1_M1/PWM1_CH 2 M1/GPIO1 C2 u |  |  | B29 |  |  | SDMMC0_DETN/SPI2_CSN1_M0/GPIO0 A7_u |  |  | 1U21 |  |  |
| _ _ _ VSS_4 |  |  | C1 |  |  | AUPLL_CLK_IN_M1/SPI2_CSN0_M0/I2 C0 SCL M0/GPIO0 B0 z |  |  | 1U22 |  |  |
| ETH1 MDIO M1/SAI2 SDI M0/I3C0 SDA M 1/PWM1 CH4 M1/GPIO1 D3 d |  |  | C28 |  |  | _ _ _ _ CLK_32K_IN/CLK0_32K_OUT/I2C6_SC L M0/GPIO0 A2 d |  |  | 1U23 |  |  |
| _ _ _ _ ETH1_RXD1_M1/SAI2_SDO_M0/UART10_TX M1/GPIO1 D0 d |  |  | C29 |  |  | _ _ _ UART0_TX_M0/JTAG_TCK_M1/GPIO0 D4 u |  |  | 1U24 |  |  |
| _ _ LP4 DQ15 B/LP4X DQ15 B/LP5 DQ15 B |  |  | D1 |  |  | _ LP4_DMI0_A/LP4X_DMI0_A/LP5_DMI0 A |  |  | 1V1 |  |  |
| EMMC_D6/SAI3_LRCK_M0/PDM0_CLK1_M1/S PI0 MISO M2/I2C9 SDA M0/GPIO1 A6 u |  |  | D28 |  |  | _ VSS_80 |  |  | 1V2 |  |  |
| _ _ _ _ _ _ LP4 DQ14 B/LP4X DQ14 B/LP5 DQ14 B |  |  | E1 |  |  | LP4 DQ4 A/LP4X DQ4 A/LP5 DQ4 A |  |  | 1V3 |  |  |
| EMMC_D0/FSPI0_D0/SAI0_SCLK_M2/UART7 RTSN M1/I2C2 SCL M1/GPIO1 A0 u |  |  | E28 |  |  | LP5_WCK0N_A |  |  | 1V4 |  |  |
| _ _ _ _ _ EMMC_D1/FSPI0_D1/SAI0_LRCK_M2/UART7 CTSN M1/I2C2 SDA M1/GPIO1 A1 u |  |  | E29 |  |  | LP5_WCK0P_A |  |  | 1V5 |  |  |
| _ _ _ _ _ EMMC_D3/FSPI0_D3/SAI0_SDO2_M2/SAI0_S DI2_M2/PDM0_SDI1_M1/UART7_RX_M1/UAR T6 CTSN M2/GPIO1 A3 u |  |  | F28 |  |  | VSS_81 |  |  | 1V6 |  |  |
| _ _ _ _ LP4 DQ7 B/LP4X DQ7 B/LP5 DQ7 B |  |  | G1 |  |  | I2C0_SDA_M1/UART8_RX_M2/I3C0_S DA M0/GPIO0 C2 d |  |  | 1V24 |  |  |
| EMMC_D5/SAI3_SCLK_M0/PDM0_SDI2_M1/S PI0 MOSI M2/I2C9 SCL M0/GPIO1 A5 u |  |  | G28 |  |  | _ _ _ VSS_82 |  |  | 1W1 |  |  |
| _ _ _ _ _ _ AVSS1_0 |  |  | G29 |  |  | LP4_DQ13_A/LP4X_DQ13_A/LP5_DQ13 A |  |  | 1W2 |  |  |
| LP4_DQS0P_B/LP4X_DQS0P_B/LP5_RDQS0P B |  |  | H1 |  |  | _ VSS_83 |  |  | 1W3 |  |  |
| _ MIPI_DPHY_CSI3_RX_D0P |  |  | H28 |  |  | LP4 DQ5 A/LP4X DQ5 A/LP5 DQ5 A |  |  | 1W4 |  |  |
| MIPI_DPHY_CSI3_RX_D0N |  |  | H29 |  |  | VSS_84 |  |  | 1W5 |  |  |
| MIPI_DPHY_CSI3_RX_D1P |  |  | J28 |  |  | VSS_85 |  |  | 1W6 |  |  |
| MIPI_DPHY_CSI3_RX_D1N |  |  | J29 |  |  | MIPI_DPHY_CSI1/2_RX_AVDD1V8 |  |  | 1W20 |  |  |
| LP4 DQ3 B/LP4X DQ3 B/LP5 DQ3 B |  |  | K1 |  |  | PDM0_CLK1_M0/HDMI_TX_CEC_M1/SP I0_CSN1_M0/PWM0_CH1_M0/GPIO0_C 3 d |  |  | 1W21 |  |  |
| MIPI DPHY CSI3 RX D2P/MIPI DPHY CSI4 RX_D0P |  |  | K28 |  |  | _ SAI0_MCLK_M1/PDM0_CLK0_M0/UART 10_TX_M2/PWM0_CH0_M0/GPIO0_C4 d |  |  | 1W22 |  |  |
| MIPI DPHY CSI3 RX D2N/MIPI DPHY CSI4 RX D0N |  |  | K29 |  |  | SAI0_SDI0_M1/PDM0_SDI0_M0/SPI0 MOSI M0/GPIO0 D0 d |  |  | 1W23 |  |  |
| _ _ LP4 A0 B/LP4X A0 B/LP5 A0 B |  |  | L1 |  |  | _ _ _ I2C2_SCL_M0/UART1_TX_M0/NPU_AV S/PWM1 CH4 M0/GPIO0 B7 d |  |  | 1W24 |  |  |
| MIPI DPHY CSI3 RX D3P/MIPI DPHY CSI4 RX D1P |  |  | L28 |  |  | _ _ _ _ LP4_DQ12_A/LP4X_DQ12_A/LP5_DQ12 A |  |  | 1Y1 |  |  |
| _ _ MIPI DPHY CSI3 RX D3N/MIPI DPHY CSI4 RX D1N |  |  | L29 |  |  | _ VSS_86 |  |  | 1Y2 |  |  |
| _ _ PCIE1_RXP/SATA1_RXP/USB3_OTG1_SSRXP |  |  | M28 |  |  | VSS_87 |  |  | 1Y3 |  |  |
| PCIE1_RXN/SATA1_RXN/USB3_OTG1_SSRXN |  |  | M29 |  |  | VSS_88 |  |  | 1Y4 |  |  |
| LP4 CLKN B/LP4X CLKN B/LP5 CLKN B |  |  | N1 |  |  | VSS_89 |  |  | 1Y5 |  |  |
| PCIE1_TXP/SATA1_TXP/USB3_OTG1_SSTXP |  |  | N28 |  |  | VSS_90 |  |  | 1Y6 |  |  |
| PCIE1_TXN/SATA1_TXN/USB3_OTG1_SSTXN |  |  | N29 |  |  | AVSS_9 |  |  | 1Y20 |  |  |

## Page 33 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LP4 CLKN A/LP4X CLKN A/LP5 CLKN A |  |  | P1 |  |  | SAI0_SCLK_M1/I2C3_SCL_M1/SPI0_C SN0 M0/GPIO0 C6 d |  |  | 1Y21 |  |  |
| PCIE0_TXN/SATA0_TXN |  |  | P28 |  |  | _ _ _ SAI0_SDI2_M1/SAI0_SDO2_M1/PDM0 SDI2_M0/I2C4_SCL_M0/CPUBIG_AVS /PWM1_CH5_M0/UART1_CTSN_M0/GPI O0 D2 d |  |  | 1Y22 |  |  |
| PCIE0_TXP/SATA0_TXP |  |  | P29 |  |  | _ _ SAI0_LRCK_M1/I2C3_SDA_M1/SPI0_C LK M0/GPIO0 C7 d |  |  | 1Y23 |  |  |
| PCIE0_RXP/SATA0_RXP |  |  | R28 |  |  | _ _ _ SDMMC0_PWREN/SDMMC1_DETN_M2/ HDMI_TX_HPDIN_M1/EDP_TX_HPDIN M1/PWM1 CH2 M0/GPIO0 B6 d |  |  | 1Y24 |  |  |
| PCIE0_RXN/SATA0_RXN |  |  | R29 |  |  | _ _ _ _ LP4_DQ15_A/LP4X_DQ15_A/LP5_DQ15 A |  |  | 1AA1 |  |  |
| LP4 A0 A/LP4X A0 A/LP5 A0 A |  |  | T1 |  |  | _ VSS_91 |  |  | 1AA2 |  |  |
| AVSS1_1 |  |  | T28 |  |  | LP4_DQ14_A/LP4X_DQ14_A/LP5_DQ14 A |  |  | 1AA3 |  |  |
| AVSS1_2 |  |  | T29 |  |  | _ VSS_92 |  |  | 1AA4 |  |  |
| LP4 DQ3 A/LP4X DQ3 A/LP5 DQ3 A |  |  | U1 |  |  | LP5_WCK1N_A |  |  | 1AA5 |  |  |
| OSC_XIN |  |  | U28 |  |  | LP5_WCK1P_A |  |  | 1AA6 |  |  |
| OSC_XOUT |  |  | U29 |  |  | HDMI_TX_REXT/EDP_TX_REXT |  |  | 1AA20 |  |  |
| VSS_5 |  |  | V28 |  |  | VSS_93 |  |  | 1AA21 |  |  |
| REF CLK0 OUT/AUPLL CLK IN M0/GPIO0 A 0_d |  |  | V29 |  |  | SAI0_SDO0_M1/DP_HPDIN_M1/UART1 0 RX M2/I3C0 SDA PU M0/GPIO0 C 5 d |  |  | 1AA22 |  |  |
| LP4 DQ0 A/LP4X DQ0 A/LP5 DQ0 A |  |  | W1 |  |  | _ SAI0_SDI3_M1/SAI0_SDO1_M1/PDM0 SDI3_M0/I2C4_SDA_M0/GPU_AVS/P WM2_CH0_M0/UART1_RTSN_M0/GPIO 0 D3 d |  |  | 1AA23 |  |  |
| NPOR |  |  | W28 |  |  | _ _ VSS_94 |  |  | 1AA24 |  |  |
| LP4_DQS0N_A/LP4X_DQS0N_A/LP5_RDQS0N A |  |  | Y1 |  |  | LP4 DQ9 A/LP4X DQ9 A/LP5 DQ9 A |  |  | 1AB1 |  |  |
| _ PWR_CTRL1/TSADC_CTRL_M1/GPIO0_A3_d |  |  | Y28 |  |  | VSS_95 |  |  | 1AB2 |  |  |
| PWR_CTRL3/I2C6_SDA_M0/GPIO0_A5_d |  |  | Y29 |  |  | LP4_DQS1N_A/LP4X_DQS1N_A/LP5_R DQS1N A |  |  | 1AB3 |  |  |
| UART0 RX M0/JTAG TMS M1/GPIO0 D5 u |  |  | AA28 |  |  | _ LP4_DQS1P_A/LP4X_DQS1P_A/LP5_RD QS1P A |  |  | 1AB4 |  |  |
| LP4 DQ7 A/LP4X DQ7 A/LP5 DQ7 A |  |  | AB1 |  |  | _ VSS_96 |  |  | 1AB5 |  |  |
| I2C0 SCL M1/UART8 TX M2/I3C0 SCL M0/ GPIO0 C1 d |  |  | AB28 |  |  | VSS_97 |  |  | 1AB6 |  |  |
| _ _ I2C2_SDA_M0/UART1_RX_M0/CPULIT_AVS/P WM1 CH3 M0/GPIO0 C0 d |  |  | AB29 |  |  | AVSS_10 |  |  | 1AB20 |  |  |
| _ _ _ _ LP4 DQ6 A/LP4X DQ6 A/LP5 DQ6 A |  |  | AC1 |  |  | AVSS_11 |  |  | 1AB21 |  |  |
| SAI0_SDI1_M1/SAI0_SDO3_M1/PDM0_SDI1 M0/SPI0 MISO M0/GPIO0 D1 d |  |  | AC28 |  |  | AVSS_12 |  |  | 1AB22 |  |  |
| _ _ _ _ _ REF CLK1 OUT/I2C1 SCL M1/UART4 TX M 2/PWM1 CH0 M0/GPIO0 B4 d |  |  | AD28 |  |  | AVSS_13 |  |  | 1AB23 |  |  |
| _ _ _ _ REF CLK2 OUT/I2C1 SDA M1/UART4 RX M 2/PWM1 CH1 M0/GPIO0 B5 d |  |  | AD29 |  |  | AVSS_14 |  |  | 1AB24 |  |  |
| _ _ _ _ LP4 DMI1 A/LP4X DMI1 A/LP5 DMI1 A |  |  | AE1 |  |  | VSS_98 |  |  | 1AC1 |  |  |
| MIPI_DPHY_CSI1_RX_D0N |  |  | AE28 |  |  | VSS_99 |  |  | 1AC2 |  |  |
| MIPI_DPHY_CSI1_RX_D0P |  |  | AE29 |  |  | VSS_100 |  |  | 1AC3 |  |  |
| LP4 DQ8 A/LP4X DQ8 A/LP5 DQ8 A |  |  | AF1 |  |  | VSS_101 |  |  | 1AC4 |  |  |
| MIPI_DPHY_CSI1_RX_D1N |  |  | AF28 |  |  | VSS_102 |  |  | 1AC5 |  |  |
| MIPI_DPHY_CSI1_RX_D1P |  |  | AF29 |  |  | UFS_TX_D0N |  |  | 1AC6 |  |  |
| MIPI DPHY CSI1 RX D2N/MIPI DPHY CSI2 RX D0N |  |  | AG28 |  |  | AVSS_15 |  |  | 1AC20 |  |  |
| _ _ MIPI DPHY CSI1 RX D2P/MIPI DPHY CSI2 RX D0P |  |  | AG29 |  |  | AVSS_16 |  |  | 1AC21 |  |  |
| _ _ LP4 DQ11 A/LP4X DQ11 A/LP5 DQ11 A |  |  | AH1 |  |  | MIPI_DPHY_CSI1_RX_CLKP |  |  | 1AC22 |  |  |

## Page 34 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MIPI DPHY CSI1 RX D3N/MIPI DPHY CSI2 RX D1N |  |  | AH28 |  |  | MIPI_DPHY_CSI1_RX_CLKN |  |  | 1AC23 |  |  |
| _ _ MIPI DPHY CSI1 RX D3P/MIPI DPHY CSI2 RX D1P |  |  | AH29 |  |  | AVSS_17 |  |  | 1AC24 |  |  |
| _ _ SAI4_SCLK_M2/VP2_SYNC_OUT/I2C6_SDA M3/SPI4_CLK_M0/CAN1_RX_M1/PWM2_CH3 M1/GPIO4 C7 d |  |  | AJ1 |  |  | LP4_DQ10_A/LP4X_DQ10_A/LP5_DQ10 A |  |  | 1AD1 |  |  |
| _ _ HDMI_TX_D2P/EDP_TX_D2P |  |  | AJ28 |  |  | UFS_RSTN/GPIO4_D0_d |  |  | 1AD2 |  |  |
| AVSS_0 |  |  | AJ29 |  |  | VSS_103 |  |  | 1AD3 |  |  |
| ISP_FLASH_TRIGOUT_M1/SAI4_SDO_M2/VP 0_SYNC_OUT/SATA1_ACTLED_M1/I2C3_SDA M3/SPI4_MOSI_M0/UART6_RX_M3/PWM2_C H5 M1/GPIO4 C5 d |  |  | AK1 |  |  | UFS_TX_D1P |  |  | 1AD4 |  |  |
| _ _ _ DSM AUD LN M1/HDMI TX HPDIN M0/PCIE 1 CLKREQN M3/I2C7 SDA M3/EDP TX HPD IN_M0/UART11_RX_M2/PWM0_CH1_M1/GPI O4 C1 d |  |  | AK2 |  |  | UFS_TX_D1N |  |  | 1AD5 |  |  |
| _ _ DSM AUD LP M1/SAI4 MCLK M2/HDMI TX CEC_M0/I2C7_SCL_M3/SPI4_CSN1_M0/UAR T11 TX M2/PWM1 CH5 M1/GPIO4 C0 d |  |  | AK3 |  |  | UFS_TX_D0P |  |  | 1AD6 |  |  |
| _ _ _ _ _ _ UFS_REFCLK/GPIO4_D1_d |  |  | AK4 |  |  | AVSS_18 |  |  | 1AD2 0 |  |  |
| OSC_UFS_XIN |  |  | AK5 |  |  | MIPI_DPHY_CSI2_RX_CLKP |  |  | 1AD2 1 |  |  |
| AVSS_1 |  |  | AK6 |  |  | MIPI_DPHY_CSI2_RX_CLKN |  |  | 1AD2 2 |  |  |
| UFS_RX_D1P |  |  | AK7 |  |  | AVSS_19 |  |  | 1AD2 3 |  |  |
| UFS_RX_D0P |  |  | AK8 |  |  | AVSS_20 |  |  | 1AD2 4 |  |  |
| USB2_OTG0_DP |  |  | AK9 |  |  | SAI4_SDI_M2/VP1_SYNC_OUT/PCIE0 CLKREQN_M3/SATA0_ACTLED_M1/I2C 6_SCL_M3/SPI4_MISO_M0/CAN1_TX M1/PWM2 CH2 M1/GPIO4 C6 d |  |  | 1AE1 |  |  |
| USB3_OTG0_SSRX1P/DP_TX_D0P |  |  | AK10 |  |  | _ _ _ _ DSM_AUD_RN_M1/HDMI_TX_SDA/I2C 2_SDA_M3/CAN0_RX_M1/UART9_RX M2/PWM2 CH1 M1/GPIO4 C3 d |  |  | 1AE2 |  |  |
| USB3_OTG0_SSTX1N/DP_TX_D1N |  |  | AK11 |  |  | _ _ _ _ VSS_104 |  |  | 1AE3 |  |  |
| USB3_OTG0_SSRX2P/DP_TX_D2P |  |  | AK12 |  |  | AVSS_21 |  |  | 1AE4 |  |  |
| USB3_OTG0_SSTX2N/DP_TX_D3N |  |  | AK13 |  |  | AVSS_22 |  |  | 1AE6 |  |  |
| AVSS_2 |  |  | AK14 |  |  | AVSS_23 |  |  | 1AE20 |  |  |
| MIPI DPHY DSI TX D0N/MIPI CPHY DSI T X TRIO0 A |  |  | AK15 |  |  | AVSS_24 |  |  | 1AE21 |  |  |
| _ _ MIPI DPHY DSI TX D1N/MIPI CPHY DSI T X TRIO0 C |  |  | AK16 |  |  | AVSS_25 |  |  | 1AE23 |  |  |
| _ _ MIPI DPHY DSI TX CLKN/MIPI CPHY DSI TX TRIO1 B |  |  | AK17 |  |  | HDMI_TX_D0P/EDP_TX_D0P |  |  | 1AE24 |  |  |
| _ _ MIPI DPHY DSI TX D2N/MIPI CPHY DSI T X TRIO2 A |  |  | AK18 |  |  | VSS_105 |  |  | 2A1 |  |  |
| _ _ MIPI DPHY DSI TX D3N/MIPI CPHY DSI T X TRIO2 C |  |  | AK19 |  |  | VCCIO2_VCC |  |  | 2A2 |  |  |
| _ _ MIPI DPHY CSI0 RX D0P/MIPI CPHY CSI R X TRIO0 B |  |  | AK20 |  |  | VSS_106 |  |  | 2A3 |  |  |
| _ _ MIPI DPHY CSI0 RX D1P/MIPI CPHY CSI R X TRIO1 A |  |  | AK21 |  |  | VCCIO5_VCC_0 |  |  | 2A4 |  |  |
| _ _ MIPI DPHY CSI0 RX CLKP/MIPI CPHY CSI RX TRIO1 C |  |  | AK22 |  |  | VCCIO5_VCC_1 |  |  | 2A5 |  |  |
| _ _ MIPI DPHY CSI0 RX D2P/MIPI CPHY CSI R X TRIO2 B |  |  | AK23 |  |  | VSS_107 |  |  | 2A6 |  |  |
| _ _ MIPI_DPHY_CSI0_RX_D3P/NO_USE |  |  | AK24 |  |  | VCCIO4_VCC |  |  | 2A7 |  |  |
| AVSS_3 |  |  | AK25 |  |  | VCCIO1_VCC |  |  | 2A8 |  |  |
| HDMI_TX_D3N/EDP_TX_D3N |  |  | AK26 |  |  | VSS_108 |  |  | 2A9 |  |  |

## Page 35 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HDMI_TX_D0N/EDP_TX_D0N |  |  | AK27 |  |  | SARADC_AVDD1V8 |  |  | 2A10 |  |  |
| HDMI_TX_D1P/EDP_TX_D1P |  |  | AK28 |  |  | VSS_109 |  |  | 2A11 |  |  |
| HDMI_TX_D2N/EDP_TX_D2N |  |  | AK29 |  |  | VSS_110 |  |  | 2A12 |  |  |
| VSS_6 |  |  | AL1 |  |  | VSS_111 |  |  | 2B1 |  |  |
| DSM AUD RP M1/HDMI TX SCL/I2C2 SCL M3/CAN0_TX_M1/UART9_TX_M2/PWM2_CH0 M1/GPIO4 C2 d |  |  | AL2 |  |  | DDRPHY_CKE_VDDQ |  |  | 2B2 |  |  |
| _ _ _ ISP_PRELIGHT_TRIG_M1/SAI4_LRCK_M2/DP HPDIN_M0/I2C3_SCL_M3/SPI4_CSN0_M0/U ART6 TX M3/PWM2 CH6 M1/GPIO4 C4 d |  |  | AL3 |  |  | VSS_112 |  |  | 2B3 |  |  |
| _ _ _ _ _ _ AVSS_4 |  |  | AL4 |  |  | VSS_113 |  |  | 2B4 |  |  |
| OSC_UFS_XOUT |  |  | AL5 |  |  | VSS_114 |  |  | 2B5 |  |  |
| UFS_RX_D1N |  |  | AL6 |  |  | VSS_115 |  |  | 2B6 |  |  |
| UFS_RX_D0N |  |  | AL7 |  |  | VSS_116 |  |  | 2B7 |  |  |
| AVSS_5 |  |  | AL8 |  |  | VSS_117 |  |  | 2B8 |  |  |
| USB2_OTG0_DM |  |  | AL9 |  |  | VSS_118 |  |  | 2B9 |  |  |
| USB3_OTG0_SSRX1N/DP_TX_D0N |  |  | AL10 |  |  | VCCIO3_VCC |  |  | 2B10 |  |  |
| USB3_OTG0_SSTX1P/DP_TX_D1P |  |  | AL11 |  |  | VSS_119 |  |  | 2B11 |  |  |
| USB3_OTG0_SSRX2N/DP_TX_D2N |  |  | AL12 |  |  | VSS_120 |  |  | 2B12 |  |  |
| USB3_OTG0_SSTX2P/DP_TX_D3P |  |  | AL13 |  |  | VSS_121 |  |  | 2C1 |  |  |
| AVSS_6 |  |  | AL14 |  |  | DDRPHY_PLL_AVSS |  |  | 2C2 |  |  |
| MIPI DPHY DSI TX D0P/MIPI CPHY DSI T X TRIO0 B |  |  | AL15 |  |  | DDRPHY_PLL_DVDD |  |  | 2C3 |  |  |
| _ _ MIPI DPHY DSI TX D1P/MIPI CPHY DSI T X TRIO1 A |  |  | AL16 |  |  | GPU_DVDD_0 |  |  | 2C4 |  |  |
| _ _ MIPI DPHY DSI TX CLKP/MIPI CPHY DSI T X TRIO1 C |  |  | AL17 |  |  | GPU_DVDD_1 |  |  | 2C5 |  |  |
| _ _ MIPI DPHY DSI TX D2P/MIPI CPHY DSI T X TRIO2 B |  |  | AL18 |  |  | VSS_122 |  |  | 2C6 |  |  |
| _ _ MIPI_DPHY_DSI_TX_D3P/NO_USE |  |  | AL19 |  |  | NPU_DVDD_0 |  |  | 2C7 |  |  |
| MIPI DPHY CSI0 RX D0N/MIPI CPHY CSI RX TRIO0 A |  |  | AL20 |  |  | NPU_DVDD_1 |  |  | 2C8 |  |  |
| _ _ MIPI DPHY CSI0 RX D1N/MIPI CPHY CSI RX TRIO0 C |  |  | AL21 |  |  | NPU_DVDD_2 |  |  | 2C9 |  |  |
| _ _ MIPI DPHY CSI0 RX CLKN/MIPI CPHY CSI RX TRIO1 B |  |  | AL22 |  |  | VSS_123 |  |  | 2C10 |  |  |
| _ _ MIPI DPHY CSI0 RX D2N/MIPI CPHY CSI RX TRIO2 A |  |  | AL23 |  |  | VSS_124 |  |  | 2C11 |  |  |
| _ _ MIPI DPHY CSI0 RX D3N/MIPI CPHY CSI RX TRIO2 C |  |  | AL24 |  |  | VSS_125 |  |  | 2C12 |  |  |
| _ _ AVSS_7 |  |  | AL25 |  |  | DDRPHY_CK_VDDQ |  |  | 2D1 |  |  |
| HDMI_TX_D3P/EDP_TX_D3P |  |  | AL26 |  |  | DDRPHY_PLL_AVDD1V8 |  |  | 2D2 |  |  |
| HDMI_TX_D1N/EDP_TX_D1N |  |  | AL28 |  |  | VSS_126 |  |  | 2D3 |  |  |
| AVSS_8 |  |  | AL29 |  |  | GPU_DVDD_2 |  |  | 2D4 |  |  |
| LP4 DQ8 B/LP4X DQ8 B/LP5 DQ8 B |  |  | 1A1 |  |  | GPU_DVDD_3 |  |  | 2D5 |  |  |
| VSS_7 |  |  | 1A2 |  |  | VSS_127 |  |  | 2D6 |  |  |
| VSS_8 |  |  | 1A3 |  |  | NPU_DVDD_3 |  |  | 2D7 |  |  |
| SPDIF_TX0_M0/FLEXBUS0_D15_M1/UART2_T X_M1/I2C3_SCL_M0/PCIE0_CLKREQN_M2/CA N1 TX M2/GPIO4 B5 d |  |  | 1A4 |  |  | NPU_DVDD_4 |  |  | 2D8 |  |  |
| _ _ _ _ SAI1_SDO1_M0/SAI1_SDI3_M0/PDM1_CLK1 M1/FLEXBUS1_D13_M1/SPI4_CLK_M2/UART 5 TX M1/UART6 RTSN M0/UART2 RTSN M1 /GPIO4 B0 d |  |  | 1A5 |  |  | VSS_128 |  |  | 2D9 |  |  |
| _ _ SAI1_SDI0_M0/SAI4_SDO_M0/PDM1_SDI0 M1/SPI4_CSN0_M2/SPI3_CSN1_M2/PWM2_C H7 M0/GPIO4 B3 d |  |  | 1A6 |  |  | AVSS1_23 |  |  | 2D10 |  |  |

## Page 36 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VO LCDC D21/VO EBC GDOE/ETH0 MDC M 0/PDM1_SDI2_M2/DSMC_DATA14/FLEXBUS0 D6/UART1_RX_M2/UART10_CTSN_M0/PWM 1 CH2 M3/GPIO3 A6 d |  |  | 1A7 |  |  | MIPI_DPHY_CSI3/4_RX_AVDD0V75 |  |  | 2D11 |  |  |
| _ _ _ _ VO_LCDC_D8/VO_EBC_SDDO8/ETH0_TXD2 M0/SAI2_LRCK_M2/DSMC_INT3/FLEXBUS0 D10/FLEXBUS0_CSN_M2/UART11_CTSN_M0/ SPI4_MOSI_M1/I2C9_SDA_M3/PWM2_CH1 M3/GPIO3 C3 d |  |  | 1A8 |  |  | MIPI_DPHY_CSI3/4_RX_AVDD1V8 |  |  | 2D12 |  |  |
| _ _ VO_LCDC_D14/VO_EBC_SDDO14/ETH0_TXD 0_M0/SPDIF_TX1_M0/DSMC_DATA8/FLEXBU S0_D0/UART9_CTSN_M1/PWM1_CH5_M3/GP IO3 B5 d |  |  | 1A9 |  |  | DDRPHY_VDDQ_0 |  |  | 2E1 |  |  |
| _ _ VO_LCDC_D1/VO_EBC_SDDO1/ETH0_RXD3 M0/SAI2_SDI_M2/DSMC_CSN3/FLEXBUS0_D 12/FLEXBUS1_D15_M0/FLEXBUS0_CSN_M3/ UART2_RTSN_M2/SPI4_CSN1_M1/I3C1_SDA M2/PWM2 CH4 M3/GPIO3 D2 d |  |  | 1A10 |  |  | DDRPHY_DVDD_0 |  |  | 2E2 |  |  |
| _ _ _ _ _ VO_LCDC_D18/VO_EBC_SDCE2/ETH0_RXD1 M0/PDM1_CLK0_M2/DSMC_DATA12/FLEXBU S0_D4/UART10_TX_M0/SPI4_CSN0_M1/PWM 1 CH3 M3/GPIO3 B1 d |  |  | 1A11 |  |  | VSS_129 |  |  | 2E3 |  |  |
| _ _ _ _ VO_LCDC_D2/VO_EBC_SDDO2/ETH0_RXCLK M0/SAI2_MCLK_M2/DSMC_CSN2/FLEXBUS0 D11/FLEXBUS1_CSN_M2/SPI4_CLK_M1/I3C 1 SDA PU M2/GPIO3 D1 d |  |  | 1A12 |  |  | GPU_DVDD_4 |  |  | 2E4 |  |  |
| _ _ _ _ _ VI CIF D1/ETH1 TXD3 M0/SAI2 SDO M1/P DM1_SDI0_M0/UART11_TX_M1/SPI1_CSN0 M1/PWM1 CH3 M2/GPIO2 C4 d |  |  | 1A13 |  |  | VSS_130 |  |  | 2E5 |  |  |
| _ _ _ _ ETH1_TXD0_M0/SAI4_SCLK_M3/UART4_CTS N_M0/I2C5_SCL_M2/PWM1_CH5_M2/GPIO2 C6 d |  |  | 1A14 |  |  | VSS_131 |  |  | 2E6 |  |  |
| _ VI CIF D4/ETH1 RXD3 M0/ETH0 PPSCLK M 1/SAI2_MCLK_M1/PDM1_CLK1_M0/UART9_T X_M0/SPI1_CSN1_M1/PWM1_CH1_M2/GPIO2 C1 d |  |  | 1A15 |  |  | LOGIC_DVDD_0 |  |  | 2E7 |  |  |
| _ _ ETH1_RXD0_M0/SAI4_SDO_M3/UART4_RX M0/I2C6_SDA_M2/PWM2_CH1_M2/GPIO2_D 1 d |  |  | 1A16 |  |  | VSS_132 |  |  | 2E8 |  |  |
| _ VI_CIF_D11/SDMMC1_CMD_M1/ETH0_TXD3 M1/SAI0_SDI2_M0/PDM0_SDI1_M3/UART1 CTSN_M1/SPI4_CSN0_M3/PCIE0_CLKREQN M0/GPIO2 B2 d |  |  | 1A17 |  |  | VSS_133 |  |  | 2E9 |  |  |
| _ _ VI CIF D12/SDMMC1 D3 M1/ETH0 TXD0 M 1/SAI0_SDI1_M0/PDM0_SDI2_M3/UART1_RX M1/GPIO2 B1 d |  |  | 1A18 |  |  | AVSS1_24 |  |  | 2E10 |  |  |
| _ _ _ VI CIF CLKI/ETH1 PTP REFCLK M0/ETH0 R XD1_M1/SAI3_SDI_M2/SPDIF_TX1_M1/UART 3 RTSN M0/SPI3 CSN0 M0/CAN1 RX M3/G PIO3 A3 d |  |  | 1A19 |  |  | PCIE1_SATA1_USB3_OTG1_AVDD0V85 |  |  | 2E11 |  |  |
| _ _ VI_CIF_CLKO/ETH1_PPSCLK_M0/ETH0_RXCT L_M1/SAI3_SDO_M2/SPDIF_RX1_M1/UART3 CTSN_M0/SPI3_MISO_M0/CAN1_TX_M3/MI PI TE M1/GPIO3 A2 d |  |  | 1A20 |  |  | PCIE1_SATA1_USB3_OTG1_AVDD1V8 |  |  | 2E12 |  |  |
| _ _ _ _ SDMMC0_CMD/FSPI1_CSN0_M0/SAI3_SDO M3/UART5_RX_M2/I2C5_SDA_M0/SPI0_CSN 0 M1/PWM2 CH4 M0/GPIO2 A4 d |  |  | 1A21 |  |  | DDRPHY_VDDQ_1 |  |  | 2F1 |  |  |
| _ _ _ _ _ SARADC_IN1 |  |  | 1A22 |  |  | DDRPHY_VDDQ_2 |  |  | 2F2 |  |  |
| ETH1_RXCLK_M1/SDMMC1_D2_M0/SAI3_SD O_M1/UART3_CTSN_M2/SPI1_MISO_M0/PCI E0 CLKREQN M1/GPIO1 B6 d |  |  | 1A23 |  |  | DDRPHY_DVDD_1 |  |  | 2F3 |  |  |
| _ _ _ _ ETH1 MDC M1/SAI2 LRCK M0/I3C0 SCL M 1/PWM1 CH3 M1/GPIO1 D2 d |  |  | 1A24 |  |  | VSS_134 |  |  | 2F4 |  |  |
| _ _ _ _ LP4 DMI1 B/LP4X DMI1 B/LP5 DMI1 B |  |  | 1B1 |  |  | VSS_135 |  |  | 2F5 |  |  |

## Page 37 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VSS_9 |  |  | 1B2 |  |  | VSS_136 |  |  | 2F6 |  |  |
| LP4 DQ5 B/LP4X DQ5 B/LP5 DQ5 B |  |  | 1B3 |  |  | LOGIC_MEM_DVDD_0 |  |  | 2F7 |  |  |
| SAI4_LRCK_M0/PDM1_CLK0_M1/FLEXBUS0 D14_M1/SPI3_MISO_M2/UART6_RX_M0/I2C4 SDA M1/CAN0 RX M2/GPIO4 A6 d |  |  | 1B5 |  |  | LOGIC_DVDD_1 |  |  | 2F8 |  |  |
| _ _ _ _ _ _ SAI1_LRCK_M0/FLEXBUS1_D12_M1/SPI4_CS N1_M2/UART5_CTSN_M1/I2C2_SDA_M2/PCI E1 CLKREQN M2/GPIO4 A5 d |  |  | 1B6 |  |  | LOGIC_DVDD_2 |  |  | 2F9 |  |  |
| _ _ _ _ VO_POST_EMPTY/SPDIF_TX0_M1/CAM_CLK2 OUT_M0/SAI4_SDO_M1/DSMC_INT2/FLEXB US0_D14_M0/FLEXBUS1_D13_M0/FLEXBUS0 CSN_M1/UART3_RX_M1/I2C7_SDA_M2/GPI O4 A1 d |  |  | 1B7 |  |  | TSADC_TEST_OUT_TS |  |  | 2F10 |  |  |
| _ _ VO_LCDC_D6/VO_EBC_SDDO6/SAI1_SDO0 M1/DSMC_DATA4/FLEXBUS1_D6/UART8_RX M0/SPI1_MISO_M2/PWM2_CH2_M3/GPIO3_C 5 d |  |  | 1B9 |  |  | PCIE0_SATA0_AVDD0V85 |  |  | 2F11 |  |  |
| _ VO_LCDC_D10/VO_EBC_SDDO10/ETH0_PTP REFCLK_M0/SAI1_SDO2_M1/DSMC_DATA6/F LEXBUS1_D8/UART11_RX_M0/SPI2_MISO_M 2/I2C5 SDA M3/CAN0 RX M3/GPIO3 C1 d |  |  | 1B10 |  |  | PCIE0_SATA0_AVDD1V8 |  |  | 2F12 |  |  |
| _ _ _ _ _ _ SPDIF RX0 M1/CAM CLK1 OUT M0/SAI4 L RCK_M1/DSMC_INT0/FLEXBUS0_D13_M0/FL EXBUS1_D14_M0/FLEXBUS1_CSN_M3/UART3 TX_M1/SPI1_CSN1_M2/I2C7_SCL_M2/MIPI TE M2/GPIO4 A0 d |  |  | 1B12 |  |  | DDRPHY_VDDQ_3 |  |  | 2G1 |  |  |
| _ _ _ _ ISP_PRELIGHT_TRIG_M0/ETH1_MDC_M0/UA RT6 RTSN M1/I2C9 SDA M2/PWM2 CH4 M 2/GPIO2 D4 d |  |  | 1B13 |  |  | DDRPHY_DVDD_2 |  |  | 2G2 |  |  |
| _ _ ISP_FLASH_TRIGOUT_M0/ETH1_MDIO_M0/U ART6_CTSN_M1/I2C9_SCL_M2/PWM2_CH5 M2/GPIO2 D5 d |  |  | 1B15 |  |  | DDRPHY_DVDD_3 |  |  | 2G3 |  |  |
| _ _ VI_CIF_D10/SDMMC1_CLK_M1/ETH0_TXCLK M1/SAI0_SDO2_M0/PDM0_CLK1_M3/UART1 RTSN_M1/SPI4_CLK_M3/PCIE1_CLKREQN M0/GPIO2 B3 d |  |  | 1B16 |  |  | VSS_137 |  |  | 2G4 |  |  |
| _ _ VI_CIF_VSYNC/ETH1_PPSTRIG_M0/ETH0_MD C_M1/SAI3_LRCK_M2/UART3_RX_M0/SPI3 MOSI M0/I2C7 SDA M1/GPIO3 A1 d |  |  | 1B18 |  |  | CPU_BIG_DVDD_0 |  |  | 2G5 |  |  |
| _ _ _ _ _ SARADC_IN2 |  |  | 1B19 |  |  | CPU_BIG_DVDD_1 |  |  | 2G6 |  |  |
| SDMMC0_CLK/FSPI1_CLK_M0/SAI3_SCLK_M 3/TEST_CLK_OUT/UART5_TX_M2/I2C5_SCL M0/SPI0_CLK_M1/I3C1_SDA_PU_M1/GPIO2 A5 d |  |  | 1B21 |  |  | VSS_138 |  |  | 2G7 |  |  |
| _ ETH1_TXCLK_M1/SDMMC1_CLK_M0/SAI3_M CLK_M1/PDM0_CLK0_M2/UART3_RX_M2/GPI O1 C1 d |  |  | 1B22 |  |  | LOGIC_DVDD_3 |  |  | 2G8 |  |  |
| _ _ ETH1 TXD0 M1/FSPI1 D0 M1/UART4 TX M 1/UART2_RTSN_M0/SPI2_MOSI_M1/PCIE0_B UTTONRSTN/GPIO1 C4 d |  |  | 1B23 |  |  | LOGIC_DVDD_4 |  |  | 2G9 |  |  |
| _ _ EMMC_D7/SAI0_SDO0_M2/SAI3_SDI_M0/SPI 0 CLK M2/GPIO1 A7 u |  |  | 1B24 |  |  | VSS_139 |  |  | 2G10 |  |  |
| _ _ _ _ LP4 DQ13 B/LP4X DQ13 B/LP5 DQ13 B |  |  | 1C1 |  |  | PLL_DVDD0V75 |  |  | 2G11 |  |  |
| VSS_10 |  |  | 1C2 |  |  | PLL_AVSS |  |  | 2G12 |  |  |
| LP4 DQ4 B/LP4X DQ4 B/LP5 DQ4 B |  |  | 1C3 |  |  | DDRPHY_VDDQ_4 |  |  | 2H1 |  |  |
| VSS_11 |  |  | 1C4 |  |  | DDRPHY_DVDD_4 |  |  | 2H2 |  |  |
| SAI4_SCLK_M0/PDM1_SDI3_M1/FLEXBUS0 D13_M1/SPI3_MOSI_M2/UART6_TX_M0/I2C4 SCL M1/CAN0 TX M2/GPIO4 A4 d |  |  | 1C5 |  |  | VSS_140 |  |  | 2H3 |  |  |
| _ _ _ _ _ _ SAI1_SCLK_M0/FLEXBUS1_CSN_M4/SPI3_CS N0_M2/UART5_RTSN_M1/I2C2_SCL_M2/PWM 2 CH4 M1/GPIO4 A3 d |  |  | 1C6 |  |  | CPU_LIT_DVDD_0 |  |  | 2H4 |  |  |

## Page 38 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VO_LCDC_D4/VO_EBC_SDDO4/SAI1_SCLK M1/DSMC_DATA2/FLEXBUS1_D4/UART8_RTS N M0/SPI1 CLK M2/GPIO3 C7 d |  |  | 1C7 |  |  | VSS_141 |  |  | 2H5 |  |  |
| _ _ _ _ _ VSS_12 |  |  | 1C9 |  |  | CPU_BIG_DVDD_2 |  |  | 2H6 |  |  |
| VO_LCDC_VSYNC/VO_EBC_SDCLK/SAI1_SDI 3_M1/DSMC_CLKN/FLEXBUS1_CLK/UART5_C TSN_M0/SPI3_MOSI_M1/PWM2_CH6_M3/GPI O3 D6 d |  |  | 1C10 |  |  | CPU_BIG_DVDD_3 |  |  | 2H7 |  |  |
| _ _ VO_LCDC_D3/VO_EBC_SDDO3/SAI1_MCLK M1/DSMC_DATA1/FLEXBUS1_D3/UART8_CTS N_M0/SPI1_CSN0_M2/PWM2_CH3_M3/GPIO3 D0 d |  |  | 1C12 |  |  | LOGIC_DVDD_5 |  |  | 2H8 |  |  |
| _ _ VSS_13 |  |  | 1C13 |  |  | LOGIC_DVDD_6 |  |  | 2H9 |  |  |
| VI CIF D0/ETH1 TXCLK M0/SAI2 SDI M1/P DM1 CLK0 M0/UART11 RX M1/SPI1 CLK M 1/PWM1 CH4 M2/GPIO2 C5 d |  |  | 1C15 |  |  | TVSS |  |  | 2H10 |  |  |
| _ _ _ _ VSS_14 |  |  | 1C16 |  |  | OTP_DVDD0V75 |  |  | 2H11 |  |  |
| VI_CIF_D8/SDMMC1_DETN_M1/ETH0_RXCLK M1/SAI0_MCLK_M0/PDM0_CLK0_M3/UART7 RTSN_M0/SPI4_MISO_M3/SATA1_ACTLED M0/GPIO2 B5 d |  |  | 1C18 |  |  | PLL_AVDD1V8 |  |  | 2H12 |  |  |
| _ _ SARADC_IN3 |  |  | 1C19 |  |  | VSS_142 |  |  | 2J1 |  |  |
| VSS_15 |  |  | 1C21 |  |  | DDRPHY_VDDQ_5 |  |  | 2J2 |  |  |
| ETH1_RXD0_M1/FSPI1_D3_M1/PDM0_SDI1 M2/UART2_RX_M0/I2C8_SDA_M1/SATA_CPD ET/GPIO1 C7 d |  |  | 1C22 |  |  | CPU_LIT_DVDD_1 |  |  | 2J3 |  |  |
| _ _ ETH1_PPSTRIG_M1/SDMMC1_DETN_M0/FSPI 1 CSN0 M1/UART4 CTSN M1/I2C6 SDA M1 /SPI2 CSN0 M1/GPIO1 C3 u |  |  | 1C23 |  |  | CPU_LIT_DVDD_2 |  |  | 2J4 |  |  |
| _ _ _ _ EMMC_D2/FSPI0_D2/SAI0_SDO1_M2/SAI0_S DI3_M2/PDM0_SDI3_M1/UART7_TX_M1/UAR T6 RTSN M2/GPIO1 A2 u |  |  | 1C24 |  |  | VSS_143 |  |  | 2J5 |  |  |
| _ _ _ _ VSS_16 |  |  | 1D1 |  |  | CPU_BIG_DVDD_4 |  |  | 2J6 |  |  |
| LP4 DQ0 B/LP4X DQ0 B/LP5 DQ0 B |  |  | 1D2 |  |  | CPU_BIG_DVDD_5 |  |  | 2J7 |  |  |
| VSS_17 |  |  | 1D3 |  |  | VSS_144 |  |  | 2J8 |  |  |
| LP5_WCK1P_B |  |  | 1D4 |  |  | LOGIC_MEM_DVDD_1 |  |  | 2J9 |  |  |
| VSS_18 |  |  | 1D5 |  |  | OSC_AVDD1V8 |  |  | 2J10 |  |  |
| SAI1_MCLK_M0/SAI4_MCLK_M0/AUPLL_CLK IN M2/PWM2 CH5 M0/GPIO4 A2 d |  |  | 1D6 |  |  | VSS_145 |  |  | 2J11 |  |  |
| _ _ _ _ _ VO_LCDC_D5/VO_EBC_SDDO5/SAI1_LRCK M1/DSMC_DATA3/FLEXBUS1_D5/UART8_TX M0/SPI1 MOSI M2/GPIO3 C6 d |  |  | 1D7 |  |  | VSS_146 |  |  | 2J12 |  |  |
| _ _ _ _ VO_LCDC_D7/VO_EBC_SDDO7/SAI1_SDO1 M1/DSMC_DATA5/FLEXBUS1_D7/UART11_TX M0/SPI2_CSN0_M2/I2C5_SCL_M3/CAN0_TX M3/GPIO3 C4 d |  |  | 1D9 |  |  | VSS_147 |  |  | 2K1 |  |  |
| _ _ _ VO_LCDC_HSYNC/VO_EBC_GDCLK/SAI1_SDI 2_M1/DSMC_CLKP/FLEXBUS1_D0/UART5_TX M0/SPI3_MISO_M1/I2C3_SDA_M2/GPIO3_D 5 d |  |  | 1D10 |  |  | VSS_148 |  |  | 2K2 |  |  |
| _ VO_LCDC_D12/VO_EBC_SDDO12/ETH0_PPS TRIG_M0/SAI1_SDI0_M1/DSMC_DQS0/FLEX BUS1_D10/FLEXBUS1_CSN_M0/UART2_RX_M 2/UART3_CTSN_M1/I2C4_SDA_M3/GPIO3_B 7 d |  |  | 1D12 |  |  | CPU_LIT_DVDD_3 |  |  | 2K3 |  |  |
| _ VO_LCDC_D23/VO_EBC_SDSHR/ETH_CLK0 25M_OUT_M0/SAI4_SDI_M1/DSMC_RDYN/FL EXBUS1_D11/FLEXBUS0_CSN_M0/UART1_CT SN_M2/SPI2_CLK_M2/PWM1_CH0_M3/GPIO3 A4 d |  |  | 1D13 |  |  | CPU_LIT_DVDD_4 |  |  | 2K4 |  |  |
| _ _ VI_CIF_D3/ETH1_RXCLK_M0/ETH0_PPSTRIG M1/SAI2 SCLK M1/PDM1 SDI2 M0/UART1 |  |  | 1D15 |  |  | VSS_149 |  |  | 2K5 |  |  |

## Page 39 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 CTSN M1/SPI1 MOSI M1/PWM1 CH2 M2 |  |  |  |  |  |  |  |  |  |  |  |
| /GPIO2 C2 d |  |  |  |  |  |  |  |  |  |  |  |
| _ _ VI CIF HREF/ETH0 MDIO M1/SAI3 SCLK M 2/UART3 TX M0/SPI3 CLK M0/I2C7 SCL M 1/GPIO3 A0 d |  |  | 1D16 |  |  | CPU_BIG_DVDD_6 |  |  | 2K6 |  |  |
| _ _ CAM CLK1 OUT M1/ETH CLK1 25M OUT M 0/ETH0_MCLK_M1/SAI3_MCLK_M2/SPDIF_RX 0 M2/UART9 RTSN M0/I3C1 SDA PU M0/P WM2 CH6 M2/GPIO2 D6 d |  |  | 1D18 |  |  | CPU_BIG_DVDD_7 |  |  | 2K7 |  |  |
| _ _ _ _ SARADC_IN5 |  |  | 1D19 |  |  | VSS_150 |  |  | 2K8 |  |  |
| SARADC_IN6 |  |  | 1D21 |  |  | VSS_151 |  |  | 2K9 |  |  |
| ETH1_RXCTL_M1/SAI2_SCLK_M0/UART10_R X M1/I3C0 SDA PU M1/GPIO1 D1 d |  |  | 1D22 |  |  | VSS_152 |  |  | 2K10 |  |  |
| _ _ _ _ _ _ EMMC_RSTN/FSPI0_CSN0/UART6_RX_M2/I2 C7 SDA M0/MIPI TE M3/PWM2 CH1 M0/GP IO1 B3 u |  |  | 1D23 |  |  | PMUIO0_VCC1V8 |  |  | 2K11 |  |  |
| _ _ EMMC_D4/SAI0_MCLK_M2/SAI3_MCLK_M0/S PI0 CSN0 M2/GPIO1 A4 u |  |  | 1D24 |  |  | VSS_153 |  |  | 2K12 |  |  |
| _ _ _ _ LP4 DQ12 B/LP4X DQ12 B/LP5 DQ12 B |  |  | 1E1 |  |  | VSS_154 |  |  | 2L1 |  |  |
| VSS_19 |  |  | 1E2 |  |  | PMU_LOGIC_DVDD0V75_0 |  |  | 2L2 |  |  |
| VSS_20 |  |  | 1E3 |  |  | VSS_155 |  |  | 2L3 |  |  |
| LP5_WCK1N_B |  |  | 1E4 |  |  | VSS_156 |  |  | 2L4 |  |  |
| VSS_21 |  |  | 1E5 |  |  | VSS_157 |  |  | 2L5 |  |  |
| VSS_22 |  |  | 1E6 |  |  | VSS_158 |  |  | 2L6 |  |  |
| VO LCDC CLK/VO EBC SDOE/CAM CLK0 O UT_M0/SAI4_SCLK_M1/DSMC_RESETN/FLEX BUS0_D15_M0/FLEXBUS1_D12_M0/FLEXBUS 1 CSN M1/UART5 RTSN M0/SPI3 CSN1 M1 /PWM2 CH7 M3/GPIO3 D7 d |  |  | 1E7 |  |  | VSS_159 |  |  | 2L7 |  |  |
| _ _ _ _ VO_LCDC_D11/VO_EBC_SDDO11/ETH0_PPS CLK_M0/SAI1_SDO3_M1/DSMC_DATA7/FLEX BUS1_D9/UART2_TX_M2/UART3_RTSN_M1/I 2C4 SCL M3/GPIO3 C0 d |  |  | 1E9 |  |  | VSS_160 |  |  | 2L8 |  |  |
| _ _ _ _ VSS_23 |  |  | 1E10 |  |  | VSS_161 |  |  | 2L9 |  |  |
| VO LCDC DEN/VO EBC SDLE/SAI1 SDI1 M 1/DSMC_DATA0/FLEXBUS1_D1/UART5_RX_M 0/SPI3 CLK M1/I2C3 SCL M2/GPIO3 D4 d |  |  | 1E12 |  |  | PMU_LOGIC_DVDD0V75_1 |  |  | 2L10 |  |  |
| _ _ _ _ _ _ VSS_24 |  |  | 1E13 |  |  | MIPI_DPHY_CSI1/2_RX_AVDD0V75 |  |  | 2L11 |  |  |
| CAM CLK2 OUT M1/ETH1 MCLK M0/ETH C LK0 25M OUT M1/SAI0 SDO3 M0/SPDIF T X0_M2/UART9_CTSN_M0/SPI3_CSN1_M0/PW M2 CH7 M2/GPIO2 D7 d |  |  | 1E15 |  |  | VSS_162 |  |  | 2L12 |  |  |
| _ _ _ _ VSS_25 |  |  | 1E16 |  |  | AVSS_26 |  |  | 2M1 |  |  |
| SARADC_IN4 |  |  | 1E18 |  |  | OSC_UFS_AVDD |  |  | 2M2 |  |  |
| SARADC_IN7 |  |  | 1E19 |  |  | VCCIO7_VCC |  |  | 2M3 |  |  |
| ETH1_MCLK_M1/SAI2_MCLK_M0/PDM0_SDI3 M2/SPDIF_RX1_M2/UART10_RTSN_M1/I2C5 SCL M1/GPIO1 D4 d |  |  | 1E21 |  |  | AVSS_27 |  |  | 2M4 |  |  |
| _ _ _ _ ETH CLK1 25M OUT M1/FSPI1 CLK M1/PD M0_CLK1_M2/SPDIF_TX1_M2/UART10_CTSN M1/I2C5_SDA_M1/SPI2_CLK_M1/SATA_MPS WIT/CLK1 32K OUT/GPIO1 D5 d |  |  | 1E22 |  |  | USB3_OTG0_DP_TX_AVDD0V85 |  |  | 2M5 |  |  |
| _ _ _ _ VSS_26 |  |  | 1E23 |  |  | AVSS_28 |  |  | 2M6 |  |  |
| VSS_27 |  |  | 1E24 |  |  | MIPI_DCPHY_AVDD |  |  | 2M7 |  |  |
| LP4_DQS0N_B/LP4X_DQS0N_B/LP5_RDQS0N B |  |  | 1F1 |  |  | MIPI_DCPHY_AVDD1V2 |  |  | 2M8 |  |  |
| _ LP4 DQ1 B/LP4X DQ1 B/LP5 DQ1 B |  |  | 1F2 |  |  | AVSS_29 |  |  | 2M9 |  |  |
| VSS_28 |  |  | 1F3 |  |  | AVSS_30 |  |  | 2M10 |  |  |
| LP4 A4 B/LP4X A4 B/LP5 A4 B |  |  | 1F4 |  |  | AVSS_31 |  |  | 2M11 |  |  |

## Page 40 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VSS_29 |  |  | 1F5 |  |  | AVSS_32 |  |  | 2M12 |  |  |
| VSS_30 |  |  | 1F6 |  |  | AVSS_33 |  |  | 2N1 |  |  |
| VSS_31 |  |  | 1F20 |  |  | UFS_AVDD0V85 |  |  | 2N2 |  |  |
| VSS_32 |  |  | 1F21 |  |  | VCCIO6_VCC |  |  | 2N3 |  |  |
| EMMC_CMD/FSPI0_RSTN/FSPI0_CSN1/UART 6 TX M2/I2C7 SCL M0/GPIO1 B0 u |  |  | 1F22 |  |  | USB3_OTG0_DP_TX_AVDD1V8 |  |  | 2N4 |  |  |
| _ _ _ _ _ _ EMMC_STRB/SAI0_SDI0_M2/SAI3_SDO_M0/ PDM0_SDI0_M1/SPI0_CSN1_M2/GPIO1_B2 d |  |  | 1F23 |  |  | USB3_OTG0_DP_TX_DVDD0V85 |  |  | 2N5 |  |  |
| VSS_33 |  |  | 1F24 |  |  | AVSS_34 |  |  | 2N6 |  |  |
| LP4 DQ2 B/LP4X DQ2 B/LP5 DQ2 B |  |  | 1G1 |  |  | MIPI_DCPHY_VREG |  |  | 2N7 |  |  |
| LP4 A3 B/LP4X A3 B/LP5 A3 B |  |  | 1G2 |  |  | AVSS_35 |  |  | 2N8 |  |  |
| VSS_34 |  |  | 1G3 |  |  | AVSS_36 |  |  | 2N9 |  |  |
| LP5_WCK0N_B |  |  | 1G4 |  |  | HDMI_TX_EDP_TX_AVDDIO1V8 |  |  | 2N10 |  |  |
| LP5_WCK0P_B |  |  | 1G5 |  |  | HDMI_TX_EDP_TX_AVDDD0V75 |  |  | 2N11 |  |  |
| VSS_35 |  |  | 1G6 |  |  | AVSS_37 |  |  | 2N12 |  |  |
| VSS_36 |  |  | 1G20 |  |  | AVSS_38 |  |  | 2P1 |  |  |
| VSS_37 |  |  | 1G21 |  |  | UFS_AVDD1V8 |  |  | 2P2 |  |  |
| VSS_38 |  |  | 1G22 |  |  | USB2_OTG0_VBUSDET |  |  | 2P3 |  |  |
| EMMC_CLK/FSPI0_CLK/SAI0_SDO3_M2/SAI0 SDI1_M2/PDM0_CLK0_M1/PWM2_CH7_M1/ GPIO1 B1 d |  |  | 1G23 |  |  | USB2_OTG_AVDD1V8 |  |  | 2P4 |  |  |
| _ _ VSS_39 |  |  | 1G24 |  |  | USB2_OTG_DVDD0V75 |  |  | 2P5 |  |  |
| VSS_40 |  |  | 1H1 |  |  | AVSS_39 |  |  | 2P6 |  |  |
| VSS_41 |  |  | 1H2 |  |  | USB2_OTG_AVDD3V3 |  |  | 2P7 |  |  |
| VSS_42 |  |  | 1H3 |  |  | MIPI_DCPHY_AVDD1V8 |  |  | 2P8 |  |  |
| VSS_43 |  |  | 1H4 |  |  | AVSS_40 |  |  | 2P9 |  |  |
| LP5_A6_B |  |  | 1H5 |  |  | HDMI_TX_EDP_TX_AVDDCMN1V8 |  |  | 2P10 |  |  |
| VSS_44 |  |  | 1H6 |  |  | HDMI_TX_EDP_TX_AVDDC0V75 |  |  | 2P11 |  |  |
| VSS_45 |  |  | 1H20 |  |  | AVSS_41 |  |  | 2P12 |  |  |
| AVSS1_3 |  |  | 1H21 |  |  | AVSS_42 |  |  | 2R1 |  |  |
| MIPI_DPHY_CSI3_RX_CLKP |  |  | 1H22 |  |  | UFS_TX_REXT |  |  | 2R2 |  |  |
| MIPI_DPHY_CSI3_RX_CLKN |  |  | 1H23 |  |  | USB2_OTG0_REXT |  |  | 2R3 |  |  |
| AVSS1_4 |  |  | 1H24 |  |  | AVSS_43 |  |  | 2R4 |  |  |
| LP4 A1 B/LP4X A1 B/LP5 A1 B |  |  | 1J1 |  |  | AVSS_44 |  |  | 2R5 |  |  |
| VSS_46 |  |  | 1J2 |  |  | USB2_OTG0_ID |  |  | 2R6 |  |  |
| LP4 A2 B/LP4X A2 B/LP5 A2 B |  |  | 1J3 |  |  | AVSS_45 |  |  | 2R7 |  |  |
| VSS_47 |  |  | 1J4 |  |  | AVSS_46 |  |  | 2R8 |  |  |
| LP4_CSN0_B/LP4X_CSN0_B |  |  | 1J5 |  |  | AVSS_47 |  |  | 2R9 |  |  |
| ZQ_B |  |  | 1J6 |  |  | AVSS_48 |  |  | 2R10 |  |  |
| VCCIO0_VCC1V8 |  |  | 1J20 |  |  | AVSS_49 |  |  | 2R11 |  |  |
| AVSS1_5 |  |  | 1J21 |  |  | AVSS_50 |  |  | 2R12 |  |  |
| AVSS1_6 |  |  | 1J22 |  |  | AVSS_51 |  |  | 2T1 |  |  |
| AVSS1_7 |  |  | 1J23 |  |  | DP_TX_AUXP |  |  | 2T2 |  |  |
| AVSS1_8 |  |  | 1J24 |  |  | DP_TX_AUXN |  |  | 2T3 |  |  |
| LP4 CLKP B/LP4X CLKP B/LP5 CLKP B |  |  | 1K1 |  |  | USB2_OTG1_DP |  |  | 2T4 |  |  |
| LP4 CKE0 B/LP4X CKE0 B/LP5 CSN0 B |  |  | 1K2 |  |  | USB2_OTG1_DM |  |  | 2T5 |  |  |
| VSS_48 |  |  | 1K3 |  |  | AVSS_52 |  |  | 2T6 |  |  |
| LP4_CSN1_B/LP4X_CSN1_B |  |  | 1K4 |  |  | USB3_OTG0_REXT/DP_TX_REXT |  |  | 2T7 |  |  |
| LP4 A5 B/LP4X A5 B/LP5 A5 B |  |  | 1K5 |  |  | AVSS_53 |  |  | 2T8 |  |  |
| VSS_49 |  |  | 1K6 |  |  | USB2_OTG1_ID |  |  | 2T9 |  |  |

## Page 41 -- pin table

|  | Pin Name |  |  | Pin |  |  | Pin Name |  |  | Pin |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AVSS1_9 |  |  | 1K20 |  |  | USB2_OTG1_VBUSDET |  |  | 2T10 |  |  |
| AVSS1_10 |  |  | 1K21 |  |  | AVSS_54 |  |  | 2T11 |  |  |
| MIPI_DPHY_CSI4_RX_CLKP |  |  | 1K22 |  |  | HDMI_TX_SBDP/EDP_TX_AUXP |  |  | 2T12 |  |  |
| MIPI_DPHY_CSI4_RX_CLKN |  |  | 1K23 |  |  | AVSS_55 |  |  | 2U1 |  |  |
| AVSS1_11 |  |  | 1K24 |  |  | AVSS_56 |  |  | 2U2 |  |  |
| LP4 CLKP A/LP4X CLKP A/LP5 CLKP A |  |  | 1L1 |  |  | AVSS_57 |  |  | 2U3 |  |  |
| VSS_50 |  |  | 1L2 |  |  | AVSS_58 |  |  | 2U4 |  |  |
| VSS_51 |  |  | 1L3 |  |  | AVSS_59 |  |  | 2U5 |  |  |
| VSS_52 |  |  | 1L4 |  |  | AVSS_60 |  |  | 2U6 |  |  |
| VSS_53 |  |  | 1L5 |  |  | AVSS_61 |  |  | 2U7 |  |  |
| VSS_54 |  |  | 1L6 |  |  | USB2_OTG1_REXT |  |  | 2U8 |  |  |
| AVSS1_12 |  |  | 1L20 |  |  | AVSS_62 |  |  | 2U9 |  |  |
| AVSS1_13 |  |  | 1L21 |  |  | AVSS_63 |  |  | 2U10 |  |  |
| AVSS1_14 |  |  | 1L22 |  |  | AVSS_64 |  |  | 2U11 |  |  |
| PCIE1_REFCLKP |  |  | 1L23 |  |  | HDMI_TX_SBDN/EDP_TX_AUXN |  |  | 2U12 |  |  |
| AVSS1_15 |  |  | 1L24 |  |  | AVSS_65 |  |  | 2V1 |  |  |
| VSS_55 |  |  | 1M1 |  |  | AVSS_66 |  |  | 2V2 |  |  |
| VSS_56 |  |  | 1M2 |  |  | AVSS_67 |  |  | 2V3 |  |  |
| LP4 CKE1 B/LP4X CKE1 B/LP5 CSN1 B |  |  | 1M3 |  |  | AVSS_68 |  |  | 2V4 |  |  |
| VSS_57 |  |  | 1M4 |  |  | AVSS_69 |  |  | 2V5 |  |  |
| LP4 A4 A/LP4X A4 A/LP5 A4 A |  |  | 1M5 |  |  | AVSS_70 |  |  | 2V6 |  |  |
| VSS_58 |  |  | 1M6 |  |  | AVSS_71 |  |  | 2V7 |  |  |
| AVSS1_16 |  |  | 1M20 |  |  | AVSS_72 |  |  | 2V8 |  |  |
| AVSS1_17 |  |  | 1M21 |  |  | AVSS_73 |  |  | 2V9 |  |  |
| AVSS1_18 |  |  | 1M22 |  |  | AVSS_74 |  |  | 2V10 |  |  |
| PCIE1_REFCLKN |  |  | 1M23 |  |  | AVSS_75 |  |  | 2V11 |  |  |
| AVSS1_19 |  |  | 1M24 |  |  | AVSS_76 |  |  | 2V12 |  |  |

## Page 42 -- spec/parameter table

|  | Parameters |  |  | Related Power Group |  |  | Min |  |  | Max |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Supply voltage for CPU |  |  | CPU_BIG_DVDD CPU_LIT_DVDD |  |  | -0.3 |  |  | 1.1 |  |  | V |  |  |
| Supply voltage for GPU |  |  | GPU_DVDD |  |  | -0.3 |  |  | 1.1 |  |  | V |  |  |
| Supply voltage for NPU |  |  | NPU_DVDD |  |  | -0.3 |  |  | 1.1 |  |  | V |  |  |
| Supply voltage for core logic |  |  | LOGIC_DVDD |  |  | -0.3 |  |  | 0.95 |  |  | V |  |  |
| Supply voltage for core memory |  |  | LOGIC_MEM_DVDD |  |  | -0.3 |  |  | 0.95 |  |  | V |  |  |
| 0.75V supply voltage |  |  | PMU_LOGIC_DVDD0V75 PLL DVDD0V75_USB2 OTG DVDD0V75 _ _ HDMI_TX_EDP_TX_AVDDD0V75 HDMI_TX_EDP_TX_AVDDC0V75 MIPI_DPHY_CSI1/2_RX_AVDD0V75 MIPI_DPHY_CSI3/4_RX_AVDD0V75 OTP_DVDD0V75 |  |  | -0.3 |  |  | 0.95 |  |  | V |  |  |
| 0.85V supply voltage |  |  | DDRPHY DVDD_DDRPHY PLL DVDD _ _ USB3_OTG0_DP_TX_DVDD0V85 USB3_OTG0_DP_TX_AVDD0V85 MIPI_DCPHY_VDD PCIE21_PORT0_SATA30_PORT0_AVDD0V85 PCIE21 PORT1 SATA30 PORT1 USB3 OTG1 AVDD0V85 UFS_AVDD0V85 |  |  | -0.3 |  |  | 1.00 |  |  | V |  |  |
| 1.2V supply voltage |  |  | MIPI_DCPHY_AVDD_1V2 |  |  | -0.3 |  |  | 1.35 |  |  | V |  |  |
| 1.8V supply voltage |  |  | OSC AVDD1V8_DDRPHY PLL AVDD1V8 _ _ MIPI_DPHY_CSI1/2_RX_AVDD1V8 MIPI_DPHY_CSI3/4_RX_AVDD1V8 MIPI_DCPHY_AVDD1V8 HDMI_TX_EDP_TX_AVDDCMN1V8 HDMI_TX_EDP_TX_AVDDIO1V8 USB3_OTG0_DP_TX_AVDD1V8 USB2_OTG_AVDD1V8 PCIE21_PORT0_SATA30_PORT0_AVDD1V8 PCIE21 PORT1 SATA30 PORT1 USB3 OTG1 AVDD1V8 SARADC AVDD1V8_PLL AVDD1V8 _ UFS_AVDD1V8 |  |  | -0.5 |  |  | 1.98 |  |  | V |  |  |
| 3.3V supply voltage |  |  | USB2_OTG_AVDD3V3 |  |  | -0.5 |  |  | 3.63 |  |  | V |  |  |
| 1.8V only GPIO supply voltage |  |  | PMUIO0_VCC1V8 |  |  | -0.5 |  |  | 1.98 |  |  | V |  |  |

## Page 43 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Min(1) |  |  | Typ |  |  | Max(1) |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Voltage for CPU BigCore(2) |  |  | CPU_BIG_DVDD |  |  | 0.675 |  |  | 0.75 |  |  | 0.9975 |  |  | V |  |  |
| Voltage for CPU LitCore and CCI(2) |  |  | CPU_LIT_DVDD |  |  | 0.675 |  |  | 0.75 |  |  | 0.9975 |  |  | V |  |  |
| Voltage for GPU(2) |  |  | GPU_DVDD |  |  | 0.675 |  |  | 0.75 |  |  | 0.919 |  |  | V |  |  |
| Voltage for NPU(2) |  |  | NPU_DVDD |  |  | 0.689 |  |  | 0.75 |  |  | 0.919 |  |  | V |  |  |
| Voltage for Logic Memory |  |  | LOGIC_MEM_DVDD |  |  | 0.675 |  |  | 0.75 |  |  | 0.825 |  |  | V |  |  |
| Voltage for PMU |  |  | PMU_LOGIC_DVDD0V75 |  |  | 0.675 |  |  | 0.75 |  |  | 0.825 |  |  | V |  |  |
| Digital GPIO Power (1.8V only) |  |  | PMUIO0 VCC1V8_VCCIO0 VCC1V8 |  |  | 1.65 |  |  | 1.8 |  |  | 1.95 |  |  | V |  |  |
| Digital GPIO Power (3.3V/1.8V) |  |  | _ PMUIO1 VCC_VCCIO1 VCC _ VCCIO2 VCC_VCCIO3 VCC _ VCCIO4 VCC_VCCIO5 VCC _ VCCIO6 VCC |  |  | 2.7 1.65 |  |  | 3.3 1.8 |  |  | 3.6 1.95 |  |  | V |  |  |
| Digital GPIO Power (1.8V/1.2V) |  |  | _ OSC_UFS_AVDD VCCIO7 VCC |  |  | 1.08 1.65 |  |  | 1.2 1.8 |  |  | 1.32 1.95 |  |  | V |  |  |
| DDR CH0 Logic power(0.75V) |  |  | _ DDRPHY_DVDD |  |  | 0.675 |  |  | 0.75 |  |  | 0.9 |  |  | V |  |  |
| DDR_CH0_PLL_power(0.75V) |  |  | DDRPHY_PLL_DVDD |  |  | 0.675 |  |  | 0.75 |  |  | 0.8925 |  |  | V |  |  |
| DDR_CH0_PLL_power(1.8V) |  |  | DDRPHY_PLL_AVDD1V8 |  |  | 1.62 |  |  | 1.8 |  |  | 1.98 |  |  | V |  |  |
| LPDDR4 IO VDDQ power |  |  | DDRPHY VDDQ_DDRPHY CK VDDQ |  |  | 0.57 |  |  | 0.6 |  |  | 0.65 |  |  | V |  |  |
| LPDDR4 Retention IO VDDQ Power |  |  | _ _ DDRPHY_CKE_VDDQ |  |  | 1.06 |  |  | 1.1 |  |  | 1.17 |  |  | V |  |  |
| LPDDR5 IO VDDQ power |  |  | DDRPHY VDDQ_DDRPHY CK VDDQ |  |  | 0.47 |  |  | 0.5 |  |  | 0.57 |  |  | V |  |  |
| LPDDR5 Retention IO VDDQ Power |  |  | _ _ DDRPHY_CKE_VDDQ |  |  | 1.01 |  |  | 1.05 |  |  | 1.12 |  |  | V |  |  |
| PLL Analog Power(0.75V) |  |  | PLL_DVDD0V75 |  |  | 0.675 |  |  | 0.75 |  |  | 0.8925 |  |  | V |  |  |
| PLL Analog Power(1.8V) |  |  | PLL_AVDD1V8 |  |  | 1.62 |  |  | 1.8 |  |  | 1.98 |  |  | V |  |  |
| USB 2.0 Analog Power (0.75V) |  |  | USB2_OTG_DVDD0V75 |  |  | 0.6975 |  |  | 0.75 |  |  | 0.825 |  |  | V |  |  |
| USB 2.0 Analog Power (1.8V) |  |  | USB2_OTG_AVDD1V8 |  |  | 1.674 |  |  | 1.8 |  |  | 1.98 |  |  | V |  |  |

## Page 44 -- spec/parameter table

|  | Parameters |  |  |  | Symbol |  |  | Min |  |  | Typ |  |  | Max |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Digital 3.3V/1.8V GPIO @3.3V |  | Input Low Voltage for CMOS operation |  | VIL |  |  | VSS-0.3 |  |  | NA |  |  | 0.8 |  |  | V |  |  |
|  |  | Input High Voltage for CMOS operation |  | VIH |  |  | 2.0 |  |  | NA |  |  | DVDD+0.3 |  |  | V |  |  |
|  |  | Input Low Voltage for Schmitt Trigger operation |  | VIL |  |  | VSS-0.3 |  |  | NA |  |  | 0.7 |  |  | V |  |  |

## Page 45 -- spec/parameter table

| Parameters |  |  |  | Symbol |  |  | Min |  |  | Typ |  |  | Max |  |  | Unit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Input High Voltage for Schmitt Trigger operation |  | VIH |  |  | 2.1 |  |  | NA |  |  | DVDD+0.3 |  |  | V |  |
|  | Output Low Voltage |  | VOL |  |  | VSS |  |  | NA |  |  | 0.25*DVDD |  |  | V |  |
|  | Output High Voltage |  | VOH |  |  | 0.75*DVDD |  |  | NA |  |  | DVDD |  |  | V |  |
|  | Pullup Resistor |  | RRPU |  |  | 10 |  |  | NA |  |  | 100 |  |  | Kohm |  |
|  | Pulldown Resistor |  | RRPD |  |  | 10 |  |  | NA |  |  | 100 |  |  | Kohm |  |
| Digital 3.3V/1.8V GPIO @1.8V | Input Low Voltage |  | VIL |  |  | VSS-0.3 |  |  | NA |  |  | 0.3*DVDD |  |  | V |  |
|  | Input High Voltage |  | VIH |  |  | 0.7*DVDD |  |  | NA |  |  | DVDD+0.3 |  |  | V |  |
|  | Output Low Voltage |  | VOL |  |  | VSS |  |  | NA |  |  | 0.25*DVDD |  |  | V |  |
|  | Output High Voltage |  | VOH |  |  | 0.75*DVDD |  |  | NA |  |  | DVDD |  |  | V |  |
|  | Pullup Resistor |  | RRPU |  |  | 10 |  |  | NA |  |  | 50 |  |  | Kohm |  |
|  | Pulldown Resistor |  | RRPD |  |  | 10 |  |  | NA |  |  | 50 |  |  | Kohm |  |
| Digital 1.8V only and Digital 1.8V/1.2V GPIO @1.8V | Input Low Voltage |  | VIL |  |  | VSS-0.3 |  |  | NA |  |  | 0.3*DVDD |  |  | V |  |
|  | Input High Voltage |  | VIH |  |  | 0.7*DVDD |  |  | NA |  |  | DVDD+0.3 |  |  | V |  |
|  | Output Low Voltage |  | VOL |  |  | VSS |  |  | NA |  |  | 0.25*DVDD |  |  | V |  |
|  | Output High Voltage |  | VOH |  |  | 0.75*DVDD |  |  | NA |  |  | DVDD |  |  | V |  |
|  | Pullup Resistor |  | RRPU |  |  | 10 |  |  | NA |  |  | 50 |  |  | Kohm |  |
|  | Pulldown Resistor |  | RRPD |  |  | 10 |  |  | NA |  |  | 50 |  |  | Kohm |  |
| Digital 1.8V/1.2V GPIO @1.2V | Input Low Voltage |  | VIL |  |  | VSS-0.3 |  |  | NA |  |  | 0.3*DVDD |  |  | V |  |
|  | Input High Voltage |  | VIH |  |  | 0.7*DVDD |  |  | NA |  |  | DVDD+0.3 |  |  | V |  |
|  | Output Low Voltage |  | VOL |  |  | VSS-0.3 |  |  | NA |  |  | 0.25*DVDD |  |  | V |  |
|  | Output High Voltage |  | VOH |  |  | 0.75*DVDD |  |  | NA |  |  | DVDD+0.3 |  |  | V |  |
|  | Pullup Resistor |  | RRPU |  |  | 10 |  |  | NA |  |  | 100 |  |  | Kohm |  |
|  | Pulldown Resistor |  | RRPD |  |  | 10 |  |  | NA |  |  | 100 |  |  | Kohm |  |
| VCCIO0 @1.8V | Input Low Voltage |  | VIL |  |  | VSS |  |  | NA |  |  | 0.35*DVDD |  |  | V |  |
|  | Input High Voltage |  | VIH |  |  | 0.65*DVDD |  |  | NA |  |  | DVDD |  |  | V |  |
|  | Output Low Voltage |  | VOL |  |  | VSS |  |  | NA |  |  | 0.45 |  |  | V |  |
|  | Output High Voltage |  | VOH |  |  | DVDD-0.45 |  |  | NA |  |  | DVDD |  |  | V |  |
|  | Pullup Resistor |  | RRPU |  |  | 10 |  |  | NA |  |  | 50 |  |  | Kohm |  |
|  | Pulldown Resistor |  | RRPD |  |  | 10 |  |  | NA |  |  | 50 |  |  | Kohm |  |
| DDR IO | Input Low Voltage |  | VIL |  |  | NA |  |  | NA |  |  | Vref-0.14 |  |  | V |  |
|  | Input High Voltage |  | VIH |  |  | Vref+0.14 |  |  | NA |  |  | NA |  |  | V |  |
|  | Output Log Voltage |  | VOL |  |  | NA |  |  | NA |  |  | 0.2 |  |  | V |  |
|  | Output High Voltage |  | VOH |  |  | 0.25 |  |  | NA |  |  | NA |  |  | V |  |
|  | Input Low Current |  | IIL |  |  | -100/-500 |  |  | NA |  |  | 100/500 |  |  | Room/Hot uA |  |
|  | Input High Current |  | IIH |  |  | -100/-500 |  |  | NA |  |  | 100/500 |  |  | Room/Hot uA |  |

## Page 45 -- spec/parameter table

| Parameters |  |  |  | Symbol |  |  | Test condition |  |  | Min |  |  | Typ |  |  | Max |  |  | Unit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Digital 3.3V/1.8V | Input leakage current |  | IPAD |  |  | DVDD=Max, VPAD=0V or DVDD |  |  | -10 |  |  | NA |  |  | 10 |  |  | uA |  |

## Page 46 -- spec/parameter table

|  | Parameters |  |  |  | Symbol |  |  | Test condition |  |  | Min |  |  | Typ | Max |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GPIO @3.3V |  | Input Hysteresis for Schmitt Trigger Operation |  | VH |  |  |  |  |  | 0.2 |  |  | NA |  | NA |  | V |  |  |
|  |  | Input pullup resistor current |  | IRPU |  |  | VPAD = 0V |  |  | -20 |  |  | NA |  | -180 |  | uA |  |  |
|  |  | Input pulldown resistor current |  | IRPD |  |  | VPAD = DVDD |  |  | 20 |  |  | NA |  | 180 |  | uA |  |  |
| Digital 3.3V/1.8V GPIO @1.8V |  | Input leakage current |  | IPAD |  |  | DVDD=Max, VPAD=0V or DVDD |  |  | -10 |  |  | NA |  | 10 |  | uA |  |  |
|  |  | Input Hysteresis for Schmitt Trigger Operation |  | VH |  |  |  |  |  | 0.1* DVDD |  |  | NA |  | NA |  | V |  |  |
|  |  | Input pullup resistor current |  | IRPU |  |  | VPAD = 0V |  |  | -20 |  |  | NA |  | -180 |  | uA |  |  |
|  |  | Input pulldown resistor current |  | IRPD |  |  | VPAD = DVDD |  |  | 20 |  |  | NA |  | 180 |  | uA |  |  |
| Digital 1.8V only and Digital 1.8V/1.2V GPIO @1.8V |  | Input leakage current |  | IPAD |  |  | DVDD=Max, VPAD=0V or DVDD |  |  | -10 |  |  | NA |  | 10 |  | uA |  |  |
|  |  | Input Hysteresis for Schmitt Trigger Operation |  | VH |  |  |  |  |  | 0.1* DVDD |  |  | NA |  | NA |  | V |  |  |
|  |  | Input pullup resistor current |  | IRPU |  |  | VPAD = 0V |  |  | -20 |  |  | NA |  | -170 |  | uA |  |  |
|  |  | Input pulldown resistor current |  | IRPD |  |  | VPAD = DVDD |  |  | 20 |  |  | NA |  | 170 |  | uA |  |  |
| Digital 1.8V/1.2V GPIO @1.2V |  | Input leakage current |  | IPAD |  |  | DVDD=Max, VPAD=0V or DVDD |  |  | -10 |  |  | NA |  | 10 |  | uA |  |  |
|  |  | Input Hysteresis for Schmitt Trigger Operation |  | VH |  |  |  |  |  | 0.1* DVDD |  |  | NA |  | NA |  | V |  |  |
|  |  | Input pullup resistor current |  | IRPU |  |  | VPAD = 0V |  |  | -10 |  |  | NA |  | -100 |  | uA |  |  |
|  |  | Input pulldown resistor current |  | IRPD |  |  | VPAD = DVDD |  |  | 10 |  |  | NA |  | 100 |  | uA |  |  |
| VCCIO0 IO @1.8V |  | Input leakage current |  | IPAD |  |  | DVDD=Max, VPAD=0V or DVDD |  |  | -10 |  |  | NA |  | 10 |  | uA |  |  |
|  |  | Input Hysteresis for Schmitt Trigger Operation |  | VH |  |  |  |  |  | 0.1* DVDD |  |  | NA |  | NA |  | V |  |  |
|  |  | Input pullup resistor current |  | IRPU |  |  | VPAD = 0V |  |  | -20 |  |  | NA |  | -170 |  | uA |  |  |
|  |  | Input pulldown resistor current |  | IRPD |  |  | VPAD = DVDD |  |  | 20 |  |  | NA |  | 170 |  | uA |  |  |

## Page 46 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Test condition |  |  | Min |  |  | Typ | Max |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Input clock frequency |  |  | FFIN |  |  |  |  |  | 4.5 |  |  | - |  | 300 |  | MHz |  |  |
| Reference frequency(FFIN/p) |  |  | FFREE |  |  |  |  |  | 4.5 |  |  | 7 |  | 12 |  | MHz |  |  |
| Frequency of PLL’s output |  |  | FFOUT |  |  |  |  |  | 35.2 |  |  | - |  | 4500 |  | MHz |  |  |
| Frequency of VCO’s output |  |  | FFVCO |  |  |  |  |  | 2250 |  |  | - |  | 4500 |  | MHz |  |  |
| Lock time |  |  | TLT |  |  | Measured at all FFIN and FFOUT range. RESETB=High |  |  | - |  |  | - |  | 150 |  | Cycles |  |  |

## Page 47 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Test condition |  |  | Min |  |  | Typ |  | Max |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Input clock frequency |  |  | FFIN |  |  |  |  |  | 4.5 |  |  | - |  |  | 300 |  | MHz |  |  |
| Reference frequency(FFIN/p) |  |  | FFREE |  |  |  |  |  | 4.5 |  |  | 20 |  |  | 30 |  | MHz |  |  |
| Frequency of PLL’s output |  |  | FFOUT |  |  |  |  |  | 35.2 |  |  | - |  |  | 4500 |  | MHz |  |  |
| Frequency of VCO’s output |  |  | FFVCO |  |  |  |  |  | 2250 |  |  | - |  |  | 4500 |  | MHz |  |  |
| Lock time |  |  | TLT |  |  | Measured at all FFIN and FFOUT range. RESETB=High |  |  | - |  |  | - |  |  | 500 |  | Cycles |  |  |

## Page 47 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Test condition |  |  | Min |  |  | Typ |  | Max |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Input clock frequency |  |  | FFIN |  |  |  |  |  | 6 |  |  | - |  |  | 300 |  | MHz |  |  |
| Reference frequency(FFIN/p) |  |  | FFREE |  |  |  |  |  | 6 |  |  | 20 |  |  | 30 |  | MHz |  |  |
| Frequency of PLL’s output |  |  | FFOUT |  |  |  |  |  | 51.6 |  |  | - |  |  | 6600 |  | MHz |  |  |
| Frequency of VCO’s output |  |  | FFVCO |  |  |  |  |  | 3300 |  |  | - |  |  | 6600 |  | MHz |  |  |
| Lock time |  |  | TLT |  |  | Measured at all FFIN and FFOUT range. RESETB=High |  |  | - |  |  | - |  |  | 500 |  | Cycles |  |  |

## Page 47 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Min |  |  | Typ |  | Max |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Transmitter |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Differential Peak-Peak TX Output Voltage Swing |  |  | VTX_DIFF_PP |  |  | 800 |  |  | 1000 |  | 1200 |  |  | mV |  |  |
| Differential Peak-Peak Low Power TX Output Voltage Swing |  |  | VTX_DIFF_PP_LOW |  |  | 400 |  |  | NA |  | 1200 |  |  | mV |  |  |
| The output impedance |  |  | RTX_DIFF_DC |  |  | 80 |  |  | 100 |  | 120 |  |  | ohm |  |  |
| Single Ended Output Resistance Matching |  |  | RTX_DC_OFFSET |  |  | NA |  |  | NA |  | 5 |  |  | % |  |  |
| Transmitter output common mode voltage |  |  | VTX_DC_CM |  |  | 400 |  |  | NA |  | 800 |  |  | mV |  |  |
| Maximum mismatch between TXP and TXM for both time and amp |  |  | VTX_CM_AC_PP_ACTIVE |  |  | NA |  |  | NA |  | 50 |  |  | mV |  |  |
| The amount of voltage change allowed during Receiver Detection |  |  | VTX_RCV_DETECT |  |  | NA |  |  | NA |  | 600 |  |  | mV |  |  |
| TX de-emphasis |  |  | VTX_DE_RATIO |  |  | 3.0 |  |  | 3.5 |  | 4.0 |  |  | dB |  |  |
| AC Coupling Capacitor(USB3.2 Gen1x1/PCIe) |  |  | CAC_COUPLING |  |  | 75 |  |  | NA |  | 200 |  |  | nF |  |  |
| AC Coupling Capacitor(SATA) |  |  |  |  |  | 6 |  |  | NA |  | 12 |  |  | nF |  |  |
| Output rising time for 20% to 80% |  |  | Tr |  |  | 25 |  |  | NA |  | NA |  |  | ps |  |  |
| Output falling time for 20% to 80% |  |  | Tf |  |  | 25 |  |  | NA |  | NA |  |  | ps |  |  |
| Transmitter short circuit limit |  |  | ITX_SHORT |  |  | NA |  |  | NA |  | 20 |  |  | mA |  |  |
| Output differential skew |  |  | TSKEW_DIFF |  |  | -15 |  |  | NA |  | 15 |  |  | ps |  |  |
| Receiver |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Input Voltage Swing |  |  | VRXDPP_C |  |  | 250 |  |  | NA |  | 1200 |  |  | mVpp |  |  |
| The input differential impedance |  |  | RRXD_C |  |  | 80 |  |  | 100 |  | 120 |  |  | Ohm |  |  |
| Single Ended input Resistance Matching |  |  | RRXD_C_MS |  |  | NA |  |  | NA |  | 5 |  |  | % |  |  |

## Page 48 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Description |  |  | Test condition |  |  | Min | Typ |  |  | Max | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LP-RX |  |  | VIH |  |  | Logic1 input voltage |  |  | All conditions |  |  | 880 |  | NA |  | NA |  | mV |  |
|  |  |  | VIL |  |  | Logic0 input voltage, not in ULPS state |  |  | All conditions |  |  | NA |  | NA |  | 550 |  | mV |  |
| Skew Calibration |  |  | Tskewcal (initial) |  |  | Duration for which the transmitter drives the skew- calibration pattern in the initial skew calibration mode |  |  | >1.5Gbps |  |  | NA |  | NA |  | 100 |  | us |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 2^15 |  | NA |  | NA |  | UI |  |
|  |  |  | Tskewcal (periodic) |  |  | Duration for which the transmitter drives the skew- calibration pattern in the periodic skew calibration mode |  |  | >1.5Gbps (optional) |  |  | NA |  | NA |  | 10 |  | us |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 2^13 |  | NA |  | NA |  | UI |  |

## Page 48 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Min |  | Typ |  |  | Max |  |  | Units |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Common-mode interference beyond 450 MHz |  |  | ΔVCMRX(HF) |  |  | NA |  |  | NA |  | 100 |  |  | mV |  |  |
|  |  |  |  |  |  | NA |  |  | NA |  | 50 |  |  | mV |  |  |
| Common-mode interference 50MHz-450MHz |  |  | ΔVCMRX(LF) |  |  | -50 |  |  | NA |  | 50 |  |  | mV |  |  |
|  |  |  |  |  |  | -25 |  |  | NA |  | 25 |  |  | mV |  |  |
| Common-mode termination |  |  | CCM |  |  | NA |  |  | NA |  | 60 |  |  | pF |  |  |
| Input pulse rejection |  |  | eSPIKE |  |  | NA |  |  | NA |  | 300 |  |  | V.ps |  |  |
| Minimum pulse width response |  |  | TMIN-RX |  |  | 20 |  |  | NA |  | NA |  |  | ns |  |  |
| Peak interference amplitude |  |  | VINT |  |  | NA |  |  | NA |  | 200 |  |  | mV |  |  |
| Interference frequency |  |  | fINT |  |  | 450 |  |  | NA |  | NA |  |  | MHz |  |  |

## Page 48 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Test condition |  |  | Min | Typ |  |  | Max | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Resolution |  |  |  |  |  |  |  |  | NA |  | 12 |  | NA |  | Bit |  |
| Anglog Input Range |  |  | AIN |  |  |  |  |  | AVSS18 |  | NA |  | AVDD18 |  | V |  |
| Differential Non-Linearity |  |  | DNL |  |  | PD = Low Fs = 1MS/s FCLK = 20MHz FSOC = 1MHz FAIN = 10kHz ramp wave |  |  | NA |  | ±1.0 |  | ±3.0 |  | LSB |  |
| Integral Non-Linearity |  |  | INL |  |  |  |  |  | NA |  | ±2.0 |  | ±6.0 |  | LSB |  |
| Top Offset Voltage Error |  |  | EOT |  |  |  |  |  | NA |  | ±10 |  | ±20 |  | LSB |  |
| Bottom Offset Voltage Error |  |  | EOB |  |  |  |  |  | NA |  | ±10 |  | ±20 |  | LSB |  |

## Page 48 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Test condition |  |  | Mi | n |  | Typ |  |  | Max | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Accuracy from -40℃ to 125℃ |  |  | TJACC |  |  | Temp: -40 ~ 125℃ Supply: 1.62V ~ 1.98V |  |  | NA |  |  | ±3 |  |  | ±5 |  | ℃ |  |
| Sensing Temperature Range |  |  | TRANGE |  |  |  |  |  | -40 |  |  | NA |  |  | 125 |  | ℃ |  |

## Page 49 -- spec/parameter table

|  | Parameters |  |  | Symbol |  |  | Test condition |  |  | Min |  |  | Typ |  |  | Max |  |  | Unit |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Resolution |  |  | TLSB |  |  |  |  |  | NA |  |  | 1 |  |  | NA |  |  | ℃ |  |  |

## Page 50 -- spec/parameter table

| Parameter | Symbol | Typical | Unit | Note |
|---|---|---|---|---|
| Junction-to-ambient thermal resistance | 𝜽 𝑱𝑨 | 15.84 | (℃/𝑾) | (1) |
| Junction-to-board thermal resistance | 𝜽 𝑱𝑩 | 6.96 | (℃/𝑾) | (2) |
| Junction-to-case thermal resistance | 𝜽 𝑱𝑪 | 0.67 | (℃/𝑾) | (3) |
| Thermal characterization parameter | ψ JT | 0.031 | (℃/𝑾) | (4) |

