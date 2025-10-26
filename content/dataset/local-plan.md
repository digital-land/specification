---
attribution: crown-copyright
collection: 'local-plan'
consideration: local-plans
dataset: local-plan
description: 'Local plans prepared by a Local Planning Authority'
end-date: ''
entity-maximum: '4229999'
entity-minimum: '4220000'
entry-date: '2024-09-14'
fields:
- field: adopted-date
- field: documentation-url
  description: local plan documentation page
- field: document-url
  description: local plan document
  guidance: The URL of the [Source documentation](#source-documentation) page.
- field: end-date
- field: entity
- field: entry-date
- field: local-plan-boundary
- field: local-planning-authorities
  description: area covered by the local plan
  guidance: |
        Enter the reference (the GSS code) for [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)
        area covered by the plan.
        For a joint local plan, enter the list of Local Planning Authority references, each separated by semi-colon ';' character.
  examples:
      - example: durham-local-plan
        entry-number: 1
        value: 'E60000001'
        description: 'The GSS code for the County Durham LPA area'
- field: name
  description: local plan name
  guidance: Use the title of the adopted local plan document.
  examples:
    - example: durham-local-plan
      entry-number: 1
      value: 'County Durham Plan'
    - example: central-linconshire-local-plan
      entry-number: 1
    - value: 'Central Linconshire Local Plan'
- field: notes
  examples:
  - value: 'Information created from the LPA website.'
  guidance: 'You may provide a short description to help users differentiate the plan from others with a similar name.'
  examples:
      - value: "Barnsley's Local Plan as adopted by Full Council on 3 January 2019"
- field: organisations
  description: organisations responsible for this local plan
  examples:
      - value: 'local-authority:DUR'
      - value: 'national-park-authority:Q72617158'
      - value: 'local-authority:LIC;local-authority:NKE;local-authority:WLI'
- field: period-end-date
  description: the end date of the period the plan covers
  guidance: 'Enter the end of the plan period. This is may be just the year in `YYYY` format.'
  examples:
    - value: 2041
- field: period-start-date
  description: the start date of the period the plan covers
  guidance: 'Enter the start of the plan period. This is usually just a year in `YYYY` format.'
  examples:
    - value: 2018
- field: prefix
- field: reference
  description: local plan reference
  guidance: |
    Give each local plan a reference value.
  examples:
    - example: 
      value: '34069/County-Durham-Plan'
    - value: 'central-lincolnshire'
    - value: 'barnet-local-plan-2021-2036'
- field: start-date
  description: when the plan was officially adopted
  guidance: |
      Enter the date when the plan was officially adopted. 
      This value should match the relevant entry for when the plan was recoreded as being adopted in the `local-plan-timetable`.
      Leave this value blank for plans which are being prepared, or haven't yet been adopted.
github-discussion: 26
key-field: ''
licence: ogl3
name: Local plan
paint-options: ''
phase: alpha
plural: Local plans
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- development
typology: legal-instrument
version: 1.0
wikidata: 
wikipedia: 
---
