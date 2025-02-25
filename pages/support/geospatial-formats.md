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
| ADRG | :white_check_mark: | :white_check_mark: | | |
| ARCGrid | :white_check_mark: | :white_check_mark: | | |
| ARCS Chart | :white_check_mark: (on request) | | | |
| ASCII DEM | :white_check_mark: | :white_check_mark: | | |
| ASRP | :white_check_mark: | :white_check_mark: | | :white_check_mark: TSLFilterTypeASRP |
| BSB Nautical Chart | :white_check_mark: | :white_check_mark: | | |
| CADRG/CIB | :white_check_mark: | | :white_check_mark: TSLKeyedCADRGDataLayer | :white_check_mark: TSLKeyedCADRGDataLayer |
| CRP | Deprecated | | | |
| DBDB | :white_check_mark: | | | |
| DMED | :white_check_mark: | | | |
| DTED | :white_check_mark: | | | |
| ECRG | :white_check_mark: | :white_check_mark: | | |
| ECW | :white_check_mark: | | :white_check_mark: TSLKeyedECWDataLayer | |
| GeoPackage | :white_check_mark: | | | |
| Geospatial PDF | :white_check_mark: | | | |
| GeoTIFF | :white_check_mark: | :white_check_mark: | :white_check_mark: TSLFilterTypeGeoTIFF | |
| MrSID | :white_check_mark: | :white_check_mark: | | |
| NTIF/NSIF | :white_check_mark: | :white_check_mark: | :white_check_mark: TSLFilterTypeNITF| |
| USRP | :white_check_mark: | :white_check_mark: | | |
| All in-built GDAL formats (e.g. JPG, IMG, PNG, etc) | :white_check_mark: | :white_check_mark: | | |
| Extended GDAL formats (if driver available) | :white_check_mark: | :white_check_mark: | | |
