"""Fix bare code blocks in threading.md (3D walkthrough section)"""

with open(r'c:\maplink\maplink-docs\pages\developers-guide\threading.md', 'rb') as f:
    content = f.read()

fixes = []

# T4: Init code - bare const char* declarations before ```cpp fence
fixes.append(('T4 init configDirPath/transformsFile',
    b'const char \\* configDirPath = NULL ; // Replace if deployed\r\n\r\n'
    b'// Full path and filename to the file tsltransforms.dat\r\n\r\n'
    b'const char \\* transformsFile = NULL; // Replace if deployed\r\n\r\n'
    b'TSLThreadedErrorStack::clear() ;\r\n\r\n'
    b'TSLDrawingSurface::loadStandardConfig( configDirPath ) ;\r\n\r\n'
    b'// Required for draped polygons.\r\n\r\n'
    b'TSLCoordinateSystem::loadCoordinateSystems( transformsFile );\r\n\r\n'
    b'```cpp\r\n'
    b'TSLSimpleString msg( "" );',
    b'```cpp\r\n'
    b'const char * configDirPath = NULL ; // Replace if deployed\r\n\r\n'
    b'// Full path and filename to the file tsltransforms.dat\r\n\r\n'
    b'const char * transformsFile = NULL; // Replace if deployed\r\n\r\n'
    b'TSLThreadedErrorStack::clear() ;\r\n\r\n'
    b'TSLDrawingSurface::loadStandardConfig( configDirPath ) ;\r\n\r\n'
    b'// Required for draped polygons.\r\n\r\n'
    b'TSLCoordinateSystem::loadCoordinateSystems( transformsFile );\r\n\r\n'
    b'TSLSimpleString msg( "" );'
))

# T5: ExitInstance split - cleanup() is bare between two fences
fixes.append(('T5 ExitInstance split',
    b'```cpp\r\nint CHelloGlobe::ExitInstance()\r\n\r\n{\r\n'
    b'```\r\n\r\n'
    b'TSLDrawingSurface::cleanup( ) ;\r\n\r\n'
    b'```cpp\r\nreturn CWinApp::ExitInstance();\r\n'
    b'```\r\n\r\n'
    b'}',
    b'```cpp\r\nint CHelloGlobe::ExitInstance()\r\n\r\n'
    b'{\r\n\r\n'
    b'TSLDrawingSurface::cleanup( ) ;\r\n\r\n'
    b'return CWinApp::ExitInstance();\r\n\r\n'
    b'}\r\n'
    b'```'
))

# T6a: Constructor signature bare before ```cpp
fixes.append(('T6a CHelloGlobeDoc constructor signature',
    b'CHelloGlobeDoc::CHelloGlobeDoc () : m_newMap( false )\r\n\r\n'
    b'```cpp\r\n'
    b'{',
    b'```cpp\r\nCHelloGlobeDoc::CHelloGlobeDoc () : m_newMap( false )\r\n\r\n'
    b'{'
))

# T6b: Destructor body split (second fence for }/} is separate)
fixes.append(('T6b CHelloGlobeDoc destructor split',
    b'm_mapDataLayer = NULL ;\r\n'
    b'```\r\n\r\n'
    b'```cpp\r\n'
    b'}\r\n\r\n'
    b'}\r\n'
    b'```',
    b'm_mapDataLayer = NULL ;\r\n\r\n'
    b'}\r\n\r\n'
    b'}\r\n'
    b'```'
))

# T7: OnOpenDocument - closing } bare after fence
fixes.append(('T7 OnOpenDocument closing brace',
    b'return TRUE;\r\n'
    b'```\r\n\r\n'
    b'}',
    b'return TRUE;\r\n\r\n'
    b'}\r\n'
    b'```'
))

# T8: View destructor - signature bare before ```cpp
fixes.append(('T8 CHelloGlobeView destructor signature',
    b'CHelloGlobeView::\\~CHelloGlobeView()\r\n\r\n'
    b'```cpp\r\n'
    b'{',
    b'```cpp\r\nCHelloGlobeView::~CHelloGlobeView()\r\n\r\n'
    b'{'
))

# T9: Camera calls split across two fences + bare lookAt + bare }
fixes.append(('T9 camera calls split',
    b'm_drawingSurface->camera()->reset();\r\n'
    b'```\r\n'
    b'```cpp\r\n'
    b'm_drawingSurface->camera()->moveTo( 50.0, 0.0, 10000000.0,\r\n\r\n'
    b'TSL3DCameraMoveActionNone ) ;\r\n'
    b'```\r\n\r\n'
    b'm_drawingSurface-\\>camera()-\\>lookAt( 50.0, -5.0, 0.0, false ) ;\r\n\r\n'
    b'}',
    b'm_drawingSurface->camera()->reset();\r\n\r\n'
    b'm_drawingSurface->camera()->moveTo( 50.0, 0.0, 10000000.0,\r\n\r\n'
    b'TSL3DCameraMoveActionNone ) ;\r\n\r\n'
    b'm_drawingSurface->camera()->lookAt( 50.0, -5.0, 0.0, false ) ;\r\n\r\n'
    b'}\r\n'
    b'```'
))

# T10: renderingCallback signature bare before ```cpp
fixes.append(('T10 renderingCallback signature',
    b'void Simple3DInteractionView::renderingCallback(void \\* arg,\r\n\r\n'
    b'int pendingTextures )\r\n\r\n'
    b'```cpp\r\n'
    b'{',
    b'```cpp\r\nvoid Simple3DInteractionView::renderingCallback(void * arg,\r\n\r\n'
    b'int pendingTextures )\r\n\r\n'
    b'{'
))

# T11: user geometry creation - signature bare before fence, destroy() bare after fence
fixes.append(('T11 user geometry create/destroy',
    b'TSL3DStandardDataLayer\\* stdLayer = \\...;\r\n\r\n'
    b'TSL3DClientUserGeometryEntity\\* client = new \\...;\r\n\r\n'
    b'TSL3DUserGeometryEntity\\* entity = stdLayer-\\>entitySet()-\\>\r\n\r\n'
    b'```cpp\r\n'
    b'create3DUserGeometry(client, false);\r\n\r\n'
    b'if (!entity)\r\n\r\n'
    b'... // handle error\r\n'
    b'```\r\n'
    b'\\...\r\n\r\n'
    b'entity-\\>destroy();\r\n\r\n'
    b'delete client; // don\'t need this if takesOwnership is true',
    b'```cpp\r\n'
    b'TSL3DStandardDataLayer* stdLayer = ...;\r\n\r\n'
    b'TSL3DClientUserGeometryEntity* client = new ...;\r\n\r\n'
    b'TSL3DUserGeometryEntity* entity = stdLayer->entitySet()->\r\n\r\n'
    b'create3DUserGeometry(client, false);\r\n\r\n'
    b'if (!entity)\r\n\r\n'
    b'... // handle error\r\n\r\n'
    b'...\r\n\r\n'
    b'entity->destroy();\r\n\r\n'
    b'delete client; // don\'t need this if takesOwnership is true\r\n'
    b'```'
))

# T12: SquareClient class - massive split into one fence
fixes.append(('T12 SquareClient class',
    b'class SquareClient : public TSL3DClientUserGeometryEntity\r\n\r\n'
    b'{\r\n\r\n'
    b'private:\r\n\r\n'
    b'TSL3DCoord m_centre;\r\n\r\n'
    b'double m_radius;\r\n\r\n'
    b'public:\r\n\r\n'
    b'// Constructor\r\n\r\n'
    b'SquareClient(TSL3DCoord centre)\r\n\r\n'
    b': m_centre(centre)\r\n\r\n'
    b', m_radius(sqrt(2000000.0\\*2000000.0 + 2000000.0\\*2000000.0))\r\n\r\n'
    b'```cpp\r\n'
    b'{\r\n\r\n'
    b'}\r\n\r\n'
    b'// Destructor\r\n'
    b'```\r\n'
    b'virtual \\~SquareClient()\r\n\r\n'
    b'```cpp\r\n'
    b'{\r\n\r\n'
    b'}\r\n\r\n'
    b'virtual double boundingSphereRadius () const\r\n\r\n'
    b'{\r\n\r\n'
    b'return m_radius;\r\n\r\n'
    b'}\r\n'
    b'```\r\n'
    b'virtual const TSL3DCoord& centre () const\r\n\r\n'
    b'```cpp\r\n'
    b'{\r\n\r\n'
    b'return m_centre;\r\n\r\n'
    b'}\r\n\r\n'
    b'// render an orange square\r\n\r\n'
    b'virtual bool draw (int uniqueSurfaceID,\r\n'
    b'```\r\n'
    b'TSL3DRenderingInterface\\* renderingInterface)\r\n\r\n'
    b'```cpp\r\n'
    b'{\r\n\r\n'
    b'glPushAttrib( GL_ALL_ATTRIB_BITS );\r\n\r\n'
    b'glPushClientAttrib( GL_CLIENT_ALL_ATTRIB_BITS );\r\n'
    b'```\r\n'
    b'GLfloat coords\\[\\] = { -100000.0f, -100000.0f, 0.0f,\r\n\r\n'
    b'100000.0f, -100000.0f, 0.0f,\r\n\r\n'
    b'-100000.0f, 100000.0f, 0.0f,\r\n\r\n'
    b'100000.0f, 100000.0f, 0.0f };\r\n\r\n'
    b'```cpp\r\n'
    b'glColor4f( 1.0f, 0.5f, 0.0f, 1.0f );\r\n\r\n'
    b'glDisable( GL_TEXTURE_2D );\r\n\r\n'
    b'glDisable( GL_CULL_FACE );\r\n\r\n'
    b'glEnableClientState( GL_VERTEX_ARRAY );\r\n\r\n'
    b'glDisableClientState( GL_TEXTURE_COORD_ARRAY );\r\n\r\n'
    b'glDisableClientState( GL_INDEX_ARRAY );\r\n\r\n'
    b'glVertexPointer( 3, GL_FLOAT, 3 * sizeof( GLfloat ), coords );\r\n\r\n'
    b'glDrawArrays( GL_TRIANGLE_STRIP, 0, 4 );\r\n\r\n'
    b'glPopAttrib();\r\n\r\n'
    b'glPopClientAttrib();\r\n\r\n'
    b'return true;\r\n\r\n'
    b'}\r\n\r\n'
    b'// stream out the polygon\r\n\r\n'
    b'virtual int save (TSLofstream& stream)\r\n\r\n'
    b'{\r\n'
    b'```\r\n'
    b'\\...\r\n\r\n'
    b'```cpp\r\n'
    b'return SQUARE_USER_GEOMETRY_ID;\r\n\r\n'
    b'}\r\n\r\n'
    b'};\r\n'
    b'```',
    b'```cpp\r\n'
    b'class SquareClient : public TSL3DClientUserGeometryEntity\r\n\r\n'
    b'{\r\n\r\n'
    b'private:\r\n\r\n'
    b'TSL3DCoord m_centre;\r\n\r\n'
    b'double m_radius;\r\n\r\n'
    b'public:\r\n\r\n'
    b'// Constructor\r\n\r\n'
    b'SquareClient(TSL3DCoord centre)\r\n\r\n'
    b': m_centre(centre)\r\n\r\n'
    b', m_radius(sqrt(2000000.0*2000000.0 + 2000000.0*2000000.0))\r\n\r\n'
    b'{\r\n\r\n'
    b'}\r\n\r\n'
    b'// Destructor\r\n\r\n'
    b'virtual ~SquareClient()\r\n\r\n'
    b'{\r\n\r\n'
    b'}\r\n\r\n'
    b'virtual double boundingSphereRadius () const\r\n\r\n'
    b'{\r\n\r\n'
    b'return m_radius;\r\n\r\n'
    b'}\r\n\r\n'
    b'virtual const TSL3DCoord& centre () const\r\n\r\n'
    b'{\r\n\r\n'
    b'return m_centre;\r\n\r\n'
    b'}\r\n\r\n'
    b'// render an orange square\r\n\r\n'
    b'virtual bool draw (int uniqueSurfaceID,\r\n\r\n'
    b'TSL3DRenderingInterface* renderingInterface)\r\n\r\n'
    b'{\r\n\r\n'
    b'glPushAttrib( GL_ALL_ATTRIB_BITS );\r\n\r\n'
    b'glPushClientAttrib( GL_CLIENT_ALL_ATTRIB_BITS );\r\n\r\n'
    b'GLfloat coords[] = { -100000.0f, -100000.0f, 0.0f,\r\n\r\n'
    b'100000.0f, -100000.0f, 0.0f,\r\n\r\n'
    b'-100000.0f, 100000.0f, 0.0f,\r\n\r\n'
    b'100000.0f, 100000.0f, 0.0f };\r\n\r\n'
    b'glColor4f( 1.0f, 0.5f, 0.0f, 1.0f );\r\n\r\n'
    b'glDisable( GL_TEXTURE_2D );\r\n\r\n'
    b'glDisable( GL_CULL_FACE );\r\n\r\n'
    b'glEnableClientState( GL_VERTEX_ARRAY );\r\n\r\n'
    b'glDisableClientState( GL_TEXTURE_COORD_ARRAY );\r\n\r\n'
    b'glDisableClientState( GL_INDEX_ARRAY );\r\n\r\n'
    b'glVertexPointer( 3, GL_FLOAT, 3 * sizeof( GLfloat ), coords );\r\n\r\n'
    b'glDrawArrays( GL_TRIANGLE_STRIP, 0, 4 );\r\n\r\n'
    b'glPopAttrib();\r\n\r\n'
    b'glPopClientAttrib();\r\n\r\n'
    b'return true;\r\n\r\n'
    b'}\r\n\r\n'
    b'// stream out the polygon\r\n\r\n'
    b'virtual int save (TSLofstream& stream)\r\n\r\n'
    b'{\r\n\r\n'
    b'...\r\n\r\n'
    b'return SQUARE_USER_GEOMETRY_ID;\r\n\r\n'
    b'}\r\n\r\n'
    b'};\r\n'
    b'```'
))

# T13a: register load callback call - bare two-liner
fixes.append(('T13a register load callback',
    b'Setting a load callback function:\r\n\r\n'
    b'TSL3DUserGeometryEntity::\r\n\r\n'
    b'registerUserGeometryClientLoadCallback(loadUserGeometryCallback);\r\n\r\n'
    b'Here is a skeleton load callback function:',
    b'Setting a load callback function:\r\n\r\n'
    b'```cpp\r\n'
    b'TSL3DUserGeometryEntity::\r\n\r\n'
    b'registerUserGeometryClientLoadCallback(loadUserGeometryCallback);\r\n'
    b'```\r\n\r\n'
    b'Here is a skeleton load callback function:'
))

# T13b: loadUserGeometryCallback - signature bare before fence, default: bare between fences
fixes.append(('T13b loadUserGeometryCallback split',
    b'static TSL3DClientUserGeometryEntity\\* loadUserGeometryCallback(\r\n\r\n'
    b'TSLifstream& stream,\r\n\r\n'
    b'int userGeometryID,\r\n\r\n'
    b'bool& assumeOwnership)\r\n\r\n'
    b'```cpp\r\n'
    b'{\r\n\r\n'
    b'// whether returned entities will be freed by MapLink:\r\n\r\n'
    b'assumeOwnership = ...;\r\n\r\n'
    b'switch (userGeometryID)\r\n\r\n'
    b'{\r\n\r\n'
    b'case SQUARE_USER_GEOMETRY_ID:\r\n\r\n'
    b'... // stream in client and return it\r\n\r\n'
    b'... // etc\r\n'
    b'```\r\n'
    b'default:\r\n\r\n'
    b'```cpp\r\n'
    b'return NULL;\r\n\r\n'
    b'}\r\n\r\n'
    b'}\r\n'
    b'```',
    b'```cpp\r\n'
    b'static TSL3DClientUserGeometryEntity* loadUserGeometryCallback(\r\n\r\n'
    b'TSLifstream& stream,\r\n\r\n'
    b'int userGeometryID,\r\n\r\n'
    b'bool& assumeOwnership)\r\n\r\n'
    b'{\r\n\r\n'
    b'// whether returned entities will be freed by MapLink:\r\n\r\n'
    b'assumeOwnership = ...;\r\n\r\n'
    b'switch (userGeometryID)\r\n\r\n'
    b'{\r\n\r\n'
    b'case SQUARE_USER_GEOMETRY_ID:\r\n\r\n'
    b'... // stream in client and return it\r\n\r\n'
    b'... // etc\r\n\r\n'
    b'default:\r\n\r\n'
    b'return NULL;\r\n\r\n'
    b'}\r\n\r\n'
    b'}\r\n'
    b'```'
))

# T14: getModel DLL export - signature bare before fence
fixes.append(('T14 getModel DLL export',
    b'extern "C" \\_\\_declspec(dllexport)\r\n\r\n'
    b'void\\* getModel( int index,\r\n\r\n'
    b'```cpp\r\n'
    b'const char* filename,',
    b'```cpp\r\n'
    b'extern "C" __declspec(dllexport)\r\n\r\n'
    b'void* getModel( int index,\r\n\r\n'
    b'const char* filename,'
))

for name, old, new in fixes:
    found = old in content
    print(f'{name}: found={found}')
    if found:
        content = content.replace(old, new, 1)
    else:
        print(f'  first 80: {old[:80]}')
        print(f'  first 80 found: {old[:80] in content}')

with open(r'c:\maplink\maplink-docs\pages\developers-guide\threading.md', 'wb') as f:
    f.write(content)
print('threading.md written')
