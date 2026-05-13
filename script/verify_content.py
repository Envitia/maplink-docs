"""
Verify that the markdown developer's guide is 1:1 with the DOCX source.
Checks: headings, images, callout/note blocks, and text coverage.
"""

import re
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAGES = ROOT / "pages" / "developers-guide"
IMAGES = ROOT / "assets" / "images" / "developers-guide" / "media"
SOURCE_TXT = ROOT / "script" / "devguide_source.txt"

PAGE_ORDER = [
    "introduction.md",
    "sdk-components.md",
    "basic-applications.md",
    "development-environment.md",
    "deployment.md",
    "samples.md",
    "walkthrough-1.md",
    "walkthrough-2.md",
    "walkthrough-3.md",
    "geometry-and-overlays.md",
    "advanced-features.md",
    "unicode.md",
    "opengl-drawing-surface.md",
    "direct-import-sdk.md",
    "tracks-sdk.md",
    "ddo-sdk.md",
    "terrain-sdk.md",
    "maplink-3d-earth-sdk.md",
    "editor-sdk.md",
    "geopackage-sdk.md",
    "owscontext-sdk.md",
    "ogc-services-sdk.md",
    "spatial-sdk.md",
    "gml-sdk.md",
    "net-sdks.md",
    "floating-point.md",
    "other-sdks.md",
    "threading.md",
]

# ── helpers ──────────────────────────────────────────────────────────────────

def strip_frontmatter(text):
    if text.startswith("---"):
        end = text.index("---", 3)
        return text[end + 3:].lstrip("\n")
    return text

def md_to_plain(text):
    """Very light stripping of markdown syntax to get comparable plain text."""
    text = strip_frontmatter(text)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Remove markdown headings markers
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # Remove image syntax
    text = re.sub(r"!\[.*?\]\(.*?\)", "[IMAGE]", text)
    # Remove link syntax, keep text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Remove table separators
    text = re.sub(r"^\|[-| :]+\|$", "", text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text)
    text = re.sub(r"_{1,2}([^_]+)_{1,2}", r"\1", text)
    # Collapse whitespace
    text = re.sub(r"[ \t]+", " ", text)
    return text

def normalise(text):
    """Normalise text for comparison: lowercase, collapse whitespace, strip punctuation variants."""
    text = text.lower()
    # Normalise dashes/hyphens
    text = re.sub(r"[–—]", "-", text)
    # Normalise quotes
    text = re.sub(r"[''`]", "'", text)
    text = re.sub(r'[""]', '"', text)
    # Collapse whitespace/newlines
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def tokenise(text):
    """Return set of meaningful words (>3 chars)."""
    return set(w for w in re.findall(r"[a-z0-9_:]{4,}", normalise(text)))

def extract_headings_from_md(text):
    return re.findall(r"^#{1,4}\s+(.+)$", text, flags=re.MULTILINE)

def extract_images_from_md(text):
    return re.findall(r"!\[.*?\]\(([^)]+)\)", text)

def extract_images_from_source(text):
    # pandoc plain output marks images as just their alt text or nothing;
    # we need to look at the raw docx markdown extraction instead
    return []


# ── load source ──────────────────────────────────────────────────────────────

source_txt = SOURCE_TXT.read_text(encoding="utf-8", errors="replace")
source_norm = normalise(source_txt)
source_tokens = tokenise(source_txt)

# Extract headings from source (lines that look like section titles —
# pandoc plain output preserves them as ALL CAPS or Title Case lines)
# We also extract from a markdown pass of the docx
source_md_path = ROOT / "script" / "devguide_source_md.md"
if not source_md_path.exists():
    print("INFO: devguide_source_md.md not found — run pandoc -t markdown first for heading extraction")

# ── load all markdown pages ───────────────────────────────────────────────────

all_md_text = ""
per_page = {}
for fname in PAGE_ORDER:
    fpath = PAGES / fname
    if not fpath.exists():
        print(f"MISSING FILE: {fname}")
        continue
    raw = fpath.read_text(encoding="utf-8", errors="replace")
    per_page[fname] = raw
    all_md_text += "\n" + raw

all_md_plain = md_to_plain(all_md_text)
all_md_norm  = normalise(all_md_plain)
all_md_tokens = tokenise(all_md_plain)


# ── 1. IMAGE CHECK ───────────────────────────────────────────────────────────

print("=" * 60)
print("1. IMAGE CHECK")
print("=" * 60)

# Images on disk
disk_images = {f.name for f in IMAGES.iterdir() if f.is_file()}

# Images referenced in markdown
md_image_refs = []
for fname, raw in per_page.items():
    for ref in extract_images_from_md(raw):
        # ref is like ../../assets/images/developers-guide/media/image1.png
        basename = Path(ref).name
        md_image_refs.append((fname, basename))

md_image_names = {name for _, name in md_image_refs}

# Also get images from the raw pandoc markdown extraction
pandoc_md_path = ROOT / "script" / "devguide_raw.md"
docx_image_names = set()
if pandoc_md_path.exists():
    pandoc_raw = pandoc_md_path.read_text(encoding="utf-8", errors="replace")
    for ref in re.findall(r"!\[.*?\]\(([^)]+)\)", pandoc_raw):
        docx_image_names.add(Path(ref).name)

print(f"  Images on disk:          {len(disk_images)}")
print(f"  Images in markdown:      {len(md_image_names)}")
if docx_image_names:
    print(f"  Images in source docx:   {len(docx_image_names)}")

# Images on disk but NOT in markdown
unreferenced = disk_images - md_image_names
if unreferenced:
    print(f"\n  WARNING — On disk but NOT referenced in any .md file ({len(unreferenced)}):")
    for img in sorted(unreferenced):
        print(f"    {img}")
else:
    print("  OK — every disk image is referenced in markdown")

# Images in markdown but NOT on disk (broken refs)
broken = md_image_names - disk_images
if broken:
    print(f"\n  ERROR — Referenced in markdown but NOT on disk ({len(broken)}):")
    for img in sorted(broken):
        pages_using = [f for f, n in md_image_refs if n == img]
        print(f"    {img}  (in: {', '.join(pages_using)})")
else:
    print("  OK — all markdown image references resolve on disk")

# Images in docx but missing from markdown
if docx_image_names:
    missing_from_md = docx_image_names - md_image_names
    if missing_from_md:
        print(f"\n  ERROR — In source docx but missing from markdown ({len(missing_from_md)}):")
        for img in sorted(missing_from_md):
            print(f"    {img}")
    else:
        print("  OK — all docx images are present in markdown")


# ── 2. HEADING CHECK ─────────────────────────────────────────────────────────

print()
print("=" * 60)
print("2. HEADING CHECK (from markdown vs source plain text)")
print("=" * 60)

# Extract all headings from markdown
all_md_headings = []
for fname, raw in per_page.items():
    for h in extract_headings_from_md(raw):
        all_md_headings.append((fname, h.strip()))

# Check each heading appears in the source plain text
missing_headings = []
for fname, heading in all_md_headings:
    h_norm = normalise(heading)
    if len(h_norm) < 4:
        continue  # too short to be meaningful
    if h_norm not in source_norm:
        missing_headings.append((fname, heading))

print(f"  Total headings in markdown: {len(all_md_headings)}")
if missing_headings:
    print(f"  WARNING — {len(missing_headings)} headings not found verbatim in source:")
    for fname, h in missing_headings[:40]:
        print(f"    [{fname}]  {h!r}")
    if len(missing_headings) > 40:
        print(f"    ... and {len(missing_headings)-40} more")
else:
    print("  OK — all headings found in source text")


# ── 3. TOKEN COVERAGE CHECK ──────────────────────────────────────────────────

print()
print("=" * 60)
print("3. TOKEN COVERAGE (vocabulary overlap)")
print("=" * 60)

common = source_tokens & all_md_tokens
only_in_source = source_tokens - all_md_tokens
only_in_md = all_md_tokens - source_tokens

coverage = len(common) / len(source_tokens) * 100 if source_tokens else 0
print(f"  Source unique tokens:    {len(source_tokens)}")
print(f"  Markdown unique tokens:  {len(all_md_tokens)}")
print(f"  Common tokens:           {len(common)}")
print(f"  Coverage (src covered):  {coverage:.1f}%")

if only_in_source:
    # Filter to tokens that look like technical terms or proper nouns
    technical = [t for t in only_in_source if re.search(r"[A-Z]|[0-9]", t, re.I) and len(t) > 5]
    # Normalise them back
    sample = sorted(technical)[:60]
    if sample:
        print(f"\n  Tokens in source but NOT in markdown (sample of technical terms):")
        for i in range(0, min(len(sample), 60), 6):
            print("    " + "  ".join(sample[i:i+6]))


# ── 4. PER-PAGE SECTION PRESENCE ─────────────────────────────────────────────

print()
print("=" * 60)
print("4. PER-PAGE SECTION CHECK")
print("=" * 60)

for fname, raw in per_page.items():
    plain = md_to_plain(raw)
    norm  = normalise(plain)
    tokens = tokenise(plain)
    if not tokens:
        print(f"  WARNING [{fname}]: appears empty")
        continue
    # Check first heading is in source
    headings = extract_headings_from_md(raw)
    if headings:
        h0 = normalise(headings[0])
        found = h0 in source_norm if len(h0) > 4 else True
        status = "OK" if found else "WARN"
        print(f"  {status:4s} [{fname}]  headings={len(headings)}  '{headings[0][:50]}'")
    else:
        print(f"  WARN [{fname}]: no headings found")


# ── 5. CALLOUT / NOTE BLOCK CHECK ────────────────────────────────────────────

print()
print("=" * 60)
print("5. CALLOUT / ANNOTATION BLOCKS")
print("=" * 60)

total_callouts = 0
total_blockquotes = 0
for fname, raw in per_page.items():
    callouts    = len(re.findall(r'<div class="callout"', raw))
    blockquotes = len(re.findall(r"^>", raw, re.MULTILINE))
    total_callouts    += callouts
    total_blockquotes += blockquotes
    if callouts or blockquotes:
        print(f"  [{fname}]  callouts={callouts}  blockquotes={blockquotes}")

print(f"\n  Total callout divs:  {total_callouts}")
print(f"  Total blockquotes:   {total_blockquotes}")

# Cross-check: count NOTE/WARNING/TIP occurrences in source
note_count_src = len(re.findall(r"\b(note|warning|tip|important)\b", source_txt, re.I))
note_count_md  = len(re.findall(r"\b(note|warning|tip|important)\b", all_md_text, re.I))
print(f"\n  'Note/Warning/Tip/Important' occurrences:")
print(f"    Source: {note_count_src}")
print(f"    Markdown: {note_count_md}")
if abs(note_count_src - note_count_md) > 5:
    print("  WARNING — counts differ by more than 5, some annotations may be missing")
else:
    print("  OK — counts are within tolerance")


# ── 6. TABLE CHECK ───────────────────────────────────────────────────────────

print()
print("=" * 60)
print("6. TABLE CHECK")
print("=" * 60)

total_tables = 0
for fname, raw in per_page.items():
    # Count markdown pipe tables (header separator rows)
    tables = len(re.findall(r"^\|[-| :]+\|$", raw, re.MULTILINE))
    total_tables += tables
    if tables:
        print(f"  [{fname}]  tables={tables}")

print(f"\n  Total markdown tables: {total_tables}")

# Source: count table-like structures (lines with multiple |)
src_table_rows = len(re.findall(r"^\s*\|.+\|", source_txt, re.MULTILINE))
print(f"  Source pipe-separated lines (rough): {src_table_rows}")


# ── SUMMARY ──────────────────────────────────────────────────────────────────

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Pages verified:     {len(per_page)}/28")
print(f"  Images on disk:     {len(disk_images)}")
print(f"  Images in markdown: {len(md_image_names)}")
print(f"  Broken image refs:  {len(broken)}")
print(f"  Unreferenced imgs:  {len(unreferenced)}")
print(f"  Token coverage:     {coverage:.1f}%")
print(f"  Headings checked:   {len(all_md_headings)}")
print(f"  Missing headings:   {len(missing_headings)}")
