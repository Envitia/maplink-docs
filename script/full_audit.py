"""
Full rendering audit of all developer's guide markdown files.
Checks every known failure mode that would cause bad output in kramdown/Jekyll.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAGES = ROOT / "pages" / "developers-guide"
IMAGES = ROOT / "assets" / "images" / "developers-guide" / "media"

PAGE_ORDER = [
    "introduction.md","sdk-components.md","basic-applications.md",
    "development-environment.md","deployment.md","samples.md",
    "walkthrough-1.md","walkthrough-2.md","walkthrough-3.md",
    "geometry-and-overlays.md","advanced-features.md","unicode.md",
    "opengl-drawing-surface.md","direct-import-sdk.md","tracks-sdk.md",
    "ddo-sdk.md","terrain-sdk.md","maplink-3d-earth-sdk.md","editor-sdk.md",
    "geopackage-sdk.md","owscontext-sdk.md","ogc-services-sdk.md",
    "spatial-sdk.md","gml-sdk.md","net-sdks.md","floating-point.md",
    "other-sdks.md","threading.md",
]

issues = {}

def flag(fname, category, msg):
    issues.setdefault(fname, {}).setdefault(category, []).append(msg)

def strip_frontmatter(text):
    if text.startswith("---"):
        try:
            end = text.index("---", 3)
            return text[end+3:].lstrip("\n"), True
        except ValueError:
            pass
    return text, False

# ─────────────────────────────────────────────────────────────────────────────

for fname in PAGE_ORDER:
    path = PAGES / fname
    if not path.exists():
        flag(fname, "MISSING", "File does not exist")
        continue

    raw = path.read_text(encoding="utf-8", errors="replace")
    body, has_fm = strip_frontmatter(raw)
    lines = body.split("\n")

    # ── 1. FRONTMATTER ───────────────────────────────────────────────────────
    if not has_fm:
        flag(fname, "FRONTMATTER", "No frontmatter found")

    # ── 2. GRID TABLES (+---+) ───────────────────────────────────────────────
    grid = [i+1 for i,l in enumerate(lines) if re.match(r'\s*\+[-=+]{3,}\+', l)]
    if grid:
        flag(fname, "GRID_TABLE", f"{len(grid)} grid-table line(s) at lines: {grid[:10]}")

    # ── 3. SIMPLE TABLES (dash-separator) ────────────────────────────────────
    simple = [i+1 for i,l in enumerate(lines) if re.match(r'^  -{10,}\s*$', l)]
    if simple:
        flag(fname, "SIMPLE_TABLE", f"{len(simple)} simple-table separator(s) at lines: {simple[:10]}")

    # ── 4. HEADING ATTRIBUTES {#anchor .class} ───────────────────────────────
    hattr = [(i+1, l.strip()) for i,l in enumerate(lines)
             if re.search(r'^#{1,6}\s+.*\{[#.][\w\s.-]+\}', l)]
    if hattr:
        flag(fname, "HEADING_ATTRS",
             f"{len(hattr)} heading(s) with leftover attributes: " +
             "; ".join(f"L{n}: {t[:60]}" for n,t in hattr[:5]))

    # ── 5. DEEP HEADINGS (h5+) ───────────────────────────────────────────────
    deep = [(i+1, l.strip()) for i,l in enumerate(lines)
            if re.match(r'^#{5,}\s', l)]
    if deep:
        flag(fname, "DEEP_HEADINGS",
             f"{len(deep)} heading(s) deeper than h4: " +
             "; ".join(f"L{n}: {t[:50]}" for n,t in deep[:5]))

    # ── 6. IMAGE ATTRIBUTES leftover {width=... height=...} ──────────────────
    imgattr = [(i+1, l.strip()) for i,l in enumerate(lines)
               if re.search(r'!\[.*\]\(.*\)\s*\{[^}]*(?:width|height|alt)=[^}]*\}', l)]
    if imgattr:
        flag(fname, "IMAGE_ATTRS",
             f"{len(imgattr)} image(s) with leftover size attributes: " +
             "; ".join(f"L{n}: {t[:80]}" for n,t in imgattr[:5]))

    # ── 7. BROKEN IMAGE PATHS ────────────────────────────────────────────────
    for i, l in enumerate(lines):
        for ref in re.findall(r'!\[.*?\]\(([^)]+)\)', l):
            ref_clean = ref.split()[0]  # strip any trailing attrs
            # Resolve relative to the page
            img_name = Path(ref_clean).name
            if img_name and not (IMAGES / img_name).exists():
                flag(fname, "BROKEN_IMAGE", f"L{i+1}: {ref_clean!r} -> '{img_name}' not on disk")

    # ── 8. RAW PANDOC ANCHORS {#_Toc...} ─────────────────────────────────────
    anchors = [(i+1, l.strip()) for i,l in enumerate(lines)
               if re.search(r'\{#_[A-Za-z]', l)]
    if anchors:
        flag(fname, "RAW_ANCHORS",
             f"{len(anchors)} raw pandoc anchor(s): " +
             "; ".join(f"L{n}: {t[:70]}" for n,t in anchors[:5]))

    # ── 9. EXCESSIVE BLOCKQUOTES (likely code rendered as blockquote) ─────────
    bq_lines = [i+1 for i,l in enumerate(lines) if l.startswith("> ") or l == ">"]
    if len(bq_lines) > 20:
        # Sample consecutive runs — long runs are almost certainly code blocks
        runs = []
        run_start, run_len = None, 0
        for k, ln_num in enumerate(bq_lines):
            if run_start is None:
                run_start, run_len = ln_num, 1
            elif ln_num == bq_lines[k-1] + 1 or ln_num == bq_lines[k-1] + 2:
                run_len += 1
            else:
                if run_len >= 8:
                    runs.append((run_start, run_len))
                run_start, run_len = ln_num, 1
        if run_len >= 8:
            runs.append((run_start, run_len))
        if runs:
            flag(fname, "BLOCKQUOTE_CODE",
                 f"Total blockquote lines: {len(bq_lines)}. "
                 f"Long runs (likely code blocks): " +
                 ", ".join(f"L{s}+{n}" for s,n in runs[:8]))

    # ── 10. INLINE ANCHOR TAGS ───────────────────────────────────────────────
    inline_anch = [(i+1, l.strip()) for i,l in enumerate(lines)
                   if re.search(r'\[\]\{#', l) or re.search(r'<a\s+id=', l, re.I)]
    if inline_anch:
        flag(fname, "INLINE_ANCHORS",
             f"{len(inline_anch)} inline anchor(s): " +
             "; ".join(f"L{n}: {t[:70]}" for n,t in inline_anch[:5]))

    # ── 11. UNFENCED CODE BLOCKS (indented code) ─────────────────────────────
    indented_code = [i+1 for i,l in enumerate(lines)
                     if l.startswith("    ") and not l.startswith("     ") and
                     re.search(r'[(){};=]', l)]
    if len(indented_code) > 5:
        flag(fname, "INDENTED_CODE",
             f"{len(indented_code)} indented-code line(s) (may not render as code block) - "
             f"first at L{indented_code[0]}")

    # ── 12. EMPTY HEADINGS ───────────────────────────────────────────────────
    empty_h = [(i+1, l.strip()) for i,l in enumerate(lines)
               if re.match(r'^#{1,4}\s*$', l.strip())]
    if empty_h:
        flag(fname, "EMPTY_HEADINGS",
             f"{len(empty_h)} empty heading(s) at: " +
             ", ".join(f"L{n}" for n,_ in empty_h))

    # ── 13. UNCLOSED HTML TAGS ───────────────────────────────────────────────
    opens  = re.findall(r'<(div|span|table|tbody|tr|td|th|ul|ol|li)\b', body, re.I)
    closes = re.findall(r'</(div|span|table|tbody|tr|td|th|ul|ol|li)>', body, re.I)
    open_ct  = {t.lower(): opens.count(t) for t in set(opens)}
    close_ct = {t.lower(): closes.count(t) for t in set(closes)}
    for tag in set(list(open_ct.keys()) + list(close_ct.keys())):
        o = open_ct.get(tag, 0)
        c = close_ct.get(tag, 0)
        if o != c:
            flag(fname, "UNCLOSED_HTML", f"<{tag}>: {o} open, {c} close")

    # ── 14. ESCAPED ANGLE BRACKETS IN HEADINGS ───────────────────────────────
    esc_heads = [(i+1, l.strip()) for i,l in enumerate(lines)
                 if re.match(r'^#{1,4}', l) and re.search(r'\\[<>]', l)]
    if esc_heads:
        flag(fname, "ESC_IN_HEADING",
             f"{len(esc_heads)} heading(s) with escaped angle brackets: " +
             "; ".join(f"L{n}: {t[:70]}" for n,t in esc_heads[:5]))

    # ── 15. LITERAL BACKSLASH-ESCAPED CHARS THAT LOOK WRONG ─────────────────
    # Check for \| in table cells which would break pipe tables
    pipe_escape = [(i+1, l.strip()) for i,l in enumerate(lines)
                   if l.startswith("|") and r"\|" in l]
    if pipe_escape:
        flag(fname, "PIPE_ESCAPE_IN_TABLE",
             f"{len(pipe_escape)} table row(s) with \\| which may break column alignment: " +
             "; ".join(f"L{n}: {t[:80]}" for n,t in pipe_escape[:5]))

    # ── 16. FOOTNOTE DEFINITIONS ─────────────────────────────────────────────
    footnote_defs = [(i+1, l.strip()) for i,l in enumerate(lines)
                     if re.match(r'^\[\^[\w]+\]:', l)]
    footnote_refs = re.findall(r'\[\^[\w]+\](?!:)', body)
    if footnote_defs or footnote_refs:
        flag(fname, "FOOTNOTES",
             f"{len(footnote_defs)} definition(s), {len(footnote_refs)} reference(s) — "
             "verify they render in Jekyll/kramdown")

    # ── 17. DUPLICATE HEADINGS ───────────────────────────────────────────────
    heading_texts = [re.sub(r'^#{1,4}\s+', '', l).strip()
                     for l in lines if re.match(r'^#{1,4}\s+', l)]
    seen = {}
    for h in heading_texts:
        seen[h] = seen.get(h, 0) + 1
    dupes = {h: c for h, c in seen.items() if c > 1 and len(h) > 4}
    if dupes:
        flag(fname, "DUPLICATE_HEADINGS",
             f"Repeated headings: " +
             ", ".join(f"'{h}'×{c}" for h,c in list(dupes.items())[:5]))

    # ── 18. LINES WITH ONLY WHITESPACE INSIDE TABLES ────────────────────────
    in_table = False
    blank_in_table = []
    for i, l in enumerate(lines):
        if l.startswith("|"):
            in_table = True
        elif in_table and l.strip() == "":
            blank_in_table.append(i+1)
            in_table = False
        else:
            in_table = False

    # ── 19. UNRESOLVED WORD CROSS-REFERENCES ─────────────────────────────────
    word_refs = [(i+1, l.strip()) for i,l in enumerate(lines)
                 if re.search(r'mk:@MSITStore|CHM::', l, re.I)]
    if word_refs:
        flag(fname, "CHM_LINKS",
             f"{len(word_refs)} CHM/MS-Help link(s) that won't work on web: " +
             "; ".join(f"L{n}: {t[:80]}" for n,t in word_refs[:5]))

    # ── 20. LINES OVER 2000 CHARS (likely malformed) ─────────────────────────
    long_lines = [(i+1, len(l)) for i,l in enumerate(lines) if len(l) > 2000]
    if long_lines:
        flag(fname, "LONG_LINES",
             f"{len(long_lines)} very long line(s): " +
             ", ".join(f"L{n}({c}chars)" for n,c in long_lines[:5]))

    # ── 21. RAW HTML COMMENTS ────────────────────────────────────────────────
    html_comments = [(i+1,) for i,l in enumerate(lines) if "<!--" in l and "-->" not in l]
    if html_comments:
        flag(fname, "UNCLOSED_COMMENTS",
             f"{len(html_comments)} unclosed HTML comment(s)")

    # ── 22. DEFINITION LISTS (pandoc :) ──────────────────────────────────────
    deflists = [(i+1, l.strip()) for i,l in enumerate(lines)
                if re.match(r'^:   ', l)]
    if deflists:
        flag(fname, "DEF_LISTS",
             f"{len(deflists)} pandoc definition-list line(s) (may not render): " +
             "; ".join(f"L{n}: {t[:60]}" for n,t in deflists[:5]))

    # ── 23. MISSING BLANK LINE BEFORE HEADING ────────────────────────────────
    bad_heading_spacing = []
    for i in range(1, len(lines)):
        if re.match(r'^#{1,4}\s+', lines[i]) and lines[i-1].strip() != "":
            # Previous line is not blank
            if not re.match(r'^#{1,4}\s+', lines[i-1]):  # not consecutive headings
                bad_heading_spacing.append(i+1)
    if len(bad_heading_spacing) > 3:
        flag(fname, "HEADING_SPACING",
             f"{len(bad_heading_spacing)} heading(s) without blank line before: "
             f"first at L{bad_heading_spacing[0]}")

# ─────────────────────────────────────────────────────────────────────────────
# REPORT
# ─────────────────────────────────────────────────────────────────────────────

SEVERITY = {
    "MISSING": 1, "GRID_TABLE": 1, "SIMPLE_TABLE": 1,
    "HEADING_ATTRS": 1, "DEEP_HEADINGS": 1, "IMAGE_ATTRS": 1,
    "BROKEN_IMAGE": 1, "RAW_ANCHORS": 2, "BLOCKQUOTE_CODE": 2,
    "INLINE_ANCHORS": 2, "INDENTED_CODE": 3, "EMPTY_HEADINGS": 1,
    "UNCLOSED_HTML": 2, "ESC_IN_HEADING": 2, "PIPE_ESCAPE_IN_TABLE": 1,
    "FOOTNOTES": 2, "DUPLICATE_HEADINGS": 3, "CHM_LINKS": 2,
    "LONG_LINES": 2, "UNCLOSED_COMMENTS": 2, "DEF_LISTS": 2,
    "HEADING_SPACING": 3, "FRONTMATTER": 1,
}

SEV_LABEL = {1: "HIGH", 2: "MEDIUM", 3: "LOW"}
SEV_ORDER = {1: [], 2: [], 3: []}

total_issues = 0
for fname, cats in sorted(issues.items()):
    for cat, msgs in cats.items():
        sev = SEVERITY.get(cat, 2)
        SEV_ORDER[sev].append((fname, cat, msgs))
        total_issues += 1

for sev in [1, 2, 3]:
    if not SEV_ORDER[sev]:
        continue
    print(f"\n{'='*70}")
    print(f"[{SEV_LABEL[sev]}] SEVERITY ISSUES ({len(SEV_ORDER[sev])} categories)")
    print(f"{'='*70}")
    for fname, cat, msgs in SEV_ORDER[sev]:
        print(f"\n  [{fname}] {cat}")
        for m in msgs:
            print(f"    {m}")

print(f"\n{'='*70}")
print(f"AUDIT SUMMARY: {total_issues} issue categories across {len(issues)} files")
clean = [f for f in PAGE_ORDER if f not in issues]
print(f"Clean files ({len(clean)}): {', '.join(clean)}")
print(f"{'='*70}")
