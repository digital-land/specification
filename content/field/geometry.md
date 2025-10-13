---
cardinality: '1'
datatype: multipolygon
description: 'A polygon or multipolygon boundary'
end-date: ''
entry-date: ''
field: geometry
guidance: |
    The boundary may be a single polygon, or a multipolygon value.
    All points should be in the WGS84 coordinate reference system.
    You may provide data containing points in another coordinate reference system, such as British National Grid,
    but they will need to be transformed into WGS84 by software such as the Planning Data platform and this transformation may lead to a small loss of accuracy.
    Geometry data provided in a CSV file should use the well-known text (WKT) representation for the field.
    If you're providing geometry in a GeoJSON, GML, Geopackage or KML, use the appropriate representation for the file format.
examples:
    - value: 'POLYGON ((-0.166189 51.572792,-0.166296 …'
    - value: 'MULTIPOLYGON (((-0.166189 51.572792,-0.166296 …'
hint: ''
name: Geometry
parent-field: multipolygon-wkt
replacement-field: ''
start-date: ''
typology: value
uri-template: ''
wikidata-property: ''
---
