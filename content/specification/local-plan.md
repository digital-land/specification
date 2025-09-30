---
specification: local-plan
name: Local plan
plural: Local plans
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2025-09-27'
github-discussion: 26
version: 2.2.1
datasets:
    - dataset: local-plan-boundary
      name: local plan boundary
      fields:
          - field: reference
            description: a unique identifier for the boundary the plan covers. If it covers the exact planning authority boundary then use the local planning authority boundary reference
          - field: name
            description: a name for the boundary. For example, `City of York boundary`
          - field: geometry
            description: the boundary in WKT format 
          - field: description
            description: a description of the boundary. Provide more detail if boundary is different from planning authority boundary
          - field: organisations
            description: a list of codes for the responsible organisations, separated by ;
          - field: entry-date
            description: the date this information has been entered as a record
          - field: start-date
            description: the date the validity of the record starts
          - field: end-date
            description: the date the validity of the record ends
    - dataset: local-plan
      name: local plan
      fields:
          - field: reference
            description: an unique identifier for a local plan
          - field: name
            description: the name of the local plan (for example, `Leeds Local Plan`)
          - field: description
            description: brief description of plan
          - field: period-start-date
            description: the start date of the period the plan covers
          - field: period-end-date
            description: the end date of the period the plan covers
          - field: local-plan-boundary
            description: the reference code for the boundary the plan covers
          - field: documentation-url
            description: the web page where you can find the documentation for the plan
          - field: adopted-date
            description: the date a plan is officially adopted
          - field: organisations
            description: a list of CURIE references for the responsible organisations, separated by ;
          - field: required-houses
            description: the total housing requirement (net additional dwellinghouses) for the plan period
          - field: committed-houses
            description: the number of dwellinghouses already committed for development within the local plan area
          - field: allocated-houses
            description: the number of additional dwellinghouses allocated to sites by the local plan
          - field: entry-date
            description: the date this information has been entered as a record
          - field: start-date
            description: the date the validity of the record starts
          - field: end-date
            description: the date the validity of the record ends
    - dataset: local-plan-document
      name: local plan document
      fields:
          - field: reference
            description: An unique identifier for this record (for example, `document-123`)
          - field: name
            description: The name of this document
          - field: description
            description: Brief description of this document
          - field: local-plan
            description: The reference for the particular local plan (for example, `dorcester-local-plan-23`)
          - field: document-types
            description: The reference code for this document type (for example "policy-map")
            dataset: local-plan-document-type
          - field: documentation-url
            description: The webpage where you can find this document 
          - field: document-url
            description: The URL of the actual document
          - field: organisations
            description: a list of codes for the responsible organisations, separated by ;
          - field: entry-date
            description: the date this information has been entered as a record
          - field: start-date
            description: the date the validity of the record starts
          - field: end-date
            description: the date the validity of the record ends
    - dataset: local-plan-timetable
      name: local plan timetable
      fields:
          - field: reference
            description: An unique identifier for this record (for example, xyz-wquiw-309)
          - field: name
            description: a human readable name for the event
          - field: local-plan
            description: the reference code for a particular local plan (for example, "dorcester-new-local-plan")
          - field: local-plan-event
            dataset: local-plan-event
            description: The reference code for the type of local plan event (for example "plan-adopted")
          - field: event-date
            description: The date this event happened 
          - field: notes
            description: Optional notes
          - field: organisation
            description: The CURIE reference for the responsible organisation (for example, "local-authority-eng:BST")
          - field: entry-date
            description: the date this information has been entered as a record
          - field: start-date
            description: the date the validity of the record starts
          - field: end-date
            description: the date the validity of the record ends
---
