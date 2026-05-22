---
title: "Walkthrough 2 - Modifying the Visible Area"
---

# Walkthrough 2 - Modifying the Visible Area

Congratulations! You have now created your first MapLink application. As applications go though, it's not the most useful since you are restricted to looking at the whole of the map area. The next step is to add some user interaction and thus look at any area of the map.

## Defining and Implementing an Interaction Model

Firstly you must decide on your interaction model. This is the combination of menu selections and mouse actions. With the sample applications, Envitia supplies the source code for a pre-built interaction model. This varies according to the specific application since some have more complex requirements such as editing. These usually require switching modes via menu selections or toolbar buttons.

For the purposes of this example, we will now implement the following interaction model, which does not require any additional menu items.

- Left button click: Pan to clicked point and zoom in by 25%

- Right button click: Zoom out by 25%

- Left button drag: Zoom in to chosen rectangle

- Right button drag: Grab and move the current view with the mouse

We shall define a click as a button press/release cycle where the cursor does not move more than 3 pixels between press/release. A drag is a press/move/release action where the movement is more than 3 pixels.

As an extension, we will also add some handling for the mouse wheel, should one be installed. You should generally be careful not to create an interaction mechanism that is totally dependent upon the mouse wheel since the user may not have such hardware. There are also various driver issues regarding wheel support that are discussed later.

- Wheel spin: Zoom in and out

- Wheel press (or middle button click with 3 button mouse): Pan to clicked point

For deployed applications, it is recommended that the TSLInteractionModes are used. These examples are merely to show how custom interactions could be used and to promote understanding of what goes on "under the bonnet" of MapLink.

### Adding Simple Zoom/Pan Handlers

These handlers should be added to the View since each Drawing Surface is independent even if attached to the same Data Layers. Note that all the view manipulation methods on the TSLDrawingSurface return true if they were successful and false if unsuccessful. A failure usually indicates that the Coordinate Space limits were reached. It is usually more efficient to inhibit the automatic redraw in these methods and control the redraw by invalidating the window. This is especially true when applying echo styles, for example with zoom to rectangle.

> Use Properties, Messages to add handlers to the View for the WM_LBUTTONUP and WM_RBUTTONUP events.
>
> In the OnLButtonUp method, check that a Drawing Surface has been created and if so convert the mouse position to a User Unit position. This position should be used as a parameter to the TSLDrawingSurface::pan method. If both pan and zoom were successful, then invalidate the window rectangle to force a redraw.

```cpp
void CHelloGlobeView::OnLButtonUp(UINT nFlags, CPoint point)

{

if ( m_drawingSurface )

{

double uux, uuy ;

if (m_drawingSurface->DUToUU( point.x, point.y, &uux, &uuy ) )

{

if ( m_drawingSurface->pan( uux, uuy, false ) )

{

if ( m_drawingSurface->zoom( 25, true, false ) )

InvalidateRect( 0, FALSE ) ;

}

}

}

CView::OnLButtonUp(nFlags, point);

}
```
> In the OnRButtonUp method, check that a Drawing Surface has been created and if so, simply zoom out.

```cpp
void CHelloGlobeView::OnRButtonUp(UINT nFlags, CPoint point)

{

if ( m_drawingSurface )

{

if ( m_drawingSurface->zoom( 25, false, false ) )

InvalidateRect( 0, FALSE ) ;

}

CView::OnRButtonUp(nFlags, point);

}
```
### Zoom to Rectangle

For this interaction we need to remember the position that the user first pressed the left button, and when they release it compare the press and release positions. If they are more than 3 pixels apart then we can assume that they have dragged a rectangle, convert the press and release mouse positions to User Units and ask the TSLDrawingSurface to display that area. Of course, the aspect ratio of the selected rectangle may not match the aspect ratio of the window. To cope with such situations, the TSLDrawingSurface::resize method has a parameter to indicate that MapLink should adjust the specified rectangle to match the window aspect ratio. If the aspect ratios are mismatched, then MapLink will attempt to ensure that the entirety of the specified rectangle is displayed.

> Add a member variable to hold the pressed mouse location: CPoint m_lmb. Use Properties, Messages to add a handler to the View for the WM_LBUTTONDOWN event.
>
> In the OnLButtonDown method, store the mouse position.

```cpp
void CHelloGlobeView::OnLButtonDown(UINT nFlags, CPoint point)

{

m_lmb = point ;

CView::OnLButtonDown(nFlags, point);

}
```
> Modify the OnLButtonUp method after the Drawing Surface has been validated.

```cpp
if ( abs( point.x - m_lmb.x ) <= 3 && abs( point.y - m_lmb.y ) <= 3 )

{

// Pan to point and zoom

double x, y ;

if ( m_drawingSurface->DUToUU( point.x, point.y, &x, &y ) )

{

if ( m_drawingSurface->pan( x, y, false ) )

{

if ( m_drawingSurface->zoom( 25, true, false ) )

InvalidateRect( 0, FALSE ) ;

}

}

}

else

{

// Zoom to rectangle

double x1, y1, x2, y2 ;

if ( m_drawingSurface->DUToUU( point.x, point.y, &x1, &y1 )

&& m_drawingSurface->DUToUU( m_lmb.x, m_lmb.y, &x2, &y2 ) )

{

if ( m_drawingSurface->resize( x1, y1, x2, y2, false, true ) )

InvalidateRect( 0, FALSE ) ;

}

}
```
The TSLViewMode classes supplied with the MapLink SDK samples have a fully functional "Zoom to Rectangle" mode, including echo of the rubber-band rectangle. For the purposes of this simple introduction, we shall ignore the echo rectangle. For information about the echo modes, please see the "mfc" sample.

### Grab Pan

For this interaction we need to remember the position that the user first pressed the right button and when the mouse moves, compare the mouse position with the press. If they are more than 3 pixels apart then we can assume that they have dragged the cursor and pan the map appropriately. This will also need a slight modification to the right button release handler to inhibit the zoom out if a grab has occurred.

Add a member variable to hold the pressed mouse location: CPoint m_rmb and also to hold the last grabbed position: CPoint m_lastGrabPoint. This variable will be used to calculate delta offsets for the pan. We also need flags to indicate whether a grab has occurred and whether one should be checked for: bool m_grabbed, m_checkForGrab.

In the View constructor, initialise the boolean variables

```cpp
CHelloGlobeView::CHelloGlobeView()

: m_drawingSurface(NULL), m_grabbed(false), m_checkForGrab(false)

{

}
```
> Use Properties, Messages to add a handler to the View for the WM_RBUTTONDOWN event. In the OnRButtonDown method, store the mouse position and clear the m_grabbed flag and set the m_checkForGrab flag. These will be checked in the WM_MOUSEMOVE handler and the WM_RBUTTONUP handler.

```cpp
void CHelloGlobeView::OnRButtonDown(UINT nFlags, CPoint point)

{

m_rmb = m_lastGrabPoint = point ;

m_grabbed = false ;

m_checkForGrab = true ;

CView::OnRButtonDown(nFlags, point);

}
```
The OnRButtonUp method now needs modifying to ensure that the zoom out only occurs if no grab was active and the grab related flags should be cleared down.

```cpp
void CHelloGlobeView::OnRButtonUp(UINT nFlags, CPoint point)

{

if ( m_drawingSurface && !m_grabbed )

{

if ( m_drawingSurface->zoom( 25, false, false ) )

InvalidateRect( 0, FALSE ) ;

}

m_grabbed = m_checkForGrab = false ;

CView::OnRButtonUp(nFlags, point);

}
```
The next step is to create a mouse move handler and determine whether any grab is active. If so, then the new display centre needs to be calculated and passed to MapLink. As before, the TSLDrawingSurface::pan method will return true on success and false on failure. A successful pan should invalidate the window rectangle.

Use Properties, Messages to add a handler to the View for the WM_MOUSEMOVE event

```cpp
void CHelloGlobeView::OnMouseMove(UINT nFlags, CPoint point)

{

if ( m_checkForGrab

&& ( m_grabbed || abs( point.x - m_rmb.x ) > 3

|| abs( point.y - m_rmb.y ) > 3 ) )

{

// Calculate offset between the last point and the new point

long du_offset_x = m_lastGrabPoint.x - point.x ;

long du_offset_y = point.y - m_lastGrabPoint.y ;

// Indicate a grab and remember the last grabbed point

m_lastGrabPoint = point ;

m_grabbed = true ;

// Convert the offset from the last point into user units

// No DUPerUU() function so we will take the long way round.

double uu_per_du = m_drawingSurface->TMCperDU()

/ m_drawingSurface->TMCperUU() ;

double uu_offset_x = du_offset_x * uu_per_du ;

double uu_offset_y = du_offset_y * uu_per_du ;

// Get the current centre point of the Drawing Surface

double x, y, x1, y1, x2, y2 ;

m_drawingSurface->getUUExtent( &x1, &y1, &x2, &y2 ) ;

x = ( x1 + x2 ) / 2 ;

y = ( y1 + y2 ) / 2 ;

// Adjust the centre for the calculated offset

x += uu_offset_x ;

y += uu_offset_y ;

// Pan and redraw the Drawing Surface

// Request redraw only if pan is successful

if ( m_drawingSurface->pan( x, y, false ) )

InvalidateRect( 0, FALSE ) ;

}

CView::OnMouseMove(nFlags, point);

}
```
## Mouse Wheel

Many modern PC systems will have a wheel mouse available, where a wheel has replaced the middle button. This can spin and also be pressed to act as a button.

### Wheel Support Issues

There are many issues surrounding wheel mouse support, particularly since there are many different drivers. Some drivers provide special functionality that overrides any application specific handling and replaces it with generic scrolling support. This is commonly termed 'Universal Scrolling' or 'IntelliPoint Wheel Support'.

Many MapLink applications, such as the MapLink Viewer and MapLink Studio provide specialist wheel handling to give control over the zoom factor. You can easily see if your mouse driver is overriding the application wheel support by trying the wheel in the MapLink Viewer. If this scrolls vertically instead of zooming in and out then your driver is ignoring any application specific behaviour. Some drivers can only turn this override off globally, whilst others allow it to be disabled for individual programs.

To control the generic scrolling, please review your mouse driver help, but you could try the following:

- Invoke the Control Panel, Mouse dialog.

- Select the Wheel tab.

- With some drivers, there may be a 'Universal Scrolling' check box here. Uncheck this box to remove the generic support and thereby enable application specific behaviour.

- Other drivers may have an 'Advanced' button to press. Be careful here since some drivers have two buttons labelled 'Advanced' on the same panel! Try both.

- The Advanced Wheel Support dialog may allow you to disable IntelliPoint wheel support or Universal Scrolling. You may be able to choose a specific program executable should you wish to maintain the generic support for non-wheel enabled programs.

If you have a mouse wheel but no access to the controls described above then you may need to install a new mouse driver. Your mouse driver may also have specific configuration control over what happens when you press the wheel. Again, please see your mouse driver help for further information.

### Wheel Controlled Zoom and Pan

Assuming you have disabled generic wheel support for your application, you can add in support for zoom and pan operations using the mouse wheel. Firstly we will add wheel zoom support.

> Use Properties, Messages to add a handler to the View for the WM_MOUSEWHEEL message. In the OnMouseWheel method, it either zooms in or out dependent upon the wheel direction.

```cpp
BOOL CHelloGlobeView::OnMouseWheel(UINT nFlags,short zDelta,CPoint pt)

{

// Zoom in or out depending upon the wheel direction

if ( m_drawingSurface

&& m_drawingSurface->zoom( 30.0, zDelta > 0, false ) )

{

InvalidateRect( NULL, FALSE );

}

return CView::OnMouseWheel(nFlags, zDelta, pt);

}
```
Use Properties, Messages to add a handler to the View for the WM_MBUTTONUP event.

```cpp
void CHelloGlobeView::OnMButtonUp(UINT nFlags, CPoint point)

{

double x, y ;

if ( m_drawingSurface

&& m_drawingSurface->DUToUU( point.x, point.y, &x, &y ) )

{

if ( m_drawingSurface->pan( x, y, false ) )

InvalidateRect( 0, FALSE ) ;

}

CView::OnMButtonUp(nFlags, point);

}
```
