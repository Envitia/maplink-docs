with open(r'c:/maplink/maplink-docs/pages/developers-guide/opengl-drawing-surface.md', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

in_fence = False
groups = []
current = []

for i, line in enumerate(lines, 1):
    s = line.rstrip()
    if s.startswith('```'):
        in_fence = not in_fence
        if current:
            groups.append(current[:])
            current = []
    if not in_fence and ('-\\>' in s or '\\*' in s or '\\[' in s):
        current.append(i)

if current:
    groups.append(current)

for g in groups:
    print(f'Lines {g[0]}-{g[-1]} ({len(g)} bare lines)')
    # Show first/last
    for ln in g[:2]:
        print(f'  L{ln}: {lines[ln-1].rstrip()[:80]}')
    if len(g) > 4:
        print(f'  ...')
    for ln in g[-2:] if len(g) > 2 else []:
        print(f'  L{ln}: {lines[ln-1].rstrip()[:80]}')
    print()
