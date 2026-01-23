---
attribution: crown-copyright
collection: ''
consideration: development-plans-and-timetables
dataset: development-plan
description: ''
end-date: ''
entry-date: ''
fields:
- field: adopted-date
  notes: This field has been deprecated. The `start-date` field records when a plan was adopted.
  end-date: 2025-11-01
  guidance: |
      The `start-date` field indicates when a plan came into force, that is adopted.
- field: dataset
  guidance: |
    Enter one of the following values to indicate the type of development plan:

    * `local-plan`
    * `supplementary-plan`
    * `minerals-plan`
    * `waste-plan`
- field: documentation-url
  description: local plan documentation page
  definition: URL of the [Source documentation](#source-documentation) page
  guidance: |
     The URL of the webpage on your website for the local plan

     Each entry in the local plan dataset should link to a documentation webpage that includes the information 
     in the entry as well as links to where this data may be downloaded, and any other supporting documents.
     Where there are several local plans listed on a single webpage, you can use an anchor link (fragment identifier) 
     to make the URL for each plan unique.
  examples:
    - value: https://eastcambs.gov.uk/planning-and-building-control/planning-policy-and-guidance/adopted-local-plan/local-plan
    - value: https://example.com/local-plans/#example-local-plan-2011
    - value: https://example.com/local-plans/#example-local-plan-2024
- field: document-url
  description: local plan core document
  guidance: |
      Enter the URL for the main or core plan document. This is usually a PDF file.
  examples:
    - value: 'https://www.walthamforest.gov.uk/sites/default/files/2024-02/LBWF_LocalPlan_LP1_Feb2024_compressed.pdf'
- field: end-date
  description: date a local plan was withdrawn or revoked
  guidance: |
      Enter the date the local plan was withdrawn or revoked, otherwise leave this field blank.
- field: entity
- field: entry-date
- field: local-plan-boundary
  description: area covered by the local plan
  guidance: This area is created by the planning data platform from the local-planning-authorites values.
- field: local-plan-process
  description: 'examination process under which this local plan was or is being produced'
  guidance: |
      Indicate the local plan examination process for the local plan using one of the following values:

      * `2012` for plans prepared under the Town and Country Planning (Local Planning) (England) Regulations 2012, including transitional arrangements
      * `2026` for plans prepared under *new Local Planning Regulations (TBD)*
- field: local-planning-authorities
  description: local planning authority areas covered by the local plan
  guidance: |
    Enter the reference (the GSS code) for the 
    [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)
    area covered by this local or supplementary plan.
    For a joint local plan, enter the list of Local Planning Authority references, each separated by semi-colon ';' character.
  examples:
    - value: 'E60000001'
    - value: 'E60000132;E60000133;E60000135;E60000136'
- field: name
  description: local plan name
  guidance: Use the title of the adopted local plan document.
  examples:
    - value: 'County Durham Plan'
    - value: 'South Oxfordshire Joint Local Plan'
- field: notes
  examples:
    - value: 'Information created from the LPA website.'
  guidance: 'You may provide notes on how this data was made, and help users differentiate the plan from others with a similar name.'
  examples:
    - value: "Barnsley's Local Plan as adopted by Full Council on 3 January 2019"
- field: organisation
- field: organisations
  description: organisations responsible for this local plan
  guidance: This value is populated by the Planning Data platform.
  examples:
    - value: 'local-authority:DUR'
    - value: 'national-park-authority:Q72617158'
    - value: 'local-authority:LIC;local-authority:NKE;local-authority:WLI'
- field: period-end-date
  description: end date of the period the plan covers
  guidance: 'Enter the end of the plan period. This is usually just a year in `YYYY` format.'
  examples:
    - value: 2038
- field: period-start-date
  description: start date of the period the plan covers
  guidance: 'Enter the start of the plan period. This is usually just a year in `YYYY` format.'
  examples:
    - value: 2026
- field: prefix
- field: reference
  description: local plan reference
  guidance: |
     Give each local plan a unique reference.
  examples:
    - value: 'LP-BRX-2024'
    - value: '34069/County-Durham-Plan'
    - value: 'central-lincolnshire'
    - value: 'barnet-local-plan-2021-2036'
- field: required-housing
  description: minimum number of homes that a plan seeks to provide during the plan period
  guidance: |
        Enter the minimum number of homes that the plan seeks to provide
        during the plan period.
        This field is mandatory for new local plans.
        When producing a joint local plan you should also provide an entry for each `local-planning-authority` area
        in a separate `local-plan-housing` dataset.
  examples:
    - example: durham-local-plan
      entry-number: 1
      value: 24852
- field: start-date
  description: date when the plan was officially adopted
  guidance: |
      Enter the date when the plan was officially adopted. 
      This value should match the relevant entry for when the plan was recorded as being adopted in the `local-plan-timetable`.
      Leave this value blank for plans which are being prepared, or haven't yet been adopted.
github-discussion: 26
key-field: ''
licence: ogl3
name: development plan
paint-options: ''
phase: alpha
plural: development plans
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
