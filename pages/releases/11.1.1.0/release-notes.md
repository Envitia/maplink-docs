# Release Notes - MapLink Pro - Version 11.1.1.0

* toc
{:toc}

# Related Pages
- [Upgrade Notes](../../support/install-and-upgrade)
- [Supported Platforms](../../support/platform-support)
- [Supported SDKs](../../support/sdk-support.md)

# Defects
    * [MLK-381] - GDAL envitiacode.h contains 'This file must not be distributed' but is shipped
    * [MLK-868] - Qt samples contain readme with incorrect information
    * [MLK-1672] - MapLink Filters include copies of libjpeg from the 1990s
    * [MLK-2048] - MapLink Compiled Help reports errors
    * [MLK-2493] - Installer does not properly display the license agreement
    * [MLK-2504] - Broken doxygen generated API docs

# Stories
    * [MLK-2057] - Update boost libraries to latest version
    * [MLK-2058] - Update Crypto++ to latest version
    * [MLK-2059] - Update Curl to latest version
    * [MLK-2060] - Update Expat to latest version
    * [MLK-2061] - Update FontConfig to latest version
    * [MLK-2062] - Update FreeType to latest version
    * [MLK-2063] - Update Fribidi to latest version
    * [MLK-2064] - Update GDAL to latest version
    * [MLK-2065] - Update geographiclib to latest version
    * [MLK-2066] - Update Glew to latest version
    * [MLK-2067] - Update Glib to latest version
    * [MLK-2068] - Update GraphicsMagick to latest version
    * [MLK-2069] - Update Harfbuzz to latest version
    * [MLK-2070] - Update to libjpeg to latest version
    * [MLK-2071] - Update IntelTBB to latest version
    * [MLK-2072] - Update libiconv to latest version
    * [MLK-2073] - Update libtess to latest version
    * [MLK-2074] - Update Libxft to latest version
    * [MLK-2075] - Update libxml2 to latest version
    * [MLK-2076] - Update lpng to latest version
    * [MLK-2077] - Update openjpeg to latest version
    * [MLK-2078] - Update OpenSceneGraph to latest version
    * [MLK-2079] - Update OSGEarth to latest version
    * [MLK-2080] - Update poppler to latest version
    * [MLK-2081] - Update poppler-data to latest version
    * [MLK-2082] - Update qt to latest version
    * [MLK-2083] - Update SQLite to latest version
    * [MLK-2084] - Update libtiff to latest version
    * [MLK-2085] - Update xmlxerces to latest version
    * [MLK-2086] - Update zlib to latest version
    * [MLK-2087] - Update minizip to latest version
    * [MLK-2192] - Generate the MapLink documentation through CMake
    * [MLK-2222] - Integrate SonarQube into the MapLink Linux pipeline
    * [MLK-2264] - Upgrade pango to latest version
    * [MLK-133] - Remove "Debug for Release" build configurations
    * [MLK-210] - Stop shipping the old unmaintained VS2005 and 2010 project files
    * [MLK-874] - Archive MapLink Visual Studio Wizards
    * [MLK-1658] - Update shipped documentation for 32-bit removal
    * [MLK-1849] - Spike: Review TUT Tests and identify dependencies on other machines
    * [MLK-1934] - Archive: WPS: Vincenty Inverse Plugin
    * [MLK-1937] - Archive: Continuous Foundation Server
    * [MLK-2027] - Static analysis on codebase
    * [MLK-2050] - Upgrade WMS for Tomcat 10
    * [MLK-2056] - Full Upgrade to Windows 11 SDK and Visual Studio 2022
    * [MLK-2134] - Test GCC 5.4 changes on Windows
    * [MLK-2221] - Integrate SonarQube into the MapLink Windows pipeline
    * [MLK-2273] - Incorporate All Dependency Updates
    * [MLK-2276] - Upgrade codebase to latest compiler toolchains
    * [MLK-2282] - Rebrand all documentation
    * [MLK-2283] - Rebrand installers
    * [MLK-2303] - Mark contouring SDK as deprecated
    * [MLK-2313] - Upgrade compiler used for Desktop Linux builds
    * [MLK-2314] - Upgrade compiler used for Windows builds
    * [MLK-2335] - Open source sample code download
    * [MLK-2426] - Installer Streamlining
    * [MLK-2432] - TS023809 Formally include createFontID() in API
    * [MLK-2434] - Archiving: Remove SDK folders from codebase
    * [MLK-2435] - Archiving: Remove SDKs from documentation
    * [MLK-2436] - Archiving: Remove SDKs from installers
    * [MLK-2437] - Archiving: Remove SDKs from build system
    * [MLK-2440] - Archiving: Disable archived SDKs in licensing system
    * [MLK-2461] - Write deprecation policy
    * [MLK-2467] - Spike - Upgrade to Windows 11 SDK and Visual Studio 2022 - what breaks?
    * [MLK-2470] - Update shipped MapLink Studio projects to remove QNAP references
    * [MLK-2518] - Generate build artifacts for all TPL libraries
    * [MLK-2520] - Upgrade Core SDK to Windows 11 SDK and Visual Studio 2022
    * [MLK-2525] - Upgrade Rocky8 container to Rocky9
    * [MLK-2570] - Turn on frame pointers in Release configurations
    * [MLK-2571] - Remove all Debug for Release references in build pipelines and VS projects
    * [MLK-2572] - Remove Debug for Release references from installers and docs
    * [MLK-2576] - Integrate new TPL libraries into CoreSDK
    * [MLK-2578] - Update project files for CoreSDK 
    * [MLK-2581] - Update CoreSDK Cmake to create release bundles for both windows and linux
    * [MLK-2594] - Update project files for APP11
    * [MLK-2597] - Update project files for Direct Import SDK
    * [MLK-2600] - Update project files for Editor
    * [MLK-2602] - Update project files for GMLInterop
    * [MLK-2603] - Update project files for InteractionModes
    * [MLK-2604] - Update project files for KML2DLayer
    * [MLK-2605] - Update project files for MapLinkOWS
    * [MLK-2608] - Update project files for OpenGLDrawingSurface
    * [MLK-2610] - Update project files for OWSContext
    * [MLK-2612] - Update project files for RenderingAttributePanel
    * [MLK-2613] - Update project files for S-52
    * [MLK-2614] - Update project files for S-63
    * [MLK-2617] - Update Terrain SDK to work with new TPLs
    * [MLK-2618] - Update project files for Terrain: Viewshed
    * [MLK-2622] - Update project files for WMTSDataLayer
    * [MLK-2631] - Update project files for GLDataOptimiser
    * [MLK-2633] - Image Studio: Update project files
    * [MLK-2635] - MapLink Studio: Update project files
    * [MLK-2636] - MapLink Studio Automation: Update project files
    * [MLK-2638] - MapViewer: Update project files
    * [MLK-2642] - SymbolStudio: Update project files
    * [MLK-2643] - Filters: ADRG: Update project files
    * [MLK-2644] - Filters: ArcGrid: Update project files
    * [MLK-2645] - Filters: ARCS: Update project files
    * [MLK-2647] - Filters: ASCII DEM: Update project files
    * [MLK-2648] - Filters: ASRP: Update project files
    * [MLK-2650] - Filters: CADRG: Update project files
    * [MLK-2651] - Filters: CIB: Update project files
    * [MLK-2653] - Filters: DAFIF: Update project files
    * [MLK-2654] - Filters: DBDBV: Update project files
    * [MLK-2656] - Filters: DTM/DTED: Update project files
    * [MLK-2657] - Filters: DXF: Update project files
    * [MLK-2658] - Filters: FileGDB: Update project files
    * [MLK-2659] - Filters: GDAL: Update project files
    * [MLK-2660] - Filters: GeoPackage: Update project files
    * [MLK-2661] - Filters: GeoTIFF: Update project files
    * [MLK-2662] - Filters: GDF: Update project files
    * [MLK-2663] - Filters: GML: Update project files
    * [MLK-2664] - Filters: Jeppesen: Update project files
    * [MLK-2665] - Filters: JPEG2000/GMLJP2: Update project files
    * [MLK-2666] - Filters: KML: Update project files
    * [MLK-2668] - Filters: NITF: Update project files
    * [MLK-2669] - Filters: NTF: Update project files
    * [MLK-2670] - Filters: OGR: Update project files
    * [MLK-2671] - Filters: OS Master Map: Update project files
    * [MLK-2672] - Filters: Raster (generic): Update project files
    * [MLK-2673] - Filters: S-57: Update project files
    * [MLK-2674] - Filters: Shapefile: Update project files
    * [MLK-2675] - Filters: VPF: Update project files
    * [MLK-2701] - SLD Handling causes test to crash
    * [MLK-2703] - Create OpenGL jenkins deployment node for Linux
    * [MLK-2747] - Build and execute CoreSDK tests on Linux using upgraded CoreSDK
    * [MLK-2748] - Integrate the required GDAL changes into GDAL 3.9 library
    * [MLK-2757] - Update project files for Core SDK .NET API
    * [MLK-2760] - Update project files for Direct Import .NET API
    * [MLK-2762] - Update project files for Editor.NET API
    * [MLK-2765] - Update project files for OpenGLDrawingSurface .NET API
    * [MLK-2767] - Update project files for RenderingAttributePanel .NET API
    * [MLK-2768] - Update project files for S-52 .NET API
    * [MLK-2769] - Update project files for S-63 .NET API
    * [MLK-2771] - Update project files for Terrain .NET API
    * [MLK-2773] - Migrate Linux raster handling to LEADTOOLS
    * [MLK-2799] - Build libtess and etcpack TPLs to unblock openGLSurface upgrades
    * [MLK-2800] - TerrainViewer: Update project files
    * 430        - Upgrade OGCSDKs projects to use new TPLs
    * 672        - Update ThirdPartyInterOp SDK to build with latest compilers and SDKs
    * 965        - Upgrade third party interop SDK
    * 1055       - Upversion to 11.1
    * 1228       - Regenerate Wix Installer
    

# Known Issues
    * 1451	KML overlay translucency