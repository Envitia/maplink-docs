---
title: "Walkthrough 3 - Adding a Simple Vector Overlay"
---

# Walkthrough 3 -- Adding a Simple Vector Overlay

In this section, you will take the application that has been developed in the earlier walkthroughs and add an overlay. Within this overlay you can create simple vector objects to be displayed using Entity Based Rendering. You will also create an example of a Symbol displayed using Feature Based Rendering.

## Interaction Mode Modifications

It is obvious that the existing interaction mode in the Hello Globe application is insufficient to allow complex chains of points to be built up so we will try and keep things simple. We will need to make some modifications to allow different kinds of Entities to be created without adding a lot of additional code and logic within the button handlers of the View. A further complication is that your application may be MDI and therefore have many Documents and Views open at the same time.

With these issues in mind we will make the following changes:

- Add a TSLStandardDataLayer to the Document.

- Add a new 'Overlays' menu with options for creating various Entities.

- Add event handlers for the menu to the Document class. The event will be sent to the currently active Document.

- Store the currently selected primitive type. This should be stored statically for MDI applications.

- In the View button handlers check for the Control key being pressed. If so, then call the associated document to create the primitive type and if successful redraw the view. Do this on release.

- In the document class, instantiate the appropriate primitive.

This is obviously a very simplified interaction and has limited encapsulation. For more complex, highly interactive primitive creation and manipulation facilities, Envitia provides the Editor SDK and the companion Spatial SDK. See later sections for details about how to integrate these into an application.

We will assume that the overlay is only available when a map is loaded.

## Adding a TSLStandardDataLayer

Simple vector overlays are usually stored in a TSLStandardDataLayer. This will need to be added to the document class. It should be created and destroyed where appropriate and added to the TSLDrawingSurface when the document and view are bound together.

> In the Document class definition, add a declaration of the Standard Data Layer just after the Map Data Layer:

```cpp
TSLMapDataLayer * m_mapDataLayer ;

TSLStandardDataLayer * m_stdDataLayer ; // This line added
```

The new class variable should be initialised to NULL in the Document constructor.

```cpp
CHelloGlobeDoc::CHelloGlobeDoc()

: m_mapDataLayer( NULL ), m_stdDataLayer( NULL )

{

}
```
The overlay layer should only be created after a map has been successfully loaded and should be destroyed when the map layer is destroyed.

> In the Document OnOpenDocument method, instantiate a TSLStandardDataLayer if the map is successful:

```cpp
if ( !m_mapDataLayer->loadData( lpszPathName ) )

{

// Error handling as before

return FALSE ;

}

m_stdDataLayer = new TSLStandardDataLayer() ; // This line added
```
> In the Document DeleteContents method, add the following code to delete the overlay layer:

```cpp
if ( m_stdDataLayer )

{

m_stdDataLayer->destroy() ;

m_stdDataLayer = NULL ;

}
```
> Modify the Document addToSurface method to add the extra layer:

```cpp
if ( !m_mapDataLayer || !m_stdDataLayer || !drawingSurface )

return false ;

bool sts = drawingSurface->addDataLayer( m_mapDataLayer, "map" ) ;

if ( sts )

sts = drawingSurface->addDataLayer( m_stdDataLayer, "overlay" ) ;

return sts ;
```
## Adding the Overlay Menu and Handlers

This menu will allow the user to select which type of Entity will be created on a button press.

> Use the Dev Studio Resource editor to create a menu called Overlays, with options for Text, Symbol, Polygon, Line and Feature.
>
> You may also wish to add toolbar icons to invoke the menu items.

We need somewhere to store the current overlay type selection. For MDI applications, we will store this globally to avoid confusing the user when swapping between currently open documents. Initialise it to the ID of one of the Overlay menu items.

> In the Document class definition, add a declaration for a static integer to hold the currently selected primitive and initialise it appropriately in the Document .cpp file

```cpp
// This line added in the Document class header, private section

static int m_overlayType ; // This line added in class header

// This line added in the Document .cpp file

int CHelloGlobeDoc::m_overlayType = ID_OVERLAYS_TEXT ;
```

Now we need to add COMMAND handlers to update the chosen overlay type on a user selection.

> Use Class Wizard to add COMMAND handlers for the overlay menu items to the Document and in each handler set the m_overlayType variable. You could use a range command handler and only have one method, but for simplicity we have added one per menu item. You should also add UPDATE_COMMAND_UI handlers to provide some feedback to the user about which overlay type is selected. The handlers for Polygons are shown below. Add them for each of the menu entries

```cpp
void CHelloGlobeDoc::OnOverlaysPolygon()

{

m_overlayType = ID_OVERLAYS_POLYGON ;

}

void CHelloGlobeDoc::OnUpdateOverlaysPolygon(CCmdUI *pCmdUI)

{

pCmdUI->SetCheck( pCmdUI->m_nID == m_overlayType ) ;

}
```
Try building your application. At this point you should have the user interface working, but no primitive creation happening. Check that the m_overlayType variable is set correctly when you select each menu item or toolbar button and that the menu items are ticked correctly.

## Adding the Overlay Creation Interface

With the user interface working, we now need to add the back-end methods which create the Entities. These will be triggered from the View, but to maintain encapsulation should actually be in the Document.

Add a public method to the Document, called createOverlay. This should return a boolean value which indicates whether the creation was successful. As a parameter it will take the Drawing Surface and the position at which the overlay should be created.

Create other, private methods, which provide the implementation for creating each overlay type. These will have the same signature as createOverlay and should be called from it according to the current value of m_overlayType. The code fragment below shows the implementation of createOverlay and a dummy implementation of the text method.

```cpp
bool CHelloGlobeDoc::createOverlay(long x,long y,TSLDrawingSurface *ds)

{

switch ( m_overlayType )

{

case ID_OVERLAYS_LINE : return createPolyline(x, y, ds) ;

case ID_OVERLAYS_POLYGON : return createPolygon(x, y, ds) ;

case ID_OVERLAYS_TEXT : return createText(x, y, ds) ;

case ID_OVERLAYS_SYMBOL : return createSymbol(x, y, ds) ;

case ID_OVERLAYS_FEATURE : return createFeature(x, y, ds) ;

}

return false ;

}

bool CHelloGlobeDoc::createText(long x,long y,TSLDrawingSurface*ds)

{

return false ;

}
```
## Triggering the Overlay Creation

In the View class LButtonUp handler, we should call the createOverlay method if the Control button is pressed.

```cpp
void CHelloGlobeView::OnLButtonUp(UINT nFlags, CPoint point)

{

if ( m_drawingSurface )

{

if ( nFlags & MK_CONTROL )

{

TSLTMC x, y ;

m_drawingSurface->DUToTMC( point.x, point.y, &x, &y ) ;

if ( GetDocument()->createOverlay( x, y, m_drawingSurface ) )

InvalidateRect( 0, FALSE ) ;

}

else if ( abs( . . . . /* Rest of method the same */ ) )
```
## Creating the Text Overlay

Build the application and ensure that the create methods are being triggered when the Control - Left Mouse Button combination is used.

Now we will create some text at the button click location and if successful return true. The success return status will force the View to redraw itself.

Replace the dummy implementation of createText with the following:

```cpp
TSLEntitySet * es = m_stdDataLayer->EntitySet() ;

TSLText * txt = es->createText( 0, x, y, "Hello World" ) ;

if ( !txt )

return false ; // Return failure if text could not be created

TSLStyleID black = TSLDrawingSurface::getIDOfNearestColour( 0, 0, 0 ) ;

// Set the rendering of the text to be black, Arial, 25 pixels high

txt->setRendering( TSLRenderingAttributeTextFont, 1 ) ;

txt->setRendering( TSLRenderingAttributeTextColour, black ) ;

txt->setRendering( TSLRenderingAttributeTextSizeFactor, 25.0 ) ;

txt->setRendering( TSLRenderingAttributeTextSizeFactorUnits,

TSLDimensionUnitsPixels ) ;

// Tell the layer that its contents have changed

m_stdDataLayer->notifyChanged( true ) ;

return true ;
```
The key points of this code are

- The Text Entity is created in the Entity Set of the overlay Standard Data Layer. If the static TSLText::create method was used, then the Text Entity would not be attached to any Drawing Surface and hence would never be displayed.

- The createText method of the Entity Set returns false if the creation failed. If this happens, examine the contents of the error stack to determine why. With Text, it is usually because the string is empty.

- You can lookup colour indices in the currently loaded palette using the static TSLDrawingSurface::getIDOfNearestColour method. Note: You may wish to use 24bit RGB colour (see TSLColourHelper API Documentation).

- Ensure that you set the minimum attributes required, as specified in section [10.6.13](#minimum-attribute-requirements). Other attributes are optional.

- Always call notifyChanged after completing a sequence of modifications to the layer. If this is not called, then MapLink will assume that any buffer associated with the Drawing Surface or Data Layer are up to date until the next change of viewing area.

## Creating the Symbol Overlay

The example Symbol that we shall create will be sized in Map Units. This means that it will scale according to the current zoom factor. It is very dependent upon the current map loaded. We are assuming that the sample Dorset map is loaded. This may be found in:

\<MAPLINK_HOME\>\\Samples\\MapForSamples\\Dorset\\Dorset.map

Replace the dummy implementation of createSymbol with the following:

```cpp
TSLEntitySet * es = m_stdDataLayer->EntitySet() ;

TSLSymbol * symbol = es->createSymbol( 0, x, y ) ;

if ( !symbol )

return false ;

// Create a green star, 1000m high.

// This looks sensible on the Dorset map!

TSLStyleID green= TSLDrawingSurface::getIDOfNearestColour( 0, 255, 0 ) ;

symbol->setRendering( TSLRenderingAttributeSymbolStyle, 14 ) ;

symbol->setRendering( TSLRenderingAttributeSymbolColour, red ) ;

symbol->setRendering( TSLRenderingAttributeSymbolSizeFactor,1000.0);

symbol->setRendering( TSLRenderingAttributeSymbolSizeFactorUnits,

TSLDimensionUnitsMapUnits ) ;

// Tell the layer that its contents have changed

m_stdDataLayer->notifyChanged( true ) ;

return true ;
```
Many different symbols are supplied with MapLink. Use the method described in section [10.6.12](#determining-styles-and-font-indices) to determine an appropriate index.

## Creating the Polygon Overlay

Unlike Text and Symbol Entities, Polygons are defined with many coordinates defining the boundary of the polygon. This list of coordinates must be created via the TSLCoordSet class and passed to the Polygon create method.

The example below uses the Drawing Surface conversion routines to determine the current zoom factor and then creates a polygon at a specific screen size for the current zoom factor. Zooming in or out will make the Polygon appear larger or smaller.

Replace the dummy implementation of createPolygon with the following:

```cpp
TSLEntitySet * es = m_stdDataLayer->EntitySet() ;

// Create a coordinate list forming a triangle around the position

// Use the Drawing Surface to calculate the coordinates

// We will make our triangle 25 pixels either side of the position

// Note that the pixels are at the current zoom factor - the polygon

// is always completely scalable

TSLCoordSet * coords = new TSLCoordSet() ;

if ( !coords )

return false ;

double tmcPerDU = ds->TMCperDU() ;

coords->add( x - 25 * tmcPerDU, y - 25 * tmcPerDU ) ;

coords->add( x + 25 * tmcPerDU, y - 25 * tmcPerDU ) ;

coords->add( x, y + 25 * tmcPerDU ) ;

// Hand ownership of the coordset to the polygon

TSLPolygon * poly = es->createPolygon( 0, coords, true ) ;

if ( !poly )

return false ;

TSLStyleID yellow = TSLDrawingSurface::getIDOfNearestColour( 255, 255, 0 );

TSLStyleID black = TSLDrawingSurface::getIDOfNearestColour( 0, 0, 0 ) ;

poly->setRendering( TSLRenderingAttributeFillStyle, 1 ) ;

poly->setRendering( TSLRenderingAttributeFillColour, yellow ) ;

poly->setRendering( TSLRenderingAttributeEdgeStyle, 1 ) ;

poly->setRendering( TSLRenderingAttributeEdgeColour, black ) ;

poly->setRendering( TSLRenderingAttributeEdgeThickness, 1.0 ) ;

// Tell the layer that its contents have changed

m_stdDataLayer->notifyChanged( true ) ;

return true ;
```
## Creating the Polyline Overlay

Polylines use the same mechanism as Polygons to specify the list of coordinates that should be used.

The example below uses the Drawing Surface conversion routines to determine the current zoom factor and then creates a Polyline at a specific size for the current map - i.e. the Polyline is drawn in real-world units. It also uses the Thickness Units Rendering Attribute to specify the thickness of the line in real-world units. Zooming in or out will make the Polygon appear larger or smaller and change the displayed thickness of the line. The values chosen are appropriate for the sample Dorset map.

Replace the dummy implementation of createPolygon with the following:

```cpp
TSLEntitySet * es = m_stdDataLayer->EntitySet() ;

// Create a coordinate list forming a triangle around the position

// Use the Drawing Surface to calculate the coordinates

TSLCoordSet * coords = new TSLCoordSet() ;

if ( !coords )

return false ;

// Make a triangle, 1km either side of the specified position

double tmcPerMU = ds->TMCperMU() ;

coords->add( x - 1000 * tmcPerMU, y + 1000 * tmcPerMU ) ;

coords->add( x, y - 1000 * tmcPerMU ) ;

coords->add( x + 1000 * tmcPerMU, y + 1000 * tmcPerMU ) ;

// Hand ownership of the coordset to the polygon

TSLPolyline * poly = es->createPolyline( 0, coords, true ) ;

if ( !poly )

return false ;

// Use MapUnit thickness so the line thickness scales as we zoom

// in/out

// Set it to 20m. Complex line styles - like style 48 have thickness

// clamping applied automatically to avoid performance

// or aesthetic problems

TSLStyleID yellow = TSLDrawingSurface::getIDOfNearestColour(255, 255, 0) ;

poly->setRendering( TSLRenderingAttributeEdgeStyle, 48 ) ;

poly->setRendering( TSLRenderingAttributeEdgeColour, yellow ) ;

poly->setRendering( TSLRenderingAttributeEdgeThickness, 20.0 ) ;

poly->setRendering( TSLRenderingAttributeEdgeThicknessUnits,

TSLDimensionUnitsMapUnits) ;

// Tell the layer that its contents have changed

m_stdDataLayer->notifyChanged( true ) ;

return true ;
```
## Creating the Feature Based Symbol Overlay

The previous examples have used Entity Based Rendering, in which every Entity has its own definition of Rendering Attributes. As discussed in Section [10.6.10](#feature-based-rendering), MapLink also has the capability to specify the Rendering Attributes of a Feature type on the Data Layer or Drawing Surface and on the individual Entity specify which Feature the Entity represents.

To do this, we must first configure the Data Layer and specify the rendering.

After the Standard Data Layer has been constructed, define some Feature Rendering for use during the Feature creation and rendering.

In the Document OnOpenDocument method, add the following code:

```cpp
TSLStyleID black = TSLDrawingSurface::getIDOfNearestColour( 0, 0, 0 ) ;

// Make up a feature name and numeric ID

m_stdDataLayer->addFeatureRendering( "Airport", 123 ) ;

// Associate some rendering with the new feature, use ID for

// efficiency

m_stdDataLayer->setFeatureRendering( 0, 123,

TSLRenderingAttributeSymbolStyle, 6003 ) ;

m_stdDataLayer->setFeatureRendering( 0, 123,

TSLRenderingAttributeSymbolColour, black ) ;

m_stdDataLayer->setFeatureRendering( 0, 123,

TSLRenderingAttributeSymbolSizeFactor, 40.0 ) ;

m_stdDataLayer->setFeatureRendering( 0, 123,

TSLRenderingAttributeSymbolSizeFactorUnits,

TSLDimensionUnitsPixels);
```

Next, we implement the createFeature method to create the symbol referencing the Feature ID that we have just created.

> Replace the dummy implementation of createFeature with the following:

```cpp
TSLEntitySet * es = m_stdDataLayer->EntitySet() ;

// 123 is the numeric feature code we assigned on the Data Layer

TSLSymbol * symbol = es->createSymbol( 123, x, y ) ;

if ( !symbol )

return false ;

// No need to configure any rendering, MapLink will look it up

// from the Data Layer at display time.

// Tell the layer that its contents have changed

m_stdDataLayer->notifyChanged( true ) ;

return true ;
```
Congratulations! You can now create vector overlays!

