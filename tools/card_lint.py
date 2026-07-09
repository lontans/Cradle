"""
Component card lint.

Checks a docs/components/<PART>.md file for the specific structural
patterns that have already broken wiring_check.py's pin-table parser twice
this project: compressed multi-pin rows with a combined name (can't be
matched back to individual pins), "same as above"-style shorthand (invisible
to substring matching against a target part name), and missing Status
values (an Open/Decided/Not-addressed judgment silently missing reads as
neither, which is worse than being explicit).

This is a lint, not a rewrite -- it flags lines, it doesn't fix them. The
underlying lesson (docs/co-design-workflow.md, 2026-07-08): a card written
for human readability (compressed ranges, backreferences) directly works
against the card's stated purpose of being machine-parseable. Every finding
here is exactly that tension showing up again in a new row.

Usage:
    python card_lint.py <component_card.md>
"""

import re
import sys
from pathlib import Path

PIN_ROW_RE = re.compile(
    r"^\|\s*([\d,\-]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*$"
)

# The actual tell of non-self-contained shorthand is a *positional* reference
# ("above", "below", "previous row") -- that's what breaks when text is
# matched/read out of row order. "Same instance as pins 40/41/42" is fine:
# it names specifics, doesn't depend on position, and reads correctly on its
# own. Originally matched "same instance as" too broadly and false-positived
# on exactly that legitimate pattern -- see co-design-workflow.md.
SHORTHAND_RE = re.compile(r"\b(above|below|previous row|preceding row|see prior)\b", re.IGNORECASE)
VALID_STATUS_RE = re.compile(r"^(Decided|Open|Not addressed)\b")


def lint_card(card_path):
    text = Path(card_path).read_text(encoding="utf-8")
    findings = []

    if not re.search(r"^\*\*Designator:\*\*\s*\S+", text, re.MULTILINE):
        findings.append(("header", 0, "No '**Designator:** <ref>' line found -- tools/project_refresh.py needs this to auto-discover which BOM designator this card describes."))

    in_table = False
    for i, line in enumerate(text.split("\n"), start=1):
        if line.strip().startswith("| #"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.strip().startswith("|"):
            in_table = False
            continue
        if set(line.strip()) <= set("|-: "):
            continue

        m = PIN_ROW_RE.match(line)
        if not m:
            continue
        pin_field, name, io_type, vendor_fn, cradle_wiring, status = m.groups()

        is_range = "-" in pin_field or "," in pin_field
        is_combined_name = "/" in name and not name.strip().startswith("`") is False and re.search(r"`[^`]+/[^`]+`|\w+/\w+", name)
        if is_range and is_combined_name:
            findings.append(("compressed-row", i, f"Pin field '{pin_field}' covers multiple pins but name '{name.strip()}' looks like a combined/slash-separated name -- split into one row per pin (see co-design-workflow.md's SDIO_DATA_3/2/0/1 lesson)."))

        if SHORTHAND_RE.search(cradle_wiring):
            findings.append(("shorthand", i, f"Pin {pin_field}: Cradle Wiring text uses 'same as above'-style shorthand -- invisible to substring matching, make self-contained (see co-design-workflow.md's BT_UART_RXD/RTS_N/CTS_N lesson)."))

        if not status.strip():
            findings.append(("missing-status", i, f"Pin {pin_field}: Status column is empty -- should be Decided/Open/Not addressed, not blank."))
        elif not VALID_STATUS_RE.match(status.strip()):
            findings.append(("odd-status", i, f"Pin {pin_field}: Status '{status.strip()}' doesn't start with Decided/Open/Not addressed -- check it's not a typo."))

    return findings


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python card_lint.py <component_card.md>")
        sys.exit(1)

    findings = lint_card(sys.argv[1])
    if not findings:
        print(f"{sys.argv[1]}: no issues found.")
    else:
        print(f"{sys.argv[1]}: {len(findings)} finding(s)")
        for kind, line, msg in findings:
            loc = f"line {line}" if line else "header"
            print(f"  [{kind}] {loc}: {msg}")
