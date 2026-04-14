---
consideration: planning-conditions
datasets:
- dataset: planning-condition
  fields:
  - description: a reference for the planning condition
    field: reference
  - description: a name used for this planning condition
    field: name
  - description: text explaining the condition
    field: description
  - description: a text reason for the condition
    field: reason
  - description: the organisation that created the condition
    field: organisation
  - description: any additional notes about the condition
    field: notes
  - description: the date the condition record was created
    field: entry-date
  - description: the date the validity of the record starts
    field: start-date
  - description: the date the validity of the record starts
    field: end-date
  name: planning condition
- dataset: planning-application-condition
  fields:
  - description: a reference for the planning application - condition connection
    field: reference
  - dataset: planning-application
    description: a planning application reference
    field: planning-application
  - dataset: planning-condition
    description: a planning condition reference
    field: planning-condition
  - description: a url to the decision notice that includes details of the condition
      applying to the planning application
    field: document-url
  - description: a url to a page where it is possible to find the decision notice
    field: documentation-url
  - description: a description of the condition applied to the application
    field: description
  - description: the organisation that as added the condition to the planning application
    field: organisation
  - description: any additional notes about the planning application - condition connection
    field: notes
  - description: the date the record was created
    field: entry-date
  - description: the date the validity of the record starts
    field: start-date
  - description: the date the validity of the record starts
    field: end-date
  name: planning application condition
end-date: ''
entry-date: '2023-11-09'
github-discussion: 40
name: Planning condition
plural: Planning conditions
specification: planning-condition
specification-reason: prospective
specification-status: working-draft
start-date: ''
---
