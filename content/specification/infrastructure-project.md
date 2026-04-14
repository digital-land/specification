---
consideration: nationally-significant-infrastructure-projects
datasets:
- dataset: infrastructure-project
  fields:
  - description: the NSIP id
    field: reference
  - description: the name of the project
    field: name
  - description: a brief description of the project
    field: description
  - description: the organisation id of the organisation making the application
    field: applicant-organisation
  - dataset: infrastructure-project-decision
    description: the decision, once it has been made. For example `consent-granted`
    field: infrastructure-project-decision
  - description: the date the decision was made, for example `2023-09-14`
    field: decision-date
  - description: which secretary of state made the decision
    field: decision-maker
  - description: the site boundary for the proposed development
    field: geometry
  - field: point
  - description: a url to a page with more information about the project
    field: documentation-url
  - dataset: infrastructure-project-type
    description: the type of project, for example generating-stations
    field: infrastructure-project-type
  - description: any additional notes in this field
    field: notes
  - description: the organisation id of the organisation that provided this data
    field: organisation
  - field: entry-date
  - field: start-date
  - field: end-date
  name: Infrastructure project
- dataset: infrastructure-project-log
  fields:
  - field: reference
  - description: the ID of the infrastructure project
    field: infrastructure-project
  - dataset: infrastructure-project-event
    description: an event reference for something that has happened during the process
    field: infrastructure-project-event
  - description: the date the event happened, for example `2023-09-14`
    field: event-date
  - description: any additional notes in this field
    field: notes
  - description: the organisation id of the organisation that provided this data
    field: organisation
  - field: entry-date
  - field: start-date
  - field: end-date
  name: Infrastructure project log
- dataset: infrastructure-project-document
  fields:
  - field: reference
  - description: the ID of the infrastructure project
    field: infrastructure-project
  - dataset: infrastructure-project-document-type
    description: the type of document, for example development-consent-order
    field: document-type
  - description: a name for the document
    field: name
  - description: any additional notes in this field
    field: notes
  - description: the organisation id of the organisation that provided this data
    field: organisation
  - description: a url to the document
    field: document-url
  - description: a url to the webpage where the document has been published
    field: documentation-url
  - field: entry-date
  - field: start-date
  - field: end-date
  name: Infrastructure project document
end-date: ''
entry-date: '2023-09-14'
github-discussion: ''
name: infrastructure project
plural: infrastructure projects
specification: infrastructure-project
specification-reason: prospective
specification-status: working-draft
start-date: ''
---
