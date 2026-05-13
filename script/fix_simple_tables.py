"""
Convert pandoc "simple table" format to GFM pipe tables.

Two patterns handled:

  TWO-COLUMN:
    -----------------------------------------------
    Header1              Header2
    -------------------- --------------------------
    Row1Col1             Row1Col2

    Row2Col1             Row2Col2
    -----------------------------------------------

  SINGLE-COLUMN (list-style):
    -----------------------------------------------
    Header
    -----------------------------------------------
    Row1

    Row2
    -----------------------------------------------
"""

import re
import sys
from pathlib import Path

DASH_LINE = re.compile(r'^( {2,})([-]{10,})\s*$')
SPLIT_DASH = re.compile(r'^( {2,})([-]+)\s+([-]+)\s*$')


def col_widths_from_split(line):
    """Return (col1_end, col2_start) char positions from a split-dash separator."""
    m = SPLIT_DASH.match(line)
    if not m:
        return None
    indent = len(m.group(1))
    col1_end = indent + len(m.group(2))
    col2_start = col1_end + 1
    while col2_start < len(line) and line[col2_start] == ' ':
        col2_start += 1
    return indent, col1_end, col2_start


def split_row(line, indent, col1_end, col2_start):
    """Split a content line into two columns using the separator positions."""
    if len(line) <= indent:
        return '', ''
    col1 = line[indent:col1_end].strip()
    col2 = line[col2_start:].strip() if col2_start < len(line) else ''
    return col1, col2


def clean_cell(s):
    return s.strip()


def make_pipe_table(headers, rows):
    """Build a GFM pipe table string."""
    n = len(headers)
    # Compute column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < n:
                widths[i] = max(widths[i], len(cell))
    widths = [max(w, 3) for w in widths]

    def fmt_row(cells):
        padded = []
        for i, cell in enumerate(cells):
            w = widths[i] if i < len(widths) else len(cell)
            padded.append(cell.ljust(w))
        return '| ' + ' | '.join(padded) + ' |'

    sep = '| ' + ' | '.join('-' * w for w in widths) + ' |'
    lines = [fmt_row(headers), sep]
    for row in rows:
        lines.append(fmt_row(row))
    return '\n'.join(lines)


def parse_and_replace(text):
    lines = text.split('\n')
    out = []
    i = 0

    while i < len(lines):
        m = DASH_LINE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        # Found an opening dash line — collect the table block
        opening = i
        indent_str = m.group(1)
        indent = len(indent_str)
        block = []  # (line_index, raw_line)
        j = i + 1

        # Collect until we find the closing dash line
        closing = None
        header_sep = None  # index within block of the split-dash separator

        while j < len(lines):
            bl = lines[j]
            if DASH_LINE.match(bl):
                # Could be the header separator (single-col) or the closing
                # If we haven't seen a split-dash yet, check next line for split
                if SPLIT_DASH.match(bl):
                    # This is actually a split-dash, not an outer dash — shouldn't happen
                    # based on pandoc output, but handle it
                    header_sep = len(block)
                    block.append(bl)
                    j += 1
                else:
                    # Full-width dash — could be header sep (single-col) or closing
                    if header_sep is None and len(block) > 0:
                        # Check if this is a single-col header separator
                        # (appears right after the header text)
                        # We'll tentatively treat it as header sep and keep scanning
                        header_sep = len(block)
                        block.append(bl)
                        j += 1
                    else:
                        # This is the closing dash line
                        closing = j
                        j += 1
                        break
            elif SPLIT_DASH.match(bl):
                header_sep = len(block)
                block.append(bl)
                j += 1
            else:
                block.append(bl)
                j += 1

        if closing is None:
            # Malformed — just emit as-is
            out.append(lines[i])
            i += 1
            continue

        # Now parse the block
        # Find header_sep position
        if header_sep is None:
            # No separator found — single-column, no header sep means whole thing is list
            out.append(lines[i])
            i += 1
            continue

        sep_line = block[header_sep]

        if SPLIT_DASH.match(sep_line):
            # TWO-COLUMN TABLE
            positions = col_widths_from_split(sep_line)
            if positions is None:
                out.append(lines[i])
                i += 1
                continue
            ind, col1_end, col2_start = positions

            # Header is everything before header_sep
            header_lines = block[:header_sep]
            # Merge header lines (usually just one)
            h1_parts, h2_parts = [], []
            for hl in header_lines:
                if hl.strip():
                    c1, c2 = split_row(hl, ind, col1_end, col2_start)
                    if c1: h1_parts.append(c1)
                    if c2: h2_parts.append(c2)
            h1 = ' '.join(h1_parts) or 'Column 1'
            h2 = ' '.join(h2_parts) or 'Column 2'

            # Data rows: everything after header_sep
            data_lines = block[header_sep + 1:]
            rows = []
            c1_acc, c2_acc = [], []

            def flush_row():
                if c1_acc or c2_acc:
                    rows.append([clean_cell(' '.join(c1_acc)),
                                 clean_cell(' '.join(c2_acc))])
                    c1_acc.clear()
                    c2_acc.clear()

            for dl in data_lines:
                if not dl.strip():
                    flush_row()
                elif DASH_LINE.match(dl):
                    flush_row()
                else:
                    c1, c2 = split_row(dl, ind, col1_end, col2_start)
                    if c1: c1_acc.append(c1)
                    if c2: c2_acc.append(c2)
            flush_row()

            table_md = make_pipe_table([h1, h2], rows)
            out.append(table_md)

        else:
            # SINGLE-COLUMN TABLE
            # header_sep is a full-width dash line
            # Header is block[0:header_sep], data is block[header_sep+1:]
            header_lines = block[:header_sep]
            h1_parts = [hl.strip() for hl in header_lines if hl.strip()]
            h1 = ' '.join(h1_parts) or 'Method'

            data_lines = block[header_sep + 1:]
            rows = []
            acc = []

            def flush_single():
                if acc:
                    rows.append([clean_cell(' '.join(acc))])
                    acc.clear()

            for dl in data_lines:
                if not dl.strip():
                    flush_single()
                elif DASH_LINE.match(dl):
                    flush_single()
                else:
                    acc.append(dl.strip())
            flush_single()

            table_md = make_pipe_table([h1], rows)
            out.append(table_md)

        i = j  # skip past closing dash line

    return '\n'.join(out)


FILES = [
    'pages/developers-guide/advanced-features.md',
    'pages/developers-guide/deployment.md',
    'pages/developers-guide/gml-sdk.md',
    'pages/developers-guide/terrain-sdk.md',
    'pages/developers-guide/walkthrough-1.md',
]

root = Path(__file__).parent.parent

for rel in FILES:
    path = root / rel
    original = path.read_text(encoding='utf-8')
    converted = parse_and_replace(original)
    if converted != original:
        path.write_text(converted, encoding='utf-8')
        # Count how many tables were fixed
        n = len(re.findall(r'^  -{10,}', original, re.MULTILINE)) // 2
        print(f'Fixed {n} table(s) in {rel}')
    else:
        print(f'No change: {rel}')
