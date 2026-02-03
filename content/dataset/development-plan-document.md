---
attribution: crown-copyright
collection: 'local-plan'
consideration: development-plans-and-timetables
dataset: development-plan-document
description: 'documents associated with a development plan'
end-date: ''
entity-maximum: '3899999'
entity-minimum: '3800000'
entry-date: '2026-01-19'
fields:
- field: description
- field: development-plan
  description: "associated development plan"
  guidance: |
    Enter the reference for the development plan which the document is associated with.
  examples:
    - value: 'LP-BRX-2024'
    - value: 'central-lincolnshire'
    - value: 'local-plan:central-lincolnshire'
- field: document-types
  datasets:
    - dataset: development-plan-document-type
  guidance: |
    Enter at least one of the following [development-plan-document-type](https://www.planning.data.gov.uk/dataset/development-plan-document-type) values:

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

    You can list more than one category, separated by a semi-colon ';' character.
  examples:
    - value: local-plan
    - value: local-plan;core-strategy;site-allocations
- field: document-url
  guidance: |
     Enter the URL for the document. This is often a PDF file.
- field: documentation-url
  description: development plan document documentation page
  guidance: |
     Enter the URL of the webpage on your website which documents and links to this document.
  examples:
    - value: https://calderdale.gov.uk/planning-and-building-control/planning-policy/local-plan
- field: end-date
  guidance: |
     Enter date when the document was archived. Otherwise leave this field blank.
- field: entity
- field: entry-date
- field: name
  guidance: |
     Enter the title of the document.
- field: notes
- field: organisation
- field: prefix
- field: reference
  guidance: |
     Give each document a unique reference.
- field: start-date
  guidance: |
     Enter the date the document was published.
github-discussion: 26
guidance: |
    Provide a list of documents associated with your development plan.
    Add a separate row with a link to each document on your website.
key-field: ''
licence: ogl3
name: Development plan document
paint-options: ''
phase: alpha
plural: Development plan documents
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- development
typology: document
wikidata: ''
wikipedia: ''
---
