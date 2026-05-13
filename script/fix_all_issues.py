"""
Fixes all rendering issues found in the audit:
  1. Blockquote runs containing code → fenced code blocks
  2. Dead CHM / ms-help links → plain text
  3. Footnote definitions misplaced in threading.md → move to correct files
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAGES = ROOT / "pages" / "developers-guide"


# ─── helpers ──────────────────────────────────────────────────────────────────

MD_UNESCAPE = re.compile(r'\\([\\`*_{}\[\]()#+\-.!<>|~^])')

def unescape_md(text):
    """Remove markdown backslash escapes — needed inside fenced code blocks."""
    return MD_UNESCAPE.sub(r'\1', text)

def detect_lang(lines):
    """Guess code language from content."""
    joined = '\n'.join(lines)
    if re.search(r'\b(Public Sub|Private Sub|Protected Overrides|Dim\s+\w+\s+As|End Sub|End Function)\b', joined, re.I):
        return 'vb'
    if re.search(r'\b(using\s+\w+\.\w+;|namespace\s+\w+|Console\.)', joined):
        return 'csharp'
    return 'cpp'

def is_code_line(line):
    """Return True if a stripped content line looks like source code."""
    raw = line.strip()
    if not raw:
        return False
    # Unescape markdown escapes before testing — e.g. \> becomes -> detectable
    s = unescape_md(raw)
    if re.search(r'//', s):                                          return True  # C++ comment
    if re.search(r'::|->', s):                                       return True  # scope/pointer
    if re.match(r'^[{};]\s*$', s):                                   return True  # lone brace/semi
    if re.search(r';\s*$', s) and re.search(r'[()[\]{}=]', s):      return True  # statement
    if re.search(r'[a-zA-Z)>_]\s*;\s*$', s):                        return True  # ends with ;
    if re.match(r'#\s*(include|ifdef|ifndef|endif|define|elif|else|pragma)\b', s): return True
    if re.search(r'\bnew\s+[A-Z]\w+', s):                           return True  # new Obj
    # C++ class/struct declarations and keywords
    if re.search(r'\bclass\s+\w+.*:', s):                            return True  # class X : base
    if re.search(r'\b(virtual|explicit|inline|const|static)\s+\w', s): return True
    if re.search(r'\b(public|private|protected)\s*:', s):            return True  # access specifier
    if re.match(r'\w+\s*\(\s*(void\s*)?\)\s*;?\s*$', s):            return True  # Foo() or Foo(void)
    # VB.NET
    if re.search(r'\b(Public|Private|Protected|Friend)\s+(Sub|Function|Class|Property|Overrides|Shared|ReadOnly)\b', s, re.I): return True
    if re.search(r'\bEnd\s+(Sub|Function|If|Class|Try|Module)\b', s, re.I):  return True
    if re.search(r'\bDim\s+\w+\s*(As|=)', s, re.I):                 return True
    if re.search(r'\b(AddressOf|RaiseEvent|WithEvents|Handles)\b', s, re.I): return True
    # C# specific
    if re.search(r'\b(namespace|using)\s+\w', s):                    return True
    if re.search(r'\b(override|virtual|abstract|readonly|partial)\s+\w', s): return True
    return False

def bq_run_is_code(content_lines):
    """Return True if a blockquote run (stripped of '> ') contains code."""
    code_count = sum(1 for l in content_lines if is_code_line(l))
    return code_count >= 1

def convert_bq_run(bq_raw_lines):
    """
    Convert a blockquote run to the appropriate output.
    bq_raw_lines: the raw '> ...' lines.
    Returns a list of output strings.
    """
    # Strip the '> ' prefix to get content
    content = []
    for l in bq_raw_lines:
        if l.startswith('> '):
            content.append(l[2:])
        elif l == '>':
            content.append('')
        else:
            content.append(l)

    if not bq_run_is_code(content):
        # Keep as blockquote unchanged
        return bq_raw_lines

    # Find first code line
    first_code = next((i for i, l in enumerate(content) if is_code_line(l)), 0)

    out = []

    # Any prose lines before the first code line → regular paragraphs
    prose_lines = content[:first_code]
    if any(l.strip() for l in prose_lines):
        out.append('\n'.join(prose_lines).strip())
        out.append('')

    # Code lines (from first_code onwards)
    code_lines = content[first_code:]
    # Strip trailing blank lines
    while code_lines and not code_lines[-1].strip():
        code_lines.pop()

    if code_lines:
        lang = detect_lang(code_lines)
        out.append(f'```{lang}')
        for cl in code_lines:
            out.append(unescape_md(cl))
        out.append('```')

    return out


def fix_blockquotes(text):
    """Convert code-containing blockquote runs to fenced code blocks."""
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('> ') or l == '>':
            # Collect the full blockquote run
            run = []
            while i < len(lines) and (lines[i].startswith('> ') or lines[i] == '>'):
                run.append(lines[i])
                i += 1
            converted = convert_bq_run(run)
            out.extend(converted)
        else:
            out.append(l)
            i += 1
    return '\n'.join(out)


# ─── CHM link removal ─────────────────────────────────────────────────────────

CHM_LINK = re.compile(r'\[([^\]]+)\]\(mk:@MSITStore:[^)]+\)')

def fix_chm_links(text):
    """Replace [text](mk:@MSITStore:...) with just the link text."""
    return CHM_LINK.sub(r'\1', text)


# ─── Footnote redistribution ──────────────────────────────────────────────────

# All footnote definitions ended up in threading.md.
# References: [^1]-[^5] are in unicode.md, [^6]-[^8] in ddo-sdk.md,
#             [^9]-[^10] in gml-sdk.md.

FOOTNOTE_FILES = {
    'unicode.md':   [1, 2, 3, 4, 5],
    'ddo-sdk.md':   [6, 7, 8],
    'gml-sdk.md':   [9, 10],
}

def extract_footnote_defs(text):
    """Return dict {n: full_definition_line} and text with those definitions removed."""
    defs = {}
    lines = text.split('\n')
    kept = []
    for l in lines:
        m = re.match(r'^\[\^(\d+)\]:(.*)', l)
        if m:
            defs[int(m.group(1))] = l
        else:
            kept.append(l)
    # Remove trailing blank lines that may remain after removing defs
    while kept and kept[-1].strip() == '':
        kept.pop()
    return defs, '\n'.join(kept)

def append_footnote_defs(text, defs, numbers):
    """Append the given footnote definitions to the file text."""
    lines_to_add = [defs[n] for n in sorted(numbers) if n in defs]
    if not lines_to_add:
        return text
    return text.rstrip('\n') + '\n\n' + '\n\n'.join(lines_to_add) + '\n'


def fix_footnotes():
    threading_path = PAGES / 'threading.md'
    threading_text = threading_path.read_text(encoding='utf-8')

    all_defs, threading_stripped = extract_footnote_defs(threading_text)

    if not all_defs:
        print('  threading.md: no footnote definitions found — skipping')
        return

    for fname, numbers in FOOTNOTE_FILES.items():
        fpath = PAGES / fname
        text = fpath.read_text(encoding='utf-8')
        # Check if this file actually has refs to these footnotes
        refs_present = [n for n in numbers if f'[^{n}]' in text]
        if not refs_present:
            print(f'  {fname}: no refs found for footnotes {numbers} — skipping')
            continue
        text = append_footnote_defs(text, all_defs, refs_present)
        fpath.write_text(text, encoding='utf-8')
        print(f'  {fname}: added footnote defs for [^{refs_present}]')

    # Write threading.md without the now-relocated definitions
    threading_path.write_text(threading_stripped + '\n', encoding='utf-8')
    remaining = [n for n in all_defs if not any(n in nums for nums in FOOTNOTE_FILES.values())]
    if remaining:
        print(f'  threading.md: WARNING — leftover defs not relocated: {remaining}')
    else:
        print('  threading.md: all footnote defs relocated, removed from file')


# ─── main ─────────────────────────────────────────────────────────────────────

BLOCKQUOTE_FILES = [
    'net-sdks.md',
    'ogc-services-sdk.md',
    'threading.md',
]

CHM_FILES = []  # already done

print('-- Blockquote -> code block conversion --')
for fname in BLOCKQUOTE_FILES:
    path = PAGES / fname
    original = path.read_text(encoding='utf-8')
    fixed = fix_blockquotes(original)
    if fixed != original:
        path.write_text(fixed, encoding='utf-8')
        before = len(re.findall(r'^>', original, re.MULTILINE))
        after  = len(re.findall(r'^>', fixed,    re.MULTILINE))
        print(f'  {fname}: blockquote lines {before} -> {after}')
    else:
        print(f'  {fname}: no changes')

print()
print('-- CHM link removal --')
for fname in CHM_FILES:
    path = PAGES / fname
    original = path.read_text(encoding='utf-8')
    fixed = fix_chm_links(original)
    if fixed != original:
        path.write_text(fixed, encoding='utf-8')
        n = len(CHM_LINK.findall(original))
        print(f'  {fname}: removed {n} CHM link(s)')
    else:
        print(f'  {fname}: no CHM links found')

print()
print('-- Footnote redistribution --')
fix_footnotes()

print()
print('Done.')
