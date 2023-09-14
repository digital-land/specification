---
specification: nationally-significant-infrastructure-project
name: Nationally significant infrastructure project
plural: Nationally significant infrastructure projects
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-09-14'
version: 1.1.0
datasets:
    - dataset: nationally-significant-infrastructure-project
      name: Nationally significant infrastructure project
      fields:
          - field: reference
          - field: name
          - field: description
          - field: applicant-organisation
          - field: nationally-significant-infrastructure-project-decision
            dataset: nationally-significant-infrastructure-project-decision
          - field: decision-date
          - field: decision-maker
          - field: geometry
          - field: point
          - field: documentation-url
          - field: nationally-significant-infrastructure-project-type
            dataset: nationally-significant-infrastructure-project-type
          - field: notes
          - field: organisation
          - field: entry-date   
          - field: start-date
          - field: end-date
    - dataset: nationally-significant-infrastructure-project-log
      name: Nationally significant infrastructure project log
      fields:
          - field: reference
          - field: nationally-significant-infrastructure-project
          - field: nationally-significant-infrastructure-project-event
            dataset: nationally-significant-infrastructure-project-event
          - field: event-date
          - field: name
          - field: notes
            description: Optional notes text
          - field: organisation
          - field: entry-date   
          - field: start-date
          - field: end-date
    - dataset: nationally-significant-infrastructure-project-document
      name: Nationally significant infrastructure project document
      fields:
          - field: reference
          - field: nationally-significant-infrastructure-project
          - field: document-type
            dataset: nationally-significant-infrastructure-project-document-type
          - field: name
          - field: notes
            description: Optional notes text
          - field: organisation
          - field: document-url
          - field: documentation-url
          - field: entry-date   
          - field: start-date
          - field: end-date
---
