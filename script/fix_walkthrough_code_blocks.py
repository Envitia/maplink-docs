"""Fix code-as-blockquote and bare-code issues in walkthrough-2 and walkthrough-3."""

### --- walkthrough-2.md ---
with open(r'c:\maplink\maplink-docs\pages\developers-guide\walkthrough-2.md', 'rb') as f:
    wt2 = f.read()

# Fix 1: Bare constructor header + init-list before a { } fence
old1 = (b'CHelloGlobeView::CHelloGlobeView()\r\n\r\n'
        b': m_drawingSurface(NULL), m_grabbed(false), m_checkForGrab(false)\r\n\r\n'
        b'```cpp\r\n{\r\n\r\n}\r\n```')
new1 = (b'```cpp\r\nCHelloGlobeView::CHelloGlobeView()\r\n\r\n'
        b': m_drawingSurface(NULL), m_grabbed(false), m_checkForGrab(false)\r\n\r\n'
        b'{\r\n\r\n}\r\n```')

# Fix 2: Split OnMouseMove — close-fence + bare escaped lines + re-open-fence
#   file bytes: \| = 0x5c 0x7c,  \> = 0x5c 0x3e
old2 = (b'if ( m_checkForGrab\r\n```\r\n'
        b'&& ( m_grabbed \x5c|\x5c| abs( point.x - m_rmb.x ) \x5c> 3\r\n\r\n'
        b'\x5c|\x5c| abs( point.y - m_rmb.y ) \x5c> 3 ) )\r\n\r\n'
        b'```cpp\r\n{')
new2 = (b'if ( m_checkForGrab\r\n\r\n'
        b'&& ( m_grabbed || abs( point.x - m_rmb.x ) > 3\r\n\r\n'
        b'|| abs( point.y - m_rmb.y ) > 3 ) )\r\n\r\n{')

print('wt2 fix1 found:', old1 in wt2)
print('wt2 fix2 found:', old2 in wt2)

wt2 = wt2.replace(old1, new1, 1).replace(old2, new2, 1)
with open(r'c:\maplink\maplink-docs\pages\developers-guide\walkthrough-2.md', 'wb') as f:
    f.write(wt2)
print('walkthrough-2.md written')

### --- walkthrough-3.md ---
with open(r'c:\maplink\maplink-docs\pages\developers-guide\walkthrough-3.md', 'rb') as f:
    wt3 = f.read()

# shorthand
BS  = b'\x5c'   # backslash
GT  = b'\x3e'   # >
AST = b'\x2a'   # *
PIPE = b'\x7c'  # |

def esc_arrow(s): return s.replace(b'-' + BS + GT, b'->')
def esc_star(s):  return s.replace(BS + AST, b'*')
def esc_all(s):   return esc_arrow(esc_star(s))

# Fix 1a: Bare variable declarations -> wrap in code fence
old3_1a = (b'TSLMapDataLayer ' + BS + AST + b' m_mapDataLayer ;\r\n\r\n'
           b'TSLStandardDataLayer ' + BS + AST + b' m_stdDataLayer ; // This line added\r\n')
new3_1a = (b'```cpp\r\n'
           b'TSLMapDataLayer * m_mapDataLayer ;\r\n\r\n'
           b'TSLStandardDataLayer * m_stdDataLayer ; // This line added\r\n'
           b'```\r\n')

# Fix 1b: Constructor header + init-list merged with following { } fence
old3_1b = (b'CHelloGlobeDoc::CHelloGlobeDoc()\r\n\r\n'
           b': m_mapDataLayer( NULL ), m_stdDataLayer( NULL )\r\n\r\n'
           b'```cpp\r\n{\r\n\r\n}\r\n```')
new3_1b = (b'```cpp\r\nCHelloGlobeDoc::CHelloGlobeDoc()\r\n\r\n'
           b': m_mapDataLayer( NULL ), m_stdDataLayer( NULL )\r\n\r\n'
           b'{\r\n\r\n}\r\n```')

# Fix 2: Static variable declarations -> wrap in code fence
old3_2 = (b'// This line added in the Document class header, private section\r\n\r\n'
          b'static int m_overlayType ; // This line added in class header\r\n\r\n'
          b'// This line added in the Document .cpp file\r\n\r\n'
          b'int CHelloGlobeDoc::m_overlayType = ID_OVERLAYS_TEXT ;\r\n\r\n'
          b'Now we need')
new3_2 = (b'```cpp\r\n'
          b'// This line added in the Document class header, private section\r\n\r\n'
          b'static int m_overlayType ; // This line added in class header\r\n\r\n'
          b'// This line added in the Document .cpp file\r\n\r\n'
          b'int CHelloGlobeDoc::m_overlayType = ID_OVERLAYS_TEXT ;\r\n'
          b'```\r\n\r\nNow we need')

# Fix 3: Bare TSLTMC + DUToTMC lines split between two code fences
old3_3 = (b'{\r\n```\r\n'
          b'TSLTMC x, y ;\r\n\r\n'
          b'm_drawingSurface-' + BS + GT + b'DUToTMC( point.x, point.y, &x, &y ) ;\r\n\r\n'
          b'```cpp\r\nif ( GetDocument()')
new3_3 = (b'{\r\n\r\n'
          b'TSLTMC x, y ;\r\n\r\n'
          b'm_drawingSurface->DUToTMC( point.x, point.y, &x, &y ) ;\r\n\r\n'
          b'if ( GetDocument()')

# Fix 4: Bare EntitySet + createText lines before code fence
old3_4 = (b'TSLEntitySet ' + BS + AST + b' es = m_stdDataLayer-' + BS + GT + b'EntitySet() ;\r\n\r\n'
          b'TSLText ' + BS + AST + b' txt = es-' + BS + GT + b'createText( 0, x, y, "Hello World" ) ;\r\n\r\n'
          b'```cpp\r\n')
new3_4 = (b'```cpp\r\n'
          b'TSLEntitySet * es = m_stdDataLayer->EntitySet() ;\r\n\r\n'
          b'TSLText * txt = es->createText( 0, x, y, "Hello World" ) ;\r\n\r\n')

# Fix 5: Bare EntitySet + createSymbol(0) before code fence
old3_5 = (b'TSLEntitySet ' + BS + AST + b' es = m_stdDataLayer-' + BS + GT + b'EntitySet() ;\r\n\r\n'
          b'TSLSymbol ' + BS + AST + b' symbol = es-' + BS + GT + b'createSymbol( 0, x, y ) ;\r\n\r\n'
          b'```cpp\r\n')
new3_5 = (b'```cpp\r\n'
          b'TSLEntitySet * es = m_stdDataLayer->EntitySet() ;\r\n\r\n'
          b'TSLSymbol * symbol = es->createSymbol( 0, x, y ) ;\r\n\r\n')

# Fix 6: EntitySet + comments + TSLCoordSet (polygon section)
old3_6 = (b'TSLEntitySet ' + BS + AST + b' es = m_stdDataLayer-' + BS + GT + b'EntitySet() ;\r\n\r\n'
          b'// Create a coordinate list forming a triangle around the position\r\n\r\n'
          b'// Use the Drawing Surface to calculate the coordinates\r\n\r\n'
          b'// We will make our triangle 25 pixels either side of the position\r\n\r\n'
          b'// Note that the pixels are at the current zoom factor - the polygon\r\n\r\n'
          b'// is always completely scalable\r\n\r\n'
          b'TSLCoordSet ' + BS + AST + b' coords = new TSLCoordSet() ;\r\n\r\n'
          b'```cpp\r\n')
new3_6 = (b'```cpp\r\n'
          b'TSLEntitySet * es = m_stdDataLayer->EntitySet() ;\r\n\r\n'
          b'// Create a coordinate list forming a triangle around the position\r\n\r\n'
          b'// Use the Drawing Surface to calculate the coordinates\r\n\r\n'
          b'// We will make our triangle 25 pixels either side of the position\r\n\r\n'
          b'// Note that the pixels are at the current zoom factor - the polygon\r\n\r\n'
          b'// is always completely scalable\r\n\r\n'
          b'TSLCoordSet * coords = new TSLCoordSet() ;\r\n\r\n')

# Fix 7: EntitySet + comments + TSLCoordSet (polyline section)
old3_7 = (b'TSLEntitySet ' + BS + AST + b' es = m_stdDataLayer-' + BS + GT + b'EntitySet() ;\r\n\r\n'
          b'// Create a coordinate list forming a triangle around the position\r\n\r\n'
          b'// Use the Drawing Surface to calculate the coordinates\r\n\r\n'
          b'TSLCoordSet ' + BS + AST + b' coords = new TSLCoordSet() ;\r\n\r\n'
          b'```cpp\r\n')
new3_7 = (b'```cpp\r\n'
          b'TSLEntitySet * es = m_stdDataLayer->EntitySet() ;\r\n\r\n'
          b'// Create a coordinate list forming a triangle around the position\r\n\r\n'
          b'// Use the Drawing Surface to calculate the coordinates\r\n\r\n'
          b'TSLCoordSet * coords = new TSLCoordSet() ;\r\n\r\n')

# Fix 8: Long bare feature rendering code block
old3_8 = (b'TSLStyleID black = TSLDrawingSurface::getIDOfNearestColour( 0, 0, 0 ) ;\r\n\r\n'
          b'// Make up a feature name and numeric ID\r\n\r\n'
          b'm_stdDataLayer-' + BS + GT + b'addFeatureRendering( "Airport", 123 ) ;\r\n\r\n'
          b'// Associate some rendering with the new feature, use ID for\r\n\r\n'
          b'// efficiency\r\n\r\n'
          b'm_stdDataLayer-' + BS + GT + b'setFeatureRendering( 0, 123,\r\n\r\n'
          b'TSLRenderingAttributeSymbolStyle, 6003 ) ;\r\n\r\n'
          b'm_stdDataLayer-' + BS + GT + b'setFeatureRendering( 0, 123,\r\n\r\n'
          b'TSLRenderingAttributeSymbolColour, black ) ;\r\n\r\n'
          b'm_stdDataLayer-' + BS + GT + b'setFeatureRendering( 0, 123,\r\n\r\n'
          b'TSLRenderingAttributeSymbolSizeFactor, 40.0 ) ;\r\n\r\n'
          b'm_stdDataLayer-' + BS + GT + b'setFeatureRendering( 0, 123,\r\n\r\n'
          b'TSLRenderingAttributeSymbolSizeFactorUnits,\r\n\r\n'
          b'TSLDimensionUnitsPixels);\r\n')
new3_8 = (b'```cpp\r\n'
          b'TSLStyleID black = TSLDrawingSurface::getIDOfNearestColour( 0, 0, 0 ) ;\r\n\r\n'
          b'// Make up a feature name and numeric ID\r\n\r\n'
          b'm_stdDataLayer->addFeatureRendering( "Airport", 123 ) ;\r\n\r\n'
          b'// Associate some rendering with the new feature, use ID for\r\n\r\n'
          b'// efficiency\r\n\r\n'
          b'm_stdDataLayer->setFeatureRendering( 0, 123,\r\n\r\n'
          b'TSLRenderingAttributeSymbolStyle, 6003 ) ;\r\n\r\n'
          b'm_stdDataLayer->setFeatureRendering( 0, 123,\r\n\r\n'
          b'TSLRenderingAttributeSymbolColour, black ) ;\r\n\r\n'
          b'm_stdDataLayer->setFeatureRendering( 0, 123,\r\n\r\n'
          b'TSLRenderingAttributeSymbolSizeFactor, 40.0 ) ;\r\n\r\n'
          b'm_stdDataLayer->setFeatureRendering( 0, 123,\r\n\r\n'
          b'TSLRenderingAttributeSymbolSizeFactorUnits,\r\n\r\n'
          b'TSLDimensionUnitsPixels);\r\n'
          b'```\r\n')

# Fix 9: Bare EntitySet + createSymbol(123) before code fence (feature section)
old3_9 = (b'TSLEntitySet ' + BS + AST + b' es = m_stdDataLayer-' + BS + GT + b'EntitySet() ;\r\n\r\n'
          b'// 123 is the numeric feature code we assigned on the Data Layer\r\n\r\n'
          b'TSLSymbol ' + BS + AST + b' symbol = es-' + BS + GT + b'createSymbol( 123, x, y ) ;\r\n\r\n'
          b'```cpp\r\n')
new3_9 = (b'```cpp\r\n'
          b'TSLEntitySet * es = m_stdDataLayer->EntitySet() ;\r\n\r\n'
          b'// 123 is the numeric feature code we assigned on the Data Layer\r\n\r\n'
          b'TSLSymbol * symbol = es->createSymbol( 123, x, y ) ;\r\n\r\n')

fixes = [
    ('fix1a', old3_1a, new3_1a),
    ('fix1b', old3_1b, new3_1b),
    ('fix2',  old3_2,  new3_2),
    ('fix3',  old3_3,  new3_3),
    ('fix4',  old3_4,  new3_4),
    ('fix5',  old3_5,  new3_5),
    ('fix6',  old3_6,  new3_6),
    ('fix7',  old3_7,  new3_7),
    ('fix8',  old3_8,  new3_8),
    ('fix9',  old3_9,  new3_9),
]

for name, old, new in fixes:
    found = old in wt3
    print(f'wt3 {name} found: {found}')
    if found:
        wt3 = wt3.replace(old, new, 1)

with open(r'c:\maplink\maplink-docs\pages\developers-guide\walkthrough-3.md', 'wb') as f:
    f.write(wt3)
print('walkthrough-3.md written')
