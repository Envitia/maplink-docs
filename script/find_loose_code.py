"""Find code lines that are outside fenced code blocks and blockquotes."""
import re
from pathlib import Path

MD_UNESCAPE = re.compile(r'\\(.)')

def unescape(s):
    return MD_UNESCAPE.sub(r'\1', s)

def is_code_line(raw):
    s = unescape(raw.strip())
    if not s:
        return False
    if re.search(r'//', s):                                              return True
    if re.search(r'::|->', s):                                           return True
    if re.match(r'^[{};]\s*$', s):                                       return True
    if re.search(r';\s*$', s) and re.search(r'[()[\]{}=]', s):          return True
    if re.match(r'#\s*(include|ifdef|ifndef|endif|define|elif|else)\b', s): return True
    if re.search(r'\bnew\s+[A-Z]\w+', s):                               return True
    if re.search(r'\bclass\s+\w+\s*:', s):                              return True
    if re.search(r'\b(virtual|explicit)\s+\w', s):                      return True
    if re.search(r'\b(Public|Private)\s+(Sub|Function)\b', s, re.I):   return True
    if re.search(r'\bEnd\s+(Sub|Function|If)\b', s, re.I):             return True
    return False

pages = Path('pages/developers-guide')
for md in sorted(pages.glob('*.md')):
    if md.name == 'index.md':
        continue
    text = md.read_text(encoding='utf-8', errors='replace')
    lines = text.split('\n')
    in_fence = False
    loose = []
    for i, l in enumerate(lines):
        stripped = l.strip()
        if stripped.startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if l.startswith('>'):
            continue
        if l.startswith('|'):
            continue
        if is_code_line(l):
            loose.append((i+1, stripped[:80]))

    if loose:
        print(f'\n{md.name}: {len(loose)} loose code line(s)')
        for ln, txt in loose[:8]:
            print(f'  L{ln}: {txt}')
        if len(loose) > 8:
            print(f'  ... and {len(loose)-8} more')
