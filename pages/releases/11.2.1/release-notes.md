# Release Notes - MapLink Pro - Version 11.2.1

* toc
{:toc}

# Related Pages

- [Upgrade Notes](../../support/install-and-upgrade)
- [Supported Platforms](../../support/platform-support)
- [Supported SDKs](../../support/sdk-support.md)

# Features
    * 1875	[Wrap-around 2D maps](../../features/wrap-around-maps)
        * As a C2 operator, I want my 2D world map to wrap around coordinate system bounds, so that I have a realistic display of geospatial features that span the dateline

# Improvements
    * 3055  [MLK-2702] Merge XXXX project fixes into MapLink 11
        * XXXX-118 Editor/Spatial .NET wrappers don't support Follow Mode with the "polyline", "polygon" or "replacesection" operations
        * XXXX-119 Backport generic improvements we make to C# demo app onto the MapLink CSharpEditorSample
        * XXXX-152 Backport generic improvements we make to C# demo app onto the MapLink CSharpAPP6ASample
        * XXXX-113 BUG: MapLink crashes if use topologicalmovepoint, topologicaladdpoint or topologicaldeletepoint on a Bordered Polygon
        * XXXX-117 BUG: movepoint, addpoint and deletepoint operations crash in MapLink 10.2
        * XXXX-121 BUG: Spatial.NET cannot return values from "calcarea" or "calclinelength" query operations
        * XXXX-124 Polygon intersections have the wrong styling when activated via Editor/Spatial .NET wrappers
        * XXXX-126 MapLink's osmastermapfilter triggers repeated assertion failures when reading certain datasets

# Known Issues
    * 4133	Some raster tiles temporarily do not draw when using wrap-around mode