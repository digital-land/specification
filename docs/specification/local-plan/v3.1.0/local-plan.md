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
version: 3.1.0
datasets:
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
          - field: period-start-date
            requirement-level: SHOULD
          - field: period-end-date
            requirement-level: SHOULD
          - field: local-planning-authorities
            requirement-level: SHOULD
          - field: local-plan-process
            requirement-level: SHOULD
          - field: documentation-url
            requirement-level: MUST
          - field: document-url
            requirement-level: MUST
            assertions:
                - reference: local-plan-A002
                  requirement-level: MUST
                  text: 'link to the core local plan document described by this data.'
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
          - field: end-date
            requirement-level: MAY
          - field: notes
            requirement-level: MAY
    - dataset: local-plan-housing
      priority: 3
      requirement-level: SHOULD
      fields:
          - field: reference
            requirement-level: MUST
          - field: local-plan
            requirement-level: MUST
          - field: local-planning-authority
            requirement-level: SHOULD
          - field: required-housing
            requirement-level: SHOULD
          - field: committed-housing
            requirement-level: SHOULD
          - field: allocated-housing
            requirement-level: SHOULD
          - field: broad-locations-housing
            requirement-level: SHOULD
          - field: windfall-housing
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
            requirement-level: MUST
          - field: document-types
            requirement-level: SHOULD
          - field: documentation-url
            requirement-level: SHOULD
          - field: document-url
            requirement-level: MUST
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
          - field: end-date
            requirement-level: MAY
          - field: notes
            requirement-level: MAY
---
