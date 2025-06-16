---
attribution: crown-copyright
collection: ''
consideration: ''
dataset: transformed
description: the denormalised combination of fact and fact resource produced directly by the pipeline
end-date: ''
entity-maximum: '0'
entity-minimum: '0'
entry-date: ''
fields:
- field: dataset
- field: entity
- field: fact
- field: field
- field: entry-date
  guidance: 'The newest entry-date of this fact with the highest priority from the fact-resource dataset.'
- field: entry-number
- guidance: the row number where the fact can be found in it's resource.
- field: priority
  guidance: 'The lowest priority of any fact-Used to order facts into a history, smaller values are higher priority than larger values.'
- field: reference-entity
  guidance: 'The entity referenced by the value, found using the lookup dataset.'
  field: resource
  guidance: 'The resource where the fact was persent'
- field: start-date
- field: value
licence: ogl3
name: Transformed
paint-options: ''
phase: alpha
plural: Facts
prefix: ''
realm: provenance
replacement-dataset: ''
start-date: ''
typology: value
version: 1.1
wikidata: ''
wikipedia: ''
partitions:
- dataset
- resource
---