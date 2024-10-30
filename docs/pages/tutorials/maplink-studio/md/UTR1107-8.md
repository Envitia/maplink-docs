![](img/LOCAL%20COPY%20UTR1107-08%20MapLink%20Studio0.jpg)

# MAPLINK STUDIO TRAINING COURSEUTR1107-08

© Envitia Ltd 2024\. All rights reserved\.


---


# Contents

An Introduction to MapLink Pro

Essential GIS Concepts

What MapLink Studio Does

How MapLink Studio Works

Raster Data

Gridded Data

Vector Data Handling

Clipping

Terrain Databases

Cataloguing

Large Maps

MapLink Maps in Runtime

WMS

Final Summary

© Envitia Ltd 2024\. All rights reserved\.


---


# Course Objectives

The MapLink Studio Course is aimed at individuals and teams using MapLink Studio to build maps for display in an Envitia MapLink Pro\-based end\-user application\.

By the end of this course\, you should understand the following:

Essential GIS

Concepts

What MapLink

Studio Can & Can’t

Be Used For

How MapLink

Studio Works

How MapLink

Maps Are

Structured

How To Build Multi\-Layer Raster\, Vector\,

& Gridded Maps

How To Use

MapLink Maps

How To Build

Multi\-Layer Terrain Databases

© Envitia Ltd 2024\. All rights reserved\.


---


# Course Materials

Containing an

overview of MapLink Studio and its uses

Sample projects

and data copied

onto your PC

Containing

detailed information and exercises

__Note__ : Please annotate your course materials where appropriate

They will provide a reference after the course\!

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio1.jpg)

# Introduction to MapLink Pro

© Envitia Ltd 2024\. All rights reserved\.


---


# What is MapLink Pro?

© Envitia Ltd 2024\. All rights reserved\.


---


© Envitia Ltd 2024\. All rights reserved\.


---


# Keys & Licensing

* __MapLink Developer Licence__ :
  * Gives access to MapLink Studio and the developer libraries
  * Gives the user the ability to develop an application based on MapLink
* __MapLink Studio Licence__ :
  * Gives a user access to the map preparation environment
* __MapLink Run\-Time License__ :
  * Allows an application linked in release mode against the MapLink libraries to be run
  * Currently not keyed
* Specific options \(map import filters\, SDK options\) are licensed separately as add\-ons
* MapLink Studio deployments\, and specific options are protected by node locked licence keying
* _Any requests/questions related to licensing or any other questions? Contact Envitia support:_
* _ _  _Phone_  _: \+44 1403 273173_
* _Email_  _: support@envitia\.com_

© Envitia Ltd 2024\. All rights reserved\.


---


# System Requirements

* __Runtime Environment__ :
  * Windows / Linux / Android
  * 64\-bit
  * Minimum of 65k colours on Windows
  * Generated maps can be used on both Windows and Linux platforms
  * Map cache size controllable

* __MapLink Studio__ :
  * Available on 64\-bit Windows only
  * Operates best with significant amounts of processor/disk/memory

© Envitia Ltd 2024\. All rights reserved\.


---


# Documentation & Examples

* __MapLink Studio Help__ :
  * An extensive resource on all details of Studio and map processing
  * Includes both reference\, and guides to using the features
* __MapLink Studio User Guide__ :
  * Under the MapLink Documentation menu
* __MapLink Studio Examples__ :
  * Example projects and the resulting maps can be found in “\[INSTALLROOT\]\\Envitia\\MapLink Pro\\\<version>\\Projects” and “\\Maps”
* __Sample Data__ :
  * Can be found in “\[INSTALLROOT\]\\Envitia\\MapLink Pro\\\<version>\\Data”
* __MapLink API Documentation__ :
  * [https://www\.envitia\.com/technologies/products/maplink\-pro/userguide/index\.html](https://www.envitia.com/technologies/products/maplink-pro/userguide/index.html)

© Envitia Ltd 2024\. All rights reserved\.


---


# Supported Data Formats

__Supported Data Formats__

© Envitia Ltd 2024\. All rights reserved\.


---


| Vector | Raster | Gridded |
| :-: | :-: | :-: |
| DIGEST VPF  (VMap0,1,2,UVMap,DNC etc.) | ADRG | ArcGrid ASCII (ESRI) |
| Envitia ASCII | CRP (Uncompressed) | ArcGrid Binary (ESRI) |
| AutoCAD DXF | BMP / JPEG / TIFF / PCX etc. | ArcGrid Float (ESRI) |
| Shapefile (ESRI) | BSB Nautical Chart Format | OS Panorama (Ordnance Survey) |
| MapInfo MIF/MID | GeoTIFF | ASCII DEM (Generic) |
| NTF (Ordnance Survey) | Geospatial PDF | DTED / DMED 0, 1, 2 |
| MasterMap (Ordnance Survey) | MrSID* | DBDBV 1, 4, 5, 6 |
| OS Vector Map Local | Other Raster* |  |
| OS Vector Map District | DIGEST RPF |  |
| OpenStreetMap | CADRG/CIB (Runtime & Studio) |  |
| U.S. Census Tiger/LINE | ASRP (ONC, TPC etc.) |  |
| File Geodatabase (FileGDB)* | NSIF / NITF 2.1 |  |
| GML2/GML3 Simple Features | ECRG |  |
| KML Simple Features | USRP |  |
| Other Vector* |  |  |
| DAFIF-Tabbed |  |  |
| DFAD |  |  |
| S-57 AML / ENC |  |  |
| S-57 AML / ENC for S-52  |  |  |
| GDF |  |  |
| NSIF / NITF 2.1 (CGM) |  |  |
| Jeppesen ARINC 424 NavData  |  |  |

__Note__ : Formats in bold are standard filters

\*User needs to download 3rd party DLLs\. Please refer to MapLink Studio Help for additional information

© Envitia Ltd 2024\. All rights reserved\.


---


# Why MapLink Studio?

Therefore\, MapLink Pro offers the option to process all this data before it is loaded into the runtime application\.

All data format parsing\, clipping\, filtering and decluttering is completed ahead of runtime\.

All styling decisions are implemented before runtime\.

All coordinate system transformations and reprojections are performed before runtime\.

__So that your map is optimised for runtime performance in the end\-user application__ \.

MapLink Pro supports many geospatial data formats\.

A MapLink Pro\-based application can simultaneously display data from many datasets\, in different data formats and types\, in different coordinate systems\.

All this data must be parsed\, clipped\, filtered\, decluttered\, reprojected\, styled…\.

To do all this at runtime \(i\.e\. in the end\-user’s application\) takes time and affects performance\.

© Envitia Ltd 2024\. All rights reserved\.


---


# What is MapLink Studio?

© Envitia Ltd 2024\. All rights reserved\.


---


# What MapLink Studio Isn’t

© Envitia Ltd 2024\. All rights reserved\.


---


# MapLink Studio Workflow

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio2.png)

Output Map / Terrain Database

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio3.png)

Geospatial data is loaded into MapLink Studio\.

Data is processed in MapLink Studio\, be that vector styling\, clipping\, filtering\, etc\.

Data is exported as a MapLink Map or Terrain Database for use as needed\.

© Envitia Ltd 2024\. All rights reserved\.


---


# MapLink Pro Components

Studio User Interface

\(Interactive Mode\)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio4.png)

Active X Control

User Application

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio5.png)

Studio Batch File

Studio Automation Interface

MapLink Run\-Time SDKs

C\+\+ / \.NET / Com

Run\-Time Map

\(Vector & Raster\)

Vector

E\.g\.: VMap

MapLink Pro Studio Engine

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio6.png)

Raster

E\.g\.: CADRG

Run\-Time Terrain

Terrain

E\.g\.: DTED

Run\-Time Network

Specialist Imports

© Envitia Ltd 2024\. All rights reserved\.


---


# Other Useful MapLink Tools

© Envitia Ltd 2024\. All rights reserved\.


---


# Introduction to MapLinkSummary

MapLink Studio is the tool provided with MapLink Pro that performs all the geospatial data processing ahead of runtime

__So that your map is optimised for runtime performance in the end\-user application__ \.

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio7.jpg)

# GIS Concepts

© Envitia Ltd 2024\. All rights reserved\.


---


# Glossary1 of 3

* __Great Circle__ :
  * Any circle on the surface of a sphere formed by the intersection of the surface with a plane passing through the centre of the sphere
  * It is the shortest path between any two points on the circle
  * Thus\, the shortest path between any two points on the sphere\, follows the great circle connecting the two points
  * Obviously important for navigation
* __Small Circle__ :
  * Any circle on the surface of a sphere formed by the intersection of the surface with a plane not passing through the centre
  * For example\, non\-equatorial lines of latitude are small circles

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio8.png)

© Envitia Ltd 2024\. All rights reserved\.


---


* __Meridian__ :
  * A reference line on the Earth’s surface formed by intersection of the surface with a plane passing through both poles and some third point in the surface
  * Lines of longitude are Meridians\, but lines of latitude are not
* __Parallel__ :
  * Small Circle on the surface of the Earth formed by the intersection with a plane parallel to the plane of the equator

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio9.png)

© Envitia Ltd 2024\. All rights reserved\.


---


* __Loxodrome / Rhumb Line__ :
  * A complex curve on the surface of the globe that crosses every meridian at the same angle
  * Can navigate between any two points along a rhumb line by maintaining a constant bearing
* __Graticule__ :
  * Network of lines representing a selection of the Earth’s parallels and meridians

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio10.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Geodetic Datums

* The globe is not perfectly spherical\, it’s an  __oblate spheroid__ \, with additional distortions added due to the topography of the surface
  * A squashed sphere\, with added mountains and valleys\!
* There have been many different measurements of the shape of the globe over the centuries\, normalised to a perfectly smooth surface
  * These are termed  __Reference Ellipsoids__
* Cartographers need to understand which model of the globe their positions are being measured against
  * Assuming the wrong one can cause severe inaccuracies
* The Reference Ellipsoid isn’t enough by itself\.  It must have an origin somewhere\, either at the centre of the globe or at a position on the surface
  * Origins are called the Fundamental Point
* The Reference Ellipsoid combined with the Fundamental Point form a ‘Geodetic Datum’

© Envitia Ltd 2024\. All rights reserved\.


---


# Datum Transformations

Lat / Long Discrepancy

Even using the same Reference Ellipsoid with a different Fundamental Point can lead to errors

WGS84 and other modern worldwide Datums use the centre of the globe as the origin

Datum Transformations define how to convert a position in one Geodetic Datum into another Geodetic Datum\, taking the lat / long discrepancy into account

Several different methods ranging from simple x\,y\,z adjustment to complex iterative equations that are specific to a particular country

MapLink makes extensive use of Datum Transformations to and from WGS84

Fundamental Points

Earth Model Sphere\(oid\)s

© Envitia Ltd 2024\. All rights reserved\.


---


# Coordinate Reference Systems

* Coordinate Reference Systems \(CRS\):
  * Sometimes known as Spatial Reference Systems \(SRS\)
  * Projection \+ Datum \+ Transformation = CRS
  * Define how the two\-dimensional\, projected map in your GIS relates to real places on the earth\.
  * Which map projection and CRS to use depends on the regional extent of the area you want to work in\, on the analysis you want to do\.

* Map Projections:
  * Portray the surface of the earth\, or a portion of the earth\, on a flat piece of paper or computer screen\.
  * Transform the earth from its spherical shape \(3D\) to a planar shape \(2D\)\.
  * More detail to follow…

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 1Coordinate Reference Systems

This exercise shows:

Selecting existing coordinates systems for a map

Showing the effect of different coordinate systems

Defining new coordinate systems

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Projections

* The mathematical equations used to transform a point measured against a Geodetic Datum into a 2D Cartesian space are called   __Map Projections__
  * The equations have parameters to define the 2D coordinate origin and other important measurements in the 2D Cartesian space or locations in 3D Geodetic space such as reference lines of latitude or longitude
  * MapLink calls the equations  __Map Projection Types__
  * MapLink only terms them as  __Map Projections__  when the parameters are known
* The equations for a  __Perspective__  projection work by projecting straight lines from a specified point \(or infinity\)\, through points on the surface
* Some projections can only apply to a spherical Earth Model\, not an ellipsoidal Earth Model
* Each Map Projection has its own properties which affect the circumstances in which it is useful
  * There will always be a distortion of some sort
  * The trick is to accentuate the properties you care about

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Projection PropertiesOverview

* An Equal\-area projection correctly represents areas of the globe on the map\.
  * A coin placed anywhere on the map covers as much of the area of the surface of the globe as it would anywhere else on the map
* An Equidistant projection can\, to a limited degree\, show true scale between points on the map\.
  * Typically\, only distances from the origin or along a meridian
* An Azimuthal projection can show correct angles from a central point
  * Rarely from two points
* A Conformal projection has all angles at infinitely small locations correct
  * Thus\, it preserves shape
  * Increasing distortion away from the lines of true scale or origin

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Projection PropertiesContinued

It is impossible to have all properties in a single map

It is possible to have certain pairs of properties in a single map\, as shown in the table below:

In summary\, any map will distort areas\, shape\, directions or distances to some extent

Choose the one that minimises distortion in the property and location you are interested in

Some Map Projections have specific useful properties\, discussed later

|  | Conformal | Equal Area | Equidistant | Azimuthal |
| :-: | :-: | :-: | :-: | :-: |
| Conformal | - | No | No | Yes |
| Equal Area | No | - | Yes | Yes |
| Equidistant | No | Yes | - | Yes |
| Azimuthal | Yes | Yes | Yes | - |

© Envitia Ltd 2024\. All rights reserved\.


---


# Tissot Indicatrix

It is possible to analyse the distortions of a Map Projection using the ‘Tissot Indicatrix’

Circles represent same size areas on the global surface\, lines represent graticules of latitude and longitude

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio11.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio12.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio13.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio14.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio15.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Projection Classifications

* There are further classifications of Map Projection\, based upon how they are constructed:
* __Cylindrical__ :
  * Normal\, Transverse\, Oblique\, and Secant
  * Pseudo\-cylindrical
* __Conic__ :
  * Normal\, Oblique\, and Secant
  * Pseudo\-Conic
  * Polyconic
* __Azimuthal__ :
  * Tangent
  * Secant
  * Modified Azimuthal

© Envitia Ltd 2024\. All rights reserved\.


---


# Cylindrical Map Projections

__Cylindrical__  projections wrap a piece of paper in a cylinder around the globe and then cast a ray through the 3D positions onto the cylinder\, then unwrap the paper

Depending upon the orientation of the cylinder\, these are termed  __Normal__ \,  __Transverse__ \, or  __Oblique__

If the cylinder is the same radius as the globe\, then it is  __Tangent__

If the cylinder is smaller than the globe\, then it touches at two small circles and is termed  __Secant__

There is also the  __Pseudo\-Cylindrical__  type\, which is not perspective

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio16.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Conic Map Projections

__Conic__  projections wrap a piece of paper in a cone around the globe and then cast a ray through the 3D positions onto the cylinder\, then unwrap the paper

Depending upon the orientation of the cone\, these are termed  __Normal__  or  __Oblique__

If the cone touches the globe at a single small circle\, then it is  __Tangent__

If the cone intersects the globe\, then it touches at two small circles and is termed  __Secant__

There is also the  __Pseudo\-Conic__  type\, which is not perspective\, and the  __Polyconic__  type\, which behaves as if multiple cones were used

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio17.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Azimuthal Map Projections

__Azimuthal__  projections place a piece of flat paper touching globe and then cast a ray through the 3D positions onto the paper\.  The ray can come from a specified point\, or infinity to produce different variants\.

Depending upon the orientation of the paper\, these are termed  __Normal__  or  __Oblique__

If the paper touches the globe at a single point\, then it is  __Tangent__

If the paper intersects the globe\, then it touches at a small circle and is termed  __Secant__

The  __Modified Azimuthal__  projections have similar properties\, but no simple geometric construction

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio18.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Projection Resources

* There are hundreds of different Map Projections that have been devised through the ages
* Many are no longer used\, or have limited situations in which they are useful
  * Some have been created for fun\!
* Useful resources for Map Projections:
* “An Album of Map Projections”
  * USGS Professional Paper 1453 \(Snyder and Voxland\)
  * Diagrams\, usage and history of around 130 projections
  * Limited maths
* “Map Projections – A Working Manual”
  * USGS Professional Paper 1395 \(Snyder\)
  * Full equations and mathematical details for around 26 common projections
  * PDF available free from USGS Publications Warehouse

© Envitia Ltd 2024\. All rights reserved\.


---


# Mercator Projection

* Cylindrical
* Conformal
  * Ellipsoidal and Spherical forms available
* Rhumb lines are straight
* Used for navigation
  * Often inappropriately used for world maps in atlases\!

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio19.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Transverse Mercator Projection

* Transverse aspect of Mercator
* Cylindrical
* Conformal
  * Ellipsoidal and Spherical forms available
* Distortion increases away from central meridian
* Usually too inaccurate after \+/\- 6 degrees
  * Recommended for north\-south extents
* Widespread usage\, basis for:
  * UTM grid
  * British National Grid

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio20.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Sinusoidal Projection

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio21.png)

* Pseudo\-Cylindrical
* Equal\-area
* Equally spaced parallels
  * Ellipsoidal and spherical forms available
* Used for Atlas maps of Africa and South America
  * Occasionally used for world maps in atlases
* Can be ‘Interrupted’ to have several segments

© Envitia Ltd 2024\. All rights reserved\.


---


# Albers Equal-Area Conic Projection

* Conic
* Equal\-Area
  * Needs two standard parallels in construction
* Used for US National Atlas and thematic maps
* Recommended for equal area display of E\-W extents

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio22.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Lambert Conformal Conic Projection

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio23.png)

* Conic
* Conformal
  * Available in Ellipsoidal or Spherical forms
* Extensively used for large scale E\-W extents
  * Used for US State 1:500\,000 scale
  * Recommended for conformal mapping of E \- W extents
  * Not suitable for global coverage\!

© Envitia Ltd 2024\. All rights reserved\.


---


# Gnomonic Projection

* Azimuthal
* Perspective
* Only Spherical Form available
  * Can only display less than one hemisphere
* All Great Circles are straight lines
* Used for navigation
  * Significant distortion of scale and area

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio24.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Orthographic Projection

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio25.png)

* Azimuthal
* Perspective
* Only Spherical Form available
  * Can only display less than one hemisphere
* All great or small circles are elliptical arcs or straight lines
* Looks like a globe\!
* Used for pictorial views of the earth from space

© Envitia Ltd 2024\. All rights reserved\.


---


# Stereographic Projection

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio26.png)

* Azimuthal
* Perspective
* Conformal
  * One hemisphere displayed\, accelerating distortion after
* All great or small circles are elliptical arcs or straight lines
* The basis for UPS
  * Polar equivalent of UTM
* In spherical form\, directions from centre are true
  * Recommended for conformal mapping of circular areas

© Envitia Ltd 2024\. All rights reserved\.


---


# Lambert Azimuthal Equal Area Projection

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio27.png)

* Azimuthal
* Equal Area
  * Both Spherical and Ellipsoid forms available
* Can display global coverage
* Used for Polar and single hemisphere maps
  * For all spherical and polar ellipsoidal forms\, directions from centre are true

© Envitia Ltd 2024\. All rights reserved\.


---


# GIS Data Types

There are three different types of GIS data that MapLink supports:

Consists of geometric objects\, such as lines\, areas\, points and text objects\, each containing one or more geographic positions\. Each object typically represents a single real\-world feature\. Often\, each object has related data attributes with further information\.

An image made up of pixels\. Rectangular\, but can be masked\. Can be synthetic\, scanned paper or aerial/satellite images\. Generally\, the term ‘imagery’ is used for photographic rasters\. Difficult to separate real world features automatically\.

Set of geographic positions with associated data\, e\.g\.: Elevation\. Can be based on a regular grid of positions or irregular network\.

© Envitia Ltd 2024\. All rights reserved\.


---


# GIS ConceptsSummary

The globe is an oblate spheroid\.

Map projections attempt to transform the oblate spheroid to a 2\-dimensional “flat Earth” for display on the screen\.

No projection or CRS is perfect in all scenarios\.

Which map projection and CRS to use depends on the regional extent of the area you want to work in\, and on the analysis you want to do\.

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio28.jpg)

# What MapLink Studio Does

© Envitia Ltd 2024\. All rights reserved\.


---


# Introduction

Recap:

MapLink Studio is the tool provided with MapLink Pro that performs all the geospatial data processing ahead of runtime

__So that your map is optimised for runtime performance in the end\-user application__ \.

© Envitia Ltd 2024\. All rights reserved\.


---


# MapLink Studio ConceptsSummary

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio29.png)

Output Map / Terrain Database

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio30.png)

Input Coordinate System

Input Clipping

Feature Masking

Format Configuration

Thumbnail Raster View

Processing Options

Output / Geodetic Clipping

Rendering \(Feature Book\)

Output Coordinate System

Attribute Collection

Tiling

Filtering

Layering

Layer Loading Strategy

Vector Optimisation

© Envitia Ltd 2024\. All rights reserved\.


---


# Coordinate Spaces

* MapLink Studio is concerned with two types of  __Coordinate Space__ :
* __Geodetic Space__  \(3D Latitude / Longitude / Altitude\):
  * The digital equivalent of the globe
  * The real world\!
* __Cartesian Space__  \(2D X / Y\):
  * The digital equivalent of the paper map
* Cartographers or Geographic Information Systems need to transform a position in Geodetic Space into Cartesian Space to represent it on paper or screen:
  * This is impossible to do without some distortion

© Envitia Ltd 2024\. All rights reserved\.


---


# Coordinate Spaces & Systems

* MapLink supports three key coordinate spaces:
  * Geodetic \(latitude / longitude / altitude\)
  * Cartesian Projected Coordinates \(Map Units and User Units \(scaled map units\)\)
  * Device Units \(Pixels\)
* All of these can be used at runtime
  * The runtime map retains the conversion details
* MapLink Studio is mostly concerned with Geodetic and Cartesian coordinate spaces
* MapLink supports a range of standard coordinate systems and custom defined systems based on supported projections and datums
* Data can be used in any coordinate system\, for example\, mix data in British National Grid with data in WGS\-84 and UTM \(or dynamic or semi\-dynamic\)
* Vector\, raster\, and gridded data can be projected from any coordinate system to any other coordinate system

© Envitia Ltd 2024\. All rights reserved\.


---


# Isomorphic or Dynamic ARC Projection

* The ARC Coordinate system is commonly used in military mapping
* For example\, both ASRP and CADRG maps use this system
  * The projection uses the Equal ARC Second coordinate system
  * This is a multi\-zoned coordinate system which changes in steps with latitude
* MapLink has a Dynamic version of this which is applied in the run\-time
  * This projects a reasonable compromise for World maps

© Envitia Ltd 2024\. All rights reserved\.


---


# Dynamic ARC ProjectionAt Equator

Uncorrected and Corrected Displays at 0 degrees \(Equator\):

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio31.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio32.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Dynamic ARC ProjectionAt 60 North

Uncorrected and Corrected Displays at 60 degrees North:

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio33.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio34.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# MapLink Coordinate System

In MapLink\, a combined Datum\, Projection\, and Linear Transformation form a Coordinate System

The map has a single Output Coordinate System

Each dataset has an optional Input Coordinate System \(more on this later\)

Fundamental Point

Linear Transformation

Coordinate System

© Envitia Ltd 2024\. All rights reserved\.


---


# Coordinate Systems Database

* MapLink has a built\-in database of standard Coordinate Systems:
* Also\, standard components of Coordinate Systems
  * Ellipsoids
  * Fundamental Point
  * Datums
  * Projection Types
  * Projections
* The database is constructed from the international standard EPSG Database
  * European Petroleum Survey Group
  * [www\.epsg\.org](http://www.epsg.org/)  or [www\.epsg\-registry\.org](http://www.epsg-registry.org/)
* Also possible to create a custom Coordinate System
* The Coordinate System definitions are used to unproject source data into raw WGS84 and then project into the desired Coordinate Space
  * Held in the configuration file ‘tsltransforms\.dat’

© Envitia Ltd 2024\. All rights reserved\.


---


# Selecting a Coordinate System

* There is no perfect Coordinate System\, the choice is usually driven by the purpose of the map
* Displaying a view of a particular geographic area
  * Usually a standard system\, e\.g\. British National Grid
  * UTM Zone
* Displaying a map to emphasise a particular property
  * May need to be conformal or equal area
  * Avoid gross distortions
  * Custom Coordinate System if necessary
  * Cannot create custom Datum or Ellipsoid
  * Cannot create custom Projection Type \(i\.e\.: the equations\)
* Dynamic Arc is a reasonable compromise for Worldwide usage
* If the Coordinate System depends upon choices made in the run\-time\, then Full Dynamic Run\-time Projection is required
  * More later
  * Ensure no production map uses “Default Coordinate System”

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Coordinate System Interface

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio35.png)

* Coordinate systems are chosen via the coordinate system GUI
* You can:
  * Select an existing coordinate system
  * Edit a custom or default editable coordinate system
  * Copy and modify an existing coordinate system
  * Define a new coordinate system using the wizard
  * View coordinate system properties

© Envitia Ltd 2024\. All rights reserved\.


---


# Dynamic Projection Options

* Dynamic Projection is ideal for accurate Worldwide coverage
* MapLink supports two types of Dynamic Projection:
  * Dynamic ARC
  * Full Dynamic Projection
* For Dynamic ARC Projection select:
  * Coordinate Systems | Worldwide | Dynamic ARC | Dynamic Arc Grid
* For Full Dynamic Projection \(WGS84 Datum\) select:
  * Coordinate Systems | Default Run\-time Projection Coordinate System

© Envitia Ltd 2024\. All rights reserved\.


---


# Accuracy and Resolution

* MapLink’s core projection mathematics has high accuracy
  * Tested against independent data
* Take a lat / long point\, forward project\, and then inverse project
  * Resulting lat / long accurate to within 10\-7 % of the original lat / long
* With datum transforms\, positional accuracy is typically a centimetre or better
  * Limited by datum transform parameters
  * Spherical datums can cause inaccuracy
* Coordinates stored as fixed\-point numbers
  * Gives well defined accuracy and efficiency of storage
  * 2cm resolution if global coverage assumed
* MapLink dynamically selects fixed\-point or floating\-point mathematics to balance accuracy and performance of map display

© Envitia Ltd 2024\. All rights reserved\.


---


# Data Source Coordinate Systems

* Many sources of digital map data use Geodetic positions
  * Often military vector data
* Some digital map data formats are defined in specific non\-geodetic Coordinate Systems
  * Often military raster data
* Digital map data from National Mapping Agencies is often in the National Grid System of the specific country
  * Ordnance Survey data is in British National Grid
* How does MapLink deal with this?
  * Using Input Coordinate Systems

© Envitia Ltd 2024\. All rights reserved\.


---


# Choosing an Input Coordinate System

* There are four possible situations for the input coordinate system:
  * Source data is in lat / long and WGS84 => Use the Default Dataset Coordinate System
  * Source data is in a format for which MapLink automatically sets the input coordinate system \(because it is available from the source\)\, e\.g\.: ASRP => Use the Default Dataset Coordinate System
  * Source data is in a known coordinate system\, but it is not set automatically => Define and select the correct Dataset Coordinate System
  * Source data is in an unknown coordinate system => Contact your data supplier\!
* Note the coordinate system can only be set on the Dataset not on a data file and thus rasters in different coordinate systems need to be added in separate datasets

© Envitia Ltd 2024\. All rights reserved\.


---


# Input & Output Coordinate SystemsWhat if They’re the Same?

* Sometimes the input data is already in the Coordinate System that you want to use for the output map
* How should you configure your MapLink project in this situation?
  * Don’t add any Coordinate System?
  * Add an Output Coordinate System?
  * Add an Input Coordinate System?
  * Add both an Output and Input Coordinate System?
* The Answer?
  * Add both an Output and Input Coordinate  System
  * MapLink will identify that they are both the same and not actually perform the projection
* Why?
  * Because without this information MapLink cannot convert to and from geodetic coordinates in the run\-time application

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Units and TMCs

* Map units are the units that are used by the Coordinate Space in the final map
  * Commonly\, map units are defined in nominal metres\, ignoring the distortion introduced by the projection type
  * They have a floating\-point precision\, e\.g\.: 20\.34
* TMCs \(TENET Mapping Coordinates\):
  * MapLink’s internal co\-ordinate system
  * They have fixed point precision\, i\.e\.: integer\, for optimisation reasons
  * The limit of the type used to store TMCs means that the maximum resolution of a map displaying the whole world is 1cm\, i\.e\. 100 TMC per metre \(map unit\)
* The map resolution is the minimum size that a pixel can represent
* By default\, MapLink chooses an appropriate mapping between Map units and TMC depending on the map displayed
  * In the Advanced panel of your Map\, the Automatic option is set

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Unit to TMC Transformation

* It is good practice to always set manual scaling from map units to TMC; as a guide:
* For an area representing the whole world
  * Set a TMC per Map Unit of 50
  * I\.e\.: 2cm resolution
* For British National Grid or similar sized area
  * Set a TMC per Map Unit of 1000
  * I\.e\.: 1mm resolution
* There is no need to apply Map Unit Shift values

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio36.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 2Create a Basic Vector Map

This exercise shows:

Creating a project

Adding a layer\, dataset\, and data item into the project

Previewing the data with the default colour & style

Creating a map for use in a runtime application

© Envitia Ltd 2024\. All rights reserved\.


---


# Optimisation

MapLink can create maps with the appropriate resolution and content for the zoom factor and so allow fast pan and zoom to virtually infinite map data sets\, using the following optimisation methods:

__Feature Masking__ : The removal of unwanted feature types from a map

__Layering__ : Displaying different levels of detail at different zoom levels

__Tiling__ : Breaking a layer into tiled grids so the whole layer needn’t be loaded all at once

__Clipping__ : Removal of data that falls outside the area of interest

All these optimisation methods are covered in more detail later

© Envitia Ltd 2024\. All rights reserved\.


---


# Attribution

Features within input data \(especially in vector data\) generally have attributes associated with them\, for instance a built\-up area may include the following information:

Name

Population

County / State / Province

Etc

Attribution and the ways attributes can be used is covered in more detail later

© Envitia Ltd 2024\. All rights reserved\.


---


# Supporting Information

The following information is useful if a support issue arises:

Message log file

MapLink Pro version

Details of any installed patches

© Envitia Ltd 2024\. All rights reserved\.


---


# What MapLink Studio DoesSummary

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio37.png)

Output Map / Terrain Database

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio38.png)

Input Coordinate System

Input Clipping

Feature Masking

Format Configuration

Thumbnail Raster View

Processing Options

Output / Geodetic Clipping

Rendering \(Feature Book\)

Output Coordinate System

Attribute Collection

Tiling

Filtering

Layering

Layer Loading Strategy

Vector Optimisation

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio39.jpg)

# How MapLink Studio Works

© Envitia Ltd 2024\. All rights reserved\.


---


# MapLink Studio User InterfaceOverview

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio40.png)

__Project & Navigation Tools__

__Status Bar__ : Displaying position\, coordinate system\, and feature information

© Envitia Ltd 2024\. All rights reserved\.


---


# MapLink Studio User InterfaceTools

* Tools are available from:
  * The Menu Bar
  * The Context Menu in the Project Tree
  * Via the toolbar\, usually docked to the left\-hand side of the window
* Tools are context sensitive\, so ensure that the correct ‘parent’ object is selected in the Project Tree
  * Some menus and entries may be disabled
* Navigation Tools allow you to review the current layer visualisation
  * Zoom to rectangle
  * Pan to point \(scrolls automatically if button held\)
  * Select feature \(double click displays the feature in the Feature Book\)
  * Zoom in / out
  * Reset to whole data extent

© Envitia Ltd 2024\. All rights reserved\.


---


# Project StructureOverview

* A MapLink Studio project defines all the processing required to create a single multi\-layer\, mixed vector\, raster and gridded data map or terrain database
* Consists of 4 files:
  * \.mlp \- the project itself
  * \.mlc \- information about the map data files referenced in the project
  * \.fbk \- the Feature Book used by the project \(more later\)
  * \.mtf \- stores details of any user defined coordinate systems
* Defines a single output coordinate system \(static or dynamic\)
  * For example\, the map is in British National Grid
* Contains multiple layer definitions containing datasets and data

© Envitia Ltd 2024\. All rights reserved\.


---


# Project StructureHierarchy

* The project is built using a standard Windows Tree\, with levels corresponding to the following hierarchy:
* __MAP__ :					The project contains a single map
  * __LAYER__ :			The map contains one or more layers
    * __DATASET__ :		Each layer consists of one or more datasets
      * __DATA__ 	 __:__ 	Each dataset contains one or more datafiles

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Level Structure

* The single map defines the following:
* The \(output\) coordinate system
  * For example\, British National Grid
* The layer loading strategy
  * This defines when swapping between layers occurs
* Some advanced options that will be covered later

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio41.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Layer Level Structure

* Each layer defines a view of the map at a particular scale or style
  * For instance\, one layer may be an overview of England
  * Another a more detailed overview of London
  * And another a street level map of London
* Each layer also has the following properties
  * Clipping\, to remove unwanted data
  * Filtering\, to reduce the density of data
  * Tiling\, to allow high performance
* Each layer contains any number of datasets\, which are what contain the data

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio42.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Dataset Level Structure

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio43.png)

* The dataset may hold any number of map data files
* All files within each dataset must be:
  * The same file format
  * The same coordinate system
* Each Dataset has the following properties:
  * Clipping\, to remove unwanted data
  * \(Input\) Coordinate system information\, to allow the data to be “unprojected”
  * Feature masking\, to remove unwanted map features
  * General raster\, vector\, or terrain configuration options
  * Format specific configuration information

© Envitia Ltd 2024\. All rights reserved\.


---


* A data file is a single map data file\, raster\, vector or gridded
* Each piece of data has the following properties:
  * General raster or vector configuration options
  * Format specific configuration information
* Each data file can be a single flat map file
  * E\.g\.: OS NTF or S\-57
* Or the index to a more complex structure
  * VPF
* When a data file is added to the project for the first time\, it is analysed to find:
  * The extent of the file
  * The features used in the file\, if a vector file
  * The size of the raster if a raster file

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio44.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Creating a Map

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio45.png)

* In the basic MapLink workflow of Input to MapLink Studio to Map\, this is the transition from Studio to Map
* Select ‘Map | Create Output Map’ invokes this dialog
  * Save a copy of the project for backup purposes
  * Metadata is extracted from the source and gives the run\-time application some information about the provenance of the data source\.  The contents vary according to the data source
  * Can output the map for use by applications built with earlier versions of MapLink
  * Convert to RGB values to avoid palette issues\.  This means that night/day palette handling will not work however
  * Remove features that wouldn’t get drawn

© Envitia Ltd 2024\. All rights reserved\.


---


# Output Files

* The following files are created when a MapLink map is generated by MapLink Studio:
* The Map creates:
  * __1 x \.map__ : The control file to be loaded into the API
  * __1 x \.pal__ : The colour palette of the map
* Each Layer creates:
  * __1 x \.dtl__ : The definition of the layer
  * __N x \.tmf__ : Vector tiles
  * __N x \.tpf\, \.tp1\, \.tp2__ : Raster Pyramid files / tiles

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio46.png)

__Note__ : For Internet Deployments\, the file names change slightly

© Envitia Ltd 2024\. All rights reserved\.


---


# The MapLink Map Viewer

* The MapLink Map Viewer is a MapLink Pro\-based application\, which allows you to view and test one or more MapLink maps
  * All must be in the same coordinate system
  * Use ‘File\->Load Map’ for the first maps\, ‘File \-> Add Map’ for subsequent maps
* The Overview\, Attributes and Declutter Panel are all dockable and resizable
* __Navigation__ :
  * Zoom\, Pan\, Zoom & Pan\, Grab\, Query\, Magnifier
  * Zoom In\, Zoom Out\, Reset to whole map display
  * Also\, Mouse Wheel for zoom
* __Overview Display__ : Drag / zoom current view
* __Data attribute querying__ : Metadata display
* __Decluttering__ : Maps or features
* Specialised British National Grid facilities integrated

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio47.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio48.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio49.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio50.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio51.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio52.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# How MapLink Studio WorksSummary

MapLink Studio provides a user interface that allows geospatial data to be loaded into a layer hierarchy\.

This layer hierarchy can be used to define the level of detail visible at different map scales\.

Data can be clipped\, filtered and tiled to optimise map performance\.

The output map can use a different CRS than the input data\.

Test your map using Map Viewer\.

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio53.jpg)

# Raster Data

© Envitia Ltd 2024\. All rights reserved\.


---


Raster data is a grid of pixels\, or image\, that stores information about features in a cell\-based manner

Information is often RGB values for images\, but can be any property

Examples of raster data include satellite imagery\, scanned charts\, relief maps\, LIDAR images etc etc

© Envitia Ltd 2024\. All rights reserved\.


---


* Using Raster Data
  * MapLink accepts many flat raster formats\, e\.g\.: TIFF\, JPEG\, BMP
  * It also accepts several structured raster formats\, e\.g\.: ASRP\, CADRG\, CIB\, GeoTIFF
  * These all contain embedded referencing information locating the raster data
* Raster referencing with flat rasters
  * When loading a flat raster\, referencing information is required
  * This tells MapLink where to locate the raster
  * MapLink reads the 2 standard referencing file types: World files & Tab files
  * If no referencing information is supplied\, MapLink will ask for it when the raster is added
  * Or use Image Studio to georeference your image\.

© Envitia Ltd 2024\. All rights reserved\.


---


# Raster Configuration

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio54.png)

* Common Raster configuration options:
* Raster downsampling
  * Creating reduced resolution raster datasets for fast loading
* Raster resizing
  * Reduce memory usage by limiting pixels
* Raster projection
  * Image interpolation for optimisation
* Transparency
  * Improving quality of low\-resolution images
* Feature Name
  * For use at runtime

© Envitia Ltd 2024\. All rights reserved\.


---


# Format Specific Configuration

Each raster format is different

MapLink provides some common raster configuration options

Some raster formats require additional configuration options\, depending on the data type

This is “Format Specific” configuration

Accessed from Data | Format Configuration…

Or from Dataset | Format Configuration…

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio55.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Additional Raster Options

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio56.png)

* Raster Loading
  * Optimised For Memory
  * Optimised For Speed
* Maximum Raster Cache Memory
  * Allows images larger than the value specified to be read in chunks
* Split Raster Threshold
  * Splits images until below value
  * Reduces memory footprint whilst loading/processing
* Multithreading

© Envitia Ltd 2024\. All rights reserved\.


---


# Raster Projection Information

* MapLink projects raster data in the same way as vector data\, but Note:
* Certain sources\, for example CADRG / ASRP\, are already in a projection
  * MapLink automatically sets an input coordinate system to convert them
* GeoTIFF can be in lat / long or in a projection
  * Since the latter has no defined specification\, you must select an appropriate input coordinate system yourself
  * MapLink reports the GeoTIFF string describing the projection to help you do this

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio57.png)

Look for GCS/CRS and lookup number in EPSG database

© Envitia Ltd 2024\. All rights reserved\.


---


# Georeferencing

MapLink Studio allows the geographic coordinates of the 4 corners of the raster to be specified

Image Studio allows more complex georeferencing\, specifying many more geographic points\, warping the image if needed\.

Georeferencing aligns raster data with the rest of your geospatial data

Many raster datasets are already georeferenced

But not always

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 3Georeference a Raster Image

This exercise shows:

Adding raster data to MapLink Studio

Georeferencing raster data

© Envitia Ltd 2024\. All rights reserved\.


---


# What is Layering?

A layer is a part of a map containing a specific level of detail

Layering is used to enable the display of parts of a map which if displayed in its most detailed state would be far too large to fit into memory or perform too slowly

Layering allows the appropriate level of detail to be displayed at a particular zoom level

© Envitia Ltd 2024\. All rights reserved\.


---


# Raster Detail Layer Example

__Top Layer__ : 1:250\,000 resolution data

__Middle Layer__ : 1:100\,000 resolution data

__Bottom Layer__ : 1:50\,000 resolution data

__Note__ : Raster and Vector Data can be mixed on the same layer\, and between layers

© Envitia Ltd 2024\. All rights reserved\.


---


# Layer Stacks

The map can be made of many “layer stacks”\, each of which can consist of one or many layers of the same extent

Overview of a country

Detailed view of a country

Area 2 detailed view

Area 1 detailed view

© Envitia Ltd 2024\. All rights reserved\.


---


# Layering

* Each Layer can be thought of as a “Layer of Detail”:
* When we are zoomed out\, the top\-most layer will be visible
  * Little data
* When we zoom in sufficiently\, we will swap into the next layer
  * More data in the layer\, but viewing a subset of it
* When we zoom in again\, we will swap into the most detailed layer
  * More data still in the layer\, but viewing an even smaller subset of it
* Our map has one major drawback
  * When we zoom into the bottom\, most detailed layer\, the whole layer needs to be read
  * This will be slow

© Envitia Ltd 2024\. All rights reserved\.


---


# Tiling

* Other packages use spatial queries to reduce the amount of information that needs to be drawn at certain levels of detail
  * This can be very slow
  * Certainly\, too slow for dynamic applications
  * Detailed information needs generalising
* MapLink uses tiling to reduce the amount of information to be drawn
  * This is much faster
* Tiling allows us to break the layers into tiled grids
  * When we zoom into the bottom layer\, we can instantly load the required portion of the layer\, instead of the whole layer
* MapLink automatically tiles raster data because:
  * The data is uniform across the raster
  * The amount of detail can be mathematically calculated
* Layer and Tiling combined help create efficient maps

© Envitia Ltd 2024\. All rights reserved\.


---


# Tiling Example

__Top Layer__ : Contains a single tile

__Middle Layer__ : Split into a tile grid of 4 x 4

16 tiles in all

__Bottom Layer__ : Split into a tile grid of 16 x 16

256 tiles in all

© Envitia Ltd 2024\. All rights reserved\.


---


# Choosing Tile Sizes

* Too few tiles:
  * Poor performance on detailed layers
* Too many tiles:
  * Increased generation time
  * File management becomes unwieldy
* Some metrics and guides:
  * Ideally largest tiles should be around 500Kb and no bigger than 5MB
  * Get tile size right for overview layer\, then detailed layer\, and the others should fit in

© Envitia Ltd 2024\. All rights reserved\.


---


# Viewing Layer & Tile Information

* The Reference section in the Feature Book allows you to configure how layer and tile information will be displayed in the Preview Panel:
  * Layer Overview rendering defines how tile boundaries and layer names will be displayed
  * Resolution overview defines how the layer change area is displayed for the current layer
  * Only one detail layer previewed at any one time

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio58.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Calculating Zoom Levels

* If the scale of a map is known\, it is possible to define the optimum layer resolution as which the map should be displayed\, using the following equation:
  * Layer resolution = Scale / \(Screen pixels per metre\)
* For example:
  * If your actual screen width is 31\.7cm \(~1/3rd metre\) and you a using a resolution of 1280x1024\, then there is 1280/0\.317 = ~4\,000 pixels per metre
  * For a map with a scale of 1:1Million\, the maximum layer resolution is 1\,000\,000/4\,000 = 250 MU per pixel

| Scale | Resolution |
| :-: | :-: |
| 1:1M | 250 |
| 1:500K | 125 |
| 1:250K | 62.5 |
| 1:50K | 12.5 |
| 1:25K | 6.25 |

© Envitia Ltd 2024\. All rights reserved\.


---


# Layer Loading StrategiesTile-Based Loading

* Unless told otherwise\, MapLink will swap intuitively between Layers without you having to define any swapping information
* “Display the Layer that would require the greatest number of tiles less than 10 to be loaded to show the required area”:
  * If Layer1 requires 1 tile
  * Layer2 requires 6 tiles
  * Layer3 requires 10 tiles
  * Pick Layer2
* Therefore\, never more than 9 tiles are ever loaded
  * Should be fast if the tile sizes are small \(300\-500k max\)

© Envitia Ltd 2024\. All rights reserved\.


---


# Layer Loading StrategiesResolution-Based Loading

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio59.png)

Allows the user to define the minimum zoom level at which the Layer should be displayed

Allows full user control of layer swapping

Independent of tiling

Easy to define

By default\, Resolution\-Based Layer Loading is used

© Envitia Ltd 2024\. All rights reserved\.


---


# Layer Loading

* Resolution\-based loading:
  * Defines the maximum zoom value \(in map units per pixel\) at which the layer will be displayed
  * Can be set graphically
  * Set the target resolution first
* Overlap Percentage:
  * Specifies how much of a layer must be on display before it is loaded in preference to the layer above
  * Usually set to 100%

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio60.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Resolution-Based Layer Loading

* Resolution based loading works by switching layers at specified zoom levels or resolutions
  * Value for top \(overview\) layer should always be set to 0
* Zoom values define the highest resolution at which a layer can be displayed and consequently the maximum \(real world\) distance that can be represented on the screen
  * Zoom values are roughly view extent in kilometres \(Map Units per pixel\)
* Zoom values are hardware dependent\, i\.e\.: they depend on the:
  * Physical screen width
  * Horizontal resolution of the screen
* Before generating the map\, check that the resolutions are sensible
  * I\.e\.: They get progressively smaller with reasonable gaps

© Envitia Ltd 2024\. All rights reserved\.


---


# Range-Based Loading

* Range Based Loading works by switching layers at specified displayed ranges
* Range values define the maximum \(real world\) distance at which a layer can be displayed
  * Range values are vertical view extent in Nautical Miles

© Envitia Ltd 2024\. All rights reserved\.


---


# Comparison of Loading Strategies

__Resolution / Range\-Based Loading__ :

Allows the user to define the minimum zoom level at which the Layer should be displayed

Allows full user control of layer swapping

Independent of tiling

Easy to define\!

* __Tile\-Based Loading__ :
* This is a straightforward case
  * Helpful for the novice user
  * Dependant on the tiling arrangements in layers
* Where more control is required use resolution\-based loading
* If Raster datasets are being used it is recommended that resolution\-based loading is used

© Envitia Ltd 2024\. All rights reserved\.


---


# Overlapping Layers

* Layers can either cover the entire or part of the map extent\, but only one layer loaded at a time
* There are circumstances where it makes sense to create multiple layers for the same level of detail which overlap
  * If the number of tiles / files generated becomes too large
  * To reduce the processing time of an individual layer
  * When tiling a sparse layer
* To set up multiple detail layers:
  * Set 100% overlap on the layer
  * Ensure that the layers overlap by at least 1 tile width

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 4Layering & Tiling a Raster Map

This exercise shows:

Defining several layers\, including an overview layer using filtering

Defining tiles for each layer

Selecting appropriate detail for the layers

Setting the zoom range of each layer

© Envitia Ltd 2024\. All rights reserved\.


---


# Reducing Processing Time

* The following options are available to reduce raster processing time:
* Select Thumbnail Raster View \(from  Tools | Options | Processing\)
  * Affects MapLink Studio only
* Switch off interpolation on Raster Downsampling and Raster Projection
  * This can be done by selecting  ‘Dataset | Raster Configuration’ for each raster dataset and changing the interpolation to ‘\<None>’
* Reduce the size of the raster
  * This can be done by selecting ‘Dataset | Raster Configuration’\, selecting ‘Reduce Raster Size’ and specifying a factor

__Note__ : Options 2 & 3 affect the quality of the output map\, and should only be applied to overview layers\, or for speed\, when configuring the map

© Envitia Ltd 2024\. All rights reserved\.


---


# Raster DataSummary

Raster data is a grid of pixels\, or image\, that stores information about features in a cell\-based manner\.

Raster data must be georeferenced to align with the rest of the map\.

Raster data can be tiled to increase performance\.

Layers of raster data can be loaded based on several criteria\.

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio61.jpg)

# Gridded Data

© Envitia Ltd 2024\. All rights reserved\.


---


# Introduction

“Terrain data” suggests ground elevation data

But can be any property recorded in a gridded format\, e\.g\. temperature\, bathymetry\, water salinity\, building elevation etc etc

“Terrain” data is also “a grid of pixels … that stores information about features in a cell\-based manner”

However\, MapLink Studio interprets the pixels as properties to be used in analysis rather than merely display information

© Envitia Ltd 2024\. All rights reserved\.


---


# Terrain Visualisations

MapLink supports the pre\-processing of Terrain Data into visualisations \- combinations of vector and raster data:

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio62.png)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio63.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Terrain Viewer

* The Terrain Viewer is supplied both as an application and as a source code example
* Select a map and then load a terrain database \(\.tdf\) from the ‘Load Terrain Option’
* Supports:
  * Point height display
  * Cross section display
  * Grid display

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio64.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Gridded DataSummary

* Can be any property recorded in a gridded format\, e\.g\.:
  * Ground terrain
  * Temperature
  * Bathymetry
  * Water salinity
  * Building elevation
  * etc etc
* Can be processed into a MapLink Map for data visualisation
* Can be processed into a MapLink Terrain Database for terrain analysis
* The MapLink Terrain SDK is needed for analysis of MapLink Terrain Database in a MapLink\-based app
  * Line of sight calculations
  * Viewshed calculations
  * Terrain profiles
  * etc

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio65.jpg)

# Vector Data

© Envitia Ltd 2024\. All rights reserved\.


---


# Introduction

Most vector data is supplied without instructions on how to “draw” it\.

So\, in most cases\, the client application needs to define the rendering styles applicable to the data\.

MapLink Studio achieves this\, ahead of runtime of the end\-user application\, by definition of a “Feature Book”\.

Geospatial vector data is a type of spatial data that represents geographic features as points\, lines\, and polygons\.

It's useful for spatial analysis operations like overlaying\, buffering\, and network analysis\. Vector data can also be easily modified or updated\, making it ideal for workflows that require frequent changes\.

© Envitia Ltd 2024\. All rights reserved\.


---


# The Feature BookOverview

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio66.png)

* In general\, vector map data does not define the rendering styles that should be used to draw it
* The Feature Book controls the rendering of Map Features
* It is a library of rendering styles that can be transported across projects
  * Define your rendering styles once\, and use them again and again
* In Exercise 1\, we defined a Feature Book Section called World
  * All the features in the data we added were automatically added to our new blank section

© Envitia Ltd 2024\. All rights reserved\.


---


# The Feature BookContinued

* The Feature Book allows you to define the following characteristics of a feature:
* Graphic attributes used for visualisation
* Style inheritance
  * Using the style of a parent feature
  * E\.g\.: Word “Normal Style \+ Bold”
* Rendering order definition
  * Useful when data is not stored in rendering order
  * E\.g\.: Lakes are required over land and therefore drawn on top
* Use of different colour palettes
  * All maps in the same application window must use the same palette

© Envitia Ltd 2024\. All rights reserved\.


---


# The Feature Book Structure

* Broken into sections
* Each Dataset can use the same section\, or a different section as required
* The recommended approach is to build a new Feature Book Section for each different map source type and possibly for each zoom range \(layer\) in which the data source is used\, for example:
  * Create a Feature Book Section for Shapefiles
  * Another for S\-57
  * Another 3 for VMap0 \(Overview / Intermediate / Detailed\)
* Sections can be imported from other Feature Books if required
* Feature Population:
  * When a Data file is added to the tree\, it is analysed to obtain a list of all features used in the file
  * These features are added to the Feature Book automatically
  * Use the Data | Vector Properties panel to review what features are in a file

© Envitia Ltd 2024\. All rights reserved\.


---


# Line Feature VisualisationStyles

* There are several variants of style:
* __Simple__ :
  * A single stroke\, which can be dashed
  * Fast to render
* __Multi\-Part__ :
  * Multiple simple strokes that build up to form a more complex style\, such as a road with casing\, carriageway\, and centreline
  * Slower to render
* __Complex__ :
  * Multiple strokes defined by a plotter pen up / move / down / draw style sequence
  * Often forming complex edges that include symbols according to specific standards
  * Slowest to draw and can have problems around corners
  * Best only used for large simple areas

© Envitia Ltd 2024\. All rights reserved\.


---


# Line Feature VisualisationProperties

The following are the available ‘Thickness Units’ options:

__Pixels__ : Fixed size on the output device\, vary between screen and printer

__Map Units__ : Fixed size in the Output Coordinate Space\, nominal Metres\, bigger when zoomed in

__Points__ : Typographic unit \(1/72 of an inch\)\, same on screen and printer

__TMC__ : Internal units often used in the run\-time environment\, do not use in MapLink Studio \(use Map Units instead\)

* The following properties can be set:
* __Colour__ :
  * From the current palette
  * Only applies to portion of non\-simple styles
* __Thickness__ :
  * How thick the line should be
  * Multi\-part and complex lines styles have a minimum thickness
* __Thickness Units__ :
  * Interpretation for the ‘Thickness’ value

__Note__ : Map Units are affected by the Output Coordinate system

Set up the Output Coordinate System first\!

© Envitia Ltd 2024\. All rights reserved\.


---


# Area Feature VisualisationStyles

* __Translucent__ :
  * Alpha blended fill\, with area below showing through
  * Slowest to render\, especially on some graphics systems
* __ROP Code__ :
  * Complex to understand
  * Recommend do not use\!

* There are several variants of style:
* __Solid__ :
  * A single block colour
  * Fast to render
* __Simple Pattern__ :
  * A simple cross\-hatch style pattern\, with non\-hatched part transparent
  * Slightly slower to render
* __Complex Pattern__ :
  * Defined by simple monochrome on / off pattern\, with non\-hatched part transparent
  * Slightly slower still to render

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio67.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Area Feature VisualisationProperties

* __Edge Thickness__ :
  * As for Line Features
  * Defines the thickness of the edge of the area
* __Thickness Units__ :
  * As for Line Features
  * Defines the units of thickness used for Edge Thickness
  * Has the same options as for Line Features \(Pixels\, Map Units\, Points\, and TMC\)

* The following properties can be set:
* __Colour__ :
  * From the current palette
* __Edge Colour__ :
  * As for Line Features
  * Defines the colour of the edge of the area
* __Edge Style__ :
  * As for Line Features
  * Defines the style of the edge of the area

© Envitia Ltd 2024\. All rights reserved\.


---


# Symbol Feature VisualisationStyles

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio68.png)

* There are several variants of style:
* __Vector__ :
  * A MapLink \.tmf file
* __Icons__ :
  * Windows \.ico file
  * Not rotatable
  * Print issue
* __Raster__ :
  * \.tiff\, \.png\, or \.gif file
* __Font__ :
  * A TrueType font specifier

© Envitia Ltd 2024\. All rights reserved\.


---


# Symbol Feature VisualisationProperties

* __Size Factor__ :
  * Height of the symbol in chosen units
* __Size Units__ :
  * As per line thickness
  * Defines the units used by Size Factor
  * Has the same options as for Line Features \(Pixels\, Map Units\, Points\, and TMC\)
* __Min / Max Size__ :
  * Clamped size in pixels
  * Typically used when Size Units are not pixels or points

* The following properties can be set:
* __Font Symbol Character__ :
  * Used for Symbol Styles that are fonts
* __Colour__ :
  * From the current palette
  * Only part of vector symbol
* __Scalable__ :
  * Flag to allow raster symbols to scale
  * Default value is read from the symbols file
* __Rotatable__ :
  * Flag to prevent rotation
  * Projection can cause symbols to rotate since they follow the line of latitude
  * Default is read from the symbols file
  * Not always wanted \(e\.g\.: Lighthouses\)

© Envitia Ltd 2024\. All rights reserved\.


---


# Modifying Rendering Styles

* The Feature Properties dialog allows you to select the following property types:
* Simple Style Selection
  * E\.g\.: Fill\, line\, and edge style
  * Select the appropriate option from the combo box
* Colour Selection
  * Select the colour from the colour palette displayed
  * Pin the colour palette for permanent display if required
* Numeric Value
  * E\.g\.: Edge thickness and text size factor
  * Simply enter a value
* Dimension Unit Selection
  * E\.g\.: Pixels or map units
* Symbol Style Selection

__Note__ : One can select multiple features using CTRL or SHIFT

__Note__ : Many properties allow you to select one of the following:

__None__ : To disable the rendering of this property

__As Parent__ : To inherit the rendering properties of a parent feature

© Envitia Ltd 2024\. All rights reserved\.


---


# Feature Ordering

* Order of features in the Feature Book tree:
* The order that features are presented in the tree is important when using heterogeneous file types
  * I\.e\.: files which contain many features of different feature classes
* It defines the rendering order of the features in a file
  * For example\, a \.mif file contains polygons for land area\, desert\, and lake
  * To ensure that the desert and lake polygons are placed on top of the land area polygons\, and therefore drawn on top\, land area must be above desert and lake in the Feature Book tree
* But if land area was in a different file to desert and lake\, then we would use the project tree to define the rendering order\!
* Simply drag items up and down the tree to change the drawing order
  * Can also use rendering level \(\-5 to \+5\)
  * All level \-5 items drawn first etc\.
  * Symbols and Text always given priority over other primitives

© Envitia Ltd 2024\. All rights reserved\.


---


# Feature Ordering Logic

When drawing a layer with several datasets and associated Feature Book Sections\, and across them several features with equally high priority\, the following logic is applied to ‘tiebreak’:

Symbols and Text always drawn after other primitives

Render level \(Lowest to highest\)

Dataset order in the Layer

Datafile order in the Dataset

Feature Class Order in the Feature Book Section

© Envitia Ltd 2024\. All rights reserved\.


---


# Feature Book Management

When using the same Feature Book for different Map projects\, the following should be kept in mind:

Once a Feature Book has been configured for a specific data product \(such as VMAP0\)\, it is desirable to reuse it within other map projects that use the same data

The MapLink Feature Book \(\.fbk\) is stored as a separate file to allow it to be shared between map projects

A new project can use the Feature Book from a previous project

A current project can import Feature Book sections from a previous project

__Note__ : Some change management MUST be applied if a feature book is to be used for multiple projects\, otherwise feature rendering may change from map to map

© Envitia Ltd 2024\. All rights reserved\.


---


# Feature Book Rules for Multiple Maps

It is possible to load multiple MapLink maps into an application

However\, some restrictions apply:

The same colour palette must be used for all maps

All maps must have the same \(output\) coordinate system

All maps must have the same TMC Per MU setting \(see later\)

© Envitia Ltd 2024\. All rights reserved\.


---


# Other Feature Book Options

* Changing the feature book section for an existing dataset
  * Use the ‘Feature Book Section’ tab under the dataset properties
  * \(‘Miscellaneous’ tab in earlier MapLink versions\)
* Importing a section from an existing feature book
  * Select Import when adding the dataset\, select the feature book and then the section to import from it
  * Or select Section | Import from the menu bar of the Feature Book
* Copying an existing section
  * Often useful when using different rendering for overview and detailed layers
  * Select Section | Clone from the Feature Book menu
* Changing the colour palette
  * Select Palette | Import from the Feature Book menu and choose a new \.pal file

© Envitia Ltd 2024\. All rights reserved\.


---


# Text Feature VisualisationProperties

* __Offset X / Y__ :
  * Offset from anchor point
  * Often used when labelling point objects
  * Applies in addition to alignment
* __Offset Units__ :
  * As per line thickness
  * Defines the units used by Offset X / Y
  * Has the same options as for Line Features \(Pixels\, Map Units\, Points\, and TMC\)
* __Size Factor__ :
  * Height of the text in chosen units

* The following properties can be set:
* __Font__ :
  * Standard Windows or X11 font\, or simple Vector \(TSLRom\)
* __Colour__ :
  * From the current palette
* __Vertical / Horizontal Alignment__ :
  * Defines where the text is drawn in relation to its position
  * Can be in source data
* __Rotatable__ :
  * Flag to prevent rotation of text
  * Projection can cause text to rotate since it follows the line of latitude
  * Text rotation is slow to render

© Envitia Ltd 2024\. All rights reserved\.


---


# Text Feature VisualisationProperties Continued

* The following properties can be set:
* __Min / Max Size__ :
  * Clamped size in pixels
  * Typically used when Size Units are not pixels or points
* __Size Units__ :
  * As per line thickness
  * Defines the units used by Size Factor \(see previous slide\)
  * Has the same options as for Line Features \(Pixels\, Map Units\, Points\, and TMC\)
* __Background__ :
  * Can accentuate the text with a halo or scaled background rectangle
  * Fill style and edge colour for rectangle as for area features
  * Edge is solid one pixel wide
  * Performance hit

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio69.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 7Create a Countries Map with Simple Labelling

This exercise shows:

Adding vector data to MapLink Studio

Collection of attributes

Query of Attributes in the runtime\, using the Map Viewer

Simple labelling

© Envitia Ltd 2024\. All rights reserved\.


---


# Vector Data Attributes

* What is attribute data?
  * Most vector data formats associate a set of data with each feature
* MapLink can use attributes in the following ways:
  * To attach a name to an object
  * To display text against an object
  * To subclass a feature in the map
  * To export attributes for use at runtime

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio70.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Attribute CollectionWhy Export Attribute Data in a Map?

* Most vector data formats associate a set of data with each feature
* It is sometimes desirable to retain this data for use in a MapLink application
* MapLink Studio can be configured to include this attribute data within a generated map
* This attribute data can be viewed at runtime in your application
* Attribute data can be obtained from the following data types:
  * S57
  * VPF
  * Shapefile / MIF
  * OS MasterMap
  * DAFIF
  * Jeppesen

© Envitia Ltd 2024\. All rights reserved\.


---


# Attribute CollectionWhy Not Always Include All Attribute Data?

* Including attribute data within a map increases the size of the map on disk
* Performance of the map may also be affected
* Only include the required attribute data
* Sometimes it is best to include a few key attributes and then to use the runtime application to locate the rest based on the key in the database
* Can raster maps include attribute data?
  * No\, only vector maps contain attribute information
  * To simulate attributes on raster maps\, a vector map layer can be hidden behind a raster layer\, so it is invisible
  * The MapLink API can then query attributes from the vector data while displaying raster data

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Metadata Configuration

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio71.png)

Generates a Map Metadata XML configuration file from the XSLT

© Envitia Ltd 2024\. All rights reserved\.


---


# Vector Subclassing

* What is subclassing?
  * Subclassing allows attributes contained within vector datasets to be used to categorise data
  * Only available on vector datasets that include attributes for each feature
  * MapLink normally allows two levels of subclassing for each feature
* Which attributes can be subclassed?
  * Any of the attributes that are available for a feature can be used for subclassing
  * For example\, the Shapefile “country\.shp” has the attributes “Name\, Continent\, Accuracy\, Population\, etc\.” then the two levels of subclassing can be ‘Country \-> Continent’ and ‘Continent \-> Name’
  * This would group each country feature according to continent and then by name

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio72.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Rules for Vector Subclassing

* Subclassing configuration is similar for each Vector panel that supports it
* Usually consists of “Level 1” and “Level 2” selection boxes
* If “Level 1” is set and “Level 2” is empty\, only one level of subclassing is configured
* Option may be available to “Subclass from theme”
  * When not selected\, “Level 1” will appear at the root of the feature book
  * This allows greater control for reordering within the feature book
  * But does not allow inheritance of styles from the parent feature class
* Subclassing can significantly increase the size of the feature book
  * May have \(slight\) performance issues
  * Do not use if not needed
* Where a “Text Attribute” is provided\, a single attribute can be selected that will be displayed as text at the location of the feature
  * The text will be assigned the same feature code as the feature\, including any subclassing

© Envitia Ltd 2024\. All rights reserved\.


---


# Range Based Subclassing Features

Format Configuration allows features to be dependent on attributes

But all values in a class are included

For numeric values\, it is sometimes better to group ranges of values under features

Range based subclassing makes this possible

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio73.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Using Attributes for Names & Labels

* MapLink objects have two fields with specific functions that can be set by attributes:
* The Name field
  * If the name field is set to an attribute\, MapLink Studio will display the name of the object in the status bar when you hover over it
  * The name is also available to a MapLink application
  * The name field is commonly used as a key to a database
* The Text Label field
  * This is the text that will be generated as a primitive for each point object in the map data
  * It is useful for adding text in map formats containing no text primitives
* Both these fields can be set on either individual files or on the dataset using ‘Format Configuration’
  * Not all datasets support this
* Use the ‘Unique Values’ button to preview the attribute contents

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 8Create a Countries Map with Subclass-Based Labelling

This exercise shows:

Setting up Format Configuration options

Setting up subclassing

Redefine visualisation for subclassed features

Redefine labelling for subclassed features

© Envitia Ltd 2024\. All rights reserved\.


---


# Vector Detail Layer Example

__Top Layer__ : Land Areas\, Coastline\, International Boundaries\, Major Rivers\, Lakes\, and Cities

__Upper Middle Layer__ : Major Roads\, Railways\, Major Towns

__Lower Middle Layer__ : Minor Roads\, Minor Rivers\, Minor Towns

__Bottom Layer__ : Streets

__Note__ : Raster and Vector Data can be mixed on the same layer\, and between layers

© Envitia Ltd 2024\. All rights reserved\.


---


# Tiling

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio74.png)

* Both vector and raster maps use tiling
* Whereas Raster data tiling is automatic\, Vector data tiling must be set\-up because:
  * It is not uniform coverage
  * The amount of detail is determined by the user

© Envitia Ltd 2024\. All rights reserved\.


---


# Feature Masking

* What is Feature Masking?
* Feature Masking is the removal of unwanted features from a map
  * For example\, a data file may contain B Roads
  * In our overview layer we do not wish to use B Roads
  * Therefore\, we should mask them out
* Feature Masking is available at the Dataset level
  * Tick only the features that you want to appear in the map
* The Feature Masking tree will remove the unselected features from all files in the dataset
* Setting the style of a feature to ‘None’ in the feature book has the same visual effect as masking\, BUT:
  * The primitives are still included in the output map
  * Performance is therefore degraded
  * Use feature masking in preference if the feature will never be needed in the application

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 9Create a Decluttered Map

This exercise shows:

Decluttering features

© Envitia Ltd 2024\. All rights reserved\.


---


# Filtering

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio75.png)

Filtering reduces the detail in a layer by removing points of a line or polygon

Useful when constructing overview layers from detailed data

This can be done safely for overview layers where some points are imperceptible from each other when zoomed out

This results in smaller tile sizes and consequently faster maps

Filtering is applied to a complete layer of data

__Note__ : Filtering must be applied cautiously\, as it may be quite destructive

© Envitia Ltd 2024\. All rights reserved\.


---


# Filtering Techniques

* MapLink supports the following filtering techniques:
  * __Line Simplification Filter__ : Uses only extreme points that define the shape of the line
  * __Line Delta Filter__ : Removes points less than a specified distance from the last
  * __Angle Change Filter__ : Removes points less than a specified angle change from the last
  * __Island Filter__ : Removes objects whose diameter is less than a specified distance
  * __Perceptual Filter__ : Reduces detail by identifying how important each point is to the overall shape of a geometric entity\, and then removing those points that have no effect on its appearance at a defined viewing resolution
* To get best results:
  * Evaluate the statistics for the layer \(e\.g\.: point separation\, angle change\)
  * Transfer the results back to the Filtering panel\, review and adjust
  * Recommend Perceptual Filtering

© Envitia Ltd 2024\. All rights reserved\.


---


# Vector Configuration

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio76.png)

Line Labelling and Entity Name Configuration are specifically intended for GDF datasets

Keyhole Polygons can improve performance with some data on most systems

__Note__ : Use of Keyhole Polygons is not recommended if using the Open GL Drawing Surface in the runtime

© Envitia Ltd 2024\. All rights reserved\.


---


# Polygon KeyholingOverview

* Replaces all input polygons with “keyholed” polygons
* Reduces the number of rings in the map
* Some processing overhead\, especially with large complex polygons
  * E\.g\.: The tree line in Canada\, sea polygon near Denmark\, etc\.
* Improved performance on some systems
* Only when edge display not required
  * E\.g\.: Another feature for coastlines

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio77.png)

Original Holed Polygon

© Envitia Ltd 2024\. All rights reserved\.


---


# Polygon KeyholingExample

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio78.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Processing Options

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio79.png)

Vector Tiling Cache:

Memory size for file cache

If you have sufficient memory\, make as high as possible

For example\, on a machine with 16GB RAM try using 12GB

Speeds up vector processing

© Envitia Ltd 2024\. All rights reserved\.


---


# Optimisation

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio80.png)

Vector optimisation:

Reduces tile sizes

Batching is OK for typical map usage

Optimisation for compression is only applicable to very poor bandwidths \(<56k\)

© Envitia Ltd 2024\. All rights reserved\.


---


# Vector Optimisation

* What is vector optimisation ?
  * Allows significant performance enhancement
  * Groups together polygons and polylines with the same feature code into a single object \(which allows graphics optimisation\)
* Are there any drawbacks ?
  * Because features are grouped together\, they can no longer be individually identified

Polygon \(12 Points\)

Polygon \(23 Points\)

Batch \(92 Points\)

1 Distinct Object

Polygon \(57 Points\)

3 Distinct Objects

© Envitia Ltd 2024\. All rights reserved\.


---


# Vector DataSummary

Geospatial vector data is a type of spatial data that represents geographic features as points\, lines\, and polygons\.

MapLink Studio configures rendering styles for vector data\, through the definition of a “Feature Book”\.

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio81.jpg)

# Clipping

© Envitia Ltd 2024\. All rights reserved\.


---


# Overview

Clipping removes data outside the area of interest :

Removes the need to store and load unwanted data at runtime

Three types of clipping are available:

__Input Clipping__ : Clip the data in its original coordinate system\, used to reduce input detail for large datasets

__Geodetic Clipping__ : __ __ Using the WGS84 coordinate system\, needed to clip around the anti\-meridian \(longitude = ±180°\)\, inserts additional vertices along the latitude/longitude limits

__Output Clipping__ : __ __ Clip the data in the output coordinate space\, often used to clip a rectangular area of a non\-rectangular map\, studio provides an option to do this graphically

© Envitia Ltd 2024\. All rights reserved\.


---


# Process Flow

Data in Input Coordinate System \(X / Y\)

Clip to Rectangle in

X / Y

Unproject to WGS 84 \(Lat / Long\)

Clip to Rectangle in Lat / Long

Project to output coordinate system

\(X / Y\)

Clip to Rectangle in

X / Y

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 10Input & Output Clip Your Data

This exercise shows:

Converting input data from projected to unprojected format

Clipping in input units\, lat / long\, and output units

© Envitia Ltd 2024\. All rights reserved\.


---


# ClippingSummary

Clipping removes data outside the area of interest\.

Three types of clipping are available:

__Input Clipping__

__Geodetic Clipping__

__Output Clipping__

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio82.jpg)

# Terrain Databases

© Envitia Ltd 2024\. All rights reserved\.


---


# Introduction

* Can be processed into a MapLink Terrain Database for terrain analysis
* The MapLink Terrain SDK is needed for analysis of MapLink Terrain Database in a MapLink\-based app
  * Line of sight calculations
  * Viewshed calculations
  * Terrain profiles
  * etc

* Gridded data can be any property recorded in a gridded format\, e\.g\.:
  * Ground terrain
  * Temperature
  * Bathymetry
  * Water salinity
  * Building elevation
  * etc etc

© Envitia Ltd 2024\. All rights reserved\.


---


# Terrain DatabasesOverview

Gridded data can be imported\, clipped\, projected and exported into a terrain database

The resulting terrain database is multi\-resolution allowing retrieval at ideal level of detail for maximum performance

Output Map

Vector / Raster

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio83.png)

Terrain Data

e\.g\.: DTED\, DBDB\-V\, ASCII\-DEM\, etc\.

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio84.png)

Terrain Database

© Envitia Ltd 2024\. All rights reserved\.


---


# Exercise 11Create a Terrain Database

This exercise shows:

Creating a terrain database

Viewing the terrain database and the map using the MapLink Terrain Viewer

© Envitia Ltd 2024\. All rights reserved\.


---


# Terrain DatabasesUse Cases

* The output terrain database then can be used for on\-the\-fly visualisation\, simple terrain interrogation at the chosen resolution to return:
  * Height of a point
  * Cross\-section array
  * Area grid
* Also:
  * Line of Sight Calculations
  * View shed display

© Envitia Ltd 2024\. All rights reserved\.


---


# Terrain DatabasesSummary

Gridded data \(AKA terrain data\) can be processed into a MapLink Terrain Database for terrain analysis

The MapLink Terrain SDK is needed for analysis of MapLink Terrain Databases in a MapLink\-based app

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio85.jpg)

# Cataloguing

© Envitia Ltd 2024\. All rights reserved\.


---


* Files are analysed \(catalogued\) on initial loading
* Many actions can cause re\-cataloguing to happen automatically
  * All format configuration changes
  * E\.g\.: Sub\-classing
  * Assigning a new Feature Book section
  * Explicit re\-cataloguing
* Re\-cataloguing can be slow but is essential in many cases to create an optimised map
  * So\, always save your project before carrying out an action which forces a catalogue to occur
* The one occasion when you should force a re\-catalogue is when a referenced data file has changed
  * For example\, when editing an ASCII file

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio86.jpg)

# Large Maps

© Envitia Ltd 2024\. All rights reserved\.


---


# Creating Large Maps

* Some MapLink maps are extremely large\, and there are tradeoffs in producing them\, with ways to mitigate this including:
* While experimenting try to keep the extent of data being used to a minimum \(pick one tile\)
* The more physical memory you have the better
  * Set the processing options to make best use of memory and file caching
* Consider splitting the map into different map sets which can be overlaid
* Concentrate on one layer at a time
* For raster data in particular\, the choice of projection can make a difference
* In MapLink Studio Options always turn off Automatic Data Loading and turn on Raster Thumbnail View if you don’t want lots of very long tea breaks
* Copy data off CDs onto local disks \(can make 10x difference to time\)

© Envitia Ltd 2024\. All rights reserved\.


---


# Loading Large Data Files

Stream files by page\, i\.e\.: read the data in chunks

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio87.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Complex Map Rendering

* The key to map rendering is to retain a balance between aesthetics and performance
* Usually\, common sense and good design gives both an aesthetically pleasing and high\-performance map
  * A map that is very slow will usually be unnecessarily complicated
* It is always good practice to try maps out on the target environment\, before finalising your map

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio88.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Rendering Checklist

* Use the following checklist when setting up your map rendering:
* Select a map source appropriate to the level of detail required
* Mask out any features not required
* Avoid heavy use of rendering styles which are slow to draw
  * “Road rendering” and complex line styles
  * Transparent hatched or translucent fill styles
  * Rotated raster text
  * Complex symbols
* Check performance on the target machine

© Envitia Ltd 2024\. All rights reserved\.


---


# Overview Layers

An Overview Layer is typically one with a much\-reduced level of detail

For viewing at small scale \(i\.e\. zoomed out\)

Configure your map to display an overview layer initially

Swap to detailed layer when the user zooms in to larger scale

© Envitia Ltd 2024\. All rights reserved\.


---


# Automatic Overview Layer Generation

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio89.png)

Determines and adds additional detail layers

Layers are rasterised versions of the least detailed layer

© Envitia Ltd 2024\. All rights reserved\.


---


# Large MapsSummary

* Without mitigation\, a map with a large amount of detailed data in it can become unusable:
  * Application performance
  * Information overload

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio90.jpg)

# MapLink Maps in a Runtime

© Envitia Ltd 2024\. All rights reserved\.


---


# Product Runtime Structure

* __Core Development Kit__
  * Management of the Map ‘base’
  * Management of the Display
  * Geometric Overlay Drawing
  * Object placement/queries
  * Management of Dynamic Objects
  * Coordinate Conversion/Management
* __Ensures__ :
  * Appropriate map detail loaded
  * Overlaying objects updated quickly
  * Accurate object overlay
* __Additionally__ :
  * Terrain Interrogation \(Terrain SDK – Windows / X11 / Android\)
  * 2D Drawing Capability \(GDI / OpenGL / X11\)
  * 3D Drawing Capability \(Earth SDK\)

Standard Data Layer

Object Data Layer

Dynamic Object Feeds

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Post Processing

* Reduces the amount of calculation performed at runtime
* Recommended that maps containing vector data should always have the option enabled
* Maps containing raster data should normally have one or more options enabled
  * __Desktop__ : Use S3TC
  * __Mobile / Embedded__ : Use ETC1
* Settings are stored in Studio configuration not the project so apply to all subsequent maps created

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio91.png)

__Note__ : Only applies to maps intended for use with the OpenGL 2D Drawing Surface

© Envitia Ltd 2024\. All rights reserved\.


---


# Partial Map Updates

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio92.png)

* When data updates are supplied\, you will need to update your existing map
* If there have been no feature code changes between the old and new data\, then only layers containing updated data need be regenerated
  * Back\-up the old map
  * Make a copy of the \.map file
  * Update the dataset with the new data files
  * Set Map File Generation for selected layers only and exclude all other layers
  * After processing overwrite the new \.map file with the original

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Generation Options

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio93.png)

Raster and Terrain Pyramid Nugget size \(pixels\)

Layers written to individual directories

Compressed map for Internet / Intranet applications

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Display Problems

If your maps do not appear:

Try reloading the layer

Check the dataset or layer is not turned off

Check the input clipping is not outside the extent of the data

Check the coordinate system

Check feature masking and rendering of features

For VMAP\, check that you have selected the right library

© Envitia Ltd 2024\. All rights reserved\.


---


# Map Design

* Tune your map:
* A well\-designed map can make a lot of difference to performance
* Don’t clutter the map
  * Use layers of detail to minimise what is displayed at any point
  * Use the Perceptual Filter
* Make sure you remove unwanted features using feature masking
  * Don’t just make them invisible
* Be aware of rendering attribute performance hits
  * Translucent fills \(Windows\)
  * Multipart line styles and map unit thickness lines
* Tile the map

© Envitia Ltd 2024\. All rights reserved\.


---


# Features in the API

* The Feature Book tree is available via the API for a generated map
* For instance\, using the Feature Book tree to the right would result in the following features being available via the API:
  * “World\.country”
  * “World\.country\.Europe”
  * “World\.country\.Europe\.Spain”
  * etc\.
  * “World\.latlon”
  * “World\.rivers”
* These feature codes can be used to declutter the map at runtime
* Only features in the generated map are available\, not everything from the Feature Book

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio94.png)

© Envitia Ltd 2024\. All rights reserved\.


---


![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio95.jpg)

# WMS

© Envitia Ltd 2024\. All rights reserved\.


---


# Introduction

MapLink Pro includes a Web Map Server \(WMS\) component

Makes a MapLink Map available over a network

Complies with the Open Geospatial Consortium \(OGC\) Web Map Service \(WMS\) open standard interface specification

Support for FAIR concepts \(Findable\, Accessible\, Interoperable\, and Reusable\)

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio96.png)

© Envitia Ltd 2024\. All rights reserved\.


---


# Web Map Server Configuration

![](img%5CLOCAL%20COPY%20UTR1107-08%20MapLink%20Studio97.png)

The MapLink WMS Server requires a file that defines the map’s metadata

Generates the Metadata XML configuration file used by a WMS

© Envitia Ltd 2024\. All rights reserved\.


---


# Final Summary

MapLink allows the following:

Creation of a multi\-layer map in a single coordinate system

Integration of a variety of different data formats

Use of data in different coordinate systems

Mixing of raster and vector data

Creation of a multi\-layer terrain database

Creation of a fast\, dynamic map display\, whatever the target application

© Envitia Ltd 2024\. All rights reserved\.

