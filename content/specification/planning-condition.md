---
specification: planning-condition
name: Planning condition
plural: Planning conditions
specification-status: working-draft
specification-reason: prospective
consideration: planning-conditions
start-date: ''
end-date: ''
entry-date: '2023-11-09'
github-discussion: 40
version: 1.5.0
datasets:
    - dataset: planning-condition
      name: planning condition
      fields:
        - field: reference
          description: a reference for the planning condition
        - field: name
          description: a name used for this planning condition
        - field: description
          description: text explaining the condition
        - field: reason
          description: a text reason for the condition
        - field: organisation
          description: the organisation that created the condition
        - field: notes
          description: any additional notes about the condition
        - field: entry-date
          description: the date the condition record was created
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record starts
    - dataset: planning-application-condition
      name: planning application condition
      fields:
        - field: reference
          description: a reference for the planning application - condition connection
        - field: planning-application
          dataset: planning-application
          description: a planning application reference
        - field: planning-condition
          dataset: planning-condition
          description: a planning condition reference
        - field: document-url
          description: a url to the decision notice that includes details of the condition applying to the planning application
        - field: documentation-url
          description: a url to a page where it is possible to find the decision notice
        - field: description
          description: a description of the condition applied to the application
        - field: organisation
          description: the organisation that as added the condition to the planning application
        - field: notes
          description: any additional notes about the planning application - condition connection
        - field: entry-date
          description: the date the record was created
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record starts
---
