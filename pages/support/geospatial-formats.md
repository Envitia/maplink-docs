# Geospatial & Mapping Format Support

* toc
{:toc}

This page summarises the geospatial file formats supported by MapLink Pro. The product is flexible and configurable so that it can be extended to support any format. Therefore, if your format is not listed, please contact us at **[https://support.envitia.com](https://support.envitia.com) (Requires an active maintenance & support contract)**.

## Raster Formats

MapLink Pro supports the visualisation of geospatial raster formats. Geospatial raster formats consist of cells or pixels arranged in equally spaced grids of cells with each cell representing a property at the cell's geospatial location. Examples of raster datasets include satellite and aerial photography, digitised charts, terrain relief maps, thematic data and environmental property grids.

To be displayed accurately on a map, raster data must be geo-referenced (which means that the geospatial extent and resolution of the data is known, as is the coordinate reference system used by the data). Many geospatial raster formats exist, MapLink's Image Studio tool allows any raster image to be geo-referenced and warped so that it can be used with MapLink Pro.

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
| OGC WMS | | | :heavy_check_mark: [TSLWMSDataLayer](../../api/cpp/class_t_s_l_w_m_s_data_layer.html) | |
