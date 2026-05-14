"""Fix all bare C++ code blocks in opengl-drawing-surface.md by wrapping them in fences."""

with open(r'c:/maplink/maplink-docs/pages/developers-guide/opengl-drawing-surface.md', 'rb') as f:
    content = f.read()

all_lines = content.split(b'\r\n')
total = len(all_lines)
print(f'Total lines: {total}')

def unescape(line):
    """Strip blockquote prefix and unescape Word-conversion operators."""
    if line.startswith(b'> '):
        line = line[2:]
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
    return line

# (start_1idx, end_1idx, lang_bytes)
code_blocks = [
    (219, 267, b'cpp'),   # Platform setup: X11 + Windows preprocessor
    (273, 313, b'cpp'),   # Drawing surface creation: GLX/WGL + context check
    (323, 333, b'cpp'),   # Map data layer creation
    (339, 371, b'cpp'),   # Mode manager creation + error handling
    (381, 405, b'cpp'),   # Window resize handler
    (415, 433, b'cpp'),   # Drawing handler (drawDU + onDraw)
    (451, 473, b'cpp'),   # Map loading (loadData + resetViews)
    (477, 489, b'cpp'),   # Reset view (rotate + reset)
    (505, 551, b'cpp'),   # Three activation methods (Pan/Zoom/Grab)
    (579, 605, b'cpp'),   # TMC extent + getOption + TMCperDU
    (619, 681, b'cpp'),   # drawLayer: matrix positioning + glUniform
    (689, 719, b'cpp'),   # drawLayer: flushPendingDraws + depth test
    (725, 769, b''),      # GLSL vertex + fragment shaders
    (931, 1023, b'cpp'),  # createFBO() function
    (1027, 1065, b'cpp'), # draw() function: draw to texture
    (1073, 1157, b'cpp'), # GLX Pbuffer windowless rendering
    (1163, 1223, b'cpp'), # EGL Pbuffer windowless rendering
    (1323, 1323, b'cpp'), # glPolygonMode one-liner
    (1369, 1399, b'cpp'), # Original migration code (Windows + X11)
    (1403, 1453, b'cpp'), # Replacement migration code (Windows + X11)
    (1493, 1517, b'cpp'), # XVisualInfo alpha channel manipulation
]

# Build lookup: 1-indexed line number -> (start, end, lang)
in_block = {}
for start, end, lang in code_blocks:
    for n in range(start, end + 1):
        in_block[n] = (start, end, lang)

# Process
result = []
i = 0
while i < len(all_lines):
    n = i + 1  # 1-indexed
    if n in in_block and in_block[n][0] == n:
        start, end, lang = in_block[n]
        fence = b'```' + lang
        result.append(fence)
        for j in range(start - 1, end):     # j is 0-indexed
            raw = all_lines[j].rstrip()
            if raw:                          # skip blank lines within block
                result.append(unescape(raw))
        result.append(b'```')
        i = end   # next 0-indexed position after block
        continue
    elif n in in_block:
        # Middle of block - already consumed above; skip (safety)
        i += 1
        continue
    result.append(all_lines[i].rstrip())
    i += 1

output = b'\r\n'.join(result)
if content.endswith(b'\r\n'):
    output += b'\r\n'

with open(r'c:/maplink/maplink-docs/pages/developers-guide/opengl-drawing-surface.md', 'wb') as f:
    f.write(output)

print(f'Done. Output lines: {len(result)}')
print(f'Lines reduced by: {total - len(result)}')

# Verify fences
fence_lines = [(i+1, r.decode(errors="replace")) for i, r in enumerate(result) if r.startswith(b'```')]
print(f'\nFence markers ({len(fence_lines)} total, expect {len(code_blocks)*2}):')
for ln, txt in fence_lines:
    print(f'  L{ln}: {txt[:60]}')
