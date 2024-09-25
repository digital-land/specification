---
specification: listed-building
name: Listed building outline
plural: Listed building outlines
specification-status: piloting
start-date: ''
end-date: ''
entry-date: '2022-06-09'
github-discussion: 44
version: 1.1.3
datasets:
    - dataset: listed-building-outline
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the listed building
        - field: name
          description: the name of the listed building
        - field: listed-building
          description: the Historic England identifier for the listed building, for example <a href="https://historicengland.org.uk/listing/the-list/list-entry/1024710" class="govuk-link">1024710</a>
        - field: listed-building-grade
          description: the Historic England listed-building-grade value for the listed building
          dataset: listed-building-grade
        - field: geometry
          description: the boundary of the listed building - format under review 
        - field: document-url
          description: the URL of the web page where you can find the document for the listed building
        - field: notes
          description: optional notes
        - field: organisation
          description: the organisation responsible for the listed building
        - field: entry-date
          description: the date this information has been entered as a record
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record ends
---
