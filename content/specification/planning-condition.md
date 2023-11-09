---
specification: planning-condition
name: Planning condition
plural: Planning conditions
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-11-09'
version: 1.1.0
datasets:
    - dataset: planning-condition
      name: planning condition
      fields:
        - field: reference
        - field: name
        - field: description
        - field: notes
        - field: organisation
        - field: planning-condition-target
          dataset: planning-condition-target
        - field: planning-condition-type
          dataset: planning-condition-type
        - field: planning-condition-purpose
          dataset: planning-condition-purpose
        - field: entry-date
        - field: start-date
        - field: end-date
    - dataset: planning-application-condition
      name: planning application condition
      fields:
        - field: reference
        - field: planning-application
          dataset: planning-application
        - field: planning-condition
          dataset: planning-condition
        - field: organisation
        - field: applied-date
        - field: discharged-date
        - field: notes
        - field: entry-date
        - field: start-date
        - field: end-date
---
