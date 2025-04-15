# Deployment of a MapLink Pro-Based Application

* toc
{:toc}

# Licences
Please see the [Licences Page](../../licences/) for licence information and required copyright statements.

# Directory Naming Conventions
MapLink expects that the following directory conventions are observed by an application installation:

| **/bin64** | All MapLink Pro binaries and executables used by the application. Only the subset of all MapLink Pro binary files that are required by the application should be shipped |
| **/config** | The MapLink Pro configuration files used by the application. Only the subset of all MapLink Pro configuration files that are required by the application should be shipped |
| **/licences** | The LEADTOOLS.lic file should be deployed here, taken from [MAPLINKPROINSTALLDIR]/licences |

# Configuration

MapLink Pro loads all of its necessary configuration files from the **/config** directory, usually through a call to
```TSLDrawingSurface::loadStandardConfig```. When deploying an application based upon MapLink Pro, a copy of this folder must be shipped along with the application.
The MapLink Pro installer adds a reference to the system registry to allow the MapLink libraries to locate the config directory at runtime. Envitia does not recommend that this registry key or any MapLink environment variable is used when deploying applications based upon MapLink
Pro.

Therefore, as the MapLink libraries will not know the location of this directory on the deployment machine’s file system, calls to various MapLink methods will need to be changed to be passed the location of the config directory. The following table lists the current method calls which will need to be updated, depending upon the technology being used.

| C++ | .NET | Arguments |
| --- | --- | --- |
| ```TSLDrawingSurface::loadStandardConfig``` | ```TSLNDrawingSurface.loadStandardConfig``` | |
| ```TSLDrawingSurface::setupColours``` | ```TSLNDrawingSurface.setupColours``` | The directory location of tslcolours.dat |
| ```TSLDrawingSurface::setupFillStyles``` | ```TSLNDrawingSurface.setupFillStyles``` | Directory location of tslfillstyles.dat |
| ```TSLDrawingSurface::setupFonts``` | ```TSLNDrawingSurface.setupFonts``` | Directory location of tslfonts.dat |
| ```TSLDrawingSurface::setupLineStyles``` | ```TSLNDrawingSurface.setupLineStyles``` | Directory location of tsllinestyles.dat |
| ```TSLDrawingSurface::setupSymbols``` | ```TSLNDrawingSurface.setupSymbols``` | Directory location of tslsymbols.dat |
| ```TSLCoordinateSystem::loadCoordinateSystems``` | ```TSLNCoordinateSystem.loadCoordinateSystems``` | Directory location of tsltransforms.dat |
| ```TSLAPP6Ahelper::setDefaultConfigPath``` | ```TSLNAPP6Ahelper.setDefaultConfigPath``` | |
| ```TSL3DDrawingSurface::loadStandardConfig``` | ```TSLN3DDrawingSurface.loadStandardConfig``` | Directory location of tslsymbols.dat |
| ```TSL3DDrawingSurface::setupModels``` | ```TSLN3DDrawingSurface.setupModels``` | Directory location of tslmodels.dat |
| ```TSLUtilityFunctions::setMapLinkHome``` | ```TSLNUtilityFunctions.setMapLinkHome``` | Set the parent directory of /config |

The MapLink Pro config directory contains all the configuration files for MapLink Pro. When you
deploy an application you do not need to deploy all the files. You only need to deploy the files
your application requires. The following tables explain what the files are required for.

## Standard Config Directories

These files and directories are normally required by a deployment:

| File/Directory | Purpose |
| --- | --- |
| fillstyles | MapLink Pro Fillstyle configuration files. |
| Fonts | Additional fonts used by MapLink Pro. | 
| Linestyles | MapLink Pro Linestyle configuration files. | 
| Symbols | MapLink Pro symbol configuration files and symbols. *NB: There is considerable scope for reducing the number of symbols deployed in the symbols
directory to just the ones you use in your application and maps.* | 
| tslandroidfonts.dat | Android font list | 
| tslcolours.dat | Colours list | 
| tslfillstyles.dat | Fillstyle list | 
| tslfonts.dat | Windows font list | 
| tsllinestyles.dat | Linestyle list | 
| tslsymbols.dat | Standard symbol list | 
| tslsymbolsAPP6A.dat | APP6A symbology setup (required for APP6A symbols) | 
| tsltransforms.dat | Projections | 
| tslunixbitmapfonts.dat | X11 bitmap font list | 
| tslunixfonts.dat | X11 xft font list | 

## Optional Directories

Only include the directories required by your application in your deployment:

| Directory | Purpose |
| --- | --- |
| DBIF | DBIF-SDK configuration files. |
| featurebooks | Featurebooks for MapLink Pro Studio. |
| FeatureDefinitionMapping | Contains MapLink Studio configuration files. The configuration files provide standard mappings of feature and field data to an actual Feature and description. |
| geotiff | GeoTIFF filter support files. |
| gdal | GDAL/OGR Configuration files. Used by: MapLink Pro Studio; KML direct import; MapLink Pro |
| palettes | Alternative palettes for MapLink Pro Studio. |
| s52 | S-52 & S-63 SDK configuration files. |
| directimport | Direct Import driver configurations. |
| colourramps | Colour-ramps for terrain visualisations (Studio and Direct Import) |
| renditions | Renditions for specific data products |

## Optional Config Files

Only include the files required by your application in your deployment:

| File | Purpose |
| --- | --- |
| AMLS57Catalogue_v10.xml | S-57 AML Filter configuration file. |
| AMLS57Catalogue_v10_s52.xml | S-57 AML Filter configuration file for S-52. |
| 2525bConfig.csv | 2525B symbology configuration file |
| 2525bUnfilledConfig.csv | 2525B unfilled symbology configuration file |
| app6aConfig.csv | APP6A symbology configuration file |
| app6aUnfilledConfig.csv | APP6A unfilled symbology configuration file |
| APP6APalettes.dat | Palette file for the APP6A sample |
| DAFIFRedirectedAttributeLookup.txt | DAFIF Filter configuration. |
| DxfFilterEncoding.csv | DXF Filter text encoding conversions configuration file. |
| IHOS57Catalogue_v31.xml | S-57 v3.1 Filter configuration file. |
| IHOS57Catalogue_v311.xml | S-57 v3.1.1 Filter configuration file. |
| IHOS57Catalogue_v31_AMLv21.xml | AML 2.1 | 
| IHOS57Catalogue_v31_AMLv30.xml | AML 3.0 | 
| ImageStudio.ini | Image Studio configuration file. | 
| Jeppesen.ini | Jeppesen Filter configuration file. | 
| jeppesenRedirectAttributeLookup.xml | Jeppesen Filter configuration file. | 
| Landscape.tpt | Print Template | 
| mapl.ini | MapLink Studio configuration file. | 
| MapLink.fbk | MapLink Studio feature book | 
| MapLinkStudioCodePages.csv | MapLink Studio text encoding conversions configuration file. | 
| Mapluserconfig.ini | MapLink Studio user confgirable items – this is copied to the users Application directory on settings change. | 
| Metadata.xsl | Metadata xsl | 
| metadatasimple.xsl |  Metadata xsl | 
| NitfConfiguration.ini | NITF Filter configuration file. | 
| Osmastermapfilterencoding.csv | OS MasterMap filter text encoding conversions configuration file. | 
| OSMasterMap.ini | OS Mastermap configuration file. | 
| OSVectorMapLocal.ini | OS Vector Map configuration file. | 
| OSVectorMapDistrict.ini | OS Vector Map District configuration file. | 
| Portrait.tpt | Print Template | 
| stdconfig.pth | Default pathlist | 
| mapviewerlayout.dat | MapViewer default panel layout. | 
| Mapviewer.ini | Map Viewer configuration file. | 
| Mifinteroperability.ini | MIF Filter configuration file. | 
| PrintTemplateStudio.ini | Print Template Studio configuration file. | 
| ptlayout.dat | Print Template Studio default layout. | 
| stlayout.dat | Symbol Studio default layout. | 
| SymbolTool.ini | Symbol Studio configuration file. | 
| TerrainViewer.ini | Terrain Viewer configuration file. | 
| vpffield.ini | VPF Filter configuration file. | 

## Error Message Files

The error message files are used to provide error information in addition to the error number.
You only need to deploy the message files your application requires.

| File/Directory | Purpose |
| --- | --- |
| allmaplinkerrors.msg | Top level error message file which pulls in all the other error message files. Required if you need a more meaningful error message. |
| tsl3dsdkerrors.msg | 3D SDK |
| ptemsgs.msg | Print Template Studio interaction messages |
| stmsgs.msg | Symbol Studio interaction messages |
| featuresymbologyhelpererrors.msg | Feature Symbology SDK |
| owscontexterrors.msg | OWSContext SDK |
| tsl3dsdkerrors.msg | 3D SDK |
| tslacceleratorsdk.msg | Accelerator SDK |
| tslasrpexportersdkerrors.msg | ASRP Exporter SDK |
| tslcadrgexportersdkerrors.msg | CADRG Exporter SDK |
| tsldbdatalayererrors.msg | Database Layer SDK |
| tsldbifjobqueueerrors.msg | DBIF and Database Layer SDK |
| tsldbifserrors.msg | DBIF SDK |
| tslfilterdatalayererrors.msg | Filter Datalayer |
| tslfiltererrors.msg | Filters |
| tsllandlinkdigmconverrors.msg | LandLink DIGM Converter |
| tslmaplink3dimodeerrors.msg | 3D SDK Interaction modes |
| tslmaplinkddoerrors.msg | Dynamic Data Object SDK |
| tsltrackmanagererrors.msg | Tracks SDK |
| tslmaplinkedterrors.msg | Editor SDK |
| tslmaplinkentitystoreerrors.msg | Entity Store SDK |
| tslmaplinkerrors.msg | MapLink: API errors |
| tslmaplinkgeopackageerrors.msg | GeoPackage SDK |
| tslmaplinkgmlerrors.msg | GML SDK |
| tslmaplinkimodeerrors.msg | MapLink: Interaction modes |
| tslmaplinkopenglsurfaceerrors.msg | OpenGL drawing surface |
| tslmaplinkspatialerrors.msg | Spatial SDK (now part of Editor SDK) |
| tslmaplinkwfsclienterrors.msg | WFS Client SDK |
| tslmetadataerrors.msg | MapLink: Metadata |
| tslnetworksdkerrors.msg | Network SDK |
| tslogcfiltererrors.msg | OGC Filter SDK |
| tslopengldataoptimisererrors.msg | OpenGL Data Optimiser SDK |
| tslrasterprojectionerrors.msg | MapLink: Raster reprojection |
| tsls52errors.msg | S-52 SDK |
| tsls63errors.msg | S-63 SDK |
| tslsatellitepropagatorerrors.msg | Satellite Propagator SDK |
| tslterrainsdkerrors.msg | Terrain SDK |
| tsltgmerrors.msg | MapLink: TGM |
| tsltmserrors.msg | MapLink: TMS |
| tsltransformerrors.msg | MapLink: Transforms (projections) |
| tsltrasherrors.msg | MapLink: Raster Handling |

# GDAL/OGR

MapLink Pro uses GDAL/OGR in the CoreSDK. The initialisation of GDAL/OGR occurs when any of the MapLink resource files are loaded.

 GDAL/OGR uses the following two environment variables to define where to find its plugins and data:
- ```GDAL_DRIVER_PATH```
- ```GDAL_DATA```

These environment variables are not used by default because they may have been set by an unrelated application on the host machine. To force use of the variables, set the following environment variables:
- ```TTL_USE_GDAL_DRIVER_PATH```
- ```TTL_USE_GDAL_DATA```

The defaults are set by MapLink internally as follows:
- ```GDAL_DATA```: *HOME*/config/gdal
- ```GDAL_DRIVER_PATH```: *HOME*/bin64/gdalplugins/*GDAL_VERSION_MAJOR.GDAL_VERSION_MINOR*

Where:
- *HOME* = one of two values:
  - ```MAPL_HOME```
  - The parent directory of the resource file being loaded.
- *GDAL_VERSION_MAJOR.GDAL_VERSION_MINOR* = GDAL/OGR Major/Minor version
