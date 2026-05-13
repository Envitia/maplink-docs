---
title: "Spatial SDK"
---

# Spatial SDK


The Spatial SDK introduces several additional spatial operations to the
Editor SDK, such as the Arc, Parallel and Ray drawing modes and the
Follow mode specialised operation. It also allows for the creation and
merging of islands of change, which can be used to apply updates to a
map.

## Library Usage and Configuration

As with the MapLink Core SDK, the Spatial SDK comes in 2 different
flavours. It should be noted that the library to be linked with should
be determined by the Core SDK library that you are using within your
application. For example, if you are using the Release mode, DLL version
of the Core SDK (MapLink.lib/MapLink64.lib) then you must also use the
equivalent Spatial SDK library (LandLink.lib/LandLink64.lib).

<table class="doc-table">
  <tbody>
    <tr><td><strong>LandLink.lib or LandLink64.lib</strong> Release mode, DLL version. Uses Multithreaded DLL C++ run-time library. Requires TTLDLL preprocessor directive. Must also link the MapLink CoreSDK library MapLink.lib Refer to the document \"MapLink Pro X.Y: Deployment of End User Applications\" for a list of run-time dependencies when redistributing. Where X.Y is the version of MapLink you are deploying.</td><td><strong>LandLinkd.lib or LandLink64d.lib</strong> Debug mode, DLL version. Uses Debug Multithreaded DLL C++ run-time library. Requires TTLDLL preprocessor directive. Must also link the MapLink CoreSDK library MapLinkd.lib No redistributable run-time available. <strong>KEYED : Development machines only.</strong></td></tr>
  </tbody>
</table>

## Islands

### What are Islands?

One of the principal uses of the Spatial SDK is to manage a series of
updates to a vector based map. These updates can be grouped into a set
of contiguous groups of entities called islands, each of which
represents an independent area of change to the map.

### Creating Islands

Islands are constructed via the two static createIslands methods
available on the TSLIsland class. Both methods take a
TSLStandardDataLayer containing the data to be converted into islands.
Usually this layer will have been populated directly from a data source
(such as a set of OS MasterMap COU files) via the interoperability
functions as described in section [12.10](#interoperability). The act of
creating the islands depopulates the source data layer, so if this layer
may be required later a clone should be passed to the createIslands
method instead of the original.

The first createIslands method performs a simple geometric merge of
entities in the source data layer to create islands of contiguous
features. This does not modify the geometry of any of the entities, it
simply sorts them into contiguous regions.

The second createIslands method takes additional parameters that
correspond to the full path to a map containing a seamless layer (see
section [**Error! Reference source not found.**](#_Ref183510906) for
information on seamless layers), with an associated entity reference
handler for the map. This method will replace 'departed' entities in the
source data layer (entities which have a negative feature ID) with the
geometry of the original entity from the map. The departed status and
the TSLDataSet of the entity from the source data layer will be
preserved on the replaced entity. This may be useful in situations where
having access to the geometry for departed entities is required.

By their nature, departed entities often overlap with the entities that
replace them. However, they may not share any common edges and in this
case the departed feature will be placed into a different island than
the feature(s) that cover the same geographical location in order to
prevent overlapping entities from being present in the island.

Should you wish these entities to be assigned to the same island that
contains the features that replace it, you should call the static
sortDepartedFeatures method on the TSLIslandSet populated by the call to
createIslands. This method uses the geometry of the original entity in
the map that is being deleted to reassign departed entities in the
island set to the correct island.

### Merging Islands

Multiple sets of updates to a map can be combined into a single update
representing the sum of all the updates via the mergeIslands methods
available on the TSLIsland class. There are two ways in which this can
be done. The first performs a purely geometric merge of all entities
contained within the source TSLIslandSet. This can be used to combine
updates for different areas of a map into a single combined update for
ingest into the map. This version of mergeIslands does not handle
multiple different versions of the same entity being present in the
source island set. If this happens, the resulting merged island set will
still contain multiple versions of the entity.

This case is handled by the other two versions of mergeIslands. The
difference between these two is that one allows merging of a new update
contained within a TSLStandardDataLayer with the existing island set,
while the other only merges the contents of the island set. The entities
within the island set are merged so that only the newest version of the
entity remains. In the case of merging a modified and departed entity
the order in which the entities are encountered during the merge
determines which remains in the merged island set. Thus, to ensure that
the merge operation leaves the correct entity in the merged set, the
following process should be followed:

1.  Import the data corresponding to the first update into a
    TSLStandardDataLayer

2.  Create an initial island set from the data using createIslands

3.  []{#_Ref183515532 .anchor}Import the data corresponding to the
    second update into a TSLStandardDataLayer

4.  []{#_Ref183515533 .anchor}Merge the initial island set and the data
    layer containing the second update using mergeIslands

5.  Repeat steps [3](#_Ref183515532)-[4](#_Ref183515533) for each of the
    remaining updates.

The following code example illustrates this process.

> // Load the map and initialise the seamless layer reference handler
>
> TSLMapDataLayer \*mapLayer = new TSLMapDataLayer();
>
> mapLayer-\>loadData( pathToMap );
>
> TSLSeamlessLayerConfig \*config = new TSLSeamlessLayerConfig();
>
> config-\>initialiseFromConfig( pathToConfig );
>
> TSLSLMEntityRefHandlerFile \*refHandler = new
> TSLSLMEntityRefHandlerFile( \*config );
>
> TSLStandardDataLayer \*initialUpdate = new TSLStandardDataLayer();
>
> // Import the initial update data
>
> TSLUtilityFunctions::importData( initialUpdate, ... );
>
> // Create the initial islands
>
> TSLIslandSet \*islandSet = new TSLIslandSet();
>
> TSLIsland::createIslands(initialUpdate, \*islandSet );
>
> // Place departed entities into the same island as their replacement
>
> // features
>
> TSLIsland::sortDepartedFeatures( mapLayer, \*refHandler, \*islandSet
> );
>
> TSLStandardDataLayer \*couLayer = new TSLStandardDataLayer();
>
> // Import the COU data
>
> TSLUtilityFunctions::importData(couLayer, ... );
>
> // Merge the COU with the initial islands
>
> TSLIslandMergeSet \*mergedIslands = new TSLIslandMergeSet();
>
> TSLIsland::mergeIslands( \*islandSet, couLayer, pathToMap,
>
> \*refHandler, \*mergedIslands );

## Additional Editor Operations

These will be discussed in much greater detail in a future version of
this document. Please contact Envitia support to see if there is a newer
version available.

The intended topics are:

- Additional Spatial Operations

- Specialised Primitives

- Spatial Interactions

- Automatic Creation of Property Boundaries



---

[← MapLink OGC Services SDK](ogc-services-sdk) | [GML SDK →](gml-sdk)