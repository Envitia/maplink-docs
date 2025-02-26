# Geospatial & Mapping Format Support

* toc
{:toc}

This page summarises the geospatial file formats supported by MapLink Pro. The product is flexible and configurable so that it can be extended to support any format. Therefore, if your format is not listed, please contact us at **[https://support.envitia.com](https://support.envitia.com) (Requires an active maintenance & support contract)**.

## Raster Formats

MapLink Pro supports the visualisation of geospatial raster formats. Geospatial raster formats consist of cells or pixels arranged in equally spaced grids of cells with each cell representing a property at the cell's geospatial location. Examples of raster datasets include satellite and aerial photography, digitised charts, terrain relief maps, thematic data and environmental property grids.

To be displayed accurately on a map, raster data must be geo-referenced (which means that the geospatial extent and resolution of the data is known, as is the coordinate reference system used by the data). Many geospatial raster formats exist, MapLink's Image Studio tool allows any raster image to be geo-referenced and warped so that it can be used with MapLink Pro.

MapLink Studio can be used to read raster data and generate an optimised MapLink Map for runtime loading by [the TSLMapDataLayer class](../../api/cpp/class_t_s_l_map_data_layer.html).

The geospatial raster formats supported by MapLink Pro are listed in the following table.

| Raster format | Can be read by [MapLink Studio](../../pdf/MapLink%20Studio%20User%20Guide.pdf)? | Can be read by [Direct Import SDK](../../api/cpp/class_t_s_l_direct_import_data_layer.html) | Other runtime import (read) | Runtime export (write) |
| --- | --- | --- | --- | --- |
| ADRG | :heavy_check_mark: | :heavy_check_mark: | | |
| ARCGrid | :heavy_check_mark: | :heavy_check_mark: | | |
| ARCS Chart | :heavy_check_mark: (on request) | | | |
| ASCII DEM | :heavy_check_mark: | :heavy_check_mark: | | |
| ASRP | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: [TSLFilterTypeASRP](../../api/cpp/group__apigroup__api.html#gga2dce89b747707f4d70f4135a54a36ff7abc922097ef260d09507e17262a2c7a96) |
| BSB Nautical Chart | :heavy_check_mark: | :heavy_check_mark: | | |
| CADRG/CIB | :heavy_check_mark: | | :heavy_check_mark: [TSLKeyedCADRGDataLayer](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a8e7d78db9647a36c83bc3b9a2a46f844) | :heavy_check_mark: [TSLKeyedCADRGDataLayer](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a8e7d78db9647a36c83bc3b9a2a46f844) |
| CRP | Deprecated | | | |
| DBDB | :heavy_check_mark: | | | |
| DMED | :heavy_check_mark: | | | |
| DTED | :heavy_check_mark: | | | |
| ECW | :heavy_check_mark: | | | |
| GeoPackage | :heavy_check_mark: | | | |
| Geospatial PDF | :heavy_check_mark: | | | |
| GeoTIFF | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: [TSLFilterTypeGeoTIFF](../../api/cpp/group__apigroup__api.html#gga2dce89b747707f4d70f4135a54a36ff7a084974d1342b6e1f8761c23e40fc6d5c) | |
| MrSID | :heavy_check_mark: | :heavy_check_mark: | | |
| NTIF/NSIF | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: [TSLFilterTypeNITF](../../api/cpp/group__apigroup__api.html#gga2dce89b747707f4d70f4135a54a36ff7a5151bdafd9d2842aec4c3bbee1956244) | |
| USRP | :heavy_check_mark: | :heavy_check_mark: | | |
| All in-built GDAL formats (e.g. JPG, IMG, PNG, etc) | :heavy_check_mark: | :heavy_check_mark: | | |
| Extended GDAL formats (if driver available) | :heavy_check_mark: | :heavy_check_mark: | | |
| OGC Web Map Service (WMS) | | | :heavy_check_mark: [TSLWMSDataLayer](../../api/cpp/class_t_s_l_w_m_s_data_layer.html) | |
| OGC Web Map Tile Service (WMTS) | | | :heavy_check_mark: [TSLWMTSDataLayer](../../api/cpp/class_t_s_l_w_m_t_s_data_layer.html) | |

## Vector Formats

Geospatial vector data represent geographic information using points, lines, and polygons. It can be used for visualisation and analysis. Vector data can represent features like roads, cities, properties, boundaries, mountains, and bodies of water. Vector data can be analyzed to show how different features interact with each other.

MapLink Studio can be used to read vector data and generate an optimised MapLink Map for runtime loading by [the TSLMapDataLayer class](../../api/cpp/class_t_s_l_map_data_layer.html).

The geospatial vector formats supported by MapLink Pro are listed in the following table.

| Vector format | Can be read by [MapLink Studio](../../pdf/MapLink%20Studio%20User%20Guide.pdf)? | Can be read by [Direct Import SDK](../../api/cpp/class_t_s_l_direct_import_data_layer.html) | Other runtime import (read) | Runtime export (write) |
| --- | --- | --- | --- | --- |
| DAFIF | :heavy_check_mark: | | | |
| DBDB | :heavy_check_mark: | | | |
| DFAD | :heavy_check_mark: | | | |
| DXF | :heavy_check_mark: | :heavy_check_mark: | | |
| Esri FileGeodatabase (FileGDB) | :heavy_check_mark: | | | |
| Esri Shapefile | :heavy_check_mark: | :heavy_check_mark: | | |
| GDF3 | :heavy_check_mark: | | | |
| GeoPackage | :heavy_check_mark: | | | |
| GML | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: [TSLKeyedGML](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685aa3fe9121ba0d29b655a9062d248dbe3b) | :heavy_check_mark: [TSLKeyedGML](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685aa3fe9121ba0d29b655a9062d248dbe3b) |
| Jeppesen/ARINC | :heavy_check_mark: | | | |
| KML Simple Features 2D | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | |
| MIF/MID | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: [TSLKeyedMIFImport](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a3b153c2e231454ebe754f7811bcfb5d5) | :heavy_check_mark: [TSLKeyedMIFExport](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685aa6a435de08a1d49c0d5ea96b197bcd27) |
| NITF/NSIF | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: [TSLFilterTypeNITF](../../api/cpp/group__apigroup__api.html#gga2dce89b747707f4d70f4135a54a36ff7a5151bdafd9d2842aec4c3bbee1956244) | |
| OpenStreetMap | :heavy_check_mark: | | | |
| OS MasterMap | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: [TSLKeyedMasterMapImport](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a58d63e0bda7da9d76c99345815983081) | :heavy_check_mark: [TSLKeyedMasterMapExport](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a2d4411823cae5d853440bb71a8302f12) |
| OS NTF | :heavy_check_mark: | :heavy_check_mark: | | |
| OS VectorMap Local | :heavy_check_mark: | | | |
| OS VectorMap District | :heavy_check_mark: | | | |
| OS Boundary Line 2000 | :heavy_check_mark: | | | |
| S-57 (unencrypted ENC & AML) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: [TSLKeyedS57Import](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a40c94985894df558de17c9ba77ea828d) | :heavy_check_mark: [TSLKeyedS57Export](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a89677fd6435f9be4e14df55531487553) |
| S-57 Encrypted (S-63) | | | :heavy_check_mark: [TSLKeyedS63](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a5ff85714a971a94678d0029870b45684) | |
| US Census TIGER/Line | :heavy_check_mark: | :heavy_check_mark: | | |
| VPF (DNC, VMAP, WVS etc.) | :heavy_check_mark: | | | |
| All in-built GDAL/OGR formats (e.g. GeoJSON, GPX, DGN, OGC Web Feature Service (WFS), etc) | :heavy_check_mark: | :heavy_check_mark: | | |
| Extended GDAL/OGR formats (if driver available) | :heavy_check_mark: | :heavy_check_mark: | | |

## Terrain/Elevation Gridded Formats

Terrain and elevation formats are used to record properties like ground and building heights for terrain analysis such as line of sight, viewshed and contouring. Other properties can be used instead of physical heights, for example, environmental data can be used with contouring algorithms to determine where temperature fronts occur.

MapLink Studio can be used to read the data and generate an optimised MapLink Terrain Database for use in the [MapLink Terrain SDK](../../api/cpp/group__apigroup__terrain__api.html).

The geospatial terrain and elevation gridded formats supported by MapLink Pro are listed in the following table.

| Terrain format | Can be read by [MapLink Studio](../../pdf/MapLink%20Studio%20User%20Guide.pdf)? | Other runtime import (read) |
| --- | --- | --- |
| ARCGrid | :heavy_check_mark: | |
| DBDB | :heavy_check_mark: | |
| DEM/DTM | :heavy_check_mark: | |
| DMED | :heavy_check_mark: | :heavy_check_mark: [TSLKeyedDMEDTerrainDatabase](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a2052a244eba73f51c85146e8b838572a) |
| DTED | :heavy_check_mark: | :heavy_check_mark: [TSLKeyedDMEDTerrainDatabase](../../api/cpp/group__apigroup__api.html#ggabe69c639edbea50d68f890ed6838d685a2052a244eba73f51c85146e8b838572a) |
