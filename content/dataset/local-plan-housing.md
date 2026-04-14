---
attribution: crown-copyright
collection: ''
consideration: local-plans
dataset: local-plan-housing
description: Housing numbers for a Local Planning Authority in a local plan
end-date: ''
entity-maximum: '1199999'
entity-minimum: '1100000'
entry-date: '2024-10-26'
fields:
- description: total number of homes planned for through local plan housing site allocations
    including mixed-use site allocations
  examples:
  - value: 9239
  field: allocated-housing
  guidance: 'Enter the total number of homes planned for through local plan housing
    site allocations

    including housing components of mixed-use site allocations

    within this `local-planning-authority` area.

    '
- description: total number of homes expected from ‘broad locations for growth’
  examples:
  - value: 15660
  field: broad-locations-housing
  guidance: 'Enter the total number of homes expected towards the end of the local
    plan period and attributed to

    ‘broad locations for growth’, as opposed to site allocations

    within this `local-planning-authority` area.

    '
- description: amount of net additional housing already committed for development
  field: committed-housing
  guidance: 'Enter the amount of housing already committed for development

    within this `local-planning-authority` area.

    '
- field: description
- description: local plan documentation page
  field: documentation-url
- description: local plan document
  field: document-url
  guidance: The URL of the [Source documentation](#source-documentation) page.
- field: end-date
  guidance: 'Enter the date these numbers were withdrawn, otherwise leave this field
    blank.

    '
- field: entity
- field: entry-date
- field: local-plan
  guidance: 'Enter the `reference` for the local plan which these numbers apply.

    '
- description: local planning authority area
  examples:
  - description: The GSS code for the County Durham LPA area
    value: E60000001
  field: local-planning-authority
  guidance: 'This should be the GSS code (statistical geography) for the `local-planning-authority`
    area to which the housing numbers apply.

    See the [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)
    dataset.

    '
- examples:
  - value: Barnsley's Local Plan as adopted by Full Council on 3 January 2019
  field: notes
  guidance: You may provide a short description to help users differentiate the plan
    from others with a similar name.
- field: organisation
- field: prefix
- description: local plan reference
  examples:
  - value: 34069/County-Durham-Plan
  - value: central-lincolnshire
  - value: barnet-local-plan-2021-2036
  field: reference
  guidance: 'Give each set of housing numbers a unique reference value.

    '
- description: minimum number of homes that a plan seeks to provide during the plan
    period
  examples:
  - entry-number: 1
    example: durham-local-plan
    value: 24852
  field: required-housing
  guidance: 'Enter the minimum number of homes that the plan seeks to provide

    within this `local-planning-authority` area.

    '
- field: start-date
  guidance: 'Enter the date these numbers were finalised.

    '
- description: total number of homes expected to arise from housing sites not specifically
    identified in the local plan
  examples:
  - value: 160
  field: windfall-housing
  guidance: 'Enter the total number of homes expected to arise from housing sites
    not specifically identified in the local plan

    within this `local-planning-authority` area.

    '
github-discussion: 26
guidance: 'Use this dataset to provide the individual `required-housing` number for
  each Local Planning Authority within a joint new local plan.

  You may also use this dataset to provide additional housing numbers related to a
  local plan.

  There is no need to provide this dataset for other kinds of plan.

  '
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
wikidata: ''
wikipedia: ''
---
