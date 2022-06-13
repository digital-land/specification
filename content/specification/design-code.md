---
specification: design-code
name: design code
plural: design codes
specification-status: working draft
start-date: ''
end-date: ''
entry-date: '2022-06-09'
datasets:
    - dataset: design-code
      name: design code
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the design code
        - field: name
        - field: description
        - field: design-code-status
        - field: design-code-categories
        - field: documentation-url
        - field: document-url
        - field: notes
        - field: start-date
          description: the <a href="#date">date</a> the design code comes, or came into force
        - field: end-date
        - field: entry-date
          description: the <a href="#date">date</a> this entry was created or last amended
    - dataset: design-code-area
      name: design code area
      fields:
        - field: reference
        - field: name
        - field: design-code
        - field: geometry
        - field: documentation-url
        - field: document-url
        - field: notes
        - field: start-date
        - field: end-date
        - field: entry-date
    - dataset: development-document
      name: design code document
      fields:
        - field: reference
        - field: name
        - field: description
        - field: development-document-type
        - field: documentation-url
        - field: document-url
        - field: notes
        - field: start-date
        - field: end-date
        - field: entry-date
---
