"""Fix bare code blocks in ddo-sdk.md"""

with open(r'c:\maplink\maplink-docs\pages\developers-guide\ddo-sdk.md', 'rb') as f:
    content = f.read()

fixes = []

# Fix DDO1: Bare class member variable declarations
fixes.append(('DDO1 member variable declarations',
    b'In the Document class definition, add a declaration of the Object Data Layer just after the Standard Data Layer:\r\n\r\n'
    b'TSLMapDataLayer \\* m_mapDataLayer ;\r\n\r\n'
    b'TSLStandardDataLayer \\* m_stdDataLayer ;\r\n\r\n'
    b'TSLObjectDataLayer \\* m_objDataLayer ; // This line added\r\n\r\n'
    b'The new class variable should be initialised to 0 in the Document constructor.',
    b'In the Document class definition, add a declaration of the Object Data Layer just after the Standard Data Layer:\r\n\r\n'
    b'```cpp\r\n'
    b'TSLMapDataLayer * m_mapDataLayer ;\r\n\r\n'
    b'TSLStandardDataLayer * m_stdDataLayer ;\r\n\r\n'
    b'TSLObjectDataLayer * m_objDataLayer ; // This line added\r\n'
    b'```\r\n\r\n'
    b'The new class variable should be initialised to 0 in the Document constructor.'
))

# Fix DDO2: Bare constructor
fixes.append(('DDO2 constructor',
    b'The new class variable should be initialised to 0 in the Document constructor.\r\n\r\n'
    b'CHelloGlobeDoc::CHelloGlobeDoc()\r\n\r\n'
    b': m_mapDataLayer( NULL ),\r\n\r\n'
    b'm_stdDataLayer( NULL ),\r\n\r\n'
    b'm_objDataLayer( NULL )\r\n\r\n'
    b'{\r\n\r\n'
    b'}\r\n\r\n'
    b'The layer should only be created',
    b'The new class variable should be initialised to 0 in the Document constructor.\r\n\r\n'
    b'```cpp\r\n'
    b'CHelloGlobeDoc::CHelloGlobeDoc()\r\n\r\n'
    b': m_mapDataLayer( NULL ),\r\n\r\n'
    b'm_stdDataLayer( NULL ),\r\n\r\n'
    b'm_objDataLayer( NULL )\r\n\r\n'
    b'{\r\n\r\n'
    b'}\r\n'
    b'```\r\n\r\n'
    b'The layer should only be created'
))

# Fix DDO3: Bare OnOpenDocument, DeleteContents, addToSurface code blocks
fixes.append(('DDO3 OnOpenDocument/DeleteContents/addToSurface',
    b'> In the Document OnOpenDocument method, instantiate a TSLObjectDataLayer if the map is successful:\r\n\r\n'
    b'if ( !m_mapDataLayer-\\>loadData( lpszPathName ) )\r\n\r\n'
    b'{\r\n\r\n'
    b'// Error handling as before\r\n\r\n'
    b'return FALSE ;\r\n\r\n'
    b'}\r\n\r\n'
    b'm_stdDataLayer = new TSLStandardDataLayer() ;\r\n\r\n'
    b'm_objDataLayer = new TSLObjectDataLayer() ;\r\n\r\n'
    b'> In the Document DeleteContents method, add the following code to delete the overlay layer:\r\n\r\n'
    b'if ( m_objDataLayer )\r\n\r\n'
    b'{\r\n\r\n'
    b'm_objDataLayer-\\>destroy() ;\r\n\r\n'
    b'm_objDataLayer = NULL ;\r\n\r\n'
    b'}\r\n\r\n'
    b'> Modify the Document addToSurface method as below to add the extra layer and to make the map layer buffered:\r\n\r\n'
    b'if ( !m_mapDataLayer \\|\\| !m_stdDataLayer\r\n\r\n'
    b'\\|\\| !m_objDatalayer \\|\\| !drawingSurface )\r\n\r\n'
    b'{\r\n\r\n'
    b'return false ;\r\n\r\n'
    b'}\r\n\r\n'
    b'bool sts = drawingSurface-\\>addDataLayer( m_mapDataLayer, "map" ) ;\r\n\r\n'
    b'if ( sts )\r\n\r\n'
    b'{\r\n\r\n'
    b'drawingSurface-\\>setDataLayerProps("map",TSLPropertyBuffered,true);\r\n\r\n'
    b'sts = drawingSurface-\\>addDataLayer( m_stdDataLayer, "overlay" ) ;\r\n\r\n'
    b'}\r\n\r\n'
    b'if ( sts )\r\n\r\n'
    b'sts = drawingSurface-\\>addDataLayer( m_objDataLayer, "dynamic" ) ;\r\n\r\n'
    b'return sts ;\r\n\r\n'
    b'### Creating a Custom Dynamic Data Object',
    b'> In the Document OnOpenDocument method, instantiate a TSLObjectDataLayer if the map is successful:\r\n\r\n'
    b'```cpp\r\n'
    b'if ( !m_mapDataLayer->loadData( lpszPathName ) )\r\n\r\n'
    b'{\r\n\r\n'
    b'// Error handling as before\r\n\r\n'
    b'return FALSE ;\r\n\r\n'
    b'}\r\n\r\n'
    b'm_stdDataLayer = new TSLStandardDataLayer() ;\r\n\r\n'
    b'm_objDataLayer = new TSLObjectDataLayer() ;\r\n'
    b'```\r\n\r\n'
    b'> In the Document DeleteContents method, add the following code to delete the overlay layer:\r\n\r\n'
    b'```cpp\r\n'
    b'if ( m_objDataLayer )\r\n\r\n'
    b'{\r\n\r\n'
    b'm_objDataLayer->destroy() ;\r\n\r\n'
    b'm_objDataLayer = NULL ;\r\n\r\n'
    b'}\r\n'
    b'```\r\n\r\n'
    b'> Modify the Document addToSurface method as below to add the extra layer and to make the map layer buffered:\r\n\r\n'
    b'```cpp\r\n'
    b'if ( !m_mapDataLayer || !m_stdDataLayer\r\n\r\n'
    b'|| !m_objDatalayer || !drawingSurface )\r\n\r\n'
    b'{\r\n\r\n'
    b'return false ;\r\n\r\n'
    b'}\r\n\r\n'
    b'bool sts = drawingSurface->addDataLayer( m_mapDataLayer, "map" ) ;\r\n\r\n'
    b'if ( sts )\r\n\r\n'
    b'{\r\n\r\n'
    b'drawingSurface->setDataLayerProps("map",TSLPropertyBuffered,true);\r\n\r\n'
    b'sts = drawingSurface->addDataLayer( m_stdDataLayer, "overlay" ) ;\r\n\r\n'
    b'}\r\n\r\n'
    b'if ( sts )\r\n\r\n'
    b'sts = drawingSurface->addDataLayer( m_objDataLayer, "dynamic" ) ;\r\n\r\n'
    b'return sts ;\r\n'
    b'```\r\n\r\n'
    b'### Creating a Custom Dynamic Data Object'
))

# Fix DDO4: MyDDO class fence missing closing };
fixes.append(('DDO4 MyDDO class closing brace outside fence',
    b'virtual TSLDisplayObject * instantiateDO(TSLDisplayType key, int dsID=0) const ;\r\n'
    b'```\r\n\r\n'
    b'};\r\n',
    b'virtual TSLDisplayObject * instantiateDO(TSLDisplayType key, int dsID=0) const ;\r\n\r\n'
    b'};\r\n'
    b'```\r\n\r\n'
))

# Fix DDO5: Mixed fence - MyDDO implementations + prose + MyDO implementations
fixes.append(('DDO5 mixed MyDDO/MyDO fence',
    b'```cpp\r\n'
    b'MyDDO::MyDDO(void) { }\r\n\r\n'
    b'MyDDO::~MyDDO(void) { }\r\n\r\n'
    b'TSLDisplayObject * MyDDO::instantiateDO(TSLDisplayType key,int dsID) const\r\n\r\n'
    b'{\r\n\r\n'
    b'return new MyDO() ;\r\n\r\n'
    b'}\r\n\r\n'
    b'In the source file for MyDO, provide initial definitions for the constructor, and destructor and a simple implementation for the draw method - draw a red circle 50 pixels high.\r\n\r\n'
    b'MyDO::MyDO(void)\r\n\r\n'
    b'{ // Without this, the symbol disappears when the centre goes off screen\r\n\r\n'
    b'setPixSize( -25, -25, 25, 25 ) ;\r\n\r\n'
    b'}\r\n\r\n'
    b'MyDO::~MyDO(void) { }\r\n\r\n'
    b'bool MyDO::draw( TSLRenderingInterface *ri, TSLEnvelope *extent )\r\n\r\n'
    b'{ // 1023 = filled circle with cross, 181=red in standard config files\r\n\r\n'
    b'ri->setupSymbolAttributes( 1023, 181, 50, TSLDimensionUnitsPixels );\r\n\r\n'
    b'ri->drawSymbol( position() ) ;\r\n\r\n'
    b'return true ;\r\n\r\n'
    b'}\r\n'
    b'```',
    b'```cpp\r\n'
    b'MyDDO::MyDDO(void) { }\r\n\r\n'
    b'MyDDO::~MyDDO(void) { }\r\n\r\n'
    b'TSLDisplayObject * MyDDO::instantiateDO(TSLDisplayType key,int dsID) const\r\n\r\n'
    b'{\r\n\r\n'
    b'return new MyDO() ;\r\n\r\n'
    b'}\r\n'
    b'```\r\n\r\n'
    b'In the source file for MyDO, provide initial definitions for the constructor, and destructor and a simple implementation for the draw method - draw a red circle 50 pixels high.\r\n\r\n'
    b'```cpp\r\n'
    b'MyDO::MyDO(void)\r\n\r\n'
    b'{ // Without this, the symbol disappears when the centre goes off screen\r\n\r\n'
    b'setPixSize( -25, -25, 25, 25 ) ;\r\n\r\n'
    b'}\r\n\r\n'
    b'MyDO::~MyDO(void) { }\r\n\r\n'
    b'bool MyDO::draw( TSLRenderingInterface *ri, TSLEnvelope *extent )\r\n\r\n'
    b'{ // 1023 = filled circle with cross, 181=red in standard config files\r\n\r\n'
    b'ri->setupSymbolAttributes( 1023, 181, 50, TSLDimensionUnitsPixels );\r\n\r\n'
    b'ri->drawSymbol( position() ) ;\r\n\r\n'
    b'return true ;\r\n\r\n'
    b'}\r\n'
    b'```'
))

# Fix DDO6: Bare updateDDOPosition method
fixes.append(('DDO6 updateDDOPosition method',
    b'In the Document class definition, add a new public method updateDDOPosition, with the following definition:\r\n\r\n'
    b'bool CHelloGlobeDoc::updateDDOPosition( long x, long y )\r\n\r\n'
    b'{\r\n\r\n'
    b'if ( m_objDataLayer )\r\n\r\n'
    b'{\r\n\r\n'
    b'// Get the solitary DDO - could iterate over DDO list\r\n\r\n'
    b'TSLDynamicDataObject \\* ddo = m_objDataLayer-\\>getDDO( 0 ) ;\r\n\r\n'
    b'if ( ddo )\r\n\r\n'
    b'{\r\n\r\n'
    b'ddo-\\>move( x, y, true ) ; // true means also updates DO\r\n\r\n'
    b'm_objDataLayer-\\>notifyChanged() ; // Invalidates buffer\r\n\r\n'
    b'UpdateAllViews( 0 ) ; // Update views displaying doc\r\n\r\n'
    b'return true ;\r\n\r\n'
    b'}\r\n\r\n'
    b'}\r\n\r\n'
    b'return false ;\r\n\r\n'
    b'}\r\n\r\n'
    b'In the View class, modify the OnMouseMove handler',
    b'In the Document class definition, add a new public method updateDDOPosition, with the following definition:\r\n\r\n'
    b'```cpp\r\n'
    b'bool CHelloGlobeDoc::updateDDOPosition( long x, long y )\r\n\r\n'
    b'{\r\n\r\n'
    b'if ( m_objDataLayer )\r\n\r\n'
    b'{\r\n\r\n'
    b'// Get the solitary DDO - could iterate over DDO list\r\n\r\n'
    b'TSLDynamicDataObject * ddo = m_objDataLayer->getDDO( 0 ) ;\r\n\r\n'
    b'if ( ddo )\r\n\r\n'
    b'{\r\n\r\n'
    b'ddo->move( x, y, true ) ; // true means also updates DO\r\n\r\n'
    b'm_objDataLayer->notifyChanged() ; // Invalidates buffer\r\n\r\n'
    b'UpdateAllViews( 0 ) ; // Update views displaying doc\r\n\r\n'
    b'return true ;\r\n\r\n'
    b'}\r\n\r\n'
    b'}\r\n\r\n'
    b'return false ;\r\n\r\n'
    b'}\r\n'
    b'```\r\n\r\n'
    b'In the View class, modify the OnMouseMove handler'
))

# Fix DDO7: Bare mouse move handler code
fixes.append(('DDO7 mouse move handler code',
    b'Add the following code before the call to CView::OnMouseMove\r\n\r\n'
    b'if ( m_drawingSurface && !moved )\r\n\r\n'
    b'{\r\n\r\n'
    b'CHelloGlobeDoc \\* doc = GetDocument() ;\r\n\r\n'
    b'TSLTMC x, y ;\r\n\r\n'
    b'if ( m_drawingSurface-\\>DUToTMC( point.x, point.y, &x, &y ) )\r\n\r\n'
    b'doc-\\>updateDDOPosition( x, y ) ;\r\n\r\n'
    b'}\r\n\r\n'
    b'Now compile and run your application.',
    b'Add the following code before the call to CView::OnMouseMove\r\n\r\n'
    b'```cpp\r\n'
    b'if ( m_drawingSurface && !moved )\r\n\r\n'
    b'{\r\n\r\n'
    b'CHelloGlobeDoc * doc = GetDocument() ;\r\n\r\n'
    b'TSLTMC x, y ;\r\n\r\n'
    b'if ( m_drawingSurface->DUToTMC( point.x, point.y, &x, &y ) )\r\n\r\n'
    b'doc->updateDDOPosition( x, y ) ;\r\n\r\n'
    b'}\r\n'
    b'```\r\n\r\n'
    b'Now compile and run your application.'
))

for name, old, new in fixes:
    found = old in content
    print(f'{name}: found={found}')
    if found:
        content = content.replace(old, new, 1)
    else:
        print(f'  first 60: {old[:60]}')
        print(f'  first 60 found: {old[:60] in content}')

with open(r'c:\maplink\maplink-docs\pages\developers-guide\ddo-sdk.md', 'wb') as f:
    f.write(content)
print('ddo-sdk.md written')
