---
consideration: 
datasets:
  - dataset: site
    fields:
      - field: reference
        requirement-level: MUST
        guidance: 'Give each site a unique reference. This could be taken from the planning application or unique document reference. For example "24_09868_SITE_LOCATION_PLAN-1892681"'
      - field: name
        requirement-level: MUST
        guidance: 'Give each site a name.'
      - field: description
        requirement-level: MAY
        guidance: "You may provide additional description for the location of the site."
      - field: geometry
        requirement-level: MUST
      - field: address-text
        requirement-level: MAY
        guidance: "Provide the address of the site where one exists."
      - field: postcode
        requirement-level: MAY
        guidance: "Provide a postcode for the address of the site where one exists."
      - field: documentation-url
        requirement-level: MUST
        guidance: "Enter a link to the authority page which links to the location plan."
      - field: document-url
        requirement-level: MUST
        guidance: "Link to the document containing the location-plan for the site which is usually a PDF file."
      - field: site-plan-url
        requirement-level: SHOULD
        guidance: "Link to the site-plan document where this is different to the `location-plan`."
      - field: start-date
        requirement-level: MUST
        guidance: "Enter the date for when the location-plan document was created."
      - field: entry-date
        requirement-level: MUST
      - field: notes
        requirement-level: MAY
    priority: 1
    requirement-level: MUST
date-precision: YYYY-MM-DD
description: plot or area of land for a proposed development, operational work, or material change of use
end-date: ''
entry-date: '2026-10-16'
github-discussion: 
long-name: site
long-plural: sites
name: site
plural: sites
specification: site
specification-reason: prospectice
specification-status: open-standard
specification-reason: prospective
specification-status: piloting
start-date: ''
---
