---
specification: development-plan
name: Development plan
plural: Development plans
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-04-05'
version: 2.4.3
datasets:
    - dataset: development-plan
      name: development plan
      fields:
          - field: reference
            description: An unique identifier for a development plan
          - field: name
            description: Name of the development plan (for example, The Adopted Local Plan for Leeds)
          - field: description
            description: Brief description of plan
          - field: development-plan-type
            description: A code for the plan type
          - field: period-start-date
            description: The start date of the period the plan covers
          - field: period-end-date
            description: The end date of the period the plan covers
          - field: development-plan-geography
            description: The reference code for the geography the plan covers
          - field: documentation-url
            description: The web page where you can find the documentation for the plan
          - field: adopted-date
            description: The date a plan is officially adopted
          - field: organisations
            description: A list of codes for the responsible organisations, spearated by ;
          - field: entry-date   
          - field: start-date
          - field: end-date
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
          - field: event-date
            description: The date this event happened 
          - field: notes
            description: Optional notes
          - field: organisation
            description: The code for the responsible organisation (for example, local-authority-eng:BST)
          - field: entry-date   
          - field: start-date
          - field: end-date
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
          - field: start-date
          - field: end-date
    - dataset: development-plan-geography
      name: Development plan geography
      fields:
        - field: reference
        - field: name
        - field: geometry
        - field: development-plan-geography-type
        - field: description
        - field: entry-date
        - field: start-date
        - field: end-date
---
