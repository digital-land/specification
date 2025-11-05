---
attribution: crown-copyright
collection: 'local-plan'
consideration: development-plans-and-timetables
dataset: local-plan-document
description: ''
end-date: ''
entity-maximum: '3899999'
entity-minimum: '3800000'
entry-date: '2024-09-14'
fields:
- field: description
- field: local-plan
- field: document-types
  datasets:
    - dataset: local-plan-document-type
  guidance: |
    Enter at least one of the following [local-plan-document-type](https://www.planning.data.gov.uk/dataset/local-plan-document-type) values:

    * `adoption-statement`
    * `area-action-plan`
    * `core-strategy`
    * `financial-viability-study`
    * `inspectors-report`
    * `local-development-scheme`
    * `local-plan`
    * `local-plan-review`
    * `policies-map`
    * `strategic-flood-risk-assessment`
    * `strategic-housing-market-assessment`
    * `supplementary-planning-document`
    * `sustainability-apprasial`
    * `site-allocations`
    * `viability-assessment`
    * `sustainability-appraisal`

    Where a single document covers multipleou can list more than one category, separated by a semi-colon ';' character.
  examples:
    - value: local-plan
    - value: local-plan;core-strategy;site-allocations
- field: document-url
- field: documentation-url
  description: local plan document documentation page
  guidance: |
     Enter the URL of the webpage on your website which references this document.
  examples:
    - value: https://calderdale.gov.uk/planning-and-building-control/planning-policy/local-plan
- field: end-date
- field: entity
- field: entry-date
- field: name
- field: notes
- field: organisation
- field: prefix
- field: reference
- field: start-date
github-discussion: 26
key-field: ''
licence: ogl3
name: Local plan document
paint-options: ''
phase: alpha
plural: Local plan documents
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- development
typology: document
version: 1.0
wikidata: ''
wikipedia: ''
---
