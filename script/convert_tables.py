"""
Convert pandoc grid tables in markdown files to GFM pipe tables.
Single-column tables become styled callout boxes.
Run this on already-split developer guide files.
"""

import re
import os
import glob

OUT_DIR = 'c:/maplink/maplink-docs/pages/developers-guide'

FILES = [
    'ddo-sdk.md', 'development-environment.md', 'direct-import-sdk.md',
    'editor-sdk.md', 'geopackage-sdk.md', 'gml-sdk.md', 'net-sdks.md',
    'ogc-services-sdk.md', 'opengl-drawing-surface.md', 'spatial-sdk.md',
    'terrain-sdk.md', 'threading.md', 'tracks-sdk.md',
]

BORDER_RE = re.compile(r'^\+[-=+]+\+\s*$')


def get_col_positions(border_line):
    return [i for i, c in enumerate(border_line.rstrip()) if c == '+']


def extract_cells(content_line, col_positions):
    cells = []
    for i in range(len(col_positions) - 1):
        start = col_positions[i] + 1
        end = col_positions[i + 1]
        cell = content_line[start:end] if len(content_line) > start else ''
        cells.append(cell.strip())
    return cells


def clean_cell(text):
    # Strip pandoc blockquote prefix from table cells
    text = re.sub(r'^>\s*', '', text)
    # Strip bold markers around standalone content for callouts
    return text.strip()


def parse_grid_table(table_lines):
    """Parse grid table lines into (is_header_row, [cells]) tuples."""
    col_positions = get_col_positions(table_lines[0])
    num_cols = len(col_positions) - 1

    rows = []          # list of (is_header, [cell_text])
    current_cells = [''] * num_cols
    is_header_sep = False

    for line in table_lines[1:]:
        if BORDER_RE.match(line):
            # This border ends a row — save it
            if any(c.strip() for c in current_cells):
                rows.append((is_header_sep, [clean_cell(c) for c in current_cells]))
            current_cells = [''] * num_cols
            # Check if this border is the header separator (uses =)
            is_header_sep = '=' in line
        elif line.startswith('|'):
            cells = extract_cells(line, col_positions)
            for i, cell in enumerate(cells):
                cleaned = clean_cell(cell)
                if cleaned:
                    if current_cells[i]:
                        current_cells[i] += ' ' + cleaned
                    else:
                        current_cells[i] = cleaned

    return num_cols, rows


def to_pipe_table(rows, num_cols):
    if not rows:
        return ''

    # Find the header row (first row, or the one before the = separator)
    header_row = rows[0][1]
    data_rows = [r[1] for r in rows[1:]]

    # Calculate column widths
    widths = [max(len(header_row[c]), 3) for c in range(num_cols)]
    for row in data_rows:
        for c in range(num_cols):
            val = row[c] if c < len(row) else ''
            widths[c] = max(widths[c], len(val))

    def fmt_row(cells):
        padded = []
        for i, w in enumerate(widths):
            val = cells[i] if i < len(cells) else ''
            padded.append(val.ljust(w))
        return '| ' + ' | '.join(padded) + ' |'

    sep = '| ' + ' | '.join('-' * w for w in widths) + ' |'

    lines = [fmt_row(header_row), sep]
    for row in data_rows:
        lines.append(fmt_row(row))

    return '\n'.join(lines) + '\n'


def to_callout(rows):
    """Single-column table → styled HTML callout div."""
    parts = []
    for _, cells in rows:
        text = cells[0].strip() if cells else ''
        if text:
            parts.append(text)
    if not parts:
        return ''
    inner = '\n\n'.join(parts)
    return f'<div class="callout" markdown="1">\n\n{inner}\n\n</div>\n'


def convert_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()

    output = []
    i = 0
    changed = False

    while i < len(lines):
        line = lines[i]

        # Detect start of a grid table
        if BORDER_RE.match(line):
            # Collect the full table
            table_lines = []
            while i < len(lines) and (BORDER_RE.match(lines[i]) or lines[i].startswith('|')):
                table_lines.append(lines[i].rstrip('\n'))
                i += 1
            # Make sure we got the closing border
            if not BORDER_RE.match(table_lines[-1]):
                # Not a complete table, pass through as-is
                output.extend(tl + '\n' for tl in table_lines)
                continue

            num_cols, rows = parse_grid_table(table_lines)

            if num_cols == 1:
                converted = to_callout(rows)
            else:
                converted = to_pipe_table(rows, num_cols)

            output.append('\n' + converted + '\n')
            changed = True
        else:
            output.append(line)
            i += 1

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(output)
        print(f'  Converted: {os.path.basename(filepath)}')
    else:
        print(f'  No tables:  {os.path.basename(filepath)}')


def main():
    for fname in FILES:
        path = os.path.join(OUT_DIR, fname)
        convert_file(path)
    print('\nDone.')


if __name__ == '__main__':
    main()
