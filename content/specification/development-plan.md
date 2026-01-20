---
specification: development-plan
name: development plan
plural: development plans
description: headline information about development plans
specification-status: working-draft
specification-reason: local-plans-2025
consideration: development-plans-and-timetables
document-url: https://digital-land.github.io/specification/specification/development-plan/
start-date: ''
end-date: ''
entry-date: '2026-01-19'
github-discussion: 26
datasets:
    - dataset: development-plan
      priority: 1
      requirement-level: MUST
      fields:
          - field: reference
            requirement-level: MUST
          - field: name
            requirement-level: SHOULD
            assertions:
                - reference: local-plan-A001
                  requirement-level: SHOULD
                  text: 'match the title of the document at `document-url`.'  
          - field: dataset
            requirement-level: MUST
          - field: period-start-date
            requirement-level: SHOULD
          - field: period-end-date
            requirement-level: SHOULD
          - field: local-planning-authorities
            requirement-level: SHOULD
            datasets:
                - local-plan
                - supplementary-plan
          - field: mineral-planning-authorities
            requirement-level: SHOULD
            datasets:
                - minerals-plan
          - field: waste-planning-authorities
            requirement-level: SHOULD
            datasets:
                - waste-plan
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
          - field: required-housing
            requirement-level: MUST
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
          - field: end-date
            requirement-level: MAY
          - field: notes
            requirement-level: MAY
    - dataset: development-plan-timetable
      priority: 2
      requirement-level: MUST
      fields:
          - field: reference
            requirement-level: MUST
          - field: development-plan
            requirement-level: MUST
          - field: development-plan-event
            requirement-level: MUST
            dataset: local-plan-event
          - field: predicted-date
            requirement-level: MUST
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
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
          - field: required-housing
            requirement-level: MUST
          - field: committed-housing
            requirement-level: MAY
          - field: allocated-housing
            requirement-level: MAY
          - field: broad-locations-housing
            requirement-level: MAY
          - field: windfall-housing
            requirement-level: MAY
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
          - field: end-date
            requirement-level: MAY
          - field: notes
            requirement-level: MAY
---
