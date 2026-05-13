---
title: "MapLink Pro Developer's Guide"
permalink: /pages/developers-guide/
---

# MapLink Pro Developer's Guide

This guide covers all MapLink Pro SDKs - describing their facilities, how to integrate them, and how to get the most from them. It applies to Windows C++ and .NET development unless otherwise noted.

<a href="{{ "/pdf/MapLink Developer's Guide.pdf" | relative_url }}" class="btn" target="_blank">Download PDF</a>

---

## Getting Started

| | |
|---|---|
| [Introduction](introduction) | Overview, glossary, and training options |
| [MapLink SDK Components and Concepts](sdk-components) | The full SDK family - Core, OpenGL, Tracks, Terrain, 3D Earth, Editor, and more |
| [Basic MapLink Applications](basic-applications) | Application architecture, Document/View model, error handling, interaction modes |

## Development Setup

| | |
|---|---|
| [MapLink and your Development Environment](development-environment) | Visual Studio configuration, library naming, headers, Unicode support |
| [Deployment of End User Application](deployment) | Runtime DLLs, config files, and distribution requirements |
| [Samples](samples) | Sample applications included with MapLink Pro |

## Walkthroughs

| | |
|---|---|
| [Walkthrough 1 - Your First MapLink Application](walkthrough-1) | MFC SDI app that loads and displays a MapLink map |
| [Walkthrough 2 - Modifying the Visible Area](walkthrough-2) | Zoom, pan, grab, and mouse wheel interaction |
| [Walkthrough 3 - Adding a Simple Vector Overlay](walkthrough-3) | Creating and displaying vector geometry on a map |

## Core SDK

| | |
|---|---|
| [Geometry and Overlays](geometry-and-overlays) | Entities, polylines, polygons, symbols, text, ellipses, and collections |
| [More Features of the Core SDK](advanced-features) | Feature rendering, coordinate systems, data layers, and surface options |
| [Unicode](unicode) | Unicode support, fonts, geometry, filenames, and FAQ |

## SDK Reference

| | |
|---|---|
| [OpenGL Drawing Surface](opengl-drawing-surface) | Hardware-accelerated rendering as a drop-in replacement for GDI/X11 surfaces |
| [Direct Import SDK](direct-import-sdk) | Runtime ingestion of geospatial formats without pre-processing |
| [Tracks SDK](tracks-sdk) | Real-time display of moving objects with history trails |
| [Dynamic Overlays with the DDO SDK](ddo-sdk) | Fully custom animated overlays via TSLDisplayObject |
| [Terrain SDK](terrain-sdk) | Elevation data, viewshed analysis, contouring, and cross-sections |
| [MapLink 3D Earth SDK](maplink-3d-earth-sdk) | Globe-based 3D rendering using osgEarth integration |
| [Editor SDK](editor-sdk) | Interactive vector overlay creation and editing |
| [Geopackage SDK](geopackage-sdk) | Reading and display of OGC GeoPackage files |
| [OWSContext SDK](owscontext-sdk) | Reading and display of OWSContext documents |
| [MapLink OGC Services SDK](ogc-services-sdk) | WMS and WPS server plug-in development |
| [Spatial SDK](spatial-sdk) | Spatial operations and map update island management |
| [GML SDK](gml-sdk) | Reading and writing GML application schemas and instance data |
| [.NET SDKs](net-sdks) | C# and VB.NET wrappers with walkthroughs |
| [MapLink Camera Manager](camera-manager) | Camera management for 3D and accelerated surfaces |

## Advanced Topics

| | |
|---|---|
| [Floating Point](floating-point) | Floating-point configuration requirements |
| [Other SDKs](other-sdks) | Additional SDK coverage |
| [Threading](threading) | Thread safety rules, known issues, and threading options |
| [DIGM to TMF Conversion](digm-to-tmf) | Converting DIGM data to TMF format |
