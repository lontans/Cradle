# Datasheet outline index: Rockchip RK3576 TRM V1.2 Part1.pdf

This document has a rich embedded PDF outline (vendor-authored table of contents), so that's used as the index instead of a page-by-page table scan -- a table scan over a reference manual this size mostly finds thousands of near-identical register/bitfield tables, which isn't a useful index at any granularity finer than 'which section'. Drill into a specific section on demand (render/read those pages) when a real design question needs a specific register, and write findings into `cradle_sidecar/data/components/<PART>.md`, not here.

Total outline entries: 762.

| Level | Section | Page |
|---|---|---|
| 1 | Table of Content | 3 |
| 1 | Figure Index | 9 |
| 1 | Table Index | 12 |
| 1 | Warranty Disclaimer | 14 |
| 2 | &nbsp;&nbsp;Chapter 1 System Overview | 15 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;1.1 Address Mapping | 15 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;1.2 System Boot | 20 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;1.3 System Interrupt Connection | 20 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;1.4 System DMA Hardware Request Connection | 26 |
| 2 | &nbsp;&nbsp;Chapter 2 Clock and Reset Unit (CRU) | 30 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.1 Overview | 30 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.2 Block Diagram | 30 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.3 Function Description | 31 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.1 System Clock Solution | 31 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.2 System Reset Solution | 31 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.3 PLL Introduction | 32 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.3.1 FRACPLL Introduction | 32 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.3.2 INTPLL Introduction | 33 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.3.3 DDRPLL Introduction | 34 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.4 CRU Register Description(register of autocs is internel only, secure register is internal only) | 34 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.4.1 Internal Address Mapping | 34 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.4.2 Registers Summary | 34 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.4.3 Detail Registers Description | 47 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.5 PPLL_CRU | 228 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.5.1 Internal Address Mapping | 228 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.5.2 Registers Summary | 228 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.5.3 Detail Registers Description | 228 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.6 SECURE_CRU | 233 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.6.1 Internal Address Mapping | 233 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.6.2 Registers Summary | 233 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.6.3 Detail Registers Description | 235 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.7 PMU1_CRU | 251 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.7.1 Internal Address Mapping | 251 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.7.2 Registers Summary | 251 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.7.3 Detail Registers Description | 253 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.8 DDR0_CRU | 270 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.8.1 Internal Address Mapping | 270 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.8.2 Registers Summary | 270 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.8.3 Detail Registers Description | 271 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.9 DDR1_CRU | 276 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.9.1 Internal Address Mapping | 276 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.9.2 Registers Summary | 277 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.9.3 Detail Registers Description | 277 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.10 BIGCORE_CRU | 283 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.1 Internal Address Mapping | 283 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.2 Registers Summary | 283 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.3 Detail Registers Description | 283 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.11 LITCORE_CRU | 289 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.11.1 Internal Address Mapping | 289 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.11.2 Registers Summary | 289 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.11.3 Detail Registers Description | 289 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.12 CCI_CRU | 295 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.12.1 Internal Address Mapping | 295 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.12.2 Registers Summary | 295 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.12.3 Detail Registers Description | 295 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;2.13 Application Notes | 302 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.1 PLL Usage | 302 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.1.1 Start-up Operation | 302 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.1.2 Bypass Operation | 303 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.1.3 Glitch-free Scaler Operation | 303 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.1.4 Setting Guide on P, M, S, and K | 303 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.1.5 Setting Guide on SSCG_EN, SEL_PF, MFR and MRR | 304 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.1.6 Setting Guide on RESETB and BYPASS | 304 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.2 Divider Usage | 304 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.2.1 DivFree Divider Usage | 304 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.2.2 Fractional Divider Usage | 304 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.2.3 DivfreeDT50 Divider Usage | 304 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.2.4 DivFreeNP5 Divider Usage | 304 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.3 Global Software Reset | 304 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.13.4 BIU Clock gating reliance | 305 |
| 2 | &nbsp;&nbsp;Chapter 3 CPU | 306 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;3.1 Overview | 306 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1 Features | 306 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.1 Cortex-A72 Cluster Feature | 306 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.2 Cortex-A53 Cluster Feature | 306 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;3.2 Block Diagram | 307 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;3.3 Function Description | 307 |
| 2 | &nbsp;&nbsp;Chapter 4 GPU (Graphics Process Unit) | 309 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;4.1 Overview | 309 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;4.2 Block Diagram | 309 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;4.3 Function Description | 309 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;4.4 Register Description | 309 |
| 2 | &nbsp;&nbsp;Chapter 5 General Register Files (GRF) | 310 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.1 Overview | 310 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.2 Function Description | 310 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.3 PMU0_GRF Register Description | 310 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.3.1 Registers Summary | 310 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.3.2 Detail Registers Description | 310 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.4 PMU1_GRF Register Description | 318 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.1 Registers Summary | 318 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.2 Detail Registers Description | 319 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.5 SYS_GRF Register Description | 327 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.5.1 Registers Summary | 327 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.5.2 Detail Registers Description | 328 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.6 LITCORE_GRF Register Description | 357 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.6.1 Registers Summary | 357 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.6.2 Detail Registers Description | 357 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.7 BIGCORE_GRF Register Description | 360 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.7.1 Registers Summary | 360 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.7.2 Detail Registers Description | 360 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.8 CCI_GRF Register Description | 362 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.8.1 Registers Summary | 362 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.8.2 Detail Registers Description | 363 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.9 DDR_GRF Register Description | 367 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.9.1 Registers Summary | 367 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.9.2 Detail Registers Description | 368 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.10 CENTER_GRF Register Description | 397 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.10.1 Registers Summary | 397 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.10.2 Detail Registers Description | 397 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.11 GPU_GRF Register Description | 399 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.11.1 Registers Summary | 399 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.11.2 Detail Registers Description | 399 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.12 NPU_GRF Register Description | 400 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.12.1 Registers Summary | 400 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.12.2 Detail Registers Description | 401 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.13 PHP_GRF Register Description | 406 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.13.1 Registers Summary | 406 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.13.2 Detail Registers Description | 407 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.14 USB_GRF Register Description | 416 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.14.1 Registers Summary | 416 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.14.2 Detail Registers Description | 416 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.15 SDGMAC_GRF Register Description | 422 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.15.1 Registers Summary | 422 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.15.2 Detail Registers Description | 423 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.16 VO0_GRF Register Description | 428 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.16.1 Registers Summary | 428 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.16.2 Detail Registers Description | 428 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.17 VO1_GRF Register Description | 439 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.17.1 Registers Summary | 439 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.17.2 Detail Registers Description | 440 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.18 VOP_GRF Register Description | 445 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.18.1 Registers Summary | 445 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.18.2 Detail Registers Description | 446 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.19 COMBO_PIPE_PHY_GRF Register Description | 446 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.19.1 Internal Address Mapping | 446 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.19.2 Registers Summary | 447 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.19.3 Detail Registers Description | 447 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.20 USBDPPHY_GRF Register Description | 456 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.20.1 Registers Summary | 456 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.20.2 Detail Registers Description | 456 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.21 USB2PHY_GRF Register Description | 458 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.21.1 Internal Address Mapping | 458 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.21.2 Registers Summary | 458 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.21.3 Detail Registers Description | 459 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.22 HDPTXPHY_GRF Register Description | 473 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.22.1 Registers Summary | 473 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.22.2 Detail Registers Description | 474 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.23 DCPHY_GRF Register Description | 476 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.23.1 Registers Summary | 476 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.23.2 Detail Registers Description | 476 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.24 CSIDPHY_GRF Register Description | 478 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.24.1 Internal Address Mapping | 478 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.24.2 Registers Summary | 478 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.24.3 Detail Registers Description | 478 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.25 MPHY_GRF Register Description | 479 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.25.1 Registers Summary | 479 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.25.2 Detail Registers Description | 479 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.26 PMU0_IOC (GPIO0 MUX/Attribute) Register Description | 480 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.26.1 Registers Summary | 480 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.26.2 Detail Registers Description | 481 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.27 PMU1_IOC (GPIO0 MUX/Attribute) Register Description | 490 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.27.1 Registers Summary | 490 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.27.2 Detail Registers Description | 491 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.28 TOP_IOC (GPIO1/2/3/4 MUX) Register Description | 505 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.28.1 Registers Summary | 505 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.28.2 Detail Registers Description | 506 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.29 VCCIO_IOC (GPIO1/2/3/4 Attribute) Register Description | 530 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.29.1 Registers Summary | 530 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.29.2 Detail Registers Description | 533 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.30 VCCIO6_IOC (GPIO4 MUX/Attribute) Register Description | 602 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.30.1 Registers Summary | 602 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.30.2 Detail Registers Description | 602 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;5.31 VCCIO7_IOC (GPIO4 MUX/Attribute) Register Description | 609 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.31.1 Registers Summary | 609 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.31.2 Detail Registers Description | 610 |
| 2 | &nbsp;&nbsp;Chapter 6 PMU | 613 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;6.1 Overview | 613 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;6.2 Block Diagram | 613 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;6.3 Function Description | 614 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.3.1 Domain Partition | 614 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.3.2 Domain Description | 614 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.3.3 Operation Mode | 619 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.3.4 Low Power Mode | 619 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;6.4 Register Description | 619 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.4.1 Registers Summary | 619 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.4.2 Detail Registers Description | 625 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;6.5 Application Notes | 736 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.1 Hardware Low Power Mode | 736 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.2 Software Low Power Mode | 737 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.3 Power Domain Dependence Relationship | 737 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.4 Virtual Power Domain | 737 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.5 Bus Interface Unit(BIU) Idle/Active Operation | 737 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.5.1 BIU idle/active operation by hardware | 738 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.5.2 BIU idle/active operation by software | 738 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.6 Power Domain(PD) Power Up/Down Operation | 738 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.6.1 PD power down/up operation by hardware | 738 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.6.2 PD power down/up operation by software | 738 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7 Voltage Domain(VD) Power On/Off Operation Sequence | 739 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.1 VD_DDR power off/on operation | 739 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.2 VD_GPU power off/on operation | 739 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.3 VD_NPU power off/on operation | 739 |
| 6 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.3.1 VD_NPU power off/on operation by hardware | 739 |
| 6 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.3.2 VD_NPU power off/on operation by software | 739 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.4 VD_BIGCORE power off/on operation | 740 |
| 6 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.4.1 VD_BIGCORE power off/on operation by hardware | 740 |
| 6 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.4.2 VD_BIGCORE power off/on operation by software | 740 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.5 VD_LITCORE power off/on operation | 740 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.6 VD_PPLL power off/on operation | 740 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.7 VD_MPHY power off/on operation | 741 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.8 VD_DCPHY power off/on operation | 741 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.9 VD_HDPTXPHY power off/on operation | 741 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.10 VD_USBDPHY power off/on operation | 741 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.11 VD_USBPHY power off/on operation | 741 |
| 6 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.11.1 VD_USBPHY power supplied with VDD_LOGIC | 741 |
| 6 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.11.2 VD_USBPHY power supplied with VDD_PMU | 741 |
| 6 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.7.11.3 VD_USBPHY power supplied with individual power | 741 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.8 Memory Repair Operation | 742 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.8.1 Memory Repair State | 742 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.8.2 Hardware Repair Operation | 742 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.8.3 Software Repair Operation | 742 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.5.9 Power Management IO Usage | 742 |
| 2 | &nbsp;&nbsp;Chapter 7 MMU | 744 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;7.1 Overview | 744 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;7.2 Block Diagram | 744 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;7.3 Function Description | 744 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;7.4 Register Description | 746 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.4.1 Internal Address Mapping | 746 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.4.2 Registers Summary | 746 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.4.3 Detail Registers Description | 746 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;7.5 Interface Description | 748 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;7.6 Application Notes | 748 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.6.1 Normal Process | 748 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.6.2 Page Fault Process | 748 |
| 2 | &nbsp;&nbsp;Chapter 8 MCU Subsystem | 750 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;8.1 Overview | 750 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;8.2 Block Diagram | 750 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;8.3 CACHE Register Description | 752 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.3.1 Internal Address Mapping | 752 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.3.2 Registers Summary | 753 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.3.3 Detail Registers Description | 753 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;8.4 INTMUX Register Description | 757 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.4.1 Internal Address Mapping | 757 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.4.2 Registers Summary | 757 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.4.3 Detail Registers Description | 758 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;8.5 Interface Description | 761 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;8.6 Application Notes | 762 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.6.1 Clock and Reset Generation | 762 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.6.2 Memory Remap | 762 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.6.3 Interrupt for MCU | 763 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.6.4 Cache Initialization | 765 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.6.5 Cache Maintenance | 765 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.6.6 Cache RAM Debug Mode | 765 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.6.7 TCM | 766 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.6.8 Other Hints | 766 |
| 2 | &nbsp;&nbsp;Chapter 9 System Debug | 767 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;9.1 Overview | 767 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.1.1 Features | 767 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.1.2 Debug Components Address Map | 767 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;9.2 Block Diagram | 767 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;9.3 Function Description | 767 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.3.1 DAP | 767 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;9.4 Register Description | 768 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;9.5 Interface Description | 768 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.5.1 DAP SWJ-DP Interface | 768 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.5.2 DAP SW-DP Interface | 768 |
| 2 | &nbsp;&nbsp;Chapter 10 Share Memory (SHRM) | 770 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;10.1 Overview | 770 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;10.2 Block Diagram | 770 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;10.3 Function Description | 771 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.3.1 AXI Slave | 771 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.3.2 Arbiter | 771 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.3.3 SRAM | 771 |
| 2 | &nbsp;&nbsp;Chapter 11 Cache Coherent Interconnect (CCI500) | 772 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;11.1 Overview | 772 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11.1.1 Features | 772 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;11.2 Block Diagram | 772 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;11.3 Function Description | 773 |
| 2 | &nbsp;&nbsp;Chapter 12 DMA Controller (DMAC) | 774 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;12.1 Overview | 774 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;12.2 Block Diagram | 774 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;12.3 Function Description | 774 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.3.1 Introduction | 774 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.3.2 Operating states | 775 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;12.4 Register Description | 775 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.4.1 Internal Address Mapping | 775 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.4.2 Registers Summary | 776 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.4.3 Detail Registers Description | 777 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;12.5 Timing Diagram | 820 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;12.6 Application Notes | 820 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.6.1 Using the APB Slave Interfaces | 820 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.6.2 Security Usage | 821 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.6.3 Programming Restrictions | 824 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.6.4 Unaligned Transfers | 825 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.6.5 Interrupt Sharing between Channels | 825 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.6.6 Instruction Sets | 826 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.6.7 Assembler Directives | 826 |
| 2 | &nbsp;&nbsp;Chapter 13 Generic Interrupt Controller (GIC) | 828 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;13.1 Overview | 828 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;13.2 Block Diagram | 829 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;13.3 Function Description | 829 |
| 2 | &nbsp;&nbsp;Chapter 14 TIMER | 830 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;14.1 Overview | 830 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;14.2 Block Diagram | 830 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;14.3 Function Description | 830 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14.3.1 TIMER Clock | 830 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14.3.2 TIMER Mode | 830 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;14.4 Register Description | 830 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14.4.1 Internal Address Mapping | 830 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14.4.2 Registers Summary | 831 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14.4.3 Detail Registers Description | 832 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;14.5 Application Notes | 833 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14.5.1 Clock and Reset | 833 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14.5.2 Programming Flow | 834 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14.5.3 Other Hints | 834 |
| 2 | &nbsp;&nbsp;Chapter 15 Watchdog Timer (WDT) | 835 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;15.1 Overview | 835 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;15.2 Block Diagram | 835 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;15.3 Function Description | 835 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15.3.1 Operation | 835 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15.3.2 Programming Sequence | 836 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;15.4 Register Description | 836 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15.4.1 Internal Address Mapping | 836 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15.4.2 Registers Summary | 837 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15.4.3 Detail Registers Description | 837 |
| 2 | &nbsp;&nbsp;Chapter 16 HPTIMER | 839 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;16.1 Overview | 839 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;16.2 Block Diagram | 839 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;16.3 Function Description | 839 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16.3.1 TIMER Clock | 839 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16.3.2 Timer Mode | 839 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;16.4 Register Description | 840 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16.4.1 Internal Address Mapping | 840 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16.4.2 Registers Summary | 840 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16.4.3 Detail Registers Description | 841 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;16.5 Application Notes | 847 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16.5.1 Clock and Reset | 847 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16.5.2 Programming Flow | 848 |
| 2 | &nbsp;&nbsp;Chapter 17 Mailbox | 851 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;17.1 Overview | 851 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;17.2 Block Diagram | 851 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;17.3 Function Description | 851 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;17.4 Register Description | 851 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;17.4.1 Internal Address Mapping | 851 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;17.4.2 Registers Summary | 852 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;17.4.3 Detail Registers Description | 852 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;17.5 Application Notes | 854 |
| 2 | &nbsp;&nbsp;Chapter 18 SAR-ADC | 855 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;18.1 Overview | 855 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;18.2 Block Diagram | 855 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;18.3 Function Description | 855 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;18.4 Register Description | 855 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18.4.1 Internal Address Mapping | 855 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18.4.2 Registers Summary | 856 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18.4.3 Detail Registers Description | 857 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;18.5 Application Notes | 870 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18.5.1 Timing Diagram | 870 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18.5.2 Series conversion mode | 870 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18.5.3 Single mode | 870 |
| 2 | &nbsp;&nbsp;Chapter 19 Temperature-Sensor ADC (TS-ADC) | 872 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;19.1 Overview | 872 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;19.2 Block Diagram | 872 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;19.3 Function Description | 872 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19.3.1 APB Interface | 872 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19.3.2 TS-ADC Controller | 872 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;19.4 Register Description | 873 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19.4.1 Internal Address Mapping | 873 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19.4.2 Registers Summary | 873 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19.4.3 Detail Registers Description | 874 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;19.5 Application Notes | 883 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19.5.1 Conversion Flow | 883 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19.5.2 Timing Diagram | 884 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19.5.3 Temperature-to-Code Mapping | 884 |
| 2 | &nbsp;&nbsp;Chapter 20 SPINLOCK | 885 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;20.1 Overview | 885 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;20.2 Block Diagram | 885 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;20.3 Register Description | 885 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20.3.1 Internal Address Mapping | 885 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20.3.2 Registers Summary | 885 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20.3.3 Detail Register Description | 885 |
| 2 | &nbsp;&nbsp;Chapter 21 GPIO | 886 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;21.1 Overview | 886 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;21.2 Block Diagram | 886 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;21.3 Function Description | 886 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21.3.1 Data Control | 886 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21.3.2 Interrupts | 887 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21.3.3 Debounce Operation | 887 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21.3.4 Four OS Operation and Four Interrupts | 887 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;21.4 Register Description | 888 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21.4.1 Internal Address Mapping | 888 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21.4.2 Registers Summary | 888 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21.4.3 Detail Registers Description | 889 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;21.5 Application Notes | 899 |
| 2 | &nbsp;&nbsp;Chapter 22 Digital Audio Codec | 900 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;22.1 Overview | 900 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;22.2 Block Diagram | 900 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;22.3 Function description | 901 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22.3.1 Filters of Digital DAC | 901 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22.3.2 Volume Control | 901 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;22.4 Register Description | 901 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22.4.1 Internal Address Mapping | 901 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22.4.2 Registers Summary | 901 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22.4.3 Detail Registers Description | 903 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;22.5 Interface Description | 913 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;22.6 Application Notes | 914 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22.6.1 Software Application Notes | 914 |
| 2 | &nbsp;&nbsp;Chapter 23 Voice DMA(VDMA) | 915 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;23.1 Overview | 915 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;23.2 Block Diagram | 915 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;23.3 Function Description | 915 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;23.4 Register Description | 916 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23.4.1 Registers Summary | 916 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23.4.2 Detail Register Description | 916 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;23.5 Application Notes | 920 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23.5.1 VDMA configuration usage flow | 920 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23.5.2 Data Transfer Interrupt usage flow | 921 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23.5.3 Timeout configuration usage flow | 921 |
| 2 | &nbsp;&nbsp;Chapter 24 Serial Audio Interface (SAI) | 922 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;24.1 Overview | 922 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.1.1 Features | 922 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;24.2 Block Diagram | 922 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;24.3 Function Description | 923 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.3.1 I2S normal mode | 923 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.3.2 I2S left justified mode | 924 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.3.3 I2S right justified mode | 924 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.3.4 PCM early mode | 924 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.3.5 Flexibility and wide range of configurations | 924 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;24.4 Register Description | 925 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.4.1 Internal Address Mapping | 925 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.4.2 Registers Summary | 926 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.4.3 Detail Registers Description | 926 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;24.5 Interface Description | 937 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;24.6 Application Notes | 946 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.6.1 Software Application Notes | 946 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.6.2 Cascade Function Application Notes | 946 |
| 2 | &nbsp;&nbsp;Chapter 25 Pulse Density Modulation(PDM) | 949 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;25.1 Overview | 949 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;25.2 Block Diagram | 949 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;25.3 Function Description | 950 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25.3.1 AHB Interface | 950 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25.3.2 PDM Interface | 950 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25.3.3 Digital Filter | 951 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25.3.4 Clock Configuration | 951 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;25.4 Register Description | 951 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25.4.1 Internal Address Mapping | 951 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25.4.2 Registers Summary | 951 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25.4.3 Detail Registers Description | 952 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;25.5 Interface Description | 959 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;25.6 Application Notes | 963 |
| 2 | &nbsp;&nbsp;Chapter 26 Sony/Philips Digital Interface Transmitter (SPDIF TX) | 964 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;26.1 Overview | 964 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;26.2 Block Diagram | 964 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;26.3 Function Description | 965 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;26.3.1 Frame Format | 965 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;26.3.2 Sub-frame Format | 965 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;26.3.3 Channel Coding | 966 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;26.3.4 Preamble | 966 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;26.4 Register Description | 966 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;26.4.1 Internal Address Mapping | 966 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;26.4.2 Registers Summary | 967 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;26.4.3 Detail Registers Description | 967 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;26.5 Interface Description | 973 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;26.6 Application Notes | 974 |
| 2 | &nbsp;&nbsp;Chapter 27 SPDIF Receiver | 975 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;27.1 Overview | 975 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;27.2 Block Diagram | 975 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;27.3 Function description | 976 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27.3.1 Frame Format | 976 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27.3.2 Sub-frame Format | 976 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27.3.3 Channel Coding | 977 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27.3.4 Preamble | 977 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;27.4 Register Description | 978 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27.4.1 Internal Address Mapping | 978 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27.4.2 Registers Summary | 978 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27.4.3 Detail Registers Description | 978 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;27.5 Interface Description | 986 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;27.6 Application Notes | 988 |
| 2 | &nbsp;&nbsp;Chapter 28 Asynchronous Sample Rate Converter (ASRC) | 989 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;28.1 Overview | 989 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.1.1 Features | 989 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;28.2 Block Diagram | 989 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;28.3 Function Description | 990 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.3.1 Memory fetch mode | 990 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.3.2 Real-time transmission mode | 990 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;28.4 Register Description | 992 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.4.1 Internal Address Mapping | 992 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.4.2 Registers Summary | 992 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.4.3 Detail Registers Description | 993 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;28.5 Application Notes | 1002 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.5.1 LRCK multiplexing selector | 1002 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.5.2 LRCK Divider | 1005 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.5.3 Tracking period configure | 1005 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.5.4 DMA configure | 1005 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.5.5 Memory fetch mode configure | 1006 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28.5.6 Real-time transmission mode configure | 1006 |
| 2 | &nbsp;&nbsp;Chapter 29 Flexible Serial Peripheral Interface（FSPI） | 1007 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;29.1 Overview | 1007 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;29.2 Block Diagram | 1007 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;29.3 Function Description | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.3.1 AHB Slave | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.3.2 AHB Master | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.3.3 REG File | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.3.4 DMA CTRL | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.3.5 FIFO | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.3.6 NSPI CTRL | 1008 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;29.4 Register Description | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.4.1 Internal Address Mapping | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.4.2 Registers Summary | 1008 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.4.3 Detail Registers Description | 1010 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;29.5 Interface Description | 1038 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;29.6 Application Notes | 1041 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.6.1 Typical Program Flow Without DMA | 1041 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.6.2 Typical READ Flow Without DMA | 1042 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.6.3 Command Flow with DMA | 1043 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.6.4 SPI Mode and Sampling Phase Control | 1043 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;29.6.5 Idle Cycles | 1044 |
| 2 | &nbsp;&nbsp;Chapter 30 Serial Peripheral Interface (SPI) | 1045 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;30.1 Overview | 1045 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;30.2 Block Diagram | 1045 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;30.3 Function Description | 1047 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;30.4 Register Description | 1048 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;30.4.1 Internal Address Mapping | 1048 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;30.4.2 Registers Summary | 1048 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;30.4.3 Detail Registers Description | 1049 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;30.5 Interface Description | 1057 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;30.6 Application Notes | 1064 |
| 2 | &nbsp;&nbsp;Chapter 31 Improved Inter-Integrated Circuit (I3C) | 1066 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;31.1 Overview | 1066 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;31.2 Block Diagram | 1066 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.2.1 REG_CONF | 1066 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.2.2 TRAN_CTL | 1067 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.2.3 AFIFO_CTL | 1067 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.2.4 I3C_TOP | 1067 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;31.3 Function Description | 1067 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.3.1 Initialization | 1067 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.3.2 Controller Mode Programming | 1067 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;31.4 Register Description | 1074 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.4.1 Internal Address Mapping | 1074 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.4.2 Registers Summary | 1074 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.4.3 Detail Registers Description | 1076 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;31.5 Interface Description | 1100 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;31.6 Application Notes | 1102 |
| 2 | &nbsp;&nbsp;Chapter 32 Inter-Integrated Circuit (I2C) | 1105 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;32.1 Overview | 1105 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;32.2 Block Diagram | 1105 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32.2.1 I2C_RF | 1105 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32.2.2 I2C_PE | 1105 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32.2.3 I2C_TOP | 1105 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;32.3 Function Description | 1106 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32.3.1 Initialization | 1106 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32.3.2 Master Mode Programming | 1106 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;32.4 Register Description | 1108 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32.4.1 Internal Address Mapping | 1108 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32.4.2 Registers Summary | 1109 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32.4.3 Detail Registers Description | 1109 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;32.5 Interface Description | 1117 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;32.6 Application Notes | 1122 |
| 2 | &nbsp;&nbsp;Chapter 33 UART | 1125 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;33.1 Overview | 1125 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;33.2 Block Diagram | 1125 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;33.3 Function Description | 1126 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;33.4 Register Description | 1128 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33.4.1 Internal Address Mapping | 1128 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33.4.2 Registers Summary | 1129 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33.4.3 Detail Registers Description | 1129 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;33.5 Interface Description | 1148 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;33.6 Application Notes | 1160 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33.6.1 No FIFO Mode Transfer Flow | 1160 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33.6.2 FIFO Mode Transfer Flow | 1160 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33.6.3 Baud Rate Calculation | 1161 |
| 2 | &nbsp;&nbsp;Chapter 34 Pulse Width Modulation (PWM) | 1163 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;34.1 Overview | 1163 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;34.2 Block Diagram | 1164 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;34.3 Function Description | 1164 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.3.1 Capture mode | 1164 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.3.2 Continuous mode | 1164 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.3.3 One-shot mode | 1165 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.3.4 Clock Counter | 1165 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.3.5 Clock frequency meter | 1165 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.3.6 Biphasic Counter | 1165 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;34.4 Register Description | 1166 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.4.1 Internal Address Mapping | 1166 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.4.2 Registers Summary | 1167 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.4.3 Detail Registers Description | 1169 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;34.5 Interface Description | 1194 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;34.6 Application Notes | 1199 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.1 PWM Capture Mode Standard Usage Flow | 1199 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.2 PWM Power key Capture Mode Standard Usage Flow | 1199 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.3 PWM Continuous Standard Usage Flow | 1199 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.4 PWM One-shot Mode Standard Usage Flow | 1200 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.5 Multi-channel synchronous start Usage Flow | 1200 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.6 IR transmission Usage Flow | 1200 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.7 Clock counter Usage Flow | 1200 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.8 Clock Frequency meter Usage Flow | 1201 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.9 Biphasic Counter Usage Flow | 1201 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;34.6.10 Generates Waveform Through Lookup Table Usage Flow | 1201 |
| 2 | &nbsp;&nbsp;Chapter 35 RKCAN | 1202 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;35.1 Overview | 1202 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;35.2 Function Description | 1202 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.1 Block Diagram | 1203 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.2 ACCEPTANCE FILTER | 1203 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.3 BIT TIMING | 1204 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.3.1 Bit Timing Logic | 1204 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.3.2 Bit Timing Definition | 1204 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.3.3 Bit time transition | 1205 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.3.4 Sampling Point and Sending Point | 1205 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.3.5  Bit Synchronization | 1206 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.3.6 Transmitter Delay Compensation | 1207 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.4 RXSTORE | 1208 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.4.1  Internal Storage Mode | 1208 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.4.2  External Storage Mode | 1208 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.4.3  ESM Timeout Mechanism | 1209 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.2.5 ERROR PROCESS | 1209 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;35.3 Register Description | 1210 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.3.1 Internal Address Mapping | 1210 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.3.2 Registers Summary | 1210 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.3.3 Detail Registers Description | 1212 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;35.4 Interface Description | 1237 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;35.5 Application Notes | 1237 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.5.1 Controller initialization flow | 1237 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.5.2 Loop-back Mode | 1237 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.5.3 Silent Mode | 1238 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.5.4 RXSTX Mode | 1238 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.5.5 Auto Retx Mode | 1238 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.5.6 Bus Off Recovery Mechanism | 1238 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.5.7 Sleep Mode | 1238 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.5.8 Multi-frame Mode | 1239 |
| 2 | &nbsp;&nbsp;Chapter 36 Double Data Rate Serial Memory Controller (DSMC) | 1240 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;36.1 Overview | 1240 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;36.2 Block Diagram | 1240 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;36.3 Function Description | 1241 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.1 DSMC Core | 1241 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.1.1 Read | 1241 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.1.2 Write | 1241 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.1.3 Byte Mask | 1242 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.2 TX/RX Controller | 1242 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.3 C/A Encoder | 1242 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.4 FIFO | 1242 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.4.1 ADDR FIFO | 1242 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.4.2 W DAT FIFO | 1242 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.4.3 R DAT FIFO | 1243 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.5 Localbus | 1243 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.5.1 Region division | 1243 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.5.2 CA Encoder | 1243 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.3.5.3 Back pressure | 1243 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;36.4 Register Description | 1244 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.4.1 Internal Address Mapping | 1244 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.4.2 Registers Summary | 1244 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.4.3 Detail Registers Description | 1245 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;36.5 Interface Description | 1258 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;36.6 Application Notes | 1261 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.6.1 Typical Program Flow for Hyper Device | 1261 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.6.2 Typical Program Flow for Localbus Device | 1261 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.6.3 Chip Select selection | 1261 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.6.4 Configurable CS# Low Time | 1262 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.6.5 Data Map | 1262 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.6.6 Merge Operation | 1262 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36.6.7 Timing Adjustment | 1262 |
| 2 | &nbsp;&nbsp;Chapter 37 FlexBUS | 1264 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;37.1 Overview | 1264 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;37.2 Block Diagram | 1265 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;37.3 Function Description | 1265 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.1 Transfer Modes | 1265 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.2 Free Running | 1266 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.3 Single and Continuous Mode | 1266 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.3.1 Single Mode | 1266 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.3.2 Continuous Mode | 1266 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.4 CPOL and CPHA | 1266 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.5 TX Then RX Mode | 1267 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.6 DVP Slave Mode | 1267 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.6.1 Support Vsync high active or low active | 1267 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.6.2 Support Href High Active or Low Active | 1268 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.6.3 Data Format | 1268 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.6.4 One Frame Stop Mode | 1268 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.6.5 Frame Ping-Pong Mode | 1268 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.6.6 Storage | 1268 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.3.6.7 Crop | 1268 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;37.4 Register Description | 1269 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.4.1 Internal Address Mapping | 1269 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.4.2 Registers Summary | 1269 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37.4.3 Detail Registers Description | 1270 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;37.5 Interface Description | 1284 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;37.6 Application Notes | 1289 |
| 2 | &nbsp;&nbsp;Chapter 38 EMMC Host Controller | 1292 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;38.1 Overview | 1292 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;38.2 Block Diagram | 1292 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;38.3 Function Description | 1292 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.3.1 The AXI Master Bus Interface Unit | 1292 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.3.2 The AHB Slave Bus Interface Unit | 1292 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.3.3 Host Controller Registers | 1292 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.3.4 DMA Engine | 1292 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.3.5 SRAM Controller | 1293 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.3.6 Command Queuing Engine | 1293 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.3.7 Transfer Level Unit | 1293 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.3.8 Clock Adjustment Unit | 1293 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;38.4 Register Description | 1293 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.4.1 Internal Address Mapping | 1293 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.4.2 Registers Summary | 1293 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.4.3 Detail Register Description | 1296 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;38.5 Interface Description | 1350 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;38.6 Application Notes | 1350 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38.6.1 Clock Adjustment | 1350 |
| 2 | &nbsp;&nbsp;Chapter 39 Mobile Storage Host Controller (SDMMC&SDIO) | 1352 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;39.1 Overview | 1352 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;39.2 Block Diagram | 1352 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;39.3 Function Description | 1354 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.1 Bus Interface Unit | 1354 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.1.1 Host Interface Unit | 1354 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.1.2 Register Unit | 1354 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.1.3 Interrupt Controller Unit | 1354 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.1.4 FIFO Controller Unit | 1357 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.1.5 Card Detection Unit | 1357 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.2 Card Interface Unit | 1358 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.2.1 Command Path | 1358 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.2.2 Data Path | 1360 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.2.3 Non-Data Transfer Commands that Use Data Path | 1365 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.2.4  SDIO Interrupt Control | 1366 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.2.5 Clock Control | 1366 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.2.6 Error Detection | 1367 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.3 Internal Direct Memory Access Controller (IDMAC) | 1368 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.3.1 IDMAC CSR Access | 1368 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.3.2 Descriptors | 1368 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.3.3 Initialization | 1371 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.3.3.4 Variable Delay/Clock Generation Unit | 1373 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;39.4 Register Description | 1373 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.4.1 Internal Address Mapping | 1373 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.4.2 Registers Summary | 1373 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.4.3 Detail Register Description | 1374 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;39.5 Interface Description | 1395 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.5.1 SDMMC Interface Description | 1395 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.5.2 SDIO Interface Description | 1395 |
| 3 | &nbsp;&nbsp;&nbsp;&nbsp;39.6 Application Notes | 1396 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.1 Software/Hardware Restriction | 1396 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2  Programming Sequence | 1397 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.1 Initialization | 1397 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.2 Enumerated Card Stack | 1398 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.3 Clock Programming | 1399 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.4 No-Data Command With or Without Response Sequence | 1399 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.5 Data Transfer Commands | 1401 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.6 Single-Block or Multiple-Block Read | 1401 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.7 Single-Block or Multiple-Block Write | 1402 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.8 Sending Stop or Abort in Middle of Transfer | 1403 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.9 Read_Wait Sequence | 1404 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.10 Controller/DMA/FIFO Reset Usage | 1404 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.11 Card Read Threshold | 1404 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.12 Error Handling | 1404 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.13 Voltage Switching | 1405 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.14 Voltage Switch Operation | 1406 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.15 Voltage Switch Normal Scenario | 1407 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.2.16 Voltage Switch Error Scenario | 1408 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.3 DDR Operation | 1409 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.3.1 4-bit DDR Programming Sequence | 1409 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.3.2 8-bit DDR Programming Sequence | 1409 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.3.3 eMMC4.5 DDR START Bit | 1409 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.3.4 Reset Command/Moving From DDR50 to SDR12 | 1409 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.4 H/W Reset Operation | 1410 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.5 FBE Scenarios | 1410 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.5.1 FIFO Overflow and Underflow | 1410 |
| 5 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.5.2 Programming of PBL and Watermark Levels | 1410 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.6 Variable Delay Usage | 1411 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.7 Variable Delay Tuning | 1411 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.8 Card Detection Method | 1411 |
| 4 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;39.6.9 SDMMC IOMUX With JTAG | 1412 |
