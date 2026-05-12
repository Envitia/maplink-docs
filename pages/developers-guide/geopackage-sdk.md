---
title: "Geopackage SDK"
---

# Geopackage SDK


The [GeoPackage](http://www.geopackage.org/) SDK allows a developer to
read, analyse and display [GeoPackage](http://www.geopackage.org/) data
files.

**Please contact** <support@envitia.com> **for additional information on
the implementation.**

## Library Usage and Configuration

As with the MapLink Core SDK, the GeoPackage SDK comes in 2 different
flavours. It should be noted that the library to be linked with should
be determined by the Core SDK library that you are using within your
application. For example, if you are using the Release mode, DLL version
of the Core SDK (MapLink.lib/MapLink64.lib) then you must also use the
equivalent GeoPackage SDK library
(MapLinkGeoPackage.lib/MapLinkGeoPackage64.lib).

+----------------------------------+-----------------------------------+
| **MapLinkGeoPackage.lib or       | **MapLinkGeoPackaged.lib or       |
| MapLinkGeoPackage64.lib**        | MapLinkGeoPackage64d.lib**        |
|                                  |                                   |
| Release mode, DLL version.       | Debug mode, DLL version.          |
|                                  |                                   |
| Uses Multithreaded DLL C++       | Uses Debug Multithreaded DLL C++  |
| run-time library.                | run-time library.                 |
|                                  |                                   |
| Requires TTLDLL preprocessor     | Requires TTLDLL preprocessor      |
| directive.                       | directive.                        |
|                                  |                                   |
| Must also link the MapLink       | Must also link the MapLink        |
| CoreSDK library MapLink.lib      | CoreSDK library MapLinkd.lib      |
|                                  |                                   |
| Refer to the document \"MapLink  | No redistributable run-time       |
| Pro X.Y: Deployment of End User  | available.                        |
| Applications\" for a list of     |                                   |
| run-time dependencies when       | **KEYED : Development machines    |
| redistributing.                  | only.**                           |
|                                  |                                   |
| Where X.Y is the version of      |                                   |
| MapLink you are deploying.       |                                   |
+----------------------------------+-----------------------------------+



---

[← Editor SDK](editor-sdk) | [OWSContext SDK →](owscontext-sdk)
