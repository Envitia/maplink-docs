---
title: "DIGM to TMF Conversion"
---

# DIGM to TMF Conversion


There are 4 stages to performing DIGM to TMF conversion using
TSLDIGMConverter.  This class is defined in the 'LandLinkDIGMConv.h'
file.

## Rendering Attribute version setup

MapLink and GMS/DIGM handle rendering attributes differently and a
mapping needs to be configured for colours and styles.

Set the colour index to map GMS colour 0 (typically white) to the
specified MapLink colour index. If no mapping is set, the index is
mapped to 1, since MapLink index 0 is no-colour.

> void setColour0Index( int index );

GMS handles hollow fill using FINTER attribute of 0.  MapLink uses a
specific fillstyle. Default is 0.

> void setFinter0Mapping( long index );

GMS handles solid fill using FINTER attribute of 1.  MapLink uses a
specific fillstyle. Default is 0.

> void setFinter1Mapping( long in );

GMS handles patterned fill using FINTER attribute of 2 or 3.  MapLink
uses a specific fillstyle.

MapLink does not support FINTER 2 and it is mapped internally to FINTER
4.

If no mapping is specified, then the fill style is used unchanged.

> void addFillMapping(long gmsFStyle, long tmsFillStyle);

Add a mapping between symbols with specified style index and stamps
(model instances) of the given name - if a model instance of
'stampName' is found, this is mapped to a TSLSymbol of the specified
index. If no mapping exists, the model instance is silently ignored.

> void addStampMapping( long index, const char \*stampName );

Add a mapping between GMS text font (precision/font pair) to MapLink
font style. If no mapping is specified, then the font style is used
unchanged.

> bool addFontMapping(long gmsPrecision, long gmsFont, long maplinkFont
> );

A typical setup for the Capture Tool is

> TSLDIGMConverter converter;
>
> converter.setColour0Index( 46 );
>
> converter.setFinter0Mapping(8);
>
> converter.setFinter1Mapping(1);
>
> converter.addFillMapping(4,2);
>
> converter.addFillMapping(7,14);

 

## Complex polygon handling

By default, MapLink will attempt to decomplexify complex polygons
automatically and silently - simplify self-intersections and remove
spikes.  Arrows are handled specially to avoid removal of spikes.  If
any decomplexification fails, then an error may be placed on the error
stack.  See \<MapLink\>\\config\\tsllandlinkdigmconverrors.msg and
tsltgmerrors.msg for a list of errors that are relevant.  Note that some
of these error messages are historical and may never be generated and
some are warnings. 

If decomplexification fails, then MapLink attempts to create an invalid,
complex polygon, but sets the feature code to a specific value and can
optionally change the rendering attributes.  Such polygons should not be
used for spatial operations, nor edited.

Set feature code for failed complex polygons.  Default is 9999.

> void setComplexPolygonFeatureCode(long featureCode );

The modify flag is used to indicate whether to modify the attributes of
failed complex polygons, and if so, what to.  The default is false.

> void modifyAttributesOnComplexPolygons(bool modify );
>
> void complexPolygonAttributes(long fillColour, long fillStyle, long
> edgeColour, long edgeStyle, long edgeThickness );

## Coordinate System setup

DIGM stores coordinates is a scaled offset form of the base GMS units. 
The following two methods are used to specify the conversion between the
MapLink coordinate space and DIGM and GMS units.

> void setupDIGMtoTMCConversion( double scale,
>
> double xOffset, double yOffset);
>
> void setupDIGMtoGMSConversion( double scale,
>
> double xOffset, double yOffset);

A typical setup for the Capture Tool is as follows.  Different units may
be required for Orkney/Shetland - see application code.

> converter.setupDIGMtoTMCConversion(10,0,0);
>
> converter.setupDIGMtoGMSConversion(.001,-29000,-66400);

## Perform import conversion

The following function converts the specified DIGM buffer, of specified
size to a TMF entity set. 

> bool import (TSLEntitySet \*entitySet,
>
> const unsigned char \*buffer, long size );

If the ingest fails for any reason, the function will return
false. Additional information about the failure may be found by querying
the error stack.

The DIGM buffer must contain data as it would be written to disk by
GSQL/DIGM, not as a database unload of the BLOB. Thus, it needs to be of
the following form, taking note of lack of backslashes at end of line
and lack of NULL character at the end of file:

> VS 1
>
> DE 1
>
> XO 28849577.500 64349504.800
>
> TC 7
>
> BC 0
>
> PA 1
>
> PR 1
>
> TS 1 1
>
> AL 1 4
>
> HT 0.200000
>
> TE \"Text1\" 592.400 566.500

.XM -0.013134332831462611 -0.99991374093022267 0 0.99991374093022267
-0.013134332831462611 0

.MV -2051127.3934587948 123459.22996837646 1

###### 

###### Developers Guide UNIX/Linux/VxWorks (X11)

MapLink has been ported to a variety of operating systems (OS), the
common denominator being that X11 is available for those operating
systems.

Limitations which are specific to a particular OS and compiler
configuration can be found in the X11 Release Notes.

The principles outlined in the 'Developers Guide for MapLink' are
applicable for use with MapLink on an X11 platform. This section covers
the differences between Windows and X11 runtime programming.

###### Programming for X11

###### TSLMotifSurface

The primary programming difference between Windows and X11 is the
Drawing Surface class that you use. For X11 you will use:
TSLMotifSurface (should really have been called X11DrawingSurface).

There are two constructors for this class:

- TSLMotifSurface (Display\* display, Screen\* screen, Colormap
  colormap, Drawable handle, int flags = 0, Visual\* visual = 0);

- TSLMotifSurface (Display\* display, Drawable handle, int flags = 0);

Ideally you should pass as much information to MapLink as possible. This
is particularly important when using raster maps, as the actual Visual
is required so that the correct raster drawing routines can be used.

TSLMotifSurface is a simple class, which provides several additional X11
specific methods, which also have similar methods on the TSLNTSurface as
follows:

- int colourValue (int index);

- bool fillStyleValue (int index, int colour, Pixmap pixmap,
  TSLSimpleString \*section = 0);

- bool fontStyleValue (int index, int colour, Pixmap pixmap, const
  char\*\* fontName = 0, const char \*outputString = 0, TSLSimpleString
  \*section = 0);

- bool lineStyleValue (int index, int colour, int thickness, Pixmap
  pixmap, TSLSimpleString \*section = 0);

- bool symbolStyleValue (int index, int colour, Pixmap pixmap, uint32_t
  fontSymbolCharacter = 0, TSLRasterSymbolScalable
  rasterSymbolScalability = TSLRasterSymbolScalableAsSymbolFile,
  TSLSimpleString \*section = 0);

- bool drawToDrawable (Drawable drawable, double x1, double y1, double
  x2, double y2, bool clear);

- bool attach (Drawable handle, bool isPixmap, Display\* display = 0,
  Screen\* screen = 0, Colormap colormap = -1, Visual\* visual = 0);

- bool fullDetach ();

All the above methods are specific to X11 (not all the default
parameters are shown).

When creating an application for X11, regardless of GUI toolkit, the
principles behind the 'Walkthrough 1 - Your First MapLink Application'
are just as valid. Some samples are included with the CD to help you.

###### Actions on close of Display

You should call TSLDrawingSurface::cleanup() before you close the
Display.

###### Using GUI Toolkits with MapLink

MapLink does not depend on any particular GUI toolkit to work. MapLink
relies only on Xlib.

It is therefore possible to use MapLink with any number of GUI toolkits,
such as Motif, FOX (http://www.fox-toolkit.org/) or Qt
(http://www.trolltech.com).

We now ship samples for Qt 4.7 and Qt 5.15.

###### Using Qt4.X

If you have difficulty integrating MapLink with Qt please contact
support.

Add a method to the Custom Widget as follows:

> virtual QPaintEngine \*paintEngine() const
>
> {
>
> return 0;
>
> }

This stops Qt drawing into the Widget itself.

In the Custom Widget constructor add the following:

> // This is required for Qt4 to stop the back ground being drawn
>
> // and Qt Double buffering. You also need to override
>
> // paintEngine().
>
> //
>
> // Ref:
>
> // <http://lists.trolltech.com/qt-interest/2006-02/thread00004-0.html>
>
> //
>
> setAttribute( Qt::WA_NoBackground, true);
>
> setAttribute( Qt::WA_NoSystemBackground, true);
>
> // Possible issue with this for Qt4.1.0 and newer versions.
>
> //
>
> // See:
>
> //
> <http://www.trolltech.com/developer/task-tracker/index_html?id=106922&method=entry>
>
> // <http://lists.trolltech.com/qt-interest/2006-05/thread00316-0.html>
>
> //
>
> // Talk to Trolltech support about getting a fix if this proves to
>
> // be a problem
>
> //
>
> // NOTE: I am not seeing this problem, probably because I\'m doing
>
> // things slightly differently from the example.
>
> setAttribute( Qt::WA_PaintOnScreen, true);
>
> setAutoFillBackground(false); //should be true for Qt4.1 and 4.0

For Qt4.1 and newer you will need to add the following:

> setAttribute(Qt::WA_OpaquePaintEvent);

When you construct the MapLink Drawing Surface use the winId or handle
method as follows:

> // Attaching to the window is much more efficent.

#ifdef WINNT

> HWND hWnd = (HWND) winId();
>
> m_drawingSurface = new TSLNTSurface( hWnd, false );

#else

QX11Info x11info = this-\>x11Info();

Display \*display = x11info.display();

int screenNum = x11info.screen();

Visual \*visual = (Visual \*)x11info.visual();

Qt::HANDLE colourmap = x11info.colormap();

Qt::HANDLE drawable = handle();

Screen \*screen = ScreenOfDisplay(display, screenNum);

m_drawingSurface = new TSLMotifSurface( display, screen, colourmap,

drawable, 0, visual);

#endif

The paintEvent in the Custom Widget should look something like this:

> void MapLinkWidget::paintEvent ( QPaintEvent \*rect )
>
> {
>
> if (m_drawingSurface == NULL)
>
> create();
>
> if (m_initialUpdate)
>
> resizeCanvas();
>
> const QRect &r = rect-\>rect();
>
> long x1 = r.x() ;
>
> long y2 = r.y() ;
>
> long x2 = r.x() + r.width() ;
>
> long y1 = r.y() + r.height() ;
>
> m_drawingSurface-\>drawDU( x1, y1, x2, y2, true, true ) ;
>
> }

###### Using Qt 5.1 or later

Add a method to the Custom Widget as follows:

> virtual QPaintEngine \*paintEngine() const
>
> {
>
> return NULL;
>
> }

This stops Qt drawing into the Widget itself.

In the Custom Widget constructor add the following:

setAttribute( Qt::WA_OpaquePaintEvent );

setAttribute( Qt::WA_PaintOnScreen );

setAttribute( Qt::WA_NativeWindow );

setAutoFillBackground( false );

When you construct the MapLink Drawing Surface use the winId method as
follows:

#ifdef WIN32

m_surface = new TSLNTSurface( (HWND)winId(), false );

#elif QT_VERSION \>= 0x50100

// Qt 5.1 or newer

Display \*display = QX11Info::display();

WId wid = winId();

XWindowAttributes attribs;

XGetWindowAttributes( display, wid, &attribs );

m_surface = new TSLMotifSurface( display, attribs.screen,
attribs.colormap, wid, 0,

attribs.visual );

#else

// Qt 5.0 does not provide easy an easy way of accessing the X11 display
or drawable

// for the widget. It is recommended that you upgrade to Qt 5.1 or
later.

#endif

###### Drawing on top of MapLink using Qt

In order to use Qt to draw on top of MapLink rendering, you will need to
draw the map data into a QtPixmap and blit the QtPixmap to the screen.
The code to disable the Qt double buffering and background clearing is
probably no-longer required depending on what you are trying to achieve.

###### Text Drawing

The X11 drawing code now uses Pango to draw text so that we can support
Unicode. On most platforms Pango uses Xft and hence XRender.

On 'Solaris 10 x86' we have had to use the latest Xft because the one
shipped is too old to work effectively with XRender. The version of
Pango we are using is the latest one that we were able to compile using
the development environment available on the platform.

On 'Solaris 10 SPARC' the version of Pango we are using is the latest
one that we were able to compile using the development environment
available on the platform.

###### Dynamic Data Object SDK

Dynamic Data Object (DDO) SDK allows developers to create fully dynamic
overlays within a MapLink application (see Developers Guide).

When you create a TSLDisplayObject derived class you have two options
when implementing the draw method.

1.  Make a sequence of calls to the Rendering Interface to set up
    attributes and draw graphical primitives (portable).

2.  Draw using X11 drawing methods (non-portable, optimal).

> Obtaining the Display and Drawable can be achieved as follows:
>
> bool AircraftDO::draw(TSLRenderingInterface \*d_surface,
>
> TSLEnvelope \*d_extent )
>
> {
>
> long ldisplay;
>
> Drawable drawable = (Drawable)
>
> (d_surface-\>handleToDrawable( &ldisplay ));
>
> Display\* display = (Display\*)ldisplay;
>
> // ......
>
> }

The TSLRenderingInterface also provides access to the Visual, Colormap
and Screen. This will make it easier to create pixmaps and images in a
custom data layer or via a DDO.

###### Raster support

All MapLink X11 targets support the display of Raster Maps locally or
remotely. The X-Server depth to use (via the Visual) will be dependent
on the X-Server and the applications use of colour.

The X11 MapLink runtime supports TIFF, PNG and JPEG formats generated by
MapLink Studio (not all combinations of these formats are supported).

Raster datasets from MapLink Studio may be configured to output at a
particular bit-depth and for 8-bit images, the number of colours used by
the image may be specified. Note: that the default is 24-bit (Please
refer to the MapLink Studio help).

Rasters which contain an alpha channel will only be displayed correctly
when using X servers that support XRender 0.6 or later.

###### Holed Polygons

Vector Maps can be generated from MapLink Studio with holed polygons or
without holes by using key-holing.

Using key-holing means that the drawing of holed polygons is a lot less
complex and more efficient. Therefore, this is the recommended approach
on X11 for performance reasons alone.

The only reason for not using this approach is if a polygon edge line
style is required to be displayed as this will show the keyhole
construction.

Note: VxWorks target Envitia uses for testing does not support drawing
of holed polygons.

###### APP-6A and 2525B Symbology

MapLink provides the capability to display many APP6A and 2525B symbols
through two classes (TSLAPP6AHelper & TSLAPP6ASymbol).

MapLink provides two configuration files, app6aConfig.csv and
2525bConfig.csv in the config directory of your MapLink installation.
Applications should pass the full path to one of these files depending
on which set of symbology is desired.

In addition to these configurations the alternate symbol file
'tslsymbolsAPP6A.dat' has been provided. This also includes OTHT-Gold
symbols. Any application using APP-6A or 2525B icons should load this
symbols file. It is acceptable simply to load it using 'setupSymbols'
after calling 'loadStandardConfig'. See the Windows APP-6A sample.

###### Stroked Linestyles

Stroked linestyles are implemented by an extension shared library
(ttlclsstrk.so/sl/o). The shared library is written specifically for the
target platform.

The file tsllinestyle.dat contains many stroked linestyle definitions,
an example of a stroked linestyle is shown below:

> 1000;ttlclsstrk;My Custom
> Line;MyCustomLineStyleTag;C\[(-1,-1,-1),4\]U\[0,-2\]D\[5,0\]D\[5,0\]BC\[(-1,-1,-1),2\]U\[0,1\]D\[5,0\]D\[5,0\]D\[4,0\]

The above line is broken down as follows:

> StyleID;typeOrCustomDLLName;Textual comment displayed in feature book,
> no semi-colons allowed;DLL specific information

For the ttlclsstrk.so/sl/dll (DLL) which implements this type of line,
the DLL specific information is:

> UniqueTag;CommandString

The CommandString is a chain of

> C\[(R,G,B),W\] colour and width, RGB obvious, W width (width \<= 0 is
> set to 1 pixel). If R, G and B are all -1, then colour defined by
> feature book is used.
>
> D\[x,y\] Pen down, line to (currentPositionX + x, currentPositionY +
> y)
>
> U\[x,y\] Pen up, move to (currentPositionX + x, currentPositionY + y)
>
> B Bend Point. This is where we can effectively start a new line
> segment.

Where:

Pen Down means place the drawing point on the paper and draw to the
specified position from the current position.

Pen Up means raise the drawing point off the paper and move to the
specified position from the current position.

All moves are relative to the current position.

The easiest approach when creating or modifying a Stroked Linestyle is
to use a pen and a piece of graph paper, recording exactly how you draw
the line (pen up, pen down, colour, amount moved).

So for \'D\[5,0\]U\[5,0\]D\[5,0\]\', you get the following simple line:

> '\-\-\-\-- \-\-\-\--'

Where:

> \- represents pen colour being drawn (Pen Down) as a solid line, but
> here represented as dashes to show the amount of movement of the Pen.
>
> space represents pen colour not being drawn (Pen Up)

The start point of your line is always at position \[0, 0\].

In the above simple line at the end of the sequence the current drawing
position is \[0, 15\].

So if you wanted to return to \[0, 0\], you would add \'U\[0,-15\]\' to
the line definition.

Please note the following:

- When drawing a custom linestyle Maplink uses the horizontal axis where
  y=0, as the middle of the line.

- Progress has to be made in the x-axis.

- The line thickness is specified in pixels. So a line thickness of
  three will be drawn in a similar way that Windows/X11 will draw a
  solid line of thickness 3.

- Line segments are drawn with a round end cap on Windows. On X11 line
  segments are drawn with CapButt and JoinMiter.

- You can also increase the number of \'B\'s to improve the ability of
  the customline style to follow the draw points.\
  In general \'B\' points must occur when the y-axis is at 0. If you
  make changes to a linestyle check the changes using a relatively
  complex map or drawing.

- Custom linestyles will have an impact on drawing performance. The more
  complex a linestyle the larger the impact on performance.

###### X11 Error Handlers

If you define Error handlers by calling XSetErrorHandler, then you need
to call any error handlers already defined (XSetErrorHandler returns the
previous error handler).

The Raster drawing shared library uses this error handler to detect
problems when using shared memory (XShm). The MapLink3D optional SDK
also hooks into the X error handling to figure out if it can use the
XShm extension.

You should setup the X error handlers before you call MapLink or MapLink
will call the default handlers if it does not handle the errors it-self.
MapLink will not call any error handlers if it handles the errors
itself.

It is possible to disable the setting up of the Error handlers by
setting of the environment variable TTL_GDK_SHM_OFF.

###### Vector and Raster Data Format Support

The list of data formats supported by MapLink Pro Studio or runtime SDKs
is constantly being expanded. The following sections describe some of
the formats currently supported at the time of writing.

###### Vector Datasets

<table class="doc-table">
  <tbody>
    <tr><td>> <strong>Data Format</strong> ======================== > DAFIF</td><td>> <strong>Studio > Import</strong> :==========: > ✔</td><td>> <strong>Direct > Import > SDK</strong> :==========:</td><td>> <strong>Other > Runtime > Import</strong> :==========:</td><td>> <strong>Runtime > Export</strong> :===========:</td></tr>
  </tbody>
</table>
| > DFAD                 | > ✔        |            |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> DXF</td><td>> ✔</td><td>> ✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > Envitia ASCII        | > ✔        |            |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> File Geodatabase > (FileGDB)</td><td>> ✔</td><td>> ✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > GDF3                 | > ✔        |            |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> GeoPackage</td><td>> ✔</td><td>> ✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > GML2/GML3            | > ✔        | > ✔        | > ✔        | > ✔         |
<table class="doc-table">
  <tbody>
    <tr><td>> Jeppesen</td><td>> ✔</td><td></td><td></td><td></td></tr>
  </tbody>
</table>
| > KML Simple Features  | > ✔        | > ✔        | > ✔        |             |
| > 2D                   |            |            |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> MIF/MID</td><td>> ✔</td><td>> ✔</td><td>> ✔</td><td>> ✔</td></tr>
  </tbody>
</table>
| > NITF/NSIF            | > ✔        | > ✔        | > ✔        |             |
<table class="doc-table">
  <tbody>
    <tr><td>> OpenStreetMap</td><td>> ✔</td><td>> ✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > OS MasterMap         | > ✔        | > ✔        | > ✔        | > ✔         |
<table class="doc-table">
  <tbody>
    <tr><td>> OS NTF</td><td>> ✔</td><td>> ✔</td><td>> ✔</td><td>> ✔</td></tr>
  </tbody>
</table>
| > OS VectorMap Local   | > ✔        | > ✔        | > ✔        |             |
<table class="doc-table">
  <tbody>
    <tr><td>> OS VectorMap > District</td><td>> ✔</td><td>> ✔</td><td>> ✔</td><td></td></tr>
  </tbody>
</table>
| > OS Boundary Line     | > ✔        | > ✔        |            |             |
| > 2000                 |            |            |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> S-57 (Unencrypted > ENC & AML)</td><td>> ✔</td><td>> ✔</td><td>> ✔</td><td>> ✔</td></tr>
  </tbody>
</table>
| > S-57 Encrypted       |            |            | > ✔        |             |
| > (S-63)               |            |            |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> ShapeFiles</td><td>> ✔</td><td>> ✔</td><td>> ✔</td><td>> ✔</td></tr>
  </tbody>
</table>
| > US Census TIGER/Line | > ✔        | > ✔        |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> VPF (DNC, VMAP, WVS > etc.)</td><td>> ✔</td><td></td><td></td><td></td></tr>
  </tbody>
</table>
| > Other Vector (e.g.   | > ✔        | > ✔        |            |             |
| > TAB,                 |            |            |            |             |
| > Spatialite/SQLite)   |            |            |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>##### Raster Datasets</td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>
| > **Data Format**      | > **Studio | > **Direct | > **Other  | > **Runtime |
|                        | > Import** | > Import   | > Runtime  | > Export**  |
|                        |            | > SDK**    | > Import** |             |
+========================+:==========:+:==========:+:==========:+:===========:+
| > ADRG                 | ✔          | ✔          |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> ARCS Chart > (Unencrypted)</td><td>✔</td><td></td><td></td><td></td></tr>
  </tbody>
</table>
| > ASRP                 | ✔          | ✔          |            | ✔           |
<table class="doc-table">
  <tbody>
    <tr><td>> BSB Nautical Chart > Format</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > CADRG/CIB            | ✔          | ✔          | ✔          | ✔           |
<table class="doc-table">
  <tbody>
    <tr><td>> CRP</td><td>✔</td><td></td><td></td><td></td></tr>
  </tbody>
</table>
| > ECRG                 | ✔          | ✔          |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> ECW</td><td>✔</td><td></td><td></td><td></td></tr>
  </tbody>
</table>
| > GeoPackage           | ✔          | ✔          |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> Geospatial PDF</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > GeoTIFF              | ✔          | ✔          | ✔          |             |
<table class="doc-table">
  <tbody>
    <tr><td>> JPEG</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > JPEG2000             | ✔          | ✔          |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>> MrSID</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > NITF/NSIF            | ✔          | ✔          | ✔          |             |
<table class="doc-table">
  <tbody>
    <tr><td>> USRP</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  </tbody>
</table>
| > Other Raster (e.g.   | ✔          | ✔          |            |             |
| > IMG, PNG etc.)       |            |            |            |             |
<table class="doc-table">
  <tbody>
    <tr><td>##### Deprecated SDKs ##### 3D SDK <em>Envitia provide an inte ymbology and draping of </em>Please contact** <suppo or additional informatio he 3D SDK incorporates t apLink maps to create a xploring. Built to exten he 3D SDK offers all of 3D environment. [Figure 27 3D Globe with s olygons.](../../assets/i ##### Library Usage and s with many of the MapLi lavours. It should be no e determined by the Core pplication. For example, f the Core SDK (MapLink6 DK library (MapLink3D64.</td><td>ration to os ll MapLink P t@envitia.co .** e advantages ully immersi and strengt he advantage US States Ex ages/develop onfiguration k SDKs, the ed that the SDK library if you are u .lib) then y ib) and one</td><td>Earth, inclu o layers.<strong> > </strong>or your of 3D terrai e environmen en the MapLi of the othe ruded rs-guide/med D SDK comes ibrary to be hat you are ing the Rele u must also r more OpenG</td><td>ing display ales represe data with e for reviewi k family of components, a/image38.pn n 2 differen linked with sing within se mode, DLL se the equiv libraries.</td><td>f tative isting g and ools, but in ) hould our version lent 3D</td></tr>
  </tbody>
</table>
| **MapLink3D64.lib**          | **MapLink3D64d.lib**           |
|                              |                                |
| Release mode, DLL version.   | Debug mode, DLL version.       |
|                              |                                |
| Uses Multithreaded DLL C++   | Uses Debug Multithreaded DLL   |
| run-time library.            | C++ run-time library.          |
|                              |                                |
| Requires TTLDLL preprocessor | Requires TTLDLL preprocessor   |
| directive.                   | directive.                     |
|                              |                                |
| Your application must also   | Your application must also     |
| link the MapLink CoreSDK     | link the MapLink CoreSDK       |
| library MapLink64.lib and    | library MapLink64d.lib and the |
| the OpenGL library           | OpenGL library opengl32.lib.   |
| opengl32.lib.                |                                |
|                              | No redistributable run-time    |
| Refer to the document        | available.                     |
| \"MapLink Pro X.Y:           |                                |
| Deployment of End User       | **KEYED : Development machines |
| Applications\" for a list of | only.**                        |
| run-time dependencies when   |                                |
| redistributing.              |                                |
|                              |                                |
| Where X.Y is the version of  |                                |
| MapLink you are deploying.   |                                |
<table class="doc-table">
  <tbody>
    <tr><td>##### Migrating from 2D to 3D he MapLink 3D SDK is designed ore SDK and this makes migrati he Core SDK concepts such as t oaded on to a data layer, whic urface. nother core MapLink concept th assivity of the library. This apLink but like for the core S anaged by the application and ntroduced with this SDK are a rom the base 3D data layer, TS s the TSL3DStandardDataLayer f quivalent to the TSLStandardDa ayers, along with any necessar erivative of the 3D drawing su uch as TSL3DWinGLSurface for W ##### The 3D Coordinate Space ll positions in the MapLink 3D oordinates; latitude, longitud arth. It is possible to perfor he reverse using the TSL3DDraw oordinates x, y, z are from th etres. Geodetic coordinates ar re specified outside of the co oles or international data lin ltitude can also be specified SL3DAltitudeType enum. It can rom the height above ground le round level can also be altere xact height to use at that poi t is important to note that as ets are specified in geodetic anipulate these with reference he TSL3DHelper class provides SL3DBoundingBox object, such a ranslate them. ##### Threading he 3D Drawing Surface uses a b ayers. s such you should review the c articular sections [29.5.4](#d 29.9](#d-sdk-accelerator-sdk). ##### Walkthrough 5 - Your Fir f you are familiar with the wa utorial might seem basic and c n the information that appears ##### Skeleton Application <em>Please note that the Wizards ee section [3.2](#maplink-pro- he starting point for this is xecutable. It can be either an ot recommended. The example co pplication. ##### Configure Project Proper nce created, build your skelet inks. You then need to set up ersion of the MapLink librarie D SDK library. These are descr 5.1](#library-usage-and-config C.1.1](#library-usage-and-conf n the x64 Debug configuration odifications to the Project Pr n 'C/C++', 'Code Generation' c s "Multi-Threaded Debug DLL" n 'C/C++', 'General' category, dditional include path, e.g. C:\\Program Files\\Envitia\\Ma n the 'Linker', 'Input' catego apLink3D64d.lib as object/libr General' category add the MapL ibrary path, e.g. C:\\Program Files\\Envitia\\Ma ake the same changes to the x6 gainst MapLink64.lib and MapLi dd #include "MapLink.h" and #i n this example, just add it in </em>Note<em>*: X.Y is the version of ##### Initialisation and Clean he configuration files for Map xecution run using static meth pplication, these are normally he Application object. The sim tandard configuration files fr irectory is specified, then Ma nstallation has taken place an n the InitInstance method of t SLDrawingSurface::loadStandard ocument Template is instantiat ou should be careful to check sing the methods supplied on t onst char \</em> configDirPath = N / Full path and filename to th onst char \<em> transformsFile = SLThreadedErrorStack::clear() SLDrawingSurface::loadStandard / Required for draped polygons SLCoordinateSystem::loadCoordi SLSimpleString msg( "" ); ool anyErrors = TSLThreadedErr "Initialisation Errors : \\n\" f ( anyErrors ) fxMessageBox( msg, MB_OK ) ; xit( 0 ) ; hen your application is deploy he location of your applicatio he transformsFile will need to nce MapLink has been initialis pplication exits, otherwise Vi hich are in fact memory curren his should be done in the Exit ill need to use the class Prop he MFC Application Wizard does ingle Document applications, i iew or Document class. se Properties, Overrides to cr bject. In this method, call Ma oad. int CHelloGlobe::ExitInstance { SLDrawingSurface::cleanup( ) ; return CWinApp::ExitInstance( f you are using the DLL versio he discussion of memory leaks 5.1.2](#visual-studio-warnings ##### Managing the Document n terms of the Document/View a ore MapLink Data Layers. This rom the 2D, for it offers a nu f this example application how SLMapDataLayer. n the private section of the D TSLMapDataLayer object. The b he object should be constructe estroyed in the destructor: HelloGlobeDoc::CHelloGlobeDoc _mapDataLayer = new TSLMapData CHelloGlobeDoc::\~CHelloGlobe { if ( m_mapDataLayer ) { m_mapDataLayer-\>destroy() ; m_mapDataLayer = NULL ; Use Properties, Overrides to this method, set you bool fla member variable. Create a pri parameters and returns void BOOL MapLink3DSimpleDoc::OnOp { if (!CDocument::OnOpenDocumen m_newMap = true ; m_mapName = lpszPathName ; return TRUE; void MapLink3DSimpleDoc::load { if (!m_newMap) return ; m_mapDataLayer-\>removeData() TSLThreadedErrorStack::clear( // Load map and then display m_mapDataLayer-\>loadData( m_ TSLSimpleString msg( "" ); bool anyErrors = TSLThreadedE \"Cannot load map\\n\" ) ; if ( msg ) AfxMessageBox( msg, MB_ICONER else m_mapDataLayer-\>notifyChange } ##### Managing the View n terms of the Document/View a nstance of a TSL3DDrawingSurfa indows platforms, TSL3DX11GLSu ignificant platform-specific d sually instantiated in the OnI indow doesn't exist in the OnC n the private section of the V SL3DWinGLSurface object. This onstructor. se Properties, Overrides to cr his method, check to see if a ecessary. You can optionally a olours as well as drape a pict ill need a private member vari o allow you to do this. You sh ize of the window. oid CHelloGlobeView::OnInitial View::OnInitialUpdate(); f ( !m_drawingSurface ) CRect rect ; etClientRect( &rect ) ; // Create the drawing surface _drawingSurface = new TSL3DWin // Give the \'sky\' a colour! static const TSLStyleID skyCo m_drawingSurface-\>setBackgro static int const wireframeCol static int const solidColourI m_backdrop = TSLUtilityFuncti m_backdrop += \"/config/earth // Set the bitmap to display // for solid-backdrop and wir m_drawingSurface-\>setTerrain solidColourIndex, m_backdrop // Notify surface what size t _drawingSurface-\>wndResize(0, / The following line is discus _drawingSurface-\>setRendering n the destructor of the View, HelloGlobeView::\~CHelloGlobeV f ( m_drawingSurface ) _drawingSurface-\>destroy() ; _drawingSurface = NULL ; ##### Binding Layers and Drawi nce both Document and View are ata Layers to the Drawing Surf he recommended approach to thi he Document, which calls the u ocument's Data Layers to the V voids the View knowing the con qually applicable to both Sing he addToSurface method should f the View, just after the Dra pplications, it is not usually eleteFromSurface method since re adding more than one Data L ave a unique name. reate a public addToSurface me SLDrawingSurface pointer as a ata Layer to the specified Dra ool CHelloGlobeDoc::addToSurfa f ( !m_mapDataLayer \|\| !draw eturn false ; oadMap(); // load the map. eturn drawingSurface-\>addData all this method in the View's urface has been created. At th efine the initial visible area SL3DCamera, before providing a irection in which it is pointi iscussed in 12.8. f ( GetDocument()-\>addToSurfa _drawingSurface-\>camera()-\>r m_drawingSurface-\>camera()-\ TSL3DCameraMoveActionNone ) ; _drawingSurface-\>camera()-\>l ote that MapLink automatically urface separation when either ##### Handling Resize Events ince MapLink is passive, the a vents and pass the information nly need to handle the window fter handling a resize event, essage so there is no need to se Properties, Messages to cre ince it is not there by defaul rawing Surface exists and if s he Drawing Surface using the w nhibit an automatic redraw and ocking the top left corner of oid CHelloGlobeView::OnSize(UI View::OnSize(nType, cx, cy); f ( m_drawingSurface ) _drawingSurface-\>wndResize( 0 andling resize events differs he option of providing a flag esizing takes place around. Th f this control and is discusse ##### Handling Paint Events n the OnDraw method of the Vie ass it to the Drawing Surface, irst. oid CHelloGlobeView::OnDraw(CD f ( m_drawingSurface ) ECT rect ; f ( pDC-\>GetClipBox( &rect ) etClientRect( &rect ) ; _drawingSurface-\>drawDU( rect ect.right, rect.top, true ) ; paint event can be triggered ant to redraw part of the wind ill set up a Clip Box to defin mprove performance it is best fficient to pass the required urface. o create a 3D application you SL3DRenderingCallback triggere endered. This is a static meth oid\</em>. reate a new static method in t mplementation: oid Simple3DInteractionView::r nt pendingTextures ) imple3DInteractionView \<em> view f ( view-\>m_hWnd ) iew-\>Invalidate() ; ow build the program, run it a ##### Reducing Flicker and Imp o far, the application is not ptimisations and the display w here are two reasons for this. he window. Secondly, both MapL rior to the redraw. In depth d olutions may be found in secti he meantime, here are a couple lease be aware this will only pplications. o solve the first issue, a sin rawing Surface is created to m erformance on expose events th hanging. o solve the second issue, you indow. se Properties, Messages to add essage. Return TRUE from this pplication will erase the back OOL CHelloGlobeView::OnEraseBk eturn TRUE ; he inhibition of the WM_ERASEB s drawing to the entire window he window then it may be neces reas that MapLink is not rende ##### 3D Standard Data Layers he TSL3DStandardDataLayer clas erivatives of TSLDataLayer tha uide such as the 2D equivalent reated and added to one or mor ontents are displayed. It is a f non-map 3D data, providing t nd save non-map 3D data as wel n the same way that a TSLStand SLEntity derived objects and t f TSLDynamicDataObject derived ontains instances of TSL3DEnti ##### 3D Entities further 2D Core SDK concept t he use of geometry Entities. A hought of as Entities, derivat SL3DEntity in the 3D. [Figure 28 3D Entity ierarchy](../../assets/images/ n the 3D SDK all entities with umber of properties including: A bounding box defined in 3D A set of rendering attributes One or more TSL3DCoord object cases the orientation and siz ##### TSL3DEntity his is the base class for all o the methods and properties c nclude the ability to query th ounding box, the centre of the rom a specific point. Other op unctions and equality comparis ##### TSL3DModel his class defines a common int ia plug-ins. The model to draw SLRenderingAttributeModelStyle slmodels.dat. ultiple Levels of Detail can b rogressively lower polygon-cou urther away from the camera. ##### TSL3DTriangle and TSL3DQ oth of these shapes are basica imited to having 3 or 4 point reated like the other multipoi r uniquely they can be created bjects. Also like other multip erimeter can be queried. A qua eaning there are no intersecti lane. he order of point specificatio ##### TSL3DTriangleFan and TSL [](../../assets/images/develop hese 3D geometric objects prov djoining triangles that use th reated from closed, filled, 3 or a TSL3DTriangleFan, the fir f the fan. The first three poi ubsequent point defines a tria he previous point and the new irst three points of the strip ubsequent point defines a tria revious two points ##### TSL3DQuadStrip [](../../assets/images/develop his is the 4 point version of he same way; each pair of adde air. Each contained 3D quad mu ontained 3D quad must lie in a ##### TSL3DPolyline his is the 3D version of TSLPo ay not have area depending upo olyline is closed then the fir ertex, except if they exist at olyline is already closed. A c f as being a polygon; the leng erimeter and it now has the co polyline must have at least t hould logically have at least imitations placed upon the coo ##### TSL3DPolygon TSL3DPolygon is a closed, fil onstituent points. It always h rea, but due to it being plana on-complex, meaning its edges 3D polygon may also have one he main polygon also being kno asically cut out sections of t he outer, nor touch or cross a ave consecutive duplicate poin raped Polygons, including extr pplicable limitations are list or draped polygons to work TSL ust be called before the 3D SD ##### Extruded 2D Primitives hese extruded shapes, TSLExtud SLExtruded2DRectangle consist n extrusion and placed at a se reated around the 3D shape, wh ithout destroying the extruded roperties to their 2D counterp irst querying this object for ##### TSL3DEntitySet his is a collection of other 3 o can contain other Entity Set eometric attributes of its own nion of its children's. Like t SL3DEntitySet differs from the ollection by allowing differen ##### 3D User Geometry his is the 3D version of user 3D user geometry entity allow eometry upon 3D standard data oaded from TMF files. A piece arts, the entity (an instance apLink) and the client (an ins SL3DClientUserGeometryEntity, ##### TSL3DUserGeometryEntity his is the 3D version of TSLUs nstances of TSL3DUserGeometryE ayers, and are allocated and d y calling TSL3DUserGeometryEnt reate3DUserGeometry on a TSL3D eometry entity can be set and etClientUserGeometryEntity and espectively. reate, create3DUserGeometry, s allback functions all provide apLink will automatically dele etClientUserGeometryEntity or he user will have to destroy t ser's code is compiled with a ersion to MapLink. reating and destroying user ge SL3DStandardDataLayer\</em> stdLay SL3DClientUserGeometryEntity\<em> SL3DUserGeometryEntity\</em> entit reate3DUserGeometry(client, fa f (!entity) ... // handle error ... ntity-\>destroy(); elete client; // don't need th ##### TSL3DClientUserGeometryE his is the 3D version of TSLCl he user creates clients by der nd creating their own instance e attached to an entity as exp t a minimum, the user must ove ethods. It is however strongly lso implemented within the cli eturned from centre, the retur o perform view frustum culling herefore ensure that the calcu or the entity being rendered i isible from being incorrectly nlike 2D geometry, view frustu s well as individual entities. t is necessary to manually upd SL3DEntitySet as the previous his is done by calling updateB ontains the TSLUserGeometryEnt his entity set can easily be r he TSLUserGeometryEntity. ithin the draw function, the e 0,0,0) in model space is at th ethod with the positive Z-axis arth (ignoring terrain) at tha ach user geometry object opera ystem, the units of which are rawing performed through metho ccept positions using TSL3DCoo bjects rendered in this fashio ould be if drawn from outside he OpenGL state on entry to dr een drawn so far in the curren epending on the view of the ap o assumptions about the OpenGL ollowing: The GL_COLOR_ARRAY, GL_EDGE_F GL_INDEX_ARRAY and GL_SECONDA be enabled. The matrix mode for the built GL_MODELVIEW_MATRIX. The active texture unit will either enabled or disabled. There will be no active progr apLink internally tracks the O tate changes. Therefore care s odifications made to the OpenG ailure to do so may result in ntities. This also applies to SL3DRenderingInterface. Aside se any OpenGL functionality wi ere is an example partial impl lass SquareClient : public TSL rivate: SL3DCoord m_centre; ouble m_radius; ublic: / Constructor quareClient(TSL3DCoord centre) m_centre(centre) m_radius(sqrt(2000000.0\<em>2000 / Destructor irtual \~SquareClient() irtual double boundingSphereRa eturn m_radius; irtual const TSL3DCoord& centr eturn m_centre; / render an orange square irtual bool draw (int uniqueSu SL3DRenderingInterface\</em> rende lPushAttrib( GL_ALL_ATTRIB_BIT lPushClientAttrib( GL_CLIENT_A Lfloat coords\[\] = { -100000. 00000.0f, -100000.0f, 0.0f, 100000.0f, 100000.0f, 0.0f, 00000.0f, 100000.0f, 0.0f }; lColor4f( 1.0f, 0.5f, 0.0f, 1. lDisable( GL_TEXTURE_2D ); lDisable( GL_CULL_FACE ); lEnableClientState( GL_VERTEX_ lDisableClientState( GL_TEXTUR lDisableClientState( GL_INDEX_ lVertexPointer( 3, GL_FLOAT, 3 lDrawArrays( GL_TRIANGLE_STRIP lPopAttrib(); lPopClientAttrib(); eturn true; / stream out the polygon irtual int save (TSLofstream& ... eturn SQUARE_USER_GEOMETRY_ID; ; ##### Loading and saving 3D us he process is almost identical f the user wants their 3D user long with other types of geome ethod on the client, and to pr tatic method SL3DUserGeometryEntity::regist he save method on the client s dentify the type of 3D user ge hey can be passed to any regis uggested that the user publish t is also suggested that the u company identifier, a byte-or ersion number. o register a load callback fun SL3DUserGeometryEntity::regist ointer should have type TSL3DU unction pointer typedef). The ser geometry is loaded, each f ne returns non-NULL. etting a load callback functio SL3DUserGeometryEntity:: egisterUserGeometryClientLoadC ere is a skeleton load callbac tatic TSL3DClientUserGeometryE SLifstream& stream, nt userGeometryID, ool& assumeOwnership) / whether returned entities wi ssumeOwnership = \...; witch (userGeometryID) ase SQUARE_USER_GEOMETRY_ID: ... // stream in client and re ... // etc efault: eturn NULL; ##### 3D Custom Data Layers t is possible to introduce you rawing surface using the TSL3D ou must add an instance of thi ttach to it your own derivativ SL3DClientCustomDataLayer. our derivative of the TSL3DCli verride the pure virtual draw hrough which a number of usefu r bounding box falls within th onversion functions can be per ##### Using the Camera he TSL3DCamera class provides f the drawing surface. It has rientation and normal. The ori osition whereas the normal is irection from the centre to th he camera also provides the ab nown as its field of view. Thi lso allows the user to set the ppear horizontal in the field alue at which the horizon has etres). ##### Integration with Other O t is sometimes desirable to us nterface toolkits or other lib ontext creation. Depending on rawing surfaces can either cre xisting context created extern his fashion, MapLink can be in hrough the swapBuffersManually pplication in control of when ore information can be found i latform\'s drawing surface (TS SL3DX11GLSurface for X11 syste ##### Creating a 3D Model Plug apLink provides an example plu oading files produced by 3D St an be found in the Samples dir odel plug-ins are loaded at ru nd are unloaded when those mod o load and draw a particular m hat is passed to TSL3DDrawingS ntry for each model is a plug- ustom options to be defined fo hould be added to this file an he count of the number of entr omplete description of the for slmodels.dat file provided in nstallation. ##### The Structure of a Plug- ll plug-ins must be compiled a lass that inherits from TSL3DC ill be created for each unique his plug-in. In addition to th ollowing "C" methods: extern \"C\" \_\_declspec(dll void\<em> getModel( int index, const char\</em> filename, const char\<em> pluginString ); extern \"C\" \_\_declspec(dll hen a model is required the ge ndex from tslmodels.dat of the nd the plug-in specific config nvoked once for each model, an erived TSL3DCustomModel class odel. hen a model is no longer requi nvoked, with the object return assed in as the parameter for ##### Drawing a Model plug-in cannot make any assum ngine when drawing, and should ack to what they were original Storing and resetting renderi bool N3DSModel::draw(int draw int lodToDraw) { glPushAttrib( GL_ALL_ATTRIB_B // Change any required states glPopAttrib(); return true; } he model itself should be draw he correct position by the 3D nvoked frequently for models t lug-in should make use of opti o ensure that the drawing take ny textures associated with a SL3DTextureLoader utility clas his class returns the texture ppropriate texture functions u lTexSubImage2D() for OpenGL. I he actual size of the texture equest. For more information s ##### Contouring he Terrain SDK also allows for olygons from the same height i he format that the generated c ontrolled entirely by the appl allbacks. ##### Providing Data for Conto he data to contour is expected SLTerrainContourVertexList of ertex object represents data a re combined, they should form ist object. ach vertex can store one or mo attributes', for the point it e used to model different info epresents. For example, the fi or the terrain at that point, emperature value at that point umidity value. Contour informa f these attributes. Each verte umber of attributes. This example shows loading of database and storing the data for the generation of contour // Process the terrain data i if( m_terrainDB.open( terrain return false; // Query the extent of the te long x1, y1, x2, y2; if( m_terrainDB.queryExtent( return false; // Inform the terrain databas // so it can determine a good long duMinX, duMaxX, duMinY, m_drawingSurface-\>getDUExten m_terrainDB.displayExtent( du x1, y1, x2, y2 ); // Read the data from the ter TSLTerrainDataItem \</em>dataItem new TSLTerrainDataItem\[ m_te if( m_terrainDB.queryArea( x1 m_terrainGridHeight, dataItems ) != TSLTerrain_OK { return false; } // Convert the terrain databa // them to the contour object TSLTerrainContourVertexList \ new TSLTerrainContourVertexLi for( int i = 0; i \< m_terrai { for( int j = 0; j \< m_terrai { vertices-\>addVertex(dataItem dataItems\[(i \<em> m_terrainGri 1, &dataItems\[(i \</em> m_terrainGr } } // Height information is now // from the terrain database delete\[\] dataItems; TSLTerrainContour contour = n // Give our vertex list to th // contouring - the contour o // list contour-\>setVertices( vertic lthough the contour object ass ata contained within the list ithout having to generate a ne ontour object. This avoids hav odify the data used for contou SLTerrainContour object should otifyChanged() method in order or future contouring operation ##### Types of Contours ontour information can be gene enerating contours as lines th an be used, specified by the T implest of these is TSLTerrain riangulated Irregular Network SLTerrainContourLineTypeStanda ome optimisation on the result oints from the calculated cont ses a different algorithm that ood as those generated by the ubstantially faster. hen generating contours as pol ake. #####  Drawing the Contours ontours generated from the TSL pplication via one of the TSLT hich callback is invoked is de ection [17.8.2](#types-of-cont ollowing table:</td><td>o be completely compatible with n very easy. It holds true to ma e Document/View model of data be are in turn loaded onto a drawi t is continued in the 3D SDK is reatly increases the flexibility K means that relevant events mus assed onto the 3D drawing surfac umber of new data layers, each d 3DDataLayer. An example of such r 3D geometric entities which is aLayer for 2D geometry. These ne 2D data layers, should be attac face base class TSL3DDrawingSurf ndows. world are specified in geodetic and altitude above the surface geodetic to geocentric conversi ngSurface where the geocentric centre of the earth and their u also wrapped around the earth i rdinate space, such as passing o . n a number of different ways usi e equated from the mean sea leve el at that point. The height abo using a range of options to ded t from the terrain data. bounding boxes of entities and e oordinates, it is difficult to to the object they were calculat everal helper functions to manip the ability to rotate, scale an ckground thread for rendering of ntents of section [0](#threading ta-layers-1), [29.5.6](#tslpathl t 3D Application kthroughs for the Core SDK then uld be run through quickly conce inside the boxes. re not available for Visual Stud isual-studio-wizards).<strong> n MFC Application Wizard generat SDI or MDI application, although e here will be based upon an SDI ies n application to ensure it compi he Project Properties according you wish to use with the corres bed in sections ration) and guration-14). ake the following checks and perties: tegory, check that the run-time add the MapLink include director Link Pro\\</strong>X.Y<strong>\\include" y, add MapLink64d.lib and ry modules and in the 'Linker', nk lib64 directory as an additio Link Pro\\</strong>X.Y<em>*\\lib64" Release configuration, except l k3D64.lib instead. clude "MapLink3D.h" to relevant o stdafx.h to keep things simple MapLink you are using. Up ink are usually only loaded once ds of TSLDrawingSurface. In an M loaded during the InitInstance m lest way is to tell MapLink to l m a particular directory. If no Link will assume that a full Map will attempt to load from there e App object, add a call to onfig. This should be done befor d. or, and report errors at this st e TSLThreadedErrorStack utility LL ; // Replace if deployed file tsltransforms.dat ULL; // Replace if deployed onfig( configDirPath ) ; ateSystems( transformsFile ); rStack::errorString( msg, ) ; d, make configDirPath variable p s copy of the MapLink config dir be handled in a similar manner. d, it needs to be cleaned up whe ual Studio will report numerous ly in use when the application e nstance method of the App class. rties Overrides to add this meth 't add it by default. Alternativ may be called in the destructor ate an ExitInstance method on th Link to cleanup the configuratio ) ; s of the MapLink libraries, plea n section and-errors). chitecture, the Document contain s where using the 3D SDK differs ber of new Data Layers. For the ver, we shall restrict this to a cument, declare a bool and a poi ol should be constructed to fals in the document constructor and ) : m_newMap( false ) ayer() ; oc () reate an OnOpenDocument handler to true and store the filename ate method loadMap that takes no nDocument(LPCTSTR lpszPathName) (lpszPathName)) return FALSE; ap() ; ; ny errors that have occurred apName.c_str() ) ; rorStack::errorString( msg, OR ) ; () ; chitecture, the View contains an e derived object - TSL3DWinGLSur face on X11 platforms. This is t fference. In an MFC application, itialUpdate method since the ass eate event or in the View constr ew, declare a pointer to a hould be initialised to NULL in ate an OnInitialUpdate handler a rawing Surface exists and create so set a sky, wire frame and sol re over the earth, as is done be ble of type CString, called m_ba uld also tell MapLink about the pdate() LSurface ( m_hWnd, false ); ourIndex( 4 ); ndColour( skyColourIndex ); urIndex( 181 ); dex( 60 ); ns::getMapLinkHome(); png\"; ver the terrain plus colours frame rendering. endering( wireframeColourIndex, ; e window is 0, rect.Width(), rect.Height()); ed in 12.5.9 allback(renderingCallback, this) estroy the Drawing Surface if it ew() g Surfaces ready available, you need to att ce so that MapLink can display i is to create an addToSurface me derlying MapLink routines to add ews Drawing Surface. This struct ents of Document in any detail a e and Multiple Document Interfac e called in the OnInitialUpdate ing Surface has been created. In necessary to have an equivalent FC calls DeleteContents instead. yer to the Drawing Surface, each hod in the Document that takes a arameter. In this, add the Docum ing Surface. e(TSL3DWinGLSurface \</em>drawingSur ngSurface ) ayer( m_mapDataLayer, \"map\" ) nInitialUpdate method, after the s point, it is also appropriate Here we call the reset method o position for the camera and the g. The workings of TSL3DCamera a e( m_drawingSurface ) ) set(); moveTo( 50.0, 0.0, 10000000.0, okAt( 50.0, -5.0, 0.0, false ) ; takes care of Data Layer and Dra s destroyed. plication needs to handle releva onto MapLink. Most applications esize and expose or paint events indows or X will usually post a orce a redraw in the resize hand te a WM_SIZE handler on the View . In this method, check to see i , pass the new corners of the wi dResize method. This example wil ask MapLink to maintain the aspe he visible map area. T nType, int cx, int cy) 0, cx, cy, false ); rom the 2D to the 3D as we are n o indicate an anchor point that s is because the TSL3DCamera tak in section 12.8. , query the required redraw area asking MapLink to clear the back \<em> pDC) = NULLREGION ) left, rect.bottom, or many reasons, some of which w w. Under these circumstances, Wi the part that needs redrawing. o only redraw that part. It is m evice Unit extent to the Drawing ust also provide a when draped data is ready to be d that returns a void and takes e View with the following nderingCallback(void \</em> arg, = (Simple3DInteractionView \<em>)ar d load one of the sample maps. oving Performance aking use of MapLink performance ll appear to flicker when it is Firstly, MapLink is drawing dire nk and Windows are clearing the scussion of these problems and t n [12.5](#optimisation-technique of quick fixes to reduce your ey ork for SDI applications and not le method call should be added w ke it buffered. This will also i t are not due to the visible map hould inhibit Windows from clear a View handler for the WM_ERASEB ethod to indicate to windows tha round. nd(CDC\</em> pDC) GND message is appropriate since If MapLink were drawing to only ary for the application to erase ing into. is a Data Layer, just like the have been discussed in this dev TSLStandardDataLayer. As such, i Drawing Surfaces from whence th specialist data layer for the ha e ability to load, create, manip as a number of miscellaneous fu rdDataLayer contains instances o e TSLObjectDataLayer contains in objects, the TSL3DStandardDataLa y derived objects. at has been continued in the 3D l geometric objects in MapLink c ves of TSLEntity in the 2D and o evelopers-guide/media/image39.pn the exception of user geometry h pace that specify how the entity appe that define the position and in of the entity. D geometric primitives and gives mmon to all its derivatives. The type of derivative an entity is object and the distance this ent rations perform movement and sca ns. rface to 3D models that can be l is determined by setting the rendering attribute to an index set for a model to allow for t models to be used when the mod ad ly restricted types of polygon; nd may not have inners. They can t 3D entities by passing a TSL3D by passing the individual TSL3DC int geometric shapes, their area specifically must be non-comple g edges, and all points must lie is anti-clockwise. DTriangleStrip rs-guide/media/image41.png) de a quick way of creating multi same rendering attributes. Both oint triangles and behave simila t point defines the common centr ts of the fan define a 3D triang gle made up of the common centre oint. For a TSL3DTriangleStrip, also define a 3D triangle. Each gle made up of the new point and rs-guide/media/TSL3DQuadstrip.pn SL3DTriangleStrip and is formed points forms a quad with the pr t be non-complex. All points of plane. yline which always has length an whether the polyline is closed. t and last points are joined by the same 3D position in which ca osed polyline can therefore be t h property becomes the equivalen cept of area. o points, although a closed poly hree, but other than that there dinates. ed, planar feature with three or s a perimeter length property an it can never have volume. It mu ust not cross, although they may r more holes also known as inner n as the outer. These inners are e polygon which may not touch or y other hole. The outer nor inne s. ded, have a number of limitation d in the Release Notes. oordinateSystem::loadCoordinateS is used. d2DPolygon, TSLExtruded2DPolylin f a MapLink 2D shape that has be altitude in a 3D world. They ar ch can be queried or changed for shape. These shapes have identic rts, most of which are accessibl ts 2D object. Entities, but is also an entity and thus be hierarchical. It ha but inherits its bounding box a e 2D version of this object, the OpenGIS specification of an enti types of entity to be contained eometry. the user to create custom-drawn ayers. User geometry can be save f 3D user geometry is composed o f TSL3DUserGeometryEntity, manag ance derived from anaged by the user). rGeometryEntity. tity can be added to 3D standard allocated by MapLink. Create ins ty::create, or by calling ntitySet. The client of a 3D use etrieved by calling getClientUserGeometryEntity, tClientUserGeometryEntity and lo takeOwnership flag. If true, th e the client if it is replaced w hen the entity is destroyed. If e client. This must be false if ifferent compiler or runtime lib metry: r = \...; client = new \...; = stdLayer-\>entitySet()-\> se); s if takesOwnership is true tity entUserGeometryEntity. ving from TSL3DClientUserGeometr of these subclasses. A client c ained above. ride the abstract draw and centr recommended that boundingSphereR nt. In conjunction with the posi value from boundingSphereRadius of user geometry. The user shoul ated bounding sphere radius is a order to avoid user entities th ulled. culling is performed on TSL3DEn If the size of the user geometry te the bounding boxes of its par ounding box may no longer be cor undingBox on the TSL3DEntitySet ty object associated with the cl trieved by using the parent meth tity will be positioned such tha location returned by the user\' perpendicular to the surface of point. This means that within a es within its own local coordina etres. The exception to this is s on the TSL3DRenderingInterface ds, TSL3DCoordSets or a TSL3DEnt are drawn in the same positions ser geometry. w is dependent on the entities t frame, and therefore will diffe lication. The user should theref state on entry to draw other tha AG_ARRAY, GL_FOG_COORD_ARRAY, Y_COLOR_ARRAY client states will in matrix stack will be e GL_TEXTURE0, however texturing m bound. enGL state in order to avoid red ould be taken to reverse any state in before returning from ncorrect rendering of subsequent ny rendering performed through t rom this restriction the user is hin draw in order to render the mentation of a user geometry cli DClientUserGeometryEntity 00.0 + 2000000.0\<em>2000000.0)) ius () const () const faceID, ingInterface) ); L_ATTRIB_BITS ); f, -100000.0f, 0.0f, f ); RRAY ); _COORD_ARRAY ); RRAY ); \</em> sizeof( GLfloat ), coords ); 0, 4 ); tream) r geometry to that of 2D user geometry. geometry classes to be saved and ry, they need to override the sa vide a load callback function to rUserGeometryClientLoadCallback. ould return a positive integer t metry. These numbers should be u ered load callback function. It and track these identifiers. er saves, along with any geometr er mark, a geometry type ID and tion, a pointer to it must be pa rUserGeometryClientLoadCallback. erGeometryLoadCallback (which is ointer will be added to a list; nction on the list will be calle : llback(loadUserGeometryCallback) function: tity\<em> loadUserGeometryCallback( l be freed by MapLink: urn it own custom drawn data to the Ma ustomDataLayer class. To accompl class to your drawing surface a of the abstract class ntCustomDataLayer class will nee ethods, which provide an interfa functions such as querying if a viewing volume and coordinate ormed. he ability to manipulate the use hree main properties: its positi ntation is also known as its loo erpendicular to this and defines top of the view. lity to specify its angle of vie is by default 45 degrees. The c altitude at which the horizon wi f view. This altitude should be meaningful definition (e.g. 100 enGL Applications MapLink in conjunction with use aries that perform their own Ope he constructor used, the MapLink te their own OpenGL context or u lly. When using a drawing surfac tructed not to perform buffer sw constructor argument, leaving th his occurs. the API documentation for each WinGLSurface for Windows, s). in -in named ttl3DS which is capabl dio Max. The source code to this ctory of your MapLink installati time as models that use them are ls are deleted. The plug-in that del is defined by the tslmodels. rface::setupModels(). A part of n specific string which allows f each model and plug-in. New mod given the next available unique es in the file should also be up at of this file can be found in he config directory of your MapL n DLL/shared objects, and must de stomModel. An instance of this c model defined in tslmodels.dat t s the DLL/shared object must exp xport) xport) void deleteModel( void\</em> Model() method will be invoked w model, the full path to the mode ration string. This method will should return an instance of yo hat is responsible for drawing t ed the deleteModel() method will d from the relevant getModel() c leanup by the plug-in. tions about the state of the ren always reset any state changes i y before the draw() method retur g state information in OpenGL. ngSurfaceId, double distanceToEy TS ); and draw the model around 0,0,0 and will be transl DK. Since the draw() method will at are visible in the applicatio isation techniques such as displ as little time as possible. odel can be loaded via the . The loadTexture() method avail n a format suitable for passing ed by the type of plug-in, for e the requested texture size diff t will be resized to satisfy the e the API class documentation. the generation of contour lines formation used in a terrain data ntour information is displayed i cation via the use of rendering ring in the form of a SLTerrainContourVertex objects. a single point, and when all ve regular or irregular grid insid e pieces of height information, epresents. Each of these attribu mation about the point that the st attribute might be height inf second attribute might be a rec and a third attribute might be a ion can be generated separately within the list must have the s height information from a terrai in a TSLTerrainContourVertexList lines. to a terrain database BFile.c_str() ) != TSLTerrain_OK rain data 1, y1, x2, y2 ) != TSLTerrain_OK of the size of our drawing surf resolution for the data uMaxY; ( &duMinX, &duMinY, &duMaxX, &du axX - duMinX, duMaxY - duMinY, ain database = rainGridWidth \<em> m_terrainGridHe y1, x2, y2, m_terrainGridWidth, e to contour vertices so we can vertices = t(); GridHeight; ++i ) GridWidth; j++ ) \[(i \</em> m_terrainGridWidth ) + j Width ) + j\].m_y, dWidth) + j\].m_z); tored in the vertex list so the s no longer required w TSLTerrainContour(); contour object so we can then p ject assumes ownership of the ve s ); mes ownership of the vertex list an still be modified by the appl vertex list and setting it on t ng to do large copies when you w ing. If this is done, the be informed of the change via th to ensure that the updated data . ated either as polygons or lines re are three different algorithm LTerrainContourLineType enumerat ontourLineTypeSimple which uses TIN) to calculate the contour li d uses a similar method but perf ng contour lines to remove dupli urs. TSLTerrainContourLineTypeCO in most cases produces contour l imple or standard methods but is gons there is no algorithm choic errainContour class are passed t rrainContourCallbacks virtual me endent on which type of contour urs)) was requested according to</td></tr>
  </tbody>
</table>
| > Callback                                 | > Used by                               |
<table class="doc-table">
  <tbody>
    <tr><td>> TSLTerrainContourCallbacks::progress</td><td>> All</td></tr>
  </tbody>
</table>
| > TSLTerrainContourCallbacks::drawLine     | > TSLTerrainContour::drawContourLine    |
|                                            | > using the following types:            |
|                                            | >                                       |
|                                            | > TSLTerrainContourLineTypeSimple       |
|                                            | >                                       |
|                                            | > TSLTerrainContourLineTypeCONREC       |
<table class="doc-table">
  <tbody>
    <tr><td>> TSLTerrainContourCallbacks::drawPolygon</td><td>> TSLTerrainContour::drawContourPolygon</td></tr>
  </tbody>
</table>
| > TSLTerrainContourCallbacks::drawPolyline | > TSLTerrainContour::drawContourLine    |
|                                            | > using the following types:            |
|                                            | >                                       |
|                                            | > TSLTerrainContourLineTypeStandard     |
<table class="doc-table">
  <tbody>
    <tr><td>> TSLTerrainContourCallbacks::drawText</td><td>> TSLTerrainContour::drawContourLine > using the following types: > > TSLTerrainContourLineTypeStandard</td></tr>
  </tbody>
</table>
| > TSLTerrainContourCallbacks::drawTIN      | > TSLTerrainContour::drawTIN            |
+--------------------------------------------+-----------------------------------------+

You should override each of the callbacks that will be used for your
selected method of contour generation. The TSLTerrainContourCallbacks
class provides default implementations of all the callbacks so that you
only need to implement the ones that you are interested in.

The callbacks will be invoked numerous times before the original draw
call returns. In order to prevent excessive redrawing your application
should wait until the draw call has returned before updating the display
of your application.

> This example shows an implementation of the
>
> TSLTerrainContourCallbacks::drawPolyline() callback in which the
> generated contour lines are added to a TSLStandardDataLayer to be
> drawn to the screen after contour generation has finished.
>
> void TerrainContouringView::drawPolyline
> (TSLTerrainContourVertexList\* vertices, double attribute)
>
> {
>
> // The coordinates of the vertices given to us are in the coordinate
>
> // system of the terrain data, which may not be the same as that of
>
> // the map we have loaded. Therefore it may be necessary to
>
> // convert the coordinates so the contour lines appear in the correct
>
> // place on the map.
>
> TSLCoordinateSystem \*terrainCS =
>
> m_terrainDatabase-\>queryCoordinateSystem();
>
> const TSLCoordinateSystem \*mapCS =
>
> m_mapDataLayer-\>queryCoordinateSystem();
>
> bool needToConvert = false;
>
> if( terrainCS-\>id() != mapCS-\>id() \|\|
>
> terrainCS-\>getTMCperMU() != mapCS-\>getTMCperMU() )
>
> needToConvert = true;
>
> TSLCoordSet \*coords = new TSLCoordSet();
>
> // Process the list of vertices given to us into a polyline so we can
>
> // display it on the map in a standard data layer
>
> for( int i = 0; i \< vertices-\>numberOfVertices(); ++i )
>
> {
>
> TSLTerrainContourVertex &vertex = vertices-\>at(i);
>
> TSLTMC tmcX = 0, tmcY = 0;
>
> if( !needToConvert )
>
> {
>
> // The terrain database and map coordinate systems are the same
>
> terrainCS-\>MUToTMC( vertex.x(), vertex.y(), &tmcX, &tmcY );
>
> }
>
> else
>
> {
>
> // Convert between the terrain database and map coordinate systems
>
> double lat = 0.0, lon = 0.0;
>
> terrainCS-\>MUToLatLong( vertex.x(), vertex.y(), &lat, &lon );
>
> mapCS-\>latLongToTMC( lat, lon, &tmcX, &tmcY );
>
> }
>
> coords-\>add( tmcX, tmcY );
>
> }
>
> TSLEntitySet \*es = m_contourLayer-\>entitySet();
>
> TSLPolyline \*line = es-\>createPolyline( 0, coords, true );
>
> if( line )
>
> {
>
> line-\>setRendering( TSLRenderingAttributeEdgeStyle, 1 ) ;
>
> // Determine line colour based on the height of the contour
>
> long colour = ( 255 / m_maxTerrainHeight ) \* attribute;
>
> line-\>setRendering( TSLRenderingAttributeEdgeColour,
>
> TSLDrawingSurface::getIDOfNearestColour( colour, 0, 255 - colour) );
>
> line-\>setRendering( TSLRenderingAttributeEdgeThickness, 1 ) ;
>
> }
>
> }

###### Drawing the Contour Labels

When drawing contour lines using TSLTerrainContourLineTypeStandard there
is the option to draw labels for the generated contour lines. This is
enabled by passing a non-NULL value to the textPrefix parameter of the
TSLTerrainContour::drawContourLine() method, which will be passed to the
TSLTerrainContourCallbacks::drawText() callback. This is usually set to
a description of what the value in the label will represent (e.g.
'Height:' or 'Temperature:'), but if nothing is desired can be set to an
empty string.

When using text labels with the alignment value set to
TSLVerticalAlignmentMiddle the contour lines are split at appropriate
points around the labels so that the lines do not run through the labels
themselves. As the contents of the labels are controlled via the
application by the TSLTerrainContourCallbacks::drawText(), this
necessitates informing the contour object of the maximum length that the
text strings will be when the TSLTerrainContour::drawContourLine()
method is invoked.

One way of doing this is to create a dummy text object of the longest
expected length and use this to determine the size to pass in as
follows:

> TSLText \*textObj = m_contourLayer-\>entitySet()-\>createText( 0, 0,
> 0,
>
> maxLengthLabel.str().c_str(), 100 );
>
> // It is necessary to set up the following attributes on the text
> object
>
> // for updateEntityExtent() to work
>
> textObj-\>setRendering( TSLRenderingAttributeTextSizeFactor,
>
> m_textSizeFactor );
>
> textObj-\>setRendering( TSLRenderingAttributeTextSizeFactorUnits,
>
> TSLDimensionUnitsMapUnits );
>
> textObj-\>setRendering( TSLRenderingAttributeTextFont, 2 );
>
> // Set an entity ID on the temporary text object so we can remove it
>
> // once we\'re done
>
> textObj-\>entityID( INT_MAX );
>
> m_contourLayer-\>notifyChanged();
>
> // Store the currently viewed area of the map. In order to calculate
> the
>
> // extent of the text object we need to change the viewed area so that
>
> // our temporary text object would be visible
>
> double viewedUUX1, viewedUUY1, viewedUUX2, viewedUUY2;
>
> m_drawingSurface-\>getUUExtent( &viewedUUX1, &viewedUUY1,
>
> &viewedUUX2, &viewedUUY2 );
>
> double newUUX1, newUUY1, newUUX2, newUUY2;
>
> long newSizeArea = 2 \* m_textSizeFactor;
>
> m_drawingSurface-\>MUToUU( -newSizeArea, -newSizeArea,
>
> &newUUX1, &newUUY1 );
>
> m_drawingSurface-\>MUToUU( newSizeArea, newSizeArea,
>
> &newUUX2, &newUUY2 );
>
> m_drawingSurface-\>resize( newUUX1, newUUY1,
>
> newUUX2, newUUY2, false, true );
>
> // Now calculate the size of our text object
>
> m_drawingSurface-\>updateEntityExtent( textObj );
>
> TSLEnvelope env = textObj-\>envelope( m_drawingSurface-\>id() );
>
> unsigned long envWidth = env.width();
>
> // Now we have the width of the text object in TMCs we need to convert
> this to the terrain database units
>
> double lat1, lon1, lat2, lon2, x1, y1, x2, y2;
>
> m_drawingSurface-\>TMCToLatLong( env.bottomLeft().x(),
>
> env.bottomLeft().y(), &lat1, &lon1 );
>
> m_drawingSurface-\>TMCToLatLong( env.topRight().x(),
>
> env.topRight().y(), &lat2, &lon2 );
>
> m_terrainDB.latLongToMU( lat1, lon1, &x1, &y1 );
>
> m_terrainDB.latLongToMU( lat2, lon2, &x2, &y2 );
>
> // This is the width of the text labels in the terrain database units
>
> // with some additional space either side
>
> width = ( x2 - x1 ) \* 1.5;
>
> // Now we have the width we no longer need our text object
>
> m_contourLayer-\>removeEntity( INT_MAX );
>
> // Finally, reset the viewied area of the map back to what it was
> originally
>
> m_drawingSurface-\>resize( viewedUUX1, viewedUUY1,
>
> viewedUUX2, viewedUUY2, false, false );

###### Performance Notes

Calculating contours can take a considerable amount of time when given
large amounts of data to work on. As the result of a draw operation will
not change if the data remains the same, it is more sensible to store
the results of the contouring operation in a form that allows for fast
rendering. The example in section [17.8.3](#drawing-the-contours) does
this by creating geometry objects for each contouring line and storing
them in a TSLStandardDataLayer. This prevents needless recalculation of
the same points on each draw in the application.

###### Removed SDKs

###### MapLink Application Framework SDK

###### Impact assessment SDK

###### WFS Client

###### Network SDK

###### Database Interference SDK

###### Time SDK

###### Satellite Propagator SDK

###### Entity Store SDK

###### Accelerator SDK

###### Database Data Layer SDK

[^1]: Please contact support if this is an issue so that we can gauge
    the importance of supporting Unicode in the 3D Text primitive.

[^2]: 7-bit ASCII is a subset of UTF-8

[^3]: The methods will be removed in a future release of MapLink. If you
    use these methods please let us know why so that we can assess the
    impact of removal.

[^4]: Only a limited set of Code Pages are listed in this enum. Please
    contact <support@envitia.com> if you need to use a Code Page not
    listed.

[^5]: Only a limited set of Code Pages are listed in this enum. Please
    contact <support@envitia.com> if you need to use a Code Page not
    listed.

[^6]: This isn't strictly true! For backwards compatibility, there is a
    base class implementation of the 'instantiateDO' method. However, in
    practise, this should always be implemented by a derived class. If
    you forget to provide this in a new class, then a run-time error,
    DDO_INSTANTIATEDO_NOT_OVERRIDDEN, will be placed onto the error
    stack.

[^7]: An issue with the Rational Rose documentation generator means that
    the const modifier is not shown in the MapLink API documentation.

[^8]: This is mainly used by the obsolete clone method. The clone and
    unclone methods are for backwards compatibility only and do not need
    to be overridden.

[^9]: This section of the documentation, covering the use of the MapLink
    GML SDK, assumes a reasonable understanding of both GML and the GML
    SF-0 profile. For further information on these topics please refer
    to the OGC website (<http://www.opengeospatial.org/>)

[^10]: All xsd:dates and xsd:dateTimes are converted to UTC time


---

[← Threading](threading)