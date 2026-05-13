"""
Convert loose C++/C# code paragraphs to fenced code blocks.

Only targets lines that are clearly function-body code (not prose mentioning APIs):
- Starts with return type + function name (void Foo::Bar...)
- Standalone braces { or }
- Control flow: if (, for (, while (, return
- Variable declarations starting with known types

Works by finding "code runs" - contiguous blocks (blank lines allowed between)
where the first line is an unambiguous code start, and subsequent lines
look like code. Wraps the whole run in ```cpp ... ```.
"""

import re
from pathlib import Path

MD_UNESCAPE = re.compile(r'\\(.)')

def unescape(s):
    return MD_UNESCAPE.sub(r'\1', s)

# These patterns identify lines that are UNAMBIGUOUSLY code (not prose mentioning APIs)
STRONG_CODE_START = re.compile(r'''
    ^(?:
        # C++ function definition: ReturnType Name::Name( or ReturnType Name(
        (?:(?:virtual|static|const|inline|explicit)\s+)?
        (?:bool|void|int|char|double|float|long|unsigned|BOOL|UINT|DWORD|HRESULT|
           TSL\w+|TSLN\w+|CString|CPoint|CRect|CDC|HDC|HWND|HBITMAP|std::\w+|
           QString|QWidget|QSize|Display|WId|XWindowAttributes)\s*\*?\s+\w+\s*[:(]
        |
        # Control flow
        (?:if|for|while|else|return|switch|case|break|continue|do)\s*[\(\{]?
        |
        # Standalone brace or semicolon
        [{}];?
        |
        # Preprocessor
        \#\s*(?:include|ifdef|ifndef|endif|define|elif|else|pragma)\b
        |
        # MFC/Windows specific
        (?:BOOL|UINT|DWORD|LRESULT|HRESULT)\s+\w+
        |
        # Assignment with new
        \w+\s*=\s*new\s+\w+
        |
        # Standalone function call ending with ; (e.g. setAttribute(...);)
        [a-z]\w+\s*\(.*\)\s*;?\s*$
        |
        # VB.NET function start
        (?:Public|Private|Protected)\s+(?:Sub|Function|Overrides)
        |
        # End statements
        End\s+(?:Sub|Function|If|Class)
    )
''', re.VERBOSE | re.IGNORECASE)

def is_strong_code(line):
    s = unescape(line.strip())
    return bool(STRONG_CODE_START.match(s))

def is_any_code(line):
    """Weaker check — is this line plausibly code (not strong prose)?"""
    s = unescape(line.strip())
    if not s:
        return False
    # Exclude clear prose: starts with capital word followed by space (sentence start)
    # but NOT function name patterns
    if re.match(r'^[A-Z][a-z]+ [a-z]', s):
        # Could be prose like "When your..." or code like "TSLFoo bar"
        # If it has :: or -> it might still be code
        if not re.search(r'::|->|;$|\{|\}', s):
            return False
    if re.search(r'//', s):        return True
    if re.search(r'::|->', s) and not re.match(r'^[A-Z][a-z]', s): return True
    if re.match(r'^[{};]\s*$', s): return True
    if re.search(r';\s*$', s) and re.search(r'[()[\]{}=]', s): return True
    # Variable declaration: TypeName varname; or TypeName *varname;
    if re.match(r'^[A-Z]\w+\s+\*?\w+\s*;', s): return True
    if re.match(r'#\s*(include|ifdef|ifndef|endif|define|elif|else|pragma)\b', s): return True
    if re.search(r'\bnew\s+[A-Z]\w+', s): return True
    if is_strong_code(line): return True
    return False

def detect_lang(lines):
    joined = '\n'.join(lines)
    if re.search(r'\b(Public Sub|Private Sub|End Sub|Dim\s+\w+\s+As)\b', joined, re.I):
        return 'vb'
    if re.search(r'\b(namespace|using\s+\w+\.\w+;)\b', joined):
        return 'csharp'
    return 'cpp'

def convert_file(path):
    text = path.read_text(encoding='utf-8', errors='replace')
    lines = text.split('\n')
    out = []
    i = 0
    in_fence = False
    changes = 0

    while i < len(lines):
        l = lines[i]

        # Track fenced code blocks — don't touch content inside them
        if l.strip().startswith('```'):
            in_fence = not in_fence
            out.append(l)
            i += 1
            continue

        if in_fence or l.startswith('>') or l.startswith('|'):
            out.append(l)
            i += 1
            continue

        # Check if this line is a strong code start (and not already in a fence)
        if is_strong_code(l):
            # Collect the full code run
            # A run continues as long as lines are: code, blank, or code
            # We stop when we hit 2+ blank lines or a clear prose line
            run = [l]
            j = i + 1
            consecutive_blanks = 0

            while j < len(lines):
                nxt = lines[j]
                if nxt.strip() == '':
                    consecutive_blanks += 1
                    if consecutive_blanks >= 2:
                        break
                    run.append(nxt)
                    j += 1
                elif nxt.strip().startswith('```'):
                    break
                elif nxt.startswith('>') or nxt.startswith('|'):
                    break
                elif nxt.startswith('#') and not re.match(
                        r'#\s*(include|ifdef|ifndef|endif|define|elif|else|pragma)\b',
                        nxt.strip()):
                    # Real markdown heading — stop the run
                    break
                elif is_any_code(nxt):
                    consecutive_blanks = 0
                    run.append(nxt)
                    j += 1
                else:
                    # Prose line — stop if we haven't seen code recently
                    # Allow 1 prose line if it's very short (continuation)
                    break

            # Only wrap if run has at least 2 meaningful lines
            code_lines = [x for x in run if x.strip()]
            if len(code_lines) >= 2:
                # Strip trailing blank lines from run
                while run and not run[-1].strip():
                    run.pop()

                lang = detect_lang([unescape(x) for x in run])
                out.append(f'```{lang}')
                for rl in run:
                    out.append(unescape(rl))
                out.append('```')
                changes += 1
                i = j
                continue

        out.append(l)
        i += 1

    return '\n'.join(out), changes


FILES = [
    'walkthrough-1.md',
    'walkthrough-2.md',
    'walkthrough-3.md',
    'threading.md',
    'net-sdks.md',
    'ogc-services-sdk.md',
]

pages = Path(__file__).parent.parent / 'pages' / 'developers-guide'

for fname in FILES:
    path = pages / fname
    result, changes = convert_file(path)
    if changes:
        path.write_text(result, encoding='utf-8')
        print(f'{fname}: {changes} code block(s) wrapped')
    else:
        print(f'{fname}: no changes')
