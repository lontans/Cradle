# Session notes — 2026-07-20 evening to 2026-07-21

Ad hoc log, not a formal part of the workflow (see `workflow-cheatsheet.md`/`co-design-workflow.md` for the actual system) — just a detailed record of what happened this session in case it's useful later. Timestamps below are netlist/BOM export times seen during the session, not wall-clock.

## Starting point

Re-oriented in the repo: read `MEMORY.md`, `cradle_sidecar/workflow-cheatsheet.md`, `README.md`. Storage sheet (U3, eMMC) was next to wire; Card1 (TF-01A) already done. No sidecar server work this session — everything went through the CLI tools and direct file edits, user had the web GUI open separately for their own review.

## EMMC04G-M627-Y02U (U3) component card — built from scratch

- Datasheet's mechanical extraction (`datasheet_index.py`/`.tables.md`) mis-categorized the ball-map figure (p.41) and the Table 4/5 signal table as "uncategorized"/"figure", so neither auto-ported. Read both directly via vision.
- Derived the full 153-ball FBGA pin table by cross-referencing the datasheet's ball map against every `U3-*` pin present in the netlist — confirmed all 153 balls populated but completely unwired at that point (single-pin auto-named nets only).
- **Found and fixed two real tooling bugs**, not specific to this card:
  - `card_lint.py` / `wiring_check.py`'s `PIN_ROW_RE` only accepted numeric pin fields (`[\d,\-]+`) — silently skipped every row of any BGA-style card (alphanumeric ball refs like `A6`, `K10`). Widened to `[A-Za-z0-9,\-]+`.
  - `wiring_check.py`'s `expand_pin_field()` had the same numeric-only assumption in a different function — returned an empty pin list for alphanumeric fields, which is why `project_refresh.py` briefly reported this card as "every pin Decided" when most rows were actually still Open. Fixed to handle both `"A3"` and `"A7-A14"` style fields.
- Verified the pin-table build mechanically (wrote a throwaway Python script to expand every compressed ball range and diff against the netlist's actual `U3-*` list — matched exactly, 153/153, no dupes, no gaps) before trusting the card.

## Reasoning topics on the EMMC card

- **VDDi (ball C2)**: initially said "no external spec given anywhere in the datasheet" — wrong. It's on Table 11 (p.26), just OCR-garbled by the mechanical porter into "V capacitor value DDi" so it read past unnoticed the first time. Corrected once re-read directly: internal regulator bypass node ("to stabilize regulator output to controller core logics"), 1-4.7uF cap to GND, no external drive.
- **HS400 vs HS200**: reasoned through RK3576's TRM — Chapter 38 "EMMC Host Controller" (has a Command Queuing Engine, an eMMC5.1-only feature) vs the separate Chapter 39 "Mobile Storage Host Controller (SDMMC&SDIO)" (DDR-only, no tuning chapter). Physical `EMMC_STRB` ball existing at all is itself evidence HS400 is supported. Concluded: target HS400; HS200 isn't a competing option, it's a mandatory intermediate step in HS400's own bring-up (tuning via CMD21); fallback if tuning proves unreliable is High Speed DDR, not HS200.
- **Data Strobe pull-down**: Figure 6 (p.21, "Bus Circuitry Diagram") revealed `R_Data_strobe` is a pull-*down*, not pull-up like the rest of the bus — a fact `datasheet_quickstart.py`'s "no candidate integration pages" finding had (wrongly) been treated as proof no application circuit existed at all. Value (10-100kOhm) was actually on Table 23 (p.38, mislabeled "HS400 Capacitance") — missed on first pass for the same OCR-adjacent reason as VDDi, corrected later.
- **VSS vs VSSQ grounding**: reasoned that the split is core-vs-I/O noise isolation (same category as VCC/VCCQ), not an analog-vs-digital problem — tie both to the single existing `GND` net, no dedicated AGND needed.
- **R_OD (open-drain switchable resistor for CMD)**: also from Figure 6. Datasheet explicitly allows a fixed `R_CMD` instead, at the cost of a lower max clock in the (brief, already-slow) open-drain/identification mode — validated the user's choice to skip it.

## Storage sheet wiring — verified across several re-exports

User wired the sheet in Altium between turns; each time, re-ran `netlist_parse.py`/`project_refresh.py`/`wiring_check.py` against the fresh export rather than trusting the stated intent:

- `CMD`/`DAT0-7`/`RST_n` → real `EMMC_*` hierarchical port nets matching RK3576's own ballout naming, 30kOhm pull-ups (`R51`-`R60`, standardized part reused from AP6275S's SDIO pull-ups) to `STORAGE_1V8`.
- `VCC`→`STORAGE_3V3`, `VCCQ`→`STORAGE_1V8` (confirms the HS400/1.8V decision as actually built).
- `VDDi`→`C99` (2.2uF) →`GND`, matching the recommendation exactly.
- `DS` wired later in the same session: `EMMC_DS`, 30kOhm pull-down to `GND`, within the Table 23 spec range.
- **Caught a self-inflicted bug**: rewriting the pin table's prose accidentally dropped the literal word "RK3576" from several rows, which silently broke `wiring_check.py`'s substring-based reachability tracking (count dropped from 11 to 3 with zero actual wiring change). Caught by re-running the check after the edit rather than assuming the rewrite was cosmetic-only.
- **DS pull-down FET** (`LBSS138LT1G`, user-scoped, gate driven by a new RK3576 GPIO "toggle net"): reviewed the part — `Vgs(th)`=0.5V gives clean turn-on margin from 1.8V or 3.3V, `RDS(on)` being spec'd at `Vgs`=5V rather than actual drive voltage is low-stakes in series with a 30kOhm resistor. Raised two real open questions rather than assuming answers: gate default state before firmware configures the GPIO, and why toggle the pull-down at all rather than leaving it always-on.

## HDMI-519S (U8) component card — built from a Chinese-only datasheet

- Datasheet (SOFNG/DongGuan CioDin, 5 pages) has zero pin-function content at all — just mechanical dimensions, a reliability-grade table (confirmed Grade B), and soldering/packaging specs. `datasheet_index.py` correctly found nothing portable here (not a tool miss, genuinely nothing to port).
- Built the pin table from the public HDMI Type-A standard pinout instead, explicitly tagged UNVERIFIED/not-vendor-sourced, and flagged it for a second-source check given how easy a TMDS polarity/position swap is to get wrong undetected.
- Cross-checked against RK3576's own ballout: confirmed the signal set (`HDMI_TX_D0P`-`D3N`, `CEC`, `SCL`/`SDA`, `HPDIN`) exists, and found RK3576 appears to use a combined HDMI/eDP PHY (4 diff pairs `D0`-`D3` rather than 3-data+clock) — exact lane mapping unconfirmed, no HDMI chapter in the TRM Part1 volume on disk.
- **5V question**: checked every documented RK3576 GPIO domain — none exceed 3.6V absolute max, and `HDMI_TX_SCL`/`SDA`/`CEC`/`HPDIN` all ride on ordinary muxed GPIO balls, not a dedicated 5V-tolerant HDMI pad. Concluded: do not pull DDC/HPD up to the connector's `+5V`, needs level-shifting. Suggested the classic single-MOSFET bidirectional shifter for the DDC pair, noting the DS-switch FET (`LBSS138LT1G`) was already the right part family for it.

## HDMI wiring — verified across several re-exports, including two rounds of self-correction

- **Pinout correction (user's finding, not mine)**: the connector's real physical pin numbering doesn't match the official HDMI signal-position numbering — shield-then-plus-then-minus per triad, not plus-then-shield-then-minus, plus CEC/Utility/HPD positions shifted. Confirmed via the user's own implementation + a Digikey reference. Rewrote the whole pin table and net-name map to match.
- **`Type` column correction**: TMDS pairs are `I` (input to the connector part), not `O` — direction is relative to the part the card describes, matching the existing `AP6275S.md`/`EMMC04G-M627-Y02U.md` convention, not relative to the whole board.
- **Level shifters** (`Q3`/`Q4`/`Q5`, `LBSS138LT1G`, one per line for `CEC`/`SCL`/`SDA`): verified against the netlist — gate biased to a new `INTERFACES_3V3` net, low side pulled to `INTERFACES_3V3`, high side pulled to a new `INTERFACES_5V` net (which also feeds the connector's own `+5V` pin). Confirms RK3576's HDMI GPIOs are on a 3.3V-capable bank.
- **`Q6` (HPD)**: initially flagged as not matching the `Q3`/`Q4`/`Q5` pattern (looked like a broken/inverted connection) — user clarified it's an intentionally different, simpler unidirectional inverting switch (`HPD` only flows one direction, so it doesn't need the full bidirectional shifter). Confirmed against the netlist that the described topology matches exactly. Real, non-obvious consequence flagged: `HDMI_HPD` ends up active-low at RK3576, which needs to be reflected in the HDMI driver/device-tree GPIO polarity config, not just the schematic.
- **TMDS ESD protection**: `D4`/`D5`/`D8` added first for Data1/Data2/Clock (`JLC_PRTR5V0U2X_C2827688`, real 2-line 0.3pF low-cap TVS array — good choice for TMDS bandwidth). Data0 initially missing; flagged two stray unwired diodes (`D6`/`D7`) with placeholder net names (`HDMI_D3`/`HDMI_D4`) as a likely-unfinished copy-paste. **Turned out backwards**: the actual mistake was a duplicate `D9` plus the stray placeholder nets, not `D6`/`D7` being debris. User fixed it by removing `D9` and the stray nets, then remapping `D6`→Data0 and `D7`→Clock. Final state (confirmed against the re-export): `D4`/`D5`/`D6`/`D7`, all consistently named, zero stray/duplicate parts.
- **`+5V` current-limiting**: still open at end of session — wired to `INTERFACES_5V`, no switch/current-limit component decided yet.

## Housekeeping

- `R62` (4.7kOhm `TFCR0603-10W-C-4701FT-1K`, the new DDC pull-up value) added to `cradle_sidecar/data/altium/standard-parts.md` as the staged/unplaced instance, matching the existing `R25`-for-30k pattern.

## Open items carried forward (see the cards themselves for full detail)

- `EMMC04G-M627-Y02U.md`: RST_n drive-vs-pull-up choice; DS FET gate default state; RK3576 pinmux instance assignment (Compute-SoC sheet doesn't exist yet).
- `HDMI-519S.md`: `+5V` current-limiting; RK3576 `D0`-`D3` lane mapping; RK3576 HDMI pinmux instance assignment; active-low `HDMI_HPD` needs to reach the software/driver config.

## Retrospective (asked directly, worth keeping)

User's take: workflow felt fast, felt like they were learning (implemented most of the HDMI level-shifting from a single suggestion + their own research), enjoyed it, asked whether it was token-expensive on my end.

My honest answer: the vision-based PDF page reads (~10-12 across both datasheets) were the real cost, not the greps. Two things kept it from compounding: `datasheet_index.py`'s per-page structural index meant every vision read was a targeted single page, never a blind full-document scan; and the write-back discipline (facts landing in the card with citations) meant a page never had to be re-read once its finding was captured — later reasoning in the same session pulled from the card text, not the PDF, multiple times. That's the mechanism sidecar is supposed to provide, and it visibly worked within a single session, not just across sessions.
