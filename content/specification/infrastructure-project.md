---
specification: infrastructure-project
name: infrastructure project
plural: infrastructure projects
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-09-14'
version: 1.1.1
datasets:
    - dataset: infrastructure-project
      name: Infrastructure project
      fields:
          - field: reference
            description: the NSIP id
          - field: name
            description: the name of the project
          - field: description
            description: a brief description of the project
          - field: applicant-organisation
            description: the organisation id of the organisation making the application
          - field: infrastructure-project-decision
            dataset: infrastructure-project-decision
            description: the decision, once it has been made. For example `consent-granted`
          - field: decision-date
            description: the date the decision was made, for example `2023-09-14`
          - field: decision-maker
            description: which secretary of state made the decision
          - field: geometry
            description: the site boundary for the proposed development
          - field: point
          - field: documentation-url
            description: a url to a page with more information about the project
          - field: infrastructure-project-type
            dataset: infrastructure-project-type
            description: the type of project, for example generating-stations
          - field: notes
            description: any additional notes in this field
          - field: organisation
            description: the organisation id of the organisation that provided this data
          - field: entry-date   
          - field: start-date
          - field: end-date
    - dataset: infrastructure-project-log
      name: Infrastructure project log
      fields:
          - field: reference
          - field: infrastructure-project
            description: the ID of the infrastructure project
          - field: infrastructure-project-event
            dataset: infrastructure-project-event
            description: an event reference for something that has happened during the process
          - field: event-date
            description: the date the event happened, for example `2023-09-14`
          - field: notes
            description: any additional notes in this field
          - field: organisation
            description: the organisation id of the organisation that provided this data
          - field: entry-date   
          - field: start-date
          - field: end-date
    - dataset: infrastructure-project-document
      name: Infrastructure project document
      fields:
          - field: reference
          - field: infrastructure-project
            description: the ID of the infrastructure project
          - field: document-type
            dataset: infrastructure-project-document-type
            description: the type of document, for example development-consent-order
          - field: name
            description: a name for the document
          - field: notes
            description: any additional notes in this field
          - field: organisation
            description: the organisation id of the organisation that provided this data
          - field: document-url
            description: a url to the document
          - field: documentation-url
            description: a url to the webpage where the document has been published
          - field: entry-date   
          - field: start-date
          - field: end-date
---
