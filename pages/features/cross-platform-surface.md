---
title: "MapLink Pro 11.3.1: Cross-platform Drawing Surface"
---

## Introducing Early Release of Skia-Based Drawing Surfaces and XAML Integration

MapLink Pro 11.3.1 introduces a major step forward in the platform’s evolution towards supporting cross-platform, code-once-deploy-anywhere geospatial applications. This version of MapLink Pro delivers early releases of a new **Skia‑based 2D rendering foundation** and modern **.NET UI integrations for WPF and Avalonia**.

These enhancements address longstanding limitations in UI embedding and platform portability, and establish the groundwork for future MapLink Pro capabilities.


## Why This Matters

Historically, MapLink Pro has provided high-performance drawing surfaces using native rendering pipelines such as GDI and X11. However, these approaches are inherently platform-specific.

The introduction of a Skia-based rendering layer changes this model:

- A single rendering backend can now operate consistently across platforms  
- Rendering is decoupled from native UI frameworks  
- Applications can evolve towards cross-platform deployment with minimal rework  

[Skia](https://skia.org/) is a widely used, high-performance 2D graphics engine with consistent rendering across Windows, Linux, mobile, and web environments.


## The Skia-Based Drawing Surface

### Overview

The new core capability introduced in 11.3.1 is a Skia-backed drawing surface:

- **.NET API:** `TSLNSkiaDrawingSurface`  
- **C++ API:** `TSLSkiaSurface`  

The classes are added to the core:

- `Envitia.MapLink.MapLink64` (.NET 10, currently Windows-only)  
- `MapLink64` (C++)

### Cross-Platform Rendering Core

The surface is designed to operate consistently across:

- Windows  
- Linux  

By using Skia’s unified rendering model, drawing commands are translated into a consistent output regardless of the underlying OS.

Core rendering capabilities supported in the release include:
- Vector, raster and terrain 2D rendering.
- Loading of map data layers, standard data layers, and Direct Import data layers.
- All coordinate system transformations, visualisation options and rendering pipelines provided by the Core SDK.

### Off-Screen Rendering Model

The surface renders into a pixel buffer, rather than directly to a native window:

- Rendering target: bitmap / pixel buffer  
- No dependency on platform drawing contexts  

### Foundation for Future Platform Independence

By abstracting away native drawing APIs:

- MapLink rendering becomes UI-framework agnostic  
- Enables future targets such as:
  - WebAssembly  
  - Mobile platforms  
  - Cross-platform .NET UI frameworks  

This forms the foundation for the **code-once / deploy-anywhere** roadmap ambition.

### Sample Application
For sample code demonstrating the use of the Skia Drawing Surface, see [the maplink-samples/SkiaDrawingSurface samples](https://github.com/Envitia/maplink-samples/tree/main/SkiaDrawingSurface).

## WPF Integration

`TSLNSkiaDrawingSurfaceWPFControl`

To support modern .NET desktop applications, MapLink Pro 11.3.1 introduces a **WPF-native drawing control**.

The control is available from a new `Envitia.MapLink.TSLNSkiaDrawingSurfaceWPFControl` .NET library included in the MapLink installation.

### Purpose

- Enables MapLink rendering directly within WPF XAML applications
- Provides a drop-in UI component for .NET developers
- Eliminates the need for custom interop layers

### Usage Model

The control can be declared directly in XAML, similar to standard WPF controls:

```
<maplink:TSLNSkiaDrawingSurfaceWPFControl x:Name="MapControl" 
    MinWidth="100"
    MinHeight="100"
    BaseMap ="C:\Program Files\Envitia\MapLink Pro\11.3\Maps\NaturalEarthBasic\NaturalEarthBasic.map" />
```

### Sample Application
For sample code demonstrating the use of the WPF control, see [the maplink-samples/WPFControlSample](https://github.com/Envitia/maplink-samples/tree/main/WPFControlSample).


## Avalonia UI Integration

`TSLNSkiaDrawingSurfaceWPFControl`

MapLink Pro 11.3.1 also introduces an **Avalonia UI drawing control**.

The control is available from a new `Envitia.MapLink.TSLNSkiaDrawingSurfaceAvaloniaControl` .NET library included in the MapLink installation.

### Purpose

- Enables MapLink rendering directly within Avalonia AXAML applications
- Provides another drop-in UI component for .NET developers
- **Demonstrates MapLink's intention to provide a code-once-deploy-anywhere capability, leveraging the flexibility of [Avalonia UI](https://avaloniaui.net/).**

### Usage Model

The control can be declared directly in AXAML, similar to standard controls:

```
<maplink:TSLNSkiaDrawingSurfaceAvaloniaControl x:Name="MapControl"
    HorizontalAlignment="Stretch"
    VerticalAlignment="Stretch"
    BaseMap="C:\Program Files\Envitia\MapLink Pro\11.3\Maps\NaturalEarthBasic\NaturalEarthBasic.map" />
```

### Sample Application

For sample code demonstrating the use of the Avalonia control, see [the maplink-samples/AvaloniaControlSample](https://github.com/Envitia/maplink-samples/tree/main/AvaloniaControlSample).


## What's Next?

> We invite comments on these early releases of both the Skia‑based 2D drawing surface and .NET UI integrations for WPF and Avalonia.

We are working on various enhancements to the capability, including:
- Support for the Tracks and DDO data layers
- Custom data layer support

Building upon these enhancements, we will be continuing the evolution to our **code-once / deploy-anywhere** roadmap ambition. The features we plan to explore and deliver include<sup>*</sup>:
- Android, iOS, macOS and WebAssembly support.
- Enhanced cross-platform 3D support.
- Integrated support for more UI frameworks: MAUI, Qt, Blazor, Java UIs, Python UIs, etc
- Integration of Skia-rendering backend rendering options (OpenGL, Vulkan, WebGL etc)

> <sup>*</sup>Roadmap items are subject to change and re-prioritisation. Please let us know if there is anything you're interested in or you'd like to see added. Your feedback is essential to ensure we deliver the right features, in the right order.