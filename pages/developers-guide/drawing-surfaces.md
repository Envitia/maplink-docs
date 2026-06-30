---
title: "Drawing Surfaces"
---

# The MapLink Pro Drawing Surface

The MapLink Pro Drawing Surface is the component that draws your mapping information to a device. It is MapLink Pro's representation of the map display. With a drawing surface, you can:
- add multiple data layers to your map display
- add moving track objects
- control the z-ordering of the data layers
- configure display properties
- draw to screen or a bitmap
- and many other mappy things.

\| [C++ API](../../api/cpp/class_t_s_l_drawing_surface_base) \| [.NET API](../../api/dotnet/class_envitia_1_1_map_link_1_1_t_s_l_n_drawing_surface_base) \|

MapLink Pro provides several types of drawing surface; the one you use depends on your application architecture and design. The different types of drawing surface are summarised below.

# Windows-Native Drawing Surfaces

The Windows-native drawing surface uses Windows GDI rendering.

\| [C++ API](../../api/cpp/class_t_s_l_n_t_surface) \| [.NET API](../../api/dotnet/class_envitia_1_1_map_link_1_1_t_s_l_n_drawing_surface) \|

# Linux-Native Drawing Surfaces

The Linux-native drawing surface uses X11 rendering.

\| [C++ API](../../api/cpp/class_t_s_l_motif_surface.html) \|

# OpenGL Drawing Surface

The OpenGL drawing surface allows an application to take advantage of hardware acceleration to enable high performance visualisations on both desktop and mobile platforms. In many circumstances it can be used as a drop-in replacement for the GDI-based and X11-based drawing surfaces from the Core SDK.

[More information...](./opengl-drawing-surface)

# Cross-platform Drawing Surfaces

As of MapLink 11.3.1, a cross platform TSLSkiaSurface is available to use as a drawing surface.  This surface uses the google skia rendering engine to render MapLink maps into a pixel buffer which can then be passed into any higher level framework control for display.  This cross platform flexibility means that a developer can "code once, deploy anywhere" using this surface.  However they are required to implement the display handling as the surface isn't aware of the platform it's deployed on.  To help with this, we provide both the assemblies and source code for several popular framework controls (e.g. WPF, Avalonia) that show how to implement this.  These controls can also be added directly to an existing application to provide a "drop right in" implementation of this surface.  

\| [C++ API](../../api/cpp/class_t_s_l_skia_surface.html) \| [C# API](../../api/dotnet/class_envitia_1_1_map_link_1_1_t_s_l_n_skia_drawing_surface.html) \|
[More information...][crossPlatformSurfaceLink]

> ** Note : The Skia-based drawing surface introduced in 11.3.1 is an early release.** Not all features are not yet supported by the drawing surface and the linux version has had minimal testing. 


[crossPlatformSurfaceLink]: ../features/cross-platform-surface
