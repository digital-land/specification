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
            description: An unique identifier for a planning application
          - field: name
            description: Name of the planning application (for example, "Residential alteration to Downton House")
          - field: description
            description: Brief description of the application (for example, "Alterations to two windows on the southern elevation of the 3rd floor flat")
          - field: address-text
            description: The address of the site as a single line of text
          - field: address
            description: The UPRN for the address of the site
          - field: geometry
            description: the boundary of the site as a POLYGON or MULTIPOLYGON, with points in the EPSG 4326 coordinate reference system, and WGS85 datum, encoded in Well-Known Text (WKT) representation of geometry
          - field: point
          - field: documentation-url
            description: The web page where you can find the documentation for the planning application.
          - field: notes
          - field: planning-application-type
          - field: planning-decision
          - field: planning-decision-type
          - field: notes
            description: Optional notes
          - field: organisation
            description: The code for the responsible organisation
          - field: entry-date   
          - field: start-date
          - field: end-date
---
