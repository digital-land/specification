---
considerations: developer-contributions
datasets:
  - dataset: developer-agreement
    description: A developer agreement is any legal document that secures contributions from a development for infrastructure or affordable housing (including section 106 planning obligations and section 278 agreements), or any demand notice for CIL.
    fields:
      - field: reference
      - field: name
      - field: developer-agreement-type
      - field: planning-application
      - field: document-url
      - field: notes
      - field: organisation
      - field: entry-date
      - field: start-date
      - field: end-date
  - dataset: developer-agreement-contribution
    description: Developer agreement contributions are the individual obligations or sums within an agreement, assigned to particular purposes such as affordable housing.
    fields:
      - field: reference
      - field: developer-agreement
      - field: contribution-purpose
      - field: amount
      - field: units
      - field: notes
      - field: organisation
      - field: entry-date
      - field: start-date
      - field: end-date
  - dataset: developer-agreement-transaction
    fields:
      - field: reference
      - field: developer-agreement-contribution
      - field: contribution-funding-status
      - field: amount
      - field: units
      - field: notes
      - field: organisation
      - field: entry-date
      - field: start-date
      - field: end-date
description: ''
documentation-url: https://www.gov.uk/guidance/publish-your-developer-contributions-data
end-date: ''
entry-date: '2026-08-14'
github-discussion: 34
name: Developer contributions
plural: Developer contributions
specification: developer-contributions
specification-reason: cil-2019
specification-status: open-standard
start-date: '2019-09-01'
---
