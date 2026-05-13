---
title: "Walkthrough 1 - Your First MapLink Application"
---

# Walkthrough 1 - Your First MapLink Application


Please note that the Wizards are not available for Visual Studio 2015,
see section [3.2](#maplink-pro-visual-studio-wizards).

This section guides you through constructing a simple MapLink
application from the ground up. By the end, you should have an
application that can load and display a map generated from MapLink
Studio and can correctly handle expose and resize events.

The example is based on MFC and the C++ SDK, but the same steps apply on
X11 targets and with the other MapLink SDK's. The steps below assume
that you are using Visual Studio 2010, but similar steps apply when
using previous versions of Visual Studio.

## Skeleton Application

The starting point for this is an MFC Application Wizard generated
executable. It can be either an SDI or MDI application. The example code
here will be based upon an MDI application.

Use the standard MFC Application Wizard to generate your skeleton
application. The example application here is called "Hello Globe".

## Configure Project Properties

Once created, build your skeleton application to ensure it compiles and
links. You then need to set up the Project Properties according to the
version of the MapLink libraries you wish to use. These are briefly
described in section [5.1](#library-usage-and-configuration) and in the
\"MapLink Pro: Installation and Upgrade Notes\".

Make the following checks and modifications to the Project Properties:

- Under the C/C++, General category, add the MapLink include directory
  as an additional include path, e.g. "C:\\Program
  Files\\Envitia\\MapLink pro\\**X.Y**\\include"

- Under the C/C++, Pre-processor category: add TTLDLL

Then check the following settings dependent on which configuration you
are using.

**Note**: '**X.Y**' refers to the MapLink version you are using.

- Under the Linker, General category: add the MapLink lib64 directory as
  additional library path e.g. "C:\\Program Files\\Envitia\\MapLink
  Pro\\**X.Y**\\lib64"

- Under the Linker, Input category: add MapLink64d.lib as an
  object/library module for the Debug configuration or MapLink64.lib for
  the Release configuration.

- Under the C/C++, Code Generation, select run-time library
  "Multi-Threaded Debug DLL" for Debug configuration or "Multi-Threaded
  DLL" for Release configuration.

Add #include "MapLink.h" to relevant files. In this example, just add it
into stdafx.h to keep things simple.

## API Types

Before we start the first walkthrough example, we should mention that
MapLink Pro has a few types to help with clearly identifying what a
variable is used for and for portability (cross platform and 64-bit).

The types are defined in tslplatformtypes.h and tslatomic.h.

The general types used are as follows:

  ----------------------------------------------------------------------
  General API Type     Meaning
  -------------------- -------------------------------------------------
  TSLTMC               TMC value.

  TSLFeatureID         Feature ID

  TSLVersion           Version related

  TSLPropertyValue     Property value.

  TSLStyleID           Linestyle ID, fill, text, colour etc.

  TSLDeviceUnits       Pixels or surface specific device units

  TSLFileLength        64-bit signed integer to store a file length in.

  TSLFilePosition      64-bit signed integer to store a file position
                       in.

  TSLFileOffset        64-bit signed integer to store a file offset in.

  TSLTimeType          64-bit time value.
  ----------------------------------------------------------------------

The types used to return OS specific drawing handles are as follows:

  ----------------------------------------------------------------------
  OS Specific API Type Meaning
  -------------------- -------------------------------------------------
  TSLDeviceContext     Windows \'HDC\'.

  TSLWindowHandle      Windows \'HWND\'.

  TSLBitmapHandle      Windows \'HBITMAP\', X11 specific structure
                       (defined below).

  TSLDrawableHandle    X11 \'Drawable\'.

  TSLVisualHandle      X11 \'Visual \*\'.

  TSLColourmapHandle   X11 \'Colormap\'.

  TSLScreenHandle      X11 \'Screen \*\'.

  TSLDisplayHandle     X11 \'Display \*\'.
  ----------------------------------------------------------------------

For example; If you pass a specific OS type to a method or you are
querying a method which returns an OS specific type as defined above you
may need to cast the result or argument to the type expected.

## Initialisation and Clean Up

The configuration files for MapLink are usually only loaded once per
execution run using static methods of TSLDrawingSurface. In an MFC
application, these are normally loaded during the InitInstance method of
the Application object. The simplest way is to tell MapLink to load all
standard configuration files from a particular directory. If no
directory is specified, then MapLink will assume that a full MapLink
installation has taken place and will attempt to load from there.

In the method InitInstance method of the App object, add a call to
TSLDrawingSurface::loadStandardConfig. This should be done before the
Document Template is instantiated.

You should be careful to check for, and report errors at this stage by
using the methods supplied on the TSLThreadedErrorStack utility class.

> // Initialise MapLink configuration files.
>
> const char \* configDirPath = 0 ; // Replace if deployed
>
> TSLThreadedErrorStack::clear() ;
>
> TSLDrawingSurface::loadStandardConfig( configDirPath ) ;
>
> // CHeck to see if an errors occured.
>
> TSLSimpleString msg( \"\" );
>
> bool anyErrors =
>
>         TSLThreadedErrorStack::errorString( msg,
>
> \"Initialisation Errors : \\n\" ) ;
>
> if ( anyErrors )
>
> {
>
> AfxMessageBox( (LPCTSTR)TSLUTF8Decoder(msg), MB_OK ) ;
>
> exit( 0 ) ;
>
> }

When your application is deployed, make configDirPath variable point to
the location of your applications copy of the MapLink config directory.

Once MapLink has been initialised, it needs to be cleaned up when the
application exits, otherwise Visual Studio will report numerous "leaks"
which are in fact memory currently in use when the application exits.
This should be done in the ExitInstance method of the App class. You
will need to use the class Properties Overrides to add this method since
the MFC Application Wizard doesn't add it by default. Alternatively, in
Single Document applications, it may be called in the destructor of the
View or Document class.

Use Properties, Overrides to create an ExitInstance method on the App
object. In this method, call MapLink to cleanup the configuration file
load.

TSLDrawingSurface::cleanup( ) ;

If you are using the DLL versions of the MapLink libraries, please note
the discussion of3 memory leaks in section
[5.1.2](#visual-studio-warnings-and-errors).

## Managing the Document

In terms of the Document/View architecture, the Document contains one or
more MapLink Data Layers. For the purposes of this example application,
we shall restrict this to a single TSLMapDataLayer.

In the private section of the Document, declare a pointer to a
TSLMapDataLayer object. This should be initialised to NULL in the
Document constructor.

Use Properties, Overrides to create an OnOpenDocument handler and in
this method, instantiate a Data Layer and load the map file ensuring
that you check for errors.

BOOL CHelloGlobeDoc::OnOpenDocument(LPCTSTR lpszPathName)

{

if (!CDocument::OnOpenDocument(lpszPathName))

return FALSE;

m_mapDataLayer = new TSLMapDataLayer() ;

if ( !m_mapDataLayer-\>loadData( lpszPathName ) )

{

TSLSimpleString msg( "" );

bool anyErrors = TSLThreadedErrorStack::errorString( msg,

\"Cannot load map : \\n\" ) ;

if ( anyErrors )

AfxMessageBox( msg, MB_OK ) ;

m_mapDataLayer-\>destroy() ;

m_mapDataLayer = NULL ;

return FALSE ;

}

return TRUE;

}

Of course, you should also destroy the Data Layer once it is finished
with.

Use Properties, Overrides to override the DeleteContents method and in
here, destroy the Map Data Layer

void CHelloGlobeDoc::DeleteContents()

{

if ( m_mapDataLayer )

{

m_mapDataLayer-\>destroy() ;

m_mapDataLayer = NULL ;

}

CDocument::DeleteContents();

}

## Managing the View

In terms of the Document/View architecture, the View contains an
instance of a TSLDrawingSurface derived object - TSLNTSurface on
Windows platforms, TSLMotifSurface (for historical reasons this surface
has Motif in its name however the drawing surface only uses X11 client
libraries such as Xft, XRender and Xlib) on X11 platforms. This is the
only significant platform specific difference. In an MFC application,
this is usually instantiated in the OnInitialUpdate method since the
associated window doesn't exist in the OnCreate event or in the View
constructor.

In the private section of the View, declare a pointer to a TSLNTSurface
object. This should be initialised to NULL in the View constructor.

Use Properties, Overrides to create an OnInitialUpdate handler and in
this method, check to see if a Drawing Surface exists and create one if
necessary. You should also tell MapLink about the default size of the
window. In the destructor of the View, delete the Drawing Surface if it
exists.

void CHelloGlobeView::OnInitialUpdate()

{

CView::OnInitialUpdate();

if ( !m_drawingSurface )

{

m_drawingSurface = new TSLNTSurface( m_hWnd, false ) ;

RECT cr ;

GetClientRect( &cr ) ;

m_drawingSurface-\>wndResize( cr.left, cr.top,

cr.right, cr.bottom, false ) ;

}

}

CHelloGlobeView::\~CHelloGlobeView()

{

if ( m_drawingSurface )

{

delete m_drawingSurface ;

m_drawingSurface = NULL ;

}

}

## Binding Layers and Drawing Surfaces

Once both Document and View are ready and available, you need to attach
the Data Layers to the Drawing Surface so that MapLink can display it.

The recommended approach to this is to create an addToSurface method on
the Document, which calls the underlying MapLink routines to add the
Documents Data Layers to the Views Drawing Surface. This structure
avoids the View knowing the contents of Document in any detail and is
equally applicable to both Single and Multiple Document Interfaces.

The addToSurface method should be called in the OnInitialUpdate method
of the View, just after the Drawing Surface has been created. In MFC
applications, it is not usually necessary to have an equivalent
deleteFromSurface method since MFC calls DeleteContents instead. If you
are adding more than one Data Layer to the Drawing Surface, each must
have a unique name.

Create a public addToSurface method in the Document that takes a
TSLDrawingSurface pointer as a parameter. In this, add the Document's
Data Layer to the specified Drawing Surface.

bool CHelloGlobeDoc::addToSurface(TSLDrawingSurface \*drawingSurface)

{

if ( !m_mapDataLayer \|\| !drawingSurface )

return false ;

return drawingSurface-\>addDataLayer( m_mapDataLayer, \"map\" ) ;

}

Call this method in the View's OnInitialUpdate method, after the Drawing
Surface has been created. At this point, it is also appropriate to
define the initial visible map area. Here we call the reset method to
display the entire map.

if ( GetDocument()-\>addToSurface( m_drawingSurface ) )

m_drawingSurface-\>reset( false ) ;

Note that MapLink automatically takes care of Data Layer and Drawing
Surface separation when either is destroyed.

## Handling Resize Events

Since MapLink is passive, the application needs to handle relevant
events and pass the information onto MapLink. Most applications will
only need to handle the window resize and expose or paint events.

After handling a resize event, Windows or X will usually post a paint
message so there is no need to force a redraw in the resize handler.
Just changing the window size may distort the aspect ratio of the
display, so MapLink can automatically adjust the visible map area to be
in sympathy with the aspect ratio of the window. This optional behaviour
allows an anchor point to be specified, which is kept at the same place
when updating the visible map area.

Use Properties, Messages to create a WM_SIZE handler on the View class
since it is not there by default. In this method, check to see if a
Drawing Surface exists and if so, pass the new corners of the window to
the Drawing Surface using the wndResize method. This example will also
inhibit an automatic redraw and ask MapLink to maintain the aspect ratio
locking the top left corner of the visible map area.

void CHelloGlobeView::OnSize(UINT nType, int cx, int cy)

{

CView::OnSize(nType, cx, cy);

if ( m_drawingSurface )

{

m_drawingSurface-\>wndResize( 0, 0, cx, cy, false,

TSLResizeActionMaintainTopLeft );

}

}

## Handling Paint Events

A paint event can be triggered for many reasons, some of which will only
want to redraw part of the window. Under these circumstances, Windows
will set up a Clip Box to define the part that needs redrawing. To
improve performance, it is best to only redraw that part. It is most
efficient to pass the required Device Unit extent to the Drawing
Surface.

In the OnDraw method of the View, query the required redraw area and
pass it to the Drawing Surface, asking MapLink to clear the background
first.

void CHelloGlobeView::OnDraw(CDC\* pDC)

{

if ( m_drawingSurface )

{

RECT rect ;

if ( pDC-\>GetClipBox( &rect ) == NULLREGION )

GetClientRect( &rect ) ;

m_drawingSurface-\>drawDU( rect.left, rect.bottom,

rect.right, rect.top, true ) ;

}

}

Now build the program, run it and load one of the sample maps.

## Reducing Flicker and Improving Performance

So far, the application is not making use of MapLink performance
optimisations and the display will appear to flicker when it is redrawn.
There are two reasons for this. Firstly, MapLink is drawing directly to
the window. Secondly, both MapLink and Windows are clearing the display
prior to the redraw. In depth discussion of these problems and their
solutions may be found in section [12.5](#optimisation-techniques). In
the meantime, here are a couple of quick fixes to reduce your eyestrain!

To solve the first issue, a single method call should be added when the
Drawing Surface is created to make it buffered. This will also improve
performance on expose events that are not due to the visible map area
changing.

In the OnInitialUpdate method of the View, add the following call
immediately after the creation of the Drawing Surface.

m_drawingSurface-\>setOption( TSLOptionDoubleBuffered, true ) ;

To solve the second issue, you should inhibit Windows from clearing the
window.

> Use Properties, Messages to add a View handler for the WM_ERASEBKGND
> message. Return TRUE from this method to indicate to windows that the
> application will erase the background.

BOOL CHelloGlobeView::OnEraseBkgnd(CDC\* pDC)

{

return TRUE ;

}

The inhibition of the WM_ERASEBKGND message is appropriate since MapLink
is drawing to the entire window. If MapLink were drawing to only part of
the window then it may be necessary for the application to erase the
areas that MapLink is not rendering into.



---

[← Samples](samples) | [Walkthrough 2 - Modifying the Visible Area →](walkthrough-2)
