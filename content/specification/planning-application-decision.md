---
consideration: planning-applications-decisions
datasets:
- dataset: planning-application
  fields:
  - description: The planning application reference (for example, "27/AP/9032")
    field: reference
  - description: Name of the planning application (for example, "Residential alteration
      to Downton House")
    field: name
  - description: Brief description of the application (for example, "Alterations to
      two windows on the southern elevation of the 3rd floor flat")
    field: description
  - description: The address of the site as a single line of text (for example, "11
      High Street, Ambridge, BO22 3LL")
    field: address-text
  - description: The UPRN for the primary address of the site
    field: uprn
  - description: the boundary of the site as a POLYGON or MULTIPOLYGON, with points
      in the EPSG 4326 coordinate reference system, and WGS85 datum, encoded in Well-Known
      Text (WKT) representation of geometry
    field: geometry
  - field: point
  - description: The URL of this planning application in the planning register.
    field: documentation-url
  - dataset: planning-application-type
    description: The reference code for the type of planning application (for example
      "full-planning-permission")
    field: planning-application-type
  - dataset: planning-decision
    description: The reference code for the planning decision made (for example "pending"
      or "permission-in-principle")
    field: planning-decision
  - dataset: planning-decision-type
    description: The reference code for the way the decision was made (for example
      "committee")
    field: planning-decision-type
  - description: Optional notes text
    field: notes
  - description: The reference code for the organisation responsible for processing
      the planning application
    field: organisation
  - description: The date this data was created or last updated
    field: entry-date
  - description: The date the planning application was submitted
    field: start-date
  - description: The date the planning application was decided upon
    field: decision-date
  - description: The date the planning application was withdrawn or removed from the
      register
    field: end-date
  name: Planning application
- dataset: planning-application-log
  fields:
  - description: The reference for the planning application status (for example, "27/AP/9032/FULL")
    field: reference
  - description: The planning application reference (for example, "27/AP/9032")
    field: planning-application
  - dataset: planning-application-status
    description: The reference code for the change of planning application status
      (for example "validated", "decided" or "under-appeal")
    field: planning-application-status
  - description: The URL for a web page where a user can see the change in the planning
      application status
    field: documentation-url
  - description: The URL for a document which evidences the change in the planning
      application status
    field: document-url
  - description: Optional notes text
    field: notes
  - description: The code for the organisation responsible for processing the application
    field: organisation
  - description: The date this event happened or the change in status applies from
    field: event-date
  - description: The date this data was created or last updated
    field: entry-date
  - description: The date this fact was true from
    field: start-date
  - description: The date this change of event no longer applies. This is the same
      as the start-date in case of an error
    field: end-date
  name: planning application log
- dataset: planning-application-document
  fields:
  - description: An unique identifier for the document (for example, "27/AP/9032/DOC/3")
    field: reference
  - description: The name of this document
    field: name
  - description: Brief description of this document
    field: description
  - description: The planning application reference (for example, "27/AP/9032")
    field: planning-application
  - dataset: planning-application-document-type
    description: The code for this document type (for example "proposed-plan")
    field: document-type
  - description: The webpage where you can find this document
    field: documentation-url
  - description: The URL of the actual document
    field: document-url
  - description: Optional notes
    field: notes
  - description: The code for the responsible organisation (for example, local-authority-eng:BST)
    field: organisation
  - description: The date this data was created or last updated
    field: entry-date
  - description: The date the document was published
    field: start-date
  name: planning application document
description: planning application
end-date: ''
entry-date: '2025-02-13'
github-discussion: 25
name: Planning application decision
plural: Planning application decisions
specification: planning-application-decision
specification-reason: prospective
specification-status: working-draft
start-date: ''
---
