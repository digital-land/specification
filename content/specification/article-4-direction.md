---
specification: article-4-direction
name: Article 4 direction
plural: article 4 directions
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2022-06-09'
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
        - field: article-4-direction-rules
          description: a list of one or more <a href="#reference">reference</a> values for <a href="article-4-direction-rule-dataset">article 4 direction rule</a> entries, separated by a semi-colon ';' character.
        - field: uprn
        - field: address-text
        - field: geometry
        - field: document-url
        - field: notes
        - field: organisation
        - field: entry-date
        - field: start-date
        - field: end-date
---
