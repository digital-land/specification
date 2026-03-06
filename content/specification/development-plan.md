---
specification: development-plan
name: development plan
long-name: local plan, minerals and waste plan, and supplementary plan
long-plural: local plans, minerals and waste plans, and supplementary plans
plural: development plans
description: headline information about development plans
specification-status: working-draft
specification-reason: local-plans-2025
consideration: development-plans-and-timetables
document-url: https://digital-land.github.io/specification/specification/development-plan/
date-precision: YYYY-MM-DD
start-date: ''
end-date: ''
entry-date: '2026-01-23'
github-discussion: 26
datasets:
    - dataset: development-plan
      priority: 1
      requirement-level: MUST
      fields:
          - field: reference
            requirement-level: MUST
          - field: name
            requirement-level: MUST
            assertions:
                - reference: local-plan-A001
                  requirement-level: SHOULD
                  text: 'match the title of the document at `document-url`.'  
          - field: dataset
            requirement-level: MUST
          - field: period-start-date
            requirement-level: MUST
          - field: period-end-date
            requirement-level: MUST
          - field: local-planning-authorities
            requirement-level: CONDITIONAL
            datasets:
                - local-plan
                - supplementary-plan
          - field: mineral-planning-authorities
            requirement-level: CONDITIONAL
            datasets:
                - minerals-plan
          - field: waste-planning-authorities
            requirement-level: CONDITIONAL
            datasets:
                - waste-plan
          - field: documentation-url
            requirement-level: MUST
          - field: document-url
            requirement-level: MUST
            assertions:
                - reference: local-plan-A002
                  requirement-level: MUST
                  text: 'link to the core local plan document described by this data.'
          - field: required-housing
            requirement-level: CONDITIONAL
            datasets:
                - local-plan
          - field: document-count
            requirement-level: CONDITIONAL
            datasets:
                - minerals-plan
                - waste-plan
          - field: entry-date
            requirement-level: MUST
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
          - field: event-date
            requirement-level: MUST
          - field: actual-date
            requirement-level: CONDITIONAL
          - field: entry-date
            requirement-level: MUST
          - field: notes
            requirement-level: MAY
---
