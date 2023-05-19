---
specification: planning-application
name: Planning application
plural: Planning applications
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2023-05-15'
datasets:
    - dataset: planning-application
      name: planning application
      fields:
          - field: reference
            description: The planning application reference (for example, "27/AP/9032")
          - field: name
            description: Name of the planning application (for example, "Residential alteration to Downton House")
          - field: description
            description: Brief description of the application (for example, "Alterations to two windows on the southern elevation of the 3rd floor flat")
          - field: address-text
            description: The address of the site as a single line of text (for example, "11 High Street, Ambridge, BO22 3LL")
          - field: address
            description: The UPRN for the primary address of the site
          - field: geometry
            description: the boundary of the site as a POLYGON or MULTIPOLYGON, with points in the EPSG 4326 coordinate reference system, and WGS85 datum, encoded in Well-Known Text (WKT) representation of geometry
          - field: point
          - field: documentation-url
            description: The URL of this planning application in the planning register.
          - field: notes
          - field: planning-application-type
            dataset: planning-application-type
            description: The reference code for the type of planning application (for example "full-planning-permission")
          - field: planning-decision
            dataset: planning-decision
            description: The reference code for the planning decision made (for example "pending" or "permission-in-principle")
          - field: planning-decision-type
            dataset: planning-decision-type
            description: The reference code for the way the decision was made (for example "committee")
          - field: notes
            description: Optional notes text
          - field: organisation
            description: The reference code for the organisation responsible for processing the planning application
          - field: entry-date   
            description: The date this data was created or last updated
          - field: start-date
            description: The date the planning application was submitted
          - field: decision-date
            description: The date the planning application was decided upon
          - field: end-date
            description: The date the planning application was withdrawn or removed from the register
    - dataset: planning-application-log
      name: planning application log
      fields:
          - field: reference
            description: The reference for the planning application status (for example, "27/AP/9032/FULL")
          - field: planning-application
            description: The planning application reference (for example, "27/AP/9032")
          - field: planning-application-status
            dataset: planning-application-status
            description: The reference code for the change of planning application status (for example "validated", "decided" or "under-appeal")
          - field: documentation-url
            description: The URL for a web page where a user can see the change in the planning application status
          - field: document-url
            description: The URL for a document which evidences the change in the planning application status
          - field: notes
            description: Optional notes text
          - field: organisation
            description: The code for the organisation responsible for processing the application
          - field: entry-date   
            description: The date this data was created or last updated
          - field: start-date
            description: The date this change in status applies from
          - field: end-date
            description: The date this change of event no longer applies. This is the same as the start-date in case of an error
    - dataset: planning-application-document
      name: planning application document
      fields:
          - field: reference
            description: An unique identifier for the document (for example, "27/AP/9032/DOC/3")
          - field: name
            description: The name of this document
          - field: description
            description: Brief description of this document
          - field: planning-application
            description: The planning application reference (for example, "27/AP/9032")
          - field: document-type
            dataset: planning-application-document-type
            description: The code for this document type (for example "proposed-plan")
          - field: documentation-url
            description: The webpage where you can find this document 
          - field: document-url
            description: The URL of the actual document
          - field: notes
            description: Optional notes
          - field: organisation
            description: The code for the responsible organisation (for example, local-authority-eng:BST)
          - field: entry-date   
            description: The date this data was created or last updated
          - field: start-date
            description: The date the document was published
---
