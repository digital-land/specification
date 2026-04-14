---
-dataset: ''
attribution: crown-copyright
collection: local-plan
consideration: local-plans
dataset: local-plan
description: local plans prepared by a Local Planning Authority
end-date: ''
entity-maximum: '4229999'
entity-minimum: '4220000'
entry-date: '2024-09-14'
fields:
- end-date: 2025-11-01
  field: adopted-date
  guidance: 'The `start-date` field indicates when a plan came into force, that is
    adopted.

    '
  notes: This field has been deprecated. The `start-date` field records when a plan
    was adopted.
- field: dataset
- field: description
- definition: URL of the [Source documentation](#source-documentation) page
  description: local plan documentation page
  examples:
  - value: https://eastcambs.gov.uk/planning-and-building-control/planning-policy-and-guidance/adopted-local-plan/local-plan
  - value: https://example.com/local-plans/#example-local-plan-2011
  - value: https://example.com/local-plans/#example-local-plan-2024
  field: documentation-url
  guidance: "The URL of the webpage on your website for the local plan\n\nEach entry
    in the local plan dataset should link to a documentation webpage that includes
    the information \nin the entry as well as links to where this data may be downloaded,
    and any other supporting documents.\nWhere there are several local plans listed
    on a single webpage, you can use an anchor link (fragment identifier) \nto make
    the URL for each plan unique.\n"
- description: local plan core document
  examples:
  - value: https://www.walthamforest.gov.uk/sites/default/files/2024-02/LBWF_LocalPlan_LP1_Feb2024_compressed.pdf
  field: document-url
  guidance: 'Enter the URL for the main or core plan document. This is usually a PDF
    file.

    '
- description: date a local plan was withdrawn or revoked
  field: end-date
  guidance: 'Enter the date the local plan was withdrawn or revoked, otherwise leave
    this field blank.

    '
- field: entity
- field: entry-date
- description: area covered by the local plan
  field: local-plan-boundary
  guidance: This area is created by the planning data platform from the local-planning-authorites
    values.
- description: examination process under which this local plan was or is being produced
  field: local-plan-process
  guidance: 'Indicate the local plan examination process for the local plan using
    one of the following values:


    * `2012` for plans prepared under the Town and Country Planning (Local Planning)
    (England) Regulations 2012, including transitional arrangements

    * `2026` for plans prepared under *new Local Planning Regulations (TBD)*

    '
- description: local planning authority areas covered by the local plan
  examples:
  - value: E60000001
  - value: E60000132;E60000133;E60000135;E60000136
  field: local-planning-authorities
  guidance: "Enter the reference (the GSS code) for the \n[Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)\narea
    covered by this local plan.\nFor a joint local plan, enter the list of Local Planning
    Authority references, each separated by semi-colon ';' character.\n"
- description: local plan name
  examples:
  - value: County Durham Plan
  - value: South Oxfordshire Joint Local Plan
  field: name
  guidance: Use the title of the local plan document.
- examples:
  - value: Barnsley's Local Plan as adopted by Full Council on 3 January 2019
  field: notes
  guidance: You may provide notes on how this data was made, and help users differentiate
    the plan from others with a similar name.
- field: organisation
- description: organisations responsible for this local plan
  examples:
  - value: local-authority:DUR
  - value: national-park-authority:Q72617158
  - value: local-authority:LIC;local-authority:NKE;local-authority:WLI
  field: organisations
  guidance: This value is populated by the Planning Data platform.
- description: end date of the period the plan covers
  examples:
  - value: 2038
  field: period-end-date
  guidance: Enter the end of the plan period. This is may be just the year in `YYYY`
    format.
- description: start date of the period the plan covers
  examples:
  - value: 2026
  field: period-start-date
  guidance: Enter the start of the plan period. This is usually just a year in `YYYY`
    format.
- field: prefix
- description: local plan reference
  examples:
  - value: LP-BRX-2024
  - value: 34069/County-Durham-Plan
  - value: central-lincolnshire
  - value: barnet-local-plan-2021-2036
  field: reference
  guidance: 'Give each local plan a unique reference.

    '
- description: minimum number of homes that a plan seeks to provide during the plan
    period
  examples:
  - entry-number: 1
    example: durham-local-plan
    value: 24852
  field: required-housing
  guidance: 'Enter the minimum number of homes that the plan seeks to provide

    during the plan period.

    '
- description: date when the plan was officially adopted
  field: start-date
  guidance: "Enter the date when the plan was officially adopted. \nThis value should
    match the relevant entry for when the plan was recorded as being adopted in the
    `local-plan-timetable`.\nLeave this value blank for plans which are being prepared,
    or haven't yet been adopted.\n"
github-discussion: 26
guidance: 'List the local plans you are responsible for with one row for each current,
  emerging or historical local plan.

  '
key-field: ''
licence: ogl3
name: Local plan
paint-options: ''
phase: alpha
plural: Local plans
prefix: ''
realm: dataset
start-date: ''
themes:
- development
typology: legal-instrument
wikidata: Q6664491
wikipedia: Local_plan
---
