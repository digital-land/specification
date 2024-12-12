---
specification: community-infrastructure-levy
name: Community infrastructure levy
plural: Community infrastructure levy
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2024-12-12'
github-discussion: 99
version: 1.0.0
datasets:
    - dataset: community-infrastructure-levy-schedule
      description: "A document that sets out the CIL charge rates for an area"
      fields:
        - field: reference
          description: a unique code for this document record, for example `ADU/1`
        - field: name
          description: a name for the document, for example, CIL Schedule 2023
        - field: description
          description: a field to provide details about the document
        - field: document-url
          description: a URL to the publication whether it is document, such as a pdf, or a webpage
        - field: documentation-url
          description: a URL to the page on a planning authority site where this document is published
        - field: organisation
          description: a code for the organisation that published the schedule
        - field: adopted-date
          description: the date the schedule was adopted, for example 2024-12-01
        - field: notes
          description: optional notes
        - field: entry-date
          description: the date this record was created
        - field: start-date
          description: the date the document was published
        - field: end-date
          description: the date this document was superseded
---
