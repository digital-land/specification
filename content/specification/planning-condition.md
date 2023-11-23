---
specification: planning-condition
name: Planning condition
plural: Planning conditions
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-11-09'
github-discussion: 40
version: 1.1.1
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
        - field: organisation
          description: the organisation that created the condition
        - field: planning-condition-target
          dataset: planning-condition-target
          description: the target of the condition, for example the planning application or the property
        - field: planning-condition-type
          dataset: planning-condition-type
          description: the type of thing the condition affects, for example permitted development rights
        - field: planning-condition-purpose
          dataset: planning-condition-purpose
          description: the high-level purpose of the condition, for example to restrict
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
          description: a planning conidtion reference
        - field: organisation
          description: the organisation that as added the condition to the planning application
        - field: applied-date
          description: the date the condition applies from
        - field: discharged-date
          description: the date the condition is discharged
        - field: notes
          description: an additional notes about the planning application - condition connection
        - field: entry-date
          description: the date the record was created
        - field: start-date
          description: the date the validity of the record starts
        - field: end-date
          description: the date the validity of the record starts
---
