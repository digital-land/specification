---
specification: local-plan
name: local plan
plural: local plans
description: headline information about one or more local plans
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2025-10-18'
github-discussion: 97
version: 3.0.1
datasets:
    - dataset: local-plan-boundary
      priority: 4
      requirement-level: MAY
      fields:
          - field: reference
            requirement-level: MUST
          - field: name
            requirement-level: SHOULD
          - field: geometry
            requirement-level: MUST
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
          - field: end-date
            requirement-level: MAY
          - field: notes
            requirement-level: MAY
    - dataset: local-plan
      priority: 1
      requirement-level: SHOULD
      fields:
          - field: reference
            requirement-level: MUST
          - field: name
            requirement-level: SHOULD
            assertions:
                - reference: local-plan-A001
                  requirement-level: SHOULD
                  text: 'match the title of the document at `document-url`.'  
          - field: organisations
            requirement-level: SHOULD
          - field: period-start-date
            requirement-level: SHOULD
          - field: period-end-date
            requirement-level: SHOULD
          - field: local-plan-boundary
          - field: documentation-url
            requirement-level: MUST
          - field: document-url
            requirement-level: MUST
            assertions:
                - reference: local-plan-A002
                  requirement-level: MUST
                  text: 'link to the core local plan document described by this data.'
          - field: adopted-date
            requirement-level: SHOULD
          - field: required-dwellings
            requirement-level: SHOULD
          - field: committed-dwellings
            requirement-level: SHOULD
          - field: allocated-dwellings
            requirement-level: SHOULD
          - field: windfall-dwellings
            requirement-level: SHOULD
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
          - field: end-date
            requirement-level: MAY
          - field: notes
            requirement-level: MAY
    - dataset: local-plan-document
      priority: 3
      requirement-level: MAY
      fields:
          - field: reference
            requirement-level: MUST
          - field: name
            requirement-level: MUST
          - field: description
            requirement-level: MAY
          - field: local-plan
          - field: document-types
            requirement-level: SHOULD
          - field: documentation-url
            requirement-level: SHOULD
          - field: document-url
            requirement-level: MUST
          - field: organisations
            requirement-level: SHOULD
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
          - field: end-date
            requirement-level: MAY
          - field: notes
            requirement-level: MAY
examples:
    - durham-local-plan
    - linconshire-local-plan
---
