---
specification: infrastructure-funding-statement
name: Infrastructure funding statement
plural: Infrastructure funding statements
specification-status: piloting
start-date: ''
end-date: ''
entry-date: '2023-11-23'
version: 1.1.1
datasets:
    - dataset: infrastructure-funding-statement
      fields:
        - field: reference
          description: a unique identifier for the IFS document
        - field: name
          description: the name given to the IFS document
        - field: document-url
          description: a url to the IFS document
        - field: documentation-url
          description: a url to the page where the IFS document has been published
        - field: organisation
          description: a reference to the publishing organisation
        - field: notes
          description: any additional notes
        - field: entry-date
          description: the date this record was created
        - field: start-date
          description: the date this record is valid from, for example the date the document was published to the urls provided
        - field: end-date
          description: the date this record is not longer true, for example if the urls to the document change
---
