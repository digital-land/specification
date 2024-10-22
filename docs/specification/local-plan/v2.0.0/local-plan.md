---
specification: local-plan
name: Local plan
plural: Local plans
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2024-09-13'
github-discussion: 26
version: 2.0.0
datasets:
    - dataset: local-plan-boundary
      name: local plan boundary
      fields:
          - field: reference
            description: a unique identifier for the boundary the plan covers. If it covers the exact planning authority boundary then use the planning authority boundary reference
          - field: name
            description: a name for the boundary. For example, `City of York boundary`
          - field: geometry
            description: the boundary in WKT format 
          - field: plan-boundary-type
            dataset: development-plan-boundary-type
            description: the type of boundary, it can be one of `planning-authority-district`, `combined-planning-authority-district` or `designated‑plan‑area`
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
            description: the name of the local plan (for example, The Adopted Local Plan for Leeds)
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
            description: a list of codes for the responsible organisations, separated by ;
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
            description: An unique identifier for this record (for example, xyz-123-abc)
          - field: name
            description: The name of this document
          - field: description
            description: Brief description of this document
          - field: local-plan
            description: The reference for the particular local plan (for example, dorcester-new-local-plan)
          - field: document-types
            description: The code for this document type (for example policy map)
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
            description: the code for a particular local plan (for example, dorcester-new-local-plan)
          - field: local-plan-event
            dataset: local-plan-event
            description: The code for a local plan event (for example plan-adopted)
          - field: event-date
            description: The date this event happened 
          - field: notes
            description: Optional notes
          - field: organisation
            description: The code for the responsible organisation (for example, local-authority-eng:BST)
          - field: entry-date
            description: the date this information has been entered as a record
          - field: start-date
            description: the date the validity of the record starts
          - field: end-date
            description: the date the validity of the record ends
---
