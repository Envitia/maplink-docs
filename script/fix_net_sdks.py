"""Fix code block boundaries in net-sdks.md"""

with open(r'c:\maplink\maplink-docs\pages\developers-guide\net-sdks.md', 'rb') as f:
    content = f.read()

fixes = []

# Fix N1a: C# Form1 - method signature bare before ```cpp
fixes.append(('N1a Form1 signature',
    b'public Form1()\r\n\r\n```cpp\r\n{',
    b'```cpp\r\npublic Form1()\r\n\r\n{'
))

# Fix N1b: C# Form1 - closing } bare after ```
fixes.append(('N1b Form1 closing brace',
    b'InitializeComponent();\r\n```\r\n\r\n}',
    b'InitializeComponent();\r\n\r\n}\r\n```'
))

# Fix N2: openToolStripMenuItem_Click - signature bare before ```cpp
fixes.append(('N2 openToolStripMenuItem_Click',
    b'private void openToolStripMenuItem_Click(object sender, EventArgs e)\r\n\r\n```cpp\r\n{',
    b'```cpp\r\nprivate void openToolStripMenuItem_Click(object sender, EventArgs e)\r\n\r\n{'
))

# Fix N3a: OnPaint - signature bare before ```cpp
fixes.append(('N3a OnPaint signature',
    b'private void OnPaint(object sender, PaintEventArgs e)\r\n\r\n```cpp\r\n{',
    b'```cpp\r\nprivate void OnPaint(object sender, PaintEventArgs e)\r\n\r\n{'
))

# Fix N3b: OnPaint - closing } bare after ```
fixes.append(('N3b OnPaint closing brace',
    b'e.ClipRectangle.Bottom,true);\r\n```\r\n\r\n}',
    b'e.ClipRectangle.Bottom,true);\r\n\r\n}\r\n```'
))

# Fix N4: OnResize - signature bare before ```cpp (body+} already inside)
fixes.append(('N4 OnResize signature',
    b'private void OnResize(object sender, EventArgs e)\r\n\r\n```cpp\r\n{',
    b'```cpp\r\nprivate void OnResize(object sender, EventArgs e)\r\n\r\n{'
))

# Fix N5a: VB Sub New - errant closing ``` after errorString(
fixes.append(('N5a VB Sub New errorString split',
    b'Dim msg As String = TSLNErrorStack.errorString(\r\n```\r\n',
    b'Dim msg As String = TSLNErrorStack.errorString(\r\n'
))

# Fix N5b: VB Sub New - errant ```cpp fence before End If
fixes.append(('N5b VB Sub New End If split',
    b'Environment.Exit(-1)\r\n\r\n```cpp\r\nEnd If',
    b'Environment.Exit(-1)\r\n\r\nEnd If'
))

# Fix N5c: VB Sub New - closing ``` before End Sub; move to after End Sub
fixes.append(('N5c VB Sub New End Sub',
    b'InitializeComponent()\r\n```\r\n\r\nEnd Sub',
    b'InitializeComponent()\r\n\r\nEnd Sub\r\n```'
))

# Fix N6a: VB Form1_Resize - errant closing ``` after True,
fixes.append(('N6a VB Form1_Resize True split',
    b'True,\r\n```\r\n\r\nTSLNResizeActionEnum',
    b'True,\r\n\r\nTSLNResizeActionEnum'
))

# Fix N6b: VB Form1_Resize - errant ```vb opening before End Sub
fixes.append(('N6b VB Form1_Resize End Sub split',
    b'MaintainCentre)\r\n\r\n```vb\r\nEnd Sub\r\n```',
    b'MaintainCentre)\r\n\r\nEnd Sub\r\n```'
))

# Fix N7: VB OnPaintBackground - entire method is bare, not wrapped in fence
fixes.append(('N7 VB OnPaintBackground',
    b"Protected Overrides Sub OnPaintBackground(ByVal pevent As PaintEventArgs)\r\n\r\n"
    b"' do nothing\\...\r\n\r\n"
    b"' we don't want the background to flash over the map\r\n\r\n"
    b"End Sub",
    b"```vb\r\n"
    b"Protected Overrides Sub OnPaintBackground(ByVal pevent As PaintEventArgs)\r\n\r\n"
    b"' do nothing\\...\r\n\r\n"
    b"' we don't want the background to flash over the map\r\n\r\n"
    b"End Sub\r\n"
    b"```"
))

for name, old, new in fixes:
    found = old in content
    print(f'{name}: found={found}')
    if found:
        content = content.replace(old, new, 1)
    else:
        print(f'  first 60: {old[:60]}')
        print(f'  first 60 found: {old[:60] in content}')

with open(r'c:\maplink\maplink-docs\pages\developers-guide\net-sdks.md', 'wb') as f:
    f.write(content)
print('net-sdks.md written')
