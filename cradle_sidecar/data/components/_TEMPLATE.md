# <PART_NUMBER> — <short description>

**Designator:** <U?>

**Wiring targets:** <target_designator>/<target_name>

Comma-separate multiple targets if needed (e.g. `U1/RK3576, U9/RK3576`). Omit this line only if the part has no signals meant to reach another IC — `cradle_sidecar/tools/project_refresh.py` uses it to run reachability checks.

**Vendor:** <vendor> **Datasheet:** `cradle_sidecar/data/datasheets/<PART>.pdf` **Structural index:** `cradle_sidecar/data/datasheets/<PART>.index.md` (or `.outline.md` for TRM-style docs).

Vendor facts use provenance tags per `cradle_sidecar/co-design-workflow.md`: `[VERIFIED — source]` / `[UNVERIFIED — source]`.

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
