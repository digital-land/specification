---
specification: development-policy
name: Development policy
plural: Development policies
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-04-05'
datasets:
    - dataset: development-policy
      name: development policy
      fields:
          - field: reference
          - field: name
          - field: development-plan-document
          - field: development-policy-categories
          - field: organisation
          - field: entry-date   
          - field: start-date
          - field: end-date
    - dataset: development-policy-area
      name: development policy area
      fields:
          - field: reference
          - field: name
          - field: development-policies
            dataset: development-policy
          - field: geometry
          - field: organisation
          - field: entry-date   
          - field: start-date
          - field: end-date
---
