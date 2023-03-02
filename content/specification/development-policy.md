---
specification: development-policy
name: Development policy
plural: Development policies
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-03-01'
datasets:
    - dataset: development-plan
      name: development plan
      fields:
          - field: reference
          - field: name
          - field: organisations
          - field: development-plan-type
          - field: development-plan-status
          - field: documentation-url
          - field: document-url
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
          - field: development-plan-status
          - field: documentation-url
          - field: document-url
          - field: start-date
          - field: end-date
          - field: entry-date   
    - dataset: development-policy
      name: development policy
      fields:
          - field: reference
          - field: name
          - field: organisation
          - field: development-plan
          - field: development-policy-categories
          - field: start-date
          - field: end-date
          - field: entry-date   
    - dataset: development-policy-area
      name: development policy area
      fields:
          - field: reference
          - field: name
          - field: organisation
          - field: geometry
          - field: development-policies
          - field: start-date
          - field: end-date
          - field: entry-date   
---
