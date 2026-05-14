"""Fix bare code blocks in editor-sdk.md"""

with open(r'c:\maplink\maplink-docs\pages\developers-guide\editor-sdk.md', 'rb') as f:
    content = f.read()

fixes = []

# Fix E1: single-line activate call bare
fixes.append(('E1 m_editor activate',
    b'm_editor-\\>activate("polygon");\r\n\r\nAn application can pass',
    b'```cpp\r\nm_editor->activate("polygon");\r\n```\r\n\r\nAn application can pass'
))

# Fix E2: two-line rendering attributes + activate bare
fixes.append(('E2 TSLRenderingAttributes + activate',
    b'TSLRenderingAttributes ra ; // Now configure rendering attributes\r\n\r\n'
    b'editor-\\>activate("renderingattributes", &ra);',
    b'```cpp\r\n'
    b'TSLRenderingAttributes ra ; // Now configure rendering attributes\r\n\r\n'
    b'editor->activate("renderingattributes", &ra);\r\n'
    b'```'
))

# Fix E3: blockquote code line - change to proper code fence (non-breaking spaces in original)
fixes.append(('E3 blockquote editMode activate',
    b'> m_editMode-\\>editor()-\\>activate(\xc2\xa0"polygon",\xc2\xa00\xc2\xa0)\xc2\xa0;',
    b'```cpp\r\nm_editMode->editor()->activate( "polygon", 0 ) ;\r\n```'
))

for name, old, new in fixes:
    found = old in content
    print(f'{name}: found={found}')
    if found:
        content = content.replace(old, new, 1)
    else:
        print(f'  first 60: {old[:60]}')
        print(f'  first 60 found: {old[:60] in content}')

with open(r'c:\maplink\maplink-docs\pages\developers-guide\editor-sdk.md', 'wb') as f:
    f.write(content)
print('editor-sdk.md written')
