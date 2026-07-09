"""
Component card note — deterministic, single-purpose writer for a card's
"## AI reading notes" section.

Same split as every other layer in this project (netlist_parse.py,
registry_check.py): reasoning about a datasheet -- what a pin does, whether
a claim holds up, cross-checking a page against a web search -- is still a
human/agent-in-conversation job. This script is only the mechanical
write-back step, so the note's format never depends on how carefully it was
typed by hand this time. An agent should call this after doing the reading,
not hand-edit the file's Notes section directly.

Usage:
    python cradle_sidecar/tools/card_note.py <card.md> --text "..." --tag VERIFIED --source "AP6275S Documentation.pdf p.12" [--page 12]
    python cradle_sidecar/tools/card_note.py <card.md> --text "..." --tag UNVERIFIED --source "web search, vendor forum thread"
    python cradle_sidecar/tools/card_note.py <card.md> --text "..." --tag MANUAL [--page 12]
"""

import argparse
import datetime
import sys
from pathlib import Path

NOTES_HEADING = "## AI reading notes"
VALID_TAGS = ("VERIFIED", "UNVERIFIED", "MANUAL")


def format_note(text, tag, source=None, page=None, today=None):
    today = today or datetime.date.today().isoformat()
    if tag == "MANUAL":
        prov = f"[MANUAL — user, {today}]"
    else:
        prov = f"[{tag} — {source}]"
    page_prefix = f"p.{page}: " if page else ""
    return f"- **{today}** {page_prefix}{text.strip()} {prov}"


def append_note(card_text, text, tag, source=None, page=None):
    """Returns the updated card text with one new note appended to the
    Notes section (created at end-of-file if this is the card's first
    note). Always appends -- no attempt to merge with or replace an
    existing note, so the section reads as a chronological log, same as
    decisions-log.md at the project level."""
    if tag not in VALID_TAGS:
        raise ValueError(f"tag must be one of {VALID_TAGS}, got {tag!r}")
    if tag != "MANUAL" and not source:
        raise ValueError(f"--source is required for tag={tag} (MANUAL is the only tag that can omit it)")

    entry = format_note(text, tag, source, page)
    lines = card_text.split("\n")
    heading_idx = next((i for i, l in enumerate(lines) if l.strip() == NOTES_HEADING), None)

    if heading_idx is None:
        sep = "" if card_text.endswith("\n\n") else ("\n" if card_text.endswith("\n") else "\n\n")
        return card_text + sep + f"{NOTES_HEADING}\n\n{entry}\n"

    end_idx = len(lines)
    for i in range(heading_idx + 1, len(lines)):
        if lines[i].startswith("## "):
            end_idx = i
            break
    section = lines[:end_idx]
    while section and section[-1].strip() == "":
        section.pop()
    section.append(entry)
    section.append("")
    return "\n".join(section + lines[end_idx:])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("card", help="Path to the component card .md file")
    ap.add_argument("--text", required=True, help="The note text (already-reasoned finding, not raw datasheet dump)")
    ap.add_argument("--tag", required=True, choices=VALID_TAGS)
    ap.add_argument("--source", help="Citation, e.g. 'AP6275S Documentation.pdf p.12' -- required for VERIFIED/UNVERIFIED")
    ap.add_argument("--page", type=int, help="Datasheet page number, if applicable")
    args = ap.parse_args()

    path = Path(args.card)
    if not path.exists():
        print(f"error: {args.card} does not exist", file=sys.stderr)
        sys.exit(1)

    try:
        new_text = append_note(path.read_text(encoding="utf-8"), args.text, args.tag, args.source, args.page)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    path.write_text(new_text, encoding="utf-8")
    print(f"Appended {args.tag} note to {args.card}")


if __name__ == "__main__":
    main()
