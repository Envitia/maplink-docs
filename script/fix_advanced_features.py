"""Fix bare C++ code blocks in advanced-features.md."""

with open(r'c:/maplink/maplink-docs/pages/developers-guide/advanced-features.md', 'rb') as f:
    content = f.read()

lines = content.split(b'\r\n')
print(f'Total lines: {len(lines)}')

def unescape(line):
    """Unescape Word-conversion artifacts for C++ code."""
    if line.startswith(b'> '):
        line = line[2:]
    line = line.replace(b'\xc2\xa0', b' ')   # non-breaking space -> regular space
    line = line.replace(b'-\\>', b'->')
    line = line.replace(b'\\*', b'*')
    line = line.replace(b'\\[', b'[')
    line = line.replace(b'\\]', b']')
    line = line.replace(b'\\~', b'~')
    line = line.replace(b'\\...', b'...')
    line = line.replace(b'\\|', b'|')
    line = line.replace(b'\\^', b'^')
    line = line.replace(b'\\<', b'<')
    line = line.replace(b'\\>', b'>')
    line = line.replace(b'\\#', b'#')
    line = line.replace(b'\\_', b'_')
    line = line.replace(b'\\\\', b'\\')     # double backslash -> single (path separators)
    line = line.replace(b"\\'", b"'")       # escaped apostrophe -> apostrophe
    return line

# (start_1idx, end_1idx, lang)
code_blocks = [
    (1069, 1155, b'cpp'),  # TSLEntitySet iteration: retrieve Name attribute
    (1163, 1221, b'cpp'),  # TSLSeamlessLayerManager: layer history management
    (1249, 1339, b'cpp'),  # TSLRasterFilterDataLayer: filter data layer example
]

in_block = {}
for start, end, lang in code_blocks:
    for n in range(start, end + 1):
        in_block[n] = (start, end, lang)

result = []
i = 0
while i < len(lines):
    n = i + 1
    if n in in_block and in_block[n][0] == n:
        start, end, lang = in_block[n]
        result.append(b'```' + lang)
        for j in range(start - 1, end):
            raw = lines[j].rstrip()
            if raw and raw.replace(b'\xc2\xa0', b''):  # skip lines that are only nbsp
                result.append(unescape(raw))
        result.append(b'```')
        i = end
        continue
    elif n in in_block:
        i += 1
        continue
    result.append(lines[i].rstrip())
    i += 1

output = b'\r\n'.join(result)
if content.endswith(b'\r\n'):
    output += b'\r\n'

with open(r'c:/maplink/maplink-docs/pages/developers-guide/advanced-features.md', 'wb') as f:
    f.write(output)

print(f'Done. Output lines: {len(result)}')

# Verify new fences
new_fences = [(i+1, r.decode(errors='replace')) for i, r in enumerate(result)
              if r.startswith(b'```')]
print(f'\nAll fences ({len(new_fences)} total):')
for ln, txt in new_fences:
    print(f'  L{ln}: {txt[:60]}')
