# Co-design knowledge architecture

Status: **partially built.** This document is a handoff/spec for continuing this design conversation (with a human, or with another Claude instance) without re-deriving the reasoning from scratch. Two pieces exist for real now — `cradle_sidecar/tools/datasheet_index.py` and `cradle_sidecar/data/components/AP6275S.md` — everything else below is still a plan. "Concrete next steps" at the bottom reflects current state, not the original proposal.

## Problem this solves

Over one extended design session on the Wireless sheet (AP6275S), a recurring cost showed up: facts had to be re-derived multiple times because nothing durable captured them the first time.

- The same AP6275S pin table got re-read from a rendered PDF image three separate times across the conversation.
- A component value (CBUCK/ABUCK inductor sizing) got contradicted between an AI web-search summary ("2.2uH", low confidence, correctly not acted on), a directly-verified schematic render ("4.7uH", high confidence), and then a *second* real schematic that turned up an independently-correct-but-different "2.2uH" from a different board. Three numbers, two of them true, from different sources — exactly the scenario per-fact provenance tracking exists to prevent silently blending.
- A separate near-miss during component-card construction: my own read of a rendered schematic crop (`XTAL_IN`/`XTAL_OUT` pin order) disagreed with a direct table-parse of the authoritative vendor PDF. Caught by re-verifying against the higher-confidence source rather than asserting either silently — this is the provenance system actually functioning, not just a design goal.
- There was no structured record of which nets cross sheet boundaries, what electrical state they already carry (voltage domain, pull resistors, protocol version), or which sheet is responsible for that state — meaning by the time later sheets (e.g. Compute/SoC) get designed, resolving cross-sheet dependencies means re-reading prior sheets' history rather than checking one table.

The goal: make datasheet knowledge and cross-sheet board knowledge cheap to query and hard to silently corrupt, without turning this into an AI-does-the-schematic workflow. The user still designs the board; the system just removes the risky, expensive, error-prone parts of manual datasheet re-archaeology and cross-sheet bookkeeping.

## Approaches considered and rejected

Worth keeping explicit so they don't get re-proposed without new information.

**A fully-automated LLM extraction pipeline** (file-watcher drop-zone → local PDF parser → LLM structured-output API call → git-branch review → auto-commit to `cradle_sidecar/data/components/`) was proposed and rejected. Reasons:
- Structured outputs (Pydantic/JSON-schema-constrained decoding) enforce *format*, not *truth* — a model can invent a wrong pin function or a wrong value while perfectly satisfying the schema. This isn't hypothetical: the "2.2uH" web-search near-miss above was exactly this failure mode, just via search-summarization instead of structured extraction. Schema conformance doesn't touch that risk.
- Full-batch extraction on drop re-introduces the problem the two-speed content split (below) was built to avoid: transcribing bulky, rarely-needed content (full RF tables, timing diagrams) before any real question has been asked about it.
- Bulk auto-generated output isn't reviewable the way a small, question-scoped extraction is — nobody catches a wrong value buried in row 40 of a diff they weren't already looking for. The review that actually worked this session worked *because* it was scoped to one fact the user was already primed to check.
- Standing up a background daemon + separate LLM API integration + git automation is real infrastructure for a problem that doesn't need it: extraction already happens naturally as part of doing real design work in-session.
- **What was kept from this proposal:** the Pydantic field names (`part_number`, `high_level_summary`, `power_domains`, `pin_table`, `deferred_index`, `known_gaps`) as a rough field-template, populated manually/interactively rather than via automated API calls. The actual component-card schema (below) diverged from this template once real content was built — see "what changed" note in that section.

**markitdown** (PDF→markdown conversion library) was evaluated and rejected for this environment specifically — not a philosophical rejection, a practical one. It pulls in `magika` (ML-based file-type sniffing) which drags in `numpy`/`onnxruntime` native DLLs, and Windows Application Control on this machine blocks that DLL load. Don't re-attempt without addressing that, or on a different machine.

## Four layers, four different jobs

### Layer 0 — Structural index (built: `cradle_sidecar/tools/datasheet_index.py`)

A script, not an AI call. Given a PDF, it does two things, both purely deterministic (PyMuPDF's layout-based table detector + regex, no LLM anywhere):

1. **Flags** where things are on every page — pin tables, spec tables, figure/diagram captions, schematic-dense pages — into a page-number index (`<name>.index.md`), every row ending in `not yet needed` until a real question pulls it.
2. **Ports** pin tables and spec/parameter tables verbatim into a companion `<name>.tables.md` — these two categories are already fully structured data, so mechanically dumping them to markdown is formatting, not interpretation. Everything else stays pointer-only.

For documents with a large embedded PDF outline (vendor-authored bookmarks — the RK3576 TRM has 762 entries), the tool uses that outline as the index (`<name>.outline.md`) instead of the page-scan: a table scan over a 1412-page register-reference manual mostly finds thousands of near-identical `Bit/Attr/Reset Value/Description` bitfield tables, which is a flood, not an index. The vendor's own bookmark tree is already curated at the right granularity (peripheral/section, not per-register) and is free. Threshold: 20+ outline entries switches modes. Applies to more than just huge TRMs — the 50-page RK3576 datasheet itself has 46 outline entries and gets outline mode too.

**Now run across all of `cradle_sidecar/data/datasheets/`** (2026-07-08). What broke on real files, and what fixing it actually required:

- **AP6275S EVB manual pull-up table, SDIO pages** — worked on first run, no changes needed. Validated the whole approach: found the two spots that cost the most manual back-and-forth earlier in the session, unprompted.
- **False positive on document header/footer boilerplate** weakly matching "pin table" keywords on AP6275S — fixed by requiring a minimum row count (5).
- **Multi-page pin table split at a page break** (AP6275S pins 1-34 on one page, 35-50 on the next, no repeated header on the continuation page) — the continuation page's table has no header row PyMuPDF can classify, so it silently failed to port. Fixed with a stitching heuristic: an unheaded table immediately following a portable one, with matching column count, is treated as more rows of the same table.
- **Small BGA pin tables rendered as one row with newline-stacked cells** (ADAU7002's 8-ball part: one cell holds all 8 pin numbers newline-separated, next cell all 8 mnemonics, etc., instead of one row per pin) — silently failed both the row-count check and, if ported naively, would have flattened to an unreadable jumble. Fixed by detecting equal-line-count cells within a row and unmerging them into proper separate rows.
- **Underscore-in-identifier rendering artifact**, present throughout every vendor PDF touched this session (`WL_ANT0` extracts as `WL ANT0\n_`, `SDIO_DATA_CMD` as `SDIO DATA CMD\n_ _`, and sometimes a single identifier splits across three lines: `GAIN_SLOT` as `GAIN\n_\nSLOT`) — this wasn't just cosmetic, it actively broke the row-count-based unmerge fix above (uneven line counts across cells for reasons unrelated to actual row structure) and corrupted identifier names in every ported table, including ones that had already looked fine (AP6275S's antenna pin literally read `WL ANT0 _` in the first port). Fixed with a dedicated cleanup pass, applied to every cell before classification.
- **The identifier fix over-corrected on its first version**: when the same stray-underscore artifact landed at the end of a full prose sentence rather than immediately after the identifier it belonged to (MAX98357A's pin description: `...GAIN SLOT are both used for channel selection (Table 7).\n_`), blindly replacing every space in that line with underscores mangled the whole sentence — a real transcription corruption, caught by manually reading the ported output rather than trusting the fix on the first pass. Fixed by gating the space-to-underscore substitution on the line looking identifier-shaped (<=6 words); longer lines just have the stray underscore line dropped, leaving the prose untouched.
- **Known residual limitation, not chased further**: the 6-word heuristic isn't perfect — a short *condition* string that isn't really an identifier (e.g. `GAIN SLOT = GND through 100kOhm`, 6 words) can still get its spaces incorrectly converted to underscores. Smaller-scale than the sentence-corruption bug above (confined to one short cell, not a whole paragraph), left as a known gap rather than adding a fourth layer of heuristic — matches the "don't over-engineer a script whose job is triage, not perfection" principle this tool is built on. Review ported tables before trusting them fully, per the standing instruction already in every `.tables.md` header.

Every one of these was found by actually reading the tool's own output against the source PDF, not by inspecting the code in isolation — the tool doesn't replace that check, and shouldn't.

This layer only ever produces pointers and verbatim table dumps. It feeds Layer 1 — it doesn't replace the reading and reasoning that happens there, and it never rephrases datasheet language (every fix above was about *correctly reconstructing* what the PDF's text stream actually says, not summarizing or rewording it).

**Cost:** under 3 seconds each for the small/medium datasheets (12-63 pages). The 1412-page RK3576 TRM took 5m48s wall-clock for the full pass (`find_tables()` on every page is the expensive part; output writing is negligible). Not a meaningful cost on any axis that matters here — no API calls, runs locally, and the TRM only needs to be re-run when its own PDF changes, not per design question.

### Layer 1 — Component cards (built first example: `cradle_sidecar/data/components/AP6275S.md`)

One markdown file per IC where pin-level detail gets referenced repeatedly (not every passive — reserve for complex parts: RK3576, RK806S-5, AP6275S, MAX98357A, BQ25601, etc.). Location: `cradle_sidecar/data/components/<PART>.md`.

**What changed from the original proposal:** the first draft of this plan kept vendor facts and Cradle's wiring decisions in separate places (vendor facts in the card, wiring decisions implied to live in the net registry). Building the real AP6275S card surfaced that this was wrong for anything *local to one pin on one sheet* — e.g. "this net got pulled up for this reason" needs to sit right next to that pin's vendor-documented function, not in a separate document you'd have to cross-reference. Fix: the pin table now carries two extra columns beyond the vendor's own Type/Function —

- **Cradle Wiring** — what Cradle actually does with this pin, citing the relevant `decisions-log.md` date
- **Status** — `Decided` / `Open` / `Not addressed`, so an in-progress judgment call never silently reads as settled

The net registry (Layer 3) stays reserved for nets that actually cross sheet boundaries — that's a genuinely different problem (two sheets touching the same net without visibility into each other) than a pin-local fact.

#### Two-speed content split (confirmed, unchanged)

**Transcribe fully, upfront** (cheap, constantly reused):
- Full pin table, high-level summary (3-5 bullets), a "known gaps" list (things the datasheet explicitly does *not* specify — e.g. AP6275S never states a CBUCK/ABUCK inductor value, confirmed absent in both the AP6275S and its AP6275P sibling datasheet)

**Flag via Layer 0's index, defer transcription until actually needed** (bulky, rarely reused):
- Timing diagrams, full RF power tables, mechanical drawings, reflow profiles

**The "publish upstream" rule:** when a real design question forces opening a deferred entry (rendering a PDF page, zooming a figure), the work isn't finished until the extraction is written back into the component card. This is what prevents re-deriving the same fact in a later session — it's a discipline, not a tool.

#### Provenance tags (confirmed, unchanged)

- `[VERIFIED — <datasheet name> p.<N>]` — read directly off the primary vendor doc (or, better, a direct table-parse rather than a manual read — the AP6275S card's pin table was rebuilt this way specifically because table-parsing is higher-confidence than reading a rendered image)
- `[VERIFIED — <external schematic name>, rendered+zoomed]` — cross-referenced against a real design, confirmed visually. Not trusted from text-extraction alone — these schematic PDFs reliably scramble on text extraction (confirmed repeatedly this session) and need a rendered-image check
- `[UNVERIFIED — web search summary]` — lowest tier; never used alone to drive a component value

#### External validation section (confirmed, unchanged)

Third-party reference designs get their own section, separate from primary vendor datasheet content. Persist *extracted facts with citation* (source, URL, date accessed, what was confirmed), not the source files — especially when they carry confidentiality markings (the Geniatech schematics used this session did; they were deleted after extraction, facts retained with citation).

### Layer 0.5 — Netlist/BOM parser (built: `cradle_sidecar/tools/netlist_parse.py`)

Same philosophy as the datasheet indexer, applied to Altium's own exports instead of vendor PDFs: deterministic parsing, no interpretation of intent. Takes a Protel netlist (`Design > Netlist For Project > Protel`) and a BOM CSV (`Reports > Bill of Materials`), cross-references designators to resolve part names, and flags two cheap things — `floating` (single-pin net, real error) and `unlabeled` (Altium auto-generated the net name, no one placed a manual label — common mid-design, not necessarily wrong).

Tested against Cradle's real, in-progress export (2026-07-08) — 175 components, 87 nets, ran in 57ms. Zero floating nets found, but that's not the same as zero problems: **a pin with no connection at all doesn't produce a floating net — it just never appears in the netlist**, since Altium only emits a net entry for pins that are actually wired to something. Caught this the hard way by cross-referencing `AP6275S.md`'s full pin table against which `U2-*` pins actually appear anywhere in the real netlist:

- 18 of 23 "missing" pins matched something already flagged `Open`/NC/not-addressed in the component card — expected, not a problem (the `CBUCK`/`ABUCK` inductor loop pins, for instance, since that value is still undecided).
- **5 were unexpected**: `WL_REG_ON`(15), `WL_HOST_WAKE`(16), `VBAT`(36), `BT_REG_ON`(38), `BT_HOST_WAKE`(50) — all marked `Decided` in the component card, meaning a real connection was already documented, but none of them have any net entry in the actual schematic yet. `VBAT` is the module's main power input, not a minor signal — worth checking in Altium directly.

**Correction (2026-07-08):** initially misattributed a separate user-reported gap ("sheets with 24-27 undefined") to this AP6275S pin analysis, since 5 of the missing pins happened to fall in that numeric range — presented with more confidence than the evidence supported, exactly the kind of unverified inference the provenance discipline is meant to catch, and it wasn't caught before being stated. The real issue was unrelated: a top-level Altium sheet (the hierarchical block diagram containing sheet-symbols for each sub-sheet) had net labels placed that were intended to become real nets but aren't wired yet. **This class of gap is invisible to the Protel netlist export entirely** — not as a floating net, not as anything; an unconnected label at the sheet-symbol/hierarchical-port level simply produces no net entry, same root cause as the missing-pin case above but one level higher in the hierarchy, and current tooling has no way to detect it from the exported files alone. The correct place to catch it is Altium's own ERC/compile step (which should flag an unconnected net label or an unmatched hierarchical port directly), not post-hoc netlist parsing — noted here so this isn't attempted again as a netlist-parser feature without first checking whether Altium's own compiler already covers it.

**Another real limitation, surfaced by the user pointing out which parts in the BOM are "standard/common" (C8, C9, C10, C11, C12, C13, C80, C83, L2, R25, R26, R27, R28, LED3) versus functionally-specific:** the BOM has no way to encode this distinction, and it isn't inferable from part value alone — several designators *not* on that list share the exact same part number as ones that are (`C84`/`C85` share `C11`'s 10pF/0402/C0G value; `C81`/`C82` share `C80`'s 30pF/0402/C0G value), meaning the same generic passive gets reused for both boilerplate decoupling and functionally-specific roles (e.g. antenna DC-block caps, crystal load caps) elsewhere in the design. "Standard vs. critical" is a property of what a specific designator instance connects to, not a property of the part itself — it can only come from the user's own knowledge or from cross-referencing each instance's actual net against an already-established component card, not from the BOM in isolation.

This is the real value case for having Layer 1 (component card) and this parser both exist: neither alone catches this. The card without the netlist is just documentation of intent; the netlist without the card is just wires with no way to know what's *supposed* to be there. `get_designator_pins()` in the script exposes exactly what's needed to repeat this check for any other component that has a card.

**Real, concrete limitation found on first use:** the BOM export has no `Sheet`/`Document` column (`Name, Description, Designator, Footprint, LibRef, Quantity` only) — the assumption in the original Layer 3 plan that a BOM would hand over designator-to-sheet mapping for free was wrong. Partial signal exists instead: net names in the real export carry sheet-derived prefixes for peripheral-specific signals (`WIRELESS_SDCMD`, `AUDIO_5V`, `MIC_CLK`, `PMIC_*`) but *not* for shared power/ground rails (`VDD`, `GND`, `PLDO1-5`), which by nature span multiple sheets and are named by rail function instead. Building the full cross-sheet Layer 3 registry will need either a re-exported BOM with a sheet column added (check the template's variable/column editor) or a small manually-maintained designator-to-sheet map — deferred until that's resolved.

**Also found:** the real Altium net names don't match what `AP6275S.md`'s Cradle Wiring column assumed — the card says `SDIO_DATA_CMD`, the actual schematic net is named `WIRELESS_SDCMD`. Naming drift between the planning conversation and what's actually in Altium; worth reconciling next time that card gets touched.

### Layer 0.6 — Wiring check (built: `cradle_sidecar/tools/wiring_check.py`)

Directly answers the recurring question this whole system exists for: "what's left to wire on the SoC side, and which direction is each signal" — without re-deriving the pin list from memory (the scenario that motivates this: remembering `HOST_WAKE_BT`/`HOST_WAKE_WIFI` need GPIOs is one failure mode, forgetting whether they're inputs or outputs is another, and the component card is what prevents the second one).

Cross-references a component card's pin table against the real netlist: parses the `## Pin table` markdown (regex on the row shape), filters to rows whose Cradle Wiring column names the target part, and reports per pin whether it has *any* net on the source designator's side yet, and whether that net actually reaches the target designator. Built and tested live against `AP6275S.md` + the real netlist (source `U2`, target `U1`/RK3576):

```
python cradle_sidecar/tools/wiring_check.py cradle_sidecar/data/components/AP6275S.md U2 U1 RK3576 cradle_sidecar/data/altium/Netlist/Cradle.NET
```

**Caught three real bugs on first run, found by comparing the script's output against a hand-verified list rather than trusting it on the first pass** — same discipline as the datasheet indexer's bug list above:
- A row with a compound name cell (`` `WL_HOST_WAKE`/`WL_GPIO_0` ``) broke the parsing regex and silently dropped that pin from the report entirely.
- Three rows (`BT_UART_RXD`/`RTS_N`/`CTS_N`) used a human-friendly shorthand ("Same UART instance as above") instead of repeating "RK3576" — invisible to a substring match, so all three silently vanished from the report.
- `BT_PCM_CLK` was a false positive: its *explanation* of why it's not routed happens to mention "RK3576," which matched the filter even though the actual instruction is "not routed."

**Fix applied to both sides, not just the script**: `AP6275S.md`'s pin table itself got de-compressed (the combined `19-22`/`SDIO_DATA_3/2/0/1` row split into 4 separate rows with correct per-pin names; the "same as above" shorthand rows made self-contained) plus the script gained a `NOT_ROUTED_RE` exclusion. The general lesson, not just this one card: **writing a component card for human readability (compressed ranges, "same as above" shorthand) directly works against the stated purpose of the file being machine-queryable** — favor self-contained rows over avoiding repetition, everywhere in `cradle_sidecar/data/components/`, not just here.

**Structural limit found (2026-07-08), not a bug to fix in the parser:** asked for the Wireless sheet's exposed nets; reported `VBAT`/`WL_GPIO_10`/`WL_GPIO_11` as unwired based on the netlist. User reported these are actually wired in Altium (`WIRELESS_3V3`, `WIRELESS_WL_GPIO_10/11`) — confirmed via raw `grep` (not just the parser) that none of those strings exist anywhere in the netlist file. Two live hypotheses, not distinguishable from the exported files alone: the netlist is stale (edited in Altium after the 16:04 export), or — the user's own hypothesis, plausible — a component pin wired directly to a net label with no matching Sheet Entry/Port on the parent sheet isn't a *resolved* hierarchical connection from Altium's point of view, and may not survive netlist export the same way a fully-linked net does.

This is not fixable by parsing harder. Hierarchical port resolution is something Altium's own compiler understands natively (Sheet Entries, Port matching, ERC rules) and a flattened Protel netlist has already lost that structure — there's no way to reconstruct "is this net label actually connected to a matching port elsewhere" from the exported text alone. **The correct source for this class of check is Altium's own ERC/Compile output** (`Project > Compile PCB Project`, then the Messages/Errors panel — would flag "net label not connected" or "unmatched hierarchical port" directly), not something to keep trying to infer post-hoc.

**Two concrete fixes applied, both about making staleness/uncertainty visible rather than silently trusting stale data:**
- `netlist_parse.py` and `wiring_check.py` both now print a `SOURCE FRESHNESS` line (file mtimes) on every run, and the generated `.md` output carries the same line plus an explicit warning that a "missing net" finding is indistinguishable from a stale export. Re-export before trusting a missing-net report, every time.
- User-reported facts that contradict the current netlist export get written into a component card as `[UNVERIFIED — user-reported <date>, not present in <netlist> export]`, not silently upgraded to confirmed/`Decided` — same provenance discipline as everything else in this doc, applied to a new source (a live claim in conversation) that hadn't come up before.

### Layer 0.7 — Sheet resolution (built: `cradle_sidecar/data/altium/sheet-map.md` + wired into `netlist_parse.py`, 2026-07-08)

The BOM-has-no-Sheet-column gap from earlier is resolved — the user added a `SheetNumber` column to the BOM template in Altium and re-exported. `cradle_sidecar/data/altium/sheet-map.md` holds the number→name mapping (`1=Cradle` (top-level), `2=Power_Charging`, ... `9=Audio`); `netlist_parse.py` resolves every designator to a sheet name automatically now, in every report.

**Real quirk in the data, not a bug:** `SheetNumber` is exact for single-designator BOM rows, but for a row grouping multiple designators sharing one part value (the standard-parts case), it's a **deduplicated set of every sheet that value touches anywhere** — no per-instance breakdown. Handled by reporting those as `ambiguous(sheet list)` rather than guessing. This turned out to cross-validate something rather than just being a limitation: `C11`/`C84`/`C85` (the shared 10pF antenna-cap value) all show `ambiguous(Cradle top-level, Cradle_Wireless)` — and independently, the netlist already confirmed `C84`/`C85` connect to `ANT1`/`ANT2` while `C11` connects to nothing. Three independent sources (user's `standard-parts.md` list, netlist connectivity, BOM sheet data) agree on the same conclusion without having been told to agree — `C11` is the still-staged instance sitting on the top-level sheet, `C84`/`C85` are the real ones. Worth remembering as a general pattern: **"Sheet 1 appears in an ambiguous sheet-set" is itself evidence for "still staged," not just an artifact to ignore.**

Concretely resolved the open "where's D1" question from earlier this session: `D1` → `Cradle_Interfaces` (was previously undeterminable — D1 has zero net connections, so nothing about connectivity could answer it; only the sheet data could).

**Methodology gap found (2026-07-08), not a script bug — this is about what got checked, not how:** asked to verify the Wireless sheet's internal wiring was correct. Checked SDIO pin-mapping, crystal IN/OUT pairing, the LPO clock chain, and GND completeness — all correct, no issues found. **Missed the CBUCK/ABUCK bridging inductor entirely** — the single most-discussed unresolved item in this whole session, already flagged `Open` in `AP6275S.md`'s own pin table. Two compounding causes, not one:

1. **Picked checks by pattern-matching "classic mistake shapes"** (pin swaps, GND coverage) instead of systematically walking every row the card itself already flags as `Open` and confirming whether the netlist had caught up. The information to catch this was already in the file being checked against — the process just didn't consult it that way.
2. **`wiring_check.py` structurally couldn't have caught it even if run.** It was built around one pattern only — "does a signal reach a *different* target designator" (RK3576). The CBUCK/ABUCK loop isn't that pattern at all: it's two pins on the *same* part (`U2`) needing an external component bridging them, entirely local to one sheet. The tool's own filter (`if target_name not in row["cradle_wiring"]`) silently excludes rows like this, since they mention `CSR_VLX`/`ASR_VLX`, never "RK3576." Building one check and treating it as covering wiring-correctness generally was the mistake — not the check itself being wrong for what it does cover.

**Fix, `cradle_sidecar/tools/wiring_check.py --open <card> <designator> <netlist>`:** walks every non-`Decided` row regardless of what it mentions, no target designator required. Caught a second, related bug on first run: it initially reported the CBUCK/ABUCK pins as "wired" anyway, because `get_designator_pins()` only checks "appears in *some* net," and Altium emits an auto-named net even for a pin with nothing else connected to it — same class of mistake as the orphaned/pending-port distinction already built into `netlist_parse.py`, just not applied here. Fixed with `get_really_wired_pins()` (requires >=2 net members), which is the semantically correct version specifically for this check: a single-pin net here means no real component was placed, full stop, unlike `check_wiring()` where a single-pin *named* net is legitimate progress (a hierarchical port waiting for its far sheet).

### Layer 2 — Sheet contracts (still proposed, not built — open question below)

For each schematic sheet, a short "what crosses this boundary" spec: every hierarchical port, direction, and any electrical commitment already locked in.

**Open question raised by building Layer 1 for real:** now that pin-local facts live in the component card, a sheet contract may be redundant with a sheet-filtered view of the net registry (Layer 3) — i.e. "show me every registry row where Wireless is the driver or consumer" might just *be* the sheet contract, with no separate document to maintain. Not resolved; flagging rather than unilaterally dropping it.

### Layer 3 — Net registry (seeded: `cradle_sidecar/data/net-registry.md`)

A single flat table, one row per net that **crosses a sheet boundary** — this scope got tightened by the Layer 1 work above; it is explicitly not for pin-local facts anymore. This is what prevents accidentally double-applying a pull resistor on a net that's already pulled elsewhere, and hunting through every prior sheet to reconstruct what a later sheet (e.g. Compute-SoC) still owes.

**Built 2026-07-08:** `cradle_sidecar/data/net-registry.md` seeded with 19 Wireless cross-sheet rows (real Altium net names). Mechanically validated against netlist exports by `cradle_sidecar/tools/registry_check.py` (presence + member count only, no interpretation). Sheet-local nets — clocks (`LPO`, `XTAL_*`), RF (`WL_ANT*`), same-sheet buck loops (`CBUCK`/`ABUCK`) — are intentionally excluded; see `AP6275S.md`'s net name map footnote for the rule.

Filtering this table by `SoC pin = TBD` **is** the Compute-SoC sheet's checklist — no separate document needed.

**Still open, not yet decided:** markdown table in `cradle_sidecar/data/net-registry.md` vs. CSV for easier mechanical filtering as row count grows.

**Still open, not yet decided:** pre-populate the "SoC pin" column with candidate constraints as each peripheral sheet is designed (e.g. "needs an RTS/CTS-capable UART instance"), or leave blank/TBD until the SoC sheet resolves it.

## Layer this sits on top of (already working, no change)

- `docs/decisions-log.md` — append-only narrative of *why*. Net registry/component cards capture *current state*; decisions-log keeps the reasoning trail. Same split as a journal vs. a queryable current-state table.
- `docs/architecture.md`, `docs/bom.md`, `docs/schematic-status.md` — living summaries, functioning well, no proposed change.
- **Netlist export (Altium)** — once schematic entry begins, a plain-text/CSV netlist export becomes ground-truth Layer 4, eventually cross-validating the net registry against what's actually wired. Not usable yet — `hardware/` has no Altium project checked in.

### Layer 0.8 — Quick-start digest (built: `cradle_sidecar/tools/datasheet_quickstart.py`, 2026-07-08)

Second pass over `datasheet_index.py`'s already-generated output (not a fresh PDF scan) — produces `<PART>.quickstart.md`: the pinout table, keyword-flagged pins worth investigating before wiring, and candidate integration-circuit pages. Deterministic keyword triage only, same boundary as everything else in this layer — it narrows where to look, doesn't explain integration itself.

Validated before being trusted, not just assumed to work: ran cold against AP6275S's already-ported pin table, and the keyword scan (`internal`, `external`, `generation`, `regulat`, `crystal`, `oscillat`, `reserved`, `floating`) flagged `CBUCK_0P9`/`CSR_VLX`/`ASR_VLX`/`ABUCK_1P12` on the very first pass — the same gap that took two external reference schematics to resolve manually earlier in this session, and the same gap `wiring_check.py`'s default mode missed later (see the methodology-gap entry above). If this tool had existed at the start, that investigation would have started from "these four pins are flagged, go check them" instead of discovering the gap by accident partway through.

Also designed to surface absence as a finding, not a null result: when no figure in the datasheet matches integration-circuit keywords (`typical application`, `reference design`, `recommended circuit`, etc.), the digest says so explicitly — "no application circuit found, expect to need an external reference design" — rather than just showing an empty table. AP6275S is exactly this case: its only figures are EVB-manual photos, no dedicated application circuit exists in the datasheet at all.

**Cold-read audit (2026-07-08):** had a fresh Claude instance read the README and this doc cold, with no session context, and report confusion/gaps. It verified claims before reporting them (checked `cradle_sidecar/data/altium/` actually has real files, checked `hardware/` is actually empty) rather than reacting to prose alone — a good sign the provenance/verification discipline documented here transfers to a new instance reading about it, not just the one that built it. Caught two real gaps, both fixed: `cradle_sidecar/data/altium/` (live, actively-used exports) was never reconciled against `hardware/README.md`'s existing claim that Altium data belongs in `hardware/` — now documented as two intentionally-parallel things in both READMEs. Separately, the README linked the new docs without carrying over their "partially built" status, implying a more finished system than exists — added explicit caveats. Two other points it raised (no enforcement for the write-back discipline; only one component card exists) were correctly self-assessed by that instance as expected/acceptable at this stage, not gaps needing a fix — agreed, left as-is.

### Layer 3 seeded, Layer 0.9 added (2026-07-08, agent-feedback-driven)

Got structured feedback from a fresh agent instance that read this system cold (see the cold-read audit entry above) plus a second round of feedback (external + the user's own suggestion). Both rounds converged on the same short list of highest-leverage gaps; built the ones that were cheap and already had the data available, deferred the ones with real staleness/scope-creep risk:

**Built:**
- **`cradle_sidecar/data/net-registry.md`** — Layer 3, seeded (not left as "still proposed") with 19 real cross-sheet rows from the Wireless sheet, using real Altium net names.
- **Net name map in `AP6275S.md`** — card-name-to-Altium-name reconciliation table, directly closes the `SDIO_DATA_CMD` vs `WIRELESS_SDCMD` drift that was flagged as an "agent trap" (string-matching between the two would silently fail).
- **`cradle_sidecar/tools/card_lint.py`** — checks a card for the exact structural patterns that already broke the pin-table parser twice: compressed multi-pin rows with a combined name, positional shorthand ("same as above"), missing Status. Its first version false-positived on "same instance as pins 40/41/42" (a legitimate, self-contained cross-reference) by pattern-matching too broadly on "same instance as" instead of the actual tell, which is a *positional* word like "above" — fixed and reverified against both the real card (clean) and a deliberately broken test case (all 4 issue types caught).
- **`cradle_sidecar/tools/project_refresh.py`** — one command aggregating netlist re-parse + card lint + open-items check + reachability check (via `**Wiring targets:**`) + registry validation across every card. Its first version reimplemented the orphaned/staged/pending-port classification inline instead of reusing `netlist_parse.py`'s already-correct version, and got it wrong (485 "orphaned" pins vs. the real 118) — fixed by extracting `classify_floating_nets()` as a shared function both scripts call, so the logic exists in exactly one place. Worth remembering as its own pattern, on top of the CBUCK/ABUCK one: **duplicating already-correct logic into a new script is itself a recurring failure mode**, not just "forgetting to check something."
- **`cradle_sidecar/tools/registry_check.py`** — mechanical validation of `cradle_sidecar/data/net-registry.md` against the netlist (net name present? member count?). No interpretation of intent; wired into `project_refresh.py`.
- **`**Designator:**` and `**Wiring targets:**` fields** added to component cards (starting with `AP6275S.md`) so `project_refresh.py` can auto-discover which BOM designator each card describes and which reachability checks to run, without per-card hardcoding.

**Deliberately not built, with reasoning:**
- **`AGENTS.md`/session-handoff block** — real staleness risk (a "current focus" snapshot is wrong the moment the next session changes anything) with no enforcement mechanism to keep it current, unlike the tooling above which is either regenerated fresh each run or self-verifying. Revisit if this specific gap (session-to-session context loss) turns out to matter more than it currently does.
- **`cradle_sidecar/data/components/RK3576.md` stub ahead of the Compute-SoC sheet starting** — would cut against the incremental-not-upfront principle that's already proven right for every other card. Build when that sheet actually starts, not before.
- **Netlist diff between exports, ERC message ingest** — good ideas, blocked on either more implementation complexity (diffing needs storing prior snapshots) or on data that doesn't exist yet (Altium ERC output isn't currently exported to a file at all).

### The cradle_sidecar migration (2026-07-08) — completed

User + Cursor produced a design spec for `cradle_sidecar/`: physically separating `docs/`'s three mixed roles (published narrative, live co-design state, agent manuals) into a dedicated directory, with a future localhost UI reading the same data agents use. Reviewed before any file was moved; `paths.py` was built first so the physical move would be a one-file edit.

**Completed 2026-07-08** (all via `git mv`, history preserved):
- `tools/` → `cradle_sidecar/tools/` (including new `paths.py`)
- `docs/Altium/` → `cradle_sidecar/data/altium/`
- `docs/Component Documentation/` → `cradle_sidecar/data/datasheets/`
- `docs/components/` → `cradle_sidecar/data/components/`
- `docs/net-registry.md` → `cradle_sidecar/data/net-registry.md`
- `docs/co-design-workflow.md` + `docs/workflow-cheatsheet.md` → `cradle_sidecar/`
- `docs/` now holds only the four published narrative files: `architecture.md`, `decisions-log.md`, `bom.md`, `schematic-status.md`

Verified post-move: `project_refresh.py` output identical to pre-move baseline (118 orphaned pins, 19/19 registry rows, 11/13 open items, 0/15 reachability). `paths.py` worked as designed — the move was repointing one file, not find-and-replace across every script.

**Still deferred (not part of migration):**
- `cradle_sidecar/scripts/update_github_docs.py` — publisher from sidecar data → `docs/` snapshots; not built yet
- `bom-annotations.yaml` + generated `docs/bom.md` — hand-edited `bom.md` stays as-is for now

**Prior note (pre-migration):** the diagnosis that `docs/` mixed three roles was agreed early; the full directory move was initially deferred until a working UI existed. The user later requested the move once `paths.py` de-risked it. **UI v0 shipped same day** — see Localhost UI section below.

### Localhost UI — v0 shipped (2026-07-08)

`cradle_sidecar/app/` is a co-design companion from day one of schematic work — not a post-design dashboard. v0 scope:

- **Read-only** views of `data/` (sheets, parts, component cards, net registry + mechanical checks)
- **User click → `project_refresh.py`** only; no markdown writes, no AI, no datasheet indexing
- **Open PDF** in system viewer (datasheet double-click)
- Agents continue using `cradle_sidecar/tools/` and updating `data/` directly — UI does not replace that workflow

Run: `python cradle_sidecar/app/server.py` → http://127.0.0.1:8765/

**Not in v0:** in-browser card editing, Altium sheet auto-sync, `update_github_docs`, LLM in sidebar.

## Fast orientation

`cradle_sidecar/workflow-cheatsheet.md` is the task-to-command lookup (which script for which job) — read this doc once for the reasoning/history, use the cheatsheet for day-to-day navigation. Both are linked from the repo root `README.md`.

## Concrete next steps

1. Decide the two open Layer 3 questions (registry format; SoC-pin pre-population policy) and the Layer 2 redundancy question (is a separate sheet contract still needed, or is a filtered registry view enough).
2. ~~Seed `cradle_sidecar/data/net-registry.md` with the nets already locked in from the Wireless sheet~~ Done 2026-07-08 — 19 cross-sheet rows seeded (BT UART x4, SDIO x6, `WL_REG_ON`/`BT_REG_ON`, `HOST_WAKE` signals, power rails). `LPO` intentionally omitted — sheet-local clock, not a hierarchical port; see Layer 3 section above.
3. ~~Run `cradle_sidecar/tools/datasheet_index.py` across the rest of `cradle_sidecar/data/datasheets/`~~ Done 2026-07-08 — every datasheet in the folder now has a `.tables.md` (and either `.index.md` or `.outline.md`, depending on document shape). RK806S-5 and BQ25601 datasheets aren't in the folder yet — index those once they're added.
4. Build component cards for other parts only as real design work touches them — not as an upfront project against the whole BOM. `AP6275S.md` is the template to follow (pin table with Cradle Wiring + Status columns, known gaps, external validation, open questions). The relevant `.tables.md` for each part is now a ready-made starting point for the pin table section, not a from-scratch PDF read.
5. Three files of unclear origin are sitting in `cradle_sidecar/data/datasheets/` (`AP6275S EVB.pdf`, `SOM-iMX8MM-OSM_Schematic.pdf`, `datasheet.zip`) — not touched during the cleanup pass since they may be user-added rather than session temp files. `SOM-iMX8MM-OSM_Schematic.pdf` in particular carries the same third-party confidentiality watermark as the Geniatech files that were deliberately not persisted elsewhere in this repo — worth a deliberate decision on whether to keep it checked in.
