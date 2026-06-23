# Drawing Surfaces

## Purpose

## Windows Drawing Surfaces

## Linux Drawning Surfaces

## Cross platform Drawing Surfaces

As of MapLink 11.3.1, a cross platform TSLSkiaSurface is available to use as a drawing surface.  This surface uses the google skia rendering engine to render MapLink maps into a pixel buffer which can then be passed into any higher level framework control for display.  This cross platform flexibility means that a developer can "code once, deploy anywhere" using this surface.  However they are required to implement the display handling as the surface isn't aware of the platform it's deployed on.  To help with this, we provide both the assemblies and source code for several popular framework controls (e.g. WPF, Avalonia) that show how to implement this.  These controls can also be added directly to an existing application to provide an "drop right in" implementation of this surface.  

**Note : For 11.3.1 the linux version of this surface has had minimal testing **
