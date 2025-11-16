---
specification: design-code
name: Design code
plural: design codes
specification-status: working-draft
specification-reason: prospective
considerations: design-codes
start-date: ''
end-date: ''
entry-date: '2022-06-09'
github-discussion: 27
datasets:
    - dataset: design-code
      name: design code
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the design code
        - field: name
          description: the name, or title of the design code
        - field: description
          description: a short, single-line description of the design code
        - field: design-code-status
          description: a <a href="#design-code-status">design-code-status</a> reference
          dataset: design-code-status
        - field: documentation-url
          description: the URL for the Web page with guidance on the design code policy document
        - field: document-url
          description: the URL for the Design Code. This should be a URL to a website or document
        - field: notes
          description: optional notes on the status of the design code
        - field: start-date
          description: the <a href="#date">date</a> the design code comes, or came into force
        - field: end-date
          description: the <a href="#date">date</a> this date the design code no longer applies
        - field: entry-date
          description: the <a href="#date">date</a> this entry was created or last amended
    - dataset: design-code-rule
      name: design code rule
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the design code rule
        - field: name
          description: the name, or title of the design code rule
        - field: design-code
          description: the <a href="#reference">reference</a> for the design code where this rule is defined.
        - field: description
          description: a short, single-line description of the design code rule
        - field: document-url
          description: the URL for the design code rule. This should be a URL to a website or document
        - field: documentation-url
          description: the URL for a page where we can find a link to the design code rule, this is usually a contents or summary page
        - field: design-code-rule-categories
          description: a list of one or more <a href="#design-code-category">design-code-rule-categories</a> references, separated by a semi-colon ';' character
          example: 'public-art;building-height'
          dataset: design-code-rule-category
        - field: notes
          description: a field to capture notes about the design code rule
        - field: entry-date
          description: the date this information has been entered as a record
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record ends
    - dataset: design-code-area
      name: design code area
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the design code area
        - field: name
          description: the name, or title of the design code area
        - field: geometry
          description: the boundaries of the design code area as a POLYGON or MULTIPOLYGON, with points in the EPSG 4326 coordinate reference system, and WGS85 datum, encoded in Well-Known Text (WKT) representation of geometry.
        - field: design-code
          description: the <a href="#reference">reference</a> for the design code which applies to this area
        - field: design-code-rules
          description: a list of one or more <a href="#reference">reference</a> values for <a href="design-code-rule-dataset">design code rule</a> entries, separated by a semi-colon ';' character.
        - field: design-code-area-type
          dataset: design-code-area-type
          description: the classification of the area, for example Rural Settlements or Urban Neighbourhood
        - field: documentation-url
          description: the URL for guidance or information defining the design code area
        - field: notes
          description: a field to capture notes about the design code area
        - field: entry-date
          description: the date this information has been entered as a record
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record ends
---
