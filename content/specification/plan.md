---
consideration: development-plans-and-timetables
datasets:
- dataset: plan
  fields:
  - field: reference
    requirement-level: MUST
  - assertions:
    - reference: plan-A001
      requirement-level: SHOULD
      text: match the title of the document at `document-url`.
    field: name
    requirement-level: MUST
  - field: description
    requirement-level: MUST
  - field: datasets
    requirement-level: MUST
  - field: period-start-date
    requirement-level: MUST
  - field: period-end-date
    requirement-level: MUST
  - datasets:
    - local-plan
    - supplementary-plan
    field: local-planning-authorities
    requirement-level: CONDITIONAL
  - datasets:
    - waste-plan
    - minerals-plan
    field: minerals-and-waste-planning-authorities
    requirement-level: CONDITIONAL
  - field: documentation-url
    requirement-level: MUST
  - assertions:
    - reference: plan-A002
      requirement-level: MUST
      text: link to the core plan document described by this data.
    field: document-url
    requirement-level: MUST
  - datasets:
    - local-plan
    field: required-housing
    requirement-level: CONDITIONAL
  - datasets:
    - minerals-plan
    - waste-plan
    field: document-count
    requirement-level: CONDITIONAL
  - field: entry-date
    requirement-level: MUST
  - field: notes
    requirement-level: MAY
  priority: 1
  requirement-level: MUST
- dataset: plan-timetable
  fields:
  - field: reference
    requirement-level: MUST
  - field: plan
    requirement-level: MUST
  - dataset: plan-event
    field: plan-event
    requirement-level: MUST
  - field: event-date
    requirement-level: MUST
  - field: actual-date
    requirement-level: CONDITIONAL
  - field: entry-date
    requirement-level: MUST
  - field: notes
    requirement-level: MAY
  priority: 2
  requirement-level: MUST
date-precision: YYYY-MM-DD
description: headline information about local plans, minerals and waste plans, and
  supplementary plans
document-url: https://digital-land.github.io/specification/specification/plan/
end-date: ''
entry-date: '2026-03-24'
github-discussion: 26
long-name: local plan, minerals and waste plan, and supplementary plan
long-plural: local plans, minerals and waste plans, and supplementary plans
name: plan
plural: plans
specification: plan
specification-reason: local-plans-2025
specification-status: working-draft
start-date: ''
---
