---
specification: article-4-direction
name: Article 4 direction
plural: article 4 directions
specification-status: candidate-standard
start-date: ''
end-date: ''
entry-date: '2023-09-11'
github-discussion: 30
version: 1.3.3
datasets:
    - dataset: article-4-direction
      name: article 4 direction
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the article 4 direction
        - field: name
          description: the name of the article 4 direction
        - field: description
          description: a brief description of the article 4 direction
        - field: documentation-url
          description: the URL of the web page where you can find information about the article 4 direction
        - field: document-url
          description: the URL of the web page where you can find the document for the article 4 direction
        - field: notes
          description: optional notes
        - field: organisation
          description: the organisation responsible for this article 4 direction
        - field: entry-date
          description: the date this information has been entered as a record
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record ends
    - dataset: article-4-direction-area
      name: article 4 direction area
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the article 4 direction area
        - field: name
          description: the name of the article 4 direction area
        - field: article-4-direction
          description: the <a href="#reference">reference</a> for the <a href="article-4-direction-dataset">article 4 direction</a> entry
        - field: permitted-development-rights
          description: a list of one or more <a href="#reference">reference</a> values for <a href="article-4-direction-rule-dataset">permitted development right</a> entries, separated by a semi-colon ';'.
          dataset: permitted-development-right
        - field: uprns
          description: unique property reference numbers for any addressable properties, separated by `;`
        - field: address-texts
          description: the addresses of any properties reference. The addresses should be written as address-text (a single line separated by commas). To write multiple address end each address with `;`
        - field: geometry
          description: the boundary of the area covered by the article 4 direction in WKT format 
        - field: point
          description: centre point of the area
        - field: notes
          description: optional notes
        - field: organisation
          description: the organisation responsible for article 4 direction area
        - field: entry-date
          description: the date this information has been entered as a record
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record ends
---
