---
attribution: crown-copyright
collection: ''
consideration: development-plans-and-timetables
dataset: plan
description: ''
end-date: ''
entry-date: '2026-03-24'
fields:
- examples:
  - value: local-plan
  - value: waste-plan
  - value: minerals-plan;waste-plan
  - value: local-plan;minerals-plan
  - value: local-plan;minerals-plan;waste-plan
  field: datasets
  guidance: 'Enter one of the following values to show the type of plan or plan document:


    * `local-plan`

    * `supplementary-plan`

    * `minerals-plan`

    * `waste-plan`


    If your plan includes multiple types, enter the list of types and separate each
    of them with a semi-colon.

    '
- field: description
  guidance: 'Enter a description of the matters which the plan deals with.

    '
- field: document-count
  guidance: 'Enter the number of documents which collectively form the plan. This
    field is only required for a minerals and waste plan.

    '
- definition: URL of the [Source documentation](#source-documentation) page
  description: local plan documentation page
  examples:
  - value: https://eastcambs.gov.uk/planning-and-building-control/planning-policy-and-guidance/adopted-local-plan/local-plan
  - value: https://example.com/local-plans/#example-local-plan-2011
  - value: https://example.com/local-plans/#example-local-plan-2024
  field: documentation-url
  guidance: "Enter the URL of the webpage which links to your main or core plan document.\n\nIf
    there are several plans listed on a single webpage, you can use an anchor link
    (fragment identifier) \nto make the `documentation-url` value for each plan unique.\n"
- description: local plan core document
  examples:
  - value: https://www.walthamforest.gov.uk/sites/default/files/2024-02/LBWF_LocalPlan_LP1_Feb2024_compressed.pdf
  field: document-url
  guidance: 'Enter the URL for the main or core plan document, which is usually a
    PDF file.


    If you do not have a main or core plan document on the day you publish your data,
    leave this field blank.

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
  guidance: 'Enter the GSS code for the 

    [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)

    area that this local or supplementary plan covers.

    For a joint local plan, enter the list of references and separate each of them
    by with a semi-colon.

    '
- description: local plan name
  examples:
  - value: York Local Plan
  - value: Plymouth and South West Devon Joint Local Plan
  field: name
  guidance: Use the title of the local plan document.
- examples:
  - value: Barnsley's Local Plan as adopted by Full Council on 3 January 2019
  field: notes
  guidance: 'You may provide notes on how you made this data to help users differentiate
    the plan from others with a similar name.

    '
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
  - value: 2040
  field: period-end-date
  guidance: Enter the end of the plan period. This is usually just a year in `YYYY`
    format.
- description: start date of the period the plan covers
  examples:
  - value: 2026
  - value: 2027
  field: period-start-date
  guidance: Enter the start of the plan period. This is usually just a year in `YYYY`
    format.
- field: prefix
- description: local plan reference
  examples:
  - value: barnet-local-plan-2021-2036
  - value: hertfordshire-minerals-and-waste-plan
  - value: essex-minerals-plan
  - value: essex-waste-plan
  field: reference
  guidance: 'Give each local plan a unique reference.

    '
- description: minimum number of homes that a plan seeks to provide during the plan
    period
  examples:
  - value: 10852
  - value: 10012
  field: required-housing
  guidance: "Enter the minimum number of homes that the plan seeks to provide during
    the plan period.  \n\nYou must provide your required-housing when you launch your
    consultation on\nyour proposed local plan. You must update your required-housing
    when you:\n\n* submit your plan for examination\n* publish the examiner’s recommendations
    and reasons\n* publish your adopted local plan\n"
- description: date when the plan was officially adopted
  field: start-date
  guidance: "Enter the date when the plan was officially adopted. \nThis value should
    match the relevant entry for when the plan was recorded as being adopted in the
    `local-plan-timetable`.\nLeave this value blank for plans which are being prepared,
    or haven't yet been adopted.\n"
github-discussion: 26
key-field: ''
licence: ogl3
name: plan
paint-options: ''
phase: alpha
plural: plans
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- development
typology: legal-instrument
wikidata: Q5266783
wikipedia: Development_plan
---

This dataset is a package made from the local-plan, waste-plan, minerals-plan and supplementary-plan datasets.
