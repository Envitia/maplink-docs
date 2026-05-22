"""
Generates _data/api_search.json from Doxygen HTML files in api/cpp/ and api/dotnet/.
Run from the repo root: python scripts/generate_api_search.py
"""

import os
import re
import json

# Files that are index/listing pages, not individual API entries
SKIP_PATTERNS = re.compile(
    r'(-members|annotated|classes|classindex|files|functions|globals|'
    r'hierarchy|index|namespaces|namespacemembers|topics|pages|'
    r'group__|dir_|struct_all|union_all|deprecated).*\.html$',
    re.IGNORECASE
)

TITLE_RE = re.compile(r'<div class="title">(.*?)(?:<div|</div>)', re.DOTALL)
TEXTBLOCK_RE = re.compile(r'<div class="textblock">(.*?)</div>', re.DOTALL)
# Anchor + memtitle pairs for method extraction
METHOD_RE = re.compile(
    r'<a id="([a-f0-9]+)"[^>]*></a>\s*'
    r'<h2 class="memtitle"><span class="permalink">.*?</span>(.*?)</h2>',
    re.DOTALL
)
OVERLOAD_RE = re.compile(r'\s*<span class="overload">.*?</span>', re.DOTALL)
TAG_RE = re.compile(r'<[^>]+>')
WHITESPACE_RE = re.compile(r'\s+')

def clean(html):
    return WHITESPACE_RE.sub(' ', TAG_RE.sub('', html)).strip()

def extract_entries(filepath, url_prefix):
    with open(filepath, encoding='utf-8', errors='ignore') as f:
        content = f.read()

    title_m = TITLE_RE.search(content)
    if not title_m:
        return []
    class_title = clean(title_m.group(1))
    if not class_title:
        return []

    # Strip "Class Reference" / "Struct Reference" suffix for brevity in method labels
    class_name = re.sub(r'\s+(Class|Struct|Union|Interface) Reference$', '', class_title).strip()

    brief = ''
    tb_m = TEXTBLOCK_RE.search(content)
    if tb_m:
        p_m = re.search(r'<p>(.*?)</p>', tb_m.group(1), re.DOTALL)
        if p_m:
            brief = clean(p_m.group(1))[:300]

    filename = os.path.basename(filepath)
    base_url = url_prefix.lstrip('/') + filename

    entries = [{
        'title': class_title,
        'url': base_url,
        'content': brief,
    }]

    # Extract methods — deduplicate overloads by method name
    seen_methods = set()
    for anchor_id, raw_name in METHOD_RE.findall(content):
        method_name = clean(OVERLOAD_RE.sub('', raw_name))
        if not method_name or method_name in seen_methods:
            continue
        seen_methods.add(method_name)
        entries.append({
            'title': method_name + ' — ' + class_name,
            'url': base_url + '#' + anchor_id,
            'content': '',
        })

    return entries

def collect(source_dir, url_prefix):
    entries = []
    if not os.path.isdir(source_dir):
        print(f'  Skipping {source_dir} (not found)')
        return entries
    for filename in sorted(os.listdir(source_dir)):
        if not filename.endswith('.html'):
            continue
        if SKIP_PATTERNS.search(filename):
            continue
        entries += extract_entries(os.path.join(source_dir, filename), url_prefix)
    return entries

if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    entries = []
    print('Collecting C++ API pages...')
    entries += collect(os.path.join(root, 'api', 'cpp'),    '/api/cpp/')
    print(f'  {len(entries)} entries so far')
    print('Collecting .NET API pages...')
    entries += collect(os.path.join(root, 'api', 'dotnet'), '/api/dotnet/')
    print(f'  {len(entries)} total entries')

    out = os.path.join(root, '_data', 'api_search.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f'Written to {out}')
