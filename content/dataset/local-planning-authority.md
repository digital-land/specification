---
attribution: ons-boundary
collection: local-planning-authority
consideration: local-planning-authority
dataset: local-planning-authority
description: Local Planning Authorities and their boundaries
end-date: ''
entity-maximum: '626999'
entity-minimum: '624000'
entry-date: ''
fields:
- field: document-url
  guidance: 'Enter the URL of the document, webpage, or data on your website containing
    the

    authorititive "red-line" boundary.

    '
- definition: URL of the [Source documentation](#source-documentation) page
  description: local planning authority documentation page
  field: documentation-url
  guidance: 'Enter the URL of the webpage on your website where information about
    the Local Planning Authority

    including the boundary may be found.

    '
- field: end-date
  guidance: 'Enter the date this area ceased to be a Local Planning Authority.

    '
- field: entity
  guidance: 'The value is managed by the Planning Data platform.

    '
- field: entry-date
- description: Local Planning Authority boundary
  field: geometry
- description: Local Planning Authority name
  examples:
  - value: Old Oak and Park Royal Development Corporation (OPDC)
  field: name
  guidance: 'Enter the name of the Local Planning Authority.

    '
- examples:
  - value: "The London Legacy Development Corporation was planning authority for its
      area until the end of November 2024.\nAll enquiries in respect of planning policy
      and Community Infrastructure Levy should now be made to \nthe relevant borough.\n"
  field: notes
  guidance: 'Enter any notes to help a user understand how the data was made or is
    to be interpreted.

    '
- description: organisation responsible for the Local Planning Authority designation
  field: organisation
  guidance: 'The value is managed by the Planning Data platform.

    '
- field: point
  guidance: 'The value is managed by the Planning Data platform.

    '
- field: prefix
  guidance: 'The value is managed by the Planning Data platform.

    '
- examples:
  - value: E60000330
  - value: borchester-development-corporation
  field: reference
  guidance: "Enter the GSS code for the Local Planning Authority area. \nYou can create
    a unique reference where no GSS code exists and\nrepublish the data with the official
    GSS code once it is known.\n"
- field: region
- field: start-date
  guidance: 'Enter the date this area became a Local Planning Authority.

    '
github-discussion: 36
guidance: "A mayoral authority, or other organisation responsible for the designation
  of a \ndevelopment corporation or other kind of Local Planning Authority can use
  this \nspecification to provide the boundary of the Local Planning Authority area.\n"
key-field: ''
licence: ogl3
name: Local Planning Authority
notes: "The `local-planning-authority` dataset name was taken from the name used by
  \nthe Office of National Statistics (ONS) for the Local Planning Authority \nboundary.
  It describes the statistical geography rather than the organisational\nrole, which
  is also known as the \"Local Planning Authority\" (LPA).\n"
paint-options: ''
phase: beta
plural: Local Planning Authorities
prefix: statistical-geography
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- administrative
typology: geography
wikidata: Q6664495
wikipedia: Local_planning_authority
---

This dataset contains the administrative boundary for each Local Planning Authority (LPA) in England.

It can be used to:
<ul>
<li>assist in the production planning and other statistics</li>
<li>help find the LPA responsible for a planning application on a map, for example</li>
</ul>
