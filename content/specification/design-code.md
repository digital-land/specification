---
considerations: design-codes
datasets:
- dataset: design-code
  fields:
  - description: the <a href="#reference">reference</a> for the design code
    field: reference
  - description: the name, or title of the design code
    field: name
  - description: a short, single-line description of the design code
    field: description
  - dataset: design-code-status
    description: a <a href="#design-code-status">design-code-status</a> reference
    field: design-code-status
  - description: the URL for the Web page with guidance on the design code policy
      document
    field: documentation-url
  - description: the URL for the Design Code. This should be a URL to a website or
      document
    field: document-url
  - description: optional notes on the status of the design code
    field: notes
  - description: the <a href="#date">date</a> the design code comes, or came into
      force
    field: start-date
  - description: the <a href="#date">date</a> this date the design code no longer
      applies
    field: end-date
  - description: the <a href="#date">date</a> this entry was created or last amended
    field: entry-date
  name: design code
- dataset: design-code-rule
  fields:
  - description: the <a href="#reference">reference</a> for the design code rule
    field: reference
  - description: the name, or title of the design code rule
    field: name
  - description: the <a href="#reference">reference</a> for the design code where
      this rule is defined.
    field: design-code
  - description: a short, single-line description of the design code rule
    field: description
  - description: the URL for the design code rule. This should be a URL to a website
      or document
    field: document-url
  - description: the URL for a page where we can find a link to the design code rule,
      this is usually a contents or summary page
    field: documentation-url
  - dataset: design-code-rule-category
    description: a list of one or more <a href="#design-code-category">design-code-rule-categories</a>
      references, separated by a semi-colon ';' character
    example: public-art;building-height
    field: design-code-rule-categories
  - description: a field to capture notes about the design code rule
    field: notes
  - description: the date this information has been entered as a record
    field: entry-date
  - description: the date the validity of the record starts
    field: start-date
  - description: the date the validity of the record ends
    field: end-date
  name: design code rule
- dataset: design-code-area
  fields:
  - description: the <a href="#reference">reference</a> for the design code area
    field: reference
  - description: the name, or title of the design code area
    field: name
  - description: the boundaries of the design code area as a POLYGON or MULTIPOLYGON,
      with points in the EPSG 4326 coordinate reference system, and WGS85 datum, encoded
      in Well-Known Text (WKT) representation of geometry.
    field: geometry
  - description: the <a href="#reference">reference</a> for the design code which
      applies to this area
    field: design-code
  - description: a list of one or more <a href="#reference">reference</a> values for
      <a href="design-code-rule-dataset">design code rule</a> entries, separated by
      a semi-colon ';' character.
    field: design-code-rules
  - dataset: design-code-area-type
    description: the classification of the area, for example Rural Settlements or
      Urban Neighbourhood
    field: design-code-area-type
  - description: the URL for guidance or information defining the design code area
    field: documentation-url
  - description: a field to capture notes about the design code area
    field: notes
  - description: the date this information has been entered as a record
    field: entry-date
  - description: the date the validity of the record starts
    field: start-date
  - description: the date the validity of the record ends
    field: end-date
  name: design code area
end-date: ''
entry-date: '2022-06-09'
github-discussion: 27
name: Design code
plural: design codes
specification: design-code
specification-reason: prospective
specification-status: working-draft
start-date: ''
---
