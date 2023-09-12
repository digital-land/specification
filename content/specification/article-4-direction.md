---
specification: article-4-direction
name: Article 4 direction
plural: article 4 directions
specification-status: piloting
start-date: ''
end-date: ''
entry-date: '2023-09-11'
version: 1.2.2
datasets:
    - dataset: article-4-direction
      name: article 4 direction
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the article 4 direction
        - field: name
        - field: description
        - field: documentation-url
        - field: document-url
        - field: notes
        - field: organisation
        - field: entry-date
        - field: start-date
        - field: end-date
    - dataset: article-4-direction-area
      name: article 4 direction area
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the article 4 direction area
        - field: name
        - field: article-4-direction
          description: the <a href="#reference">reference</a> for the <a href="article-4-direction-dataset">article 4 direction</a> entry
        - field: permitted-development-right
          description: a list of one or more <a href="#reference">reference</a> values for <a href="article-4-direction-rule-dataset">permitted development right</a> entries, separated by a semi-colon ';'.
        - field: uprn
          dataset: address
        - field: address-text
        - field: geometry
        - field: point
        - field: notes
        - field: organisation
        - field: entry-date
        - field: start-date
        - field: end-date
---
