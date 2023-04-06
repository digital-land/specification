---
specification: development-plan
name: Development plan
plural: Development plans
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-04-05'
datasets:
    - dataset: development-plan
      name: development plan
      fields:
          - field: reference
          - field: name
          - field: organisation
          - field: development-plan-type
          - field: documentation-url
          - field: period-start-date   
          - field: period-end-date
          - field: start-date
          - field: end-date
          - field: entry-date   
    - dataset: development-plan-timetable
      name: development plan timetable
      fields:
          - field: reference
          - field: name
          - field: organisation
          - field: development-plan
          - field: development-plan-event
          - field: event-date
          - field: start-date
          - field: end-date
          - field: entry-date   
    - dataset: development-plan-document
      name: development plan document
      fields:
          - field: reference
          - field: name
          - field: organisation
          - field: development-plan
          - field: development-plan-document-type
          - field: documentation-url
          - field: document-url
          - field: start-date
          - field: end-date
          - field: entry-date   
---
