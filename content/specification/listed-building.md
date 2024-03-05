---
specification: listed-building
name: Listed building outline
plural: Listed building outlines
specification-status: piloting
start-date: ''
end-date: ''
entry-date: '2022-06-09'
github-discussion: 44
version: 1.1.1
datasets:
    - dataset: listed-building-outline
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the listed building
        - field: name
          description: the name of the listed building
        - field: listed-building
          description: the Historic England <a href="#reference">reference</a> for the listed building
        - field: listed-building-grade
          description: the Historic England listed-building-grade value for the listed building
        - field: geometry
          description: the boundary of the listed building in WKT format 
        - field: document-url
          description: the URL of the web page where you can find the document for the listed building
        - field: notes
          description: optional notes
        - field: organisation
          description: the organisation responsible for listed buildings
        - field: entry-date
          description: the date this information has been entered as a record
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record ends
---
