"""Analyze opengl-drawing-surface.md to identify code block boundaries"""
import re

with open(r'c:/maplink/maplink-docs/pages/developers-guide/opengl-drawing-surface.md', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

CODE_INDICATORS = [
    r'-\\>',         # escaped arrow
    r'\\\*',         # escaped star (pointer)
    r'\\[',          # escaped bracket
    r'^//',          # C++ comment
    r'^\s*#',        # preprocessor
    r'^\s*\{',       # opening brace
    r'^\s*\}',       # closing brace
    r';\s*$',        # semicolon at end
    r'^[a-zA-Z_:]+[*&\s]+\w+\s*[=({\[]',  # type declarations
    r'\bif\s*\(',    # if statement
    r'\bfor\s*\(',   # for loop
    r'\bwhile\s*\(', # while loop
    r'\bnew\s+\w',   # new keyword
    r'\breturn\b',   # return statement
    r'glPush|glPop|glEnable|glDisable|glVertex|glDraw|glColor|glUniform',  # GL calls
    r'#ifdef|#else|#endif|#define|#version',  # preprocessor
    r'^extern\b',    # extern
    r'^\s*GL[A-Z]',  # GL types
    r'TSL[A-Z].*->',  # MapLink methods
]
CODE_RE = re.compile('|'.join(CODE_INDICATORS))

PROSE_RE = re.compile(r'^[A-Z][a-z]|^The |^This |^In |^When |^Note|^After |^Each |^If ')

in_code = False
blocks = []
block_start = None

for i, line in enumerate(lines, 1):
    s = line.rstrip()

    # Skip empty lines (ambiguous)
    if not s:
        continue

    # Skip headers and list items
    if s.startswith('#') or s.startswith('- ') or s.startswith('>') or re.match(r'^\d+\.', s):
        if in_code:
            blocks.append((block_start, i-1))
            in_code = False
        continue

    is_code = bool(CODE_RE.search(s))
    is_prose = bool(PROSE_RE.match(s)) and not is_code

    if is_code and not in_code:
        in_code = True
        block_start = i
    elif is_prose and in_code:
        blocks.append((block_start, i-1))
        in_code = False

if in_code:
    blocks.append((block_start, len(lines)))

print('Detected code blocks:')
for start, end in blocks:
    # Find actual start and end (skip empty lines at edges)
    while start <= end and not lines[start-1].rstrip():
        start += 1
    while end >= start and not lines[end-1].rstrip():
        end -= 1
    if start <= end:
        print(f'  Lines {start}-{end}:')
        print(f'    first: {lines[start-1].rstrip()[:70]}')
        print(f'    last:  {lines[end-1].rstrip()[:70]}')
