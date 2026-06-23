# .NET Controls

## Overview

MapLink 11.3.1 onwards provide simple mechanisms for integrating MapLink visuals and interactions into your .NET applications.  There are several options available, and the underlying mechanism can be used to create controls for a host of frameworks.  The MapLink install currently provides controls for WPF and Avalonia (Windows only) applications.

## WPF Control

The WPF control provides an interactive MapLink visual "out of the box" with minimal set up.  It also provides mechanisms for more advanced interactions with the underlying drawing surface if required.  

### XAML API

To get started, first add the ```bin64/Envitia.MapLink.TSLNSkiaDrawingSurfaceWPFControl.dll``` as a reference in your .NET 10 project.

Then add the following code snippets to your applications xaml file : 

```xaml
    xmlns:ctrl="clr-namespace:Envitia.MapLink.TSLNSkiaDrawingSurfaceControl;assembly=Envitia.MapLink.TSLNSkiaDrawingSurfaceWPFControl"
```

```xaml  
    <ctrl:TSLNSkiaDrawingSurfaceWPFControl x:Name="MapControl" 
                                    MinWidth="100"
                                    MinHeight="100"
                                    BaseMap ="C:\Program Files\Envitia\MapLink Pro\11.2\Maps\NaturalEarthBasic\NaturalEarthBasic.map" 
                                    />
```

### Programming API

The control can be accessed programmatically via the MapControl handle.  It provides the following API:

| Name | Signature | Description |
|:-------- |:------- |:-------- |
|LoadMap  |bool LoadMap(string mapPath) |Imperatively load a map layer|
|Zoom |bool Zoom(int percentage, bool zoomIn) |Programmatic zoom|
|Pan |bool Pan(double x, double y) |Pan to user-unit coordinate|
|DUToUU |bool DUToUU(int deviceX, int deviceY, out double userX, out double userY) |Convert device → map coordinates|
|ResetView |void ResetView() |Reset to full map extent|
|RequestRender| void RequestRender() |Trigger a re-render|

### Advanced Features

The control exposes a property named ```DrawingSurface``` that can be accessed via ```MapControl.DrawingSurface``` to provide access to the full API provided by ```TSLNSkiaDrawingSurface```.

### Known Issues

The WPF XAML editor will crash unless the MapLink dlls are copied into the applications output folder.  This is due to the designer creating a shadow cache of dlls and failing to find the native C++ libraries unless they are
co-located with the C# dlls.



## Avalonia Control

### XAML API

This functions in a very similar way to the WPF control. Add the ```bin64/Envitia.MapLink.TSLNSkiaDrawingSurfaceAvaloniaControl.dll``` assembly to your project, then add the following snippets to your .axaml file: 
```xaml  
      xmlns:ctrl="clr-namespace:Envitia.MapLink.TSLNSkiaDrawingSurfaceControl;assembly=Envitia.MapLink.TSLNSkiaDrawingSurfaceAvaloniaControl"
```

```xaml  
      <ctrl:TSLNSkiaDrawingSurfaceAvaloniaControl x:Name="MapControl"
                                          HorizontalAlignment="Stretch"
                                          VerticalAlignment="Stretch"
                                          BaseMap="C:\Program Files\Envitia\MapLink Pro\11.3\Maps\NaturalEarthBasic\NaturalEarthBasic.map"/>
```

The control can then be accessed programmatically in the same way as the WPF control.
