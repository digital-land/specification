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
    Enter one of the following values to show the type of development plan:

    * `local-plan`
    * `supplementary-plan`
    * `minerals-plan`
    * `waste-plan`
- field: document-count
  guidance: |
      Enter the number of documents which collectively form the plan. This field is only required for a minerals and waste plan.
- field: documentation-url
  description: local plan documentation page
  definition: URL of the [Source documentation](#source-documentation) page
  guidance: |
     Enter the URL of the webpage which links to your main or core plan document.

     If there are several plans listed on a single webpage, you can use an anchor link (fragment identifier) 
     to make the `documentation-url` value for each plan unique.
  examples:
    - value: https://eastcambs.gov.uk/planning-and-building-control/planning-policy-and-guidance/adopted-local-plan/local-plan
    - value: https://example.com/local-plans/#example-local-plan-2011
    - value: https://example.com/local-plans/#example-local-plan-2024
- field: document-url
  description: local plan core document
  guidance: |
      Enter the URL for the main or core plan document, which is usually a PDF file.

      If you do not have a main or core plan document on the day you publish your data, leave this field blank.
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
    Enter the GSS code for the 
    [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)
    area that this local or supplementary plan covers.
    For a joint local plan, enter the list of references and separate each of them by with a semi-colon.
  examples:
    - value: 'E60000001'
    - value: 'E60000132;E60000133;E60000135;E60000136'
- field: name
  description: local plan name
  guidance: Use the title of the local plan document.
  examples:
    - value: 'County Durham Plan'
    - value: 'South Oxfordshire Joint Local Plan'
- field: notes
  examples:
    - value: 'Information created from the LPA website.'
  guidance: |
      You may provide notes on how you made this data to help users differentiate the plan from others with a similar name.
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
    - value: 2040
- field: period-start-date
  description: start date of the period the plan covers
  guidance: 'Enter the start of the plan period. This is usually just a year in `YYYY` format.'
  examples:
    - value: 2026
    - value: 2027
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
        Enter the minimum number of homes that the plan seeks to provide during the plan period.  

        You must provide your required-housing when you launch your consultation on
        your proposed local plan. You must update your required-housing when you:

        * submit your plan for examination
        * publish the examiner’s recommendations and reasons
        * publish your adopted local plan
  examples:
    - value: 1024
    - value: 24852
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
