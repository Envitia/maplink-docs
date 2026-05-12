---
title: "Threading"
---

# Threading


This section applies to the Core SDK, Terrain SDK, 3D SDK, Accelerator
SDK and Dynamic Data Object SDK only. With other SDKs ensure that you do
not share objects across threads.

Introducing multi-threading complicates matters as MapLink is not
completely thread safe. This is principally to ensure maximum
performance.

You should review the whole of this section if you are going to use
MapLink in multiple threads.

If you are using MapLink for drawing in multiple threads, then you may
need to use the following methods:

- TSLUtilityFunctions::getThreadedOptions

- TSLUtilityFunctions::setThreadedOptions

The following classes have been updated to provide additional functions
which do not store results in static data:

- TSLCoordinateConverter

- TSLProfileHelper

- TSLPathList

- TSLCoordinateConverter

- TSLFileLoader

- TSLInteropConfig

- TSLInteropExportSet

- TSLInteropImportSet

The following methods are no longer static:

- TSLMapDataLayer::setRuntimeProjectionParameters (C++ /.NET)

- TSLAPPSymbol::write

## Known Threading Issues

The following are known not to be thread-safe and you should stop all
threads before performing any of the following (PLEASE read the
following sections as well):

- Any method noted as Deprecated by the compiler should be updated to
  use the new replacement method.

- Loading and adding CoordinateSystems and CoordinateSystem registries.

- Static setter methods are not thread safe. For example, you should
  make sure that if you set your own loader or pathlist on the Drawing
  Surface that this occurs before your application starts any threads
  using MapLink (or stop all threads using MapLink outside of MapLink
  methods).

- Don\'t share Display connections between threads on X11. Resources are
  keyed on the Display.

- Seamless Layer Manager is not thread safe.

- Flashback is not thread safe.

- History is not thread safe.

- DBIF is not thread safe.

- Entity Store SDK is not thread safe.

- S63 SDK is not thread safe when saving data.

- Don\'t setup a Persistent cache with shared layers.

- Sharing Drawing surfaces between threads is not safe.

- TSLErrorStack interface is not thread safe, use the
  TSLThreadedErrorStack.

The following Core SDK methods and classes are also known not to be
thread safe. If you need to call the methods from a multi-threaded
context protect the calls and copy the results immediately.

- TSLCompareHelper

- TSLVariant::id (use getID)

- TSLMapDataLayer::getPaletteFilename

- TSLMapDataLayer::getPathlistFilename

- TSLMapDataLayer::getDetailLayerName

- TSLMapDataLayer::getOverviewLayer

- TSLMapDataLayer::metadata

- TSLErrorStack::first (use TSLThreadedErrorStack)

- TSLErrorStack::index (use TSLThreadedErrorStack)

- TSLErrorStack::lastError (use TSLThreadedErrorStack)

- TSLErrorStack::next (use TSLThreadedErrorStack)

- TSLErrorStack::previous (use TSLThreadedErrorStack)

- TSLProfileHelper

- TSLInteropConfig::basefilename

- TSLInteropConfig::groupingAttribute

- TSLInteropExportSet::item

- TSLInteropImportSet::item

- TSLMapDataLayer::copyRasterFeatures

- TSLSeamlessLayerManager::setMapLinkVersion

- TSLUtilityFunctions::sav( int arg )

- TSLPathList::getMatchingDirectories

  (use getMatchingDirectoriesMT)

## Threading Options

Several threading options can be set or cleared when using MapLink.
Currently the only one that you should consider using is the
TSLThreadedOptionsRenderingSupport (also see
[29.5.2](#drawing-surface-rendering)).

The threading options may be set and queried using the following
methods:

- TSLUtilityFunctions::setThreadedOptions

- TSLUtilityFunctions::getThreadedOptions

## Saving Data

MapLink allows you to save data as the current version or as a previous
version.

The setting of the version is not local to a layer but is stored
globally, because of this we currently take a global lock to ensure data
is written out in the correct version.

## Drawing Surface ID

The drawing surface ID that the user can set is no longer used by
MapLink. We now create a unique value internally.

The user ids must be positive values. If the user does not set one the
internal unique id is returned as a negative number.

## CoreSDK

The following notes are based upon our experiencing of using MapLink in
multiple threads.

### Drawing Surface Resource Loading

In general, you should setup the Drawing Surface resources before your
application goes multi-threaded. The line-styles, fill-styles, fonts and
symbols are a shared resource and take time to load. The loading is
thread-safe however the propagation of the new resources is lazy and
only occurs on a draw.

Note: Delayed loading of resources is not thread-safe.

### Drawing Surface Rendering

While in general the drawing is thread safe you should avoid sharing
layers between threads (see [29.5.4](#data-layers-1)).

If you wish to share the TSLStandardDataLayer (see
[29.5.4.1](#standard-data-layer-1)) between threads then you need to
call TSLUtilityFunctions::setThreadedOptions to set the bit represented
by TSLThreadedOptionsRenderingSupport.

### Coordinate System Resource Loading

The loading of the Coordinate System information
(TSLCoordianteSystem::loadCoordinateSystems) is not thread safe and
therefore the coordinate systems should be loaded before the application
uses MapLink in a threaded manner. A map loads and creates a coordinate
system local to the layer so it is not strictly necessary to load all
the Coordinate Systems unless you need to convert between different
projections.

### Data Layers

The following types of data layers must not be shared between threads:

- Map Data Layers

- CADRG Data Layers

- Raster Data Layers

- WMS Data Layers

- Filter Data Layers

- All Grid Data Layers

- ECW Layer

- Dynamic Object Data-layer and the Display Objects

Adding or removing a layer from a drawing surface is not thread safe.
Stop all drawing surfaces that the layer is to be added to or removed
from before adding or removing.

#### Standard Data Layer

Sharing the standard 2D data-layer is safe as long as the Drawing
Surface IDs are different for each thread (see
[29.5.2](#drawing-surface-rendering)).

You must not edit (add or remove entities) the layer unless you stop the
drawing in all threads the layer has been added too.

The changing of rendering styles is permitted, though the updating of
the drawing maybe delayed.

#### Custom Data Layer

It is the responsibility of the developer to ensure that the layer is
thread-safe.

If you are adding a Custom 2D Data Layer to an Accelerator or 3D
surface, you should note that the layer will be called from a
back-ground thread.

### Dynamic Rendering

It is the responsibility of the developer to ensure that the dynamic
renderer is thread-safe.

If you are adding a dynamic renderer to an Accelerator or 3D surface
then you should note that the layer will be called from a back-ground
thread

### TSLPathList

TSLPathList is not thread safe unless the application takes the
following measures:

1.  Do not use the callback.

2.  If you are setting up a pathlist for the Drawing Surfaces to use;
    Set up the drawing surface pathlist object and add this to the
    drawing surface before your application starts using multiple
    threads.

3.  If you need to change the drawing surface pathlist or modify it
    after your application has started its threads; Stop all threads
    outside of MapLink calls and do the necessary modifications.

4.  If you are setting up a pathlist for data layers; Ideally use a
    separate pathlist per map data-layer (do not share cached layers
    between drawing surfaces in different threads). If you need to share
    the pathlist between map data-layers then only modify the pathlist
    when all threads using MapLink are stopped outside of MapLink method
    calls.

## User Geometry

It is the developer's responsibility to ensure thread safety for the
user implemented functionality

## Dynamic Data Object Layer

The Dynamic Data Object Layer should not be shared between Drawing
Surfaces in different threads.

The layer and its associated objects should only be modified from the
thread containing the associated Drawing Surface.

## Terrain SDK and Contouring SDK

Terrain can be used in multiple Threads as long as the terrain layer
(TSLTerrainDatabase) is unique for each thread (not shared between
threads).

The Contouring SDK has not been used in a threaded manner and thus may
not be thread-safe. The Contouring SDK modifies the floating-point
registry to enable strict IEEE floating point and as such is unlikely to
be thread-safe.

## 3D SDK & Accelerator SDK

Both the 3D and Accelerator Drawing surfaces use a background thread for
drawing 2D layers.

The 3D SDK and the Accelerator SDK clone their Map, CADRG and WMS Data
Layers to ensure thread safety. These layers can be shared between
Drawing Surfaces in the same thread.

Other data-layers are not currently cloned and as such you should not
share these layers between multiple drawing surfaces, with the exception
of the 2D Standard Data Layer (see [29.5.4.1](#standard-data-layer-1)).
In addition, you should stop the drawing surfaces before modifying the
layers in any-way.

All data layer types, except the S63 and ECW Data-layer, should be
acceptable to the 3D SDK and Accelerator SDK. If you need to use these
layers with the 3D or Accelerator SDK please contact support.

- Drawing should always occur from the thread that created the Surface.

- Sharing Drawing surfaces between threads is not safe.

- Picking with 3D Surface is not thread safe. Picking must occur in the
  main drawing thread.

- Removing and deleting 3D entities is not thread safe. Removing and
  deleting of entities must occur in the main drawing thread.

- Deleting a layer in a thread other than the main drawing thread is not
  thread safe (deletion of OpenGL/DirectX resources will occur).

### Accelerator Drawing Surface Rendering

While in general the drawing is thread safe you should avoid sharing
layers between threads (see [29.5.4](#data-layers-1)).

If you update a layer\'s content the changes will not be reflected upon
the display until you have called notifyChanged on the surface.

### 3D Drawing Surface Rendering

While in general the drawing is thread safe you should avoid sharing
layers between threads (see [29.5.4](#data-layers-1)).

If you wish to share the TSL3DStandardDataLayer between threads, you
must call TSLUtilityFunctions::setThreadedOptions to set the bit
represented by TSLThreadedOptionsRenderingSupport. In addition, you must
add the layer to all drawing surfaces before you start any drawing and
you should not edit the layer once drawing has occurred.

Ideally you should not share the TSL3DStandardDataLayer between threads
principally because we store data upon the entities which is drawing
surface specific and the locking will affect the performance of the
drawing.

## X11 Threading

On X11 you must either serialise the calls to MapLink or use a separate
display connection for each drawing surface.

Resources are allocated on a display basis and are cached in MapLink
based on the Display as the key.

Use of separate display connections in each thread is the safe way to
use MapLink. Sharing of Display connections may appear to work until you
start using processors with multiple cores or a multi-processor system.

You should call XInitThreads() before any other Xlib calls in your
application as the Xlib library and generally the extensions are not
thread safe until this method has been called. You may need to review
the source code of the libraries you use as we know that the Xft
extension is not thread safe.

We have found that XInitThreads() is not always required if you limit
your use to Xlib and avoid Xft (or protected access to Xft methods - see
[29.2](#threading-options) and [12.6.5.1](#xft-fonts-x11)), however this
is a case of test and review the client side library source code as the
versions you are using may be very different from the ones we have used.
Additionally, we have ensured that we do not share X resources between
drawing surfaces.

The principle drawing limitation in a threaded environment is the
X-Server. The X-Server is a single process so all drawing calls will be
serialised at the X-Server. This is not necessarily a problem as MapLink
and your application may be able to do something else in the dead time.

Synchronisation calls are kept to a minimum within the X11 Drawing
Surface.



---

[← Other SDKs](other-sdks) | [DIGM to TMF Conversion →](digm-to-tmf)
