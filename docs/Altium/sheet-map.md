# Altium sheet number map

Sheet numbers as they appear in the BOM's `SheetNumber` column (added 2026-07-08) — maps to actual sheet names in the Altium project.

| # | Sheet |
|---|---|
| 1 | Cradle (top-level/block-diagram sheet) |
| 2 | Cradle_Power_Charging |
| 3 | Cradle_Power_PMIC |
| 4 | Cradle_Compute_SOC |
| 5 | Cradle_Compute_Memory |
| 6 | Cradle_Wireless |
| 7 | Cradle_Storage |
| 8 | Cradle_Interfaces |
| 9 | Cradle_Audio |

**A real quirk, not a bug, worth understanding before trusting this column:** for a BOM row listing a single designator, `SheetNumber` is exact. For a row grouping multiple designators that share one part value (the common case for generic passives — see `standard-parts.md`), `SheetNumber` is a **deduplicated set of every sheet that value touches anywhere**, not a per-designator breakdown. E.g. the 0.1uF cap group (`C2, C10, C15, C18, ...` — 18 designators) shows `SheetNumber = "2, 1, 3, 9, 6"` (5 numbers) — there is no way to tell which specific instance is on which specific sheet from this column alone when a row is grouped like that.

One useful pattern that falls out of this: **Sheet 1 appearing in a grouped row's sheet list very often means "at least one instance of this value is still sitting unplaced on the top-level sheet"** — i.e. it's corroborating evidence for `standard-parts.md`, not a contradiction of it. Cross-check the two when in doubt.
