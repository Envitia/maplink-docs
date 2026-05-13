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

<table class="doc-table">
  <tbody>
    <tr><td><strong>MapLinkGeoPackage.lib or MapLinkGeoPackage64.lib</strong> Release mode, DLL version. Uses Multithreaded DLL C++ run-time library. Requires TTLDLL preprocessor directive. Must also link the MapLink CoreSDK library MapLink.lib Refer to the document \"MapLink Pro X.Y: Deployment of End User Applications\" for a list of run-time dependencies when redistributing. Where X.Y is the version of MapLink you are deploying.</td><td><strong>MapLinkGeoPackaged.lib or MapLinkGeoPackage64d.lib</strong> Debug mode, DLL version. Uses Debug Multithreaded DLL C++ run-time library. Requires TTLDLL preprocessor directive. Must also link the MapLink CoreSDK library MapLinkd.lib No redistributable run-time available. <strong>KEYED : Development machines only.</strong></td></tr>
  </tbody>
</table>



---

[← Editor SDK](editor-sdk) | [OWSContext SDK →](owscontext-sdk)