---
title: "GML SDK"
---

# GML SDK


## Library Usage and Configuration

As with most MapLink SDKs, the MapLink GML SDK comes in 2 flavours. It
should be noted that the library to be linked with should be determined
by the Core SDK library that you are using within your application. For
example, if you are using the Release mode, DLL version of the Core SDK
(MapLink.lib/MapLink64.lib) then you must also use the equivalent GML
SDK library (MapLinkGML.lib/MapLinkGML.lib).

+----------------------------------+-----------------------------------+
| **MapLinkGML.lib or              | **MapLinkGMLd.lib or              |
| MapLinkGML64.lib**               | MapLinkGML64d.lib**               |
|                                  |                                   |
| Release mode, DLL version.       | Debug mode, DLL version.          |
|                                  |                                   |
| Uses Multithreaded DLL C++       | Uses Debug Multithreaded DLL C++  |
| run-time library.                | run-time library.                 |
|                                  |                                   |
| Requires TTLDLL preprocessor     | Requires TTLDLL preprocessor      |
| directive.                       | directive.                        |
|                                  |                                   |
| Must also link the MapLink Core  | Must also link the MapLink Core   |
| SDK library MapLink.lib          | SDK library MapLinkd.lib          |
|                                  |                                   |
| Refer to the document \"MapLink  | No redistributable run-time       |
| Pro X.Y: Deployment of End User  | available.                        |
| Applications\" for a list of     |                                   |
| run-time dependencies when       |                                   |
| redistributing.                  |                                   |
|                                  |                                   |
| Where X.Y is the version of      |                                   |
| MapLink you are deploying.       |                                   |
+----------------------------------+-----------------------------------+

The MapLink GML SDK is runtime locked meaning that before it may be used
on any machine it must be unlocked programmatically. This is achieved
using the TSLUtilityFunctions class by calling the unlockSupport method,
passing the TSLKeyedGML enumeration value and the required unlock code.
The unlock code can be provided on request from Envitia Sales, subject
to licensing.

## Supported Capabilities

The MapLink GML SDK offers the ability to read and write GML Application
Schemas and corresponding instance data that either conforms to the
'Geography Markup Language (GML) Simple Features Profile' level 0 (SF-0)
or GML of an equivalent complexity, that conforms to GML version
3.1.1.[^9]

Non-SF-0 compliant instance data should use the 'FeatureCollection' top
level collection element.

If either the application schema or instance data is found to be
incompatible during ingest, the GML library will attempt to continue but
will disregard those feature definitions or feature instances that were
not understood. The incompatible feature definitions or feature
instances can be returned to the caller as self-contained blocks of XML
if the relevant callback has been set.

A correctly defined GML feature definition should inherit from the
gml:AbstractFeatureType type, which defines several properties that all
derivates inherit. MapLink does not support the use of the base
properties except for attribute gml:id. Instead the gml:id is added to
all feature definitions and will be named 'gml:id'.

MapLink requires that a GML instance data document only use a single
coordinate reference system (CRS) for all geometry data. If a document
uses more than one CRS, all uses of subsequent CRSs will cause the
containing feature or features to be rejected.

## GML Application Schemas 

### Schema Storage

The information read from a GML Application Schema, or used to write
one, is represented by a TSLGMLApplicationSchema object. This class
gives access to such properties as the version, target namespace, target
namespace prefix and conforming GML profile of the schema.

The TSLGMLApplicationSchema class also offers the ability save the
feature definitions it contains to a MapLink TSLStandardDataLayer
object, through its applyToLayer method. The saving of feature
definitions conforms to the following steps:

- Each feature definition is mapped to a MapLink 'feature' and can
  therefore be queried from the layer's feature class list. The name of
  the MapLink feature will be the same as the feature definition's
  enclosing XML tag.

- Each geometry property of a feature definition is added as a 'Source
  Info' property of the MapLink feature class. The details of these
  'Source Info' objects can be queried via the TSLFeatureClassList
  class' getSourceInfoItem and getSourceInfoCount methods. 'Source Info'
  items can be added, removed or updated via the TSLStandardDataLayer
  class' addSourceInfo, deleteSourceInfo and updateSourceInfo methods.

The 'Source Info' details are mapped in the following way to each
geometric feature property:

- The sourceName value corresponds to enclosing GML tags of the feature
  property

- The sourceID value corresponds to the zero-based index of the feature
  property. This allows the order of geometric and non-geometric feature
  properties to be maintained or determined.

- The sourceDescription value corresponds to GML annotation associated
  with the feature property, should one exist or wish to be set.

- The sourceType value corresponds to the type of GML geometry
  permitted. The following table lists the supported abstract GML
  geometry types and their corresponding values in the TSLGeometryType
  enumeration.

  ---------------------------------------------------------
  GML Type                   TSLGeometryType value
  -------------------------- ------------------------------
  Point                      TSLGeometryTypeSymbol

  Curve                      TSLGeometryTypePolyline

  Surface                    TSLGeometryTypePolygon

  Geometry                   TSLGeometryTypeEntity

  MultiPoint                 TSLGeometryTypeMultiPoint

  MultiCurve                 TSLGeometryTypeMultiPolyline

  MultiSurface               TSLGeometryTypeMultiPolygon

  MultiGeometry              TSLGeometryTypeEntitySet
  ---------------------------------------------------------

- The minOccurs and maxOccurs values correspond to the multiplicity of
  the property. Only positive values are valid, except for -1 for
  maxOccurs which is used to denote there being no upper limit.

<!-- -->

- Each non-geometry property of a feature definition is added to the
  TSLDataHandler of the Standard Data Layer, as a 'field definition'.
  The ways of interacting and the information stored in this class have
  been changed from previous versions of MapLink. MapLink 6.0 introduced
  a new class, TSLFieldDefinition, which represents a single 'field
  definition' or, in this case, a feature property definition.

A feature property definition maps to the fields of the
TSLFieldDefinition class in the following ways:

- The name value corresponds to the enclosing GML tags of the feature
  property.

- The type value corresponds to the GML SF-0 supported type of which the
  field is defined as. The following table lists how the schema type
  supported by SF-0 is mapping to a
  [TSLVariantType](mk:@MSITStore:C:\Temp\MapLinkAPI.chm::/rosefiles/cat421218fc015a/cat37a038e10247/class3ec0b8f703ca.htm)
  value

  ----------------------------------------------------------
  Schema Type                    TSLVariantType value
  ------------------------------ ---------------------------
  xsd:integer                    TSLVariantTypeLong

  xsd:double                     TSLVariantTypeDouble

  xsd:string                     TSLVariantTypeStr

  xsd:date and xsd:dateTime[^10] TSLVariantTypeDateTime

  xsd:boolean                    TSLVariantTypeBool

  Extensions of xsd:base64Binary TSLVariantTypeBinary
  and xsd:hexBinary              

  xsd:anyURI                     TSLVariantTypeURI

  xsd:ReferenceType              TSLVariantTypeReference

  Restrictions of gml:CodeType   TSLVariantTypeCode

  Restrictions of                TSLVariantTypeMeasurement
  gml:MeasureType                
  ----------------------------------------------------------

- The minOccurs and maxOccurs values correspond to the multiplicity of
  the property. Only positive values are valid, except for -1 for
  maxOccurs which is used to denote there being no upper limit.

- The maxExclusive, maxInclusive, minExclusive and minInclusive values
  map to the schema facets of the same name. MapLink stores each value
  as a TSLVariant, which are meant to hold the appropriate value. The
  variant type should be the same as the field to which they belong.

- The length, minLength and maxLength values map to the schema facets of
  the same name.

- The enumeration value may hold an array of objects of the same type as
  the field to represent the enumeration schema facet.

- The nillable value is used to denote if the GML property is nullable.

- The precision value may hold the fraction digits schema facet value.

- The encoding field is used in certain cases to hold additional
  information. gml:CodeType types for instance store in this field their
  fixed or default constraint value, should one be defined.

- The referenceTargetType value is used to hold the targetElement value
  from a correctly formed gml:ReferenceType typed feature property
  declaration.

### Schema Ingest 

To load a GML Application Schema, first construct an instance of the
TSLGMLApplicationSchemaLoader class. The following can optionally be set
on the loader class before loading a schema:

- When loading a GML SF-0 compliant schema, it is possible to check that
  the schema is correct through using the gmlSFValidationLevel option.
  When turned on, this option will check the schema against the
  validation rules defined in the GML Simple Features profile.

- The strictValidation option can be used to perform more rigorous
  checks of the correctness of the schema. This is independent of any
  GML or GML SF-0 checks.

- The unhandledFeatureDefinitionCallback methods can be used to provide
  the loader with a callback that will be called whenever a feature
  definition is encountered that is not supported.

- During schema loading, any dependant schemas are also loaded using the
  URL referenced in the schema file. For cases when those addresses are
  no longer correct or inaccessible, the urlLoaderCallback methods allow
  a callback to be set that will redirect the loading address.

Finally the schema document may either the loaded from a file, URL or
buffer using one of the loadSchema methods. On successful loading of a
schema document, an instance of the TSLGMLApplicationSchema class will
be returned.

### Schema Creation and Export

To create a GML schema using the MapLink GML library, a
TSLGMLApplicationSchemaFactory is used. It should be provided with
instances of the TSLStandardDataLayer and
TSLGMLApplicationSchemaCreationParameters classes. The standard data
layer should define the features that the schema should contain while
the parameters class will contain the namespace, namespace prefix,
version and GML profile to conform to. How to define GML features is
described in section [24.3.1](#schema-storage).

Optionally, a third parameter may be passed to the schema factory: a
TSLGMLPropertyMapping or TSLGMLPropertyMappingSet class instance. These
can be used to define additional feature properties whose values are
determined by the rendering attributes of MapLink geometry. This concept
will be described in more detail in section
[24.4.1.1](#schema-based-instance-data-ingest-and-storage), but it is
necessary to define those feature properties on the schema for instance
data to conform to its application schema.

On successful creation of a schema, an instance of the
TSLGMLApplicationSchema class is returned. Instances of this class can
be used to write the schema to a file or buffer using the
TSLGMLApplicationSchemaWriter class. All schemas written by MapLink will
reference the opengis.net website for their dependent GML schemas.

## GML Instance Data Ingest and Export

### Instance Data Ingest and Storage

GML instance data can be loaded using MapLink via the
TSLGMLInstanceDataLoader class. The information read from a GML instance
data document, or used to write one, is stored in a MapLink
TSLStandardDataLayer. The root TSLEntitySet will contain a child entity
that represents each GML feature instance. This means that every GML
feature instance read or written using MapLink must contain at least one
geometric property.

As noted in section [24.2](#supported-capabilities), all GML instance
data either ingested or exported must be in a single coordinate
reference system. When ingesting data, the TSLGMLInstanceDataLoader
class will also return a TSLCoordinateSystem that represents that CRS.

Exactly how the information is store depends upon a number of factors,
but one of the key ones is whether MapLink reads the instance data's
schema. This is due to MapLink being capable of reading instance data
without ever reading the schema; helpful if the schema is unavailable or
not compatible with MapLink. When reading without a schema, MapLink
treats all non-geometric properties as string values as it is not
capable of determining their type. The following sections therefore deal
with how the instance data is read and stored depending upon whether a
schema was used to load it.

#### Schema Based Instance Data Ingest and Storage

The following rules define how the feature instance is stored as a
MapLink entity:

- If the feature is defined as having more than one geometric property
  or the multiplicity of the geometric property allows for zero or
  multiple instances of the property, then the root MapLink entity that
  represents the feature instance will be a TSLEntitySet. Each child
  entity within the root entity set will have its new dataSourceID field
  set to denote the index of the 'Source Info' item to which it belongs.

For instance, if a feature defines two geometric properties; property
'A' with a multiplicity of 0..n and property 'B' with a multiplicity of
1..1. The instance data document contains just two feature instances.
The first instance of that feature does not contain any 'A's but
contains the required 'B' property. The second instance of that feature
contains two 'A's and a 'B'. Therefore the standard data layer's entity
set will contain two child entity sets; the first representing the first
feature instance and the second set representing the second instance.
The first child entity set, representing the first feature, will in turn
contain one child entity representing property 'B' and that entity will
have its dataSourceID set to 2. The second child entity set will in turn
contain three child entities representing the two 'A' properties and one
representing 'B'. These child entities will have the following
dataSourceID values: 1, 1 and 2.

Alternatively, if the feature only defines a single geometric property
with a minOccurs and maxOccurs of 1, then the geometry for that property
will be used to represent the feature.

The reason for these two different schemes is to reduce the memory
footprint of an application loading large amounts of instance data in
the more common, latter, scenario.

- The TSLDataSet of the root entity representing the feature instance
  will be populated with non-geometric properties' values. By examining
  the standard data layer's TSLDataHandler, the two-character lookup key
  can be determined to discover the value of a particular property's
  value.

If a feature instance contains multiple instances of a property, then
the dataset will be populated with multiple values for that property.

If the property is nil, then the TSLVariant's isNil property will be set
to true. Should a nilReason also be present, the variant will also
contain a string value containing the content of this attribute.

- Using either a TSLGMLPropertyMapping or TSLGMLPropertyMappingSet class
  instance, it is however possible to map feature property values to the
  rendering attributes and other properties of the root entity
  representing the feature instance. Rather than a property's value
  being added to the TSLDataSet, it could for instance be set as the
  root entity's name or entity id.

The TSLGMLPropertyMapping class is used to setup a mapping for all types
of features in the same way. Whereas the TSLGMLPropertyMappingSet class
can setup a different mapping for each feature type.

The mapping object is not only used during reading of instance data but
also when writing it. The process is simple reversed with the values of
feature property's being determined from the root entity representing
the feature.

MapLink offers two ways in which instance data can be loaded with a
schema; Pre-load the schema using a TSLGMLApplicationSchemaLoader class
or by loading the schema at the same time from the location referenced
in the instance data document. The benefit of the former being that
multiple instance data documents, that use the same schema, can be
loaded serially far quicker than via the latter.

#### Schemaless Instance Data Ingest and Storage

The following rules define how the feature instance is stored as a
MapLink entity:

- In the same way as the schema-based storage, the root entity used to
  represent the feature instance is determined by how many geometric
  properties the feature 'appears' to contain. The problem being that
  MapLink can only use the feature instances that the instance data
  document contains to make this determination. This can lead to two
  instance data documents, based upon the same original schema, being
  loaded and stored differently.

As with the schema-based loading, if all seen instances of a feature
always contain a single geometry property, then that geometry object is
used to represent the feature in the MapLink standard data layer's root
entity set. Otherwise a TSLEntitySet is used and all the geometric
properties are added as child entities.

- The TSLDataSet of the root entity representing the feature instance
  will again be populated with non-geometric properties' values. All of
  the entries will be of type TSLVariantTypeStr type with the exception
  of correctly formed restrictions of 'gml:MeasureType' which will be
  formed into TSLVariantTypeMeasurement types.

As all non-geometric properties are treated as strings, this means that
only the content of the property will be stored. Any XML attributes on
the enclosing property tags encountered when reading the instance data
will be ignored.

- As with the schema-based loading, either a TSLGMLPropertyMapping or
  TSLGMLPropertyMappingSet class instance can optionally be used when
  loading without a schema. These mapping classes allow feature property
  values to be used to populate rendering attributes and other
  properties of the root MapLink entity representing the feature
  property.

#### Instance Data Ingest Options

The following options can be set on the TSLGMLInstanceDataLoader class
to control aspects of the ingest:

- The mapUnitShiftX, mapUnitShiftY and tmcPerMU options provide control
  over how GML geometries are converted into TMC space.

- The swapXandY option sets whether the GML coordinates ingested should
  be treated as Y, X rather than X, Y.

- The propertyMapping and propertyMappingSet methods allow the settings
  of a mapping that will be used by subsequent loads. How these mappings
  alter the ingest process is described in section
  [24.4.1.1](#schema-based-instance-data-ingest-and-storage).

- The unhandledFeatureCallback method allows a callback to be set on the
  loaded that will be called whenever the loader encounters a feature
  instance that it cannot process. This may occur if the instance is of
  a feature type that is not supported by MapLink, contains a GML
  geometry type that is not supported or when a feature instance is
  encountered that is too complex during schema-less loading.

### Instance Data Export

Exporting GML instance data requires it to be contained by a
TSLStandardDataLayer in the same form as schema-based reading populates
a layer. Exporting is performed by the TSLGMLInstanceDataWriter class
and must be provided with both the TSLStandardDataLayer and a
TSLCoordinateSystem class instance. The TSLCoordinateSystem describes
both the CRS that the GML instance data will be written in and how to
convert the TMC based geometry into Map Units (MUs).

MapLink also requires the schema to be provided to the exporter so that
it can determine the format of the output. This schema can either be
loaded using the TSLGMLApplicationSchemaLoader or created using the
TSLGMLApplicationSchemaFactory.

Lastly, the export call can optionally be provided with a location at
which the schema should be referenced. This location will be used to
populate the schemaLocation XML attribute of the GML instance data
document.

The following options are also available when exporting instance data
and should be set on the exporter prior to the export call being made:

- The swapXandY option sets whether the GML coordinates exported should
  be treated as Y, X rather than X, Y.

- The propertyMapping and propertyMappingSet methods allow the settings
  of a mapping that will be used by subsequent exports. These mappings
  work in the reverse of how the ingest process uses them, thus the
  entity's properties are used to create the exported feature's
  properties. How these mappings alter the ingest process is described
  in section [24.4.1.1](#schema-based-instance-data-ingest-and-storage).



---

[← Spatial SDK](spatial-sdk) | [.NET SDKs →](net-sdks)
