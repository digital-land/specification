---
attribution: crown-copyright
collection:
consideration: local-plans
dataset: local-plan-housing
description: 'Housing numbers for a Local Planning Authority in a local plan'
end-date: ''
entity-maximum: '1199999'
entity-minimum: '1100000'
entry-date: '2024-10-26'
fields:
- field: allocated-housing
  description: amount of additional housing allocated to sites within the local-planning-authority area in the local-plan
  guidance: |
        Enter the amount of net additional housing which have been allocated to sites with the local planning authority area in the local plan.
  examples:
    - example: durham-local-plan
      entry-number: 1
      value: 15660
- field: broad-locations-housing
  description: 'amount of net additional housing expected to be delivered from broad locations for development within the local-planning-authority-area in the local plan'
  guidance: |
        Enter the amount of net additional housing which have been allocated to sites in the local plan.
  examples:
    - example: durham-local-plan
      entry-number: 1
      value: 15660
- field: committed-housing
  description: the amount of housing already committed for development within the local-plannning-authority area in the local-plan
  guidance: Enter the amount of housing already committed for development within the local plan area at the time the local plan was adopted.
- field: description
- field: documentation-url
  description: local plan documentation page
- field: document-url
  description: local plan document
  guidance: The URL of the [Source documentation](#source-documentation) page.
- field: end-date
- field: entity
- field: entry-date
- field: local-plan
- field: local-planning-authority
  description: local planning authority area
  guidance: |
        This should be the statistical geography for the local-planning-authority area to which the housing numbers apply.
        See the [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority) dataset.
  examples:
      - example: durham-local-plan
        entry-number: 1
        value: 'E60000001'
        description: 'The GSS code for the County Durham LPA area'
- field: notes
  examples:
  - value: 'Information created from the LPA website.'
  guidance: 'You may provide a short description to help users differentiate the plan from others with a similar name.'
  examples:
      - value: "Barnsley's Local Plan as adopted by Full Council on 3 January 2019"
- field: organisation
  description: organisations responsible for this local plan
  examples:
      - value: 'local-authority:DUR'
      - value: 'national-park-authority:Q72617158'
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
- field: required-housing
  description: the total housing requirement (net additional housing) for the local-plan period
  guidance: Enter the amount of housing required in the local planning authority area for the local plan period.
  examples:
    - example: durham-local-plan
      entry-number: 1
      value: 24852
- field: start-date
- field: windfall-housing
  description: the amount of additional housing expected to be delivered from windfall developments during the local plan period
github-discussion: 26
key-field: ''
licence: ogl3
name: Local plan housing number
paint-options: ''
phase: alpha
plural: Local plan housing numbers
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
