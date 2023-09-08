---
specification: conservation-area
name: Conservation area
plural: conservation areas
specification-status: piloting
start-date: ''
end-date: ''
entry-date: '2022-06-09'
version: 1.2.2
datasets:
    - dataset: conservation-area
      fields:
        - field: reference
        - field: name
          description: the official name for the conservation area
        - field: documentation-url
          description: a URL to a page on the local planning authority website that provides information about the conservation area
        - field: geometry
        - field: point
          description: provide the centre point of the conservation area if you do not have a full geometry available
        - field: notes
        - field: organisation
        - field: entry-date
        - field: start-date
        - field: end-date
    - dataset: conservation-area-document
      fields:
        - field: reference
        - field: conservation-area
          description: "the reference for the conservation area this document is about"
        - field: name
          description: the title of the conservation area document
        - field: documentation-url
          description: the URL of the webpage citing the document
        - field: document-url
          description: the URL of the document
        - field: document-type
          dataset: conservation-area-document-type
          description: "the type of the conservation area document which MUST be one of the following values: 'area-appraisal', 'notice', or blank"
        - field: notes
        - field: organisation
        - field: entry-date
        - field: start-date
        - field: end-date
---
