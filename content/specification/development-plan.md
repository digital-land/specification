---
specification: development-plan
name: Development plan
plural: Development plans
specification-status: withdrawn
specification-reason: prospective
consideration: development-plans
start-date: ''
end-date: ''
entry-date: '2024-08-15'
notes: |
   This specification describes a collective set of plans which are now expected to be 
   separate `local-plan`, `waste-plan`, `minerals-plan`, `strategic-plan`, etc specifications.
github-discussion: 26
datasets:
    - dataset: development-plan-boundary
      name: Development plan boundary
      fields:
          - field: reference
            description: a unique identifier for the boundary the plan covers. If it covers the planning authority boundary reference should be the planning authority boundary reference
          - field: name
            description: a name for the boundary. For example, `City of York boundary`
          - field: geometry
            description: the boundary in WKT format 
          - field: description
            description: a description of the boundary. Provide more detail if boundary is different from planning authority boundary
          - field: organisation
            description: reference to the organisation responsible for the designation
          - field: entry-date
            description: the date this information has been entered as a record
          - field: start-date
            description: the date the validity of the record starts
          - field: end-date
            description: the date the validity of the record ends
    - dataset: development-plan
      name: development plan
      fields:
          - field: reference
            description: an unique identifier for a development plan
          - field: name
            description: the name of the development plan (for example, The Adopted Local Plan for Leeds)
          - field: description
            description: brief description of plan
          - field: development-plan-type
            description: a code for the plan type
            dataset: development-plan-type
          - field: period-start-date
            description: the start date of the period the plan covers
          - field: period-end-date
            description: the end date of the period the plan covers
          - field: development-plan-boundary
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
    - dataset: development-plan-timetable
      name: development plan timetable
      fields:
          - field: reference
            description: An unique identifier for this record (for example, xyz-wquiw-309)
          - field: name
          - field: development-plan
            description: The code for a particular development plan (for example, dorcester-new-local-plan)
          - field: development-plan-event
            reference: development-plan-event
            description: The code for a development plan event (for example plan-adopted)
            dataset: development-plan-event
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
    - dataset: development-plan-document
      name: development plan document
      fields:
          - field: reference
            description: An unique identifier for this record (for example, xyz-123-abc)
          - field: name
            description: The name of this document
          - field: description
            description: Brief description of this document
          - field: development-plan
            description: The code for the particular development plan (for example, dorcester-new-local-plan)
          - field: document-type
            dataset: development-plan-document-type
            description: The code for this document type (for example new-report)
          - field: documentation-url
            description: The webpage where you can find this document 
          - field: document-url
            description: The URL of the actual document
          - field: organisation
            description: The code for the responsible organisation (for example, local-authority-eng:BST)
          - field: entry-date
            description: the date this information has been entered as a record
          - field: start-date
            description: the date the validity of the record starts
          - field: end-date
            description: the date the validity of the record ends
---
