---
specification: local-plan-timetable
name: local plan timetable
plural: local plan timetables
description: a log of past and predicted milestones and events when producint a local plan
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2025-11-05'
github-discussion: 97
version: 0.1.0
datasets:
    - dataset: local-plan-timetable
      priority: 2
      requirement-level: SHOULD
      fields:
          - field: reference
            requirement-level: MUST
          - field: local-plan
            requirement-level: MUST
          - field: local-plan-event
            requirement-level: MUST
            dataset: local-plan-event
          - field: predicted-earliest-date
            requirement-level: SHOULD
          - field: predicted-latest-date
            requirement-level: SHOULD
          - field: entry-date
            requirement-level: SHOULD
          - field: start-date
            requirement-level: SHOULD
          - field: notes
            requirement-level: MAY
---
