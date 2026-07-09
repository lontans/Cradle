"""
Datasheet structural indexer + mechanical table porter.

Two things happen here, and they are deliberately different in kind:

1. FLAGGING (light, rule-based, applies to every page): classify tables and
   pages using deterministic heuristics -- PyMuPDF's layout-based table
   detector plus regex (figure/table captions, reference-designator density).
   This is pattern matching on shape, not semantic understanding. No LLM
   involved anywhere in this file.

2. PORTING (mechanical, applies only to high-confidence tabular content):
   when a table is classified as a pin table or a spec/parameter table --
   the two categories that are already fully structured data, not prose --
   its rows are dumped verbatim into a companion `.tables.md` file as clean
   markdown. This is formatting, not interpretation: the cells are copied
   as PyMuPDF extracted them, nothing is summarized or reworded.

Everything else (figures, schematics, uncategorized tables, narrative text)
stays pointer-only in the index -- page number and a short preview, nothing
transcribed. Actual reading and reasoning about what any of this *means* for
Cradle -- known gaps, Cradle-specific wiring, cross-referencing other
sources -- still happens in-conversation and gets written into
`docs/components/<PART>.md` by hand. This script never touches that file.

Usage:
    python datasheet_index.py "path/to/datasheet.pdf" [output_prefix]

Writes <output_prefix>.index.md (all flagged pages, pointers only) and
<output_prefix>.tables.md (verbatim pin/spec tables, ready to review and
fold into a component card).
"""

import re
import sys
from pathlib import Path

import fitz

PIN_TABLE_KEYWORDS = {"pin", "ball", "signal", "gpio", "no", "no.", "number", "name"}
SPEC_TABLE_KEYWORDS = {"parameter", "min", "max", "typ", "unit", "symbol", "rating", "condition"}
FIGURE_CAPTION_RE = re.compile(r"\b(Figure|Fig\.?)\s*\d+", re.IGNORECASE)
REFDES_RE = re.compile(r"\b(?:R|C|L|U|Y|J|Q|D|FB|SW|TP)\d{1,4}\b")
REFDES_DENSITY_THRESHOLD = 8
MIN_PIN_TABLE_ROWS = 5
PORTABLE_TYPES = {"pin table", "spec/parameter table"}
TOC_MODE_THRESHOLD = 20  # embedded outline entries needed to prefer TOC over page-scan
UNDERSCORE_LINE_RE = re.compile(r"^[_ ]+$")


IDENTIFIER_LIKE_MAX_WORDS = 6


def fix_underscore_artifacts(text):
    """PyMuPDF (and PDF text extraction generally) frequently renders a literal
    underscore in an identifier as a separate line instead of inline -- e.g.
    'WL_ANT0' extracts as 'WL ANT0\\n_', 'SDIO_DATA_CMD' as 'SDIO DATA CMD\\n_ _',
    and sometimes a single identifier gets split entirely across three lines
    ('GAIN_SLOT' as 'GAIN\\n_\\nSLOT'). Left alone this corrupts identifiers and
    breaks row-count-based table parsing (see unmerge_stacked_rows).

    This only fires on short, identifier-shaped lines (<=6 words) -- a
    multi-word prose description can *also* end in a stray '_' line when an
    identifier appears mid-sentence (e.g. '...GAIN SLOT are both used for
    channel selection (Table 7).\\n_'), and blindly replacing every space in
    that whole sentence with underscores would corrupt real prose. In that
    case the stray line is dropped without touching the preceding text --
    losing one underscore character is a far smaller, more visible defect
    than silently mangling a sentence.
    """
    if not text:
        return text
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Pattern: word <underscore-only line> word -- e.g. 'GAIN\n_\nSLOT'
        if (i + 2 < len(lines) and lines[i + 1] == "_"
                and not UNDERSCORE_LINE_RE.match(lines[i + 2])
                and len(line.split()) <= IDENTIFIER_LIKE_MAX_WORDS
                and len(lines[i + 2].split()) <= IDENTIFIER_LIKE_MAX_WORDS):
            out.append(line + "_" + lines[i + 2])
            i += 3
            continue
        # Pattern: word(s) <underscore/space-only line> -- e.g. 'WL ANT0\n_'
        if i + 1 < len(lines) and "_" in lines[i + 1] and UNDERSCORE_LINE_RE.match(lines[i + 1]):
            if len(line.split()) <= IDENTIFIER_LIKE_MAX_WORDS:
                out.append(line.replace(" ", "_"))
            else:
                out.append(line)  # prose: drop the stray underscore line, don't touch the text
            i += 2
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def clean_table(rows):
    """Apply fix_underscore_artifacts to every cell. Always run before
    classification/unmerge/porting -- see fix_underscore_artifacts docstring."""
    return [[fix_underscore_artifacts(str(c)) if c else c for c in row] for row in rows]


def unmerge_stacked_rows(rows):
    """Some small-pin-count datasheets render an entire pin table as one data row
    per column, with each cell holding newline-separated values for every pin
    (e.g. cell 0 = 'A1\\nA2\\nB1...', cell 1 = 'PDM_DAT\\nPDM_CLK\\nSDATA...') instead
    of one row per pin. find_tables() sees this as a 2-row table (header + one
    merged row), which fails both the pin-table row-count check and, if ported
    as-is, would flatten to an unreadable jumble (newlines -> spaces, alignment
    lost). Detected by: every cell in a data row splits into the same number of
    lines. Split back into one logical row per line when found."""
    if len(rows) < 2:
        return rows
    header = rows[0]
    out = [header]
    for row in rows[1:]:
        cells = list(row) + [""] * (len(header) - len(row))
        cells = cells[:len(header)]
        line_counts = {len(str(c or "").split("\n")) for c in cells if c}
        if len(line_counts) == 1 and line_counts != {1}:
            n = line_counts.pop()
            split_cells = [str(c or "").split("\n") + [""] * n for c in cells]
            for j in range(n):
                out.append([split_cells[col][j] for col in range(len(header))])
        else:
            out.append(row)
    return out


def classify_table(header_row, row_count):
    header_text = " ".join(str(c or "") for c in header_row).lower()
    pin_hits = sum(1 for kw in PIN_TABLE_KEYWORDS if kw in header_text)
    spec_hits = sum(1 for kw in SPEC_TABLE_KEYWORDS if kw in header_text)
    if pin_hits >= 2 and row_count >= MIN_PIN_TABLE_ROWS:
        return "pin table"
    if spec_hits >= 2:
        return "spec/parameter table"
    return "table (uncategorized)"


def rows_to_markdown(rows):
    """Verbatim cell dump as a markdown table. No reformatting of content, just layout."""
    if not rows:
        return ""
    header = [str(c or "").replace("\n", " ").strip() for c in rows[0]]
    lines = ["| " + " | ".join(c.replace("|", "\\|") for c in header) + " |",
             "|" + "|".join(["---"] * len(header)) + "|"]
    for row in rows[1:]:
        cells = list(row) + [""] * (len(header) - len(row))
        cells = [str(c or "").replace("\n", " ").replace("|", "\\|").strip() for c in cells[:len(header)]]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_outline_md(pdf_path, toc, out_path):
    """For documents with a rich embedded outline (large reference manuals, TRMs):
    the vendor's own bookmark tree is a better index than a page-by-page table
    scan would be -- it's already curated at the right granularity (peripheral/
    section, not per-register), so a table scan here would mostly produce
    thousands of near-duplicate 'uncategorized register table' rows instead of
    anything useful. Used instead of write_index_md's page-scan when the PDF has
    more than TOC_MODE_THRESHOLD outline entries."""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Datasheet outline index: {Path(pdf_path).name}\n\n")
        f.write(
            "This document has a rich embedded PDF outline (vendor-authored table "
            "of contents), so that's used as the index instead of a page-by-page "
            "table scan -- a table scan over a reference manual this size mostly "
            "finds thousands of near-identical register/bitfield tables, which "
            "isn't a useful index at any granularity finer than 'which section'. "
            "Drill into a specific section on demand (render/read those pages) "
            "when a real design question needs a specific register, and write "
            "findings into `docs/components/<PART>.md`, not here.\n\n"
        )
        f.write(f"Total outline entries: {len(toc)}.\n\n")
        f.write("| Level | Section | Page |\n")
        f.write("|---|---|---|\n")
        for level, title, page in toc:
            indent = "&nbsp;&nbsp;" * (level - 1)
            title_escaped = title.replace("|", "\\|")
            f.write(f"| {level} | {indent}{title_escaped} | {page} |\n")


def index_pdf(pdf_path, toc_mode=False):
    """toc_mode=True: still scan for portable (pin/spec) tables to port, but skip
    logging uncategorized tables, figure captions, and refdes-density hits to the
    index -- in a document with a rich outline, those would flood the index with
    thousands of low-value entries (see write_outline_md) instead of navigation
    the outline already provides for free."""
    doc = fitz.open(pdf_path)
    index_rows = []
    ported_tables = []
    narrative_only_pages = 0
    last_portable = None  # most recent portable-table entry, for cross-page stitching

    for i, page in enumerate(doc):
        page_num = i + 1
        text = page.get_text() or ""
        page_hits = 0

        try:
            tabs = page.find_tables()
            for t in tabs.tables:
                extracted = t.extract()
                if not extracted:
                    continue
                extracted = clean_table(extracted)
                extracted = unmerge_stacked_rows(extracted)
                header = extracted[0]
                kind = classify_table(header, len(extracted))

                # Continuation heuristic: an unheaded table on the page immediately
                # after a portable table, with the same column count, is treated as
                # more rows of that table rather than a new one. Vendor PDFs don't
                # repeat the header row on continuation pages, so find_tables() would
                # otherwise misread the first data row as a header and this table
                # would silently fail classification.
                if (kind == "table (uncategorized)" and last_portable is not None
                        and last_portable["end_page"] == page_num - 1
                        and len(header) == last_portable["col_count"]):
                    last_portable["rows"].extend(extracted)
                    last_portable["end_page"] = page_num
                    page_hits += 1
                    continue

                if kind in PORTABLE_TYPES:
                    preview = " | ".join(str(c or "") for c in header)[:80]
                    index_rows.append({
                        "page": page_num, "type": kind,
                        "preview": preview, "detail": f"{len(extracted)} rows",
                    })
                    entry = {
                        "start_page": page_num, "end_page": page_num, "type": kind,
                        "rows": extracted, "col_count": len(header),
                    }
                    ported_tables.append(entry)
                    last_portable = entry
                else:
                    last_portable = None
                    if not toc_mode:
                        preview = " | ".join(str(c or "") for c in header)[:80]
                        index_rows.append({
                            "page": page_num, "type": kind,
                            "preview": preview, "detail": f"{len(extracted)} rows",
                        })
                page_hits += 1
        except Exception:
            pass

        if not toc_mode:
            seen_captions = set()
            for m in FIGURE_CAPTION_RE.finditer(text):
                line_start = text.rfind("\n", 0, m.start()) + 1
                line_end = text.find("\n", m.start())
                line = text[line_start:line_end if line_end != -1 else m.start() + 80].strip()
                if line and line not in seen_captions:
                    seen_captions.add(line)
                    index_rows.append({
                        "page": page_num, "type": "figure/diagram",
                        "preview": line[:80], "detail": "",
                    })
                    page_hits += 1

            refdes_hits = set(REFDES_RE.findall(text))
            if len(refdes_hits) >= REFDES_DENSITY_THRESHOLD:
                index_rows.append({
                    "page": page_num, "type": "schematic/BOM-dense",
                    "preview": f"{len(refdes_hits)} unique reference designators", "detail": "",
                })
                page_hits += 1

        if page_hits == 0 and text.strip():
            narrative_only_pages += 1

    return index_rows, ported_tables, len(doc), narrative_only_pages


def write_index_md(pdf_path, rows, total_pages, narrative_pages, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Datasheet structural index: {Path(pdf_path).name}\n\n")
        f.write(
            "Auto-generated. Deterministic structural detection only (PyMuPDF table "
            "detector + regex) -- no LLM involved, no content interpretation. Page "
            "numbers are 1-indexed PDF pages, not printed page numbers. Pin/spec "
            "tables are additionally ported verbatim to the companion `.tables.md` "
            "file. Everything else is a pointer, not a transcription: open the page "
            "when a real design question needs it, and write findings into "
            "`docs/components/<PART>.md`, not here.\n\n"
        )
        f.write(f"Total pages: {total_pages}. Narrative-only (no flagged structure): {narrative_pages}.\n\n")
        f.write("| Page | Detected type | Preview | Detail | Status |\n")
        f.write("|---|---|---|---|---|\n")
        for r in sorted(rows, key=lambda r: r["page"]):
            preview = r["preview"].replace("|", "\\|")
            status = "ported, see .tables.md" if r["type"] in PORTABLE_TYPES else "not yet needed"
            f.write(f"| {r['page']} | {r['type']} | {preview} | {r['detail']} | {status} |\n")


def write_tables_md(pdf_path, ported_tables, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Ported tables: {Path(pdf_path).name}\n\n")
        f.write(
            "Mechanically extracted pin tables and spec/parameter tables -- cell "
            "contents are verbatim from the PDF, not reworded or interpreted. "
            "Review before trusting (table detection can misparse merged cells or "
            "footnote markers) and fold the relevant parts into "
            "`docs/components/<PART>.md` by hand, including the Cradle Wiring and "
            "Status columns that only a real design decision can fill in.\n\n"
        )
        if not ported_tables:
            f.write("No pin or spec/parameter tables detected.\n")
            return
        for t in ported_tables:
            page_label = (f"Page {t['start_page']}" if t["start_page"] == t["end_page"]
                          else f"Pages {t['start_page']}-{t['end_page']} (stitched)")
            f.write(f"## {page_label} -- {t['type']}\n\n")
            f.write(rows_to_markdown(t["rows"]))
            f.write("\n\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python datasheet_index.py "path/to/datasheet.pdf" [output_prefix]')
        sys.exit(1)

    pdf_path = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else str(Path(pdf_path).with_suffix(""))

    toc = fitz.open(pdf_path).get_toc()
    toc_mode = len(toc) >= TOC_MODE_THRESHOLD

    index_rows, ported_tables, total_pages, narrative_pages = index_pdf(pdf_path, toc_mode=toc_mode)
    write_tables_md(pdf_path, ported_tables, prefix + ".tables.md")
    print(f"Ported {len(ported_tables)} pin/spec tables -> {prefix}.tables.md")

    if toc_mode:
        write_outline_md(pdf_path, toc, prefix + ".outline.md")
        print(
            f"Rich embedded outline detected ({len(toc)} entries) -- used outline "
            f"instead of page-scan -> {prefix}.outline.md"
        )
    else:
        write_index_md(pdf_path, index_rows, total_pages, narrative_pages, prefix + ".index.md")
        print(
            f"Indexed {total_pages} pages ({narrative_pages} narrative-only), "
            f"{len(index_rows)} flagged entries -> {prefix}.index.md"
        )
