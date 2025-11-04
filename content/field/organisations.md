---
cardinality: n
datatype: string
description: 'list of organisations.'
end-date: ''
entry-date: ''
field: organisations
guidance: |   
    A list of CURIE references for one or more organisations.
    Where you need to list more than one organisation, separate the values with a semicolon ';' character.
    You can find the CURIE reference for each organisation from our [list of organisations](https://www.planning.data.gov.uk/organisation/).
    The CURIE is made from the prefix value, followed by a colon ':' character, and then the reference value for the organisation being identified. 
    You may leave this value blank when the list of organisations is just the single organisation providing the data.
examples:
  - value: 'local-authority:DUR'
  - value: 'national-park-authority:Q72617158'
  - value: 'local-authority:LIC;local-authority:NKE;local-authority:WLI'
hint: ''
name: Organisations
parent-field: organisation
replacement-field: ''
start-date: ''
typology: organisation
uri-template: ''
wikidata-property: ''
---
