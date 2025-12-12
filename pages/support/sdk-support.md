# MapLink Pro SDK & Component Support

* toc
{:toc}

MapLink Pro includes many individual SDKs and supporting components. These are listed below.

A deprecated SDK or feature will continue to be available in the product until the next major version. Where possible, a deprecation will be accompanied with a recommendation for an alternative solution.


# Column Descriptions
- **Status**: whether the component is supported, deprecated or archived.
- **Windows**: the latest MapLink Pro version that provides support for the component on Windows.
- **Linux**: the latest MapLink Pro version that provides support for the component on Linux.
- **Android**: the latest MapLink Pro version that provides support for the component on Android.
- **C++ API**: whether the SDK has a C++ API.
- **.NET API**: whether the SDK has a .NET API.
- **Java API**: whether the SDK has a Java API for Android solutions.

# SDKs
All supported MapLink Pro runtime SDKs are listed.

| SDK | Status | Windows | Linux | Android | C++ API | .NET API | Java API |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **MapLink Pro Core** | **Supported** | **11.2.4** | **11.2.4** | **10.2** | **Yes** | **Yes** | **Yes** |
| 3D | **Deprecated** Superseded by Earth | 11.2.4 | 11.2.4 | | Yes | Yes | |
| Accelerator | **Deprecated** Superseded by OpenGLDrawingSurface | 11.2.4 | | | Yes | | |
| Android Native Surface | Supported | | | 10.2 | Yes | | |
| App11 | Supported | 11.2.4 | | | Yes | | |
| ASRP Exporter SDK | **Archived** | | | | | | |
| CADRG Exporter SDK | Supported | 10.2 | | | Yes | | |
| Database Interface SDK | **Archived** | | | | | | |
| Database Layer | **Archived** | | | | | | |
| Direct Import | Supported | 11.2.4 | 11.2.4 | 10.2 | Yes | Yes | Yes |
| Dynamic Data Objects (DDO) | **Deprecated** Superseded by Tracks | 11.2.4 | 11.2.4 | | Yes | Yes | |
| Earth | Supported | 10.2 | 10.2 | | Yes | | |
| ECW Data Layer | **Archived** | | | | | | |
| Editor | Supported | 11.2.4 | 11.2.4 | | Yes | Yes | |
| Entity Store | **Archived** | | | | | | |
| ER Mapper | **Archived** | | | | | | |
| GeoPackage | Supported | 11.2.4 | | 11.2.4 | Yes | Yes | Yes |
| GML Interop | Supported | 11.2.4 | 11.2.4 | | Yes | | |
| Impact Assessment | **Archived** | | | | | | |
| Interaction Modes | Supported | 11.2.4 | 11.2.4 | | Yes | Yes | |
| KML 2D Layer | Supported | 11.2.4 | | | Yes | | |
| MapLink OWS | Supported | 11.2.4 | | | Yes | | |
| Network | Supported | 11.2.4 | | | Yes | | |
| OGC Filter SDK | **Archived** | | | | | | |
| OGC Framework | Supported | 10.2 | 10.2 | 10.2 | Yes | Yes | Yes |
| OpenGL Drawing Surface | Supported | 11.2.4 | 11.2.4 | | Yes | Yes | |
| OpenGL Track Helper | Supported | 11.2.4 | 11.2.4 | | Yes | Yes | |
| OWS Context | Supported | 11.2.4 | | 10.2 | Yes | | |
| OSGEarth Bridge | **Deprecated** Use Earth SDK | 10.2 | | | Yes | | |
| Rendering Attribute Panel | Supported | 11.2.4 | | | Yes | Yes | |
| S-52 | Supported | 11.2.4 | 11.2.4 | | Yes | Yes | |
| S-63 | Supported | 11.2.4 | | | Yes | | |
| Satellite Propagator | **Deprecated** | 10.2 | | | Yes | | |
| Seamless Layer Manager | **Archived** | | | | | | |
| Spatial | **Deprecated** Merged into Editor SDK | 10.2 | 10.2 | | Yes | Yes | |
| Terrain | Supported | 11.2.4 | 11.2.4 | 10.2 | Yes | Yes | Yes |
| Terrain Viewshed | Supported | 11.2.4 | 11.2.4 | 10.2 | Yes | Yes | Yes |
| Terrain Contouring | **Deprecated** Use gdal_contour | | | | Yes | | |
| Time | **Deprecated** | 10.2 | | | Yes | | |
| Tracks | Supported | 11.2.4 | 11.2.4 | 10.2 | Yes | Yes | Yes |
| WMTS Data Layer | Supported | 11.2.4 | 11.2.4 | 10.2 | Yes | | |

# Server Components

These components provide capabilities to distribute geospatial information over a network via OGC-compliant open standard interfaces.

| Component | Status | Windows | Linux | C++ API |
| ----- | ----- | ----- | ----- | ----- |
| Web Map Service (WMS) Server (tomcat) | Supported | 10.2 | 10.2 | |
| WMS Plugin API | Supported | 10.2 | 10.2 | Yes |
| WMS Server (IIS) | **Archived** | | | |
| WMS Server (docker) | Supported | | 10.2 | |
| WMS Basic Map Config SDK | **Archived** | | | |
| WMS Basic Map Plugin | Supported | 10.2 | 10.2 | |
| WMS CADRG Map Plugin | **Archived** | | | |
| WMS Historical Map Plugin | **Archived** | | | |
| WMS Super Map Plugin | Supported | 10.2 | 10.2 | |
| Web Processing Service (WPS) Server (tomcat) | **Deprecated** | 10.2 | | |
| WPS Plugin API | **Deprecated** | 10.2 | 10.2 | Yes |
| WPS Viewshed Plugin | **Deprecated** | 10.2 | | |

# Tools

MapLink Tools support configuration and optimisation of MapLink runtimes.

| Tool | Status | Windows | Linux | Android |
| -- | -- | -- | -- | -- |
| AML XML Generator | **Archived** | | | |
| GL Data Optimiser | Supported | 11.2.4 | 11.2.4 | |
| Imagery Masking Tool | Supported | 10.2 | | |
| Image Studio | Supported | 11.2.4 | | |
| **MapLink Studio** | Supported | 11.2.4* | | |
| MapLink Studio Automation | Supported | 11.2.4 | | |
| MapViewer | Supported | 11.2.4 | | |
| Print Template Studio | Supported | 10.2 | | |
| Raster Compressor | Supported | | | 10.2 |
| Rendition Editor | Supported | 10.2 | | |
| Symbol Studio | Supported | 11.2.4 | | |

> *Although MapLink Studio is supported on Windows only, the optimised MapLink maps it generates can be loaded by MapLink runtimes on all operating systems.

# MapLink Studio Filters

MapLink Studio filters can be thought of as native geospatial format drivers that provide file parsing capabilities to MapLink Studio. Your solution requires the filters appropriate for your native geospatial formats, if you need to pre-process your geospatial data in MapLink Studio.

Because MapLink Studio is only currently supported on Windows, all filters are also supported on Windows only.

| Filter | Status | Windows |
| -- | -- | -- |
| ADRG | Supported | 11.2.4 |
| ArcGrid | Supported | 11.2.4 |
| ARCS | Supported | 11.2.4 - On request |
| Envtia ASCII | **Deprecated** | 10.2 |
| ASCII DEM | Supported | 11.2.4 |
| ASRP | Supported | 11.2.4 |
| OS Boundary Line | **Deprecated** | 10.2 |
| CADRG | Supported | 11.2.4 |
| CIB | Supported | 11.2.4 |
| CRP | **Deprecated** | 10.2 |
| DAFIF | Supported | 11.2.4 |
| DBDBV | Supported | 11.2.4 |
| DFAD | **Deprecated** | 10.2 |
| DTM/DTED | Supported | 11.2.4 |
| DXF | Supported | 11.2.4 |
| File GeoDatabase | Supported | 11.2.4 |
| GDAL | Supported | 11.2.4 |
| GeoPackage | Supported | 11.2.4 |
| GeoTIFF | Supported | 11.2.4 |
| GDF | Supported | 11.2.4 |
| GML | Supported | 11.2.4 |
| Jeppesen (ARINC) | Supported | 11.2.4 |
| JPEG2000/GMLJP2 | Supported | 11.2.4 |
| KML | Supported | 11.2.4 |
| MIF (MapInfo) | **Deprecated** | 10.2 |
| NITF | Supported | 11.2.4 |
| NTF | Supported | 11.2.4 |
| OGR | Supported | 11.2.4 |
| OS Master Map | Supported | 11.2.4 |
| Raster (generic) | Supported | 11.2.4 |
| S-57 | Supported | 11.2.4 |
| Shapefile | Supported | 11.2.4 |
| VPF | Supported | 11.2.4 |

# Note
> Any component that is listed as supported in MapLink 10.2 on Windows or Linux, but not MapLink 11.x, will be upgraded by an upcoming release.
