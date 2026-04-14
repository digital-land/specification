---
consideration: local-plans
datasets:
- dataset: local-plan-timetable
  fields:
  - field: reference
    requirement-level: MUST
  - field: local-plan
    requirement-level: MUST
  - dataset: local-plan-event
    field: local-plan-event
    requirement-level: MUST
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
  priority: 2
  requirement-level: SHOULD
description: log of past and predicted milestones and events when producing a local
  plan
document-url: https://digital-land.github.io/specification/specification/local-plan-timetable/
end-date: ''
entry-date: '2025-11-05'
github-discussion: 97
name: local plan timetable
plural: local plan timetables
specification: local-plan-timetable
specification-reason: prospective
specification-status: working-draft
start-date: ''
---
