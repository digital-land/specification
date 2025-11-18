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
  description: 'total number of homes planned for through local plan housing site allocations including mixed-use site allocations'
  guidance: |
        Enter the total number of homes planned for through local plan housing site allocations
        including housing components of mixed-use site allocations
        within this `local-planning-authority` area.
  examples:
    - value: 9239
- field: broad-locations-housing
  description: 'total number of homes expected from ‘broad locations for growth’'
  guidance: |
        Enter the total number of homes expected towards the end of the local plan period and attributed to
        ‘broad locations for growth’, as opposed to site allocations
        within this `local-planning-authority` area.
  examples:
    - value: 15660
- field: committed-housing
  description: 'amount of net additional housing already committed for development'
  guidance: |
        Enter the amount of housing already committed for development
        within this `local-planning-authority` area.
- field: description
- field: documentation-url
  description: local plan documentation page
- field: document-url
  description: local plan document
  guidance: The URL of the [Source documentation](#source-documentation) page.
- field: end-date
  guidance: |
    Enter the date these numbers were withdrawn, otherwise leave this field blank.
- field: entity
- field: entry-date
- field: local-plan
  guidance: |
    Enter the `reference` for the local plan which these numbers apply.
- field: local-planning-authority
  description: local planning authority area
  guidance: |
        This should be the GSS code (statistical geography) for the `local-planning-authority` area to which the housing numbers apply.
        See the [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority) dataset.
  examples:
      - value: 'E60000001'
        description: 'The GSS code for the County Durham LPA area'
- field: notes
  examples:
    - value: 'Information created from the LPA website.'
  guidance: 'You may provide a short description to help users differentiate the plan from others with a similar name.'
  examples:
    - value: "Barnsley's Local Plan as adopted by Full Council on 3 January 2019"
- field: organisation
- field: prefix
- field: reference
  description: local plan reference
  guidance: |
        Give each set of housing numbers a unique reference value.
  examples:
    - value: '34069/County-Durham-Plan'
    - value: 'central-lincolnshire'
    - value: 'barnet-local-plan-2021-2036'
- field: required-housing
  description: minimum number of homes that a plan seeks to provide during the plan period
  guidance: |
        Enter the minimum number of homes that the plan seeks to provide
        within this `local-planning-authority` area.
  examples:
    - example: durham-local-plan
      entry-number: 1
      value: 24852
- field: start-date
  guidance: |
    Enter the date these numbers were finalised.
- field: windfall-housing
  description: total number of homes expected to arise from housing sites not specifically identified in the local plan
  guidance: |
        Enter the total number of homes expected to arise from housing sites not specifically identified in the local plan
        within this `local-planning-authority` area.
github-discussion: 26
guidance: |
   Create a row containing the housing numbers for each local plan.
   For a joint local plan, break the numbers down further by providing a separate row for each Local Planning Authority.
key-field: ''
licence: ogl3
name: local plan housing number
paint-options: ''
phase: alpha
plural: local plan housing numbers
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- development
typology: legal-instrument
wikidata:
wikipedia:
---
