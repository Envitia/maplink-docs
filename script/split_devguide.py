"""
Split devguide_new_raw.md into individual section files for pages/developers-guide/.
Handles heading level normalisation, image path fixes, and frontmatter.
"""

import re
import os

RAW_FILE = "c:/maplink/maplink-docs/devguide_new_raw.md"
OUT_DIR = "c:/maplink/maplink-docs/pages/developers-guide"

# Maps the exact heading text (after stripping attributes) to (filename, title)
SECTION_MAP = {
    "Introduction": ("introduction.md", "Introduction"),
    "MapLink SDK Components and Concepts": ("sdk-components.md", "MapLink SDK Components and Concepts"),
    "Basic MapLink Applications": ("basic-applications.md", "Basic MapLink Applications"),
    "Unicode": ("unicode.md", "Unicode"),
    "MapLink and your Development Environment": ("development-environment.md", "MapLink and your Development Environment"),
    "Deployment of End User Application": ("deployment.md", "Deployment of End User Application"),
    "Samples": ("samples.md", "Samples"),
    "Walkthrough 1 - Your First MapLink Application": ("walkthrough-1.md", "Walkthrough 1 - Your First MapLink Application"),
    "Walkthrough 2 - Modifying the Visible Area": ("walkthrough-2.md", "Walkthrough 2 - Modifying the Visible Area"),
    "Geometry and Overlays": ("geometry-and-overlays.md", "Geometry and Overlays"),
    "Walkthrough 3 - Adding a Simple Vector Overlay": ("walkthrough-3.md", "Walkthrough 3 - Adding a Simple Vector Overlay"),
    "Walkthrough 3 -- Adding a Simple Vector Overlay": ("walkthrough-3.md", "Walkthrough 3 - Adding a Simple Vector Overlay"),
    "More Features of the Core SDK": ("advanced-features.md", "More Features of the Core SDK"),
    "OpenGL Drawing Surface": ("opengl-drawing-surface.md", "OpenGL Drawing Surface"),
    "Direct Import SDK": ("direct-import-sdk.md", "Direct Import SDK"),
    "Tracks SDK": ("tracks-sdk.md", "Tracks SDK"),
    "Dynamic Overlays with the DDO SDK": ("ddo-sdk.md", "Dynamic Overlays with the DDO SDK"),
    "Terrain SDK": ("terrain-sdk.md", "Terrain SDK"),
    "MapLink 3D Earth SDK": ("maplink-3d-earth-sdk.md", "MapLink 3D Earth SDK"),
    "Editor SDK": ("editor-sdk.md", "Editor SDK"),
    "Geopackage SDK": ("geopackage-sdk.md", "Geopackage SDK"),
    "OWSContext SDK": ("owscontext-sdk.md", "OWSContext SDK"),
    "MapLink OGC Services SDK": ("ogc-services-sdk.md", "MapLink OGC Services SDK"),
    "Spatial SDK": ("spatial-sdk.md", "Spatial SDK"),
    "GML SDK": ("gml-sdk.md", "GML SDK"),
    ".NET SDKs": ("net-sdks.md", ".NET SDKs"),
    "Floating Point": ("floating-point.md", "Floating Point"),
    "Other SDKs": ("other-sdks.md", "Other SDKs"),
    "Threading": ("threading.md", "Threading"),
}

# Regex for heading lines with ENV class attributes
HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s*\{[^}]*\.(?:ENV|Env)---Heading-(\d)[^}]*\}\s*$')
# Heading-1 marker (to split sections)
H1_RE = re.compile(r'^#\s+(.+?)\s*\{[^}]*\.(?:ENV|Env)---Heading-1[^}]*\}\s*$')
# Any heading with ENV class
ANY_HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s*\{[^}]*\.(?:ENV|Env)---Heading-(\d)[^}]*\}\s*$')
# Inline anchors like [{#id .anchor}]
INLINE_ANCHOR_RE = re.compile(r'\[\]\{[^}]*\.anchor[^}]*\}')
# Image path: absolute path to assets
IMAGE_PATH_RE = re.compile(r'c:/maplink/maplink-docs/assets/images/developers-guide/(media/[^\)]+)')
# Image size attributes
IMAGE_ATTRS_RE = re.compile(r'\{width="[^"]*"(?:\s+height="[^"]*")?\}')
# Backslash before apostrophe/quote
BACKSLASH_RE = re.compile(r"\\('|\")")


def clean_heading_text(text):
    """Remove inline anchors and backslash escapes from heading text."""
    text = INLINE_ANCHOR_RE.sub('', text)
    text = BACKSLASH_RE.sub(r'\1', text)
    return text.strip()


def fix_line(line, in_code_block):
    """Apply line-level fixes."""
    if in_code_block:
        return line

    # Fix heading levels based on ENV class
    m = ANY_HEADING_RE.match(line)
    if m:
        level = min(int(m.group(3)), 4)
        text = clean_heading_text(m.group(2))
        return '#' * level + ' ' + text + '\n'

    # Drop empty headings (blank Word heading styles pandoc emits as "###### ")
    if re.match(r'^#{1,}\s*$', line):
        return ''

    # Cap plain headings (no ENV class) at h4 — pandoc can generate h5-h9
    # from deeply nested Word styles which are invalid HTML beyond h6
    plain_m = re.match(r'^(#{4,})\s+(.+)', line)
    if plain_m:
        level = min(len(plain_m.group(1)), 4)
        text = clean_heading_text(plain_m.group(2))
        return '#' * level + ' ' + text + '\n'

    # Fix image paths and remove size attributes
    line = IMAGE_PATH_RE.sub(r'../../assets/images/developers-guide/\1', line)
    line = IMAGE_ATTRS_RE.sub('', line)

    # Remove inline anchors
    line = INLINE_ANCHOR_RE.sub('', line)

    # Fix backslash escapes
    line = BACKSLASH_RE.sub(r'\1', line)

    # Fix em-dash (--) to single dash, but not in code-like contexts
    # Only replace ' -- ' (surrounded by spaces) to avoid breaking option flags
    line = line.replace(' -- ', ' - ')

    return line


def write_section(filename, title, lines):
    path = os.path.join(OUT_DIR, filename)
    frontmatter = f'---\ntitle: "{title}"\n---\n\n'
    # Remove leading blank lines
    while lines and lines[0].strip() == '':
        lines.pop(0)
    # Remove trailing blank lines
    while lines and lines[-1].strip() == '':
        lines.pop()
    content = frontmatter + ''.join(lines) + '\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Wrote {filename} ({len(lines)} lines)")


def main():
    with open(RAW_FILE, encoding='utf-8') as f:
        raw_lines = f.readlines()

    sections = []  # list of (heading_text, [lines])
    current_heading = None
    current_lines = []
    in_code_block = False

    for line in raw_lines:
        # Track code blocks
        if line.startswith('```') or line.startswith('~~~'):
            in_code_block = not in_code_block

        m = H1_RE.match(line)
        if m and not in_code_block:
            heading_text = clean_heading_text(m.group(1))
            if current_heading is not None:
                sections.append((current_heading, current_lines))
            current_heading = heading_text
            # Write the heading as h1 for the new file
            current_lines = [f'# {heading_text}\n']
        else:
            if current_heading is not None:
                current_lines.append(fix_line(line, in_code_block))
            # else: before first heading - skip (cover page, TOC)

    if current_heading is not None:
        sections.append((current_heading, current_lines))

    print(f"Found {len(sections)} sections\n")

    written = 0
    skipped = []
    for heading, lines in sections:
        if heading in SECTION_MAP:
            filename, title = SECTION_MAP[heading]
            write_section(filename, title, lines)
            written += 1
        else:
            skipped.append(heading)

    print(f"\nDone: {written} files written.")
    if skipped:
        print(f"Skipped (no mapping): {skipped}")


if __name__ == '__main__':
    main()
