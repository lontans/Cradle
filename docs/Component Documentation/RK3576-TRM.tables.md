# Ported tables: Rockchip RK3576 TRM V1.2 Part1.pdf

Mechanically extracted pin tables and spec/parameter tables -- cell contents are verbatim from the PDF, not reworded or interpreted. Review before trusting (table detection can misparse merged cells or footnote markers) and fold the relevant parts into `docs/components/<PART>.md` by hand, including the Cradle Wiring and Status columns that only a real design decision can fill in.

## Page 762 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| mcujtag tckm0 _ | I | SDMMC0 D2/FSPI1 D2 M0/DSM AUD _ _ _ _ _ RP M0/SAI3 LRCK M3/JTAG TCK M0/U _ _ _ _ _ ART5 RTSN M2/SPI0 CSN1 M1/CAN1 M_ 0/I3C1_ M1_ /GPIO2_ _ RX SCL A2 d _ _ _ _ _ | TOP IOC GPIO2A IOMUX S _ _ _ _ EL L[11:8] = 4’h9 _ |
| mcujtag tmsm0 _ | I/O | SDMMC0 D3/FSPI1 D3 M0/DSM AUD _ _ _ _ _ RN M0/SAI3 SDI M3/JTAG TMS M0/UA _ _ _ _ _ RT5 CTSN M2/CAN1 TX M0/I3C1 SDA _ _ _ _ _ M1/GPIO2 A3 d | TOP IOC GPIO2A IOMUX S _ _ _ _ EL L[15:12] = 4’h9 _ |
| mcujtag tckm1 _ | I | _ _ _ UART0 TX M0/JTAG TCK M1/GPIO0 D4 _ _ _ _ _ u | PMU1 IOC GPIO0D IOMUX _ _ _ _ SEL H[3:0] = 4’ha |
| mcujtag tmsm1 _ | I/O | _ UART0 RX M0/JTAG TMS M1/GPIO0 D _ _ _ _ _ 5 u | _ PMU1 IOC GPIO0D IOMUX _ _ _ _ SEL H[7:4] = 4’ha |

## Page 913 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| AUDIO DSM L P _ _ _ | O | SDMMC0 D0/FSPI1 D0 M0/DSM A _ _ _ _ UD LP M0/UART0 RX M1/UART7 R _ _ _ _ _ X M2/I2C8 SCL M0/SPI0 MOSI M1 _ _ _ _ _ /CAN0 RX M0/PWM2 CH2 M0/GPIO _ _ _ _ 2 A0 d | TOP IOC GPIO2A IOMUX S _ _ _ _ EL L[3:0]=4’h3 _ |
| AUDIO DSM L N _ _ _ | O | _ _ SDMMC0 D1/FSPI1 D1 M0/DSM A _ _ _ _ UD LN M0/SAI3 MCLK M3/UART0 _ _ _ _ _ TX M1/UART7 TX M2/I2C8 SDA M _ _ _ _ _ 0/SPI0 MISO M1/CAN0 TX M0/PW _ _ _ _ M2 CH3 M0/GPIO2 A1 d _ _ _ _ | TOP IOC GPIO2A IOMUX S _ _ _ _ EL L[7:4]=4’h3 _ |
| AUDIO DSM R P _ _ _ | O | SDMMC0 D2/FSPI1 D2 M0/DSM A _ _ _ _ UD RP M0/SAI3 LRCK M3/JTAG TC _ _ _ _ _ K M0/UART5 RTSN M2/SPI0 CSN1 _ _ _ _ M1/CAN1 RX M0/I3C1 SCL M1/G _ _ _ _ _ PIO2 A2 d _ _ | TOP IOC GPIO2A IOMUX S _ _ _ _ EL L[11:8]=4’h3 _ |
| AUDIO DSM R N _ _ _ | O | SDMMC0 D3/FSPI1 D3 M0/DSM A _ _ _ _ UD RN M0/SAI3 SDI M3/JTAG TM _ _ _ _ _ S M0/UART5 CTSN M2/CAN1 TX M _ _ _ _ _ 0/I3C1 SDA M1/GPIO2 A3 d _ _ _ _ | TOP IOC GPIO2A IOMUX S _ _ _ _ EL L[15:12]=4’h3 _ |

## Page 938 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai0 lrck _ | I/O | VI CIF D6/ETH0 RXD2 M1/SAI0 LRCK _ _ _ _ _ _ M0/UART7 RX M0/UART8 CTSN M1/I2C _ _ _ _ 8 SDA M2/GPIO2 B7 d _ _ _ _ | TOP IOC GPIO2B IOMUX _ _ _ _ SEL H[15:12]=4 _ |
| sai0 sdo0 _ | O | VI CIF D15/SDMMC1 D0 M1/ETH0 RXD _ _ _ _ _ 0 M1/SAI0 SDO0 M0/UART8 TX M1/SPI _ _ _ _ _ 4 CSN1 M3/I2C4 SCL M2/GPIO2 A6 d _ _ _ _ _ _ | TOP IOC GPIO2A IOMUX _ _ _ _ SEL H[11:8]=4 _ |
| sai0 sdo1 _ | O | VI CIF D14/SDMMC1 D1 M1/ETH0 TXC _ _ _ _ _ TL M1/SAI0 SDO1 M0/UART8 RX M1/I2 _ _ _ _ _ C4 SDA M2/GPIO2 A7 d _ _ _ _ | TOP IOC GPIO2A IOMUX _ _ _ _ SEL H[15:12]=4 _ |
| sai0 sdo2 _ | O | VI CIF D10/SDMMC1 CLK M1/ETH0 TXC _ _ _ _ _ LK M1/SAI0 SDO2 M0/PDM0 CLK1 M3/ _ _ _ _ _ UART1 RTSN M1/SPI4 CLK M3/PCIE1 C _ _ _ _ _ LKREQN M0/GPIO2 B3 d _ _ _ | TOP IOC GPIO2B IOMUX _ _ _ _ SEL L[15:12]=4 _ |
| sai0 sdo3 _ | O | CAM CLK2 OUT M1/ETH1 MCLK M0/ETH _ _ _ _ _ CLK0 25M OUT M1/SAI0 SDO3 M0/SP _ _ _ _ _ _ DIF TX0 M2/UART9 CTSN M0/SPI3 CSN _ _ _ _ _ 1 M0/PWM2 CH7 M2/GPIO2 D7 d _ _ _ _ _ | TOP IOC GPIO2D IOMUX _ _ _ SEL H[15:12]=4 _ _ |
| sai0 sdi0 _ | I | VI CIF D13/SDMMC1 D2 M1/ETH0 TXD _ _ _ _ _ 1 M1/SAI0 SDI0 M0/PDM0 SDI3 M3/UA _ _ _ _ _ RT1 TX M1/GPIO2 B0 d _ _ _ _ | TOP IOC GPIO2B IOMUX _ _ _ _ SEL L[3:0]=4 _ |
| sai0 sdi1 _ | I | VI CIF D12/SDMMC1 D3 M1/ETH0 TXD _ _ _ _ _ 0 M1/SAI0 SDI1 M0/PDM0 SDI2 M3/UA _ _ _ _ _ RT1 RX M1/GPIO2 B1 d _ _ _ _ | TOP IOC GPIO2B IOMUX _ _ _ _ SEL L[7:4]=4 _ |
| sai0 sdi2 _ | I | VI CIF D11/SDMMC1 CMD M1/ETH0 TX _ _ _ _ _ D3 M1/SAI0 SDI2 M0/PDM0 SDI1 M3/U _ _ _ _ _ ART1 CTSN M1/SPI4 CSN0 M3/PCIE0 C _ _ _ _ _ LKREQN M0/GPIO2 B2 d _ _ _ | TOP IOC GPIO2B IOMUX _ _ _ _ SEL L[11:8]=4 _ |
| sai0 sdi3 _ | I | VI CIF D9/SDMMC1 PWREN M1/ETH0 T _ _ _ _ _ XD2 M1/SAI0 SDI3 M0/PDM0 SDI0 M3/ _ _ _ _ _ UART7 CTSN M0/SPI4 MOSI M3/SATA0 _ _ _ _ ACTLED M0/GPIO2 B4 d _ _ _ _ | TOP IOC GPIO2B IOMUX _ _ _ _ SEL H[3:0]=4 _ |

## Pages 938-939 (stitched) -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai0 mclk _ | I/O | SAI0 MCLK M1/PDM0 CLK0 M0/UART10 _ _ _ _ TX M2/PWM0 CH0 M0/GPIO0 C4 d | PMU1 IOC GPIO0C IOMU _ _ _ X SEL H[3:0]=1 |
| sai0 sclk _ | I/O | _ _ _ _ _ _ SAI0 SCLK M1/I2C3 SCL M1/SPI0 CSN _ _ _ _ _ 0 M0/GPIO0 C6 d _ _ _ | _ _ PMU1 IOC GPIO0C IOMU _ _ _ X SEL H[11:8]=1 _ _ |
| sai0 lrck _ | I/O | SAI0 LRCK M1/I2C3 SDA M1/SPI0 CLK _ _ _ _ _ M0/GPIO0 C7 d _ _ _ | PMU1 IOC GPIO0C IOMU _ _ _ X SEL H[15:12]=1 _ _ |
| sai0 sdo0 _ | O | SAI0 SDO0 M1/DP HPDIN M1/UART10 _ _ _ _ _ RX M2/I3C0 SDA PU M0/GPIO0 C5 d _ _ _ _ _ _ | PMU1 IOC GPIO0C IOMU _ _ _ X SEL H[7:4]=1 _ _ |
| sai0 sdo1/sai0 _ sdi3 _ | I/O | SAI0 SDI3 M1/SAI0 SDO1 M1/PDM0 S _ _ _ _ _ DI3 M0/I2C4 SDA M0/GPU AVS/PWM2 _ _ _ _ _ CH0 M0/UART1 RTSN M0/GPIO0 D3 d _ _ _ _ _ | PMU1 IOC GPIO0D IOMU _ _ _ X SEL L[15:12]=2 _ _ PMU1 IOC GPIO0D IOMU _ _ _ X SEL L[15:12]=1 _ _ |
| sai0 sdo2/sai0 _ sdi2 _ | I/O | SAI0 SDI2 M1/SAI0 SDO2 M1/PDM0 S _ _ _ _ _ DI2 M0/I2C4 SCL M0/CPUBIG AVS/PW _ _ _ _ | PMU1 IOC GPIO0D IOMU _ _ _ X SEL L[11:8]=2 _ _ PMU1 IOC GPIO0D IOMU |
| Module Pin | Direction | Pad Name | IOMUX Setting |
|  |  | M1 CH5 M0/UART1 CTSN M0/GPIO0 D _ _ _ _ _ 2 d _ | X SEL L[11:8]=1 _ _ |
| sai0 sdo3/sai0 _ sdi1 _ | I/O | SAI0 SDI1 M1/SAI0 SDO3 M1/PDM0 S _ _ _ _ _ DI1 M0/SPI0 MISO M0/GPIO0 D1 d _ _ _ _ _ | PMU1 IOC GPIO0D IOMU _ _ _ X SEL L[7:4]=2 _ _ PMU1 IOC GPIO0D IOMU _ _ _ X SEL L[7:4]=1 |
| sai0 sdi0 _ | I | SAI0 SDI0 M1/PDM0 SDI0 M0/SPI0 M _ _ _ _ _ OSI M0/GPIO0 D0 d _ _ _ | _ _ PMU1 IOC GPIO0D IOMU _ _ _ X SEL L[3:0]=1 _ _ |

## Page 939 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai0 mclk _ | I/O | EMMC D4/SAI0 MCLK M2/SAI3 MCLK _ _ _ _ _ M0/SPI0 CSN0 M2/GPIO1 A4 u | TOP IOC GPIO1A IOMUX _ _ _ _ SEL H[3:0]=3 |
| sai0 sclk _ | I/O | _ _ _ _ EMMC D0/FSPI0 D0/SAI0 SCLK M2/UA _ _ _ _ RT7 RTSN M1/I2C2 SCL M1/GPIO1 A0 _ _ _ _ _ u _ | _ TOP IOC GPIO1A IOMUX _ _ _ _ SEL L[3:0]=3 _ |
| sai0 lrck _ | I/O | EMMC D1/FSPI0 D1/SAI0 LRCK M2/UA _ _ _ _ RT7 CTSN M1/I2C2 SDA M1/GPIO1 A1 _ _ _ _ _ u _ | TOP IOC GPIO1A IOMUX _ _ _ _ SEL L[7:4]=3 _ |
| sai0 sdo0 _ | O | EMMC D7/SAI0 SDO0 M2/SAI3 SDI M0 _ _ _ _ _ /SPI0 CLK M2/GPIO1 A7 u _ _ _ _ | TOP IOC GPIO1A IOMUX _ _ _ _ SEL H[15:12]=3 _ |
| sai0 sdo1/sai0 _ sdi3 _ | I/O | EMMC D2/FSPI0 D2/SAI0 SDO1 M2/SA _ _ _ _ I0 SDI3 M2/PDM0 SDI3 M1/UART7 TX _ _ _ _ _ M1/UART6 RTSN M2/GPIO1 A2 u _ _ _ _ _ | TOP IOC GPIO1A IOMUX _ _ _ _ SEL L[11:8]=3 _ TOP IOC GPIO1A IOMUX _ _ _ _ SEL L[11:8]=4 _ |
| sai0 sdo2/sai0 _ sdi2 _ | I/O | EMMC D3/FSPI0 D3/SAI0 SDO2 M2/SA _ _ _ _ I0 SDI2 M2/PDM0 SDI1 M1/UART7 RX _ _ _ _ _ M1/UART6 CTSN M2/GPIO1 A3 u _ _ _ _ _ | TOP IOC GPIO1A IOMUX _ _ _ _ SEL L[15:12]=3 _ TOP IOC GPIO1A IOMUX _ _ _ _ SEL L[15:12]=4 _ |
| sai0 sdo3/sai0 _ sdi1 _ | I/O | EMMC CLK/FSPI0 CLK/SAI0 SDO3 M2/ _ _ _ _ SAI0 SDI1 M2/PDM0 CLK0 M1/PWM2 _ _ _ _ _ CH7 M1/GPIO1 B1 d _ _ _ | TOP IOC GPIO1B IOMUX _ _ _ _ SEL L[7:4]=3 _ TOP IOC GPIO1B IOMUX _ _ _ _ SEL L[7:4]=4 _ |
| sai0 sdi0 _ | I | EMMC STRB/SAI0 SDI0 M2/SAI3 SDO _ _ _ _ _ M0/PDM0 SDI0 M1/SPI0 CSN1 M2/GPI _ _ _ _ O1 B2 d _ _ | TOP IOC GPIO1B IOMUX _ _ _ _ SEL L[11:8]=3 _ |

## Page 939 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai1 mclk _ | I/O | SAI1 MCLK M0/SAI4 MCLK M0/AUPLL _ _ _ _ _ CLK IN M2/PWM2 CH5 M0/GPIO4 A2 d | TOP IOC GPIO4A IOMUX _ _ _ _ SEL L[11:8]=1 |
| sai1 sclk _ | I/O | _ _ _ _ _ _ SAI1 SCLK M0/FLEXBUS1 CSN M4/SPI3 _ _ _ _ CSN0 M2/UART5 RTSN M1/I2C2 SCL _ _ _ _ _ _ M2/PWM2 CH4 M1/GPIO4 A3 d _ _ _ _ | _ TOP IOC GPIO4A IOMUX _ _ _ _ SEL L[15:12]=1 _ |
| sai1 lrck _ | I/O | SAI1 LRCK M0/FLEXBUS1 D12 M1/SPI4 _ _ _ _ CSN1 M2/UART5 CTSN M1/I2C2 SDA _ _ _ _ _ _ M2/PCIE1 CLKREQN M2/GPIO4 A5 d _ _ _ _ | TOP IOC GPIO4A IOMUX _ _ _ _ SEL H[7:4]=1 _ |
| sai1 sdo0 _ | O | SAI1 SDO0 M0/SAI4 SDI M0/SPI3 CLK _ _ _ _ _ M2/PWM2 CH6 M0/GPIO4 A7 d _ _ _ _ _ | TOP IOC GPIO4A IOMUX _ _ _ _ SEL H[15:12]=1 _ |
| sai1 sdo1/sai1 _ sdi3 _ | I/O | SAI1 SDO1 M0/SAI1 SDI3 M0/PDM1 C _ _ _ _ _ LK1 M1/FLEXBUS1 D13 M1/SPI4 CLK _ _ _ _ _ | TOP IOC GPIO4B IOMUX _ _ _ _ SEL L[3:0]=1 _ TOP IOC GPIO4B IOMUX _ _ _ _ SEL L[3:0]=2 |

## Page 940 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
|  |  | M2/UART5 TX M1/UART6 RTSN M0/UA _ _ _ _ RT2 RTSN M1/GPIO4 B0 d _ _ _ _ |  |
| sai1 sdo2/sai1 _ sdi2 _ | I/O | SAI1 SDO2 M0/SAI1 SDI2 M0/PDM1 S _ _ _ _ _ DI2 M1/FLEXBUS1 D14 M1/SPI4 MOSI _ _ _ _ M2/UART5 RX M1/UART6 CTSN M0/U _ _ _ _ _ ART2 CTSN M1/GPIO4 B1 d _ _ _ _ | TOP IOC GPIO4B IOMUX _ _ _ _ SEL L[7:4]=1 _ TOP IOC GPIO4B IOMUX _ _ _ _ SEL L[7:4]=2 _ |
| sai1 sdo3/sai1 _ sdi1 _ | I/O | SAI1 SDO3 M0/SAI1 SDI1 M0/PDM1 S _ _ _ _ _ DI1 M1/FLEXBUS1 D15 M1/SPI4 MISO _ _ _ _ M2/MIPI TE M0/GPIO4 B2 d _ _ _ _ _ | TOP IOC GPIO4B IOMUX _ _ _ _ SEL L[11:8]=1 _ TOP IOC GPIO4B IOMUX _ _ _ _ SEL L[11:8]=2 _ |
| sai1 sdi0 _ | I | SAI1 SDI0 M0/SAI4 SDO M0/PDM1 SD _ _ _ _ _ I0 M1/SPI4 CSN0 M2/SPI3 CSN1 M2/P _ _ _ _ _ WM2 CH7 M0/GPIO4 B3 d _ _ _ _ | TOP IOC GPIO4B IOMUX _ _ _ _ SEL L[15:12]=1 _ |

## Page 940 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai1 mclk _ | I/O | VO LCDC D3/VO EBC SDDO3/SAI1 MC _ _ _ _ _ LK M1/DSMC DATA1/FLEXBUS1 D3/UAR _ _ _ T8 CTSN M0/SPI1 CSN0 M2/PWM2 CH _ _ _ _ _ 3 M3/GPIO3 D0 d | TOP IOC GPIO3D IOMUX _ _ _ SEL L[3:0]=4 _ _ |
| sai1 sclk _ | I/O | _ _ _ VO LCDC D4/VO EBC SDDO4/SAI1 SC _ _ _ _ _ LK M1/DSMC DATA2/FLEXBUS1 D4/UAR _ _ _ T8 RTSN M0/SPI1 CLK M2/GPIO3 C7 _ _ _ _ _ _ d | TOP IOC GPIO3C IOMUX _ _ _ _ SEL H[15:12]=4 _ |
| sai1 lrck _ | I/O | VO LCDC D5/VO EBC SDDO5/SAI1 LR _ _ _ _ _ CK M1/DSMC DATA3/FLEXBUS1 D5/UA _ _ _ RT8 TX M0/SPI1 MOSI M2/GPIO3 C6 _ _ _ _ _ _ d | TOP IOC GPIO3C IOMUX _ _ _ _ SEL H[11:8]=4 _ |
| sai1 sdo0 _ | O | VO LCDC D6/VO EBC SDDO6/SAI1 SD _ _ _ _ _ O0 M1/DSMC DATA4/FLEXBUS1 D6/UA _ _ _ RT8 RX M0/SPI1 MISO M2/PWM2 CH2 _ _ _ _ _ M3/GPIO3 C5 d _ _ _ | TOP IOC GPIO3C IOMUX _ _ _ _ SEL H[7:4]=4 _ |
| sai1 sdo1 _ | O | VO LCDC D7/VO EBC SDDO7/SAI1 SD _ _ _ _ _ O1 M1/DSMC DATA5/FLEXBUS1 D7/UA _ _ _ RT11 TX M0/SPI2 CSN0 M2/I2C5 SCL _ _ _ _ _ _ M3/CAN0 TX M3/GPIO3 C4 d _ _ _ _ | TOP IOC GPIO3C IOMUX _ _ _ _ SEL H[3:0]=4 _ |
| sai1 sdo2 _ | O | VO LCDC D10/VO EBC SDDO10/ETH0 _ _ _ _ _ PTP REFCLK M0/SAI1 SDO2 M1/DSMC _ _ _ _ _ DATA6/FLEXBUS1 D8/UART11 RX M0/S _ _ _ PI2 MISO M2/I2C5 SDA M3/CAN0 RX _ _ _ _ _ _ M3/GPIO3 C1 d _ _ | TOP IOC GPIO3C IOMUX _ _ _ _ SEL L[7:4]=4 _ |
| sai1 sdo3 _ | O | VO LCDC D11/VO EBC SDDO11/ETH0 _ _ _ _ _ PPSCLK M0/SAI1 SDO3 M1/DSMC DAT _ _ _ _ A7/FLEXBUS1 D9/UART2 TX M2/UART3 _ _ _ RTSN M1/I2C4 SCL M3/GPIO3 C0 d _ _ _ _ _ _ | TOP IOC GPIO3C IOMUX _ _ _ _ SEL L[3:0]=4 _ |
| sai1 sdi0 _ | I | VO LCDC D12/VO EBC SDDO12/ETH0 _ _ _ _ _ PPSTRIG M0/SAI1 SDI0 M1/DSMC DQS _ _ _ _ 0/FLEXBUS1 D10/FLEXBUS1 CSN M0/U _ _ _ | TOP IOC GPIO3B IOMUX _ _ _ _ SEL H[15:12]=4 _ |

## Page 941 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
|  |  | ART2 RX M2/UART3 CTSN M1/I2C4 SD _ _ _ _ _ A M3/GPIO3 B7 d _ _ _ |  |
| sai1 sdi1 _ | I | VO LCDC DEN/VO EBC SDLE/SAI1 SDI _ _ _ _ _ 1 M1/DSMC DATA0/FLEXBUS1 D1/UART _ _ _ 5 RX M0/SPI3 CLK M1/I2C3 SCL M2/G _ _ _ _ _ _ PIO3 D4 d _ _ | TOP IOC GPIO3D IOMUX _ _ _ SEL H[3:0]=4 _ _ |
| sai1 sdi2 _ | I | VO LCDC HSYNC/VO EBC GDCLK/SAI1 _ _ _ _ SDI2 M1/DSMC CLKP/FLEXBUS1 D0/U _ _ _ _ ART5 TX M0/SPI3 MISO M1/I2C3 SDA _ _ _ _ _ M2/GPIO3 D5 d _ _ _ | TOP IOC GPIO3D IOMUX _ _ _ SEL H[7:4]=4 _ _ |
| sai1 sdi3 _ | I | VO LCDC VSYNC/VO EBC SDCLK/SAI1 _ _ _ _ _ SDI3 M1/DSMC CLKN/FLEXBUS1 CLK/U _ _ _ ART5 CTSN M0/SPI3 MOSI M1/PWM2 _ _ _ _ _ CH6 M3/GPIO3 D6 d _ _ _ | TOP IOC GPIO3D IOMUX _ _ _ SEL H[11:8]=4 _ _ |

## Page 941 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai2 mclk _ | I/O | ETH1 MCLK M1/SAI2 MCLK M0/PDM0 _ _ _ _ _ SDI3 M2/SPDIF RX1 M2/UART10 RTSN _ _ _ _ M1/I2C5 SCL M1/GPIO1 D4 d | TOP IOC GPIO1D IOMUX _ _ _ SEL H[3:0]=4 _ _ |
| sai2 sclk _ | I/O | _ _ _ _ _ ETH1 RXCTL M1/SAI2 SCLK M0/UART1 _ _ _ _ 0 RX M1/I3C0 SDA PU M1/GPIO1 D1 _ _ _ _ _ _ _ d | TOP IOC GPIO1D IOMUX _ _ _ SEL L[7:4]=4 _ _ |
| sai2 lrck _ | I/O | ETH1 MDC M1/SAI2 LRCK M0/I3C0 SC _ _ _ _ _ L M1/PWM1 CH3 M1/GPIO1 D2 d _ _ _ _ _ | TOP IOC GPIO1D IOMUX _ _ _ SEL L[11:8]=4 _ _ |
| sai2 sdo0 _ | O | ETH1 RXD1 M1/SAI2 SDO M0/UART10 _ _ _ _ _ TX M1/GPIO1 D0 d _ _ _ | TOP IOC GPIO1D IOMUX _ _ _ SEL L[3:0]=4 _ _ |
| sai2 sdi0 _ | I | ETH1 MDIO M1/SAI2 SDI M0/I3C0 SD _ _ _ _ _ A M1/PWM1 CH4 M1/GPIO1 D3 d _ _ _ _ _ | TOP IOC GPIO1D IOMUX _ _ _ SEL L[15:12]=4 _ _ |

## Pages 941-942 (stitched) -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai2 mclk _ | I/O | VI CIF D4/ETH1 RXD3 M0/ETH0 PPSCL _ _ _ _ _ K M1/SAI2 MCLK M1/PDM1 CLK1 M0/U _ _ _ _ _ ART9 TX M0/SPI1 CSN1 M1/PWM1 CH _ _ _ _ _ 1 M2/GPIO2 C1 d | TOP IOC GPIO2C IOMUX _ _ _ _ SEL L[7:4]=4 _ |
| sai2 sclk _ | I/O | _ _ _ VI CIF D3/ETH1 RXCLK M0/ETH0 PPST _ _ _ _ _ RIG M1/SAI2 SCLK M1/PDM1 SDI2 M0 _ _ _ _ _ /UART11 CTSN M1/SPI1 MOSI M1/PWM _ _ _ _ 1 CH2 M2/GPIO2 C2 d _ _ _ _ | TOP IOC GPIO2C IOMUX _ _ _ _ SEL L[11:8]=4 _ |
| sai2 lrck _ | I/O | VI CIF D2/ETH1 TXD2 M0/SAI2 LRCK _ _ _ _ _ _ M1/PDM1 SDI3 M0/UART11 RTSN M1/S _ _ _ _ PI1 MISO M1/PWM0 CH0 M2/GPIO2 C _ _ _ _ _ 3 d _ | TOP IOC GPIO2C IOMUX _ _ _ _ SEL L[15:12]=4 _ |
| sai2 sdo0 _ | O | VI CIF D1/ETH1 TXD3 M0/SAI2 SDO _ _ _ _ _ _ M1/PDM1 SDI0 M0/UART11 TX M1/SPI _ _ _ _ 1 CSN0 M1/PWM1 CH3 M2/GPIO2 C4 _ _ _ _ _ _ d | TOP IOC GPIO2C IOMUX _ _ _ _ SEL H[4:0]=4 _ |
| Module Pin | Direction | Pad Name | IOMUX Setting |
| sai2 sdi0 _ | I | VI CIF D0/ETH1 TXCLK M0/SAI2 SDI _ _ _ _ _ _ M1/PDM1 CLK0 M0/UART11 RX M1/SPI _ _ _ _ 1 CLK M1/PWM1 CH4 M2/GPIO2 C5 d _ _ _ _ _ _ | TOP IOC GPIO2C IOMUX _ _ _ _ SEL H[7:4]=4 _ |

## Page 942 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai2 mclk _ | I/O | VO LCDC D2/VO EBC SDDO2/ETH0 RX _ _ _ _ _ CLK M0/SAI2 MCLK M2/DSMC CSN2/FL _ _ _ _ EXBUS0 D11/FLEXBUS1 CSN M2/SPI4 _ _ _ _ CLK M1/I3C1 SDA PU M2/GPIO3 D1 d | TOP IOC GPIO3D IOMUX _ _ _ SEL L[7:4]=4 _ _ |
| sai2 sclk _ | I/O | _ _ _ _ _ _ VO LCDC D9/VO EBC SDDO9/ETH0 TX _ _ _ _ _ D3 M0/SAI2 SCLK M2/DSMC INT1/FLE _ _ _ _ XBUS0 D9/UART11 RTSN M0/SPI4 MIS _ _ _ _ O M1/I2C9 SCL M3/PWM2 CH0 M3/GPI _ _ _ _ _ O3 C2 d _ _ | TOP IOC GPIO3C IOMUX _ _ _ _ SEL L[11:8]=4 _ |
| sai2 lrck _ | I/O | VO LCDC D8/VO EBC SDDO8/ETH0 TX _ _ _ _ _ D2 M0/SAI2 LRCK M2/DSMC INT3/FLE _ _ _ _ XBUS0 D10/FLEXBUS0 CSN M2/UART11 _ _ _ CTSN M0/SPI4 MOSI M1/I2C9 SDA M _ _ _ _ _ _ 3/PWM2 CH1 M3/GPIO3 C3 d _ _ _ _ | TOP IOC GPIO3C IOMUX _ _ _ _ SEL L[15:12]=4 _ |
| sai2 sdo0 _ | O | VO LCDC D0/VO EBC SDDO0/ETH0 RX _ _ _ _ _ D2 M0/SAI2 SDO M2/DSMC CSN0/FLE _ _ _ _ XBUS1 D2/UART2 CTSN M2/I3C1 SCL _ _ _ _ _ M2/PWM2 CH5 M3/GPIO3 D3 d _ _ _ _ | TOP IOC GPIO3D IOMUX _ _ _ SEL L[15:12]=4 _ _ |
| sai2 sdi0 _ | I | VO LCDC D1/VO EBC SDDO1/ETH0 RX _ _ _ _ _ D3 M0/SAI2 SDI M2/DSMC CSN3/FLEX _ _ _ _ BUS0 D12/FLEXBUS1 D15 M0/FLEXBUS _ _ _ 0 CSN M3/UART2 RTSN M2/SPI4 CSN1 _ _ _ _ _ M1/I3C1 SDA M2/PWM2 CH4 M3/GPI _ _ _ _ _ O3 D2 d _ _ | TOP IOC GPIO3D IOMUX _ _ _ SEL L[11:8]=4 _ _ |

## Page 942 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai3 mclk _ | I/O | EMMC D4/SAI0 MCLK M2/SAI3 MCLK _ _ _ _ _ M0/SPI0 CSN0 M2/GPIO1 A4 u | TOP IOC GPIO1A IOMUX _ _ _ _ SEL H[3:0]=4 |
| sai3 sclk _ | I/O | _ _ _ _ EMMC D5/SAI3 SCLK M0/PDM0 SDI2 _ _ _ _ _ M1/SPI0 MOSI M2/I2C9 SCL M0/GPIO1 _ _ _ _ A5 u _ _ | _ TOP IOC GPIO1A IOMUX _ _ _ _ SEL H[7:4]=4 _ |
| sai3 lrck _ | I/O | EMMC D6/SAI3 LRCK M0/PDM0 CLK1 _ _ _ _ _ M1/SPI0 MISO M2/I2C9 SDA M0/GPIO _ _ _ _ 1 A6 u _ _ | TOP IOC GPIO1A IOMUX _ _ _ _ SEL H[11:8]=4 _ |
| sai3 sdo0 _ | O | EMMC STRB/SAI0 SDI0 M2/SAI3 SDO _ _ _ _ _ M0/PDM0 SDI0 M1/SPI0 CSN1 M2/GPI _ _ _ _ O1 B2 d _ _ | TOP IOC GPIO1B IOMUX _ _ _ _ SEL L[11:8]=4 _ |
| sai3 sdi0 _ | I | EMMC D7/SAI0 SDO0 M2/SAI3 SDI M0 _ _ _ _ _ /SPI0 CLK M2/GPIO1 A7 u _ _ _ _ | TOP IOC GPIO1A IOMUX _ _ _ _ SEL H[15:12]=4 _ |

## Page 943 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
|  |  | MCLK M1/PDM0 CLK0 M2/UART3 RX _ _ _ _ _ _ M2/GPIO1 C1 d | SEL L[3:0]=4 _ |
| sai3 sclk _ | I/O | _ _ ETH1 RXD2 M1/SDMMC1 D0 M0/SAI3 _ _ _ _ _ SCLK M1/I2C9 SDA M1/SPI1 CLK M0/P _ _ _ _ _ CIE1 CLKREQN M1/PWM1 CH0 M1/GPI _ _ _ _ O1 B4 d _ _ | TOP IOC GPIO1B IOMUX _ _ _ _ SEL H[3:0]=4 _ |
| sai3 lrck _ | I/O | ETH1 RXD3 M1/SDMMC1 D1 M0/SAI3 _ _ _ _ _ LRCK M1/I2C9 SCL M1/SPI1 MOSI M0/ _ _ _ _ _ PWM1 CH1 M1/GPIO1 B5 d _ _ _ _ | TOP IOC GPIO1B IOMUX _ _ _ _ SEL H[7:4]=4 _ |
| sai3 sdo0 _ | O | ETH1 RXCLK M1/SDMMC1 D2 M0/SAI3 _ _ _ _ SDO M1/UART3 CTSN M2/SPI1 MISO _ _ _ _ _ _ M0/PCIE0 CLKREQN M1/GPIO1 B6 d _ _ _ _ | TOP IOC GPIO1B IOMUX _ _ _ _ SEL H[11:8]=4 _ |
| sai3 sdi0 _ | I | ETH1 TXD2 M1/SDMMC1 D3 M0/SAI3 _ _ _ _ _ SDI M1/UART3 RTSN M2/SPI1 CSN0 M _ _ _ _ _ 0/GPIO1 B7 d _ _ | TOP IOC GPIO1B IOMUX _ _ _ _ SEL H[15:12]=4 _ |

## Page 943 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai3 mclk _ | I/O | CAM CLK1 OUT M1/ETH CLK1 25M OU _ _ _ _ _ _ T M0/ETH0 MCLK M1/SAI3 MCLK M2/S _ _ _ _ _ PDIF RX0 M2/UART9 RTSN M0/I3C1 S _ _ _ _ _ DA PU M0/PWM2 CH6 M2/GPIO2 D6 d | TOP IOC GPIO2D IOMUX _ _ _ SEL H[11:8]=4 _ _ |
| sai3 sclk _ | I/O | _ _ _ _ _ _ VI CIF HREF/ETH0 MDIO M1/SAI3 SCL _ _ _ _ _ K M2/UART3 TX M0/SPI3 CLK M0/I2C7 _ _ _ _ _ SCL M1/GPIO3 A0 d _ _ _ _ | TOP IOC GPIO3A IOMUX _ _ _ _ SEL L[3:0]=4 _ |
| sai3 lrck _ | I/O | VI CIF VSYNC/ETH1 PPSTRIG M0/ETH0 _ _ _ _ MDC M1/SAI3 LRCK M2/UART3 RX M _ _ _ _ _ _ 0/SPI3 MOSI M0/I2C7 SDA M1/GPIO3 _ _ _ _ _ A1 d _ | TOP IOC GPIO3A IOMUX _ _ _ _ SEL L[7:4]=4 _ |
| sai3 sdo0 _ | O | VI CIF CLKO/ETH1 PPSCLK M0/ETH0 R _ _ _ _ _ XCTL M1/SAI3 SDO M2/SPDIF RX1 M1 _ _ _ _ _ /UART3 CTSN M0/SPI3 MISO M0/CAN1 _ _ _ _ TX M3/MIPI TE M1/GPIO3 A2 d _ _ _ _ _ _ | TOP IOC GPIO3A IOMUX _ _ _ _ SEL L[11:8]=4 _ |
| sai3 sdi0 _ | I | VI CIF CLKI/ETH1 PTP REFCLK M0/ETH _ _ _ _ _ 0 RXD1 M1/SAI3 SDI M2/SPDIF TX1 _ _ _ _ _ _ M1/UART3 RTSN M0/SPI3 CSN0 M0/CA _ _ _ _ N1 RX M3/GPIO3 A3 d _ _ _ _ | TOP IOC GPIO3A IOMUX _ _ _ _ SEL L[15:12]=4 _ |

## Page 944 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai4 mclk _ | I/O | SAI1 MCLK M0/SAI4 MCLK M0/AUPLL _ _ _ _ _ CLK IN M2/PWM2 CH5 M0/GPIO4 A2 d | TOP IOC GPIO4A IOMUX _ _ _ _ SEL L[11:8]=2 |
| sai4 sclk _ | I/O | _ _ _ _ _ _ SAI4 SCLK M0/PDM1 SDI3 M1/FLEXBU _ _ _ _ S0 D13 M1/SPI3 MOSI M2/UART6 TX _ _ _ _ _ _ M0/I2C4 SCL M1/CAN0 TX M2/GPIO4 _ _ _ _ _ A4 d _ | _ TOP IOC GPIO4A IOMUX _ _ _ _ SEL H[3:0]=2 _ |
| sai4 lrck _ | I/O | SAI4 LRCK M0/PDM1 CLK0 M1/FLEXBU _ _ _ _ S0 D14 M1/SPI3 MISO M2/UART6 RX _ _ _ _ _ _ M0/I2C4 SDA M1/CAN0 RX M2/GPIO4 _ _ _ _ _ A6 d _ | TOP IOC GPIO4A IOMUX _ _ _ _ SEL H[11:8]=2 _ |
| sai4 sdo0 _ | O | SAI1 SDI0 M0/SAI4 SDO M0/PDM1 SD _ _ _ _ _ I0 M1/SPI4 CSN0 M2/SPI3 CSN1 M2/P _ _ _ _ _ WM2 CH7 M0/GPIO4 B3 d _ _ _ _ | TOP IOC GPIO4B IOMUX _ _ _ _ SEL L[15:12]=2 _ |
| sai4 sdi0 _ | I | SAI1 SDO0 M0/SAI4 SDI M0/SPI3 CLK _ _ _ _ _ M2/PWM2 CH6 M0/GPIO4 A7 d _ _ _ _ _ | TOP IOC GPIO4A IOMUX _ _ _ _ SEL H[15:12]=2 _ |

## Page 945 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai4 mclk _ | I/O | DSM AUD LP M1/SAI4 MCLK M2/HDMI _ _ _ _ _ TX CEC M0/I2C7 SCL M3/SPI4 CSN1 _ _ _ _ _ _ _ M0/UART11 TX M2/PWM1 CH5 M1/GPI _ _ _ _ O4 C0 d | VCCIO6 IOC GPIO4C IOM _ _ _ UX SEL L[3:0]=2 _ _ |
| sai4 sclk _ | I/O | _ _ SAI4 SCLK M2/VP2 SYNC OUT/I2C6 S _ _ _ _ _ DA M3/SPI4 CLK M0/CAN1 RX M1/PW _ _ _ _ _ M2 CH3 M1/GPIO4 C7 d _ _ _ _ | VCCIO6 IOC GPIO4C IOM _ _ _ UX SEL H[15:12]=2 _ _ |
| sai4 lrck _ | I/O | ISP PRELIGHT TRIG M1/SAI4 LRCK M2 _ _ _ _ _ /DP HPDIN M0/I2C3 SCL M3/SPI4 CSN _ _ _ _ _ 0 M0/UART6 TX M3/PWM2 CH6 M1/GP _ _ _ _ _ IO4 C4 d _ _ | VCCIO6 IOC GPIO4C IOM _ _ _ UX SEL H[3:0]=2 _ _ |
| sai4 sdo0 _ | O | ISP FLASH TRIGOUT M1/SAI4 SDO M2 _ _ _ _ _ /VP0 SYNC OUT/SATA1 ACTLED M1/I2 _ _ _ _ C3 SDA M3/SPI4 MOSI M0/UART6 RX _ _ _ _ _ _ M3/PWM2 CH5 M1/GPIO4 C5 d _ _ _ _ | VCCIO6 IOC GPIO4C IOM _ _ _ UX SEL H[7:4]=2 _ _ |
| sai4 sdi0 _ | I | SAI4 SDI M2/VP1 SYNC OUT/PCIE0 CL _ _ _ _ _ KREQN M3/SATA0 ACTLED M1/I2C6 SC _ _ _ _ L M3/SPI4 MISO M0/CAN1 TX M1/PWM _ _ _ _ _ 2 CH2 M1/GPIO4 C6 d _ _ _ _ | VCCIO6 IOC GPIO4C IOM _ _ _ UX SEL H[11:8]=2 _ _ |

## Pages 945-946 (stitched) -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sai4 mclk _ | I/O | CAM CLK0 OUT M1/ETH1 RXD1 M0/SA _ _ _ _ _ I4 MCLK M3/UART6 TX M1/I3C1 SCL _ _ _ _ _ _ M0/PWM2 CH2 M2/GPIO2 D2 d | TOP IOC GPIO2D IOMUX _ _ _ SEL L[11:8]=4 _ _ |
| sai4 sclk _ | I/O | _ _ _ _ ETH1 TXD0 M0/SAI4 SCLK M3/UART4 _ _ _ _ _ CTSN M0/I2C5 SCL M2/PWM1 CH5 M2 _ _ _ _ _ /GPIO2 C6 d _ _ | TOP IOC GPIO2C IOMUX _ _ _ _ SEL H[11:8]=4 _ |
| sai4 lrck _ | I/O | ETH1 TXD1 M0/SAI4 LRCK M3/UART4 _ _ _ _ _ RTSN M0/I2C5 SDA M2/PWM0 CH1 M2 _ _ _ _ _ /GPIO2 C7 d _ _ | TOP IOC GPIO2C IOMUX _ _ _ _ SEL H[15:12]=4 _ |
| sai4 sdo0 _ | O | ETH1 RXD0 M0/SAI4 SDO M3/UART4 _ _ _ _ _ RX M0/I2C6 SDA M2/PWM2 CH1 M2/G _ _ _ _ _ PIO2 D1 d _ _ | TOP IOC GPIO2D IOMUX _ _ _ SEL L[7:4]=4 _ _ |
| Module Pin | Direction | Pad Name | IOMUX Setting |
| sai4 sdi0 _ | I | ETH1 TXCTL M0/SAI4 SDI M3/UART4 T _ _ _ _ _ X M0/I2C6 SCL M2/PWM2 CH0 M2/GPI _ _ _ _ _ O2 D0 d _ _ | TOP IOC GPIO2D IOMUX _ _ _ SEL L[3:0]=4 _ _ |

## Page 959 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| O pdm clk(0) _ _ | O | SAI0 MCLK M1/PDM0 CL _ _ _ K0 M0/UART10 TX M2/P _ _ _ WM0 CH0 M0/GPIO0 C4 _ _ _ d | PMU1 IOC GPIO0C IOMUX _ _ _ _ SEL H[3:0]=4’h3 _ |
| O pdm clk(1) _ _ | O | _ PDM0 CLK1 M0/HDMI T _ _ _ X CEC M1/SPI0 CSN1 M _ _ _ _ 0/PWM0 CH1 M0/GPIO0 _ _ C3 d | PMU1 IOC GPIO0C IOMUX _ _ _ _ SEL L[15:12]=4’h3 _ |
| I pdm data0 _ _ | I | _ _ SAI0 SDI0 M1/PDM0 SD _ _ _ I0 M0/SPI0 MOSI M0/G _ _ _ PIO0 D0 d | PMU1 IOC GPIO0D IOMUX _ _ _ _ SEL L[3:0]=4’h3 _ |
| I pdm data1 _ _ | I | _ _ SAI0 SDI1 M1/SAI0 SD _ _ _ O3 M1/PDM0 SDI1 M0/S _ _ _ PI0 MISO M0/GPIO0 D1 _ _ _ d | PMU1 IOC GPIO0D IOMUX _ _ _ _ SEL L[7:4]=4’h3 _ |
| I pdm data2 _ _ | I | _ SAI0 SDI2 M1/SAI0 SD _ _ _ O2 M1/PDM0 SDI2 M0/I _ _ _ 2C4 SCL M0/CPUBIG AV _ _ _ S/PWM1 CH5 M0/UART1 _ _ CTSN M0/GPIO0 D2 d | PMU1 IOC GPIO0D IOMUX _ _ _ _ SEL L[11:8]=4’h3 _ |
| I pdm data3 _ _ | I | _ _ _ _ SAI0 SDI3 M1/SAI0 SD _ _ _ O1 M1/PDM0 SDI3 M0/I _ _ _ 2C4 SDA M0/GPU AVS/P _ _ _ WM2 CH0 M0/UART1 RT _ _ _ SN M0/GPIO0 D3 d | PMU1 IOC GPIO0D IOMUX _ _ _ _ SEL L[15:12]=4’h3 _ |

## Page 960 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| O pdm clk(0) _ _ | O | ETH1 TXCLK M1/SDMMC _ _ 1 CLK M0/SAI3 MCLK M _ _ _ _ 1/PDM0 CLK0 M2/UART3 _ _ RX M2/GPIO1 C1 d | TOP IOC GPIO1C IOMUX S _ _ _ _ EL L[7:4]=4’h5 _ |
| O pdm clk(1) _ _ | O | _ _ _ _ ETH CLK1 25M OUT M1 _ _ _ _ /FSPI1 CLK M1/PDM0 CL _ _ _ K1 M2/SPDIF TX1 M2/U _ _ _ ART10 CTSN M1/I2C5 S _ _ _ DA M1/SPI2 CLK M1/SA _ _ _ TA MPSWIT/CLK1 32K O _ _ _ UT/GPIO1 D5 d | TOP IOC GPIO1D IOMUX S _ _ _ _ EL H[7:4]=4’h5 _ |
| I pdm data0 _ _ | I | _ _ ETH1 TXCTL M1/FSPI1 _ _ _ D2 M1/PDM0 SDI0 M2/U _ _ _ ART2 TX M0/I2C8 SCL _ _ _ _ M1/SATA CPPOD/GPIO1 _ _ C6 d | TOP IOC GPIO1C IOMUX S _ _ _ _ EL H[11:8]=4’h5 _ |
| I pdm data1 _ _ | I | _ ETH1 RXD0 M1/FSPI1 D _ _ _ 3 M1/PDM0 SDI1 M2/UA _ _ _ RT2 RX M0/I2C8 SDA M _ _ _ _ 1/SATA CPDET/GPIO1 C _ _ 7 d | TOP IOC GPIO1C IOMUX S _ _ _ _ EL H[15:12]=4’h5 _ |
| I pdm data2 _ _ | I | _ ETH1 TXD3 M1/SDMMC1 _ _ CMD M0/PDM0 SDI2 M _ _ _ _ 2/UART3 TX M2/SPI1 C _ _ _ SN1 M0/PWM0 CH0 M1/ _ _ _ GPIO1 C0 d | TOP IOC GPIO1C IOMUX S _ _ _ _ EL L[3:0]=4’h5 _ |
| I pdm data3 _ _ | I | _ _ ETH1 MCLK M1/SAI2 MC _ _ _ LK M0/PDM0 SDI3 M2/S _ _ _ PDIF RX1 M2/UART10 R _ _ _ TSN M1/I2C5 SCL M1/G _ _ _ PIO1 D4 d | TOP IOC GPIO1D IOMUX S _ _ _ _ EL H[3:0]=4’h5 _ |

## Page 961 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| O pdm clk(0) _ _ | O | VI CIF D0/ETH1 TXCLK _ _ _ _ M0/SAI2 SDI M1/PDM1 _ _ _ CLK0 M0/UART11 RX M _ _ _ 1/SPI1 CLK M1/PWM1 C _ _ _ H4 M2/GPIO2 C5 d | TOP IOC GPIO2C IOMUX S _ _ _ _ EL H[7:4]=4’h5 _ |
| O pdm clk(1) _ _ | O | _ _ _ VI CIF D4/ETH1 RXD3 _ _ _ _ M0/ETH0 PPSCLK M1/SA _ _ I2 MCLK M1/PDM1 CLK1 _ _ _ M0/UART9 TX M0/SPI1 _ _ _ CSN1 M1/PWM1 CH1 M _ _ _ _ 2/GPIO2 C1 d | TOP IOC GPIO2C IOMUX S _ _ _ _ EL L[7:4]=4’h5 _ |
| I pdm data0 _ _ | I | _ _ VI CIF D1/ETH1 TXD3 _ _ _ _ M0/SAI2 SDO M1/PDM1 _ _ SDI0 M0/UART11 TX M _ _ _ _ 1/SPI1 CSN0 M1/PWM1 _ _ _ CH3 M2/GPIO2 C4 d | TOP IOC GPIO2C IOMUX S _ _ _ _ EL H[3:0]=4’h5 _ |
| I pdm data1 _ _ | I | _ _ _ VI CIF D5/ETH1 RXD2 _ _ _ _ M0/ETH0 PTP REFCLK M _ _ _ 1/PDM1 SDI1 M0/UART9 _ _ RX M0/PWM1 CH0 M2/ _ _ _ _ GPIO2 C0 d | TOP IOC GPIO2C IOMUX S _ _ _ _ EL L[3:0]=4’h5 _ |
| I pdm data2 _ _ | I | _ _ VI CIF D3/ETH1 RXCLK _ _ _ _ M0/ETH0 PPSTRIG M1/S _ _ AI2 SCLK M1/PDM1 SDI _ _ _ 2 M0/UART11 CTSN M1/ _ _ _ SPI1 MOSI M1/PWM1 C _ _ _ H2 M2/GPIO2 C2 d | TOP IOC GPIO2C IOMUX S _ _ _ _ EL L[11:8]=4’h5 _ |
| I pdm data3 _ _ | I | _ _ _ VI CIF D2/ETH1 TXD2 _ _ _ _ M0/SAI2 LRCK M1/PDM1 _ _ SDI3 M0/UART11 RTSN _ _ _ M1/SPI1 MISO M1/PW _ _ _ M0 CH0 M2/GPIO2 C3 d | TOP IOC GPIO2C IOMUX S _ _ _ _ EL L[15:12]=4’h5 _ |

## Pages 962-963 (stitched) -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| O pdm clk(0) _ _ | O | VO LCDC D18/VO EBC _ _ _ _ SDCE2/ETH0 RXD1 M0/P _ _ DM1 CLK0 M2/DSMC DA _ _ _ TA12/FLEXBUS0 D4/UAR _ T10 TX M0/SPI4 CSN0 _ _ _ _ M1/PWM1 CH3 M3/GPIO _ _ 3 B1 d | TOP IOC GPIO3B IOMUX S _ _ _ _ EL L[7:4]=4’h4 _ |
| O pdm clk(1) _ _ | O | _ _ VO LCDC D20/VO EBC _ _ _ _ VCOM/ETH0 RXCTL M0/P _ _ DM1 CLK1 M2/DSMC DA _ _ _ TA13/FLEXBUS0 D5/UAR _ T1 TX M2/UART10 RTSN _ _ _ M0/GPIO3 A7 d | TOP IOC GPIO3A IOMUX S _ _ _ _ EL H[15:12]=4’h4 _ |
| I pdm data0 _ _ | I | _ _ _ VO LCDC D16/VO EBC _ _ _ _ SDCE0/ETH0 TXCTL M0/ _ _ PDM1 SDI0 M2/DSMC D _ _ _ ATA10/FLEXBUS0 D2/UA _ RT9 TX M1/I2C8 SCL M _ _ _ _ 3/GPIO3 B3 d | TOP IOC GPIO3B IOMUX S _ _ _ _ EL L[15:12]=4’h4 _ |
| I pdm data1 _ _ | I | _ _ VO LCDC D17/VO EBC _ _ _ _ SDCE1/ETH0 RXD0 M0/P _ _ DM1 SDI1 M2/DSMC DA _ _ _ TA11/FLEXBUS0 D3/UAR _ T9 RX M1/I2C8 SDA M3 _ _ _ _ /GPIO3 B2 d | TOP IOC GPIO3B IOMUX S _ _ _ _ EL L[11:8]=4’h4 _ |
| I pdm data2 _ _ | I | _ _ VO LCDC D21/VO EBC _ _ _ _ GDOE/ETH0 MDC M0/PD _ _ M1 SDI2 M2/DSMC DAT _ _ _ A14/FLEXBUS0 D6/UART _ 1 RX M2/UART10 CTSN _ _ _ _ M0/PWM1 CH2 M3/GPIO _ _ 3 A6 d | TOP IOC GPIO3A IOMUX S _ _ _ _ EL H[11:8]=4’h4 _ |
| I pdm data3 | I | _ _ VO LCDC D22/VO EBC | TOP IOC GPIO3A IOMUX S |
|  |  | GDSP/ETH0 MDIO M0/P _ _ DM1 SDI3 M2/DSMC DA _ _ _ TA15/FLEXBUS0 D7/UAR _ T1 RTSN M2/SPI2 CSN1 _ _ _ M2/PWM1 CH1 M3/GPI _ _ _ O3 A5 d | EL H[7:4]=4’h4 _ |

## Page 1038 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sfc0 sclk _ | O | EMMC CLK/FSPI0 C _ _ LK/SAI0 SDO3 M2/ _ _ SAI0 SDI1 M2/PDM _ _ 0 CLK0 M1/PWM2 _ _ _ CH7 M1/GPIO1 B1 _ _ _ d | TOP IOC GPIO1B IOMUX SEL L[ _ _ _ _ _ 7:4]=4’h2 |
| sfc0 cs0n _ | O | EMMC RSTN/FSPI0 _ CSN0/UART6 RX _ _ _ M2/I2C7 SDA M0/ _ _ MIPI TE M3/PWM2 _ _ CH1 M0/GPIO1 B _ _ _ 3 u | TOP IOC GPIO1B IOMUX SEL L[ _ _ _ _ _ 15:12]=4’h2 |
| sfc0 cs1n _ | O | _ EMMC CMD/FSPI0 _ _ RSTN/FSPI0 CSN1/ _ UART6 TX M2/I2C7 _ _ SCL M0/GPIO1 B0 _ _ _ u | TOP IOC GPIO1B IOMUX SEL L[ _ _ _ _ _ 3:0]=4’h2 |
| sfc0 rstn _ | O | _ EMMC CMD/FSPI0 _ _ RSTN/FSPI0 CSN1/ _ UART6 TX M2/I2C7 _ _ SCL M0/GPIO1 B0 _ _ _ u | NOTE:Use GPIO1 B0 to reset _ device in maskrom |
| sfc0 sio0 _ | I/O | _ EMMC D0/FSPI0 D0 _ _ /SAI0 SCLK M2/UA _ _ RT7 RTSN M1/I2C2 _ _ SCL M1/GPIO1 A0 _ _ _ u | TOP IOC GPIO1A IOMUX SEL L[ _ _ _ _ _ 3:0]=4’h2 |
| sfc0 sio1 | I/O | _ EMMC D1/FSPI0 D1 | TOP IOC GPIO1A IOMUX SEL L[ |

## Page 1039 -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
|  |  | /SAI0 LRCK M2/UA _ _ RT7 CTSN M1/I2C2 _ _ SDA M1/GPIO1 A _ _ _ 1 u | 7:4]=4’h2 |
| sfc0 sio2 _ | I/O | _ EMMC D2/FSPI0 D2 _ _ /SAI0 SDO1 M2/SA _ _ I0 SDI3 M2/PDM0 _ _ _ SDI3 M1/UART7 TX _ _ M1/UART6 RTSN _ _ _ M2/GPIO1 A2 u | TOP IOC GPIO1A IOMUX SEL L[ _ _ _ _ _ 11:8]=4’h2 |
| sfc0 sio3 _ | I/O | _ _ EMMC D3/FSPI0 D3 _ _ /SAI0 SDO2 M2/SA _ _ I0 SDI2 M2/PDM0 _ _ _ SDI1 M1/UART7 RX _ _ M1/UART6 CTSN _ _ _ M2/GPIO1 A3 u | TOP IOC GPIO1A IOMUX SEL L[ _ _ _ _ _ 15:12]=4’h2 |
| sfc1 sclk m0 _ _ | O | _ _ SDMMC0 CLK/FSPI1 _ CLK M0/SAI3 SCL _ _ _ K M3/TEST CLK O _ _ _ UT/UART5 TX M2/I _ _ 2C5 SCL M0/SPI0 _ _ _ CLK M1/I3C1 SDA _ _ _ PU M1/GPIO2 A5 d | TOP IOC GPIO2A IOMUX SEL H[ _ _ _ _ _ 7:4]=4’h2 |
| sfc1 cs0n m0 _ _ | O | _ _ _ SDMMC0 CMD/FSPI _ 1 CSN0 M0/SAI3 S _ _ _ DO M3/UART5 RX _ _ _ M2/I2C5 SDA M0/S _ _ PI0 CSN0 M1/PWM _ _ 2 CH4 M0/GPIO2 A _ _ _ 4 d | TOP IOC GPIO2A IOMUX SEL H[ _ _ _ _ _ 3:0]=4’h2 |
| sfc1 sio0 m0 _ _ | I/O | _ SDMMC0 D0/FSPI1 _ D0 M0/DSM AUD _ _ _ _ LP M0/UART0 RX _ _ _ M1/UART7 RX M2/I _ _ 2C8 SCL M0/SPI0 _ _ _ MOSI M1/CAN0 RX _ _ M0/PWM2 CH2 M0 _ _ _ /GPIO2 A0 d | TOP IOC GPIO2A IOMUX SEL L[ _ _ _ _ _ 3:0]=4’h2 |
| sfc1 sio1 m0 _ _ | I/O | _ _ SDMMC0 D1/FSPI1 _ D1 M0/DSM AUD _ _ _ _ LN M0/SAI3 MCLK _ _ _ M3/UART0 TX M1/ _ _ UART7 TX M2/I2C8 _ _ SDA M0/SPI0 MIS _ _ _ O M1/CAN0 TX M0 _ _ _ /PWM2 CH3 M0/GP _ _ IO2 A1 d | TOP IOC GPIO2A IOMUX SEL L[ _ _ _ _ _ 7:4]=4’h2 |
| sfc1 sio2 m0 _ _ | I/O | _ _ SDMMC0 D2/FSPI1 _ D2 M0/DSM AUD _ _ _ RP M0/SAI3 LRC _ _ _ K M3/JTAG TCK M _ _ _ 0/UART5 RTSN M2 _ _ /SPI0 CSN1 M1/C _ _ AN1 RX M0/I3C1 _ _ _ SCL M1/GPIO2 A2 _ _ d _ | TOP IOC GPIO2A IOMUX SEL L[ _ _ _ _ _ 11:8]=4’h2 |

## Pages 1040-1041 (stitched) -- pin table

| Module Pin | Direction | Pad Name | IOMUX Setting |
|---|---|---|---|
| sfc1 sio3 m0 _ _ | I/O | SDMMC0 D3/FSPI1 _ D3 M0/DSM AUD _ _ _ _ RN M0/SAI3 SDI M _ _ _ 3/JTAG TMS M0/UA _ _ RT5 CTSN M2/CAN _ _ 1 TX M0/I3C1 SDA _ _ _ M1/GPIO2 A3 d | TOP IOC GPIO2A IOMUX SEL L[ _ _ _ _ _ 15:12]=4’h2 |
| sfc1 sclk m1 _ _ | O | _ _ _ ETH CLK1 25M OU _ _ _ T M1/FSPI1 CLK M _ _ _ 1/PDM0 CLK1 M2/S _ _ PDIF TX1 M2/UART _ _ 10 CTSN M1/I2C5 _ _ _ SDA M1/SPI2 CLK _ _ _ M1/SATA MPSWIT/ _ CLK1 32K OUT/GPI _ _ O1 D5 d | TOP IOC GPIO1D IOMUX SEL H _ _ _ _ _ [7:4]=4’h3 |
| sfc1 cs0n m1 _ _ | O | _ _ ETH1 PPSTRIG M1/ _ _ SDMMC1 DETN M0/ _ _ FSPI1 CSN0 M1/UA _ _ RT4 CTSN M1/I2C6 _ _ SDA M1/SPI2 CSN _ _ _ 0 M1/GPIO1 C3 u | TOP IOC GPIO1C IOMUX SEL L[ _ _ _ _ _ 15:12]=4’h3 |
| sfc1 cs1n m1 _ _ | O | _ _ _ ETH1 PPSCLK M1/S _ _ DMMC1 PWREN M0 _ _ /FSPI1 RSTN M1/F _ _ SPI1 CSN1 M1/UAR _ _ T4 RTSN M1/I2C6 _ _ _ SCL M1/SPI2 CSN1 _ _ M1/PWM1 CH2 M1 _ _ _ /GPIO1 C2 u _ _ | TOP IOC GPIO1C IOMUX SEL L[ _ _ _ _ _ 11:8]=4’h3 |
| sfc1 rstn m1 _ _ | O | ETH1 PPSCLK M1/S _ _ DMMC1 PWREN M0 _ _ /FSPI1 RSTN M1/F _ _ SPI1 CSN1 M1/UAR _ _ T4 RTSN M1/I2C6 _ _ _ SCL M1/SPI2 CSN1 _ _ M1/PWM1 CH2 M1 _ _ _ /GPIO1 C2 u | NOTE:Use GPIO1 C2 to reset _ device in maskrom |
| sfc1 sio0 m1 _ _ | I/O | _ _ ETH1 TXD0 M1/FSP _ _ I1 D0 M1/UART4 T _ _ _ X M1/UART2 RTSN _ _ M0/SPI2 MOSI M1 _ _ _ /PCIE0 BUTTONRST _ N/GPIO1 C4 d | TOP IOC GPIO1C IOMUX SEL H[ _ _ _ _ _ 3:0]=4’h3 |
| sfc1 sio1 m1 _ _ | I/O | _ _ ETH1 TXD1 M1/FSP _ _ I1 D1 M1/UART4 R _ _ _ X M1/UART2 CTSN _ _ M0/SPI2 MISO M1 _ _ _ /PCIE1 BUTTONRST _ N/GPIO1 C5 d | TOP IOC GPIO1C IOMUX SEL H[ _ _ _ _ _ 7:4]=4’h3 |
| sfc1 sio2 m1 _ _ | I/O | _ _ ETH1 TXCTL M1/FS _ _ PI1 D2 M1/PDM0 S _ _ _ DI0 M2/UART2 TX _ _ _ M0/I2C8 SCL M1/S _ _ ATA CPPOD/GPIO1 _ _ C6 d | TOP IOC GPIO1C IOMUX SEL H[ _ _ _ _ _ 11:8]=4’h3 |
| Module Pin | Direction | Pad Name | IOMUX Setting |
| sfc1 sio3 m1 _ _ | I/O | ETH1 RXD0 M1/FSP _ _ I1 D3 M1/PDM0 S _ _ _ DI1 M2/UART2 RX _ _ _ M0/I2C8 SDA M1/S _ _ ATA CPDET/GPIO1 _ _ C7 d | TOP IOC GPIO1C IOMUX SEL H[ _ _ _ _ _ 15:12]=4’h3 |

## Pages 1057-1058 (stitched) -- pin table

| Module Pin | i | D Pad Name r | IOMUX Setting |
|---|---|---|---|
| IOMUX0 |  |  |  |
| spi sclk _ |  | I SAI0 LRCK M1/I2C3 SDA M1/S / _ _ _ _ PI0 CLK M0/GPIO0 C7 d O _ _ _ _ | PMU1 IOC GPIO0C IO _ _ _ MUX SEL H[15:12]=4' _ _ hb |
| spi mosi _ |  | I SAI0 SDI0 M1/PDM0 SDI0 M0/ / _ _ _ _ SPI0 MOSI M0/GPIO0 D0 d O _ _ _ _ | PMU1 IOC GPIO0D IO _ _ _ MUX SEL L[3:0]=4'hb _ _ |
| spi miso _ |  | I SAI0 SDI1 M1/SAI0 SDO3 M1/ _ _ _ _ / PDM0 SDI1 M0/SPI0 MISO M0/ _ _ _ _ O GPIO0 D1 d | PMU1 IOC GPIO0D IO _ _ _ MUX SEL L[7:4]=4'hb _ _ |
| spi csn0 _ |  | _ _ I SAI0 SCLK M1/I2C3 SCL M1/SP / _ _ _ _ I0 CSN0 M0/GPIO0 C6 d O _ _ _ _ | PMU1 IOC GPIO0C IO _ _ _ MUX SEL H[11:8]=4'h _ _ b |
| spi csn1 _ |  | PDM0 CLK1 M0/HDMI TX CEC _ _ _ _ _ O M1/SPI0 CSN1 M0/PWM0 CH1 _ _ _ _ M0/GPIO0 C3 d | PMU1 IOC GPIO0C IO _ _ _ MUX SEL L[15:12]=4'h _ _ b |
| _ _ IOMUX1 |  |  |  |
| spi sclk _ |  | SDMMC0 CLK/FSPI1 CLK M0/SA _ _ _ I I3 SCLK M3/TEST CLK OUT/UA _ _ _ _ / RT5 TX M2/I2C5 SCL M0/SPI0 _ _ _ _ _ O CLK M1/I3C1 SDA PU M1/GPIO _ _ _ _ 2 A5 d | TOP IOC GPIO2A IOM _ _ _ UX SEL H[7:4]=4'hc _ _ |
| spi mosi _ |  | _ _ SDMMC0 D0/FSPI1 D0 M0/DSM _ _ _ I AUD LP M0/UART0 RX M1/UAR _ _ _ _ _ / T7 RX M2/I2C8 SCL M0/SPI0 M _ _ _ _ _ O OSI M1/CAN0 RX M0/PWM2 CH _ _ _ _ 2 M0/GPIO2 A0 d | TOP IOC GPIO2A IOM _ _ _ UX SEL L[3:0]=4'hc _ _ |
| spi miso _ |  | _ _ _ SDMMC0 D1/FSPI1 D1 M0/DSM _ _ _ AUD LN M0/SAI3 MCLK M3/UA I _ _ _ _ _ RT0 TX M1/UART7 TX M2/I2C8 / _ _ _ _ SDA M0/SPI0 MISO M1/CAN0 O _ _ _ _ _ TX M0/PWM2 CH3 M0/GPIO2 A _ _ _ _ 1 d | TOP IOC GPIO2A IOM _ _ _ UX SEL L[7:4]=4'hc _ _ |
| spi csn0 _ |  | _ SDMMC0 CMD/FSPI1 CSN0 M0/ I _ _ _ SAI3 SDO M3/UART5 RX M2/I2 / _ _ _ _ C5 SDA M0/SPI0 CSN0 M1/PW O _ _ _ _ M2 CH4 M0/GPIO2 A4 d | TOP IOC GPIO2A IOM _ _ _ UX SEL H[3:0]=4'hc _ _ |
| spi csn1 _ |  | _ _ _ _ SDMMC0 D2/FSPI1 D2 M0/DSM _ _ _ AUD RP M0/SAI3 LRCK M3/JT _ _ _ _ _ O AG TCK M0/UART5 RTSN M2/SP _ _ _ _ I0 CSN1 M1/CAN1 RX M0/I3C1 _ _ _ _ SCL M1/GPIO2 A2 d | TOP IOC GPIO2A IOM _ _ _ UX SEL L[11:8]=4'hc _ _ |
| _ _ _ _ IOMUX2 |  |  |  |
| spi sclk _ |  | I EMMC D7/SAI0 SDO0 M2/SAI3 _ _ _ _ / SDI M0/SPI0 CLK M2/GPIO1 A7 | TOP IOC GPIO1A IOM _ _ _ UX SEL H[15:12]=4'h9 |
|  |  | O u |  |
| spi mosi _ |  | _ I EMMC D5/SAI3 SCLK M0/PDM0 _ _ _ / SDI2 M1/SPI0 MOSI M2/I2C9 _ _ _ _ _ O SCL M0/GPIO1 A5 u | TOP IOC GPIO1A IOM _ _ _ UX SEL H[7:4]=4'h9 _ _ |
| spi miso _ |  | _ _ _ I EMMC D6/SAI3 LRCK M0/PDM0 _ _ _ / CLK1 M1/SPI0 MISO M2/I2C9 _ _ _ _ _ O SDA M0/GPIO1 A6 u | TOP IOC GPIO1A IOM _ _ _ UX SEL H[11:8]=4'h9 _ _ |
| spi csn0 _ |  | _ _ _ I EMMC D4/SAI0 MCLK M2/SAI3 _ _ _ _ / MCLK M0/SPI0 CSN0 M2/GPIO1 _ _ _ O A4 u | TOP IOC GPIO1A IOM _ _ _ UX SEL H[3:0]=4'h9 _ _ |
| spi csn1 _ |  | _ _ EMMC STRB/SAI0 SDI0 M2/SAI _ _ _ O 3 SDO M0/PDM0 SDI0 M1/SPI0 _ _ _ _ CSN1 M2/GPIO1 B2 d | TOP IOC GPIO1B IOM _ _ _ UX SEL L[11:8]=4'h9 _ _ |

## Pages 1058-1059 (stitched) -- pin table

| Module Pin | i | D Pad Name r | IOMUX Setting |
|---|---|---|---|
| IOMUX0 |  |  |  |
| spi sclk _ |  | ETH1 RXD2 M1/SDMMC1 D0 M I _ _ _ _ 0/SAI3 SCLK M1/I2C9 SDA M1/ / _ _ _ _ SPI1 CLK M0/PCIE1 CLKREQN O _ _ _ _ M1/PWM1 CH0 M1/GPIO1 B4 d | TOP IOC GPIO1B IOM _ _ _ UX SEL H[3:0]=4'hb _ _ |
| spi mosi _ |  | _ _ _ _ ETH1 RXD3 M1/SDMMC1 D1 M I _ _ _ _ 0/SAI3 LRCK M1/I2C9 SCL M1/ / _ _ _ _ SPI1 MOSI M0/PWM1 CH1 M1/ O _ _ _ _ GPIO1 B5 d | TOP IOC GPIO1B IOM _ _ _ UX SEL H[7:4]=4'hb _ _ |
| spi miso _ |  | _ _ ETH1 RXCLK M1/SDMMC1 D2 M I _ _ _ _ 0/SAI3 SDO M1/UART3 CTSN M / _ _ _ _ 2/SPI1 MISO M0/PCIE0 CLKREQ O _ _ _ N M1/GPIO1 B6 d | TOP IOC GPIO1B IOM _ _ _ UX SEL H[11:8]=4'hb _ _ |
| spi csn0 _ |  | _ _ _ I ETH1 TXD2 M1/SDMMC1 D3 M0 _ _ _ _ / /SAI3 SDI M1/UART3 RTSN M2/ _ _ _ _ O SPI1 CSN0 M0/GPIO1 B7 d | TOP IOC GPIO1B IOM _ _ _ UX SEL H[15:12]=4'hb _ _ |
| spi csn1 _ |  | _ _ _ _ ETH1 TXD3 M1/SDMMC1 CMD _ _ _ _ M0/PDM0 SDI2 M2/UART3 TX O _ _ _ _ M2/SPI1 CSN1 M0/PWM0 CH0 _ _ _ _ M1/GPIO1 C0 d | TOP IOC GPIO1C IOM _ _ _ UX SEL L[3:0]=4'hb _ _ |
| _ _ IOMUX1 |  |  |  |
| spi sclk _ |  | VI CIF D0/ETH1 TXCLK M0/SAI I _ _ _ _ 2 SDI M1/PDM1 CLK0 M0/UART / _ _ _ _ 11 RX M1/SPI1 CLK M1/PWM1 O _ _ _ _ _ CH4 M2/GPIO2 C5 d | TOP IOC GPIO2C IOM _ _ _ UX SEL H[7:4]=4'ha _ _ |
| spi mosi _ |  | _ _ _ VI CIF D3/ETH1 RXCLK M0/ETH _ _ _ _ I 0 PPSTRIG M1/SAI2 SCLK M1/P _ _ _ _ / DM1 SDI2 M0/UART11 CTSN M _ _ _ _ O 1/SPI1 MOSI M1/PWM1 CH2 M _ _ _ _ 2/GPIO2 C2 d | TOP IOC GPIO2C IOM _ _ _ UX SEL L[11:8]=4'ha _ _ |
| spi miso _ |  | _ _ VI CIF D2/ETH1 TXD2 M0/SAI2 I _ _ _ _ LRCK M1/PDM1 SDI3 M0/UART / _ _ _ _ 11 RTSN M1/SPI1 MISO M1/PW O _ _ _ _ M0 CH0 M2/GPIO2 C3 d | TOP IOC GPIO2C IOM _ _ _ UX SEL L[15:12]=4'ha _ _ |
| spi csn0 _ |  | _ _ _ _ VI CIF D1/ETH1 TXD3 M0/SAI2 I _ _ _ _ SDO M1/PDM1 SDI0 M0/UART / _ _ _ _ 11 TX M1/SPI1 CSN0 M1/PWM1 O _ _ _ _ CH3 M2/GPIO2 C4 d | TOP IOC GPIO2C IOM _ _ _ UX SEL H[3:0]=4'ha _ _ |
| spi csn1 |  | _ _ _ _ O VI CIF D4/ETH1 RXD3 M0/ETH0 | TOP IOC GPIO2C IOM |
|  |  | PPSCLK M1/SAI2 MCLK M1/PD _ _ _ _ M1 CLK1 M0/UART9 TX M0/SPI _ _ _ _ 1 CSN1 M1/PWM1 CH1 M2/GPI _ _ _ _ O2 C1 d | UX SEL L[7:4]=4'ha _ _ |
| _ _ IOMUX2 |  |  |  |
| spi sclk _ |  | VO LCDC D4/VO EBC SDDO4/S I _ _ _ _ AI1 SCLK M1/DSMC DATA2/FLE / _ _ _ XBUS1 D4/UART8 RTSN M0/SPI O _ _ _ 1 CLK M2/GPIO3 C7 d | TOP IOC GPIO3C IOM _ _ _ UX SEL H[15:12]=4'ha _ _ |
| spi mosi _ |  | _ _ _ _ VO LCDC D5/VO EBC SDDO5/S I _ _ _ _ AI1 LRCK M1/DSMC DATA3/FLE / _ _ _ XBUS1 D5/UART8 TX M0/SPI1 O _ _ _ _ MOSI M2/GPIO3 C6 d | TOP IOC GPIO3C IOM _ _ _ UX SEL H[11:8]=4'ha _ _ |
| spi miso _ |  | _ _ _ VO LCDC D6/VO EBC SDDO6/S _ _ _ _ I AI1 SDO0 M1/DSMC DATA4/FLE _ _ _ / XBUS1 D6/UART8 RX M0/SPI1 _ _ _ _ O MISO M2/PWM2 CH2 M3/GPIO3 _ _ _ C5 d | TOP IOC GPIO3C IOM _ _ _ UX SEL H[7:4]=4'ha _ _ |
| spi csn0 _ |  | _ _ VO LCDC D3/VO EBC SDDO3/S _ _ _ _ I AI1 MCLK M1/DSMC DATA1/FLE _ _ _ / XBUS1 D3/UART8 CTSN M0/SPI _ _ _ O 1 CSN0 M2/PWM2 CH3 M3/GPI _ _ _ _ O3 D0 d | TOP IOC GPIO3D IOM _ _ _ UX SEL L[3:0]=4'ha _ _ |
| spi csn1 _ |  | _ _ SPDIF RX0 M1/CAM CLK1 OUT _ _ _ _ _ M0/SAI4 LRCK M1/DSMC INT0/ _ _ _ FLEXBUS0 D13 M0/FLEXBUS1 D O _ _ _ 14 M0/FLEXBUS1 CSN M3/UART _ _ _ 3 TX M1/SPI1 CSN1 M2/I2C7 S _ _ _ _ _ CL M2/MIPI TE M2/GPIO4 A0 d | TOP IOC GPIO4A IOM _ _ _ UX SEL L[3:0]=4'ha _ _ |

## Pages 1059-1060 (stitched) -- pin table

| Module Pin | i | D Pad Name r | IOMUX Setting |
|---|---|---|---|
| IOMUX0 |  |  |  |
| spi sclk _ |  | I SPI2 CLK M0/I2C1 SCL M0/GPI / _ _ _ _ O0 B2 z O _ _ | PMU0 IOC GPIO0B IO _ _ _ MUX SEL L[11:8]=4'h9 _ _ |
| spi mosi _ |  | I SPI2 MOSI M0/I2C1 SDA M0/G / _ _ _ _ PIO0 B3 z O _ _ | PMU0 IOC GPIO0B IO _ _ _ MUX SEL L[15:12]=4'h _ _ 9 |
| spi miso _ |  | I SPI2 MISO M0/I2C0 SDA M0/G / _ _ _ _ PIO0 B1 z O _ _ | PMU0 IOC GPIO0B IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| spi csn0 _ |  | I AUPLL CLK IN M1/SPI2 CSN0 / _ _ _ _ _ M0/I2C0 SCL M0/GPIO0 B0 z O _ _ _ _ | PMU0 IOC GPIO0B IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| spi csn1 _ |  | SDMMC0 DETN/SPI2 CSN1 M0/ O _ _ _ GPIO0 A7 u _ _ | PMU0 IOC GPIO0A IO _ _ _ MUX SEL H[15:12]=4' _ _ h9 |
| IOMUX1 |  |  |  |
| spi sclk _ |  | ETH CLK1 25M OUT M1/FSPI1 _ _ _ _ _ CLK M1/PDM0 CLK1 M2/SPDIF I _ _ _ _ TX1 M2/UART10 CTSN M1/I2C5 / _ _ _ SDA M1/SPI2 CLK M1/SATA M O _ _ _ _ _ PSWIT/CLK1 32K OUT/GPIO1 D _ _ _ 5 d | TOP IOC GPIO1D IOM _ _ _ UX SEL H[7:4]=4'hb _ _ |
| spi mosi _ |  | ETH1 TXD0 M1/FSPI1 D0 M1/U I _ _ _ _ ART4 TX M1/UART2 RTSN M0/S / _ _ _ _ PI2 MOSI M1/PCIE0 BUTTONRS O _ _ _ TN/GPIO1 C4 d | TOP IOC GPIO1C IOM _ _ _ UX SEL H[3:0]=4'hb _ _ |
| spi miso _ |  | _ _ ETH1 TXD1 M1/FSPI1 D1 M1/U I _ _ _ _ ART4 RX M1/UART2 CTSN M0/S / _ _ _ _ PI2 MISO M1/PCIE1 BUTTONRS O _ _ _ TN/GPIO1 C5 d | TOP IOC GPIO1C IOM _ _ _ UX SEL H[7:4]=4'hb _ _ |
| spi csn0 _ |  | _ _ ETH1 PPSTRIG M1/SDMMC1 DE I _ _ _ TN M0/FSPI1 CSN0 M1/UART4 / _ _ _ _ CTSN M1/I2C6 SDA M1/SPI2 C O _ _ _ _ SN0 M1/GPIO1 C3 u | TOP IOC GPIO1C IOM _ _ _ UX SEL L[15:12]=4'hb _ _ |
| spi csn1 _ |  | _ _ _ ETH1 PPSCLK M1/SDMMC1 PWR _ _ _ EN M0/FSPI1 RSTN M1/FSPI1 C _ _ _ _ O SN1 M1/UART4 RTSN M1/I2C6 _ _ _ _ SCL M1/SPI2 CSN1 M1/PWM1 _ _ _ _ CH2 M1/GPIO1 C2 u | TOP IOC GPIO1C IOM _ _ _ UX SEL L[11:8]=4'hb _ _ |
| _ _ _ IOMUX2 |  |  |  |
| spi sclk _ |  | VO LCDC D23/VO EBC SDSHR/ _ _ _ _ ETH CLK0 25M OUT M0/SAI4 S I _ _ _ _ _ DI M1/DSMC RDYN/FLEXBUS1 / _ _ _ D11/FLEXBUS0 CSN M0/UART1 O _ _ _ CTSN M2/SPI2 CLK M2/PWM1 C _ _ _ _ H0 M3/GPIO3 A4 d | TOP IOC GPIO3A IOM _ _ _ UX SEL H[3:0]=4'ha _ _ |
| spi mosi _ |  | _ _ _ VO LCDC D19/VO EBC SDCE3/E _ _ _ _ I TH0 MCLK M0/SAI4 MCLK M1/D _ _ _ _ / SMC CSN1/FLEXBUS0 D8/UART1 _ _ O 0 RX M0/SPI2 MOSI M2/PWM0 _ _ _ _ _ CH0 M3/GPIO3 B0 d | TOP IOC GPIO3B IOM _ _ _ UX SEL L[3:0]=4'ha _ _ |
| spi miso _ |  | _ _ _ VO LCDC D10/VO EBC SDDO10 _ _ _ _ /ETH0 PTP REFCLK M0/SAI1 SD I _ _ _ _ O2 M1/DSMC DATA6/FLEXBUS1 / _ _ _ D8/UART11 RX M0/SPI2 MISO O _ _ _ _ M2/I2C5 SDA M3/CAN0 RX M3/ _ _ _ _ GPIO3 C1 d | TOP IOC GPIO3C IOM _ _ _ UX SEL L[7:4]=4'ha _ _ |
| spi csn0 _ |  | _ _ VO LCDC D7/VO EBC SDDO7/S _ _ _ _ I AI1 SDO1 M1/DSMC DATA5/FLE _ _ _ / XBUS1 D7/UART11 TX M0/SPI2 _ _ _ O CSN0 M2/I2C5 SCL M3/CAN0 _ _ _ _ _ TX M3/GPIO3 C4 d | TOP IOC GPIO3C IOM _ _ _ UX SEL H[3:0]=4'ha _ _ |
| spi csn1 _ |  | _ _ _ VO LCDC D22/VO EBC GDSP/E _ _ _ _ TH0 MDIO M0/PDM1 SDI3 M2/ _ _ _ _ O DSMC DATA15/FLEXBUS0 D7/UA _ _ RT1 RTSN M2/SPI2 CSN1 M2/P _ _ _ _ WM1 CH1 M3/GPIO3 A5 d | TOP IOC GPIO3A IOM _ _ _ UX SEL H[7:4]=4'ha _ _ |

## Pages 1062-1064 (stitched) -- pin table

| Module Pin | i | D Pad Name r | IOMUX Setting |
|---|---|---|---|
| IOMUX0 |  |  |  |
| spi sclk _ |  | SAI4 SCLK M2/VP2 SYNC OUT/I I _ _ _ _ 2C6 SDA M3/SPI4 CLK M0/CAN / _ _ _ _ 1 RX M1/PWM2 CH3 M1/GPIO4 O _ _ _ _ C7 d | VCCIO6 IOC GPIO4C I _ _ _ OMUX SEL H[15:12]=4 _ _ 'hc |
| spi mosi _ |  | _ _ ISP FLASH TRIGOUT M1/SAI4 S _ _ _ _ I DO M2/VP0 SYNC OUT/SATA1 A _ _ _ _ / CTLED M1/I2C3 SDA M3/SPI4 _ _ _ _ O MOSI M0/UART6 RX M3/PWM2 _ _ _ _ CH5 M1/GPIO4 C5 d | VCCIO6 IOC GPIO4C I _ _ _ OMUX SEL H[7:4]=4'h _ _ c |
| spi miso _ |  | _ _ _ SAI4 SDI M2/VP1 SYNC OUT/P _ _ _ _ I CIE0 CLKREQN M3/SATA0 ACTL _ _ _ / ED M1/I2C6 SCL M3/SPI4 MISO _ _ _ _ O M0/CAN1 TX M1/PWM2 CH2 M _ _ _ _ _ 1/GPIO4 C6 d | VCCIO6 IOC GPIO4C I _ _ _ OMUX SEL H[11:8]=4' _ _ hc |
| spi csn0 _ |  | _ _ ISP PRELIGHT TRIG M1/SAI4 L _ _ _ _ I RCK M2/DP HPDIN M0/I2C3 SC _ _ _ _ / L M3/SPI4 CSN0 M0/UART6 TX _ _ _ _ O M3/PWM2 CH6 M1/GPIO4 C4 _ _ _ _ _ d | VCCIO6 IOC GPIO4C I _ _ _ OMUX SEL H[3:0]=4'h _ _ c |
| spi csn1 _ |  | DSM AUD LP M1/SAI4 MCLK M _ _ _ _ _ 2/HDMI TX CEC M0/I2C7 SCL O _ _ _ _ _ M3/SPI4 CSN1 M0/UART11 TX _ _ _ _ M2/PWM1 CH5 M1/GPIO4 C0 d | VCCIO6 IOC GPIO4C I _ _ _ OMUX SEL L[3:0]=4'hc _ _ |
| _ _ _ _ IOMUX1 |  |  |  |
| spi sclk _ |  | VO LCDC D2/VO EBC SDDO2/E _ _ _ _ I TH0 RXCLK M0/SAI2 MCLK M2/ _ _ _ _ / DSMC CSN2/FLEXBUS0 D11/FLE _ _ O XBUS1 CSN M2/SPI4 CLK M1/I _ _ _ _ 3C1 SDA PU M2/GPIO3 D1 d | TOP IOC GPIO3D IOM _ _ _ UX SEL L[7:4]=4'ha _ _ |
| spi mosi _ |  | _ _ _ _ _ VO LCDC D8/VO EBC SDDO8/E _ _ _ _ TH0 TXD2 M0/SAI2 LRCK M2/D I _ _ _ _ SMC INT3/FLEXBUS0 D10/FLEXB / _ _ US0 CSN M2/UART11 CTSN M0 O _ _ _ _ /SPI4 MOSI M1/I2C9 SDA M3/P _ _ _ _ WM2 CH1 M3/GPIO3 C3 d | TOP IOC GPIO3C IOM _ _ _ UX SEL L[15:12]=4'ha _ _ |
| spi miso _ |  | _ _ _ _ VO LCDC D9/VO EBC SDDO9/E _ _ _ _ TH0 TXD3 M0/SAI2 SCLK M2/D I _ _ _ _ SMC INT1/FLEXBUS0 D9/UART1 / _ _ 1 RTSN M0/SPI4 MISO M1/I2C9 O _ _ _ _ SCL M3/PWM2 CH0 M3/GPIO3 _ _ _ _ C2 d | TOP IOC GPIO3C IOM _ _ _ UX SEL L[11:8]=4'ha _ _ |
| spi csn0 _ |  | _ _ I VO LCDC D18/VO EBC SDCE2/E _ _ _ _ / TH0 RXD1 M0/PDM1 CLK0 M2/ _ _ _ _ O DSMC DATA12/FLEXBUS0 D4/UA | TOP IOC GPIO IOMUX _ _ _ SEL []=4'h _ _ |
|  |  | RT10 TX M0/SPI4 CSN0 M1/PW _ _ _ _ M1 CH3 M3/GPIO3 B1 d |  |
| spi csn1 _ |  | _ _ _ _ VO LCDC D1/VO EBC SDDO1/E _ _ _ _ TH0 RXD3 M0/SAI2 SDI M2/DS _ _ _ _ MC CSN3/FLEXBUS0 D12/FLEXB _ _ O US1 D15 M0/FLEXBUS0 CSN M _ _ _ _ 3/UART2 RTSN M2/SPI4 CSN1 _ _ _ _ M1/I3C1 SDA M2/PWM2 CH4 M _ _ _ _ 3/GPIO3 D2 d | TOP IOC GPIO3D IOM _ _ _ UX SEL H[11:8]=4'ha _ _ |
| _ _ IOMUX2 |  |  |  |
| spi sclk _ |  | SAI1 SDO1 M0/SAI1 SDI3 M0/ _ _ _ _ I PDM1 CLK1 M1/FLEXBUS1 D13 _ _ _ _ / M1/SPI4 CLK M2/UART5 TX M1 _ _ _ _ O /UART6 RTSN M0/UART2 RTSN _ _ _ _ M1/GPIO4 B0 d | TOP IOC GPIO4B IOM _ _ _ UX SEL L[3:0]=4'h9 _ _ |
| spi mosi _ |  | _ _ SAI1 SDO2 M0/SAI1 SDI2 M0/ _ _ _ _ I PDM1 SDI2 M1/FLEXBUS1 D14 _ _ _ _ / M1/SPI4 MOSI M2/UART5 RX M _ _ _ _ O 1/UART6 CTSN M0/UART2 CTSN _ _ _ M1/GPIO4 B1 d | TOP IOC GPIO4B IOM _ _ _ UX SEL L[7:4]=4'h9 _ _ |
| spi miso _ |  | _ _ _ SAI1 SDO3 M0/SAI1 SDI1 M0/ _ _ _ _ I PDM1 SDI1 M1/FLEXBUS1 D15 _ _ _ _ / M1/SPI4 MISO M2/MIPI TE M0/ _ _ _ _ O GPIO4 B2 d/PCIE1 PERSTN M2/ _ _ _ _ GPIO4 B2 d | TOP IOC GPIO4B IOM _ _ _ UX SEL L[11:8]=4'h9 _ _ |
| spi csn0 _ |  | _ _ SAI1 SDI0 M0/SAI4 SDO M0/P I _ _ _ _ DM1 SDI0 M1/SPI4 CSN0 M2/S / _ _ _ _ PI3 CSN1 M2/PWM2 CH7 M0/G O _ _ _ _ PIO4 B3 d | TOP IOC GPIO4B IOM _ _ _ UX SEL L[15:12]=4'h9 _ _ |
| spi csn1 _ |  | _ _ SAI1 LRCK M0/FLEXBUS1 D12 _ _ _ _ M1/SPI4 CSN1 M2/UART5 CTSN O _ _ _ M1/I2C2 SDA M2/PCIE1 CLKRE _ _ _ _ QN M2/GPIO4 A5 d | TOP IOC GPIO4A IOM _ _ _ UX SEL H[7:4]=4'h9 _ _ |
| _ _ _ IOMUX3 |  |  |  |
| spi sclk _ |  | VI CIF D10/SDMMC1 CLK M1/E _ _ _ _ I TH0 TXCLK M1/SAI0 SDO2 M0/ _ _ _ _ / PDM0 CLK1 M3/UART1 RTSN M _ _ _ _ O 1/SPI4 CLK M3/PCIE1 CLKREQN _ _ _ M0/GPIO2 B3 d | TOP IOC GPIO2B IOM _ _ _ UX SEL L[15:12]=4'ha _ _ |
| spi mosi _ |  | _ _ _ VI CIF D9/SDMMC1 PWREN M1 _ _ _ _ I /ETH0 TXD2 M1/SAI0 SDI3 M0/ _ _ _ _ / PDM0 SDI0 M3/UART7 CTSN M _ _ _ _ O 0/SPI4 MOSI M3/SATA0 ACTLED _ _ _ M0/GPIO2 B4 d | TOP IOC GPIO2B IOM _ _ _ UX SEL H[3:0]=4'ha _ _ |
| spi miso _ |  | _ _ _ VI CIF D8/SDMMC1 DETN M1/E _ _ _ _ I TH0 RXCLK M1/SAI0 MCLK M0/ _ _ _ _ / PDM0 CLK0 M3/UART7 RTSN M _ _ _ _ O 0/SPI4 MISO M3/SATA1 ACTLED _ _ _ M0/GPIO2 B5 d | TOP IOC GPIO2B IOM _ _ _ UX SEL H[7:4]=4'ha _ _ |
| spi csn0 _ |  | _ _ _ VI CIF D11/SDMMC1 CMD M1/E _ _ _ _ I TH0 TXD3 M1/SAI0 SDI2 M0/P _ _ _ _ / DM0 SDI1 M3/UART1 CTSN M1 _ _ _ _ O /SPI4 CSN0 M3/PCIE0 CLKREQN _ _ _ M0/GPIO2 B2 d | TOP IOC GPIO2B IOM _ _ _ UX SEL L[11:8]=4'ha _ _ |
| spi csn1 _ |  | _ _ _ VI CIF D15/SDMMC1 D0 M1/ET _ _ _ _ O H0 RXD0 M1/SAI0 SDO0 M0/U _ _ _ _ ART8 TX M1/SPI4 CSN1 M3/I2C | TOP IOC GPIO2A IOM _ _ _ UX SEL H[11:8]=4'ha _ _ |
|  |  | 4 SCL M2/GPIO2 A6 d |  |

## Pages 1149-1150 (stitched) -- pin table

| Module Pin | i | D Pad Name r | IOMUX Setting |
|---|---|---|---|
| IOMUX0 |  |  |  |
| uart rx _ |  | I2C2 SDA M0/UART1 RX M0/CPUL _ _ _ _ I IT AVS/PWM1 CH3 M0/GPIO0 C0 _ _ _ _ _ d | PMU1 IOC GPIO0C I _ _ _ OMUX SEL L[3:0]=4' _ _ ha |
| uart tx _ |  | I2C2 SCL M0/UART1 TX M0/NPU O _ _ _ _ _ AVS/PWM1 CH4 M0/GPIO0 B7 d _ _ _ _ | PMU1 IOC GPIO0B I _ _ _ OMUX SEL H[15:12] _ _ =4'ha |
| uart cts _ n |  | SAI0 SDI2 M1/SAI0 SDO2 M1/PD I _ _ _ _ M0 SDI2 M0/I2C4 SCL M0/PCIE0 _ _ _ _ _ WAKEN M0/CPUBIG AVS/PWM1 CH _ _ _ O 5 M0/UART1 CTSN M0/GPIO0 D2 _ _ _ _ _ d | PMU1 IOC GPIO0D I _ _ _ OMUX SEL L[11:8]=4 _ _ 'hd |
| _ uart re _ |  |  |  |
| uart rts _ n |  | SAI0 SDI3 M1/SAI0 SDO1 M1/PD O _ _ _ _ M0 SDI3 M0/I2C4 SDA M0/PCIE1 _ _ _ _ _ WAKEN M0/GPU AVS/PWM2 CH0 O _ _ _ _ M0/UART1 RTSN M0/GPIO0 D3 d | PMU1 IOC GPIO0D I _ _ _ OMUX SEL L[15:12]= _ _ 4'hd |
| _ uart de _ |  |  |  |
| _ _ _ _ IOMUX1 |  |  |  |
| uart rx _ |  | VI CIF D12/SDMMC1 D3 M1/ETH0 _ _ _ _ TXD0 M1/SAI0 SDI1 M0/PDM0 S I _ _ _ _ _ DI2 M3/UART1 RX M1/GPIO2 B1 _ _ _ _ _ d | TOP IOC GPIO2B IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart tx _ |  | VI CIF D13/SDMMC1 D2 M1/ETH0 _ _ _ _ TXD1 M1/SAI0 SDI0 M0/PDM0 S O _ _ _ _ _ DI3 M3/UART1 TX M1/GPIO2 B0 _ _ _ _ _ d | TOP IOC GPIO2B IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart cts _ n |  | VI CIF D11/SDMMC1 CMD M1/ETH I _ _ _ _ 0 TXD3 M1/SAI0 SDI2 M0/PDM0 _ _ _ _ _ SDI1 M3/UART1 CTSN M1/SPI4 C _ _ _ _ O SN0 M3/PCIE0 CLKREQN M0/GPIO _ _ _ 2 B2 d | TOP IOC GPIO2B IO _ _ _ MUX SEL L[11:8]=4'h _ _ 9 |
| _ uart re _ |  |  |  |
| uart rts _ n |  | _ _ VI CIF D10/SDMMC1 CLK M1/ETH O _ _ _ _ 0 TXCLK M1/SAI0 SDO2 M0/PDM0 _ _ _ _ CLK1 M3/UART1 RTSN M1/SPI4 _ _ _ _ _ O CLK M3/PCIE1 CLKREQN M0/GPIO _ _ _ 2 B3 d | TOP IOC GPIO2B IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| _ uart de _ |  |  |  |
| _ _ IOMUX2 |  |  |  |
| uart rx _ |  | VO LCDC D21/VO EBC GDOE/ETH _ _ _ _ 0 MDC M0/PDM1 SDI2 M2/DSMC _ _ _ _ _ I DATA14/FLEXBUS0 D6/UART1 RX _ _ _ M2/UART10 CTSN M0/PWM1 CH2 _ _ _ _ M3/GPIO3 A6 d | TOP IOC GPIO3A IO _ _ _ MUX SEL H[11:8]=4' _ _ h9 |
| uart tx _ |  | _ _ VO LCDC D20/VO EBC VCOM/ETH _ _ _ _ 0 RXCTL M0/PDM1 CLK1 M2/DSM _ _ _ _ O C DATA13/FLEXBUS0 D5/UART1 T _ _ _ X M2/UART10 RTSN M0/GPIO3 A7 _ _ _ _ d | TOP IOC GPIO3A IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| uart cts _ n _ |  | _ VO LCDC D23/VO EBC SDSHR/ET I _ _ _ _ H CLK0 25M OUT M0/SAI4 SDI M _ _ _ _ _ _ 1/DSMC RDYN/FLEXBUS1 D11/FLE _ _ XBUS0 CSN M0/UART1 CTSN M2/ O _ _ _ _ SPI2 CLK M2/PWM1 CH0 M3/GPIO | TOP IOC GPIO3A IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| uart re _ |  |  |  |
|  |  | 3 A4 d _ _ |  |
| uart rts _ n _ |  | VO LCDC D22/VO EBC GDSP/ETH O _ _ _ _ 0 MDIO M0/PDM1 SDI3 M2/DSMC _ _ _ _ DATA15/FLEXBUS0 D7/UART1 RT _ _ _ SN M2/SPI2 CSN1 M2/PWM1 CH1 O _ _ _ _ M3/GPIO3 A5 d | TOP IOC GPIO3A IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| uart de _ |  |  |  |

## Pages 1150-1158 (stitched) -- pin table

| Module Pin | i | D Pad Name r | IOMUX Setting |
|---|---|---|---|
| IOMUX0 |  |  |  |
| uart rx _ |  | ETH1 RXD0 M1/FSPI1 D3 M1/PDM _ _ _ _ I 0 SDI1 M2/UART2 RX M0/I2C8 S _ _ _ _ _ DA M1/SATA CPDET/GPIO1 C7 d | TOP IOC GPIO1C IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| uart tx _ |  | _ _ _ _ ETH1 TXCTL M1/FSPI1 D2 M1/PD _ _ _ _ O M0 SDI0 M2/UART2 TX M0/I2C8 _ _ _ _ _ SCL M1/SATA CPPOD/GPIO1 C6 d | TOP IOC GPIO1C IO _ _ _ MUX SEL H[11:8]=4' _ _ h9 |
| uart cts _ n _ |  | _ _ _ _ ETH1 TXD1 M1/FSPI1 D1 M1/UAR I _ _ _ _ T4 RX M1/UART2 CTSN M0/SPI2 _ _ _ _ _ MISO M1/PCIE1 BUTTONRSTN/GPI O _ _ O1 C5 d _ _ | TOP IOC GPIO1C IO _ _ _ MUX SEL H[7:4]=4'h _ _ a |
| uart re _ |  |  |  |
| uart rts _ n _ |  | ETH1 TXD0 M1/FSPI1 D0 M1/UAR O _ _ _ _ T4 TX M1/UART2 RTSN M0/SPI2 _ _ _ _ _ MOSI M1/PCIE0 BUTTONRSTN/GPI O _ _ O1 C4 d _ _ | TOP IOC GPIO1C IO _ _ _ MUX SEL H[3:0]=4'h _ _ a |
| uart de _ |  |  |  |
| IOMUX1 |  |  |  |
| uart rx _ |  | SPDIF RX0 M0/FLEXBUS0 CSN M4 _ _ _ _ I /UART2 RX M1/I2C3 SDA M0/CAN _ _ _ _ 1 RX M2/GPIO4 B4 d | TOP IOC GPIO4B IO _ _ _ MUX SEL H[3:0]=4'h _ _ a |
| uart tx _ |  | _ _ _ _ SPDIF TX0 M0/FLEXBUS0 D15 M1 _ _ _ _ /UART2 TX M1/I2C3 SCL M0/PCIE O _ _ _ _ 0 CLKREQN M2/CAN1 TX M2/GPIO _ _ _ _ 4 B5 d | TOP IOC GPIO4B IO _ _ _ MUX SEL H[7:4]=4'h _ _ a |
| uart cts _ n |  | _ _ SAI1 SDO2 M0/SAI1 SDI2 M0/PD I _ _ _ _ M1 SDI2 M1/FLEXBUS1 D14 M1/S _ _ _ _ PI4 MOSI M2/UART5 RX M1/UART _ _ _ _ O 6 CTSN M0/UART2 CTSN M1/GPIO _ _ _ _ 4 B1 d | TOP IOC GPIO4B IO _ _ _ MUX SEL L[7:4]=4'hc _ _ |
| _ uart re _ |  |  |  |
| uart rts _ n |  | _ _ SAI1 SDO1 M0/SAI1 SDI3 M0/PD O _ _ _ _ M1 CLK1 M1/FLEXBUS1 D13 M1/S _ _ _ _ PI4 CLK M2/UART5 TX M1/UART6 _ _ _ _ O RTSN M0/UART2 RTSN M1/GPIO4 _ _ _ _ B0 d | TOP IOC GPIO4B IO _ _ _ MUX SEL L[3:0]=4'hc _ _ |
| _ uart de _ |  |  |  |
| _ _ IOMUX2 |  |  |  |
| uart rx _ |  | VO LCDC D12/VO EBC SDDO12/E _ _ _ _ TH0 PPSTRIG M0/SAI1 SDI0 M1/D _ _ _ _ SMC DQS0/FLEXBUS1 D10/FLEXBU I _ _ S1 CSN M0/UART2 RX M2/UART3 _ _ _ _ _ CTSN M1/I2C4 SDA M3/GPIO3 B7 _ _ _ _ d | TOP IOC GPIO3B IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| uart tx _ |  | _ VO LCDC D11/VO EBC SDDO11/E O _ _ _ _ TH0 PPSCLK M0/SAI1 SDO3 M1/D | TOP IOC GPIO3C IO _ _ _ MUX SEL L[3:0]=4'h9 |
|  |  | SMC DATA7/FLEXBUS1 D9/UART2 _ _ _ TX M2/UART3 RTSN M1/I2C4 SCL _ _ _ _ M3/GPIO3 C0 d |  |
| uart cts _ n |  | _ _ _ VO LCDC D0/VO EBC SDDO0/ETH I _ _ _ _ 0 RXD2 M0/SAI2 SDO M2/DSMC _ _ _ _ _ CSN0/FLEXBUS1 D2/UART2 CTSN _ _ _ O M2/I3C1 SCL M2/PWM2 CH5 M3/ _ _ _ _ GPIO3 D3 d | TOP IOC GPIO3D IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| _ uart re _ |  |  |  |
| uart rts _ n _ |  | _ _ VO LCDC D1/VO EBC SDDO1/ETH _ _ _ _ O 0 RXD3 M0/SAI2 SDI M2/DSMC C _ _ _ _ _ SN3/FLEXBUS0 D12/FLEXBUS1 D1 _ _ 5 M0/FLEXBUS0 CSN M3/UART2 R _ _ _ _ O TSN M2/SPI4 CSN1 M1/I3C1 SDA _ _ _ _ M2/PWM2 CH4 M3/GPIO3 D2 d | TOP IOC GPIO3D IO _ _ _ MUX SEL L[11:8]=4'h _ _ 9 |
| uart de _ |  |  |  |
| _ _ _ _ _ Table 33-4 UART3 Interface Description |  |  |  |
| Module Pin | i | D Pad Name r | IOMUX Setting |
| IOMUX0 |  |  |  |
| uart rx _ |  | VI CIF VSYNC/ETH1 PPSTRIG M0/ _ _ _ _ ETH0 MDC M1/SAI3 LRCK M2/UAR I _ _ _ _ T3 RX M0/SPI3 MOSI M0/I2C7 S _ _ _ _ _ DA M1/GPIO3 A1 d | TOP IOC GPIO3A IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart tx _ |  | _ _ _ VI CIF HREF/ETH0 MDIO M1/SAI3 _ _ _ _ O SCLK M2/UART3 TX M0/SPI3 CL _ _ _ _ _ K M0/I2C7 SCL M1/GPIO3 A0 d | TOP IOC GPIO3A IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart cts _ n |  | _ _ _ _ _ VI CIF CLKO/ETH1 PPSCLK M0/ET I _ _ _ _ H0 RXCTL M1/SAI3 SDO M2/SPDI _ _ _ _ F RX1 M1/UART3 CTSN M0/SPI3 _ _ _ _ _ O MISO M0/CAN1 TX M3/MIPI TE M _ _ _ _ _ 1/GPIO3 A2 d | TOP IOC GPIO3A IO _ _ _ MUX SEL L[11:8]=4'h _ _ 9 |
| _ uart re _ |  |  |  |
| uart rts _ n |  | _ _ VI CIF CLKI/ETH1 PTP REFCLK M O _ _ _ _ _ 0/ETH0 RXD1 M1/SAI3 SDI M2/SP _ _ _ _ DIF TX1 M1/UART3 RTSN M0/SPI3 _ _ _ _ O CSN0 M0/CAN1 RX M3/GPIO3 A3 _ _ _ _ _ d | TOP IOC GPIO3A IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| _ uart de _ |  |  |  |
| _ IOMUX1 |  |  |  |
| uart rx _ |  | VO POST EMPTY/SPDIF TX0 M1/C _ _ _ _ AM CLK2 OUT M0/SAI4 SDO M1/ _ _ _ _ _ DSMC INT2/FLEXBUS0 D14 M0/FL I _ _ _ EXBUS1 D13 M0/FLEXBUS0 CSN _ _ _ _ M1/UART3 RX M1/I2C7 SDA M2/G _ _ _ _ PIO4 A1 d | TOP IOC GPIO4A IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart tx _ |  | _ _ SPDIF RX0 M1/CAM CLK1 OUT M _ _ _ _ _ 0/SAI4 LRCK M1/DSMC INT0/FLEX _ _ _ BUS0 D13 M0/FLEXBUS1 D14 M0/ O _ _ _ _ FLEXBUS1 CSN M3/UART3 TX M1/ _ _ _ _ SPI1 CSN1 M2/I2C7 SCL M2/MIPI _ _ _ _ TE M2/GPIO4 A0 d | TOP IOC GPIO4A IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart cts _ n _ |  | _ _ _ _ VO LCDC D12/VO EBC SDDO12/E I _ _ _ _ TH0 PPSTRIG M0/SAI1 SDI0 M1/D _ _ _ _ SMC DQS0/FLEXBUS1 D10/FLEXBU _ _ S1 CSN M0/UART2 RX M2/UART3 O _ _ _ _ _ CTSN M1/I2C4 SDA M3/GPIO3 B7 _ _ _ _ d | TOP IOC GPIO3B IO _ _ _ MUX SEL H[15:12]=4 _ _ 'ha |
| uart re _ |  |  |  |
| uart rts _ n |  | VO LCDC D11/VO EBC SDDO11/E O _ _ _ _ TH0 PPSCLK M0/SAI1 SDO3 M1/D _ _ _ _ SMC DATA7/FLEXBUS1 D9/UART2 _ _ _ O TX M2/UART3 RTSN M1/I2C4 SCL _ _ _ _ M3/GPIO3 C0 d | TOP IOC GPIO3C IO _ _ _ MUX SEL L[3:0]=4'ha _ _ |
| _ uart de _ |  |  |  |
| _ _ _ IOMUX2 |  |  |  |
| uart rx _ |  | ETH1 TXCLK M1/SDMMC1 CLK M0 _ _ _ _ I /SAI3 MCLK M1/PDM0 CLK0 M2/U _ _ _ _ ART3 RX M2/GPIO1 C1 d | TOP IOC GPIO1C IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart tx _ |  | _ _ _ _ ETH1 TXD3 M1/SDMMC1 CMD M0/ _ _ _ _ PDM0 SDI2 M2/UART3 TX M2/SPI O _ _ _ _ 1 CSN1 M0/PWM0 CH0 M1/GPIO1 _ _ _ _ C0 d | TOP IOC GPIO1C IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart cts _ n |  | _ _ ETH1 RXCLK M1/SDMMC1 D2 M0/ I _ _ _ _ SAI3 SDO M1/UART3 CTSN M2/SP _ _ _ _ I1 MISO M0/PCIE0 CLKREQN M1/ O _ _ _ _ GPIO1 B6 d | TOP IOC GPIO1B IO _ _ _ MUX SEL H[11:8]=4' _ _ h9 |
| _ uart re _ |  |  |  |
| uart rts _ n _ |  | _ _ ETH1 TXD2 M1/SDMMC1 D3 M0/S O _ _ _ _ AI3 SDI M1/EMMC TESTDATA OUT _ _ _ _ /FSPI0 TESTDATA OUT/FSPI1 TEST _ _ _ DATA OUT M1/UART3 RTSN M2/SP O _ _ _ _ I1 CSN0 M0/PCIE0 WAKEN M1/GP _ _ _ _ IO1 B7 d | TOP IOC GPIO1B IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| uart de _ |  |  |  |
| _ _ Table 33-5 UART4 Interface Description |  |  |  |
| Module Pin | i | D Pad Name r | IOMUX Setting |
| IOMUX0 |  |  |  |
| uart rx _ |  | ETH1 RXD0 M0/SAI4 SDO M3/UA _ _ _ _ I RT4 RX M0/I2C6 SDA M2/PWM2 _ _ _ _ _ CH1 M2/GPIO2 D1 d | TOP IOC GPIO2D IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart tx _ |  | _ _ _ ETH1 TXCTL M0/SAI4 SDI M3/UA _ _ _ _ O RT4 TX M0/I2C6 SCL M2/PWM2 C _ _ _ _ _ H0 M2/GPIO2 D0 d | TOP IOC GPIO2D IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart cts _ n |  | _ _ _ I ETH1 TXD0 M0/SAI4 SCLK M3/UA _ _ _ _ RT4 CTSN M0/I2C5 SCL M2/PWM1 _ _ _ _ O CH5 M2/GPIO2 C6 d _ _ _ _ | TOP IOC GPIO2C IO _ _ _ MUX SEL H[11:8]=4' _ _ h9 |
| _ uart re _ |  |  |  |
| uart rts _ n |  | O ETH1 TXD1 M0/SAI4 LRCK M3/UA _ _ _ _ RT4 RTSN M0/I2C5 SDA M2/PWM _ _ _ _ O 0 CH1 M2/GPIO2 C7 d _ _ _ _ | TOP IOC GPIO2C IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| _ uart de _ |  |  |  |
| IOMUX1 |  |  |  |
| uart rx _ |  | ETH1 TXD1 M1/FSPI1 D1 M1/UAR _ _ _ _ T4 RX M1/UART2 CTSN M0/SPI2 I _ _ _ _ _ MISO M1/PCIE1 BUTTONRSTN/GPI _ _ O1 C5 d | TOP IOC GPIO1C IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| uart tx _ |  | _ _ ETH1 TXD0 M1/FSPI1 D0 M1/UAR _ _ _ _ T4 TX M1/UART2 RTSN M0/SPI2 O _ _ _ _ _ MOSI M1/PCIE0 BUTTONRSTN/GPI _ _ O1 C4 d | TOP IOC GPIO1C IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| uart cts _ n |  | _ _ ETH1 PPSTRIG M1/SDMMC1 DETN I _ _ _ M0/FSPI1 CSN0 M1/UART4 CTSN _ _ _ _ M1/I2C6 SDA M1/SPI2 CSN0 M1 O _ _ _ _ _ /GPIO1 C3 u | TOP IOC GPIO1C IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| _ uart re _ |  |  |  |
| uart rts _ n _ |  | ETH1 PPSCLK M1/SDMMC1 PWREN O _ _ _ M0/FSPI1 RSTN M1/FSPI1 RSTN _ _ _ _ _ M1/UART4 RTSN M1/I2C6 SCL M1 _ _ _ _ O /SPI2 CSN1 M1/PWM1 CH2 M1/GP _ _ _ _ IO1 C2 u | TOP IOC GPIO1C IO _ _ _ MUX SEL L[11:8]=4'h _ _ 9 |
| uart de _ |  |  |  |
| _ _ IOMUX2 |  |  |  |
| uart rx _ |  | REF CLK2 OUT/I2C1 SDA M1/UAR _ _ _ _ I T4 RX M2/PWM1 CH1 M0/GPIO0 _ _ _ _ _ B5 d | PMU1 IOC GPIO0B I _ _ _ OMUX SEL H[7:1]=4' _ _ ha |
| uart tx _ |  | _ REF CLK1 OUT/I2C1 SCL M1/UAR _ _ _ _ O T4 TX M2/PWM1 CH0 M0/GPIO0 _ _ _ _ _ B4 d | PMU1 IOC GPIO0B I _ _ _ OMUX SEL H[3:0]=4' _ _ ha |
| _ Table 33-6 UART5 Interface Description |  |  |  |
| Module Pin | i | D Pad Name r | IOMUX Setting |
| IOMUX0 |  |  |  |
| uart rx _ |  | VO LCDC DEN/VO EBC SDLE/SAI1 _ _ _ _ SDI1 M1/DSMC DATA0/FLEXBUS1 I _ _ _ D1/UART5 RX M0/SPI3 CLK M1/I _ _ _ _ _ 2C3 SCL M2/GPIO3 D4 d | TOP IOC GPIO3D IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| uart tx _ |  | _ _ _ _ VO LCDC HSYNC/VO EBC GDCLK/ _ _ _ _ SAI1 SDI2 M1/DSMC CLKP/FLEXB O _ _ _ US1 D0/UART5 TX M0/SPI3 MISO _ _ _ _ M1/I2C3 SDA M2/GPIO3 D5 d | TOP IOC GPIO3D IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| uart cts _ n |  | _ _ _ _ _ VO LCDC VSYNC/VO EBC SDCLK/ I _ _ _ _ SAI1 SDI3 M1/DSMC CLKN/FLEXB _ _ _ US1 CLK/UART5 CTSN M0/SPI3 M _ _ _ _ O OSI M1/PWM2 CH6 M3/GPIO3 D6 _ _ _ _ d | TOP IOC GPIO3D IO _ _ _ MUX SEL H[11:2]=4' _ _ h9 |
| _ uart re _ |  |  |  |
| uart rts _ n _ |  | _ VO LCDC CLK/VO EBC SDOE/CAM _ _ _ _ O CLK0 OUT M0/SAI4 SCLK M1/DS _ _ _ _ _ MC RESETN/FLEXBUS0 D15 M0/FL _ _ _ EXBUS1 D12 M0/FLEXBUS1 CSN _ _ _ _ O M1/UART5 RTSN M0/SPI3 CSN1 M _ _ _ _ 1/PWM2 CH7 M3/GPIO3 D7 d | TOP IOC GPIO3D IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| uart de _ |  |  |  |
| _ _ _ _ IOMUX1 |  |  |  |
| uart rx _ |  | SAI1 SDO2 M0/SAI1 SDI2 M0/PD _ _ _ _ M1 SDI2 M1/FLEXBUS1 D14 M1/S _ _ _ _ I PI4 MOSI M2/UART5 RX M1/UART _ _ _ _ 6 CTSN M0/UART2 CTSN M1/GPIO _ _ _ _ 4 B1 d | TOP IOC GPIO4B IO _ _ _ MUX SEL L[7:1]=4'ha _ _ |
| uart tx _ |  | _ _ SAI1 SDO1 M0/SAI1 SDI3 M0/PD _ _ _ _ M1 CLK1 M1/FLEXBUS1 D13 M1/S _ _ _ _ O PI4 CLK M2/UART5 TX M1/UART6 _ _ _ _ RTSN M0/UART2 RTSN M1/GPIO4 _ _ _ _ B0 d | TOP IOC GPIO4B IO _ _ _ MUX SEL L[3:0]=4'ha _ _ |
| uart cts _ n |  | _ _ SAI1 LRCK M0/FLEXBUS1 D12 M1 I _ _ _ _ /SPI4 CSN1 M2/UART5 CTSN M1/I _ _ _ _ 2C2 SDA M2/PCIE1 CLKREQN M2/ O _ _ _ _ GPIO4 A5 d | TOP IOC GPIO4A IO _ _ _ MUX SEL H[7:4]=4'h _ _ a |
| _ uart re _ |  |  |  |
| uart rts _ n |  | _ _ SAI1 SCLK M0/FLEXBUS1 CSN M4 O _ _ _ _ /SPI3 CSN0 M2/UART5 RTSN M1/I _ _ _ _ 2C2 SCL M2/PWM2 CH4 M1/GPIO O _ _ _ _ 4 A3 d | TOP IOC GPIO4A IO _ _ _ MUX SEL L[15:12]=4' _ _ ha |
| _ uart de _ |  |  |  |
| IOMUX2 |  |  |  |
| uart rx _ |  | SDMMC0 CMD/FSPI1 CSN0 M0/SAI _ _ _ 3 SDO M3/UART5 RX M2/I2C5 SD I _ _ _ _ _ A M0/SPI0 CSN0 M1/PWM2 CH4 _ _ _ _ _ M0/GPIO2 A4 d | TOP IOC GPIO2A IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| uart tx _ |  | _ _ SDMMC0 CLK/FSPI1 CLK M0/SAI3 _ _ _ SCLK M3/TEST CLK OUT/UART5 O _ _ _ _ _ TX M2/I2C5 SCL M0/SPI0 CLK M1 _ _ _ _ _ /I3C1 SDA PU M1/GPIO2 A5 d | TOP IOC GPIO2A IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| uart cts _ n _ |  | _ _ _ _ _ SDMMC0 D3/FSPI1 D3 M0/DSM A I _ _ _ _ UD RN M0/SAI3 SDI M3/JTAG TM _ _ _ _ _ S M0/UART5 CTSN M2/CAN1 TX O _ _ _ _ _ M0/I3C1 SDA M1/GPIO2 A3 d _ _ _ _ | TOP IOC GPIO2A IO _ _ _ MUX SEL L[15:12]=4' _ _ ha |
| uart re _ |  |  |  |
| uart rts _ n _ |  | SDMMC0 D2/FSPI1 D2 M0/DSM A O _ _ _ _ UD RP M0/SAI3 LRCK M3/JTAG T _ _ _ _ _ CK M0/UART5 RTSN M2/SPI0 CSN _ _ _ _ 1 M1/CAN1 RX M0/I3C1 SCL M1/ O _ _ _ _ _ GPIO2 A2 d | TOP IOC GPIO2A IO _ _ _ MUX SEL L[11:8]=4'h _ _ a |
| uart de _ |  |  |  |
| _ _ Table 33-7 UART6 Interface Description |  |  |  |
| Module Pin | i | D Pad Name r | IOMUX Setting |
| IOMUX0 |  |  |  |
| uart rx _ |  | SAI4 LRCK M0/PDM1 CLK0 M1/FL _ _ _ _ EXBUS0 D14 M1/SPI3 MISO M2/U I _ _ _ _ ART6 RX M0/I2C4 SDA M1/CAN0 _ _ _ _ _ RX M2/GPIO4 A6 d | TOP IOC GPIO4A IO _ _ _ MUX SEL H[11:8]=4' _ _ ha |
| uart tx _ |  | _ _ _ SAI4 SCLK M0/PDM1 SDI3 M1/FL _ _ _ _ EXBUS0 D13 M1/SPI3 MOSI M2/U O _ _ _ _ ART6 TX M0/I2C4 SCL M1/CAN0 _ _ _ _ _ TX M2/GPIO4 A4 d | TOP IOC GPIO4A IO _ _ _ MUX SEL H[3:0]=4'h _ _ a |
| uart cts _ n |  | _ _ _ SAI1 SDO2 M0/SAI1 SDI2 M0/PD I _ _ _ _ M1 SDI2 M1/FLEXBUS1 D14 M1/S _ _ _ _ PI4 MOSI M2/UART5 RX M1/UART _ _ _ _ O 6 CTSN M0/UART2 CTSN M1/GPIO _ _ _ _ 4 B1 d | TOP IOC GPIO4B IO _ _ _ MUX SEL L[7:4]=4'hb _ _ |
| _ uart re _ |  |  |  |
| uart rts _ n |  | _ _ SAI1 SDO1 M0/SAI1 SDI3 M0/PD O _ _ _ _ M1 CLK1 M1/FLEXBUS1 D13 M1/S _ _ _ _ PI4 CLK M2/UART5 TX M1/UART6 _ _ _ _ O RTSN M0/UART2 RTSN M1/GPIO4 _ _ _ _ B0 d | TOP IOC GPIO4B IO _ _ _ MUX SEL L[3:0]=4'hb _ _ |
| _ uart de _ |  |  |  |
| _ _ IOMUX1 |  |  |  |
| uart rx _ |  | ETH1 RXCTL M0/UART6 RX M1/I3 _ _ _ _ I C1 SDA M0/PWM2 CH3 M2/GPIO2 _ _ _ _ D3 d | TOP IOC GPIO2D IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| uart tx _ |  | _ _ CAM CLK0 OUT M1/ETH1 RXD1 M _ _ _ _ _ 0/SAI4 MCLK M3/UART6 TX M1/I3 O _ _ _ _ C1 SCL M0/PWM2 CH2 M2/GPIO2 _ _ _ _ D2 d | TOP IOC GPIO2D IO _ _ _ MUX SEL L[11:8]=4'h _ _ 9 |
| uart cts _ n |  | _ _ I ISP FLASH TRIGOUT M0/ETH1 MD _ _ _ _ IO M0/UART6 CTSN M1/I2C9 SCL _ _ _ _ O M2/PWM2 CH5 M2/GPIO2 D5 d _ _ _ _ _ | TOP IOC GPIO2D IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| _ uart re _ |  |  |  |
| uart rts _ n |  | ISP PRELIGHT TRIG M0/ETH1 MD O _ _ _ _ C M0/UART6 RTSN M1/I2C9 SDA | TOP IOC GPIO2D IO _ _ _ MUX SEL H[3:0]=4'h |
| uart de _ |  | M2/PWM2 CH4 M2/GPIO2 D4 d O _ _ _ _ | 9 |
| IOMUX2 |  |  |  |
| uart rx _ |  | EMMC RSTN/FSPI0 CSN0/UART6 R _ _ _ I X M2/I2C7 SDA M0/MIPI TE M3/P _ _ _ _ _ WM2 CH1 M0/GPIO1 B3 u | TOP IOC GPIO1B IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| uart tx _ |  | _ _ _ _ EMMC CMD/FSPI0 RSTN/FSPI0 CS _ _ _ O N1/UART6 TX M2/I2C7 SCL M0/G _ _ _ _ PIO1 B0 u | TOP IOC GPIO1B IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart cts _ n |  | _ _ EMMC D3/FSPI0 D3/SAI0 SDO2 M I _ _ _ _ 2/SAI0 SDI2 M2/PDM0 SDI1 M1/U _ _ _ _ ART7 RX M1/UART6 CTSN M2/GPI O _ _ _ _ O1 A3 u | TOP IOC GPIO1A IO _ _ _ MUX SEL L[15:12]=4' _ _ ha |
| _ uart re _ |  |  |  |
| uart rts _ n |  | _ _ EMMC D2/FSPI0 D2/SAI0 SDO1 M O _ _ _ _ 2/SAI0 SDI3 M2/PDM0 SDI3 M1/U _ _ _ _ ART7 TX M1/UART6 RTSN M2/GPI O _ _ _ _ O1 A2 u | TOP IOC GPIO1A IO _ _ _ MUX SEL L[11:8]=4'h _ _ a |
| _ uart de _ |  |  |  |
| _ _ IOMUX3 |  |  |  |
| uart rx _ |  | ISP FLASH TRIGOUT M1/SAI4 SD _ _ _ _ O M2/VP0 SYNC OUT/SATA1 ACTL _ _ _ _ I ED M1/I2C3 SDA M3/SPI4 MOSI _ _ _ _ _ M0/UART6 RX M3/PWM2 CH5 M1/ _ _ _ _ GPIO4 C5 d | VCCIO6 IOC GPIO4C _ _ IOMUX SEL H[7:4]= _ _ _ 4'hd |
| uart tx _ |  | _ _ ISP PRELIGHT TRIG M1/SAI4 LRC _ _ _ _ K M2/DP HPDIN M0/I2C3 SCL M3 O _ _ _ _ _ /SPI4 CSN0 M0/UART6 TX M3/PW _ _ _ _ M2 CH6 M1/GPIO4 C4 d | VCCIO6 IOC GPIO4C _ _ IOMUX SEL H[3:0]= _ _ _ 4'hd |
| _ _ _ _ Table 33-8 UART7 Interface Description |  |  |  |
| Module Pin | i | D Pad Name r | IOMUX Setting |
| IOMUX0 |  |  |  |
| uart rx _ |  | VI CIF D6/ETH0 RXD2 M1/SAI0 L _ _ _ _ _ I RCK M0/UART7 RX M0/UART8 CTS _ _ _ _ N M1/I2C8 SDA M2/GPIO2 B7 d | TOP IOC GPIO2B IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| uart tx _ |  | _ _ _ _ _ VI CIF D7/ETH1 PTP REFCLK M1/ _ _ _ _ _ ETH0 RXD3 M1/SAI0 SCLK M0/UA O _ _ _ _ RT7 TX M0/UART8 RTSN M1/I2C8 _ _ _ _ SCL M2/GPIO2 B6 d | TOP IOC GPIO2B IO _ _ _ MUX SEL H[11:8]=4' _ _ h9 |
| uart cts _ n _ |  | _ _ _ _ VI CIF D9/SDMMC1 PWREN M1/ET I _ _ _ _ H0 TXD2 M1/SAI0 SDI3 M0/PDM0 _ _ _ _ SDI0 M3/UART7 CTSN M0/SPI4 _ _ _ _ _ MOSI M3/SATA0 ACTLED M0/GPIO O _ _ _ 2 B4 d | TOP IOC GPIO2B IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| uart re _ |  |  |  |
| uart rts _ n _ |  | _ _ VI CIF D8/SDMMC1 DETN M1/ETH O _ _ _ _ 0 RXCLK M1/SAI0 MCLK M0/PDM0 _ _ _ _ CLK0 M3/UART7 RTSN M0/SPI4 _ _ _ _ _ MISO M3/SATA1 ACTLED M0/GPIO O _ _ _ 2 B5 d | TOP IOC GPIO2B IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| uart de _ |  |  |  |
| _ _ IOMUX1 |  |  |  |
| uart rx _ |  | EMMC D3/FSPI0 D3/SAI0 SDO2 M _ _ _ _ 2/SAI0 SDI2 M2/PDM0 SDI1 M1/U I _ _ _ _ ART7 RX M1/UART6 CTSN M2/GPI _ _ _ _ O1 A3 u | TOP IOC GPIO1A IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| uart tx _ |  | _ _ EMMC D2/FSPI0 D2/SAI0 SDO1 M O _ _ _ _ 2/SAI0 SDI3 M2/PDM0 SDI3 M1/U | TOP IOC GPIO1A IO _ _ _ MUX SEL L[11:8]=4'h |
|  |  | ART7 TX M1/UART6 RTSN M2/GPI _ _ _ _ O1 A2 u | 9 |
| uart cts _ n |  | _ _ I EMMC D1/FSPI0 D1/SAI0 LRCK M _ _ _ _ 2/UART7 CTSN M1/I2C2 SDA M1/ _ _ _ _ O GPIO1 A1 u _ _ | TOP IOC GPIO1A IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| _ uart re _ |  |  |  |
| uart rts _ n |  | O EMMC D0/FSPI0 D0/SAI0 SCLK M _ _ _ _ 2/UART7 RTSN M1/I2C2 SCL M1/ _ _ _ _ O GPIO1 A0 u _ _ | TOP IOC GPIO1A IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| _ uart de _ |  |  |  |
| IOMUX2 |  |  |  |
| uart rx _ |  | SDMMC0 D0/FSPI1 D0 M0/DSM A _ _ _ _ UD LP M0/UART0 RX M1/UART7 R _ _ _ _ _ I X M2/I2C8 SCL M0/SPI0 MOSI M _ _ _ _ _ 1/CAN0 RX M0/PWM2 CH2 M0/GP _ _ _ _ IO2 A0 d | TOP IOC GPIO2A IO _ _ _ MUX SEL L[3:0]=4'ha _ _ |
| uart tx _ |  | _ _ SDMMC0 D1/FSPI1 D1 M0/DSM A _ _ _ _ UD LN M0/SAI3 MCLK M3/UART0 _ _ _ _ _ O TX M1/UART7 TX M2/I2C8 SDA M _ _ _ _ _ 0/SPI0 MISO M1/CAN0 TX M0/PW _ _ _ _ M2 CH3 M0/GPIO2 A1 d | TOP IOC GPIO2A IO _ _ _ MUX SEL L[7:4]=4'ha _ _ |
| _ _ _ _ Table 33-9 UART8 Interface Description |  |  |  |
| Module Pin | i | D Pad Name r | IOMUX Setting |
| IOMUX0 |  |  |  |
| uart rx _ |  | VO LCDC D6/VO EBC SDDO6/SAI _ _ _ _ 1 SDO0 M1/DSMC DATA4/FLEXBU I _ _ _ S1 D6/UART8 RX M0/SPI1 MISO _ _ _ _ _ M2/PWM2 CH2 M3/GPIO3 C5 d | TOP IOC GPIO3C IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| uart tx _ |  | _ _ _ _ VO LCDC D5/VO EBC SDDO5/SAI _ _ _ _ 1 LRCK M1/DSMC DATA3/FLEXBUS O _ _ _ 1 D5/UART8 TX M0/SPI1 MOSI M _ _ _ _ _ 2/GPIO3 C6 d | TOP IOC GPIO3C IO _ _ _ MUX SEL H[11:8]=4' _ _ h9 |
| uart cts _ n _ |  | _ _ VO LCDC D3/VO EBC SDDO3/SAI I _ _ _ _ 1 MCLK M1/DSMC DATA1/FLEXBUS _ _ _ 1 D3/UART8 CTSN M0/SPI1 CSN0 O _ _ _ _ M2/PWM2 CH3 M3/GPIO3 D0 d _ _ _ _ _ | TOP IOC GPIO3D IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart re _ |  |  |  |
| uart rts _ n |  | VO LCDC D4/VO EBC SDDO4/SAI O _ _ _ _ 1 SCLK M1/DSMC DATA2/FLEXBUS _ _ _ 1 D4/UART8 RTSN M0/SPI1 CLK O _ _ _ _ _ M2/GPIO3 C7 d | TOP IOC GPIO3C IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| _ uart de _ |  |  |  |
| _ _ IOMUX1 |  |  |  |
| uart rx _ |  | VI CIF D14/SDMMC1 D1 M1/ETH0 _ _ _ _ TXCTL M1/SAI0 SDO1 M0/UART8 I _ _ _ _ RX M1/I2C4 SDA M2/GPIO2 A7 _ _ _ _ _ _ d | TOP IOC GPIO2A IO _ _ _ MUX SEL H[15:12]=4 _ _ 'h9 |
| uart tx _ |  | VI CIF D15/SDMMC1 D0 M1/ETH0 _ _ _ _ RXD0 M1/SAI0 SDO0 M0/UART8 O _ _ _ _ _ TX M1/SPI4 CSN1 M3/I2C4 SCL _ _ _ _ _ M2/GPIO2 A6 d | TOP IOC GPIO2A IO _ _ _ MUX SEL H[11:8]=4' _ _ h9 |
| uart cts _ n |  | _ _ I VI CIF D6/ETH0 RXD2 M1/SAI0 L _ _ _ _ _ RCK M0/UART7 RX M0/UART8 CTS _ _ _ _ O N M1/I2C8 SDA M2/GPIO2 B7 d _ _ _ _ _ | TOP IOC GPIO2B IO _ _ _ MUX SEL H[15:12]=4 _ _ 'ha |
| _ uart re _ |  |  |  |
| uart rts _ n |  | VI CIF D7/ETH1 PTP REFCLK M1/ O _ _ _ _ _ ETH0 RXD3 M1/SAI0 SCLK M0/UA _ _ _ _ RT7 TX M0/UART8 RTSN M1/I2C8 O _ _ _ _ SCL M2/GPIO2 B6 d | TOP IOC GPIO2B IO _ _ _ MUX SEL H[11:8]=4' _ _ ha |
| _ uart de _ |  |  |  |
| _ _ _ _ IOMUX2 |  |  |  |
| uart rx _ |  | I2C0 SDA M1/UART8 RX M2/I3C0 I _ _ _ _ SDA M0/GPIO0 C2 d _ _ _ _ | PMU1 IOC GPIO0C I _ _ _ OMUX SEL L[11:8]=4 _ _ 'ha |
| uart tx _ |  | I2C0 SCL M1/UART8 TX M2/I3C0 O _ _ _ _ _ SCL M0/GPIO0 C1 d _ _ _ | PMU1 IOC GPIO0C I _ _ _ OMUX SEL L[7:4]=4' _ _ ha |
| Table 33-10 UART9 Interface Description |  |  |  |
| Module Pin | i | D Pad Name r | IOMUX Setting |
| IOMUX0 |  |  |  |
| uart rx _ |  | VI CIF D5/ETH1 RXD2 M0/ETH0 P _ _ _ _ _ TP REFCLK M1/PDM1 SDI1 M0/UA I _ _ _ _ RT9 RX M0/PWM1 CH0 M2/GPIO2 _ _ _ _ C0 d | TOP IOC GPIO2C IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart tx _ |  | _ _ VI CIF D4/ETH1 RXD3 M0/ETH0 P _ _ _ _ _ PSCLK M1/SAI2 MCLK M1/PDM1 C O _ _ _ _ LK1 M0/UART9 TX M0/SPI1 CSN1 _ _ _ _ M1/PWM1 CH1 M2/GPIO2 C1 d | TOP IOC GPIO2C IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart cts _ n _ |  | _ _ _ _ _ CAM CLK2 OUT M1/ETH1 MCLK M I _ _ _ _ _ 0/ETH CLK0 25M OUT M1/SAI0 S _ _ _ _ _ DO3 M0/SPDIF TX0 M2/UART9 CT _ _ _ _ SN M0/SPI3 CSN1 M0/PWM2 CH7 O _ _ _ _ M2/GPIO2 D7 d | TOP IOC GPIO2D IO _ _ _ MUX SEL H[15:8]=4' _ _ h9 |
| uart re _ |  |  |  |
| uart rts _ n _ |  | _ _ _ CAM CLK1 OUT M1/ETH CLK1 25 O _ _ _ _ _ M OUT M0/ETH0 MCLK M1/SAI3 _ _ _ _ _ MCLK M2/SPDIF RX0 M2/UART9 R _ _ _ _ TSN M0/I3C1 SDA PU M0/PWM2 O _ _ _ _ _ CH6 M2/GPIO2 D6 d | TOP IOC GPIO2D IO _ _ _ MUX SEL H[11:8]=4' _ _ h9 |
| uart de _ |  |  |  |
| _ _ _ IOMUX1 |  |  |  |
| uart rx _ |  | VO LCDC D17/VO EBC SDCE1/ET _ _ _ _ H0 RXD0 M0/PDM1 SDI1 M2/DSM I _ _ _ _ C DATA11/FLEXBUS0 D3/UART9 R _ _ _ X M1/I2C8 SDA M3/GPIO3 B2 d | TOP IOC GPIO3B IO _ _ _ MUX SEL L[11:8]=4'h _ _ 9 |
| uart tx _ |  | _ _ _ _ _ VO LCDC D16/VO EBC SDCE0/ET _ _ _ _ H0 TXCTL M0/PDM1 SDI0 M2/DS O _ _ _ _ MC DATA10/FLEXBUS0 D2/UART9 _ _ _ TX M1/I2C8 SCL M3/GPIO3 B3 d | TOP IOC GPIO3B IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| uart cts _ n |  | _ _ _ _ _ VO LCDC D14/VO EBC SDDO14/E I _ _ _ _ TH0 TXD0 M0/SPDIF TX1 M0/DSM _ _ _ _ C DATA8/FLEXBUS0 D0/UART9 CT _ _ _ O SN M1/PWM1 CH5 M3/GPIO3 B5 _ _ _ _ _ d | TOP IOC GPIO3B IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| _ uart re _ |  |  |  |
| uart rts _ n |  | VO LCDC D15/VO EBC SDDO15/E O _ _ _ _ TH0 TXD1 M0/SPDIF RX1 M0/DSM _ _ _ _ C DATA9/FLEXBUS0 D1/UART9 RT _ _ _ O SN M1/PWM1 CH4 M3/GPIO3 B4 _ _ _ _ _ d | TOP IOC GPIO3B IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| _ uart de _ |  |  |  |
| IOMUX2 |  |  |  |
| uart rx |  | I DSM AUD RN M1/HDMI TX SDA/I | VCCIO6 IOC GPIO4C |
|  |  | 2C2 SDA M3/CAN0 RX M1/UART9 _ _ _ _ RX M2/PWM2 CH1 M1/GPIO4 C3 _ _ _ _ _ d | IOMUX SEL L[15:12 _ _ _ ]=4'hd |
| uart tx _ |  | _ DSM AUD RP M1/HDMI TX SCL/I2 _ _ _ _ _ O C2 SCL M3/CAN0 TX M1/UART9 T _ _ _ _ _ X M2/PWM2 CH0 M1/GPIO4 C2 d | VCCIO6 IOC GPIO4C _ _ IOMUX SEL L[11:8] _ _ _ =4'hd |

## Page 1158 -- pin table

| Module Pin | i | D Pad Name r | IOMUX Setting |
|---|---|---|---|
| IOMUX0 |  |  |  |
| uart rx _ |  | VO LCDC D19/VO EBC SDCE3/ET _ _ _ _ H0 MCLK M0/SAI4 MCLK M1/DSM _ _ _ _ I C CSN1/FLEXBUS0 D8/UART10 RX _ _ _ M0/SPI2 MOSI M2/PWM0 CH0 M _ _ _ _ _ 3/GPIO3 B0 d | TOP IOC GPIO3B IO _ _ _ MUX SEL L[3:0]=4'h9 _ _ |
| uart tx _ |  | _ _ VO LCDC D18/VO EBC SDCE2/ET _ _ _ _ H0 RXD1 M0/PDM1 CLK0 M2/DSM _ _ _ _ O C DATA12/FLEXBUS0 D4/UART10 _ _ _ TX M0/SPI4 CSN0 M1/PWM1 CH3 _ _ _ _ M3/GPIO3 B1 d | TOP IOC GPIO3B IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart cts _ n _ |  | _ _ _ VO LCDC D21/VO EBC GDOE/ETH I _ _ _ _ 0 MDC M0/PDM1 SDI2 M2/DSMC _ _ _ _ _ DATA14/FLEXBUS0 D6/UART1 RX _ _ _ M2/UART10 CTSN M0/PWM1 CH2 O _ _ _ _ M3/GPIO3 A6 d | TOP IOC GPIO3A IO _ _ _ MUX SEL H[11:8]=4' _ _ ha |
| uart re _ |  |  |  |
| uart rts _ n |  | _ _ VO LCDC D20/VO EBC VCOM/ETH O _ _ _ _ 0 RXCTL M0/PDM1 CLK1 M2/DSM _ _ _ _ C DATA13/FLEXBUS0 D5/UART1 T _ _ _ O X M2/UART10 RTSN M0/GPIO3 A7 _ _ _ _ d | TOP IOC GPIO3A IO _ _ _ MUX SEL H[15:12]=4 _ _ 'ha |
| _ uart de _ |  |  |  |
| _ IOMUX1 |  |  |  |
| uart rx _ |  | I ETH1 RXCTL M1/SAI2 SCLK M0/U _ _ _ _ ART10 RX M1/I3C0 SDA PU M1/G _ _ _ _ _ PIO1 D1 d | TOP IOC GPIO1D IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart tx _ |  | _ _ O ETH1 RXD1 M1/SAI2 SDO M0/UA _ _ _ _ RT10 TX M1/GPIO1 D0 d | TOP IOC GPIO1D IO _ _ _ MUX SEL L[3:0]=4'h9 |
| uart cts _ n _ |  | _ _ _ _ I ETH CLK1 25M OUT M1/FSPI1 CL _ _ _ _ _ K M1/PDM0 CLK1 M2/SPDIF TX1 _ _ _ _ _ M2/UART10 CTSN M1/I2C5 SDA M O _ _ _ _ 1/SPI2 CLK M1/SATA MPSWIT/CLK _ _ _ 1 32K OUT/GPIO1 D5 d | _ _ TOP IOC GPIO1D IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| uart re _ |  |  |  |
| uart rts _ n |  | _ _ _ _ O ETH1 MCLK M1/SAI2 MCLK M0/PD _ _ _ _ M0 SDI3 M2/SPDIF RX1 M2/UART _ _ _ _ O 10 RTSN M1/I2C5 SCL M1/GPIO1 _ _ _ _ D4 d | TOP IOC GPIO1D IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| _ uart de _ |  |  |  |
| _ _ IOMUX2 |  |  |  |
| uart rx _ |  | I SAI0 SDO0 M1/DP HPDIN M1/UAR _ _ _ _ T10 RX M2/I3C0 SDA PU M0/GPI _ _ _ _ _ O0 C5 d | PMU1 IOC GPIO0C I _ _ _ OMUX SEL H[7:4]=4' _ _ ha |
| uart tx _ |  | _ _ O SAI0 MCLK M1/PDM0 CLK0 M0/UA _ _ _ _ RT10 TX M2/PWM0 CH0 M0/GPIO _ _ _ _ 0 C4 d | PMU1 IOC GPIO0C I _ _ _ OMUX SEL H[3:0]=4' _ _ ha |

## Page 1159 -- pin table

| Module Pin | i | D Pad Name r | IOMUX Setting |
|---|---|---|---|
| IOMUX0 |  |  |  |
| uart rx _ |  | VO LCDC D10/VO EBC SDDO10/E _ _ _ _ TH0 PTP REFCLK M0/SAI1 SDO2 _ _ _ _ _ I M1/DSMC DATA6/FLEXBUS1 D8/UA _ _ RT11 RX M0/SPI2 MISO M2/I2C5 _ _ _ _ _ SDA M3/CAN0 RX M3/GPIO3 C1 d | TOP IOC GPIO3C IO _ _ _ MUX SEL L[7:4]=4'h9 _ _ |
| uart tx _ |  | _ _ _ _ _ VO LCDC D7/VO EBC SDDO7/SAI _ _ _ _ 1 SDO1 M1/DSMC DATA5/FLEXBU _ _ _ O S1 D7/UART11 TX M0/SPI2 CSN0 _ _ _ _ M2/I2C5 SCL M3/CAN0 TX M3/G _ _ _ _ _ PIO3 C4 d | TOP IOC GPIO3C IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| uart cts _ n _ |  | _ _ VO LCDC D8/VO EBC SDDO8/ETH _ _ _ _ I 0 TXD2 M0/SAI2 LRCK M2/DSMC _ _ _ _ _ INT3/FLEXBUS0 D10/FLEXBUS0 CS _ _ N M2/UART11 CTSN M0/SPI4 MOS _ _ _ _ O I M1/I2C9 SDA M3/PWM2 CH1 M _ _ _ _ _ 3/GPIO3 C3 d | TOP IOC GPIO3C IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| uart re _ |  |  |  |
| uart rts _ n _ |  | _ _ VO LCDC D9/VO EBC SDDO9/ETH O _ _ _ _ 0 TXD3 M0/SAI2 SCLK M2/DSMC _ _ _ _ _ INT1/FLEXBUS0 D9/UART11 RTSN _ _ _ M0/SPI4 MISO M1/I2C9 SCL M3/P O _ _ _ _ WM2 CH0 M3/GPIO3 C2 d | TOP IOC GPIO3C IO _ _ _ MUX SEL L[11:8]=4'h _ _ 9 |
| uart de _ |  |  |  |
| _ _ _ _ IOMUX1 |  |  |  |
| uart rx _ |  | VI CIF D0/ETH1 TXCLK M0/SAI2 _ _ _ _ _ SDI M1/PDM1 CLK0 M0/UART11 R I _ _ _ _ X M1/SPI1 CLK M1/PWM1 CH4 M _ _ _ _ _ 2/GPIO2 C5 d | TOP IOC GPIO2C IO _ _ _ MUX SEL H[7:4]=4'h _ _ 9 |
| uart tx _ |  | _ _ VI CIF D1/ETH1 TXD3 M0/SAI2 S _ _ _ _ _ DO M1/PDM1 SDI0 M0/UART11 T O _ _ _ _ X M1/SPI1 CSN0 M1/PWM1 CH3 _ _ _ _ _ M2/GPIO2 C4 d | TOP IOC GPIO2C IO _ _ _ MUX SEL H[3:0]=4'h _ _ 9 |
| uart cts _ n |  | _ _ VI CIF D3/ETH1 RXCLK M0/ETH0 I _ _ _ _ _ PPSTRIG M1/SAI2 SCLK M1/PDM1 _ _ _ SDI2 M0/UART11 CTSN M1/SPI1 _ _ _ _ O MOSI M1/PWM1 CH2 M2/GPIO2 _ _ _ _ _ C2 d | TOP IOC GPIO2C IO _ _ _ MUX SEL L[11:8]=4'h _ _ 9 |
| _ uart re _ |  |  |  |
| uart rts _ n |  | _ VI CIF D2/ETH1 TXD2 M0/SAI2 L O _ _ _ _ _ RCK M1/PDM1 SDI3 M0/UART11 R _ _ _ _ TSN M1/SPI1 MISO M1/PWM0 CH O _ _ _ _ 0 M2/GPIO2 C3 d | TOP IOC GPIO2C IO _ _ _ MUX SEL L[15:12]=4' _ _ h9 |
| _ uart de _ |  |  |  |
| _ _ _ IOMUX2 |  |  |  |
| uart rx _ |  | DSM AUD LN M1/HDMI TX HPDIN _ _ _ _ _ M0/PCIE1 CLKREQN M3/I2C7 SD _ _ _ _ I A M3/EDP TX HPDIN M0/UART11 _ _ _ _ _ RX M2/PWM0 CH1 M1/GPIO4 C1 _ _ _ _ _ d | VCCIO6 IOC GPIO4C _ _ IOMUX SEL L[7:4]= _ _ _ 4'hd |
| uart tx _ |  | DSM AUD LP M1/SAI4 MCLK M2/ _ _ _ _ _ HDMI TX CEC M0/I2C7 SCL M3/S O _ _ _ _ _ PI4 CSN1 M0/UART11 TX M2/PWM _ _ _ _ 1 CH5 M1/GPIO4 C0 d | VCCIO6 IOC GPIO4C _ _ IOMUX SEL L[3:0]= _ _ _ 4'hd |

## Page 1166 -- pin table

| . hen the input of phase B is ON and phase A is OFF->ON, the count de hen the A-phase input is ON and the B-phase input is ON->OFF, the co . hen the input of phase B is OFF and the input of phase A is ON->OFF, ecreases by 1. 4.4 Register Description 4.4.1 Internal Address Mapping lave address can be divided into different length for different controller ollows. Operational Base Name Base Address PWM0 0x27330000 PWM1 0x2ADD0000 PWM2 0x2ADE0000 |  |  |
|---|---|---|
|  | Name | Base Address |
|  | PWM0 | 0x27330000 |
|  | PWM1 | 0x2ADD0000 |
|  | PWM2 | 0x2ADE0000 |

## Page 1194 -- pin table

| Module Pin | Direc tion | _ Pin Name | IOMUX Setting |
|---|---|---|---|
| PWM0 _ CH0 M _ 0 | I/O | SAI0 MCLK M1/PDM0 CLK0 M0/UART10 TX M2/PW _ _ _ _ _ _ M0 CH0 M0/GPIO0 C4 d _ _ _ _ | PMU1 IOC GPIO0C IOMUX _ _ _ SEL H[3:0] = 0xc _ _ |
| PWM0 _ CH1 M _ 0 | I/O | PDM0 CLK1 M0/HDMI TX CEC M1/SPI0 CSN1 M0/ _ _ _ _ _ _ _ PWM0 CH1 M0/GPIO0 C3 d _ _ _ _ | PMU1 IOC GPIO0C IOMUX _ _ _ SEL L[15:12] = 0xc _ _ |
| PWM1 _ CH0 M _ 0 | I/O | REF CLK1 OUT/I2C1 SCL M1/UART4 TX M2/PWM1 _ _ _ _ _ _ CH0 M0/GPIO0 B4 d _ _ _ _ | PMU1 IOC GPIO0B IOMUX _ _ _ SEL H[3:0] = 0xc _ _ |
| PWM1 _ CH1 M _ 0 | I/O | REF CLK2 OUT/I2C1 SDA M1/UART4 RX M2/PWM1 _ _ _ _ _ _ CH1 M0/GPIO0 B5 d _ _ _ _ | PMU1 IOC GPIO0B IOMUX _ _ _ SEL H[7:4] = 0xc _ _ |
| PWM1 _ CH2 M _ 0 | I/O | SDMMC0 PWREN/SDMMC1 DETN M2/HDMI TX HPD _ _ _ _ _ IN M1/EDP TX HPDIN M1/PWM1 CH2 M0/GPIO0 B _ _ _ _ _ _ _ 6 d _ | PMU1 IOC GPIO0B IOMUX _ _ _ SEL H[11:8] = 0xc _ _ |
| PWM1 _ CH3 M _ 0 | I/O | I2C2 SDA M0/UART1 RX M0/CPULIT AVS/PWM1 C _ _ _ _ _ _ H3 M0/GPIO0 C0 d _ _ _ | PMU1 IOC GPIO0C IOMUX _ _ _ SEL L[3:0 ] = 0xc _ _ |
| PWM1 _ CH4 M _ 0 | I/O | I2C2 SCL M0/UART1 TX M0/NPU AVS/PWM1 CH4 _ _ _ _ _ _ _ M0/GPIO0 B7 d _ _ | PMU1 IOC GPIO0B IOMUX _ _ _ SEL H[15:12] = 0xc _ _ |

## Page 1195 -- pin table

| Module Pin | Direc tion | Pin Name | IOMUX Setting |
|---|---|---|---|
| PWM1 _ CH5 M _ 0 | I/O | SAI0 SDI2 M1/SAI0 SDO2 M1/PDM0 SDI2 M0/I2C _ _ _ _ _ _ 4 SCL M0/CPUBIG AVS/PWM1 CH5 M0/UART1 CTS _ _ _ _ _ _ N M0/GPIO0 D2 d _ _ _ | PMU1 IOC GPIO0D IOMUX _ _ _ SEL L[11:8] = 0xc _ _ |
| PWM2 _ CH0 M _ 0 | I/O | SAI0 SDI3 M1/SAI0 SDO1 M1/PDM0 SDI3 M0/I2C _ _ _ _ _ _ 4 SDA M0/GPU AVS/PWM2 CH0 M0/UART1 RTSN _ _ _ _ _ _ _ M0/GPIO0 D3 d _ _ | PMU1 IOC GPIO0C IOMUX _ _ _ SEL L[15:12] = 0xc _ _ |
| PWM2 _ CH1 M _ 0 | I/O | EMMC RSTN/FSPI0 CSN0/UART6 RX M2/I2C7 SDA _ _ _ _ _ M0/MIPI TE M3/PWM2 CH1 M0/GPIO1 B3 u _ _ _ _ _ _ _ | TOP IOC GPIO1B IOMUX S _ _ _ _ EL L[15:12] = 0xc _ |
| PWM2 _ CH2 M _ 0 | I/O | SDMMC0 D0/FSPI1 D0 M0/DSM AUD LP M0/UART0 _ _ _ _ _ _ RX M1/UART7 RX M2/I2C8 SCL M0/SPI0 MOSI M _ _ _ _ _ _ _ _ 1/CAN0 RX M0/PWM2 CH2 M0/GPIO2 A0 d _ _ _ _ _ _ | TOP IOC GPIO2A IOMUX S _ _ _ _ EL L[3:0] = 0xe _ |
| PWM2 _ CH3 M _ 0 | I/O | SDMMC0 D1/FSPI1 D1 M0/DSM AUD LN M0/SAI3 _ _ _ _ _ _ _ MCLK M3/UART0 TX M1/UART7 TX M2/I2C8 SDA _ _ _ _ _ _ _ M0/SPI0 MISO M1/CAN0 TX M0/PWM2 CH3 M0/GP _ _ _ _ _ _ IO2 A1 d _ _ | TOP IOC GPIO2A IOMUX S _ _ _ _ EL L[7:4] = 0xe _ |
| PWM2 _ CH4 M _ 0 | I/O | SDMMC0 CMD/FSPI1 CSN0 M0/SAI3 SDO M3/UAR _ _ _ _ _ T5 RX M2/I2C5 SDA M0/SPI0 CSN0 M1/PWM2 CH _ _ _ _ _ _ _ 4 M0/GPIO2 A4 d _ _ _ | TOP IOC GPIO2A IOMUX S _ _ _ _ EL H[3:0] = 0xe _ |
| PWM2 _ CH5 M _ 0 | I/O | SAI1 MCLK M0/SAI4 MCLK M0/AUPLL CLK IN M2/ _ _ _ _ _ _ _ PWM2 CH5 M0/GPIO4 A2 d _ _ _ _ | TOP IOC GPIO4A IOMUX S _ _ _ _ EL L[11:8] = 0xd _ |
| PWM2 _ CH6 M _ 0 | I/O | SAI1 SDO0 M0/SAI4 SDI M0/SPI3 CLK M2/PWM2 _ _ _ _ _ _ _ CH6 M0/GPIO4 A7 d _ _ _ | TOP IOC GPIO4A IOMUX S _ _ _ _ EL H[15:12] = 0xd _ |
| PWM2 _ CH7 M _ 0 | I/O | SAI1 SDI0 M0/SAI4 SDO M0/PDM1 SDI0 M1/SPI4 _ _ _ _ _ _ CSN0 M2/SPI3 CSN1 M2/PWM2 CH7 M0/GPIO4 B _ _ _ _ _ _ _ 3 d _ | TOP IOC GPIO4B IOMUX S _ _ _ _ EL L[15:12] = 0xd _ |
| Table 34-2 PWM M1 Interface Description |  |  |  |
| Module Pin | Dire ction | _ Pin Name | IOMUX Setting |
| PWM0 C _ H0 M1 _ | I/O | ETH1 TXD3 M1/SDMMC1 CMD M0/PDM0 SDI2 M2/ _ _ _ _ _ _ UART3 TX M2/SPI1 CSN1 M0/PWM0 CH0 M1/GPIO _ _ _ _ _ _ 1 C0 d _ _ | TOP IOC GPIO1C IOMUX S _ _ _ _ EL L[3:0] = 0xd _ |
| PWM0 C _ H1 M1 _ | I/O | DSM AUD LN M1/HDMI TX HPDIN M0/PCIE1 CLKR _ _ _ _ _ _ _ EQN M3/I2C7 SDA M3/EDP TX HPDIN M0/UART11 _ _ _ _ _ _ RX M2/PWM0 CH1 M1/GPIO4 C1 d _ _ _ _ _ _ | VCCIO6 IOC GPIO4C IOMU _ _ _ X SEL L[7:4] = 0xe _ _ |
| PWM1 C _ H0 M1 _ | I/O | ETH1 RXD2 M1/SDMMC1 D0 M0/SAI3 SCLK M1/I2 _ _ _ _ _ _ C9 SDA M1/SPI1 CLK M0/PCIE1 CLKREQN M1/PW _ _ _ _ _ _ M1 CH0 M1/GPIO1 B4 d _ _ _ _ | TOP IOC GPIO1B IOMUX S _ _ _ _ EL H[3:0] = 0xd _ |
| PWM1 C _ H1 M1 _ | I/O | ETH1 RXD3 M1/SDMMC1 D1 M0/SAI3 LRCK M1/I2 _ _ _ _ _ _ C9 SCL M1/SPI1 MOSI M0/PWM1 CH1 M1/GPIO1 _ _ _ _ _ _ _ B5 d _ | TOP IOC GPIO1B IOMUX S _ _ _ _ EL H[7:4] = 0xd _ |

## Page 1196 -- pin table

| Module Pin | Dire ction | Pin Name | IOMUX Setting |
|---|---|---|---|
| PWM1 C _ H2 M1 _ | I/O | ETH1 PPSCLK M1/SDMMC1 PWREN M0/FSPI1 RSTN _ _ _ _ _ M1/FSPI1 CSN1 M1/UART4 RTSN M1/I2C6 SCL M _ _ _ _ _ _ _ 1/SPI2 CSN1 M1/PWM1 CH2 M1/GPIO1 C2 u _ _ _ _ _ _ | TOP IOC GPIO1C IOMUX S _ _ _ _ EL L[11:8] = 0xd _ |
| PWM1 C _ H3 M1 _ | I/O | ETH1 MDC M1/SAI2 LRCK M0/I3C0 SCL M1/PWM1 _ _ _ _ _ _ CH3 M1/GPIO1 D2 d _ _ _ _ | TOP IOC GPIO1D IOMUX S _ _ _ _ EL L[11:8] = 0xd _ |
| PWM1 C _ H4 M1 _ | I/O | ETH1 MDIO M1/SAI2 SDI M0/I3C0 SDA M1/PWM1 _ _ _ _ _ _ CH4 M1/GPIO1 D3 d _ _ _ _ | TOP IOC GPIO1D IOMUX S _ _ _ _ EL L[15:12] = 0xd _ |
| PWM1 C _ H5 M1 _ | I/O | DSM AUD LP M1/SAI4 MCLK M2/HDMI TX CEC M _ _ _ _ _ _ _ _ 0/I2C7 SCL M3/SPI4 CSN1 M0/UART11 TX M2/PW _ _ _ _ _ _ M1 CH5 M1/GPIO4 C0 d _ _ _ _ | VCCIO6 IOC GPIO4C IOMU _ _ _ X SEL L[3:0] = 0xe _ _ |
| PWM2 C _ H0 M1 _ | I/O | DSM AUD RP M1/HDMI TX SCL/I2C2 SCL M3/CAN _ _ _ _ _ _ _ 0 TX M1/UART9 TX M2/PWM2 CH0 M1/GPIO4 C2 _ _ _ _ _ _ _ _ d | VCCIO6 IOC GPIO4C IOMU _ _ _ X SEL L[11:8] = 0xe _ _ |
| PWM2 C _ H1 M1 _ | I/O | DSM AUD RN M1/HDMI TX SDA/I2C2 SDA M3/CA _ _ _ _ _ _ _ N0 RX M1/UART9 RX M2/PWM2 CH1 M1/GPIO4 C _ _ _ _ _ _ _ 3 d _ | VCCIO6 IOC GPIO4C IOMU _ _ _ X SEL L[15:12] = 0xe _ _ |
| PWM2 C _ H2 M1 _ | I/O | SAI4 SDI M2/VP1 SYNC OUT/PCIE0 CLKREQN M3/ _ _ _ _ _ _ SATA0 ACTLED M1/I2C6 SCL M3/SPI4 MISO M0/C _ _ _ _ _ _ AN1 TX M1/PWM2 CH2 M1/GPIO4 C6 d _ _ _ _ _ _ | VCCIO6 IOC GPIO4C IOMU _ _ _ X SEL H[11:8] = 0xe _ _ |
| PWM2 C _ H3 M1 _ | I/O | SAI4 SCLK M2/VP2 SYNC OUT/I2C6 SDA M3/SPI4 _ _ _ _ _ _ CLK M0/CAN1 RX M1/PWM2 CH3 M1/GPIO4 C7 d _ _ _ _ _ _ _ _ | VCCIO6 IOC GPIO4C IOMU _ _ _ X SEL H[15:12] = 0xe _ _ |
| PWM2 C _ H4 M1 _ | I/O | SAI1 SCLK M0/FLEXBUS1 CSN M4/SPI3 CSN0 M2/ _ _ _ _ _ _ UART5 RTSN M1/I2C2 SCL M2/PWM2 CH4 M1/GPI _ _ _ _ _ _ O4 A3 d _ _ | TOP IOC GPIO4A IOMUX S _ _ _ _ EL L[15:12] = 0xd _ |
| PWM2 C _ H5 M1 _ | I/O | ISP FLASH TRIGOUT M1/SAI4 SDO M2/VP0 SYNC _ _ _ _ _ _ _ OUT/SATA1 ACTLED M1/I2C3 SDA M3/SPI4 MOSI _ _ _ _ _ _ M0/UART6 RX M3/PWM2 CH5 M1/GPIO4 C5 d _ _ _ _ _ _ | VCCIO6 IOC GPIO4C IOMU _ _ _ X SEL H[7:4] = 0xe _ _ |
| PWM2 C _ H6 M1 _ | I/O | ISP PRELIGHT TRIG M1/SAI4 LRCK M2/DP HPDIN _ _ _ _ _ _ _ M0/I2C3 SCL M3/SPI4 CSN0 M0/UART6 TX M3/PW _ _ _ _ _ _ M2 CH6 M1/GPIO4 C4 d _ _ _ _ | VCCIO6 IOC GPIO4C IOMU _ _ _ X SEL H[3:0] = 0xe _ _ |
| PWM2 C _ H7 M1 _ | I/O | EMMC CLK/FSPI0 CLK/SAI0 SDO3 M2/SAI0 SDI1 _ _ _ _ _ _ M2/PDM0 CLK0 M1/PWM2 CH7 M1/GPIO1 B1 d _ _ _ _ _ _ | TOP IOC GPIO1B IOMUX S _ _ _ _ EL L[7:4] = 0xc _ |
| Table 34-3 PWM M2 Interface Description |  |  |  |
| Module Pin | Direc tion | _ Pin Name | IOMUX Setting |
| PWM0 _ CH0 M2 _ | I/O | VI CIF D2/ETH1 TXD2 M0/SAI2 LRCK M1/PDM1 S _ _ _ _ _ _ _ DI3 M0/UART11 RTSN M1/SPI1 MISO M1/PWM0 C _ _ _ _ _ _ H0 M2/GPIO2 C3 d _ _ _ | TOP IOC GPIO2C IOMUX S _ _ _ _ EL L[15:12] = 0xd _ |
| PWM0 _ CH1 M2 _ | I/O | ETH1 TXD1 M0/SAI4 LRCK M3/UART4 RTSN M0/I2 _ _ _ _ _ _ C5 SDA M2/PWM0 CH1 M2/GPIO2 C7 d _ _ _ _ _ _ | TOP IOC GPIO2C IOMUX S _ _ _ _ EL H[15:12] = 0xd _ |
| PWM1 _ CH0 M2 _ | I/O | VI CIF D5/ETH1 RXD2 M0/ETH0 PTP REFCLK M1/P _ _ _ _ _ _ _ DM1 SDI1 M0/UART9 RX M0/PWM1 CH0 M2/GPIO _ _ _ _ _ _ 2 C0 d _ _ | TOP IOC GPIO2C IOMUX S _ _ _ _ EL L[3:0] = 0xd _ |

## Page 1197 -- pin table

| Module Pin | Direc tion | Pin Name | IOMUX Setting |
|---|---|---|---|
| PWM1 _ CH1 M2 _ | I/O | VI CIF D4/ETH1 RXD3 M0/ETH0 PPSCLK M1/SAI2 _ _ _ _ _ _ _ MCLK M1/PDM1 CLK1 M0/UART9 TX M0/SPI1 CSN _ _ _ _ _ _ 1 M1/PWM1 CH1 M2/GPIO2 C1 d _ _ _ _ _ | TOP IOC GPIO2C IOMUX S _ _ _ _ EL L[7:4] = 0xd _ |
| PWM1 _ CH2 M2 _ | I/O | VI CIF D3/ETH1 RXCLK M0/ETH0 PPSTRIG M1/SAI _ _ _ _ _ _ 2 SCLK M1/PDM1 SDI2 M0/UART11 CTSN M1/SPI1 _ _ _ _ _ _ MOSI M1/PWM1 CH2 M2/GPIO2 C2 d _ _ _ _ _ _ | TOP IOC GPIO2C IOMUX S _ _ _ _ EL L[11:8] = 0xd _ |
| PWM1 _ CH3 M2 _ | I/O | VI CIF D1/ETH1 TXD3 M0/SAI2 SDO M1/PDM1 SD _ _ _ _ _ _ _ I0 M0/UART11 TX M1/SPI1 CSN0 M1/PWM1 CH3 _ _ _ _ _ _ _ M2/GPIO2 C4 d _ _ | TOP IOC GPIO2C IOMUX S _ _ _ _ EL H[3:0] = 0xd _ |
| PWM1 _ CH4 M2 _ | I/O | VI CIF D0/ETH1 TXCLK M0/SAI2 SDI M1/PDM1 CL _ _ _ _ _ _ _ K0 M0/UART11 RX M1/SPI1 CLK M1/PWM1 CH4 M _ _ _ _ _ _ _ 2/GPIO2 C5 d _ _ | TOP IOC GPIO2C IOMUX S _ _ _ _ EL H[7:4] = 0xd _ |
| PWM1 _ CH5 M2 _ | I/O | ETH1 TXD0 M0/SAI4 SCLK M3/UART4 CTSN M0/I2 _ _ _ _ _ _ C5 SCL M2/PWM1 CH5 M2/GPIO2 C6 d _ _ _ _ _ _ | TOP IOC GPIO2C IOMUX S _ _ _ _ EL H[11:8] = 0xd _ |
| PWM2 _ CH0 M2 _ | I/O | ETH1 TXCTL M0/SAI4 SDI M3/UART4 TX M0/I2C6 _ _ _ _ _ _ SCL M2/PWM2 CH0 M2/GPIO2 D0 d _ _ _ _ _ _ | TOP IOC GPIO2D IOMUX S _ _ _ _ EL L[3:0] = 0xd _ |
| PWM2 _ CH1 M2 _ | I/O | ETH1 RXD0 M0/SAI4 SDO M3/UART4 RX M0/I2C6 _ _ _ _ _ _ SDA M2/PWM2 CH1 M2/GPIO2 D1 d _ _ _ _ _ _ | TOP IOC GPIO2D IOMUX S _ _ _ _ EL L[7:4] = 0xd _ |
| PWM2 _ CH2 M2 _ | I/O | CAM CLK0 OUT M1/ETH1 RXD1 M0/SAI4 MCLK M _ _ _ _ _ _ _ 3/UART6 TX M1/I3C1 SCL M0/PWM2 CH2 M2/GPI _ _ _ _ _ _ O2 D2 d _ _ | TOP IOC GPIO2D IOMUX S _ _ _ _ EL L[11:8] = 0xd _ |
| PWM2 _ CH3 M2 _ | I/O | ETH1 RXCTL M0/UART6 RX M1/I3C1 SDA M0/PWM _ _ _ _ _ _ 2 CH3 M2/GPIO2 D3 d _ _ _ _ | TOP IOC GPIO2D IOMUX S _ _ _ _ EL L[15:12] = 0xd _ |
| PWM2 _ CH4 M2 _ | I/O | ISP PRELIGHT TRIG M0/ETH1 MDC M0/UART6 RTS _ _ _ _ _ _ N M1/I2C9 SDA M2/PWM2 CH4 M2/GPIO2 D4 d _ _ _ _ _ _ _ | TOP IOC GPIO2D IOMUX S _ _ _ _ EL H[3:0] = 0xd _ |
| PWM2 _ CH5 M2 _ | I/O | ISP FLASH TRIGOUT M0/ETH1 MDIO M0/UART6 C _ _ _ _ _ _ TSN M1/I2C9 SCL M2/PWM2 CH5 M2/GPIO2 D5 d _ _ _ _ _ _ _ | TOP IOC GPIO2D IOMUX S _ _ _ _ EL H[7:4] = 0xd _ |
| PWM2 _ CH6 M2 _ | I/O | CAM CLK1 OUT M1/ETH CLK1 25M OUT M0/ETH0 _ _ _ _ _ _ _ MCLK M1/SAI3 MCLK M2/SPDIF RX0 M2/UART9 _ _ _ _ _ _ _ RTSN M0/I3C1 SDA PU M0/PWM2 CH6 M2/GPIO2 _ _ _ _ _ _ _ D6 d _ | TOP IOC GPIO2D IOMUX S _ _ _ _ EL H[11:8] = 0xd _ |
| PWM2 _ CH7 M2 _ | I/O | CAM CLK2 OUT M1/ETH1 MCLK M0/ETH CLK0 25 _ _ _ _ _ _ _ M OUT M1/SAI0 SDO3 M0/SPDIF TX0 M2/UART9 _ _ _ _ _ _ _ CTSN M0/SPI3 CSN1 M0/PWM2 CH7 M2/GPIO2 D7 _ _ _ _ _ _ d _ | TOP IOC GPIO2D IOMUX S _ _ _ _ EL H[15:12] = 0xd _ |
| Table 34-3 PWM M3 Interface Description |  |  |  |
| Module Pin | Direc tion | _ Pin Name | IOMUX Setting |
| PWM0 _ CH0 M3 _ | I/O | VO LCDC D19/VO EBC SDCE3/ETH0 MCLK M0/SAI _ _ _ _ _ _ 4 MCLK M1/DSMC CSN1/FLEXBUS0 D8/UART10 RX _ _ _ _ _ M0/SPI2 MOSI M2/PWM0 CH0 M3/GPIO3 B0 d _ _ _ _ _ _ _ | TOP IOC GPIO3B IOMUX S _ _ _ _ EL L[3:0] = 0xc _ |
| PWM0 _ CH1 M3 _ | I/O | VO LCDC D13/VO EBC SDDO13/ETH0 TXCLK M0/D _ _ _ _ _ _ SMC DQS1/FLEXBUS0 CLK/SPI3 CSN0 M1/PWM0 C _ _ _ _ _ H1 M3/GPIO3 B6 d _ _ _ | TOP IOC GPIO3B IOMUX S _ _ _ _ EL H[11:8] = 0xc _ |

## Pages 1198-1199 (stitched) -- pin table

| Module Pin | Direc tion | Pin Name | IOMUX Setting |
|---|---|---|---|
| PWM1 _ CH0 M3 _ | I/O | VO LCDC D23/VO EBC SDSHR/ETH CLK0 25M OU _ _ _ _ _ _ _ T M0/SAI4 SDI M1/DSMC RDYN/FLEXBUS1 D11/FL _ _ _ _ _ EXBUS0 CSN M0/UART1 CTSN M2/SPI2 CLK M2/P _ _ _ _ _ _ WM1 CH0 M3/GPIO3 A4 d _ _ _ _ | TOP IOC GPIO3A IOMUX S _ _ _ _ EL H[3:0] = 0xc _ |
| PWM1 _ CH1 M3 _ | I/O | VO LCDC D22/VO EBC GDSP/ETH0 MDIO M0/PDM _ _ _ _ _ _ 1 SDI3 M2/DSMC DATA15/FLEXBUS0 D7/UART1 R _ _ _ _ _ TSN M2/SPI2 CSN1 M2/PWM1 CH1 M3/GPIO3 A5 _ _ _ _ _ _ _ d | TOP IOC GPIO3A IOMUX S _ _ _ _ EL H[7:4] = 0xc _ |
| PWM1 _ CH2 M3 _ | I/O | VO LCDC D21/VO EBC GDOE/ETH0 MDC M0/PDM1 _ _ _ _ _ _ SDI2 M2/DSMC DATA14/FLEXBUS0 D6/UART1 RX _ _ _ _ _ M2/UART10 CTSN M0/PWM1 CH2 M3/GPIO3 A6 d _ _ _ _ _ _ _ | TOP IOC GPIO3A IOMUX S _ _ _ _ EL H[11:8] = 0xc _ |
| PWM1 _ CH3 M3 _ | I/O | VO LCDC D18/VO EBC SDCE2/ETH0 RXD1 M0/PD _ _ _ _ _ _ M1 CLK0 M2/DSMC DATA12/FLEXBUS0 D4/UART10 _ _ _ _ TX M0/SPI4 CSN0 M1/PWM1 CH3 M3/GPIO3 B1 _ _ _ _ _ _ _ _ d | TOP IOC GPIO3B IOMUX S _ _ _ _ EL L[7:4] = 0xc _ |
| PWM1 _ CH4 M3 _ | I/O | VO LCDC D15/VO EBC SDDO15/ETH0 TXD1 M0/SP _ _ _ _ _ _ DIF RX1 M0/DSMC DATA9/FLEXBUS0 D1/UART9 R _ _ _ _ _ TSN M1/PWM1 CH4 M3/GPIO3 B4 d _ _ _ _ _ | TOP IOC GPIO3B IOMUX S _ _ _ _ EL H[3:0] = 0xc _ |
| PWM1 _ CH5 M3 _ | I/O | VO LCDC D14/VO EBC SDDO14/ETH0 TXD0 M0/SP _ _ _ _ _ _ DIF TX1 M0/DSMC DATA8/FLEXBUS0 D0/UART9 C _ _ _ _ _ TSN M1/PWM1 CH5 M3/GPIO3 B5 d _ _ _ _ _ | TOP IOC GPIO3B IOMUX S _ _ _ _ EL H[7:4] = 0xc _ |
| PWM2 _ CH0 M3 _ | I/O | VO LCDC D9/VO EBC SDDO9/ETH0 TXD3 M0/SAI2 _ _ _ _ _ _ SCLK M2/DSMC INT1/FLEXBUS0 D9/UART11 RTS _ _ _ _ _ N M0/SPI4 MISO M1/I2C9 SCL M3/PWM2 CH0 M3 _ _ _ _ _ _ _ /GPIO3 C2 d _ _ | TOP IOC GPIO3C IOMUX S _ _ _ _ EL L[11:8] = 0xc _ |
| PWM2 _ CH1 M3 _ | I/O | VO LCDC D8/VO EBC SDDO8/ETH0 TXD2 M0/SAI2 _ _ _ _ _ _ LRCK M2/DSMC INT3/FLEXBUS0 D10/FLEXBUS0 C _ _ _ _ _ SN M2/UART11 CTSN M0/SPI4 MOSI M1/I2C9 SD _ _ _ _ _ _ A M3/PWM2 CH1 M3/GPIO3 C3 d _ _ _ _ _ | TOP IOC GPIO3C IOMUX S _ _ _ _ EL L[15:12] = 0xc _ |
| PWM2 _ CH2 M3 _ | I/O | VO LCDC D6/VO EBC SDDO6/SAI1 SDO0 M1/DSM _ _ _ _ _ _ C DATA4/FLEXBUS1 D6/UART8 RX M0/SPI1 MISO _ _ _ _ _ _ M2/PWM2 CH2 M3/GPIO3 C5 d _ _ _ _ | TOP IOC GPIO3C IOMUX S _ _ _ _ EL H[7:4] = 0xc _ |
| PWM2 _ CH3 M3 _ | I/O | VO LCDC D3/VO EBC SDDO3/SAI1 MCLK M1/DSM _ _ _ _ _ _ C DATA1/FLEXBUS1 D3/UART8 CTSN M0/SPI1 CSN _ _ _ _ _ 0 M2/PWM2 CH3 M3/GPIO3 D0 d _ _ _ _ _ | TOP IOC GPIO3D IOMUX S _ _ _ _ EL L[3:0] = 0xc _ |
| PWM2 _ CH4 M3 _ | I/O | VO LCDC D1/VO EBC SDDO1/ETH0 RXD3 M0/SAI2 _ _ _ _ _ _ SDI M2/DSMC CSN3/FLEXBUS0 D12/FLEXBUS1 D _ _ _ _ _ 15 M0/FLEXBUS0 CSN M3/UART2 RTSN M2/SPI4 _ _ _ _ _ _ CSN1 M1/I3C1 SDA M2/PWM2 CH4 M3/GPIO3 D2 _ _ _ _ _ _ _ d | TOP IOC GPIO3D IOMUX S _ _ _ _ EL L[11:8] = 0xc _ |
| PWM2 _ CH5 M3 _ | I/O | VO LCDC D0/VO EBC SDDO0/ETH0 RXD2 M0/SAI2 _ _ _ _ _ _ SDO M2/DSMC CSN0/FLEXBUS1 D2/UART2 CTSN _ _ _ _ _ M2/I3C1 SCL M2/PWM2 CH5 M3/GPIO3 D3 d _ _ _ _ _ _ _ | TOP IOC GPIO3D IOMUX S _ _ _ _ EL L[15:12] = 0xc _ |
| Module Pin | Direc tion | Pin Name | IOMUX Setting |
| PWM2 _ CH6 M3 _ | I/O | VO LCDC VSYNC/VO EBC SDCLK/SAI1 SDI3 M1/D _ _ _ _ _ _ SMC CLKN/FLEXBUS1 CLK/UART5 CTSN M0/SPI3 _ _ _ _ _ MOSI M1/PWM2 CH6 M3/GPIO3 D6 d _ _ _ _ _ | TOP IOC GPIO3D IOMUX S _ _ _ _ EL H[11:8] = 0xc _ |
| PWM2 _ CH7 M3 _ | I/O | VO LCDC CLK/VO EBC SDOE/CAM CLK0 OUT M0/ _ _ _ _ _ _ _ SAI4 SCLK M1/DSMC RESETN/FLEXBUS0 D15 M0/ _ _ _ _ _ FLEXBUS1 D12 M0/FLEXBUS1 CSN M1/UART5 RTS _ _ _ _ _ N M0/SPI3 CSN1 M1/PWM2 CH7 M3/GPIO3 D7 d _ _ _ _ _ _ _ | TOP IOC GPIO3D IOMUX S _ _ _ _ EL H[15:12] = 0xc _ |
| Notes: I=input, O=output, I/O=input/output. 34.6 Application Notes 34.6.1 PWM Capture Mode Standard Usage Flow 1. Set PWM ENABLE.pwm en to 1’b0 to disable the PWM channel. _ _ 2. Set PWM CLK CTRL.prescale/scale/clk src sel to configure the clock selection and _ _ _ _ division. 3. Set PWM CTRL.pwm mode to 2’b10 to select capture mode. _ _ 4. Set PWM INT EN.cap lpc int en/cap hpc int en to 1’b1 to enable the interrupt. _ _ _ _ _ _ _ _ 5. Set PWM ENABLE.pwm en/pwm clk en to 1’b1 to enable the channel. _ _ _ _ 6. When an interrupt is asserted, refer to PWM INTSTS register to know the raw interrupt _ status. User should read the PWM HPC register to know the effective high cycles of input _ waveforms when cap hpc intsts is asserted and read the PWM LPC register to know the _ _ _ effective low cycles when cap lpc intsts is asserted. User should set 1’b1 to correspond bit _ _ of PWM INTSTS to clear the interrupt. _ 7. If user want to disable PWM channel, set PWM ENABLE.pwm en/pwm clk en to 1’b0. _ _ _ _ 34.6.2 PWM Power key Capture Mode Standard Usage Flow 1. Set PWM ENABLE.pwm en to 1’b0 to disable the PWM channel. _ _ 2. Set PWM CLK CTRL.prescale/scale/clk src sel to configure the clock selection and _ _ _ _ division. The clock frequency should be 1 MHz after division. |  |  |  |

## Page 1259 -- pin table

| Module Pin | Direct ion | Pin Name | IOMUX Setting |
|---|---|---|---|
| DQS0 | I/O | VO LCDC D12/VO EBC SDDO12/E _ _ _ _ TH0 PPSTRIG M0/SAI1 SDI0 M1/ _ _ _ _ DSMC DQS0/FLEXBUS1 D10/FLEX _ _ BUS1 CSN M0/UART2 RX M2/UAR _ _ _ _ T3 CTSN M1/I2C4 SDA M3/GPIO3 _ _ _ _ B7 d _ _ | TOP IOC GPIO3B IOMUX SEL _ _ _ _ H[15:12]=4'h5 _ |
| DQS1 | I/O | VO LCDC D13/VO EBC SDDO13/E _ _ _ _ TH0 TXCLK M0/DSMC DQS1/FLEX _ _ _ BUS0 CLK/SPI3 CSN0 M1/PWM0 _ _ _ _ CH1 M3/GPIO3 B6 d _ _ _ | TOP IOC GPIO3B IOMUX SEL _ _ _ _ H[11:8]=4'h5 _ |
| DQ0 | I/O | VO LCDC DEN/VO EBC SDLE/SAI1 _ _ _ _ SDI1 M1/DSMC DATA0/FLEXBUS1 _ _ _ D1/UART5 RX M0/SPI3 CLK M1/I _ _ _ _ _ 2C3 SCL M2/GPIO3 D4 d _ _ _ _ | TOP IOC GPIO3D IOMUX SEL _ _ _ _ H[3:0]=4'h5 _ |
| DQ1 | I/O | VO LCDC D3/VO EBC SDDO3/S _ _ _ _ AI1 MCLK M1/DSMC DATA1/FLE _ _ _ XBUS1 D3/UART8 CTSN M0/SPI _ _ _ 1 CSN0 M2/PWM2 CH3 M3/GPI _ _ _ _ O3 D0 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ L[3:0]=4'h5 _ |
| DQ2 | I/O | _ _ VO LCDC D4/VO EBC SDDO4/S _ _ _ _ AI1 SCLK M1/DSMC DATA2/FLEX _ _ _ BUS1 D4/UART8 RTSN M0/SPI1 _ _ _ _ CLK M2/GPIO3 C7 d _ _ _ | TOP IOC GPIO3C IOMUX SEL _ _ _ _ H[15:12]=4'h5 _ |
| DQ3 | I/O | VO LCDC D5/VO EBC SDDO5/SAI _ _ _ _ 1 LRCK M1/DSMC DATA3/FLEXBU _ _ _ S1 D5/UART8 TX M0/SPI1 MOSI _ _ _ _ _ M2/GPIO3 C6 d _ _ | TOP IOC GPIO3C IOMUX SEL _ _ _ _ H[11:8]=4'h5 _ |
| DQ4 | I/O | VO LCDC D6/VO EBC SDDO6/SAI _ _ _ _ 1 SDO0 M1/DSMC DATA4/FLEXBU _ _ _ S1 D6/UART8 RX M0/SPI1 MISO _ _ _ _ _ M2/PWM2 CH2 M3/GPIO3 C5 d _ _ _ _ | TOP IOC GPIO3C IOMUX SEL _ _ _ _ H[7:4]=4'h5 _ |
| DQ5 | I/O | VO LCDC D7/VO EBC SDDO7/SAI _ _ _ _ 1 SDO1 M1/DSMC DATA5/FLEXBU _ _ _ S1 D7/UART11 TX M0/SPI2 CSN0 _ _ _ _ M2/I2C5 SCL M3/CAN0 TX M3/G _ _ _ _ _ PIO3 C4 d _ _ | TOP IOC GPIO3C IOMUX SEL _ _ _ _ H[3:0]=4'h5 _ |
| DQ6 | I/O | VO LCDC D10/VO EBC SDDO10/E _ _ _ _ TH0 PTP REFCLK M0/SAI1 SDO2 _ _ _ _ _ M1/DSMC DATA6/FLEXBUS1 D8/U _ _ ART11 RX M0/SPI2 MISO M2/I2C _ _ _ _ 5 SDA M3/CAN0 RX M3/GPIO3 C _ _ _ _ _ 1 d _ | TOP IOC GPIO3C IOMUX SEL _ _ _ _ L[7:4]=4'h5 _ |
| DQ7 | I/O | VO LCDC D11/VO EBC SDDO11/E _ _ _ _ TH0 PPSCLK M0/SAI1 SDO3 M1/D _ _ _ _ SMC DATA7/FLEXBUS1 D9/UART2 _ _ _ | TOP IOC GPIO3C IOMUX SEL _ _ _ _ L[3:0]=4'h5 _ |

## Page 1260 -- pin table

| Module Pin | Direct ion | Pin Name | IOMUX Setting |
|---|---|---|---|
|  |  | TX M2/UART3 RTSN M1/I2C4 SCL _ _ _ _ M3/GPIO3 C0 d _ _ _ |  |
| DQ8 | I/O | VO LCDC D14/VO EBC SDDO14/E _ _ _ _ TH0 TXD0 M0/SPDIF TX1 M0/DS _ _ _ _ MC DATA8/FLEXBUS0 D0/UART9 C _ _ _ TSN M1/PWM1 CH5 M3/GPIO3 B5 _ _ _ _ d _ | TOP IOC GPIO3B IOMUX SEL _ _ _ _ H[7:4]=4'h5 _ |
| DQ9 | I/O | VO LCDC D15/VO EBC SDDO15/E _ _ _ _ TH0 TXD1 M0/SPDIF RX1 M0/DS _ _ _ _ MC DATA9/FLEXBUS0 D1/UART9 R _ _ _ TSN M1/PWM1 CH4 M3/GPIO3 B4 _ _ _ _ d _ | TOP IOC GPIO3B IOMUX SEL _ _ _ _ H[3:0]=4'h5 _ |
| DQ10 | I/O | VO LCDC D16/VO EBC SDCE0/ET _ _ _ _ H0 TXCTL M0/PDM1 SDI0 M2/DS _ _ _ _ MC DATA10/FLEXBUS0 D2/UART9 _ _ _ TX M1/I2C8 SCL M3/GPIO3 B3 d _ _ _ _ _ | TOP IOC GPIO3B IOMUX SEL _ _ _ _ L[15:12]=4'h5 _ |
| DQ11 | I/O | VO LCDC D17/VO EBC SDCE1/ET _ _ _ _ H0 RXD0 M0/PDM1 SDI1 M2/DSM _ _ _ _ C DATA11/FLEXBUS0 D3/UART9 R _ _ _ X M1/I2C8 SDA M3/GPIO3 B2 d _ _ _ _ _ | TOP IOC GPIO3B IOMUX SEL _ _ _ _ L[11:8]=4'h5 _ |
| DQ12 | I/O | VO LCDC D18/VO EBC SDCE2/ET _ _ _ _ H0 RXD1 M0/PDM1 CLK0 M2/DSM _ _ _ _ C DATA12/FLEXBUS0 D4/UART10 _ _ _ TX M0/SPI4 CSN0 M1/PWM1 CH3 _ _ _ _ M3/GPIO3 B1 d _ _ _ | TOP IOC GPIO3B IOMUX SEL _ _ _ _ L[7:4]=4'h5 _ |
| DQ13 | I/O | VO LCDC D20/VO EBC VCOM/ETH _ _ _ _ 0 RXCTL M0/PDM1 CLK1 M2/DSM _ _ _ _ C DATA13/FLEXBUS0 D5/UART1 T _ _ _ X M2/UART10 RTSN M0/GPIO3 A7 _ _ _ _ d _ | TOP IOC GPIO3A IOMUX SEL _ _ _ _ H[15:12]=4'h5 _ |
| DQ14 | I/O | VO LCDC D21/VO EBC GDOE/ETH _ _ _ _ 0 MDC M0/PDM1 SDI2 M2/DSMC _ _ _ _ _ DATA14/FLEXBUS0 D6/UART1 RX _ _ _ M2/UART10 CTSN M0/PWM1 CH2 _ _ _ _ M3/GPIO3 A6 d _ _ | TOP IOC GPIO3A IOMUX SEL _ _ _ _ H[11:8]=4'h5 _ |
| DQ15 | I/O | VO LCDC D22/VO EBC GDSP/ETH _ _ _ _ 0 MDIO M0/PDM1 SDI3 M2/DSMC _ _ _ _ DATA15/FLEXBUS0 D7/UART1 RT _ _ _ SN M2/SPI2 CSN1 M2/PWM1 CH1 _ _ _ _ M3/GPIO3 A5 d _ _ _ | TOP IOC GPIO3A IOMUX SEL _ _ _ _ H[7:4]=4'h5 _ |
| INT0 | I | SPDIF RX0 M1/CAM CLK1 OUT M _ _ _ _ _ 0/SAI4 LRCK M1/DSMC INT0/FLEX _ _ _ BUS0 D13 M0/FLEXBUS1 D14 M0 _ _ _ _ /FLEXBUS1 CSN M3/UART3 TX M1 _ _ _ _ | TOP IOC GPIO4A IOMUX SEL _ _ _ _ L[3:0]=4'h5 _ |

## Page 1261 -- pin table

| Module Pin | Direct ion | Pin Name | IOMUX Setting |
|---|---|---|---|
|  |  | /SPI1 CSN1 M2/I2C7 SCL M2/MIP _ _ _ _ I TE M2/GPIO4 A0 d _ _ _ _ |  |
| INT1 | I | VO LCDC D9/VO EBC SDDO9/ETH _ _ _ _ 0 TXD3 M0/SAI2 SCLK M2/DSMC _ _ _ _ INT1/FLEXBUS0 D9/UART11 RTS _ _ _ N M0/SPI4 MISO M1/I2C9 SCL M _ _ _ _ _ 3/PWM2 CH0 M3/GPIO3 C2 d _ _ _ _ | TOP IOC GPIO3C IOMUX SEL _ _ _ _ L[11:8]=4'h5 _ |
| INT2 | I | VO POST EMPTY/SPDIF TX0 M1/C _ _ _ _ AM CLK2 OUT M0/SAI4 SDO M1/ _ _ _ _ _ DSMC INT2/FLEXBUS0 D14 M0/FL _ _ _ EXBUS1 D13 M0/FLEXBUS0 CSN _ _ _ _ M1/UART3 RX M1/I2C7 SDA M2/G _ _ _ _ PIO4 A1 d _ _ | TOP IOC GPIO4A IOMUX SEL _ _ _ _ L[7:4]=4'h5 _ |
| INT3 | I | VO LCDC D8/VO EBC SDDO8/ETH _ _ _ _ 0 TXD2 M0/SAI2 LRCK M2/DSMC _ _ _ _ INT3/FLEXBUS0 D10/FLEXBUS0 C _ _ _ SN M2/UART11 CTSN M0/SPI4 M _ _ _ _ OSI M1/I2C9 SDA M3/PWM2 CH1 _ _ _ _ M3/GPIO3 C3 d _ _ _ | TOP IOC GPIO3C IOMUX SEL _ _ _ _ L[15:12]=4'h5 _ |
| RDYN | I | VO LCDC D23/VO EBC SDSHR/ET _ _ _ _ H CLK0 25M OUT M0/SAI4 SDI _ _ _ _ _ _ M1/DSMC RDYN/FLEXBUS1 D11/FL _ _ EXBUS0 CSN M0/UART1 CTSN M2 _ _ _ _ /SPI2 CLK M2/PWM1 CH0 M3/GPI _ _ _ _ O3 A4 d _ _ | TOP IOC GPIO3A IOMUX SEL _ _ _ _ H[3:0]=4'h5 _ |
| Notes: I=input, O=output, I/O=input/output, bidirectional. 36.6 Application Notes 36.6.1 Typical Program Flow for Hyper Device 1. Configure the DSMC DEV SIZE according to the size of device applied. _ _ 2. Configure the DSMC MRGTCRx to support merge operation, and the DSMC BDRTCRx _ _ to support crossing the boundary. 3. Configure the DSMC MTRx to adjust the transfer timing. _ 4. Configure DSMC MCRx to access the slave configure register. _ 5. Set the slave configuration to be consistent with the host, such as write and read latency. 6. Configure DSMC MCRx to access the slave memory space. _ 36.6.2 Typical Program Flow for Localbus Device 1. Configure the DSMC DEV SIZE according to the size of device applied. _ _ |  |  |  |

## Page 1285 -- pin table

| Module Pin | Direction | Pin Name | IOMUX Setting |
|---|---|---|---|
| flexbus0 d1 _ | I/O | VO LCDC D15/VO EBC SDD _ _ _ _ O15/ETH0 TXD1 M0/SPDIF _ _ _ RX1 M0/DSMC DATA9/FLEXB _ _ US0 D1/UART9 RTSN M1/P _ _ _ WM1 CH4 M3/GPIO3 B4 d | TOP IOC GPIO3B IOMUX SEL _ _ _ _ H[3:0] = 4’h6 _ |
| flexbus0 d2 _ | I/O | _ _ _ _ VO LCDC D16/VO EBC SDC _ _ _ _ E0/ETH0 TXCTL M0/PDM1 S _ _ _ DI0 M2/DSMC DATA10/FLEX _ _ BUS0 D2/UART9 TX M1/I2C _ _ _ 8 SCL M3/GPIO3 B3 d | TOP IOC GPIO3B IOMUX SEL _ _ _ _ L[15:12] = 4’h6 _ |
| flexbus0 d3 _ | I/O | _ _ _ _ VO LCDC D17/VO EBC SDC _ _ _ _ E1/ETH0 RXD0 M0/PDM1 S _ _ _ DI1 M2/DSMC DATA11/FLEX _ _ BUS0 D3/UART9 RX M1/I2C _ _ _ 8 SDA M3/GPIO3 B2 d | TOP IOC GPIO3B IOMUX SEL _ _ _ _ L[11:8] = 4’h6 _ |
| flexbus0 d4 _ | I/O | _ _ _ _ VO LCDC D18/VO EBC SDC _ _ _ _ E2/ETH0 RXD1 M0/PDM1 CL _ _ _ K0 M2/DSMC DATA12/FLEXB _ _ US0 D4/UART10 TX M0/SPI _ _ _ 4 CSN0 M1/PWM1 CH3 M3/ _ _ _ _ GPIO3 B1 d | TOP IOC GPIO3B IOMUX SEL _ _ _ _ H[7:4] = 4’h6 _ |
| flexbus0 d5 _ | I/O | _ _ VO LCDC D20/VO EBC VCO _ _ _ _ M/ETH0 RXCTL M0/PDM1 CL _ _ _ K1 M2/DSMC DATA13/FLEXB _ _ US0 D5/UART1 TX M2/UART _ _ _ 10 RTSN M0/GPIO3 A7 d | TOP IOC GPIO3A IOMUX SEL _ _ _ _ H[15:12] = 4’h6 _ |
| flexbus0 d6 _ | I/O | _ _ _ _ VO LCDC D21/VO EBC GDO _ _ _ _ E/ETH0 MDC M0/PDM1 SDI _ _ _ 2 M2/DSMC DATA14/FLEXBU _ _ S0 D6/UART1 RX M2/UART1 _ _ _ 0 CTSN M0/PWM1 CH2 M3/ _ _ _ _ GPIO3 A6 d | TOP IOC GPIO3A IOMUX SEL _ _ _ _ H[11:8] = 4’h6 _ |
| flexbus0 d7 _ | I/O | _ _ VO LCDC D22/VO EBC GDS _ _ _ _ P/ETH0 MDIO M0/PDM1 SDI _ _ _ 3 M2/DSMC DATA15/FLEXBU _ _ S0 D7/UART1 RTSN M2/SPI _ _ _ 2 CSN1 M2/PWM1 CH1 M3/ _ _ _ _ GPIO3 A5 d | TOP IOC GPIO3A IOMUX SEL _ _ _ _ H[7:4] = 4’h6 _ |
| flexbus0 d8 _ | I/O | _ _ VO LCDC D19/VO EBC SDC _ _ _ _ E3/ETH0 MCLK M0/SAI4 MC _ _ _ LK M1/DSMC CSN1/FLEXBUS _ _ 0 D8/UART10 RX M0/SPI2 _ _ _ _ MOSI M2/PWM0 CH0 M3/GP _ _ _ IO3 B0 d | TOP IOC GPIO3B IOMUX SEL _ _ _ _ L[3:0] = 4’h6 _ |
| flexbus0 d9 _ | I/O | _ _ VO LCDC D9/VO EBC SDDO _ _ _ _ 9/ETH0 TXD3 M0/SAI2 SCL _ _ _ K M2/DSMC INT1/FLEXBUS0 _ _ D9/UART11 RTSN M0/SPI4 _ _ _ MISO M1/I2C9 SCL M3/PW _ _ _ _ M2 CH0 M3/GPIO3 C2 d | TOP IOC GPIO3C IOMUX SEL _ _ _ _ L[11:8] = 4’h6 _ |
| flexbus0 d10 _ | I/O | _ _ _ _ VO LCDC D8/VO EBC SDDO _ _ _ _ 8/ETH0 TXD2 M0/SAI2 LRC _ _ _ K M2/DSMC INT3/FLEXBUS0 _ _ D10/FLEXBUS0 CSN M2/UA _ _ _ RT11 CTSN M0/SPI4 MOSI _ _ _ _ M1/I2C9 SDA M3/PWM2 CH | TOP IOC GPIO3C IOMUX SEL _ _ _ _ L[15:12] = 4’h6 _ |

## Page 1286 -- pin table

| Module Pin | Direction | Pin Name | IOMUX Setting |
|---|---|---|---|
|  |  | 1 M3/GPIO3 C3 d |  |
| flexbus0 d11 _ | I/O | _ _ _ VO LCDC D2/VO EBC SDDO _ _ _ _ 2/ETH0 RXCLK M0/SAI2 MC _ _ _ LK M2/DSMC CSN2/FLEXBUS _ _ 0 D11/FLEXBUS1 CSN M2/S _ _ _ PI4 CLK M1/I3C1 SDA PU _ _ _ _ _ M2/GPIO3 D1 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ L[7:4] = 4’h6 _ |
| flexbus0 d12 _ | I/O | _ _ VO LCDC D1/VO EBC SDDO _ _ _ _ 1/ETH0 RXD3 M0/SAI2 SDI _ _ _ M2/DSMC CSN3/FLEXBUS0 _ _ D12/FLEXBUS1 D15 M0/FL _ _ _ EXBUS0 CSN M3/UART2 RT _ _ _ SN M2/SPI4 CSN1 M1/I3C1 _ _ _ SDA M2/PWM2 CH4 M3/GP _ _ _ _ IO3 D2 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ L[11:8] = 4’h6 _ |
| flexbus0 d13 _ m0 _ | I/O | _ _ SPDIF RX0 M1/CAM CLK1 O _ _ _ _ UT M0/SAI4 LRCK M1/DSMC _ _ _ INT0/FLEXBUS0 D13 M0/FL _ _ _ EXBUS1 D14 M0/FLEXBUS1 _ _ _ CSN M3/UART3 TX M1/SPI1 _ _ _ CSN1 M2/I2C7 SCL M2/MI _ _ _ _ PI TE M2/GPIO4 A0 d | TOP IOC GPIO4A IOMUX SEL _ _ _ _ L[3:0] = 4’h6 _ |
| flexbus0 d13 _ m1 _ | I/O | _ _ _ _ SAI4 SCLK M0/PDM1 SDI3 _ _ _ _ M1/FLEXBUS0 D13 M1/SPI3 _ _ MOSI M2/UART6 TX M0/I2 _ _ _ _ C4 SCL M1/CAN0 TX M2/GP _ _ _ _ IO4 A4 d | TOP IOC GPIO4A IOMUX SEL _ _ _ _ H[3:0] = 4’h4 _ |
| flexbus0 d14 _ m0 _ | I/O | _ _ VO POST EMPTY/SPDIF TX0 _ _ _ M1/CAM CLK2 OUT M0/SAI _ _ _ _ 4 SDO M1/DSMC INT2/FLEX _ _ _ BUS0 D14 M0/FLEXBUS1 D1 _ _ _ 3 M0/FLEXBUS0 CSN M1/UA _ _ _ RT3 RX M1/I2C7 SDA M2/G _ _ _ _ PIO4 A1 d | TOP IOC GPIO4A IOMUX SEL _ _ _ _ L[7:4] = 4’h6 _ |
| flexbus0 d14 _ m1 _ | I/O | _ _ SAI4 LRCK M0/PDM1 CLK0 _ _ _ _ M1/FLEXBUS0 D14 M1/SPI3 _ _ MISO M2/UART6 RX M0/I2 _ _ _ _ C4 SDA M1/CAN0 RX M2/G _ _ _ _ PIO4 A6 d | TOP IOC GPIO4A IOMUX SEL _ _ _ _ H[11:8] = 4’h4 _ |
| flexbus0 d15 _ m0 _ | I/O | _ _ VO LCDC CLK/VO EBC SDO _ _ _ _ E/CAM CLK0 OUT M0/SAI4 _ _ _ _ SCLK M1/DSMC RESETN/FLE _ _ XBUS0 D15 M0/FLEXBUS1 _ _ _ D12 M0/FLEXBUS1 CSN M1/ _ _ _ UART5 RTSN M0/SPI3 CSN1 _ _ _ M1/PWM2 CH7 M3/GPIO3 _ _ _ _ D7 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ H[15:12] = 4’h6 _ |
| flexbus0 d15 _ m1 _ | I/O | _ SPDIF TX0 M0/FLEXBUS0 D _ _ _ 15 M1/UART2 TX M1/I2C3 _ _ _ _ SCL M0/PCIE0 CLKREQN M2 _ _ _ /CAN1 TX M2/GPIO4 B5 d | TOP IOC GPIO4B IOMUX SEL _ _ _ _ H[7:4] = 4’h4 _ |
| flexbus1 clk _ | I/O | _ _ _ _ VO LCDC VSYNC/VO EBC S _ _ _ _ DCLK/SAI1 SDI3 M1/DSMC _ _ _ CLKN/FLEXBUS1 CLK/UART5 _ CTSN M0/SPI3 MOSI M1/P _ _ _ _ WM2 CH6 M3/GPIO3 D6 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ H[11:8] = 4’h6 _ |

## Page 1287 -- pin table

| Module Pin | Direction | Pin Name | IOMUX Setting |
|---|---|---|---|
| flexbus1 csn _ m0 _ | O | VO LCDC D12/VO EBC SDD _ _ _ _ O12/ETH0 PPSTRIG M0/SAI1 _ _ SDI0 M1/DSMC DQS0/FLEX _ _ _ BUS1 D10/FLEXBUS1 CSN _ _ _ M0/UART2 RX M2/UART3 CT _ _ _ SN M1/I2C4 SDA M3/GPIO3 _ _ _ B7 d | TOP IOC GPIO3B IOMUX SEL _ _ _ _ H[15:12] = 4’h8 _ |
| flexbus1 csn _ m1 _ | O | _ _ VO LCDC CLK/VO EBC SDO _ _ _ _ E/CAM CLK0 OUT M0/SAI4 _ _ _ _ SCLK M1/DSMC RESETN/FLE _ _ XBUS0 D15 M0/FLEXBUS1 _ _ _ D12 M0/FLEXBUS1 CSN M1/ _ _ _ UART5 RTSN M0/SPI3 CSN1 _ _ _ M1/PWM2 CH7 M3/GPIO3 _ _ _ _ D7 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ H[15:12] = 4’h8 _ |
| flexbus1 csn _ m2 _ | O | _ VO LCDC D2/VO EBC SDDO _ _ _ _ 2/ETH0 RXCLK M0/SAI2 MC _ _ _ LK M2/DSMC CSN2/FLEXBUS _ _ 0 D11/FLEXBUS1 CSN M2/S _ _ _ PI4 CLK M1/I3C1 SDA PU _ _ _ _ _ M2/GPIO3 D1 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ L[7:4] = 4’h8 _ |
| flexbus1 csn _ m3 _ | O | _ _ SPDIF RX0 M1/CAM CLK1 O _ _ _ _ UT M0/SAI4 LRCK M1/DSMC _ _ _ INT0/FLEXBUS0 D13 M0/FL _ _ _ EXBUS1 D14 M0/FLEXBUS1 _ _ _ CSN M3/UART3 TX M1/SPI1 _ _ _ CSN1 M2/I2C7 SCL M2/MI _ _ _ _ PI TE M2/GPIO4 A0 d | TOP IOC GPIO4A IOMUX SEL _ _ _ _ L[3:0] = 4’h8 _ |
| flexbus1 csn _ m4 _ | O | _ _ _ _ SAI1 SCLK M0/FLEXBUS1 C _ _ _ SN M4/SPI3 CSN0 M2/UART _ _ _ 5 RTSN M1/I2C2 SCL M2/P _ _ _ _ WM2 CH4 M1/GPIO4 A3 d | TOP IOC GPIO4A IOMUX SEL _ _ _ _ L[15:12] =4’h4 _ |
| flexbus1 d0 _ | I | _ _ _ _ VO LCDC HSYNC/VO EBC G _ _ _ _ DCLK/SAI1 SDI2 M1/DSMC _ _ _ CLKP/FLEXBUS1 D0/UART5 _ _ TX M0/SPI3 MISO M1/I2C3 _ _ _ _ SDA M2/GPIO3 D5 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ H[7:4] = 4’h6 _ |
| flexbus1 d1 _ | I | _ _ _ VO LCDC DEN/VO EBC SDL _ _ _ _ E/SAI1 SDI1 M1/DSMC DAT _ _ _ A0/FLEXBUS1 D1/UART5 RX _ _ M0/SPI3 CLK M1/I2C3 SCL _ _ _ _ M2/GPIO3 D4 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ H[3:0] = 4’h6 _ |
| flexbus1 d2 _ | I | _ _ _ VO LCDC D0/VO EBC SDDO _ _ _ _ 0/ETH0 RXD2 M0/SAI2 SDO _ _ _ M2/DSMC CSN0/FLEXBUS1 _ _ D2/UART2 CTSN M2/I3C1 _ _ _ _ SCL M2/PWM2 CH5 M3/GPI _ _ _ O3 D3 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ L[15:12] = 4’h6 _ |
| flexbus1 d3 _ | I | _ _ VO LCDC D3/VO EBC SDDO _ _ _ _ 3/SAI1 MCLK M1/DSMC DAT _ _ _ A1/FLEXBUS1 D3/UART8 CT _ _ SN M0/SPI1 CSN0 M2/PWM _ _ _ 2 CH3 M3/GPIO3 D0 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ L[3:0] = 4’h6 _ |
| flexbus1 d4 _ | I | _ _ _ _ VO LCDC D4/VO EBC SDDO _ _ _ _ 4/SAI1 SCLK M1/DSMC DAT _ _ _ A2/FLEXBUS1 D4/UART8 RT | TOP IOC GPIO3C IOMUX SEL _ _ _ _ H[15:12] = 4’h6 _ |

## Page 1288 -- pin table

| Module Pin | Direction | Pin Name | IOMUX Setting |
|---|---|---|---|
|  |  | SN M0/SPI1 CLK M2/GPIO3 _ _ _ C7 d |  |
| flexbus1 d5 _ | I | _ _ VO LCDC D5/VO EBC SDDO _ _ _ _ 5/SAI1 LRCK M1/DSMC DAT _ _ _ A3/FLEXBUS1 D5/UART8 TX _ _ M0/SPI1 MOSI M2/GPIO3 _ _ _ _ C6 d | TOP IOC GPIO3C IOMUX SEL _ _ _ _ H[11:8] = 4’h6 _ |
| flexbus1 d6 _ | I | _ VO LCDC D6/VO EBC SDDO _ _ _ _ 6/SAI1 SDO0 M1/DSMC DAT _ _ _ A4/FLEXBUS1 D6/UART8 RX _ _ M0/SPI1 MISO M2/PWM2 _ _ _ _ CH2 M3/GPIO3 C5 d | TOP IOC GPIO3C IOMUX SEL _ _ _ _ H[7:4] = 4’h6 _ |
| flexbus1 d7 _ | I | _ _ _ VO LCDC D7/VO EBC SDDO _ _ _ _ 7/SAI1 SDO1 M1/DSMC DAT _ _ _ A5/FLEXBUS1 D7/UART11 T _ _ X M0/SPI2 CSN0 M2/I2C5 _ _ _ _ SCL M3/CAN0 TX M3/GPIO3 _ _ _ C4 d | TOP IOC GPIO3C IOMUX SEL _ _ _ _ H[3:0] = 4’h6 _ |
| flexbus1 d8 _ | I | _ _ VO LCDC D10/VO EBC SDD _ _ _ _ O10/ETH0 PTP REFCLK M0/ _ _ _ SAI1 SDO2 M1/DSMC DATA _ _ _ 6/FLEXBUS1 D8/UART11 RX _ _ M0/SPI2 MISO M2/I2C5 S _ _ _ _ DA M3/CAN0 RX M3/GPIO3 _ _ _ C1 d | TOP IOC GPIO3C IOMUX SEL _ _ _ _ L[7:4] = 4’h6 _ |
| flexbus1 d9 _ | I | _ _ VO LCDC D11/VO EBC SDD _ _ _ _ O11/ETH0 PPSCLK M0/SAI1 _ _ SDO3 M1/DSMC DATA7/FLE _ _ _ XBUS1 D9/UART2 TX M2/UA _ _ _ RT3 RTSN M1/I2C4 SCL M3 _ _ _ _ /GPIO3 C0 d | TOP IOC GPIO3C IOMUX SEL _ _ _ _ L[3:0] = 4’h6 _ |
| flexbus1 d10 _ | I | _ _ VO LCDC D12/VO EBC SDD _ _ _ _ O12/ETH0 PPSTRIG M0/SAI1 _ _ SDI0 M1/DSMC DQS0/FLEX _ _ _ BUS1 D10/FLEXBUS1 CSN _ _ _ M0/UART2 RX M2/UART3 CT _ _ _ SN M1/I2C4 SDA M3/GPIO3 _ _ _ B7 d | TOP IOC GPIO3B IOMUX SEL _ _ _ _ H[15:12] = 4’h6 _ |
| flexbus1 d11 _ | I | _ _ VO LCDC D23/VO EBC SDS _ _ _ _ HR/ETH CLK0 25M OUT M0/ _ _ _ _ SAI4 SDI M1/DSMC RDYN/F _ _ _ LEXBUS1 D11/FLEXBUS0 CS _ _ N M0/UART1 CTSN M2/SPI2 _ _ _ CLK M2/PWM1 CH0 M3/GP _ _ _ _ IO3 A4 d | TOP IOC GPIO3A IOMUX SEL _ _ _ _ H[3:0] = 4’h6 _ |
| flexbus1 d12 _ m0 _ | I | _ _ VO LCDC CLK/VO EBC SDO _ _ _ _ E/CAM CLK0 OUT M0/SAI4 _ _ _ _ SCLK M1/DSMC RESETN/FLE _ _ XBUS0 D15 M0/FLEXBUS1 _ _ _ D12 M0/FLEXBUS1 CSN M1/ _ _ _ UART5 RTSN M0/SPI3 CSN1 _ _ _ M1/PWM2 CH7 M3/GPIO3 _ _ _ _ D7 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ H[15:12] = 4’h7 _ |
| flexbus1 d12 _ m1 _ | I | _ SAI1 LRCK M0/FLEXBUS1 D _ _ _ 12 M1/SPI4 CSN1 M2/UART _ _ _ 5 CTSN M1/I2C2 SDA M2/P | TOP IOC GPIO4A IOMUX SEL _ _ _ _ H[7:4] = 4’h4 _ |

## Page 1289 -- pin table

| Module Pin | Direction | Pin Name | IOMUX Setting |
|---|---|---|---|
|  |  | CIE1 CLKREQN M2/GPIO4 A _ _ _ 5 d |  |
| flexbus1 d13 _ m0 _ | I | _ VO POST EMPTY/SPDIF TX0 _ _ _ M1/CAM CLK2 OUT M0/SAI _ _ _ _ 4 SDO M1/DSMC INT2/FLEX _ _ _ BUS0 D14 M0/FLEXBUS1 D1 _ _ _ 3 M0/FLEXBUS0 CSN M1/UA _ _ _ RT3 RX M1/I2C7 SDA M2/G _ _ _ _ PIO4 A1 d | TOP IOC GPIO4A IOMUX SEL _ _ _ _ L[7:4] = 4’h7 _ |
| flexbus1 d13 _ m1 _ | I | _ _ SAI1 SDO1 M0/SAI1 SDI3 _ _ _ _ M0/PDM1 CLK1 M1/FLEXBUS _ _ 1 D13 M1/SPI4 CLK M2/UA _ _ _ _ RT5 TX M1/UART6 RTSN M0 _ _ _ _ /UART2 RTSN M1/GPIO4 B0 _ _ _ d | TOP IOC GPIO4B IOMUX SEL _ _ _ _ L[3:0] = 4’h4 _ |
| flexbus1 d14 _ m0 _ | I | _ SPDIF RX0 M1/CAM CLK1 O _ _ _ _ UT M0/SAI4 LRCK M1/DSMC _ _ _ INT0/FLEXBUS0 D13 M0/FL _ _ _ EXBUS1 D14 M0/FLEXBUS1 _ _ _ CSN M3/UART3 TX M1/SPI1 _ _ _ CSN1 M2/I2C7 SCL M2/MI _ _ _ _ PI TE M2/GPIO4 A0 d | TOP IOC GPIO4A IOMUX SEL _ _ _ _ L[3:0] = 4’h7 _ |
| flexbus1 d14 _ m1 _ | I | _ _ _ _ SAI1 SDO2 M0/SAI1 SDI2 _ _ _ _ M0/PDM1 SDI2 M1/FLEXBUS _ _ 1 D14 M1/SPI4 MOSI M2/U _ _ _ _ ART5 RX M1/UART6 CTSN _ _ _ _ M0/UART2 CTSN M1/GPIO4 _ _ _ B1 d | TOP IOC GPIO4B IOMUX SEL _ _ _ _ L[7:4] = 4’h4 _ |
| flexbus1 d15 _ -m0 | I | _ VO LCDC D1/VO EBC SDDO _ _ _ _ 1/ETH0 RXD3 M0/SAI2 SDI _ _ _ M2/DSMC CSN3/FLEXBUS0 _ _ D12/FLEXBUS1 D15 M0/FL _ _ _ EXBUS0 CSN M3/UART2 RT _ _ _ SN M2/SPI4 CSN1 M1/I3C1 _ _ _ SDA M2/PWM2 CH4 M3/GP _ _ _ _ IO3 D2 d | TOP IOC GPIO3D IOMUX SEL _ _ _ _ L[11:8] = 4’h7 _ |
| flexbus1 d15 _ -m1 | I | _ _ SAI1 SDO3 M0/SAI1 SDI1 _ _ _ _ M0/PDM1 SDI1 M1/FLEXBUS _ _ 1 D15 M1/SPI4 MISO M2/M _ _ _ _ IPI TE M0/GPIO4 B2 d | TOP IOC GPIO4B IOMUX SEL _ _ _ _ L[11:8] = 4’h4 _ |
| _ _ _ _ Notes: I=input, O=output, I/O=input/output, bidirectional. 37.6 Application Notes Clock Ratios The frequency of PAD is half of FlexBUS operation clock.When FlexBUS operation clock is |  |  |  |

## Page 1350 -- pin table

| Module Pin | Dir | PAD Name | IOMUX Setting |
|---|---|---|---|
| emmc cclk _ | O | EMMC CLK/FSPI0 CLK/SAI0 SDO3 M2/SAI0 SDI1 _ _ _ _ _ M2/PDM0 CLK0 M1/PWM2 CH7 M1/GPIO1 B1 d | TOP IOC GPIO1B IOMUX SEL L[7:4] _ _ _ _ _ =4’h1 |
| emmc ccmd _ | I/O | _ _ _ _ _ _ _ EMMC CMD/FSPI0 RSTN/FSPI0 CSN1/UART6 TX _ _ _ _ _ M2/I2C7 SCL M0/GPIO1 B0 u | TOP IOC GPIO1B IOMUX SEL L[3:0] _ _ _ _ _ =4’h1 |
| emmc cdata0 _ | I/O | _ _ _ _ EMMC D0/FSPI0 D0/SAI0 SCLK M2/UART7 RTSN _ _ _ _ _ M1/I2C2 SCL M1/GPIO1 A0 u | TOP IOC GPIO1A IOMUX SEL L[3:0] _ _ _ _ _ =4’h1 |
| emmc cdata1 _ | I/O | _ _ _ _ _ EMMC D1/FSPI0 D1/SAI0 LRCK M2/UART7 CTSN _ _ _ _ _ M1/I2C2 SDA M1/GPIO1 A1 u | TOP IOC GPIO1A IOMUX SEL L[7:4] _ _ _ _ _ =4’h1 |
| emmc cdata2 _ | I/O | _ _ _ _ _ EMMC D2/FSPI0 D2/SAI0 SDO1 M2/SAI0 SDI3 _ _ _ _ _ _ M2/PDM0 SDI3 M1/UART7 TX M1/UART6 RTSN _ _ _ _ _ _ M2/GPIO1 A2 u | TOP IOC GPIO1A IOMUX SEL L[11:8] _ _ _ _ _ =4’h1 |
| emmc cdata3 _ | I/O | _ _ EMMC D3/FSPI0 D3/SAI0 SDO2 M2/SAI0 SDI2 _ _ _ _ _ _ M2/PDM0 SDI1 M1/UART7 RX M1/UART6 CTSN _ _ _ _ _ _ M2/GPIO1 A3 u | TOP IOC GPIO1A IOMUX SEL L[15:12] _ _ _ _ _ =4’h1 |
| emmc cdata4 _ | I/O | _ _ EMMC D4/SAI0 MCLK M2/SAI3 MCLK M0/SPI0 C _ _ _ _ _ _ SN0 M2/GPIO1 A4 u | TOP IOC GPIO1A IOMUX SEL H[3:0] _ _ _ _ _ =4’h1 |
| emmc cdata5 _ | I/O | _ _ _ EMMC D5/SAI3 SCLK M0/PDM0 SDI2 M1/SPI0 M _ _ _ _ _ _ OSI M2/I2C9 SCL M0/GPIO1 A5 u | TOP IOC GPIO1A IOMUX SEL H[7:4] _ _ _ _ _ =4’h1 |
| emmc cdata6 _ | I/O | _ _ _ _ _ EMMC D6/SAI3 LRCK M0/PDM0 CLK1 M1/SPI0 M _ _ _ _ _ _ ISO M2/I2C9 SDA M0/GPIO1 A6 u | TOP IOC GPIO1A IOMUX SEL H[11:8] _ _ _ _ _ =4’h1 |
| emmc cdata7 _ | I/O | _ _ _ _ _ EMMC D7/SAI0 SDO0 M2/SAI3 SDI M0/SPI0 CL _ _ _ _ _ _ K M2/GPIO1 A7 u | TOP IOC GPIO1A IOMUX SEL H[15:12] _ _ _ _ _ =4’h1 |
| emmc strbin _ | I | _ _ _ EMMC STRB/SAI0 SDI0 M2/SAI3 SDO M0/PDM0 _ _ _ _ _ SDI0 M1/SPI0 CSN1 M2/GPIO1 B2 d _ _ _ _ _ _ | EMMC STRB/SAI0 SDI0 M2/SAI3 SDO _ _ _ _ _ M0/PDM0 SDI0 M1/SPI0 CSN1 M2/GPI _ _ _ _ O1 B2 d |
| emmc rstn _ | O | EMMC RSTN/FSPI0 CSN0/UART6 RX M2/I2C7 SD _ _ _ _ _ A M0/MIPI TE M3/PWM2 CH1 M0/GPIO1 B3 u | _ _ TOP IOC GPIO1B IOMUX SEL L[15:12] _ _ _ _ _ =4’h1 |

## Pages 1364-1365 (stitched) -- spec/parameter table

| transferred from the card; the end bit of the stop command may not exactly match the end bit of the last data block. If the requested block size for data transfers to cards is less than 4, 16, or 32 bytes for 1- bit, 4-bit, or 8-bit data transfer modes, respectively, the data-transmit state machine terminates the data transfer when all data is transferred, at which point the internally- generated stop command is loaded in the command path. Data received from the card after that are then ignored by the data path. If the byte count is 0—the block size must be greater than 0—it is an open-ended block _ transfer. For this type of data transfer, the data-receive state machine continues the block- read data transfer until the host software issues a stop or abort command. Auto-Stop The Host Controller internally generates a stop command and is loaded in the command path when the send auto stop bit is set in the SDMMC CMD register. _ _ _ The software should set the send auto stop bit according to details listed in following _ _ table. Table 39-2 Auto-Stop Generation |  |  |  |  |
|---|---|---|---|---|
| Card type | Transfer type | Byte Count | send auto stop _ _ bit set | Comments |
| MMC | Stream read | 0 | No | Open-ended stream |
| MMC | Stream read | >0 | Yes | Auto-stop after all bytes transfer |
| MMC | Stream write | 0 | No | Open-ended stream |
| MMC | Stream write | >0 | Yes | Auto-stop after all bytes transfer |
| MMC | Single-block read | >0 | No | Byte count =0 is illegal |
| MMC | Single-block write | >0 | No | Byte count =0 is illegal |
| MMC | Multiple-block read | 0 | No | Open-ended multiple block |
| MMC | Multiple-block read | >0 | Yes○1 | Pre-defined multiple block |
| MMC | Multiple-block write | 0 | No | Open-ended multiple block |
| MMC | Multiple-block write | >0 | Yes○1 | Pre-defined multiple block |
| SDMEM | Single-block read | >0 | No | Byte count =0 is illegal |
| SDMEM | Single-block write | >0 | No | Byte count =0 illegal |
| SDMEM | Multiple-block read | 0 | No | Open-ended multiple block |
| SDMEM | Multiple-block read | >0 | Yes | Auto-stop after all bytes transfer |
| SDMEM | Multiple-block write | 0 | No | Open-ended multiple block |
| SDMEM | Multiple-block write | >0 | Yes | Auto-stop after all bytes transfer |
| SDIO | Single-block read | >0 | No | Byte count =0 is illegal |
| SDIO | Single-block write | >0 | No | Byte count =0 illegal |
| SDIO | Multiple-block | 0 | No | Open-ended multiple block |
| Card type | Transfer type | Byte Count | send auto stop _ _ bit set | Comments |
|  | read |  |  |  |
| SDIO | Multiple-block read | >0 | No | Pre-defined multiple block |
| SDIO | Multiple-block write | 0 | No | Open-ended multiple block |
| SDIO | Multiple-block write | >0 | No | Pre-defined multiple block |

## Page 1373 -- pin table

| Fig. 39-9 Clock Generation Unit 39.4 Register Description 39.4.1 Internal Address Mapping Slave address can be divided into different length for different usage, which is shown as follows. Operational Base Name Base Address SDMMC 0x2A310000 SDIO 0x2A320000 39.4.2 Registers Summary |  |  |  |  |
|---|---|---|---|---|
| Name | Offset | Size | Reset Value | Description |
| SDMMC CTRL | 0x0000 | W | 0x00000000 | Control register |
| _ SDMMC PWREN | 0x0004 | W | 0x00000000 | Power enable register |
| _ SDMMC CLKDIV | 0x0008 | W | 0x00000000 | Clock divider register |
| _ SDMMC CLKSRC | 0x000C | W | 0x00000000 | SD clock source register |
| _ SDMMC CLKENA | 0x0010 | W | 0x00000000 | Clock enable register |
| _ SDMMC TMOUT | 0x0014 | W | 0xFFFFFF40 | Timeout register |
| _ SDMMC CTYPE | 0x0018 | W | 0x00000000 | Card type register |
| _ SDMMC BLKSIZ | 0x001C | W | 0x00000200 | Block size register |
| _ SDMMC BYTCNT | 0x0020 | W | 0x00000200 | Byte count register |
| _ SDMMC INTMASK | 0x0024 | W | 0x00000000 | Interrupt mask register |

## Page 1395 -- pin table

| Module Pin | Dir. | PAD Name | IOMUX Setting |
|---|---|---|---|
| sdmmc cclk _ | O | SDMMC0 CLK/FSPI1 CLK M0/SAI3 SCLK M3/TEST _ _ _ _ _ _ CLK OUT/UART5 TX M2/I2C5 SCL M0/SPI0 CLK M _ _ _ _ _ _ _ 1/I3C1 SDA PU M1/GPIO2 A5 d | TOP IOC GPIO2A IOMUX SEL H[7:4] _ _ _ _ _ =4’h1 |
| sdmmc ccmd _ | I/O | _ _ _ _ _ SDMMC0 CMD/FSPI1 CSN0 M0/SAI3 SDO M3/UAR _ _ _ _ _ T5 RX M2/I2C5 SDA M0/SPI0 CSN0 M1/PWM2 CH _ _ _ _ _ _ _ 4 M0/GPIO2 A4 d | TOP IOC GPIO2A IOMUX SEL H[3:0] _ _ _ _ _ =4’h1 |
| sdmmc cdata0 _ | I/O | _ _ _ SDMMC0 D0/FSPI1 D0 M0/DSM AUD LP M0/UART _ _ _ _ _ _ 0 RX M1/UART7 RX M2/I2C8 SCL M0/SPI0 MOSI _ _ _ _ _ _ _ _ M1/CAN0 RX M0/PWM2 CH2 M0/GPIO2 A0 d | TOP IOC GPIO2A IOMUX SEL L[3:0] _ _ _ _ _ =4’h1 |
| sdmmc cdata1 _ | I/O | _ _ _ _ _ _ SDMMC0 D1/FSPI1 D1 M0/DSM AUD LN M0/SAI3 _ _ _ _ _ _ _ MCLK M3/UART0 TX M1/UART7 TX M2/I2C8 SDA _ _ _ _ _ _ _ M0/SPI0 MISO M1/CAN0 TX M0/PWM2 CH3 M0/G _ _ _ _ _ _ PIO2 A1 d | TOP IOC GPIO2A IOMUX SEL L[7:4] _ _ _ _ _ =4’h1 |
| sdmmc cdata2 _ | I/O | _ _ SDMMC0 D2/FSPI1 D2 M0/DSM AUD RP M0/SAI3 _ _ _ _ _ _ _ LRCK M3/JTAG TCK M0/UART5 RTSN M2/SPI0 CS _ _ _ _ _ _ N1 M1/CAN1 RX M0/I3C1 SCL M1/GPIO2 A2 d | TOP IOC GPIO2A IOMUX SEL L[11:8] _ _ _ _ _ =4’h1 |
| sdmmc cdata3 _ | I/O | _ _ _ _ _ _ _ SDMMC0 D3/FSPI1 D3 M0/DSM AUD RN M0/SAI3 _ _ _ _ _ _ SDI M3/JTAG TMS M0/UART5 CTSN M2/CAN1 TX _ _ _ _ _ _ _ M0/I3C1 SDA M1/GPIO2 A3 d | TOP IOC GPIO2A IOMUX SEL L[15:12] _ _ _ _ _ =4’h1 |
| sdmmc cdetn _ | I | _ _ _ _ _ SDMMC0 DETN/SPI2 CSN1 M0/GPIO0 A7 u _ _ _ _ _ | PMU0 IOC GPIO0A IOMUX SEL H[15:1 _ _ _ _ _ 2]=4’h1 |
| sdmmc pwren _ | O | SDMMC0 PWREN/SDMMC1 DETN M2/HDMI TX HPD _ _ _ _ _ IN M1/EDP TX HPDIN M1/PWM1 CH2 M0/GPIO0 B _ _ _ _ _ _ _ 6 d | PMU1 IOC GPIO0B IOMUX SEL H[11:8] _ _ _ _ _ =4’h1 |

## Pages 1395-1396 (stitched) -- pin table

| Module Pin | Dir. | PAD Name | IOMUX Setting |
|---|---|---|---|
| sdio cclk _ | O | ETH1 TXCLK M1/SDMMC1 CLK M0/SAI3 MCLK M1/PD _ _ _ _ _ _ M0 CLK0 M2/UART3 RX M2/GPIO1 C1 d _ _ _ _ _ _ | TOP IOC GPIO1C IOMUX SEL L[7:4 _ _ _ _ _ ] =4’h2 |
| sdio ccmd _ | I/O | ETH1 TXD3 M1/SDMMC1 CMD M0/PDM0 SDI2 M2/UA _ _ _ _ _ _ RT3 TX M2/SPI1 CSN1 M0/PWM0 CH0 M1/GPIO1 C0 _ _ _ _ _ _ _ _ d | TOP IOC GPIO1C IOMUX SEL L[3:0 _ _ _ _ _ ] =4’h2 |
| sdio cdata0 _ | I/O | ETH1 RXD2 M1/SDMMC1 D0 M0/SAI3 SCLK M1/I2C9 _ _ _ _ _ _ _ SDA M1/SPI1 CLK M0/PCIE1 CLKREQN M1/PWM1 CH0 _ _ _ _ _ _ M1/GPIO1 B4 d | TOP IOC GPIO1B IOMUX SEL H[3:0 _ _ _ _ _ ] =4’h2 |
| sdio cdata1 _ | I/O | _ _ _ ETH1 RXD3 M1/SDMMC1 D1 M0/SAI3 LRCK M1/I2C9 _ _ _ _ _ _ _ SCL M1/SPI1 MOSI M0/PWM1 CH1 M1/GPIO1 B5 d _ _ _ _ _ _ _ | TOP IOC GPIO1B IOMUX SEL H[7:4 _ _ _ _ _ ] =4’h2 |
| sdio cdata2 _ | I/O | ETH1 RXCLK M1/SDMMC1 D2 M0/SAI3 SDO M1/UART _ _ _ _ _ _ 3 CTSN M2/SPI1 MISO M0/PCIE0 CLKREQN M1/GPIO _ _ _ _ _ _ 1 B6 d | TOP IOC GPIO1B IOMUX SEL H[11: _ _ _ _ _ 8]=4’h2 |
| sdio cdata3 _ | I/O | _ _ ETH1 TXD2 M1/SDMMC1 D3 M0/SAI3 SDI M1/UART3 _ _ _ _ _ _ RTSN M2/SPI1 CSN0 M0/GPIO1 B7 d | TOP IOC GPIO1B IOMUX SEL H[15: _ _ _ _ _ 12]=4’h2 |
| sdio cdetn _ | I | _ _ _ _ _ _ ETH1 PPSTRIG M1/SDMMC1 DETN M0/FSPI1 CSN0 M _ _ _ _ _ _ 1/UART4 CTSN M1/I2C6 SDA M1/SPI2 CSN0 M1/GPIO _ _ _ _ _ _ 1 C3 u | TOP IOC GPIO1C IOMUX SEL L[15: _ _ _ _ _ 12]=4’h2 |
| Module Pin | Dir. | PAD Name | IOMUX Setting |
| sdio pwren _ | O | ETH1 PPSCLK M1/SDMMC1 PWREN M0/FSPI1 RSTN M _ _ _ _ _ _ 1/FSPI1 CSN1 M1/UART4 RTSN M1/I2C6 SCL M1/SPI _ _ _ _ _ _ 2 CSN1 M1/PWM1 CH2 M1/GPIO1 C2 u | TOP IOC GPIO1C IOMUX SEL L[11: _ _ _ _ _ 8]=4’h2 |

## Page 1396 -- pin table

| Module Pin | Dir. | PAD Name | IOMUX Setting |
|---|---|---|---|
| sdio cclk _ | O | VI CIF D10/SDMMC1 CLK M1/ETH0 TXCLK M1/SAI0 S _ _ _ _ _ _ _ DO2 M0/PDM0 CLK1 M3/UART1 RTSN M1/SPI4 CLK _ _ _ _ _ _ _ M3/PCIE1 CLKREQN M0/GPIO2 B3 | TOP IOC GPIO2B IOMUX SEL L[15: _ _ _ _ _ 12]=4’h2 |
| sdio ccmd _ | I/O | _ _ _ _ VI CIF D11/SDMMC1 CMD M1/ETH0 TXD3 M1/SAI0 S _ _ _ _ _ _ _ DI2 M0/PDM0 SDI1 M3/UART1 CTSN M1/SPI4 CSN0 _ _ _ _ _ _ _ M3/PCIE0 CLKREQN M0/GPIO2 B2 d | TOP IOC GPIO2B IOMUX SEL L[11: _ _ _ _ _ 8]=4’h2 |
| sdio cdata0 _ | I/O | _ _ _ _ VI CIF D15/SDMMC1 D0 M1/ETH0 RXD0 M1/SAI0 SD _ _ _ _ _ _ _ O0 M0/UART8 TX M1/SPI4 CSN1 M3/I2C4 SCL M2/G _ _ _ _ _ _ _ PIO2 A6 d | TOP IOC GPIO2A IOMUX SEL H[11: _ _ _ _ _ 8]=4’h2 |
| sdio cdata1 _ | I/O | _ _ VI CIF D14/SDMMC1 D1 M1/ETH0 TXCTL M1/SAI0 S _ _ _ _ _ _ _ DO1 M0/UART8 RX M1/I2C4 SDA M2/GPIO2 A7 d | TOP IOC GPIO2A IOMUX SEL H[15: _ _ _ _ _ 12]=4’h2 |
| sdio cdata2 _ | I/O | _ _ _ _ _ _ _ VI CIF D13/SDMMC1 D2 M1/ETH0 TXD1 M1/SAI0 SD _ _ _ _ _ _ _ I0 M0/PDM0 SDI3 M3/UART1 TX M1/GPIO2 B0 d _ _ _ _ _ _ _ | TOP IOC GPIO2B IOMUX SEL L[3:0 _ _ _ _ _ ] =4’h2 |
| sdio cdata3 _ | I/O | VI CIF D12/SDMMC1 D3 M1/ETH0 TXD0 M1/SAI0 SD _ _ _ _ _ _ _ I1 M0/PDM0 SDI2 M3/UART1 RX M1/GPIO2 B1 d _ _ _ _ _ _ _ | TOP IOC GPIO2B IOMUX SEL L[7:4 _ _ _ _ _ ] =4’h2 |
| sdio cdetn _ | I | VI CIF D8/SDMMC1 DETN M1/ETH0 RXCLK M1/SAI0 _ _ _ _ _ _ _ MCLK M0/PDM0 CLK0 M3/UART7 RTSN M0/SPI4 MISO _ _ _ _ _ _ M3/SATA1 ACTLED M0/GPIO2 B5 d | TOP IOC GPIO2B IOMUX SEL H[7:4 _ _ _ _ _ ] =4’h2 |
| sdio pwren _ | O | _ _ _ _ _ VI CIF D9/SDMMC1 PWREN M1/ETH0 TXD2 M1/SAI0 _ _ _ _ _ _ _ SDI3 M0/PDM0 SDI0 M3/UART7 CTSN M0/SPI4 MOSI _ _ _ _ _ _ M3/SATA0 ACTLED M0/GPIO2 B4 d | TOP IOC GPIO2B IOMUX SEL H[3:0 _ _ _ _ _ ] =4’h2 |
| _ _ _ _ _ Notes: I=input, O=output, I/O=input/output, bidirectional Table 39-11 SDIO-m2 Interface Description |  |  |  |
| Module Pin | Dir. | PAD Name | IOMUX Setting |
| sdio cdetn _ | I | SDMMC0 PWREN/SDMMC1 DETN M2/HDMI TX HPDIN _ _ _ _ _ _ M1/EDP TX HPDIN M1/PWM1 CH2 M0/GPIO0 B6 d | PMU1 IOC GPIO0B IOMUX SEL H[1 _ _ _ _ _ 1:8]=4’h2 |
| _ _ _ _ _ _ _ Notes: I=input, O=output, I/O=input/output, bidirectional 39.6 Application Notes |  |  |  |

