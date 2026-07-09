"""
Datasheet quick-start digest.

Second pass over datasheet_index.py's output (NOT a fresh PDF scan) -- takes
the already-generated <prefix>.tables.md and <prefix>.index.md and produces
one consolidated "start here" file for bringing up a new component: the
pinout table, which specific pins are worth investigating before wiring
(keyword-flagged), and which pages of the datasheet probably explain how to
actually integrate it.

Still deterministic keyword triage only -- no LLM reasoning anywhere in this
script. It narrows where to look; it does not explain why a pin is flagged
or what the integration should be. Reading the flagged pins/pages and
writing the actual integration guidance into a component card
(cradle_sidecar/data/components/<PART>.md) is still a human/Claude-in-conversation task --
see cradle_sidecar/co-design-workflow.md and cradle_sidecar/workflow-cheatsheet.md.

Validated against a real case before being trusted: run cold against
AP6275S's already-ported pin table, the keyword scan flagged
CBUCK_0P9/CSR_VLX/ASR_VLX/ABUCK_1P12 ("Internal ... generation pin") on the
first pass -- the same gap that took two external reference schematics to
resolve manually earlier in that investigation.

Usage:
    python datasheet_quickstart.py <prefix>
    (expects <prefix>.tables.md and <prefix>.index.md/.outline.md to already
    exist -- run datasheet_index.py on the source PDF first if they don't)
"""

import re
import sys
from pathlib import Path

PIN_FLAG_KEYWORDS = re.compile(
    r"\b(internal|external|generation|regulat|crystal|oscillat|reserved|floating|do not|don.t connect)\b",
    re.IGNORECASE,
)
INTEGRATION_PAGE_KEYWORDS = re.compile(
    r"typical application|reference (design|circuit|schematic)|recommended (circuit|application)|"
    r"evaluation board|interface circuit|application circuit|hardware setup",
    re.IGNORECASE,
)


def extract_pin_table(tables_md_path):
    """Returns the markdown pin table block from a .tables.md file (may
    span multiple ported tables if the pin table was split across pages
    before stitching, or if there's more than one pin table section --
    concatenates all of them), or None if no pin table section exists."""
    text = Path(tables_md_path).read_text(encoding="utf-8")
    blocks = re.findall(r"^## .*-- pin table\s*\n\n(.*?)(?=\n## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not blocks:
        return None
    return "\n\n".join(b.strip() for b in blocks)


def flag_pins(pin_table_block):
    if not pin_table_block:
        return []
    flagged = []
    for line in pin_table_block.split("\n"):
        if not line.startswith("|") or set(line.strip()) <= set("|-: "):
            continue
        if PIN_FLAG_KEYWORDS.search(line):
            flagged.append(line)
    return flagged


def find_integration_pages(index_md_path):
    """Scan a .index.md for figure/diagram rows whose preview text suggests
    an application/integration circuit. Returns None (not []) if no index
    exists at all (e.g. outline-mode documents don't produce one) so the
    caller can distinguish 'checked, found nothing' from 'nothing to
    check'."""
    if not Path(index_md_path).exists():
        return None
    text = Path(index_md_path).read_text(encoding="utf-8")
    candidates = []
    for line in text.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        page, kind, preview = cells[0], cells[1], cells[2]
        if kind == "figure/diagram" and INTEGRATION_PAGE_KEYWORDS.search(preview):
            candidates.append((page, preview))
    return candidates


def write_quickstart(prefix, pin_table_block, flagged, integration_pages, out_path):
    name = Path(prefix).name
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Quick-start digest: {name}\n\n")
        f.write(
            "Second pass over `datasheet_index.py`'s output, not a fresh PDF scan. "
            "Deterministic keyword triage only -- narrows where to look, doesn't "
            "explain why or what to do. Reading the flagged pins/pages and writing "
            "real integration guidance into `cradle_sidecar/data/components/<PART>.md` is still a "
            "human/Claude task, not something this script does.\n\n"
        )

        f.write("## Pinout\n\n")
        if pin_table_block:
            f.write(pin_table_block + "\n\n")
        else:
            f.write(
                "*No pin table found in the ported tables -- check the source PDF "
                "directly, the pin table may have failed to be detected/ported "
                "(see cradle_sidecar/co-design-workflow.md for known table-detection "
                "limitations), or this document is in outline mode and pin data "
                "lives in the .outline.md instead.*\n\n"
            )

        f.write("## Pins worth investigating before wiring\n\n")
        f.write(
            "Rows whose vendor description matches a keyword suggesting non-trivial "
            "integration (needs an external component, internal regulator, crystal, "
            "reserved/floating, etc.) -- not a guarantee something's wrong, just "
            "worth reading closely before assuming a pin is a simple wire.\n\n"
        )
        if flagged:
            for line in flagged:
                f.write(line + "\n")
            f.write("\n")
        else:
            f.write("*None matched -- either a simple part, or the keyword list missed something. Worth a manual skim regardless.*\n\n")

        f.write("## Candidate integration pages\n\n")
        if integration_pages is None:
            f.write(
                "*No `.index.md` found for this document -- it's likely in outline "
                "mode (large embedded PDF outline, e.g. a TRM). Check the "
                "`.outline.md` for section titles like \"Application\" or "
                "\"Reference Design\" instead.*\n"
            )
        elif integration_pages:
            f.write("| Page | Caption |\n|---|---|\n")
            for page, preview in integration_pages:
                f.write(f"| {page} | {preview} |\n")
        else:
            f.write(
                "**No typical-application/reference-circuit figure found in this "
                "datasheet.** This is a real finding, not a null result -- expect "
                "to need an external reference design (a real shipped product "
                "using the same part) rather than a vendor-provided application "
                "circuit. See cradle_sidecar/co-design-workflow.md's External Validation "
                "convention.\n"
            )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cradle_sidecar/tools/datasheet_quickstart.py <prefix>")
        print("  (expects <prefix>.tables.md to already exist -- run datasheet_index.py first)")
        sys.exit(1)

    prefix = sys.argv[1]
    tables_path = prefix + ".tables.md"
    index_path = prefix + ".index.md"

    if not Path(tables_path).exists():
        print(f"Missing {tables_path} -- run datasheet_index.py on the source PDF first.")
        sys.exit(1)

    pin_table_block = extract_pin_table(tables_path)
    flagged = flag_pins(pin_table_block)
    integration_pages = find_integration_pages(index_path)

    out_path = prefix + ".quickstart.md"
    write_quickstart(prefix, pin_table_block, flagged, integration_pages, out_path)

    print(f"Pin table: {'found' if pin_table_block else 'NOT FOUND'}")
    print(f"Flagged pins: {len(flagged)}")
    print(f"Candidate integration pages: {'n/a (outline mode)' if integration_pages is None else len(integration_pages)}")
    print(f"-> {out_path}")
