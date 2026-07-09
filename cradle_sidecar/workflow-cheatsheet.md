# Workflow cheatsheet — which script, when

Fast task-to-command lookup for navigating this repo's tooling. For *why* any of this exists, what's been tried and rejected, and the full bug/lesson history, see [`co-design-workflow.md`](co-design-workflow.md) — read that once for context, use this file for day-to-day command lookup.

## "I'm starting a session and want the current state in one shot"

```
python cradle_sidecar/tools/project_refresh.py
```

Or open the **sidecar web UI** and click **Run project refresh** (same script, read-only otherwise):

```
python cradle_sidecar/app/server.py
```

→ http://127.0.0.1:8765/ — renamed to just **Sidecar** in the tab/title (2026-07-09); the app's own name, not scoped to this one project, since the same server could front any co-design repo shaped like this one. Clicking the title always returns to **Home**, a stats dashboard (BOM/netlist/card/net-registry counts, aggregate pin-Decided/Open progress, a live session-usage timer) computed the same way — every number re-read from disk, nothing cached — so it updates whenever you click **Run project refresh** while Home is open, same as every other view.

Re-parses the netlist/BOM, lints every component card, runs `--open` plus reachability checks (when a card has `**Wiring targets:**`), and mechanically validates `cradle_sidecar/data/net-registry.md` against the netlist — one consolidated status instead of running several scripts separately. Doesn't call `datasheet_index.py`/`datasheet_quickstart.py` (those are per-new-datasheet tools, not part of a routine refresh) and doesn't write anything back anywhere — it's a status readout, not an update. Start here, then drill into whichever script's output actually needs a closer look.

## "I need to research a new component / datasheet"

```
python cradle_sidecar/tools/datasheet_index.py "cradle_sidecar/data/datasheets/<PART>.pdf"
python cradle_sidecar/tools/datasheet_quickstart.py "cradle_sidecar/data/datasheets/<PART>"
```

1. `datasheet_index.py` first — produces `<PART>.index.md` (page pointers) and `<PART>.tables.md` (pin/spec tables ported verbatim). For documents with a large embedded PDF outline (a TRM-style reference manual), it produces `<PART>.outline.md` instead — expect that on anything covering a whole SoC's register map, not a single-part datasheet.
2. `datasheet_quickstart.py` second (needs step 1's output already on disk) — produces `<PART>.quickstart.md`: the full pinout, which specific pins are keyword-flagged as needing real investigation before wiring, and which pages (if any) look like they contain a reference/application circuit. **If it reports no candidate integration pages, that's a real finding** — the datasheet likely doesn't document how to wire the part, and you should expect to need an external reference design (see `co-design-workflow.md`'s External Validation convention) rather than keep searching the same PDF.
3. Read the quickstart digest, investigate the flagged pins/pages yourself (this part is still manual — the scripts only narrow where to look, they don't explain integration).
4. Write findings into `cradle_sidecar/data/components/<PART>.md` — copy [`cradle_sidecar/data/components/_TEMPLATE.md`](components/_TEMPLATE.md) as a starting point. Required header fields: `**Designator:**`, `**Card origin:**` (`Datasheet-derived` / `Manually authored` / `Mixed`), and `**Wiring targets:** <designator>/<part_name>` if any signals reach another IC (e.g. `U1/RK3576`). Follow `AP6275S.md` for the full shape: vendor pin table with Cradle Wiring + Status columns, Net name map once hierarchical ports exist, Known Gaps, External Validation with provenance tags.
5. Run `python cradle_sidecar/tools/card_lint.py cradle_sidecar/data/components/<PART>.md` before considering the card done — catches the exact structural mistakes that have already broken the parser twice (compressed multi-pin rows with a combined name, "same as above"-style positional shorthand, missing Status values), plus a missing `**Card origin:**` header.

## "The datasheet is bad and datasheet_index.py/datasheet_quickstart.py gave me nothing"

Some vendor datasheets in this project are bad enough (no application circuit, scrambled PDF text layer, missing values entirely) that `datasheet_index.py`'s mechanical PyMuPDF text-extraction pass has nothing to give you — see AP6275S's Known Gaps and TF-01A's header (a 1-page scanned image, zero-length text layer) for two real examples. **Don't hand this straight to the user as a blank textarea.** Writing a card by hand from nothing — provenance tags, pin-table shape, the whole `_TEMPLATE.md` structure — is real friction, and it's exactly the same reading-a-datasheet work an agent already does for every other card. The right split is: **agent drafts, user reviews and fills the genuine gaps.**

1. **Agent (in a Claude Code conversation, not the sidecar server — see "why not a server-side AI button" below) reads the datasheet directly**, bypassing the mechanical extractor that already failed: open the PDF with `Read` and look at the rendered pages yourself (vision, not text-layer parsing) — this is a different, higher-effort path than `datasheet_index.py`, reserve it for exactly the cases where the mechanical pass came back empty. Supplement with a web search for the part number (reference designs, other boards using the same part) when the datasheet itself is silent on something.
2. **Write the draft card** to `cradle_sidecar/data/components/<PART>.md` (copy `_TEMPLATE.md`) with real provenance tags for everything the agent could actually determine — `[VERIFIED — <datasheet name>, visual read of scanned page]` for a direct-but-manual read (same tier as the existing "rendered+zoomed" schematic convention, since it's still primary-source, just not text-extracted), `[UNVERIFIED — web search summary]` for supplementary hits. Set `**Card origin:**` to `Datasheet-derived` if the datasheet covered everything found, or leave it for step 3 to set to `Mixed`.
3. **Leave every genuine gap as an unfilled `<placeholder>` or an entry in Known Gaps / Open questions** — do not guess, do not silently fill a blank with a plausible-sounding value. `card_lint.py` (and the sidecar editor's Lint button) now flags leftover `<...>` placeholders specifically so a half-drafted card can't quietly pass as done.
4. **User reviews in the sidecar UI**: open the sidecar (`python cradle_sidecar/app/server.py`) → **Component cards** → click the card. The card view shows the actual datasheet PDF embedded beside the rendered card (see "reviewing a card" below) — read the two side by side instead of context-switching to a separate PDF viewer. Use the **Add a note** box for anything you confirm, correct, or add (tagged `MANUAL` for your own knowledge, or `VERIFIED`/`UNVERIFIED` if you're citing the datasheet/a web source yourself) — this is the lightweight path, not the full editor. Use **Edit** (the raw-markdown editor, still there for structural changes — new pin-table rows, rewriting a section) only when a note can't express the fix; it still auto-lints and has **Next blank** for the remaining `<placeholder>` gaps, and flip `**Card origin:**` to `Mixed` once the card has both datasheet-derived and user-supplied facts.
5. Lint clean before considering it done — same check, same file, same format regardless of who wrote which line.

**Why the AI-drafting step happens in a Claude Code conversation, not as a button in the sidecar:** the sidecar server is deliberately kept free of any AI/LLM call (no API key, no cost, no latency, no error handling for a model call baked into a small local tool) — see `paths.py`'s comment and this file's own architecture. The sidecar's job is review (PDF + card side by side, add notes, lint, save), not authoring; reading a datasheet with real reasoning is still the agent/CLI-side job it always was, just now the *output* of that work becomes a draft the user reviews here instead of a wall of chat text that has to get manually retyped into a file.

**Only start from a truly blank template** (`+ New card` with no prior draft) when there's no datasheet to draft from at all — a part the user is speccing from their own knowledge, a placeholder BOM line, etc. That case is legitimately `Manually authored` from the first keystroke, not a review pass.

## "I want to add a finding to a card without opening the full editor"

The card view (**Component cards** → click a card, or select a part with a card from a sheet) embeds the datasheet PDF declared in the card's own `**Datasheet:**` header directly next to the rendered card — no external viewer, no "open file" round-trip. Two things make reviewing this side-by-side pane actually useful instead of just two panels bolted together:

- **Provenance citations are live links.** Any `[VERIFIED — ... p.12]` / `[UNVERIFIED — ... p.12]` tag rendered in the card is clickable — it jumps the embedded PDF straight to that page, so checking a claim against its source is one click, not a manual scroll.
- **The Add a note box** at the bottom of the card pane appends a single tagged, dated entry to the card's `## AI reading notes` section — pick `My own knowledge` (writes `[MANUAL — user, <date>]`) or `Verified`/`Unverified` (asks for a source citation, e.g. `AP6275S Documentation.pdf p.12`) and it's saved immediately. This is for incremental findings — "pin 5 is actually NC per rev B," "confirmed R33 is 0R" — not for restructuring the pin table; use **Edit** for that.

**The same mechanism, scripted, is available to an agent mid-conversation:**

```
python cradle_sidecar/tools/card_note.py cradle_sidecar/data/components/<PART>.md --text "..." --tag VERIFIED --source "<PART> Documentation.pdf p.12" --page 12
python cradle_sidecar/tools/card_note.py cradle_sidecar/data/components/<PART>.md --text "..." --tag MANUAL
```

This is the standard way to commit an incremental datasheet-reading finding once a card already exists — same split as every other tool here: the agent still does the actual reading/reasoning in conversation, but the write-back (exact formatting, timestamp, section placement) is this one deterministic script, not a freehand `Edit` on the file. Reserve a direct file edit for restructuring (new pin-table rows, rewriting a whole section) — a one-fact addition to an existing card should go through `card_note.py` (or the UI's Add a note box, which calls the same underlying write-back), not a hand-formatted bullet appended wherever felt right that session.

## "I need to check the current Altium state"

```
python cradle_sidecar/tools/netlist_parse.py "cradle_sidecar/data/altium/Netlist/Cradle.NET" "cradle_sidecar/data/altium/BOM/Cradle.csv" "cradle_sidecar/data/altium/Cradle"
```

Produces `Cradle.netlist-summary.md`: every net, resolved to real part names and (if the BOM's `SheetNumber` column is populated) sheet names via `sheet-map.md`. Separates genuinely-orphaned pins (no label, connects to nothing — worth reviewing) from pending-port nets (deliberately named, single-pin only because the far sheet doesn't exist yet — expected, not a problem) and known staged/standard parts (`standard-parts.md` — excluded from the review list by design).

**Always check the printed `SOURCE FRESHNESS` line before trusting a "missing/not wired" finding** — that's indistinguishable from a stale export otherwise. Re-export from Altium if in doubt, don't assume the files on disk reflect the current schematic.

## "I need to validate the net registry against the current export"

```
python cradle_sidecar/tools/registry_check.py cradle_sidecar/data/net-registry.md "cradle_sidecar/data/altium/Netlist/Cradle.NET"
```

Mechanical only: for each row in `cradle_sidecar/data/net-registry.md`, reports whether that net name exists in the netlist and how many pins are on it. Does not interpret *why* a net is missing (stale export vs. not wired yet vs. unresolved hierarchical port). Also run automatically as part of `project_refresh.py`.

## "I need to know if a component's signals are actually wired"

Two different questions, two different modes of `wiring_check.py`:

```
python cradle_sidecar/tools/wiring_check.py cradle_sidecar/data/components/<PART>.md <designator> <target_designator> <target_name> "cradle_sidecar/data/altium/Netlist/Cradle.NET"
```
"Do this part's signals meant for `<target>` (e.g. RK3576/U1) actually reach it yet?" — cross-references the card's pin table against real connectivity.

```
python cradle_sidecar/tools/wiring_check.py --open cradle_sidecar/data/components/<PART>.md <designator> "cradle_sidecar/data/altium/Netlist/Cradle.NET"
```
"Are there any pins this card marks `Open`/not-`Decided` that still have no real connection at all — regardless of what they're for?" **Use this one, not just the target-designator mode, when doing a general wiring-correctness pass** — the target-designator mode is structurally blind to same-part loops (e.g. two pins on one IC needing an external bridging component), which is exactly the class of bug that got missed the one time only the first mode was used. See `co-design-workflow.md`'s 2026-07-08 methodology-gap entry for the full story.

## File location map

| Location | What lives there |
|---|---|
| `cradle_sidecar/data/datasheets/` | Raw vendor PDF datasheets, plus generated `.index.md`/`.tables.md`/`.outline.md`/`.quickstart.md` per part |
| `cradle_sidecar/data/components/` | Curated component cards (`_TEMPLATE.md` to copy for new ones) |
| `cradle_sidecar/data/altium/Netlist/`, `cradle_sidecar/data/altium/BOM/` | Real, periodically re-exported Altium netlist + BOM — check freshness before trusting |
| `cradle_sidecar/data/altium/sheet-map.md` | Sheet number → sheet name lookup |
| `cradle_sidecar/data/altium/standard-parts.md` | User-maintained list of designators held as generic staged stock, not yet functionally placed |
| `cradle_sidecar/data/altium/*.netlist-summary.md` | Generated output of `netlist_parse.py` |
| `cradle_sidecar/data/net-registry.md` | Cross-sheet net tracking (Layer 3) — seeded from Wireless, not yet covering every sheet, still hand-maintained (not auto-generated) |
| `cradle_sidecar/tools/` | All the scripts referenced above. `paths.py` centralizes every path they use |
| `docs/decisions-log.md`, `docs/architecture.md`, `docs/bom.md`, `docs/schematic-status.md` | Published narrative docs, hand-owned, unrelated to this tooling system — still the source of truth for locked decisions and overall board status |

## The one discipline that makes all of this worth maintaining

Every script above only *narrows where to look* — none of them reason about what a pin does for Cradle specifically, or explain why something matters. That's still a human/Claude-in-conversation task every time. The system only stays valuable if the outcome of that reasoning gets written back into the relevant file (a component card, `standard-parts.md`, `sheet-map.md`) as part of finishing the task — not left to live only in chat history. Skipping that write-back doesn't break anything immediately; it just means the next session re-derives the same fact from scratch, possibly getting a different answer next time.
