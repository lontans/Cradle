# Quick-start digest: TF-01A Datasheet

Second pass over `datasheet_index.py`'s output, not a fresh PDF scan. Deterministic keyword triage only -- narrows where to look, doesn't explain why or what to do. Reading the flagged pins/pages and writing real integration guidance into `cradle_sidecar/data/components/<PART>.md` is still a human/Claude task, not something this script does.

## Pinout

*No pin table found in the ported tables -- check the source PDF directly, the pin table may have failed to be detected/ported (see cradle_sidecar/co-design-workflow.md for known table-detection limitations), or this document is in outline mode and pin data lives in the .outline.md instead.*

## Pins worth investigating before wiring

Rows whose vendor description matches a keyword suggesting non-trivial integration (needs an external component, internal regulator, crystal, reserved/floating, etc.) -- not a guarantee something's wrong, just worth reading closely before assuming a pin is a simple wire.

*None matched -- either a simple part, or the keyword list missed something. Worth a manual skim regardless.*

## Candidate integration pages

**No typical-application/reference-circuit figure found in this datasheet.** This is a real finding, not a null result -- expect to need an external reference design (a real shipped product using the same part) rather than a vendor-provided application circuit. See cradle_sidecar/co-design-workflow.md's External Validation convention.
