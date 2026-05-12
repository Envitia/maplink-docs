---
title: "MapLink 3D Earth SDK"
---

# MapLink 3D Earth SDK


The MapLink Pro Earth SDK provides a MapLink 3D API to customer
applications, building upon the powerful and performant OsgEarth 3D
library.

## Sample Application

A sample application is provided to demonstrate capability and the usage
of the API. The sample code may be found in the installation at
Samples/NT/3DEarth.

### Interaction Modes

The sample application demonstrates various methods of interacting with
the scene, accessible through the sample application's Interaction Mode
menu. When a menu entry is selected that mode will be activated and
remain active until the user selects another.

The implementation of these interaction modes may be found in the
interactions folder within the sample application.

### Trackball View Interaction

A mode which provides the ability to navigate the globe using the mouse
pointer.

When active (by the default settings), the following actions can be
performed:

- Pan: Click and drag the left mouse button across the globe to move the
  camera's eye and target together across the map. Movement is relative
  to the actual movement of the mouse pointer across the map.

- Tilt: Click and drag the right mouse button to change the orientation
  of the camera's eye relative to the target. Vertical mouse movement
  raises or lowers the tilt angle, and horizontal movement changes the
  heading.

- Zoom: Scroll with the mouse wheel to decrease or increase the distance
  between the camera and the target. Forward scrolling brings the camera
  closer to the target.

An alternative constructor has been provided to allow remapping of Pan
and Tilt operations to different mouse buttons.

The sensitivity (the factor by which mouse movement affects the camera
movement) can also be changed for the Tilt and Zoom operations. This can
be done in the alternative constructor, or via separate setter
functions.

### Select Geometry/Track

A mode which provides picking/selection functionality of tracks and
geometry primitives. When active a left click will perform picking
operations on the scene bound to the left mouse button.

If a Track is clicked it will become the active track and display
additional information.

If a geometry instance is clicked its rendering will toggle the
primitive's style between a normal and selected variant, which primarily
affects the colour of the primitive.

### Create Polygon

A mode which creates earth::geometry::Polygon primitives within the
scene.

The left mouse button will start a new primitive or add points to the
in-progress one. The right mouse button will finish creation of the
primitive and add the final version into the scene.

These polygons will be created as draped 2D primitives and will
automatically follow any underlying terrain.

### Create Polyline

A mode which creates earth::geometry::Polyline primitives within the
scene.

The left mouse button will start a new primitive or add points to the
in-progress one. The right mouse button will finish creation of the
primitive and add the final version into the scene.

These lines will be created as draped 2D primitives and will
automatically follow any underlying terrain.

### Create Text

A mode which creates earth::geometry::Text instances within the scene.

The left mouse button will create a new text instance at the clicked
location, with the value 'Test Text'.

### Create Symbol

A mode which creates earth::geometry::Symbol instances within the scene.

The left mouse button will create a new symbol instance at the clicked
location, displayed as a MapLink vector symbol.

### Create Extruded Polygon

A variant of the polygon mode which creates extruded primitives. These
primitives are not draped over the terrain but are extruded to form 3D
volumes.

The left mouse button will start a new primitive or add points to the
in-progress one. The right mouse button will finish creation of the
primitive and add the final version into the scene.

### Create Extruded Polyline

A variant of the polyline mode which creates extruded primitives.

These primitives are not draped over the terrain but are extruded to
form vertical walls.

The left mouse button will start a new primitive or add points to the
in-progress one. The right mouse button will finish creation of the
primitive and add the final version into the scene.

### Delete Geometry

A mode which deletes geometry primitives from the scene.

Clicking the left mouse button on a geometry instance will remove it
from the scene.

This interaction will have no effect on tracks.

## API usage

### Layer loading

To load a map file the user needs to do the following:

- Create a TSLMapDataLayer;

- Call loadData on the layer and provide the path to the .map file;

- Add the layer to the earth::Surface3D.

See CEarthSampleDoc::loadMapLayer and CEarthSampleView::addDataLayer in
the EarthSample project for usage examples.

### Terrain Loading

To load a Terrain database into the scene, the user needs to:

- Create a TSLTerrainDatabase;

- Call the open function on the database, providing a path to the
  database file;

- Add the database to the earth::Surface3D.

See CEarthSampleDoc::loadTerrainDatabase and
EarthSampleView::addTerrainDatabase in the EarthSample project for usage
examples.

### Camera Movement

To update the camera, the user needs to do the following:

- Query the camera from the earth::Surface3D;

- The position of the camera and other such variables can be updated by
  calling the relevant functions on the class;

- To set the camera's target position, the easiest way is to use the
  lookAt function which sets the camera's eye and target position
  simultaneously, with roll angle as an additional option.

See CCameraControlFormView::updateCamera in the EarthSample project for
usage examples.

### Track Management

To simulate tracked objects on the globe, the user needs to:

- Create earth::TrackSymbol visualisations, which define how a Track
  will be rendered;

- Create earth::Track objects that use those visualisations, and store
  them for later use;

- Add each Track to the earth::Surface3D (which will use a pointer to
  the original Track objects);

- The Tracks can then be updated at run time using the variable and
  attribute functions on the Track objects.

See CEarthSampleDoc::initialiseTracks, CEarthSampleView::addTracks, and
CEarthSampleDoc::updateTracks for usage examples.

### Managing Geometry

To display geometry, the user must first configure a Style. This concept
is similar to 'feature rendering' within the Core SDK but provides a
distinctly different set of rendering parameters.

- A style is defined by an instance of the earth::geometry::Style class;

- Unlike the Core SDK a default style is provided. This is the initial
  state of the Style class, and will be used if a geometry references an
  unknown/invalid style on the surface;

- Once configured the user must pass the style to Surface3D::setStyle.

The set of styles may be configured independently on multiple surfaces.
If a geometry instance is present in multiple surfaces it will be
rendered according to the style on each one.

Once a style is configured geometry may be created by:

- Creating an instance of earth::Geometry, such as a Polygon or
  Polyline;

- Defining the primitive's coordinates;

- Setting the styleName parameter of the Geometry to the name of a
  style;

- Passing the Geometry instance to Surface3D::addGeometry.

Once added to the surface the geometry may be updated at any time, and
the scene will be refreshed automatically to reflect this.

Note that very frequent updates to the primitive or to the styles may
cause a performance loss, so these should be kept to a minimum. The
CreatePolygonInteraction and CreatePolylineInteraction classes within
the sample demonstrate a technique to reduce this impact by performing
most of the geometry creation with a much simpler style (e.g. one that
has less detailed draping and tessellation options).

As with Tracks the application is responsible for memory management of
Geometry instances.



---

[← Terrain SDK](terrain-sdk) | [Editor SDK →](editor-sdk)
