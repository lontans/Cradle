# <PART_NUMBER> — <short description>

**Designator:** <U?>

**Wiring targets:** <target_designator>/<target_name>

Comma-separate multiple targets if needed (e.g. `U1/RK3576, U9/RK3576`). Omit this line only if the part has no signals meant to reach another IC — `cradle_sidecar/tools/project_refresh.py` uses it to run reachability checks.

**Card origin:** <Datasheet-derived | Manually authored | Mixed>

Required, so a reader (or the sidecar UI) knows at a glance whether this card came from vendor documentation or from the user filling gaps by hand. Use **Manually authored** when the datasheet was unusable (missing, scrambled text extraction, no application circuit) and the user supplied the facts directly; **Mixed** once a manually authored card later gets datasheet facts added, or vice versa. Never silently upgrade a manual card to Datasheet-derived just because it looks complete.

**Vendor:** <vendor> **Datasheet:** `cradle_sidecar/data/datasheets/<PART>.pdf` **Structural index:** `cradle_sidecar/data/datasheets/<PART>.index.md` (or `.outline.md` for TRM-style docs). If there is no usable datasheet, say so here instead (e.g. `**Datasheet:** none usable — text extraction scrambled, see Known Gaps`).

Vendor facts use provenance tags per `cradle_sidecar/co-design-workflow.md`: `[VERIFIED — source]` / `[UNVERIFIED — source]` / `[MANUAL — user, <date>]`. Use `MANUAL` for any fact supplied directly by the user rather than transcribed from a document — a confident, first-hand statement, not a lower-confidence `UNVERIFIED` one. Tag it at the fact, not just at the card level, so a later reader can tell exactly which lines are user-supplied when the card is `Mixed`.

Once this card exists, add incremental findings (a claim double-checked, a fact confirmed) via `cradle_sidecar/tools/card_note.py` (`--text`, `--tag` one of VERIFIED/UNVERIFIED/MANUAL, `--source`, `--page` -- see the script's own `--help`), or the sidecar UI's **Add a note** box — not a hand-edit. It creates and appends to a `## AI reading notes` section automatically; don't add that heading yourself.

## High-level summary

- Bullet points only — what this part does on Cradle, host interfaces, anything non-obvious.

## Power domains

| Domain | Pin(s) | Range | Cradle rail |
|---|---|---|---|
| | | | |

## Pin table

Vendor columns cite source. **Cradle wiring** = what Cradle does with the pin. **Status** = `Decided` / `Open` / `Not addressed` only — never leave blank.

One row per pin. No compressed multi-pin rows with slash-separated names. No positional shorthand ("same as above") in Cradle wiring — name the target explicitly every time.

| # | Name | Type | Vendor function | Cradle wiring | Status |
|---|---|---|---|---|---|
| | | | | | |

## Known gaps (things the vendor datasheet does not specify)

-

## External validation (secondary sources, not the primary datasheet)

Extract facts with citation; do not persist confidential source files in-repo.

-

## Net name map (card name -> real Altium name)

Add once hierarchical ports exist. Pin table keeps vendor pin names; this table maps them to real Altium net names. Sheet-local nets (clocks, RF, same-sheet loops) stay out of this table and out of `cradle_sidecar/data/net-registry.md` — see `AP6275S.md` for the pattern.

| Card name (vendor pin name) | Pin | Real Altium net name |
|---|---|---|
| | | |

## Open questions

1.
