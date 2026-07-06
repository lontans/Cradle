# Engineering decisions & corrections log

Append-only. Each entry is a decision made (with rationale) or an error caught and corrected during a design session. Don't edit past entries except to fix typos — if a decision is later reversed, add a new entry that supersedes it and link back.

Format per entry:
```
### YYYY-MM-DD — Title
**Decision/Correction:** what was decided or fixed
**Why:** the reasoning
```

---

### 2026 (design sessions, date not individually logged) — AP6275S over BL-M8800DS2
**Decision:** Use AMPAK AP6275S (Broadcom BCM43752) instead of BL-M8800DS2 (AIC8800).
**Why:** Mainline `brcmfmac` Linux driver support vs. out-of-tree AIC8800 vendor drivers. Driver ecosystem is a real selection criterion for a platform targeting community Linux support. Also, BL-M8800DS2 was out of stock on LCSC.

### Dual USB-C over USB-C + Micro-USB
**Decision:** Both ports are USB-C: USB1 sink/charge role, USB2 source/host role.
**Why:** Modern, cleaner design, same connector family reduces BOM, better ergonomics. Host port needs 56kΩ CC pull-ups (source role) vs. 5.1kΩ CC pull-downs (sink role) on the charging port.

### Mini-HDMI added to v1
**Decision:** Include mini-HDMI (signal only, no power) for bench debug.
**Why:** Enables a complete bench debug setup without additional hardware. Separate decision from the MIPI-DSI exclusion — this is about debug ergonomics, not product display output.

### 6-layer stackup mandatory
**Decision:** 6-layer SIG/GND/SIG/PWR/GND/SIG, not 4-layer.
**Why:** 4-layer is insufficient for LPDDR4X impedance control + multiple power domains + RF + HDMI differential routing on a credit-card form factor.

### Via-in-pad (POFV) used liberally
**Decision:** Use via-in-pad under both BGAs (RK3576, LPDDR4X) wherever helpful.
**Why:** Free on JLCPCB 6-layer boards, so there's no cost tradeoff to avoid.

### 47µF ceramic over tantalum on output caps
**Decision:** Ceramic (X5R) output caps on VSYS and PMIC buck outputs, not tantalum.
**Why:** Tantalum fails short circuit — a fire risk on a battery-native board with USB hot-plug transients. Ceramic derates under DC bias; compensated with higher voltage rating / parallel caps.

### BQ25601 input cap: 22µF per datasheet text, not 1µF per schematic figure
**Decision:** Use 22µF 25V X5R on the charger input.
**Why:** The BQ25601 datasheet text specifies 22µF; the sample schematic figure shows 1µF. Datasheet text takes precedence over schematic figures when they conflict.

### Speaker as JST connector, mics soldered
**Decision:** Microphones soldered on-board; speaker off-board via JST-PH cable.
**Why:** Mics are semiconductor components — tiny, position-critical for array geometry. Speakers are mechanical transducers needing air volume, physically incompatible with flat PCB mounting.

### 2026-07-05 — No external PDM codec (ADAU7002) for mic input
**Decision:** Mics (T3902 x2) connect directly to RK3576's native PDM input controller. No ADAU7002 or similar PDM-to-I2S/TDM decimation chip in the audio input path.
**Why:** RK3576 datasheet v1.6, page 21, confirms an on-chip PDM controller that does the decimation itself. Adding a separate codec (evaluated: ADAU7002ACBZ-R7) would be redundant — extra cost, extra part, extra failure point — since the SoC already does that job. The Audio sheet only needs the mic array wiring (CLK/DATA/SELECT) plus the MAX98357A output amp, not an input codec.

### Charge current limited to 2A in software
**Decision:** BQ25601 configured for 2A charge current via I2C, despite being capable of 3A.
**Why:** JST-PH battery connector is rated 2A nominal — the connector is the limiting factor, not the charger IC. Documented in schematic notes so it isn't "corrected" back to 3A later.

### 2026-07-05 — AP6275S requires external antenna (correcting earlier note)
**Correction:** architecture.md previously stated the AP6275S has "onboard antenna within module" — wrong. `WL_ANT0`/`WL_ANT1` are bare RF I/O pins with no integrated antenna; the module needs external antenna(s) routed on the Cradle PCB, same as the AP6275S EVB (which uses external SMA dipoles).
**Why:** Confirmed directly from the AP6275S datasheet pin definition table (pins 2, 9) and block diagram — no antenna structure exists inside the 15x13mm SIP package. High-throughput 2T2R SDIO combo modules generally leave antenna external because performance depends on the host PCB's ground plane/clearance, which module vendors can't bake in.

### 2026-07-05 — WiFi limited to 2.4GHz only for v1
**Decision:** Drop 5GHz band support; AP6275S wiring and antenna designed for 2.4GHz operation only.
**Why:** Dual-band (2.4/5GHz) chip antennas are harder to source (the originally-identified Taoglas WLA.10 isn't on LCSC) and need a more complex matching network to tune across both bands without access to a VNA. 5GHz's lower UNII-1 sub-bands (W52/W53) are also indoor-use-only per regulatory rules (confirmed in the AP6275S EVB manual's FCC section), which is awkward for a device meant for portable robotics/wearable use. Bluetooth and the mainline `brcmfmac` driver support are unaffected — only the 5GHz WiFi radio path goes unused. Can be revisited in a later revision since the module itself still supports 5GHz.

### 2026-07-05 — Bluetooth uses UART only; PCM interface omitted
**Decision:** Wire `BT_UART_TXD/RXD/RTS/CTS` to the RK3576. Don't route `BT_PCM_CLK/SYNC/IN/OUT`.
**Why:** UART (HCI) is the mandatory Bluetooth control/data interface. PCM is only needed if audio is meant to stream directly through Bluetooth in real time (e.g. acting as a BT headset/handsfree audio path). Cradle's audio already goes through the RK3576's own I2S/PDM pipeline (mics + MAX98357A) — no use case requires a second, BT-native audio path, so the PCM pins and their routing are skipped.

### 2026-07-05 — AP6275S clock requirements
**Decision:** AP6275S needs two dedicated external clock sources, not shared with the RK3576: 32.768kHz on `LPO` (sleep clock, external input — the module has no internal source for it) and 37.4MHz on `XTAL_IN`/`XTAL_OUT` (via crystal + 18pF load caps, or a single-ended clock source).
**Why:** Confirmed in the AP6275S datasheet pin definitions and external clock reference section (37.4MHz X'TAL: 18pF load cap, +/-10ppm tolerance; LPO: 32.768kHz square/sine wave input). These are separate from whatever clock references the RK3576 itself uses.

### 2026-07-05 — GPS/GNSS excluded from v1, left to expansion FPC
**Decision:** No onboard GNSS receiver. GPS is a consumer-addable peripheral via the 20-pin expansion FPC (UART/I2C available), not integrated into Cradle itself.
**Why:** AP6275S doesn't do GPS — adding it means a separate GNSS chip, its own antenna, and continuous power draw for a feature only some use cases (outdoor robotics/wearable) need. Indoor voice AI doesn't need location at all. Keeping it off-board avoids scope creep and battery budget impact for the common case, while still letting anyone who needs it wire one in externally.

### 2026-07-05 — Audio: mono speaker output, multi-mic array input (asymmetric architecture)
**Decision:** Single mono speaker (not stereo) on output; two-mic PDM array (not a single mic) on input.
**Why:** Voice AI/TTS output doesn't need stereo imaging — mono halves output power draw and simplifies routing/firmware. Input needs multiple mics for beamforming, wake-word detection, and acoustic echo cancellation (AEC), which a single mic can't do. Output and input have genuinely different requirements, so they're sized differently on purpose.

### 2026-07-05 — MAX98357A (U9) configured for I2S Channel 0, default 9dB gain
**Decision:** `SD_MODE` tied HIGH (3.3V from RK3576, below the 5V PVDD rail) to select I2S left channel (Channel 0). `GAIN` left NC (default 9dB).
**Why:** Fixing the amp to Channel 0 avoids running a full stereo I2S frame in firmware for a single speaker — less RK3576-side overhead. Default 9dB gain avoids clipping early while still reaching the MAX98357A's full 3.2W into 4Ω at 5V VDD. `OUTP`/`OUTN` are bridge-tied and routed directly to the speaker JST-PH 2-pin header (Adafruit-standard pinout) on the Interfaces sheet.

### 2026-07-05 — PDM mic stereo clocking: MIC1/MIC2 split by clock edge
**Decision:** MIC1 (SELECT tied to GND, right channel) samples on the PDM clock's rising edge; MIC2 (SELECT tied to 3V3, left channel) samples on the falling edge. Both share a single CLK/DATA pair.
**Why:** Standard PDM stereo technique — rising/falling edge multiplexing is what lets one DATA line carry two independent channels, avoiding a second DATA trace per mic. Confirms the RK3576 can decode both without any external PDM-to-I2S bridge: it has 2 independent PDM controllers plus 5 SAI/I2S blocks on-chip (RK3576 datasheet v1.6, p.21), so the mic PDM path and speaker I2S path run on separate peripherals simultaneously.

### 2026-07-05 — AP6275S clock components finalized
**Decision:** 37.4MHz reference: TXC crystal (18pF load capacitance) + ~30pF load caps on `XTAL_IN`/`XTAL_OUT` (calculated from CL=18pF assuming ~3pF board/pin stray capacitance). 32.768kHz sleep clock: SiTime SIT1552AI-JF-DCC-32.768D (C2650725) active MEMS oscillator wired directly to `LPO` — no load caps (it's active, not a passive resonator) and no decoupling cap (SiTime's internal supply filtering makes it optional per datasheet, saving the footprint).
**Why:** Closes out the two external clock requirements identified when reading the AP6275S datasheet's external clock reference section (p.30). The 32.768kHz part specifically needed to be an active oscillator, not a bare crystal, since `LPO` is a clock input pin with no internal Pierce-oscillator driver circuitry (unlike `XTAL_IN`/`XTAL_OUT`, which do have one).

### 2026-07-05 — AP6275S VDDIO must match RK3576 SDIO/UART logic levels
**Decision:** AP6275S's 1.8V `VDDIO` rail must match whatever logic level the RK3576's SDIO and UART pins run at.
**Why:** SDIO and UART are digital interfaces referenced to VDDIO — a mismatch would mean incorrect logic thresholds on the shared bus. Flagging this now so the PMIC rail feeding AP6275S gets confirmed against the RK3576's actual SDIO3/UART I/O voltage during the Compute/PMIC sheets.

### 2026-07-05 — WiFi antenna finalized: Johanson 2450AT18A100E
**Decision:** Antenna part is Johanson 2450AT18A100E (C89334), 2.4-2.5GHz single-band ceramic chip antenna — x2 for the AP6275S's 2T2R RF paths.
**Why:** ~74-76% efficiency (per Johanson's own datasheet) meaningfully beats the dual-band alternative originally considered (~51-65%), consistent with the decision to drop 5GHz — single-band tuning is both easier to source and measurably more efficient. Uses a "tee" (series-shunt-series) matching network, a different topology than the dual-band part's "pi" network — reference component values are a starting point, not guaranteed for Cradle's actual board without further tuning.

---

## Corrections caught by the designer (Claude errors)

These are logged separately because they're a signal of where to double-check future Claude-assisted work on this project — mostly datasheet detail and pin semantics.

- **QON is duration-based, not edge-triggered.** ~1s hold = wake from ship mode, ~8-12s hold = system reset.
- **QON has an internal pull-up** — no external pull-up resistor needed.
- **BQ25601 inductor is 1µH per datasheet**, not 2.2µH as initially suggested.
- **WPN252012ER47MT inductor ratings**: 4.1A is continuous, 7A is saturation (initially stated reversed).
- **RK806S-5 VOUT pins are distinct from SW pins**, bridged by the inductor. VOUT is both output and internal feedback sense — not interchangeable with SW.
- **Single-channel TVS (PESD5V0S1BA) is sufficient** for VBUS-only protection on USB1, not dual-channel (D+/D- are NC on this port).
- **REGN-to-TS fixed divider is 10kΩ** for JEITA compliance with the 103AT-series NTC.
