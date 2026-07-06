# Architecture — Locked

Cradle is a credit-card sized (85mm x 54mm) edge AI compute platform built around the Rockchip RK3576 SoC. It is a purpose-built consumer logic board — not a carrier board, not an embedded systems project. It targets the gap between Raspberry Pi (no NPU, not battery-native) and Jetson Orin Nano (overkill, expensive, not portable).

**Reference design:** Radxa ROCK 4D (RK3576 + RK806S-5). Primary reference for power tree, DDR topology, and PMIC configuration. Cradle diverges in form factor (credit card vs large SBC), power architecture (battery-native vs wall power only), interface philosophy (flat FPC vs vertical ports), wireless implementation (soldered SDIO vs USB dongle), audio (onboard mics + amp vs none), and software target (AI inference platform vs general purpose SBC). Radxa's schematic is flat topology; Cradle uses hierarchical sheets in Altium, requiring careful port and net name translation.

The items below are locked design decisions. Treat this section as a spec, not a scratchpad — update it deliberately and log the change in [CHANGELOG.md](../CHANGELOG.md), don't let it drift silently.

## Compute
- SoC: Rockchip RK3576, package FCCSP698L (16mm x 16mm, 0.6mm pitch, 698-ball BGA)
- RAM: Samsung K4UBE3D4AB-MGCL, 4GB (32Gbit) x32 LPDDR4X, 4266Mbps, 200-ball FBGA
  - Sourcing note: stock was volatile at selection time. Footprint-compatible fallback is K4U6E3S4AA-MGCL (2GB, same 200-ball FBGA)
  - 4GB chosen for headroom: Whisper small (~500MB) + RKNN runtime + Linux userspace (~400MB) + wake word detection concurrently
- Storage: Kingston EMMC04G-M627-Y02U, 4GB eMMC 5.1, FBGA-153
- MicroSD: Korean Hroparts TF-01A (C91145), push-push with locating pins, 1.85mm height, SMD

## Power
- Charger/power path: TI BQ25601RTWR — USB-C input, 1S LiPo charging, outputs VSYS
  - QFN-24 (4x4mm), I2C controlled, 3A max charge current (limited to 2A by JST-PH connector rating)
  - 1.5MHz switching frequency
  - NVDC power path management — instant-on works with no battery or deeply discharged battery
  - QON pin is **duration-based**, not edge-triggered: ~1s hold exits ship mode (power on), ~8-12s hold triggers full system reset. Ship mode entry via I2C command with 10-15s delay
  - QON has an internal pull-up — no external pull-up needed. Momentary switch (KMR221GLFS) to GND
  - TS pin: 10kΩ fixed resistor from REGN to TS, 103AT-series NTC thermistor (10kΩ, B=3435K) from TS to GND for JEITA-compliant temperature monitoring
  - Input cap: 22µF 25V X5R ceramic **per datasheet text** (not 1µF as shown in the sample schematic figure — text overrides figure)
  - Output caps: 47µF X5R ceramic on VSYS (not tantalum — tantalum fails short circuit, dangerous on a battery-native board)
  - Inductor: SWPA4030S1R0NT (C42193), 1µH, 5.7A saturation, 4.15A continuous, 18mΩ DCR, 4x4mm shielded
  - TVS on VBUS: PESD5V0S1BA,115 — single-channel, 5V standoff, SOD-323 (single-channel is sufficient; D+/D- are NC on this port)
  - D+/D- intentionally not connected to BQ25601 — default 500mA limit, overridden via I2C at boot
  - Battery connector: JST-PH 2-pin, pin 1 positive, pin 2 ground, rated 2A nominal
  - Reverse polarity protection MOSFET on battery input (DMP2035U or similar P-channel)
- PMIC: Rockchip RK806S-5, downstream of VSYS, handles all SoC rail sequencing
  - QFN-68 (7x7mm), OTP-programmed power sequence validated for RK3576 (same variant Radxa uses)
  - 10 buck converter stages, mostly 3-6.5A rated
  - SW and VOUT are **distinct pins** bridged by the inductor — VOUT is both power output and the internal feedback sense point (no external feedback divider)
  - Rail voltages are OTP-programmed at the factory
  - Buck inductors: WPN252012ER47MT (C317620), 0.47µH, 7A saturation, 4.1A continuous, 26mΩ DCR, 1008 package
  - Output caps: 47µF X5R ceramic (not tantalum)
  - Communicates with RK3576 over I2C for dynamic voltage scaling
- Dual input architecture: USB-C PD and LiPo battery both work independently. USB-C can power the board even if the battery circuit has issues — deliberate debug strategy
- CC resistors: 5.1kΩ pull-downs on CC1/CC2 of USB1 (charging port, sink role) vs 56kΩ pull-ups on CC1/CC2 of USB2 (host port, source role advertisement)

## Wireless
- AMPAK AP6275S (C2918717) — Broadcom BCM43752-based, WiFi 6 + Bluetooth 5.3
  - SDIO 3.0 for WiFi data: `SDIO_DATA_CMD/CLK/0/1/2/3`, 4-bit mode, direct to the RK3576's SDIO3.0 host controller. AP6275S's 1.8V `VDDIO` must match the RK3576's SDIO/UART pin logic levels
  - Bluetooth host interface is UART only (`BT_UART_TXD/RXD/RTS/CTS`, HCI, up to 4Mbps) — the `BT_PCM_*` pins are not routed. PCM is only needed for real-time BT audio streaming (e.g. acting as a BT headset), and Cradle's audio already runs through the RK3576's own I2S/PDM pipeline
  - Two external clocks, not shared with the RK3576:
    - 37.4MHz on `XTAL_IN`/`XTAL_OUT` — TXC 37.4MHz crystal (18pF load capacitance) + ~30pF load caps (C1/C2), calculated from CL=18pF assuming ~3pF board/pin stray capacitance
    - 32.768kHz on `LPO` — SiTime SIT1552AI-JF-DCC-32.768D (C2650725), active MEMS oscillator, wired directly: both GND pins to ground, VDD to 1.8V, CLK Out straight to `LPO`. No load caps (it's an active oscillator, not a passive crystal) and no decoupling cap (SiTime's internal supply filtering makes it optional per datasheet)
  - Soldered directly to board (not a USB dongle like Radxa) — cleaner integration, lower latency, better power management for battery-native use
  - Mainline `brcmfmac` Linux driver support — major advantage over AIC8800, which needs out-of-tree vendor drivers
  - Replaced original BL-M8800DS2 (AIC8800-based) which was out of stock on LCSC
  - SMD-50P, 15x13mm module footprint
  - No integrated antenna — `WL_ANT0`/`WL_ANT1` are bare RF I/O pins that must be routed to external antennas. 2T2R WiFi needs two RF paths; Bluetooth shares the `ANT1` path internally via the module's diplexer, no separate BT antenna needed
  - 2.4GHz-only for v1 (5GHz band dropped) — simplifies antenna sourcing/tuning and sidesteps the indoor-use-only restriction on 5GHz's lower UNII-1 sub-bands (W52/W53), which is awkward for a portable/robotics device. Bluetooth and driver support unaffected
  - Antenna: Johanson 2450AT18A100E (C89334), 2.4-2.5GHz single-band ceramic chip antenna, ~74-76% efficiency, x2 (one per RF path, 2T2R) — each needs a "tee" (series-shunt-series) matching network and a PCB keepout zone with ground vias per the antenna's layout guide; reference matching values are a starting point and may need tuning

## Interfaces
- Dual USB-C ports (both TYPE-C 16P QTWT, C5187472):
  - USB1: charging input + USB 2.0 data + MaskROM flashing. 5.1kΩ CC pull-downs (sink role)
  - USB2: USB 2.0 host output. 56kΩ CC pull-ups (source role). VBUS powered through AP2141WG-7 load switch (500mA current-limited, overcurrent protection, GPIO-controlled enable from RK3576)
  - "USB-C in, USB-C out" — clean product story, better developer ergonomics than Pi Zero's single micro-USB OTG
  - USB 2.0 chosen over 3.0 for v1 — no SuperSpeed need, avoids routing complexity
- Mini-HDMI (Type C): HDMI-519S (C183605), 19P female, SMD right angle
  - Signal only, no power delivery to the display — displays have their own power
  - Enables a complete bench debug setup: USB-C power + mini-HDMI to monitor + USB-C host to keyboard
  - Operating temp -10°C to +60°C (narrower than most components, acceptable for a dev platform)
- 30-pin FPC (FC-05D30P11H20, C23398805): MIPI-CSI camera interface, 0.5mm pitch, bottom contact, slide lock, right angle
- 20-pin FPC (FC-05D20P11H20, C23398799): I2C, SPI, UART, GPIO expansion, 0.5mm pitch, bottom contact, slide lock, right angle
  - Same manufacturer series as the 30-pin FPC for consistent footprint geometry and actuator feel
  - Users connect peripherals via FPC-to-header adapter cables or custom FPC cables to daughter boards
- MicroSD: TF-01A (C91145), push-push, 1.85mm height
- UART debug header: SM04B-GHS-TB(LF)(SN), JST GH 4-pin SMD right angle — TX/RX/GND/3.3V. Non-negotiable for bring-up, the primary debug interface before WiFi/SSH is up
- JTAG: pogo pin pad footprint (no connector), exposed copper pads, 10-pin ARM Cortex layout. Flat board aesthetic preserved; pogo pin jig pressed against pads during bring-up

## Audio
- Asymmetric input/output: multi-mic array on input (beamforming, wake-word, AEC), single mono speaker on output (voice AI/TTS doesn't need stereo imaging, and mono halves power draw and simplifies routing/firmware)
- Dual PDM MEMS microphones: TDK MMICT390200012 (C3171752), designators MIC1 (right) / MIC2 (left)
  - Omnidirectional, bottom-port, LGA-5 (3.5x2.7mm)
  - Placed at opposite corners for a noise-canceling array
  - Chosen over cheaper MEMSensing MSM261DGT003 for better SNR on a voice AI platform
  - PDM stereo over a shared CLK/DATA pair: MIC1 (SELECT tied to GND, right channel) samples on the CLK rising edge, MIC2 (SELECT tied to 3V3, left channel) samples on the CLK falling edge — this rising/falling-edge split is what lets one DATA line carry two independent channels
  - No external PDM-to-I2S/TDM codec (e.g. ADAU7002) needed — RK3576 has 2x independent PDM controllers plus 5x SAI/I2S blocks on-chip (confirmed in RK3576 datasheet v1.6, p.21), so PDM mics and I2S speaker output wire to separate peripherals simultaneously with no bridge chip
  - Two mics at opposite corners is a beamforming array, not a music-stereo pair — enables direction-of-arrival and noise cancellation for wake-word detection and cleaner Whisper input in non-quiet environments
- Class D amplifier: MAX98357AEWL+T (U9)
  - I2S input directly from RK3576, no separate audio codec or DAC needed
  - Configured as I2S Channel 0 (left channel) — `SD_MODE` tied HIGH (3.3V from RK3576, below the 5V PVDD rail) — reduces RK3576-side firmware overhead vs. running a full stereo I2S frame for a single speaker
  - `GAIN` left NC — defaults to 9dB, sized so the amp doesn't clip early and can still hit its full 3.2W into 4Ω at 5V
  - Filterless Class D, 3.2W into 4Ω at 5V, scales down at 3.3V
  - WLCSP BGA-9 (1.3x1.3mm) — extremely compact but requires X-ray inspection at JLCPCB
  - 100nF + 10µF bypass caps on PVDD
  - `OUTP`/`OUTN` bridge-tied, routed directly to the speaker JST-PH 2-pin header (Adafruit-standard pinout) on the Interfaces sheet
- Speaker: JST-PH 2-pin connector output from MAX98357A
  - Off-board, connected via cable — physically impossible to mount a speaker transducer flat on a credit card PCB
  - Mics are soldered (semiconductor components, tiny, position-critical for array geometry); speakers are mechanical transducers needing air volume — the two are handled differently on purpose

## Deliberately excluded from v1
- MIPI-DSI display output — not needed for target use cases (voice AI, robotics, wearable); mini-HDMI covers debug/demo; a wearable display would need power management beyond the 1S LiPo budget
- Full-size HDMI — too large for the credit-card form factor
- USB-A — vertical connector conflicts with the flat dense form factor goal; USB-C host port serves the same function
- RJ45 Ethernet — not needed for a wireless-first platform
- 40-pin GPIO header — replaced by the 20-pin micro-pitch FPC for flat form factor
- PCIe slot — overkill for v1, scope creep
- USB 3.0 — unnecessary for v1 use cases, saves routing complexity
- GPS/GNSS — AP6275S doesn't do GPS, and a separate GNSS chip is scope creep for use cases that don't need location (indoor voice AI). Left as a consumer-addable peripheral via the 20-pin expansion FPC (UART/I2C available) for anyone building outdoor robotics/wearable variants

## PCB design
- 85mm x 54mm credit card form factor
- 6-layer stackup: SIG / GND / SIG / PWR / GND / SIG
  - 4-layer is insufficient — not enough routing layers for LPDDR4X + multiple power domains + RF + HDMI differential pairs
  - Dual ground planes critical for the RF section and LPDDR4X signal integrity
  - 6-layer at JLCPCB is not significantly more expensive than 4-layer at this board size
- Controlled impedance: 50-ohm single-ended, 100-ohm differential
- All SMD, no vertical connectors except USB-C and mini-HDMI at the board edge — flat and dense
- Single-sided component placement for v1 (simpler assembly, single reflow pass, lower cost)
- JLCPCB fabrication and assembly

### Via strategy
- Standard vias: 20mil/10mil (0.5mm/0.25mm) used everywhere except BGA escape zones
- BGA escape: via-in-pad with POFV (Plated Over Filled Via) — free on JLCPCB 6-layer boards, resin-filled, copper-capped, no additional cost. Use liberally under RK3576 and LPDDR4X BGAs
- Two via styles in Altium DRC: `VIA_STANDARD` (20/10) and `VIA_BGA` (escape zone)

### Layout considerations
- LPDDR4X: length matched (~25ps group-to-group, ~5ps within byte lane), impedance controlled, placed immediately adjacent to the SoC
- RK3576 BGA fanout: outer rows escape with traces to nearby vias, inner rows use via-in-pad (free, so use it liberally)
- RK806S-5 PMIC: 10 buck inductors (1008 package each) plus ~40-50 passives. Place centrally with inductors radiating outward in a tight cluster
- HDMI: four differential pairs (TMDS data + clock) need 100-ohm impedance control, routed from SoC to board edge with no stubs and minimal vias
- AP6275S WiFi: RF traces need a solid ground reference, keep switching noise sources away

## Software target
- Mainline-adjacent Linux with real community support
- NPU inference via RKNN toolkit (6 TOPS)
- Whisper tiny/small for local speech-to-text transcription
- Wake word detection, always-on
- Cloud offload for heavy reasoning
- SSH over WiFi as the primary development interface once the network stack is up

One-line summary: Cradle is a purpose-built edge AI platform for battery-powered applications — not a better general-purpose SBC, a different product for a different use case.

## Key decisions and corrections

Design decisions with rationale, and Claude-caught corrections made during design sessions, are logged in [decisions-log.md](decisions-log.md) rather than duplicated here.
