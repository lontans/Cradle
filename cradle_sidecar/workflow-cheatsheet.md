# Workflow cheatsheet — which script, when

Fast task-to-command lookup for navigating this repo's tooling. For *why* any of this exists, what's been tried and rejected, and the full bug/lesson history, see [`co-design-workflow.md`](co-design-workflow.md) — read that once for context, use this file for day-to-day command lookup.

## "I'm starting a session and want the current state in one shot"

```
python cradle_sidecar/tools/project_refresh.py
```

Re-parses the netlist/BOM, lints every component card, runs `--open` plus reachability checks (when a card has `**Wiring targets:**`), and mechanically validates `cradle_sidecar/data/net-registry.md` against the netlist — one consolidated status instead of running several scripts separately. Doesn't call `datasheet_index.py`/`datasheet_quickstart.py` (those are per-new-datasheet tools, not part of a routine refresh) and doesn't write anything back anywhere — it's a status readout, not an update. Start here, then drill into whichever script's output actually needs a closer look.

## "I need to research a new component / datasheet"

```
python cradle_sidecar/tools/datasheet_index.py "cradle_sidecar/data/datasheets/<PART>.pdf"
python cradle_sidecar/tools/datasheet_quickstart.py "cradle_sidecar/data/datasheets/<PART>"
```

1. `datasheet_index.py` first — produces `<PART>.index.md` (page pointers) and `<PART>.tables.md` (pin/spec tables ported verbatim). For documents with a large embedded PDF outline (a TRM-style reference manual), it produces `<PART>.outline.md` instead — expect that on anything covering a whole SoC's register map, not a single-part datasheet.
2. `datasheet_quickstart.py` second (needs step 1's output already on disk) — produces `<PART>.quickstart.md`: the full pinout, which specific pins are keyword-flagged as needing real investigation before wiring, and which pages (if any) look like they contain a reference/application circuit. **If it reports no candidate integration pages, that's a real finding** — the datasheet likely doesn't document how to wire the part, and you should expect to need an external reference design (see `co-design-workflow.md`'s External Validation convention) rather than keep searching the same PDF.
3. Read the quickstart digest, investigate the flagged pins/pages yourself (this part is still manual — the scripts only narrow where to look, they don't explain integration).
4. Write findings into `cradle_sidecar/data/components/<PART>.md` — copy [`cradle_sidecar/data/components/_TEMPLATE.md`](components/_TEMPLATE.md) as a starting point. Required header fields: `**Designator:**`, and `**Wiring targets:** <designator>/<part_name>` if any signals reach another IC (e.g. `U1/RK3576`). Follow `AP6275S.md` for the full shape: vendor pin table with Cradle Wiring + Status columns, Net name map once hierarchical ports exist, Known Gaps, External Validation with provenance tags.
5. Run `python cradle_sidecar/tools/card_lint.py cradle_sidecar/data/components/<PART>.md` before considering the card done — catches the exact structural mistakes that have already broken the parser twice (compressed multi-pin rows with a combined name, "same as above"-style positional shorthand, missing Status values).

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
