---
title: MapLink Pro Developer's Guide
---

# MapLink Pro Developer's Guide

> This guide covers MapLink Pro API concepts, SDK components, and the steps required to build a MapLink application. It applies to all supported platforms unless otherwise noted.

---

## SDK Components

MapLink Pro is composed of a Core SDK and a collection of optional add-on SDKs. The Core SDK provides fundamental map display and interaction. Additional SDKs extend this with specialised capabilities.

### Core SDK

The Core SDK is the foundation of all MapLink applications. It provides:

- High-performance 2D map display
- A drawing surface abstraction (`TSLNTSurface` on Windows, `TSLMotifSurface` on X11)
- Data layer management (`TSLMapDataLayer`, `TSLStandardDataLayer`)
- Coordinate system handling and projection support
- Feature rendering and styling
- Geometry entities (symbols, polylines, polygons)
- Interaction mode framework
- Error stack and diagnostic utilities

### Optional SDKs

| SDK | Description |
|---|---|
| OpenGL Drawing Surface SDK | Hardware-accelerated 2D rendering via OpenGL |
| Direct Import SDK | Runtime ingestion of geospatial formats without pre-processing |
| Tracks SDK | Real-time display of moving objects |
| Dynamic Data Object (DDO) SDK | Fully programmatic animated overlays |
| Terrain SDK | 3D terrain elevation data, viewshed analysis and contouring |
| MapLink 3D Earth SDK | Globe-based 3D rendering using osgEarth integration |
| Editor SDK | Interactive vector overlay creation and editing |
| Spatial SDK | Advanced spatial operations: arcs, parallels, island merging |
| GeoPackage SDK | Read and display OGC GeoPackage data |
| OWSContext SDK | Read and display OWSContext documents |
| OGC Services SDK | WMS and WPS server plug-in development |
| GML SDK | Read and write GML application schemas and instance data |
| .NET SDKs | C# and VB.NET wrappers for most SDKs |
| S52/S63 SDK | Marine electronic navigational charts |

---

## Development Environment Setup

### Library Naming Convention

As of MapLink 11.1, only 64-bit Release mode libraries are supplied. Link against Release mode libraries in all build configurations.

For the Core SDK:

| Library | Description |
|---|---|
| `MapLink64.lib` | Release mode, DLL version (requires `TTLDLL` preprocessor directive) |

Each optional SDK has its own `.lib` file (e.g. `MapLinkTerrain64.lib`, `MapLinkEDT64.lib`). All require the `TTLDLL` preprocessor directive.

### Visual Studio Project Configuration

In your Visual Studio project properties:

1. Under **C/C++ → General**, add the MapLink include path:
   ```
   C:\Program Files\Envitia\MapLink Pro\X.Y\include
   ```
2. Under **Linker → General**, add the MapLink library path:
   ```
   C:\Program Files\Envitia\MapLink Pro\X.Y\lib64
   ```
3. Under **Linker → Input**, add the required `.lib` files.
4. Add `TTLDLL` to your preprocessor definitions.

### MapLink Headers

Add `#include "MapLink.h"` to any file that uses MapLink classes. For optional SDKs, include their own header (e.g. `#include "MapLinkTerrain.h"`). The simplest approach is to add these includes to `stdafx.h`.

---

## Unicode Support

MapLink Pro supports Unicode on both Windows and Linux. The library is compiled as Unicode-enabled on Windows, allowing full Unicode character handling in text drawing, feature names, and file paths.

---

## Deployment

When deploying a MapLink application, the MapLink runtime DLLs must be present on the target machine. Refer to the separate document **"MapLink Pro Deployment of End User Applications"** for a full list of redistributable dependencies.

Key points:
- On Windows, copy the required DLLs from `<INSTALL_DIR>\bin64\` to your application directory or a location on the system `PATH`.
- On Linux, the shared libraries (`.so` files) from the installation must be accessible.
- The MapLink `config` directory must be accessible at runtime. Set the config path when calling `TSLDrawingSurface::loadStandardConfig()`.

---

## Samples

MapLink Pro ships with a range of sample applications. These are found in `<INSTALL_DIR>\samples\` and are organised as follows:

| Folder | Description |
|---|---|
| `NT` | Windows MFC samples |
| `QT` | Windows and X11 Qt samples |
| `X11` | X11-only samples |
| `Wizards` | Visual Studio project wizards |

Each sample entry in the **MapLink Pro Samples** launcher shows a description, a **Launch** button, and a **Code** button to open the source directory. The same samples are available on [GitHub](https://github.com/envitia).

---

## Walkthrough 1 — Your First MapLink Application

This walkthrough produces an MFC SDI application that loads and displays a MapLink map.

### Skeleton Application

Start from an MFC Application Wizard–generated SDI executable. Build it first to confirm the baseline compiles.

### Configure Project Properties

Set up include paths, library paths, and preprocessor directives as described in the [Development Environment Setup](#development-environment-setup) section above, linking `MapLink64.lib`.

### Initialisation and Clean Up

MapLink configuration files are loaded once per run. Do this in the `InitInstance` method of your App object, before the Document Template is created:

```cpp
const char* configDirPath = NULL; // replace with your config path when deployed
TSLThreadedErrorStack::clear();
TSLDrawingSurface::loadStandardConfig(configDirPath);

TSLSimpleString msg("");
bool anyErrors = TSLThreadedErrorStack::errorString(msg, "Initialisation Errors:\n");
if (anyErrors)
{
    AfxMessageBox(msg, MB_OK);
    exit(0);
}
```

Clean up in `ExitInstance`:

```cpp
int CMyApp::ExitInstance()
{
    TSLDrawingSurface::cleanup();
    return CWinApp::ExitInstance();
}
```

### Managing the Document

Declare a `TSLMapDataLayer*` in the Document. Construct it in the constructor and destroy it in the destructor:

```cpp
CMyDoc::CMyDoc() { m_mapDataLayer = new TSLMapDataLayer(); }
CMyDoc::~CMyDoc()
{
    if (m_mapDataLayer) { m_mapDataLayer->destroy(); m_mapDataLayer = NULL; }
}
```

In the `OnOpenDocument` override, load the map file:

```cpp
BOOL CMyDoc::OnOpenDocument(LPCTSTR lpszPathName)
{
    if (!CDocument::OnOpenDocument(lpszPathName)) return FALSE;
    m_mapDataLayer->loadData(lpszPathName);
    return TRUE;
}
```

### Managing the View

The View holds a `TSLNTSurface*`. Create it in `OnInitialUpdate` when the window handle is available:

```cpp
void CMyView::OnInitialUpdate()
{
    if (!m_drawingSurface)
    {
        CRect rect;
        GetClientRect(&rect);
        m_drawingSurface = new TSLNTSurface(m_hWnd, false);
        GetDocument()->addToSurface(m_drawingSurface);
        m_drawingSurface->reset(false);
        m_drawingSurface->wndResize(0, 0, rect.Width(), rect.Height(), false,
            TSLResizeActionMaintainTopLeft);
    }
}
```

Destroy it in the View destructor:

```cpp
if (m_drawingSurface) { m_drawingSurface->destroy(); m_drawingSurface = NULL; }
```

### Handling Resize Events

```cpp
void CMyView::OnSize(UINT nType, int cx, int cy)
{
    if (m_drawingSurface)
        m_drawingSurface->wndResize(0, 0, cx, cy, true, TSLResizeActionMaintainTopLeft);
}
```

### Handling Paint Events

```cpp
void CMyView::OnDraw(CDC* pDC)
{
    if (m_drawingSurface)
    {
        RECT rect;
        if (pDC->GetClipBox(&rect) == NULLREGION)
            GetClientRect(&rect);
        m_drawingSurface->drawDU(rect.left, rect.bottom, rect.right, rect.top, true);
    }
}
```

Suppress the background erase to avoid flicker:

```cpp
BOOL CMyView::OnEraseBkgnd(CDC*) { return TRUE; }
```

---

## Walkthrough 2 — Interaction Modes

MapLink Pro provides a standard set of interaction modes that allow users to pan, zoom, and grab the map. These are managed by a `TSLInteractionModeManagerNT` (Windows) or `TSLInteractionModeManagerX11` (X11).

### Setting Up Interaction Modes

In the View's `OnInitialUpdate`, create the mode manager and register standard modes:

```cpp
m_modeManager = new TSLInteractionModeManagerNT(this, m_hWnd);
m_modeManager->addMode(new TSLInteractionModeZoom(1), true);
m_modeManager->addMode(new TSLInteractionModePan(2), false);
m_modeManager->addMode(new TSLInteractionModeGrab(3), false);
m_modeManager->setCurrentMode(1);
m_modeManager->attachToSurface(m_drawingSurface, 0, 0, rect.Width(), rect.Height());
```

Pass mouse and keyboard events to the mode manager from your message handlers.

---

## Walkthrough 3 — Drawing and Editing Overlays

MapLink Pro allows you to add geometric overlays to a map using a `TSLStandardDataLayer`. This layer holds `TSLEntity`-derived objects: symbols, polylines, and polygons.

### Creating a Standard Data Layer

```cpp
TSLStandardDataLayer* overlayLayer = new TSLStandardDataLayer();
m_drawingSurface->addDataLayer(overlayLayer, "overlay");
```

### Adding Geometry

To add a polyline:

```cpp
TSLPolyline* polyline = new TSLPolyline(featureCode);
polyline->append(TMCx1, TMCy1);
polyline->append(TMCx2, TMCy2);
overlayLayer->entitySet()->insert(polyline);
```

To commit changes:

```cpp
overlayLayer->notifyChanged();
m_drawingSurface->redraw();
```

Coordinates are in Transformed Map Coordinates (TMC). Use `TSLDrawingSurface::DUToTMC()` to convert from device (screen) units.

---

## Coordinate Systems

MapLink uses three coordinate types:

| Type | Description |
|---|---|
| **Map Units (MU)** | The coordinate space of the source data |
| **Transformed Map Coordinates (TMC)** | Internal representation, derived from MU via a transformation |
| **Device Units (DU)** | Screen pixels |

Conversion methods on `TSLDrawingSurface`:
- `DUToTMC(duX, duY, &tmcX, &tmcY)` — screen to internal
- `TMCToDU(tmcX, tmcY, &duX, &duY)` — internal to screen

---

## Feature Rendering

MapLink controls the visual appearance of vector data through a feature rendering system. Each feature in a data layer is associated with a **feature code** that maps to a rendering style.

Rendering attributes include:
- Colour (using a colour table index or RGB)
- Line style, width, and thickness
- Fill pattern
- Symbol style
- Text font, size, and alignment
- Transparency

Use `TSLRenderingAttributes` to configure attributes programmatically. Feature rendering files (`.ftr` or `.dat`) define the default mapping.

---

## Core SDK — Key Concepts

### Drawing Surfaces

The drawing surface (`TSLNTSurface` on Windows, `TSLMotifSurface` on X11, `TSLOpenGLSurface` for OpenGL) manages the visual display. Multiple data layers can be stacked on a single drawing surface.

Key methods:
- `loadStandardConfig()` — load MapLink configuration files
- `addDataLayer()` — attach a data layer
- `removeDataLayer()` — detach a data layer
- `drawDU()` — render to the window
- `wndResize()` — notify of window resize
- `reset()` — fit the view to the loaded data
- `setOption()` — configure surface behaviour (e.g. double buffering)

### Data Layers

| Layer Type | Description |
|---|---|
| `TSLMapDataLayer` | Pre-processed MapLink map files (`.map`, `.mpc`) |
| `TSLStandardDataLayer` | Programmatic 2D vector geometry |
| `TSLObjectDataLayer` | Dynamic Data Object (DDO) display objects |
| `TSLCADRGDataLayer` | CADRG/CIB raster data |
| `TSLRasterDataLayer` | General raster imagery |
| `TSLWMSDataLayer` | OGC WMS tile data |
| `TSLFilterDataLayer` | GeoTIFF, NITF, and raster filter data |
| `TSLKMLDataLayer` | KML/KMZ overlay data |
| `TSLS63DataLayer` | S-63 / S-57 encrypted ENC data |
| `TSLDatabaseLayer` | Vector data from Oracle |
| `TSLCustomDataLayer` | Application-defined custom data |

### Error Handling

MapLink uses a thread-aware error stack:

```cpp
TSLThreadedErrorStack::clear();
// ... perform MapLink operation ...
TSLSimpleString msg("");
TSLThreadedErrorStack::errorString(msg, "Errors:");
if (msg) AfxMessageBox(msg);
```

---

## OpenGL Drawing Surface

The `TSLOpenGLSurface` SDK provides hardware-accelerated rendering. It is a drop-in replacement for `TSLNTSurface` and supports the same data layers and interaction modes.

### Library

```
MapLinkOpenGLSurface64.lib
```

Requires `TTLDLL` preprocessor directive. Must also link `opengl32.lib`.

### Usage

Replace `TSLNTSurface` with `TSLOpenGLSurface` in your View initialisation. All other API calls remain the same.

---

## Direct Import SDK

The Direct Import SDK allows MapLink to load many geospatial data formats at runtime without pre-processing through MapLink Studio.

### Library

```
MapLinkDirectImport64.lib  (also: ttldirectimport64.dll at runtime)
```

### Supported Import Mechanisms

| Class | Data |
|---|---|
| `TSLKMLDataLayer` | KML/KMZ (2D drawing surfaces) |
| `TSLS63DataLayer` | S-63 / S-57 data including updates |
| `TSLCADRGDataLayer` | CADRG/CIB raster data |
| `TSLFilterDataLayer` | GeoTIFF, NITF/NSIF, raster data |
| `TSLUtilityFunctions::importData` | S-57, Shapefile, MIF/MID, KML, OS MasterMap, OS VectorMap Local |
| `TSLRasterDataLayer` / `TSLRasterFilterDataLayer` | General raster |
| `TSLDatabaseLayer` | Oracle vector data |
| `TSLCustomDataLayer` | Custom application data |
| `TSLWMSDataLayer` | OGC WMS server data |
| `TSLWMTSDataLayer` | OGC WMTS server data |

> Some Direct Import mechanisms require runtime licence keys. Contact your Envitia sales representative for details.

---

## Tracks SDK

The Tracks SDK provides real-time display of moving objects such as aircraft, ships, or vehicles. It supports thousands of simultaneous tracks with history trails.

### Library

```
MapLinkTrack64.lib
```

### Key Classes

- `TSLTrackDisplayLayer` — manages track display
- `TSLTrack` — represents a single moving entity
- `TSLTrackHistory` — records position history for trail display

Tracks are updated by calling `TSLTrack::update()` with the new position, and the drawing surface will reflect changes on the next redraw.

---

## Dynamic Data Object SDK

The DDO SDK allows you to create fully custom, animated map overlays by deriving from `TSLDisplayObject`. Your `draw()` method is called each frame.

### Library

```
MapLinkDDO64.lib
```

### Usage

Derive from `TSLDisplayObject` and implement the `draw` method:

```cpp
class MyOverlay : public TSLDisplayObject
{
    virtual bool draw(TSLRenderingInterface* surface, TSLEnvelope* extent)
    {
        // Draw using surface->drawSymbol(), drawPolyline(), etc.
        return true;
    }
};
```

Add the object to a `TSLObjectDataLayer`, then add the layer to the drawing surface. Objects are invalidated by calling `notifyChanged()`.

---

## Terrain SDK

The Terrain SDK extends MapLink with support for elevation data, terrain following, viewshed analysis, and contour generation.

### Library

```
MapLinkTerrain64.lib
```

Requires: `TTLDLL`, link `MapLink64.lib` first.

### Terrain Databases

Load a terrain database using `TSLTerrainDatabase`:

```cpp
TSLTerrainDatabase* terrain = new TSLTerrainDatabase();
terrain->loadData("path/to/terrain.dmed");
```

Attach it to the drawing surface:

```cpp
m_drawingSurface->addTerrainDatabase(terrain);
```

### Elevation Queries

```cpp
double elevation;
terrain->elevation(latRadians, lonRadians, &elevation);
```

### Viewshed Analysis

`TSLViewshedCalculator` computes line-of-sight areas from an observer point. Configure observer position, altitude, range, and bearing sector, then call `calculate()`. The result is a raster mask that can be displayed as a `TSLRasterDataLayer`.

### Contouring

`TSLContourGenerator` produces vector contour lines from elevation data. Specify the interval and style, then add the result to a `TSLStandardDataLayer`.

### Profile / Cross-Section

`TSLProfileHelper` generates elevation profiles along a polyline path, returning a set of sample points suitable for plotting as a graph.

---

## MapLink 3D Earth SDK

The 3D Earth SDK provides a globe-based 3D display using an osgEarth integration. It extends MapLink's data model to a 3D coordinate space.

### Library

```
MapLinkEarth64.lib
```

Requires: `TTLDLL`, link `MapLink64.lib` and OpenGL libraries.

### Key Classes

| Class | Description |
|---|---|
| `earth::Surface3D` | The 3D globe drawing surface |
| `earth::Camera` | Controls viewpoint position and orientation |
| `earth::Track` / `earth::TrackSymbol` | 3D track objects |
| `earth::Geometry` | 3D geometric primitives (polygons, polylines) |
| `earth::geometry::Style` | Rendering configuration for 3D geometry |

### Sample Application Interactions

The EarthSample project demonstrates:

- Loading terrain databases via `CEarthSampleDoc::loadTerrainDatabase`
- Camera control via `CCameraControlFormView::updateCamera`
- Track management via `CEarthSampleDoc::initialiseTracks` and `CEarthSampleDoc::updateTracks`
- Geometry creation via `CreatePolygonInteraction` and `CreatePolylineInteraction`

### Camera Movement

```cpp
earth::Camera* camera = surface3D->camera();
camera->lookAt(latitude, longitude, altitude, rollAngle);
```

### Track Management

```cpp
earth::TrackSymbol* symbol = new earth::TrackSymbol(symbolConfig);
earth::Track* track = new earth::Track(symbol);
surface3D->addTrack(track);
// Update at runtime:
track->setPosition(lat, lon, alt);
```

### Managing Geometry

```cpp
earth::geometry::Style style;
surface3D->setStyle(style);

earth::Polygon* polygon = new earth::Polygon();
polygon->addCoord(lat1, lon1);
polygon->addCoord(lat2, lon2);
polygon->setStyleName("myStyle");
surface3D->addGeometry(polygon);
```

---

## Editor SDK

The Editor SDK provides a framework for creating, selecting, and modifying vector overlays. It handles user interaction through a mode-based architecture with built-in operations for drawing, selection, and manipulation.

### Library

```
MapLinkEDT64.lib
```

### Key Concepts

**Operations** encapsulate user interactions. There are four styles:
1. **One-shot** — e.g. "Delete all selected entities"
2. **Creation** — e.g. drawing a polygon
3. **Manipulation** — e.g. moving vertices of selected entities
4. **Attribute** — e.g. setting fill colour of selected polygons

**Select List** — an ordered list of entities the user has interacted with.

### Main Classes

| Class | Role |
|---|---|
| `TSLEditor` | Main application interface to the Editor |
| `TSLEditorRequest` | Callback interface for application-side prompts and events |
| `TSLUserOperation` | Base class for custom operations |
| `TSLUserOperationRequest` | Interface for custom operations to interact with the Editor |

### Initialising the Editor

```cpp
// Derive from TSLEditorRequest and provide your UI callbacks
class MyEditorRequest : public TSLEditorRequest { ... };

TSLEditor* editor = new TSLEditor(new MyEditorRequest());
editor->initialise("path/to/editor.ini");
editor->attach(m_drawingSurface);
editor->dataChanged();
TSLAllOperations::add(editor);
editor->reset();
```

### Activating Operations

```cpp
editor->activate("polygon");
editor->activate("delete");
// Pass user data where required:
TSLRenderingAttributes ra;
editor->activate("renderingattributes", &ra);
```

### Limitations

- Only one `TSLEditor` instance per application.
- Only edits vector TMF geometry in a `TSLStandardDataLayer` (the topmost detectable, selectable layer).
- Call `reset()` before changing layer contents externally; call `dataChanged()` after.

### Using Standard Interaction Modes

The `TSLInteractionModeEdit` class integrates Editor operations into the standard interaction mode manager. Derive from both `TSLInteractionModeRequest` and `TSLInteractionModeEditorRequest` in your View class:

```cpp
m_editMode = new TSLInteractionModeEdit("editor.ini", editorRequestHandler);
m_modeManager->addMode(m_editMode, false);
// Activate an operation:
m_editMode->editor()->activate("polygon", 0);
```

### Custom User Operations

Derive from `TSLUserOperation` to create new operations:

```cpp
class MyOperation : public TSLUserOperation
{
    virtual int activate(void* userData) { ... return promptId; }
    virtual int locator(int eventType, double x, double y, ...) { ... return promptId; }
    virtual int done() { ... return promptId; }
};
```

Key overridable methods: `activate`, `deactivate`, `locator`, `done`, `backup`, `undo`, `activatePossible`, `undoPossible`.

---

## GeoPackage SDK

The GeoPackage SDK allows reading, analysis, and display of OGC GeoPackage files.

### Library

```
MapLinkGeoPackage64.lib
```

Contact `support@envitia.com` for implementation details.

---

## OWSContext SDK

The OWSContext SDK allows reading and display of OWSContext documents.

Contact `support@envitia.com` for implementation details.

---

## OGC Services SDK

The OGC Services SDK provides interfaces for building MapLink WMS and WPS server plug-ins.

### Library

```
MapLinkOGCServices64.lib    (for client use)
MapLinkWMS64.lib            (for WMS plug-in development)
MapLinkWPS64.lib            (for WPS plug-in development)
```

### The MapLink WMS

The MapLink Web Map Service conforms to OGC WMS 1.3.0. It is deployed in IIS or Apache Tomcat and serves map data to OGC-compliant clients.

**Plug-in development** requires implementing and exporting the `createDataSource` function:

```cpp
extern "C"
{
    TSLWMSPluginDataSource* createDataSource(const char* spatialData,
                                              const char* dataSourceConfig)
    {
        return new MyDataSource(spatialData, dataSourceConfig);
    }
}
```

Your `MyDataSource` class derives from `TSLWMSPluginDataSource` and implements:
- `getLayers()` — builds the layer capability tree
- `getMap()` — responds to WMS GetMap requests
- `getFeatureInfo()` (optional) — responds to GetFeatureInfo requests

### The MapLink WPS

The MapLink Web Processing Service allows plug-ins to expose geospatial algorithms as OGC processes.

Export either `createDataSource` (single process) or `createAllDataSources` (multiple processes):

```cpp
extern "C"
{
    TSLWPSPluginDataSource* createDataSource(const char* dataLocation,
                                              const char* configLocation)
    {
        return new MyWPSDataSource(dataLocation, configLocation);
    }
}
```

Your `MyWPSDataSource` derives from `TSLWPSPluginDataSource` and implements:
- `describeProcess()` — returns process metadata and I/O descriptions
- `executeProcess()` — performs the computation and returns results

---

## Spatial SDK

The Spatial SDK extends the Editor SDK with additional spatial operations and the ability to manage map update islands.

### Library

```
LandLink64.lib
```

Also requires `MapLink64.lib`.

### Islands

Islands represent contiguous groups of entities that form independent areas of change to a vector map. They are used to manage and apply incremental updates.

**Creating islands:**

```cpp
TSLIslandSet* islandSet = new TSLIslandSet();
TSLIsland::createIslands(sourceLayer, *islandSet);
```

**Merging islands** (processing multiple updates in order):

```cpp
// For each update:
TSLIslandMergeSet* merged = new TSLIslandMergeSet();
TSLIsland::mergeIslands(*islandSet, updateLayer, pathToMap, *refHandler, *merged);
```

Always apply updates in chronological order to ensure the correct version of each entity survives the merge.

---

## GML SDK

The GML SDK provides reading and writing of GML Application Schemas and GML instance data (GML SF-0 compliant or equivalent).

### Library

```
MapLinkGML64.lib
```

Also requires `MapLink64.lib`. Runtime-locked: call `TSLUtilityFunctions::unlockSupport(TSLKeyedGML, code)` before use.

### GML Application Schemas

Load a schema:

```cpp
TSLGMLApplicationSchemaLoader loader;
TSLGMLApplicationSchema* schema = loader.loadSchema("path/to/schema.xsd");
```

Save feature definitions to a data layer:

```cpp
schema->applyToLayer(standardDataLayer);
```

Create a schema from a data layer:

```cpp
TSLGMLApplicationSchemaFactory factory;
TSLGMLApplicationSchema* schema = factory.createSchema(dataLayer, parameters);
TSLGMLApplicationSchemaWriter writer;
writer.write(schema, "output.xsd");
```

### GML Instance Data

Load instance data:

```cpp
TSLGMLInstanceDataLoader loader;
TSLCoordinateSystem* crs = NULL;
loader.loadInstanceData("data.gml", standardDataLayer, &crs, schema);
```

Export instance data:

```cpp
TSLGMLInstanceDataWriter writer;
writer.write(standardDataLayer, coordinateSystem, schema, "output.gml");
```

### Geometry Type Mapping

| GML Type | MapLink Type |
|---|---|
| Point | `TSLGeometryTypeSymbol` |
| Curve | `TSLGeometryTypePolyline` |
| Surface | `TSLGeometryTypePolygon` |
| MultiPoint | `TSLGeometryTypeMultiPoint` |
| MultiCurve | `TSLGeometryTypeMultiPolyline` |
| MultiSurface | `TSLGeometryTypeMultiPolygon` |

---

## .NET SDKs

The .NET SDKs are C# and VB.NET wrappers around the C++ libraries. Class names use the `TSLN` prefix instead of `TSL`. Properties replace many get/set methods, and colours use `System.Drawing.Color` rather than colour table indices.

### Available .NET Libraries

| SDK | Assembly |
|---|---|
| Core SDK | `Envitia.MapLink64.dll` |
| OpenGL Surface | `Envitia.MapLink.OpenGLSurface64.dll` |
| Direct Import | `Envitia.MapLink.DirectImport64.dll` |
| Interaction Modes | `Envitia.MapLink.InteractionModes64.dll` |
| DDO SDK | `Envitia.MapLink.DDO64.dll` |
| Editor SDK | `Envitia.MapLink.Editor64.dll` |
| Spatial Editor SDK | `Envitia.MapLink.Spatial64.dll` |
| Terrain SDK | `Envitia.MapLink.Terrain64.dll` |
| GeoPackage SDK | `Envitia.MapLink.GeoPackage64.dll` |
| 3D SDK | `Envitia.MapLink.ML3D64.dll` |
| OGC Services SDK | `Envitia.MapLink.OGCServices64.dll` |
| S52/S63 SDKs | `Envitia.MapLink.S5264.dll` / `Envitia.MapLink.S6364.dll` |

Add the assemblies as references by browsing to `<INSTALL_DIR>\bin64\`. They are not registered in the standard GAC list.

### C# Walkthrough 1 — Your First C# MapLink Application

#### Initialisation

```csharp
public Form1()
{
    TSLNErrorStack.clear();
    string configDirPath = null; // replace when deployed
    TSLNDrawingSurface.loadStandardConfig(configDirPath);
    string msg = TSLNErrorStack.errorString("Initialisation errors:\n",
        TSLNErrorCategory.TSLNErrorCategoryError |
        TSLNErrorCategory.TSLNErrorCategoryFatal);
    if (msg != null) { MessageBox.Show(this, msg); Environment.Exit(-1); }
    InitializeComponent();
}
```

#### Clean Up

```csharp
protected override void Dispose(bool disposing)
{
    if (disposing && (components != null)) components.Dispose();
    TSLNDrawingSurface.cleanup();
    base.Dispose(disposing);
}
```

#### Drawing Surface and Map Loading

```csharp
// In Load event:
m_drawingSurface = new TSLNDrawingSurface(this.Handle, false);

// In File Open handler:
m_mapDataLayer = new TSLNMapDataLayer();
if (!m_mapDataLayer.loadData(openFileDialog1.FileName))
{
    string error = TSLNErrorStack.errorString("Errors:", TSLNErrorCategory.TSLNErrorCategoryAll);
    if (error != null) MessageBox.Show(this, "Error", error, MessageBoxButtons.OK);
    return;
}
m_drawingSurface.addDataLayer(m_mapDataLayer, "map");
m_drawingSurface.reset(true);
```

#### Paint and Resize Events

```csharp
private void OnPaint(object sender, PaintEventArgs e)
{
    if (m_drawingSurface == null) return;
    m_drawingSurface.drawDU(e.ClipRectangle.Left, e.ClipRectangle.Top,
        e.ClipRectangle.Right, e.ClipRectangle.Bottom, true);
}

private void OnResize(object sender, EventArgs e)
{
    if (m_drawingSurface == null) return;
    m_drawingSurface.wndResize(ClientRectangle.Left, ClientRectangle.Top,
        ClientRectangle.Right, ClientRectangle.Bottom, true,
        TSLNResizeActionEnum.TSLNResizeActionMaintainCentre);
}
```

### VB.NET Walkthrough 1 — Your First VB MapLink Application

The VB walkthrough follows the same structure as the C# walkthrough. The namespace is imported via **Project Properties → References → Imported Namespaces** rather than `using` statements.

```vb
Public Sub New()
    TSLNErrorStack.clear()
    Dim configDirPath As String = Nothing
    TSLNDrawingSurface.loadStandardConfig(configDirPath)
    Dim msg As String = TSLNErrorStack.errorString("Initialisation Errors:\n",
        TSLNErrorCategory.TSLNErrorCategoryError Or
        TSLNErrorCategory.TSLNErrorCategoryFatal)
    If Not msg Is Nothing Then
        MessageBox.Show(Me, msg)
        Environment.Exit(-1)
    End If
    InitializeComponent()
End Sub
```

Resize and paint handlers are identical in structure to the C# versions with VB syntax.

---

## Floating Point

MapLink assumes the floating-point unit is configured to the standard C/C++ runtime settings. When using MapLink via .NET or similar technologies, verify that the floating-point setup matches. The DirectX Accelerator SDK requires specific floating-point configuration as per DirectX requirements.

---

## Other SDKs

Future versions of this guide will cover in greater detail:

**Interactive Editing with the Editor SDK:**
- Editing Architecture
- Interactive Operations
- Entity Creation and Manipulation

**Network Analysis and Routing:**
- Network Construction and Traversal
- Routing and Complex Cost Objects

Contact [Envitia support](mailto:support@envitia.com) for the latest available documentation.

---

## Threading

This section applies to the Core SDK, Terrain SDK, 3D SDK, Accelerator SDK, and DDO SDK. For all other SDKs, do not share objects across threads.

MapLink is not fully thread-safe. This is by design to maximise performance.

### Known Threading Issues

Stop all threads before performing any of the following:

- Loading and adding coordinate systems or coordinate system registries
- Setting static Drawing Surface properties (loaders, path lists) — do this before starting threads
- Using the Seamless Layer Manager, Flashback, History, DBIF, Entity Store SDK, or S63 SDK
- Adding or removing data layers from drawing surfaces
- Using the TSLErrorStack interface (use `TSLThreadedErrorStack` instead)

The following data layer types **must not** be shared between threads:
- Map Data Layers
- CADRG Data Layers
- Raster Data Layers
- WMS Data Layers
- Filter Data Layers
- Grid Data Layers
- ECW Layers
- Dynamic Object Data Layers

### Threading Options

```cpp
TSLUtilityFunctions::setThreadedOptions(TSLThreadedOptionsRenderingSupport);
```

Set this before drawing if you intend to share a `TSLStandardDataLayer` across Drawing Surfaces in different threads.

### Standard Data Layer

Sharing a `TSLStandardDataLayer` is safe as long as each thread's drawing surface has a different ID and `TSLThreadedOptionsRenderingSupport` is set. Do not add or remove entities while drawing is active in another thread.

### Custom Data Layer / Dynamic Renderer

Thread safety is the developer's responsibility. Note that both are called from background threads when used with the Accelerator or 3D Drawing Surface.

### 3D and Accelerator SDKs

Both use a background thread for 2D layer rendering. Always draw from the thread that created the surface. Picking, entity removal, and layer deletion must all occur in the main drawing thread.

### Path Lists

`TSLPathList` is not thread-safe. Set up path lists for drawing surfaces before starting threads. If modifications are needed after threads start, stop all MapLink threads first.

### X11 Threading

Use a separate `Display` connection per thread. Resources are keyed on the Display pointer and sharing between threads may appear to work on single-core systems but will fail on multi-core hardware. Call `XInitThreads()` before any other Xlib calls.

---

## Appendix A — UNIX/Linux/VxWorks (X11)

### TSLMotifSurface

The X11 drawing surface is `TSLMotifSurface`. Its constructor accepts the Display, Screen, Colormap, and Drawable (window handle):

```cpp
TSLMotifSurface* surface = new TSLMotifSurface(display, screen, colormap, drawable, 0, visual);
```

Call `TSLDrawingSurface::cleanup()` before closing the Display.

### Using Qt 5.1 or Later

Add to the custom widget constructor:

```cpp
setAttribute(Qt::WA_OpaquePaintEvent);
setAttribute(Qt::WA_PaintOnScreen);
setAttribute(Qt::WA_NativeWindow);
setAutoFillBackground(false);
```

Override `paintEngine` to return `NULL`. Construct the surface:

```cpp
Display* display = QX11Info::display();
WId wid = winId();
XWindowAttributes attribs;
XGetWindowAttributes(display, wid, &attribs);
m_surface = new TSLMotifSurface(display, attribs.screen, attribs.colormap, wid, 0, attribs.visual);
```

### Text Drawing

X11 rendering uses Pango (via Xft/XRender) to draw text, which provides full Unicode support.

### Raster Support

X11 MapLink supports TIFF, PNG, and JPEG raster formats from MapLink Studio. Alpha channel support requires XRender 0.6 or later.

### Holed Polygons

On X11, key-holing is the recommended approach for holed polygons (configured in MapLink Studio). This is more efficient than true holed polygon rendering and avoids performance issues on VxWorks targets.

### APP-6A and 2525B Symbology

Two configuration files are provided: `app6aConfig.csv` and `2525bConfig.csv`. Load the appropriate one and the alternate symbol file `tslsymbolsAPP6A.dat`:

```cpp
TSLDrawingSurface::loadStandardConfig(configDir);
TSLDrawingSurface::setupSymbols("tslsymbolsAPP6A.dat");
```

### Stroked Line Styles

Custom stroked line styles are defined in `tsllinestyle.dat` using a command string syntax:

```
StyleID;ttlclsstrk;Comment;Tag;CommandString
```

Command strings use `D[x,y]` (pen down), `U[x,y]` (pen up), `C[(R,G,B),W]` (colour and width), and `B` (bend point). Progress must be made in the x-axis. Test new line styles with complex maps to verify performance.

### X11 Error Handlers

If you define custom X error handlers via `XSetErrorHandler`, chain to the previous handler. MapLink uses error handlers for XShm shared memory detection. Set up handlers before initialising MapLink.

---

## Appendix B — Vector and Raster Data Format Support

### Vector Datasets

| Format | Studio Import | Direct Import SDK | Runtime Export | Other Runtime |
|---|---|---|---|---|
| DXF | Yes | Yes | | |
| File Geodatabase (FileGDB) | Yes | Yes | | |
| GeoPackage | Yes | Yes | | |
| GML 2/3 | Yes | Yes | Yes | Yes |
| KML Simple Features 2D | Yes | Yes | Yes | |
| MIF/MID | Yes | Yes | Yes | Yes |
| NITF/NSIF | Yes | Yes | Yes | |
| OpenStreetMap | Yes | Yes | | |
| OS MasterMap | Yes | Yes | Yes | Yes |
| OS NTF | Yes | Yes | Yes | Yes |
| OS VectorMap Local | Yes | Yes | Yes | |
| OS VectorMap District | Yes | Yes | Yes | |
| S-57 (Unencrypted ENC & AML) | Yes | Yes | Yes | Yes |
| S-57 Encrypted (S-63) | Yes | | | |
| Shapefiles | Yes | Yes | Yes | Yes |
| US Census TIGER/Line | Yes | Yes | | |
| VPF (DNC, VMAP, WVS etc.) | Yes | | | |
| DAFIF | | | | Yes |
| DFAD | | | | Yes |

### Raster Datasets

| Format | Studio Import | Direct Import SDK | Runtime Export | Other Runtime |
|---|---|---|---|---|
| ADRG | Yes | Yes | | |
| ASRP | Yes | Yes | Yes | |
| BSB Nautical Chart Format | Yes | Yes | | |
| CADRG/CIB | Yes | Yes | Yes | Yes |
| ECRG | Yes | Yes | | |
| ECW | | | | Yes |
| GeoPackage | Yes | Yes | | |
| Geospatial PDF | Yes | Yes | | |
| GeoTIFF | Yes | Yes | Yes | |
| JPEG | Yes | Yes | | |
| JPEG2000 | Yes | Yes | | |
| MrSID | Yes | Yes | | |
| NITF/NSIF | Yes | Yes | Yes | |
| USRP | Yes | Yes | | |

---

## Appendix C — Deprecated SDKs

### Legacy 3D SDK (MapLink3D)

> This SDK is deprecated. The current 3D solution is the [MapLink 3D Earth SDK](#maplink-3d-earth-sdk), which provides an osgEarth-based globe. Contact `support@envitia.com` for migration guidance.

The legacy 3D SDK used `TSL3DWinGLSurface` (Windows) or `TSL3DX11GLSurface` (X11) as its drawing surface. It introduced the `TSL3DDataLayer` hierarchy:

- `TSL3DStandardDataLayer` — 3D vector geometry
- `TSL3DModel` — 3D model rendering with LOD support
- `TSL3DTriangle`, `TSL3DQuad` — basic polygonal geometry
- `TSL3DTriangleFan`, `TSL3DTriangleStrip` — efficient multi-triangle geometry

**Library:**

```
MapLink3D64.lib
```

Requires `MapLink64.lib` and `opengl32.lib`.

**3D Coordinate Space:** Positions are specified as geodetic coordinates (latitude, longitude, altitude). Use `TSL3DDrawingSurface` for geodetic/geocentric conversion. Altitude can be expressed relative to mean sea level or height above ground.

**Walkthrough 5 (legacy):** Set up a 3D application using MFC. Create a `TSL3DWinGLSurface` in `OnInitialUpdate`. Attach data layers using `addDataLayer`. Set up the `TSL3DCamera` using `moveTo()` and `lookAt()`. Provide a `TSL3DRenderingCallback` that calls `Invalidate()` to trigger redraws when draped data is ready.

---

## Further Information

- **API Reference** — Windows CHM documents for C++ and .NET, accessible from the MapLink Pro Documentation Launcher in the Start Menu
- **Release Notes** — See the [Releases page](/pages/releases/) for the latest platform information and known issues
- **OGC Services Deployment** — See the [MapLink OGC Services Deployment User Guide](/pages/MapLink%20OGC%20Services%20Deployment%20User%20Guide) for WMS/WPS deployment instructions
- **Deployment Guide** — See the [Deployment Guide](/pages/support/deployment-guide) for runtime distribution requirements
- **Training and Consultancy** — Contact [sales@envitia.com](mailto:sales@envitia.com) or call +44 1403 273173
