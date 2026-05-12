---
title: ".NET SDKs"
---

# .NET SDKs


Developers familiar with the MapLink C++ API will find that the .NET
APIs are very similar with the only major difference being the names of
the classes.

The C++ API uses the class name prefix TSL to denote Envitia classes
whereas the .NET libraries use the prefix TSLN. Other differences
include the removal of Envitia helper classes such as TSLSimpleString,
TSLifstream and TSLofstream which have been replaced with similar
helpers from the .NET framework.

Furthermore certain 'getter' and 'setter' methods have been replaced by
.NET properties or indexers.

Lastly the concept of colour indexes taken from the colour table has
been hidden in the .NET wrappers meaning that when getting or setting
colours the .NET framework class Color should be used.

Developers new to MapLink may wish to read the sections that deal with
the basic use of MapLink in this document as the use of the .NET
wrappers is almost identical. Although this section of the document will
repeat some of these basic topics from a .NET view point, it won't cover
them in such depth and is intended for users familiar with MapLink to
assist getting to grips with its use via .NET.

## Library Usage and Configuration

Currently MapLink supports .NET wrappers for the following SDKs with the
library name and namespace listed:

+-------------+-----------------------------------------------+-----------------------------------------+
| SDK         | Library Name                                  | Namespace                               |
+=============+===============================================+=========================================+
| Core SDK    | Envitia.MapLink64.dll                         | Envitia.MapLink                         |
|             |                                               |                                         |
|             | Envitia.MapLinkEx64.dll                       |                                         |
|             |                                               |                                         |
|             | Envitia.MapLink.NativeHelpers.dll             |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| OpenGL      | Envitia.MapLink.OpenGLSurface64.dll           | Envitia.MapLink.OpenGLSurface           |
| Drawing     |                                               |                                         |
| Surface SDK |                                               |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| OpenGL      | Envitia.MapLink.OpenGLTrackHelper64.dll       |                                         |
| Track       |                                               |                                         |
| Helper SDK  |                                               |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| Direct      | Envitia.MapLink.DirectImport64.dll            | Envitia.MapLink.DirectImport            |
| Import SDK  |                                               |                                         |
|             | ttldirectimport.net64.dll                     |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| Interaction | Envitia.MapLink.InteractionModes64.dll        | Envitia.MapLink.InteractionModes        |
| Modes SDK   |                                               |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| Dynamic     | Envitia.MapLink.DDO64.dll                     | Envitia.MapLink.DDO                     |
| Data Object |                                               |                                         |
| SDK         |                                               |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| Editor SDK  | Envitia.MapLink.Editor64.dll                  | Envitia.MapLink.Editor                  |
+-------------+-----------------------------------------------+-----------------------------------------+
| Spatial     | Envitia.MapLink.Spatial64.dll                 | Envitia.MapLink.Spatial                 |
| Editor SDK  |                                               |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| Terrain SDK | Envitia.MapLink.Terrain64.dll                 | Envitia.Maplink.Terrain                 |
+-------------+-----------------------------------------------+-----------------------------------------+
| GeoPackage  | Envitia.MapLink.GeoPackage64.dll              | Envitia.MapLink.GeoPackage              |
| SDK         |                                               |                                         |
|             | ttlgeopackage.net64.dll                       |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| 3D SDK      | Envitia.MapLink.ML3D64.dll                    | Envitia.MapLink.ML3D                    |
+-------------+-----------------------------------------------+-----------------------------------------+
| 3D          | Envitia.MapLink.InteractionModes.ML3D64.dll   | Envitia.MapLink.InteractionModes.ML3D   |
| Interaction |                                               |                                         |
| Modes SDK   |                                               |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| OGC         | Envitia.MapLink.OGCServices64.dll             | Envitia.MapLink.OGCServices             |
| Services    |                                               |                                         |
| SDK         |                                               |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| Rendering   | Envitia.MapLink.RenderingAttributePanel64.dll | Envitia.MapLink.RenderingAttributePanel |
| Attribute   |                                               |                                         |
| Panel       | ttlrenderingattributepanel.net64.dll          |                                         |
+-------------+-----------------------------------------------+-----------------------------------------+
| S52/S63     | Envitia.MapLink.S5264.dll                     | Envitia.MapLink.S52                     |
| SDKs        |                                               |                                         |
|             | Envitia.MapLink.S6364.dll                     | Envitia.MapLink.S63                     |
+-------------+-----------------------------------------------+-----------------------------------------+

All other libraries are dependent on the Core SDK wrappers,
Envitia.MapLink, while the Spatial Editor wrappers are also dependent on
the Editor wrappers.

This is discussed further in the deployment guide, but it should be
noted that these libraries are all wrappers around the C++ versions and
therefore require the C++ libraries at runtime. This also means that the
.NET wrappers will not work with the current versions of Mono, the .NET
port to non-Windows operating systems.

The .NET version of the Spatial Editor SDK is the only SDK that does not
offer all the functionality of its C++ counterpart. Several helper
classes dealing with Islands have been omitted from this release. Later
versions of MapLink may add this additional functionality.

## C# Walkthrough 1 - Your First C# MapLink Application

Please note that the Wizards are not available for Visual Studio 2015,
see section [3.2](#maplink-pro-visual-studio-wizards).

This section guides you through constructing a simple MapLink
application from the skeleton application generated by the Visual Studio
Application Wizard. The steps below assume that you are using Visual
Studio 2010 SP1, but similar steps apply when using Visual Studio 2003,
2005 and 2008. By the end, you should have an application that can load
and display a map generated from MapLink Studio and can correctly handle
paint and resize events.

It is assumes that you are familiar with both C# and the earlier C++
walk through application.

### Skeleton Application

The starting point for this is a C# 'Windows Forms Application'
Application Wizard generated executable. These instructions assume that
the .NET Framework 4 is targeted.

Use the standard C# 'Windows Forms Application' Application Wizard to
generate your skeleton application. The example application here is
called "Hello Globe".

### Configure Project Properties

Once created, build your skeleton application to ensure it compiles and
links. You then need to import the appropriate MapLink .NET libraries
into the project references. The MapLink installer does not integrate
these .NET assemblies into the Visual Studio standard list of assemblies
so you will need to browse to your installations bin directory, E.G.

> C:\\Program Files\\Envitia\\MapLink Pro\\X.Y\\bin64

Where X.Y is the version of MapLink you are using.

For the purposes of this walk through we will only import the Core
MapLink .NET assembly Envitia.MapLink64.dll

**NOTE:** If you look at any of the projects for the C# samples that
ship with MapLink you\'ll find that the MapLink .NET assemblies don\'t
appear under the \"References\" node of the Solution Explorer. This is
because the Visual Studio GUI doesn\'t support the x86 build
configurations using one assembly and the x64 configuration using
another. The underlying build system that Visual Studio uses, MSBuild,
doesn\'t have such as limitation so they\'re included in the project but
just don\'t appear in the GUI.

### Initialisation and Clean Up

The first thing you'll need to do is add namespace declarations to the
project's main form for all the newly added MapLink assemblies. This
will mean that subsequent references to MapLink classes won't need to be
prefixed with the namespaces that contain them. The namespaces for each
of the MapLink assemblies are listed in section
[25.1](#library-usage-and-configuration-12), e.g.

> using Envitia.MapLink;

The configuration files for MapLink are usually only loaded once per
execution run using static methods of TSLNDrawingSurface. In a C#
application this can be done in a number of places, but the easiest is
in the main form's constructor. The simplest way to go about this is to
tell MapLink to load all standard configuration files from a particular
directory. If no directory is specified, then MapLink will assume that a
full MapLink installation has taken place and will attempt to load from
there.

In the method constructor of the applications main form add a call to
TSLNDrawingSurface::loadStandardConfig. This should be done before the
call to InitializeComponent in case MapLink classes are constructed
during this call.

You should be careful to check for, and report errors at this stage by
using the methods supplied on the TSLNErrorStack utility class.

> public Form1()
>
> {
>
> TSLNErrorStack.clear() ;
>
> String configDirPath = null; //Replace if deployed
>
> TSLNDrawingSurface.loadStandardConfig(configDirPath);
>
> String msg =
>
> TSLNErrorStack.errorString(\"Initialisation errors :\\n\",
>
> TSLNErrorCategory.TSLNErrorCategoryError \|
>
> TSLNErrorCategory.TSLNErrorCategoryFatal) ;
>
> if ( msg != null )
>
> {
>
> MessageBox.Show(this, msg) ;
>
> Environment.Exit(-1);
>
> }
>
> InitializeComponent();

}

When your application is deployed, make configDirPath variable point to
the location of your applications copy of the MapLink config directory.

Once MapLink has been initialised, it needs to be cleaned up when the
application exits, otherwise Visual Studio will report numerous "leaks"
which are in fact memory currently in use when the application exits.
This should be done in the Dispose method of the main form. This Dispose
method is usually provided for you in the form designer but can be added
via the class wizard if missing.

The tidy up of MapLink should occur after the form's components have
been disposed of but before the form itself is disposed of.

> protected override void Dispose(bool disposing)
>
> {
>
> if (disposing && (components != null))
>
> {
>
> components.Dispose();
>
> }
>
> TSLNDrawingSurface.cleanup();
>
> base.Dispose(disposing);
>
> }

### The Drawing Surface and Map Data Layer

First of all we'll add some UI features to the main form to allow users
to load a map:

- Add a Menu Strip to the form (Drag from the toolbox to the top of the
  form in designer mode)

- Add a 'File' menu group.

- Add an 'Open' and 'Exit' menu items to the File menu group. Add an
  event handler for each of the operations. (Click on the buttons to
  achieve this)

- Add an OpenFileDialog object to the main form. (Drag the icon from the
  toolbox to anywhere on the form). Set the filter in the properties
  window to:

> MapLink Maps\|\*.map;\*.mpc\|All files\|\*.\*

Also set the title and any other settings if required.

Next we'll declare the variables required and setup the drawing surface:

- Before the constructor in the main form's main class, declare private
  instances of both the TSLNDrawingSurface and TSLNMapDataLayer class
  and initialise them to null.

- Add an event handler for the main form's 'Load' event. This can be
  achieved via the properties window when the form is viewed from the
  designer by clicking on the events (the lightning icon) button at the
  top. When viewing the form events, find the Load event and type a
  method name next to it, or double click for the default method name to
  be used.

- In the load event handler construct the TSLNDrawingSurface, passing in
  the form's 'Handle' member variable and the second argument as false
  to indicate that the handle is a window handle. For example:

> m_drawingSurface = new TSLNDrawingSurface(this.Handle, false);

Finally we'll hook up the menu event handlers to allow the map to load
and the program to exit.

- In the File Open event handler call your instance of the
  FileOpenDialog's ShowDialog method. Capture the return value and
  return from the method if it's anything but DialogResult.OK.

- Construct your instance of the TSLNMapDataLayer class and call its
  loadData method using the filename retrieved from the user.

- Check the return value of the loadData call and if it fails check the
  error stack for the reason.

- Finally add the new data load to your instance of TSLNDrawingSurface
  via the addDataLayer method, assigning it a unique name.

For example:

> private void openToolStripMenuItem_Click(object sender, EventArgs e)
>
> {
>
> if (openFileDialog1.ShowDialog() != DialogResult.OK)
>
> return;
>
> m_mapDataLayer = new TSLNMapDataLayer();
>
> if (!m_mapDataLayer.loadData(openFileDialog1.FileName))
>
> {
>
> String error = TSLNErrorStack.errorString(\"Errors:\",
>
> TSLNErrorCategory.TSLNErrorCategoryAll);
>
> m_mapDataLayer = null;
>
> if (error != null)
>
> {
>
> MessageBox.Show(this, \"Error\", error, MessageBoxButtons.OK);
>
> return;
>
> }
>
> }
>
> m_drawingSurface.addDataLayer(m_mapDataLayer, \"map\");
>
> m_drawingSurface.reset(true);
>
> }

- Lastly when the File Exit menu button is clicked call the form's Close
  method.

At this point it would be advisable to compile the project to check if
any coding errors have occurred so far. Although the program should run,
you'll find that it won't do very much as we haven't told MapLink when
it needs to draw yet!

### Handling Paint and Resize Events

Since MapLink is passive, the application needs to handle relevant
events and pass the information onto MapLink. Most applications will
only need to handle the window paint and resize events.

A paint event can be triggered for many reasons, some of which will only
want to redraw part of the window. Under these circumstances, Windows
will set up a Clip Box to define the part that needs redrawing. To
improve performance, it is best to only redraw that part. It is most
efficient to pass the required Device Unit extent to the Drawing
Surface.

After handling a resize event, Windows will usually post a paint message
so there is no need to force a redraw in the resize handler. Just
changing the window size may distort the aspect ratio of the display, so
MapLink can automatically adjust the visible map area to be in sympathy
with the aspect ratio of the window. This optional behaviour allows an
anchor point to be specified, which is kept at the same place when
updating the visible map area.

To add Paint and Resize event handlers to your form, the steps are the
same as outlined for adding a Load event handler detailed earlier in
this walkthrough.

In the Paint event handler, first check that the drawing surface has
been constructed and if so request a redraw via the drawDU method, e.g.

> private void OnPaint(object sender, PaintEventArgs e)
>
> {
>
> if ( m_drawingSurface == null )
>
> return;
>
> m_drawingSurface.drawDU(e.ClipRectangle.Left, e.ClipRectangle.Top,
>
> e.ClipRectangle.Right,
>
> e.ClipRectangle.Bottom,true);

}

In the Resize event hander, once again first check that the drawing
surface has been constructed and if so, request a resize via the
wndResize method. The second to last argument is whether a redraw should
occur, which is required as .NET will only redraw if the control gets
larger. The final argument to the wndResize method dictates how the
existing view should relate to the new view, e.g.

> private void OnResize(object sender, EventArgs e)
>
> {
>
> if (m_drawingSurface == null)
>
> return;
>
> m_drawingSurface.wndResize(ClientRectangle.Left,
>
> ClientRectangle.Top,
>
> ClientRectangle.Right,
>
> ClientRectangle.Bottom,
>
> true,
>
> TSLNResizeActionEnum.TSLNResizeActionMaintainCentre);
>
> }

Finally, we need to handle the initial resize of the main window. For
some reason a Resize event is not sent by the .NET framework when the
form is initially sized. So we'll have to tell the drawing surface its
initial size. Simple copy the wndResize statement into your Load event
handler after the drawing surface has been constructed.

Now build the program, run it and load one of the sample maps.

### Further tweaks to your first MapLink C# application

One of the problems with the setup used in the walkthrough is that the
menu strip at the top of the application actually hides some of the map
area. You'll notice this affect if you load a map as the area of white
space at the bottom won't match the amount at the top. In the sample C#
applications supplied with MapLink we get around this issue by moving
the drawing surface into a panel within the main form's client area. The
same effect could, however, be achieved by sizing the drawing surface
using the menu strip's bottom coordinates.

To add double buffering to the form in C#, users will need to override
the form/panel's OnPaintBackground and not call the base implementation.
This will be in addition to calling setOption on the drawing surface as
described in section
[8.10](#reducing-flicker-and-improving-performance), e.g.

> protected override void OnPaintBackground( PaintEventArgs pevent)
>
> {
>
> // do nothing\...
>
> // we don\'t want the background to flash over the map
>
> }

NOTE: Override the OnPaintBackground method can cause havoc when viewing
the UI object via the Visual Studio designer. For an example of how to
work around this problem refer to the sample C# programs supplied with
MapLink that utilise the ControlDesigner class.

## VB Walkthrough 1 - Your First VB MapLink Application

Please note that the Wizards are not available for Visual Studio 2015,
see section [3.2](#maplink-pro-visual-studio-wizards).

This section guides you through constructing a simple MapLink
application from the skeleton application generated by the Visual Studio
Application Wizard. The steps below assume that you are using Visual
Studio 2010 SP1, but similar steps apply when using Visual Studio 2003,
2005 and 2008. By the end, you should have an application that can load
and display a map generated from MapLink Studio and can correctly handle
paint and resize events.

It assumes that you are familiar with both VB and the earlier C++ walk
through application.

### Skeleton Application

The starting point for this is a VB 'Windows Forms Application'
Application Wizard generated executable. These instructions assume that
the .NET Framework 4 is targeted, although there will be instructions
along the way for targeting Framework 2.

Use the standard VB 'Windows Application' Application Wizard to generate
your skeleton application. The example application here is called "Hello
Globe".

### Configure Project Properties

Once created, build your skeleton application to ensure it compiles and
links. You then need to import the appropriate MapLink .NET libraries
into the project references. The MapLink installer does not integrate
these .NET assemblies into the Visual Studio standard list of assemblies
so you will need to browse to your installations bin directory, E.G.

C:\\Program Files\\Envitia\\MapLink Pro\\X.Y\\bin64

Where X.Y is the version of MapLink you are using.

For the purposes of this walk through we will only import the Core
MapLink .NET assembly Envitia.MapLink64.dll

**NOTE:** If you look at any of the projects for the C# samples that
ship with MapLink you\'ll find that the MapLink .NET assemblies don\'t
appear under the \"References\" node of the Solution Explorer. This is
because the Visual Studio GUI doesn\'t support the x86 build
configurations using one assembly and the x64 configuration using
another. The underlying build system that Visual Studio uses, MSBuild,
doesn\'t have such as limitation so they\'re included in the project but
just don\'t appear in the GUI.

### Initialisation and Clean Up

The first thing you'll need to do is import the namespaces to the
project for all the newly added MapLink assemblies. This will mean that
subsequent references to MapLink classes won't need to be prefixed with
the namespaces that contain them. The namespaces for each of the MapLink
assemblies are listed in section
[25.1](#library-usage-and-configuration-12).

To import a namespace, navigate to the references tab of the project
properties. At the bottom of the page is a list of all the globally
imported namespaces.

The configuration files for MapLink are usually only loaded once per
execution run using static methods of TSLNDrawingSurface. In a VB
application this can be done in several places, but the easiest is in
the main form's constructor. The simplest way to go about this is to
tell MapLink to load all standard configuration files from a particular
directory. If no directory is specified, then MapLink will assume that a
full MapLink installation has taken place and will attempt to load from
there.

Add a constructor to the application's main form and add a call to
TSLNDrawingSurface::loadStandardConfig. This should be done before the
call to InitializeComponent in case MapLink classes are constructed
during this call.

You should be careful to check for, and report errors at this stage by
using the methods supplied on the TSLNErrorStack utility class.

> Public Sub New()
>
> TSLNErrorStack.clear()
>
> Dim configDirPath As String = Nothing \'Replace if deployed
>
> TSLNDrawingSurface.loadStandardConfig(configDirPath)
>
> Dim msg As String = TSLNErrorStack.errorString(

\"Initialisation Errors : \\n\",

> TSLNErrorCategory.TSLNErrorCategoryError Or
>
> TSLNErrorCategory.TSLNErrorCategoryFatal)
>
> If (Not msg Is Nothing) Then
>
> MessageBox.Show(Me, msg)
>
> Environment.Exit(-1)
>
> End If
>
> \' This call is required by the Windows Form Designer.
>
> InitializeComponent()

End Sub

When your application is deployed, make configDirPath variable point to
the location of your applications copy of the MapLink config directory.

Once MapLink has been initialised, it needs to be cleaned up when the
application exits, otherwise Visual Studio will report numerous "leaks"
which are in fact memory currently in use when the application exits.
This should be done in the Dispose method of the main form.

> The tidy up of MapLink should occur after the form's components have
> been disposed of but before the form itself is disposed of.
>
> Protected Overrides Sub Dispose(ByVal disposing As Boolean)
>
> Try
>
> If disposing AndAlso components IsNot Nothing Then
>
> components.Dispose()
>
> End If
>
> Finally
>
> TSLNDrawingSurface.cleanup() 'MapLink Code
>
> MyBase.Dispose(disposing)
>
> End Try
>
> End Sub

### The Drawing Surface and Map Data Layer

First of all, we'll add some UI features to the main form to allow users
to load a map:

- Add a Menu Strip to the form (Drag from the toolbox to the top of the
  form in designer mode)

- Add a 'File' menu group.

- Add an 'Open' and 'Exit' menu items to the File menu group. Add an
  event handler for each of the operations. (Click on the buttons to
  achieve this)

- Add an OpenFileDialog object to the main form. (Drag the icon from the
  toolbox to anywhere on the form). Set the filter in the properties
  window to:

> MapLink Maps\|\*.map;\*.mpc\|All files\|\*.\*

Also set the title and any other settings if required.

Next we'll declare the variables required and setup the drawing surface:

- Before the constructor in the main form's main class, declare private
  instances of both the TSLNDrawingSurface and TSLNMapDataLayer class
  and initialise them to null.

- Add an event handler for the main form's 'Load' event. This can be
  achieved via the properties window when the form is viewed from the
  designer by clicking on the events (the lightning icon) buttons at the
  top. When viewing the form events, find the Load event and type a
  method name next to it, or double click for the default method name to
  be used.

- In the load event handler construct the TSLNDrawingSurface passing in
  the form's 'Handle' member variable and the second argument as false
  to indicate that the handle is a window handle. For example:

> m_drawingSurface = New TSLNDrawingSurface(Me.Handle, False)

Finally, we'll hook up the menu event handlers to allow the map to load
and the program to exit.

- In the File Open event handler call you instance of the
  FileOpenDialog's ShowDialog method. Capture the return value and
  return from the method if it anything but DialogResult.OK.

- Construct your instance of the TSLNMapDataLayer class and call its
  loadData method using the filename retrieved from the user.

- Check the return value of the loadData call and if it fails check the
  error stack for the reason.

- Finally add the new data load to your instance of TSLNDrawingSurface
  via the addDataLayer method, assigning it a unique name.

For example:

> Private Sub OpenToolStripMenuItem_Click(\...
>
> If (OpenFileDialog1.ShowDialog() \<\> DialogResult.OK) Then
>
> Return
>
> End If
>
> m_mapDataLayer = New TSLNMapDataLayer()
>
> If (Not m_mapDataLayer.loadData(OpenFileDialog1.FileName)) Then
>
> Dim errorStr As String = TSLNErrorStack.errorString(\"Errors:\",
>
> TSLNErrorCategory.TSLNErrorCategoryAll)
>
> m_mapDataLayer = Nothing
>
> If (Not errorStr Is Nothing) Then
>
> MessageBox.Show(Me, \"Error\", errorStr, MessageBoxButtons.OK)
>
> Return
>
> End If
>
> End If
>
> m_drawingSurface.addDataLayer(m_mapDataLayer, \"map\")
>
> m_drawingSurface.reset(True)
>
> End Sub

- Lastly when the File Exit menu button is clicked call the form's Close
  method.

At this point it would be advisable to compile the project to check if
any coding errors have occurred so far. Although the program should run,
you'll find that it won't do very much as we haven't told MapLink when
it needs to draw yet!

### Handling Paint and Resize Events

Since MapLink is passive, the application needs to handle relevant
events and pass the information onto MapLink. Most applications will
only need to handle the window paint and resize events.

A paint event can be triggered for many reasons, some of which will only
want to redraw part of the window. Under these circumstances, Windows
will set up a Clip Box to define the part that needs redrawing. To
improve performance, it is best to only redraw that part. It is most
efficient to pass the required Device Unit extent to the Drawing
Surface.

After handling a resize event, Windows will usually post a paint message
so there is no need to force a redraw in the resize handler. Just
changing the window size may distort the aspect ratio of the display, so
MapLink can automatically adjust the visible map area to be in sympathy
with the aspect ratio of the window. This optional behaviour allows an
anchor point to be specified, which is kept at the same place when
updating the visible map area.

To add Paint and Resize event handlers to your form, the steps are the
same as outlined for adding a Load event handler detailed earlier in
this walkthrough.

To the Paint event handler, first check that the drawing surface has
been constructed and if so, request a redraw via the drawDU method,
e.g.:

> Private Sub Form1_Paint(\...
>
> If (m_drawingSurface Is Nothing) Then
>
> Return
>
> End If
>
> m_drawingSurface.drawDU(e.ClipRectangle.Left,
>
> e.ClipRectangle.Top,
>
> e.ClipRectangle.Right,
>
> e.ClipRectangle.Bottom,
>
> **True**)
>
> End Sub

To the Resize event hander, once again first check that the drawing
surface has been constructed and if so, request a resize via the
wndResize method. The second to last argument is whether a redraw should
occur, which is required as .NET will only redraw if the control gets
larger. The final argument to the wndResize method dictates how the
existing view should relate to the new view, e.g.:

> Private Sub Form1_Resize(\...
>
> If (m_drawingSurface Is Nothing) Then
>
> Return
>
> End If
>
> m_drawingSurface.wndResize(ClientRectangle.Left,
>
> ClientRectangle.Top,
>
> ClientRectangle.Right,
>
> ClientRectangle.Bottom,
>
> True,

TSLNResizeActionEnum.TSLNResizeActionMaintainCentre)

> End Sub

Finally, we need to handle the initial resize of the main window. For
some reason a Resize event is not sent by the .NET framework when the
form is initially sized. So we'll have to tell the drawing surface its
initial size. Simple copy the wndResize statement into your Load event
handler after the drawing surface has been constructed.

Now build the program, run it and load one of the sample maps.

### Further tweaks to your first MapLink VB application

One of the problems with the setup used in the walkthrough is that the
menu strip at the top of the application hides some of the map area.
You'll notice this affect if you load a map as the area of white space
at the bottom won't match the amount at the top. In the sample C#
applications supplied with MapLink we get around this issue by moving
the drawing surface into a panel within the main form's client area. The
same effect could, however, be achieved by sizing the drawing surface
using the menu strip's bottom coordinates.

To add double buffering to the form in VB, users will need to override
the form/panel's OnPaintBackground and not call the base implementation.
This will be in addition to calling setOption on the drawing surface as
described in section
[8.10](#reducing-flicker-and-improving-performance), e.g.:

Protected Overrides Sub OnPaintBackground(ByVal pevent As
PaintEventArgs)

\' do nothing\...

\' we don\'t want the background to flash over the map

End Sub

NOTE: Override the OnPaintBackground method can cause havoc when viewing
the UI object via the Visual Studio designer. For an example of how to
work around this problem refer to the sample C# programs supplied with
MapLink that utilise the ControlDesigner class.



---

[← GML SDK](gml-sdk) | [MapLink Camera Manager →](camera-manager)
