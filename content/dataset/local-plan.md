---
attribution: crown-copyright
collection: 'local-plan'
consideration: local-plans
dataset: local-plan
description: 'local plans prepared by a Local Planning Authority'
end-date: ''
entity-maximum: '4229999'
entity-minimum: '4220000'
entry-date: '2024-09-14'
fields:
- field: adopted-date
  notes: This field has been deprecated. The `start-date` field records when a plan was adopted.
  end-date: 2025-11-01
  guidance: |
      The `start-date` field indicates when a plan came into force, that is adopted.
- field: documentation-url
  description: local plan documentation page
  definition: URL of the [Source documentation](#source-documentation) page
  guidance: |
     The URL of the webpage on your website for the local plan

     Each entry in the local plan dataset should link to a documentation webpage that includes the information 
     in the entry as well as links to where this data may be downloaded, and any other supporting documents.
     Each local plan should have a unique URL.
     Where there are several local plans listed on a single webpage, you will need to use use an anchor link (fragment identifier) for each plan.
  examples:
    - value: https://calderdale.gov.uk/planning-and-building-control/planning-policy/local-plan
    - value: https://example.com/local-plans/#example-local-plan-2011
    - value: https://example.com/local-plans/#example-local-plan-2024
- field: document-url
  description: local plan core document
  guidance: |
      Enter the URL for the main or core plan document. This is usually a PDF file.
  examples:
    - value: 'https://www.walthamforest.gov.uk/sites/default/files/2024-02/LBWF_LocalPlan_LP1_Feb2024_compressed.pdf'
- field: end-date
  description: date a local plan was withdran or revoked
- field: entity
- field: entry-date
- field: local-plan-boundary
  description: area covered by the local plan
  guidance: This area is created by the planning data platform from the local-planning-authorites values.
- field: local-plan-process
  description: 'examination process under which this local plan was or is being produced'
  guidance: 'Enter the local plan examination process under which this local plan was or is being produced.'
  examples:
    - value: "2025"
      description: "the plan is being produced under the 2025 local plan regulations"
    - value: "2012"
      description: "the plan was produced under the previous local plan regulations"
- field: local-planning-authorities
  description: local planning authority areas covered by the local plan
  guidance: |
    Enter the reference (the GSS code) for the 
    [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)
    area covered by the plan.
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
- field: organisations
  description: organisations responsible for this local plan
  guidance: This value is populated by the Planning Data platform.
  examples:
    - value: 'local-authority:DUR'
    - value: 'national-park-authority:Q72617158'
    - value: 'local-authority:LIC;local-authority:NKE;local-authority:WLI'
- field: period-end-date
  description: end date of the period the plan covers
  guidance: 'Enter the end of the plan period. This is may be just the year in `YYYY` format.'
  examples:
    - value: 2041
    - value: 2035-06-30
- field: period-start-date
  description: start date of the period the plan covers
  guidance: 'Enter the start of the plan period. This is usually just a year in `YYYY` format.'
  examples:
    - value: 2018
    - value: 2025-04
    - value: 2025-04-19
- field: prefix
- field: reference
  description: local plan reference
  guidance: |
    A reference or ID for each local plan that is:

    * unique within your dataset
    * persistent - it doesn’t change when the dataset is updated

    If you don’t have a reference for the local plan already, you will need to create one. This can be a short set of letters or numbers.
  examples:
    - value: 'LP-BRX-2024'
    - value: '34069/County-Durham-Plan'
    - value: 'central-lincolnshire'
    - value: 'barnet-local-plan-2021-2036'
- field: start-date
  description: date when the plan was officially adopted
  guidance: |
      Enter the date when the plan was officially adopted. 
      This value should match the relevant entry for when the plan was recoreded as being adopted in the `local-plan-timetable`.
      Leave this value blank for plans which are being prepared, or haven't yet been adopted.
github-discussion: 26
key-field: ''
licence: ogl3
name: local plan
paint-options: ''
phase: alpha
plural: local plans
prefix: ''
realm: dataset
-dataset: ''
start-date: ''
themes:
- development
typology: legal-instrument
version: 1.0
wikidata: Q6664491
wikipedia: Local_plan
---
