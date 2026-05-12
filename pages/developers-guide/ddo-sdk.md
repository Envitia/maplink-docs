---
title: "Dynamic Overlays with the DDO SDK"
---

# Dynamic Overlays with the DDO SDK


The Dynamic Data Object (DDO) SDK allows developers to create fully
dynamic overlays within a MapLink application. Each object within this
overlay can have application specific data associated with it through
custom derivations of the base class. The architecture splits the
real-world Data Object from the visualisation, allowing the same object
to be displayed in different ways and in different positions according
to application specific rules.

## Library Usage and Configuration

+-----------------------------------+----------------------------------+
| **MapLinkDDO.lib or               | **MapLinkDDOd.lib or             |
| MapLinkDDO64.lib**                | MapLinkDDO64d.lib**              |
|                                   |                                  |
| Release mode, DLL version.        | Debug mode, DLL version.         |
|                                   |                                  |
| Uses Multithreaded DLL C++        | Uses Debug Multithreaded DLL C++ |
| run-time library.                 | run-time library.                |
|                                   |                                  |
| Requires TTLDLL preprocessor      | Requires TTLDLL preprocessor     |
| directive.                        | directive.                       |
|                                   |                                  |
| Refer to the document \"MapLink   | No redistributable run-time      |
| Pro X.Y: Deployment of End User   | available.                       |
| Applications\" for a list of      |                                  |
| run-time dependencies when        | **KEYED: Development machines    |
| redistributing.                   | only.**                          |
|                                   |                                  |
| Where X.Y is the version of       |                                  |
| MapLink you are deploying.        |                                  |
+-----------------------------------+----------------------------------+

As with the MapLink Core SDK, the Dynamic Data Object SDK comes in 2
different flavours. It should be noted that the library to be linked
with should be determined by the Core SDK library that you are using
within your application. For example, if you are using the Release mode,
DLL version of the Core SDK (MapLink.lib) then you must use the
equivalent Dynamic Data Object SDK library
(MapLinkDDO.lib/MapLinkDDO64.lib). The table below describes the
preprocessor directives and link options that should be set in the
Project Properties for using the MapLink Dynamic Data Object SDK. For
X11 targets, refer to the product Release Notes.

## When to use Dynamic Data Objects

You have already seen how the Core SDK can be used to create dynamic
overlays that are displayed in a TSLStandardDataLayer. These overlays
are dynamically created, but typically change very little once they have
been created. A Dynamic Data Object however is expected to be completely
dynamic. There are several specific circumstances that would suggest
that an Object Data Layer is used instead of a Standard Data Layer

- Objects are frequently created and destroyed.

- Objects are frequently moving or changing size.

- Completely different rendering is required on different Drawing
  Surfaces - e.g. displayed as a symbol in one surface and a polygon in
  another.

- Objects are displayed on multiple Drawing Surfaces with differing
  Coordinate Systems.

- Objects have significant amounts of application data.

- The rendering of an object requires the use of low-level Operating
  System calls for performance reasons, or for primitives that MapLink
  does not support.

## Object Data Layers

The TSLObjectDataLayer class is a Data Layer, just like the
TSLMapDataLayer and TSLStandardDataLayer that you have previously
encountered. As such, it may be created and added to one or more Drawing
Surfaces from whence the contents are displayed.

In the same way that a TSLStandardDataLayer contains instances of
TSLEntity derived objects, the TSLObjectDataLayer contains instances of
TSLDynamicDataObject derived objects. TSLDynamicDataObject is an
abstract class and must be derived from before it can be used. Each
Dynamic Data Object has

- A real-world position and extent.

- Optional, application-specific connection to a database or live feed.

- One or more visualisation objects - one for each Drawing Surface that
  the owning TSLObjectDataLayer is attached to.

The visualisation objects are instances of classes derived from the
abstract TSLDisplayObject. In MapLink parlance, these are Display
Objects. When an Object Data Layer is added to a Drawing Surface, all
Dynamic Data Objects that it currently contains have their instantiateDO
method called in order to create a Display Object for that Drawing
Surface. When a new Dynamic Data Object is added to an Object Data
Layer, the instantiateDO method is called for each Drawing Surface that
the layer is currently attached to.

Query methods are available on the Object Data Layer to obtain a list of
Dynamic Data Objects in the layer, the Display Objects associated with a
particular Drawing Surface or the Display Objects within a particular
area.

In addition to the position and extent associated with a Dynamic Data
Object, Display Objects have their own position and extent. By default,
these are identical to those of the owning Dynamic Data Object however
they can be changed. This separation can be useful under several
circumstances:

- When the Display Object can be dragged or moved away from the position
  of the Dynamic Data Object to prevent clutter or hiding of underlay
  data.

- When the Drawing Surfaces that the Object Data Layer is attached to
  have different coordinate systems or TMC coordinate spaces.

- When the Display Object is fixed-size in pixels and hence requires a
  different TMC extent in each Drawing Surface.

When the Object Data Layer is drawn onto a Drawing Surface, the list of
Display Objects is iterated and any Display Objects whose extent
overlaps the drawn extent have their 'draw' method called. This method
is passed a pointer to a TSLRenderingInterface object which may be used
to perform low-level rendering commands directly onto the Drawing
Surface without the need for the creation of geometric Entities.

## Custom Dynamic Data Objects

TSLDynamicDataObject is an abstract class[^6] and must be derived from
to be of use in an application. The key things to take note of are that
the destructor of the derived class should be virtual and that the
instantiateDO method should be implemented. The signature of this method
is:

TSLDisplayObject\* instantiateDO(TSLDisplayType key, int dsID = 0) const
;

Note that this is a 'const' method[^7]. A common mistake is to miss off
the const modifier resulting in the derived method never being triggered
and a run-time error generated. The key parameter is now obsolete and
may be safely ignored. The dsID is the identifier of the Drawing Surface
as specified with the TSLDrawingSurface::id method. It is supplied so
that decisions can be made about the specific Drawing Surface that the
Display Object is being instantiated for.

For simple applications, the only thing required is to maintain the
position and extent of the Dynamic Data Object using the various
position, move, translate and setExtent methods. In such applications,
it is recommended that any updateDOextent parameters are set to true.

- The move methods set the position and extent of the Dynamic Data
  Object and optionally update the Display Objects positions and
  extents.

- The translate methods adjust the position and extent of the Dynamic
  Data Object by the specified delta values and optionally update the
  Display Objects positions and extents.

- The position methods affect the position of the Dynamic Data Object
  without updating any Display Objects or the Dynamic Data Object
  extent. This is usually only called during initialisation of the
  Dynamic Data Object.

The derived class may contain any application specific information
required and may be driven by an application controlled external data
feed.

## Custom Display Objects

TSLDisplayObject is an abstract class and must be derived from to be of
use in an application. The key things to take note of are that the
destructor of the derived class should be virtual and that the draw
method should be implemented. It is recommended, but not required, that
a copy constructor is also implemented[^8]. The signature of the draw
method is:

bool draw(TSLRenderingInterface \*ri, TSLEnvelope \*extent);

A simple custom implementation of this method will make a sequence of
calls to the Rendering Interface to set up attributes and draw graphical
primitives. The Rendering Interface also provides facilities for
coordinate conversion and access to the low-level Drawable or HDC. The
varieties of attributes available are discussed in sections
[10.6.1](#rendering-attributes).

For simple applications, the Display Object position and extent will be
the same as the owning Dynamic Data Object. More complex applications
often involving multiple representations are discussed in section
[16.7](#advanced-uses-of-the-dynamic-data-object-sdk). Note that it is
the Display Object extent that determines whether it is displayed, not
the Dynamic Data Object extent. To modify the position and extent of the
Display Object independently from its owner, the following methods may
be used:

- The move methods set the position of the Display Object and update the
  extents accordingly.

- The translate methods adjust the position of Display Object by the
  specified delta values and update the extents accordingly.

- The position methods affect the position of the Display Object without
  updating the extent. This is usually only called during initialisation
  of the Display Object.

- The setExtent methods adjust the extent of the Display Object without
  affecting the position.

- The setSize method updates the extent of the Display Object by
  defining a size around the origin rather than the position. This is
  usually only called during initialisation of the Display Object when
  the position of the owning Dynamic Data Object will subsequently be
  used to update the extent.

- The getExtent method returns the current TMC extent of the Display
  Object. Note, for fixed pixel size Display Objects, the current zoom
  factor is used to convert the pixel size into a TMC extent.

For Display Objects that are fixed size in Device Units rather than in
TMC Units, the following methods may be used:

- The setPixSize method defines the size of the Display Object with a
  pixel extent around the origin. This is used dynamically during the
  rendering pass to determine whether the Display Object should be
  drawn. To override this once it has been set use the normal setSize,
  or setExtent methods.

- The getPixSize method queries the extent that was defined using
  setPixSize. Note, for Display Objects that are not fixed size in
  Device Units, this method returns current TMC extent.

- The fixedPixSize method can be used to query whether the Display
  Object is fixed size in Device Units.

## Walkthrough 4 -- Adding Simple Dynamic Objects

This section guides you through adding a simple Dynamic Object Layer to
the MapLink application that has been developed in the earlier
walkthroughs. By the end, you should have an application that displays a
single object which tracks the mouse cursor as it moves over the map.

The example is based on MFC and the C++ SDK, but the same steps apply on
X11 targets and with the other MapLink SDK's.

### Configure Project Settings

You need to set up the project settings according to the version of the
MapLink libraries you wish to use. These are described in section
[16.1](#library-usage-and-configuration-4) and must match those used for
the Core MapLink SDK.

Check/change the following settings in Project Properties:

[x64 configuration:]{.underline} check/change the following settings in
Project Properties:

Under the Link,Input category, add MapLinkDDO64d.lib as an
object/library for the Debug configuration (or MapLinkDDO64.lib for the
Release configuration).

Add #include "MapLinkDDO.h" to relevant files. In this example, just add
it into stdafx.h to keep things simple.

### Adding a TSLObjectDataLayer

The Object Data Layer will be used to manage the Dynamic Data Object and
will need to be added to the document class along with the other Data
Layers. It should be created and destroyed where appropriate and added
to the TSLDrawingSurface when the document and view are bound together.
As an optimisation, we will also make the Map Data Layer double buffered
to avoid having to redraw it every time the Dynamic Objects are updated.

In the Document class definition, add a declaration of the Object Data
Layer just after the Standard Data Layer:

TSLMapDataLayer \* m_mapDataLayer ;

TSLStandardDataLayer \* m_stdDataLayer ;

TSLObjectDataLayer \* m_objDataLayer ; // This line added

The new class variable should be initialised to 0 in the Document
constructor.

CHelloGlobeDoc::CHelloGlobeDoc()

: m_mapDataLayer( NULL ),

m_stdDataLayer( NULL ),

m_objDataLayer( NULL )

{

}

The layer should only be created after a map has been successfully
loaded and should be destroyed when the map layer is destroyed.

> In the Document OnOpenDocument method, instantiate a
> TSLObjectDataLayer if the map is successful:

if ( !m_mapDataLayer-\>loadData( lpszPathName ) )

{

// Error handling as before

return FALSE ;

}

m_stdDataLayer = new TSLStandardDataLayer() ;

m_objDataLayer = new TSLObjectDataLayer() ;

> In the Document DeleteContents method, add the following code to
> delete the overlay layer:

if ( m_objDataLayer )

{

m_objDataLayer-\>destroy() ;

m_objDataLayer = NULL ;

}

> Modify the Document addToSurface method as below to add the extra
> layer and to make the map layer buffered:

if ( !m_mapDataLayer \|\| !m_stdDataLayer

\|\| !m_objDatalayer \|\| !drawingSurface )

{

return false ;

}

bool sts = drawingSurface-\>addDataLayer( m_mapDataLayer, \"map\" ) ;

if ( sts )

{

drawingSurface-\>setDataLayerProps("map",TSLPropertyBuffered,true);

sts = drawingSurface-\>addDataLayer( m_stdDataLayer, \"overlay\" ) ;

}

if ( sts )

sts = drawingSurface-\>addDataLayer( m_objDataLayer, "dynamic" ) ;

return sts ;

### Creating a Custom Dynamic Data Object

Two custom classes are required -- one derived from TSLDynamicDataObject
to supply the interface to the application data and one derived from
TSLDisplayObject to provide the visualisation.

Create a new class, MyDDO which derives from TSLDynamicDataObject and
override the instantiateDO method. Include the header file in the
Document source file.

> class MyDDO : public TSLDynamicDataObject
>
> {
>
> public:
>
> MyDDO(void);
>
> virtual \~MyDDO(void);
>
> virtual TSLDisplayObject \* instantiateDO(TSLDisplayType key, int
> dsID=0) const ;

};

Create a new class, MyDO which derives from TSLDisplayObject and
override the draw method. Include the header file in the MyDDO source
file.

> class MyDO : public TSLDisplayObject
>
> {
>
> public:
>
> MyDO(void);
>
> virtual \~MyDO(void);
>
> virtual bool draw(TSLRenderingInterface \*ri, TSLEnvelope \*extent);
>
> }

In the source file for MyDDO, provide initial empty definitions for the
constructor, and destructor and a simple implementation for the
instantiateDo method.

> MyDDO::MyDDO(void) { }
>
> MyDDO::\~MyDDO(void) { }
>
> TSLDisplayObject \* MyDDO::instantiateDO(TSLDisplayType key,int dsID)
> const
>
> {
>
> return new MyDO() ;
>
> }
>
> In the source file for MyDO, provide initial definitions for the
> constructor, and destructor and a simple implementation for the draw
> method -- draw a red circle 50 pixels high.
>
> MyDO::MyDO(void)
>
> { // Without this, the symbol disappears when the centre goes off
> screen
>
> setPixSize( -25, -25, 25, 25 ) ;
>
> }
>
> MyDO::\~MyDO(void) { }
>
> bool MyDO::draw( TSLRenderingInterface \*ri, TSLEnvelope \*extent )
>
> { // 1023 = filled circle with cross, 181=red in standard config files
>
> ri-\>setupSymbolAttributes( 1023, 181, 50, TSLDimensionUnitsPixels );
>
> ri-\>drawSymbol( position() ) ;
>
> return true ;
>
> }

### Moving the Dynamic Data Object

If you compile and run the application, then load the sample World map,
you will see an object appear in the middle of the map. This is the
Display Object that has been rendered using the MyDO::draw method. In a
real application, there are likely to be many more objects with their
positions being driven via some external data feed. For this example,
however, we will merely update the position of the DDO on a mouse move
event. This will cause updates in all views displaying the Object Data
Layer so if you have created a multiple-document application then the
object will move in all views attached to the document.

In the Document class definition, add a new public method
updateDDOPosition, with the following definition:

bool CHelloGlobeDoc::updateDDOPosition( long x, long y )

{

if ( m_objDataLayer )

{

// Get the solitary DDO -- could iterate over DDO list

TSLDynamicDataObject \* ddo = m_objDataLayer-\>getDDO( 0 ) ;

if ( ddo )

{

ddo-\>move( x, y, true ) ; // true means also updates DO

m_objDataLayer-\>notifyChanged() ; // Invalidates buffer

UpdateAllViews( 0 ) ; // Update views displaying doc

return true ;

}

}

return false ;

}

In the View class, modify the OnMouseMove handler to call this new
method that should make the DDO track the mouse cursor. In the handler,
declare a boolean variable 'moved' at the top of the function and
initialize it to false. If the call to 'pan' is successful, then set
this variable to 'true' as well as invalidating the view rectangle. Add
the following code before the call to CView::OnMouseMove

if ( m_drawingSurface && !moved )

{

CHelloGlobeDoc \* doc = GetDocument() ;

TSLTMC x, y ;

if ( m_drawingSurface-\>DUToTMC( point.x, point.y, &x, &y ) )

doc-\>updateDDOPosition( x, y ) ;

}

Now compile and run your application. Load a map and you should see the
DDO track the mouse across the window. If you have a multiple document
application, create a new window on the document and note that both
views are updated.

## Advanced Uses of the Dynamic Data Object SDK

The earlier walkthrough has shown how to implement a simple dynamic
overlay. Real world applications are rarely that simple however! Common
issues are discussed in the following sections.

### Multiple Representations 

Many applications require an object to have different representations on
different Drawing Surfaces. The Dynamic Data Object SDK allows you to
implement these by instantiating a different Display Object on different
Drawing Surfaces.

The visualisation is encapsulated within the Display Object and may thus
be very specific to a particular usage. The Dynamic Data Object can
distinguish between Drawing Surfaces by using the dsID parameter that is
passed to the instantiateDO method. This is the value that has been set
by the application using the TSLDrawingSurface::id method.

### Multiple Coordinate Systems

Some classes of application have a common dynamic overlay displayed on
top of multiple maps. These maps may be in different coordinate systems.
For example, tracks may be displayed on a Mercator or Dynamic Arc
overview map and on a zoomed-in detailed map -- usually in an
appropriate projection for the location such as the local UTM zone.

The Dynamic Data Object SDK allows you to set the position and extent of
Display Objects independently of the Dynamic Data Objects. One way to
make use of this feature is to hold the generic position of the
real-world object within the Dynamic Data Object as latitude/longitude.
During the instantiateDO call, overwrite the position of the Display
Object with the TMC unit position appropriate to the Drawing Surface for
which the Display Object is being created. A common trick is to set the
TSLDrawingSurface::id to the address of the Drawing Surface, thus
allowing the TSLDrawingSurface pointer to be used to perform coordinate
transformations in the instantiateDO call.

If the Display Object position is updated in sympathy with the Drawing
Surface coordinate system, then Display Objects can be positioned
correctly in all circumstances.

### Rendering using Xlib or Win32

For high performance, the low-level handle to the Drawable or HDC can be
queried during rendering using the Rendering Interface handleToDrawable
method. The application can then make low-level calls to create the
visualisation. Note that the application must be careful to leave the
low-level handle in the state it was when returned from handleToDrawable
-- for example, using the Win32 saveDC and restoreDC methods.



---

[← Tracks SDK](/pages/developers-guide/tracks-sdk) | [Terrain SDK →](/pages/developers-guide/terrain-sdk)
