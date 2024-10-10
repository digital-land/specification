---
specification: conservation-area
name: Conservation area
plural: conservation areas
specification-status: candidate-standard
start-date: ''
end-date: ''
entry-date: '2023-09-08'
github-discussion: 33
version: 1.4.3
datasets:
    - dataset: conservation-area
      fields:
        - field: reference
          description: provide a reference such as CA01
        - field: name
          description: the official name for the conservation area
        - field: designation-date
          description: the date that the conservation area was officially designated
        - field: document-url
          description: a URL to the authoritative source for the area, this is often a PDF containing a map with the area drawn on it
        - field: documentation-url
          description: a URL to a page on the local planning authority website that provides information about the conservation area
        - field: geometry
          description: the boundary of the area covered by the conservation area in WKT format 
        - field: point
          description: provide the centre point of the conservation area if you do not have a full geometry available
        - field: notes
          description: provide any extra information if needed
        - field: organisation
          description: the organisation responsible for conservation areas
        - field: entry-date
          description: the date the information has been entered as a record
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record ends
    - dataset: conservation-area-document
      fields:
        - field: reference
          description: provide a reference such as CA01-decision-notice
        - field: conservation-area
          description: the reference for the conservation area this document is about
        - field: name
          description: the title of the conservation area document
        - field: documentation-url
          description: the URL of the webpage citing the document
        - field: document-url
          description: the URL of the document
        - field: document-type
          dataset: conservation-area-document-type
          description: "the type of the conservation area document which must be one of the following values: 'area-appraisal', 'notice', or leave blank"
        - field: notes
          description: provide any extra information if needed
        - field: organisation
          description: the organisation that published the document
        - field: entry-date
          description: the date this information has been entered as a record
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record ends
---
