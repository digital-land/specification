---
consideration: ''
datasets:
- dataset: development-policy
  fields:
  - field: reference
  - field: name
  - field: development-plan-document
  - field: development-policy-categories
  - field: organisation
  - field: entry-date
  - field: start-date
  - field: end-date
  name: development policy
- dataset: development-policy-area
  fields:
  - field: reference
  - field: name
  - dataset: development-policy
    field: development-policies
  - field: geometry
  - field: organisation
  - field: entry-date
  - field: start-date
  - field: end-date
  name: development policy area
end-date: ''
entry-date: '2023-04-05'
github-discussion: ''
name: Development policy
plural: Development policies
specification: development-policy
specification-reason: prospective
specification-status: working-draft
start-date: ''
---
