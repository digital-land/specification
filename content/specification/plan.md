---
specification: plan
name: plan
long-name: local plan, minerals and waste plan, and supplementary plan
long-plural: local plans, minerals and waste plans, and supplementary plans
plural: plans
description: headline information about local plans, minerals and waste plans, and supplementary plans
specification-status: working-draft
specification-reason: local-plans-2025
consideration: development-plans-and-timetables
document-url: https://digital-land.github.io/specification/specification/plan/
date-precision: YYYY-MM-DD
start-date: ''
end-date: ''
entry-date: '2026-03-24'
github-discussion: 26
datasets:
    - dataset: plan
      priority: 1
      requirement-level: MUST
      fields:
          - field: reference
            requirement-level: MUST
          - field: name
            requirement-level: MUST
            assertions:
                - reference: plan-A001
                  requirement-level: SHOULD
                  text: 'match the title of the document at `document-url`.'  
          - field: description
            requirement-level: MUST
          - field: datasets
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
          - field: minerals-and-waste-planning-authorities
            requirement-level: CONDITIONAL
            datasets:
                - waste-plan
                - minerals-plan
          - field: documentation-url
            requirement-level: MUST
          - field: document-url
            requirement-level: MUST
            assertions:
                - reference: plan-A002
                  requirement-level: MUST
                  text: 'link to the core plan document described by this data.'
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
    - dataset: plan-timetable
      priority: 2
      requirement-level: MUST
      fields:
          - field: reference
            requirement-level: MUST
          - field: plan
            requirement-level: MUST
          - field: plan-event
            requirement-level: MUST
            dataset: plan-event
          - field: event-date
            requirement-level: MUST
          - field: actual-date
            requirement-level: CONDITIONAL
          - field: entry-date
            requirement-level: MUST
          - field: notes
            requirement-level: MAY
---
