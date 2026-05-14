with open(r'c:/maplink/maplink-docs/pages/developers-guide/opengl-drawing-surface.md', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
print(f'Total lines: {len(lines)}')
print('Fence markers:')
for i, line in enumerate(lines, 1):
    s = line.rstrip()
    if s.startswith('`' * 3):
        print(f'  L{i}: {s[:60]}')
