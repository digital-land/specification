---
specification: tree-preservation-order
name: Tree preservation order
plural: Tree preservation orders
specification-status: piloting
start-date: ''
end-date: ''
entry-date: '2023-09-08'
github-discussion: 43
version: 1.3.1
datasets:
  - dataset: tree-preservation-order
    name: tree preservation order
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the tree preservation order
        guidance: |
          A reference or ID for each tree preservation order that is:

          - unique within your dataset
          - permanent - it doesn't change when the dataset is updated
          If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

          Example: `TPO1`
      - field: name
        description: the name of the tree preservation order
        guidance: |
          This will be the title of the page hosting data about this tree preservation order on your website. This can be:

          - name
          - reference
          - address
          - blank
      - field: documentation-url
        description: the URL of the web page where you can find information about the tree preservation order
        guidance: |
          The URL of the webpage on your website that introduces the document.

          Each document should be linked to from a documentation webpage that includes a short description of the data and the document you’re linking to. Each tree preservation order should have a unique URL. This means you can create a separate page for each one, or you could list several on one page. If you do that, there must be a separate anchor link (fragment identifier) for each one.

          This means each section of your page should have its own URL. Most publishing systems will allow you to use a hashtag to create the identifiers for each tree preservation order you list - as in the examples shown.

          Examples:

          One tree preservation order per page:

          `http://www.LPAwebsite.org.uk/data/treepreservationorders/smithroad`

          More than one tree preservation order per page with an anchor link for each one:

          `http://www.LPAwebsite.org.uk/data/treepreservationorders#smithroad`

          `http://www.LPAwebsite.org.uk/data/treepreservationorders#broadhousepark`
      - field: document-url
        description: the URL of the tree preservation order document. If a TPO is revoked you can blank out this field.
        guidance: |
          The URL of an authoritative order or notice designating the tree preservation order. If the TPO has been revoked, you can blank out this field.

          Example: `http://www.LPAwebsite.org.uk/tpo1.pdf`
      - field: made-date
        description: the date the tree preservation order was "made"
        guidance: |
          The date a tree preservation order was made available to the public. The tree or trees are temporarily protected from this date, until the order is confirmed.

          Write in YYYY-MM-DD format.

          Example: `2022-12-20`
      - field: confirmed-date
        description: the date the tree preservation order was "confirmed"
        guidance: |
          The date a tree preservation order is confirmed as being in effect, and the tree or trees are fully protected. This comes after all objections have been considered.

          Write in YYYY-MM-DD format.

          Example: `2022-12-20`
      - field: notes
        description: optional notes
        guidance: |
          Optional text on how this data was or produced, or how it can be interpreted.
      - field: organisation
        description: the organisation responsible for this tree preservation order
      - field: entry-date
        description: the <a href="#date">date</a> this entry was created or amended
        guidance: |
          The date the entity was last updated.

          If the entity has never been updated, enter the same date as start-date.

          Write in YYYY-MM-DD format.

          Example: `2022-12-20`
      - field: start-date
        description: the <a href="#date">date</a> the tree preservation order came into force
        guidance: |
          The date that the tree preservation order came into force, written in `YYYY-MM-DD` format.

          Example: `1984-03-28`
      - field: end-date
        description: the <a href="#date">date</a> the tree preservation order was revoked. Leave blank if the TPO is still active
        guidance: |
          Where the tree preservation order is [revoked](https://standards.planning-data.dev/principles/#we-shouldn%E2%80%99t-delete-entries-in-a-register), this should be the date that it was no longer in effect, written in `YYYY-MM-DD` format. If the TPO is still active, leave this field blank. If the tree has been felled, use the felled-date field.

          Example: `1999-01-20`
  - dataset: tree-preservation-zone
    name: tree preservation zone
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the tree preservation zone
        guidance: |
          A reference or ID for each tree preservation zone that is:

          - unique within your dataset
          - permanent - it doesn't change when the dataset is updated
          If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

          Example: `TPO1`
      - field: name
        description: the name of the tree preservation zone
        guidance: |
          This will be the display name of the page hosting data about this tree preservation zone on your website. This can be:

          - name
          - reference
          - address
          - blank
      - field: tree-preservation-order
        description: the <a href="#reference">reference</a> for the tree preservation order
        guidance: |
          The reference for the tree preservation order that covers this zone.
      - field: tree-preservation-zone-type
        description: the type of zone, for example area, group or woodland
        dataset: tree-preservation-zone-type
        guidance: |
          What sort of tree preservation zone this is.

          This can be:

          - area
          - group
          - woodland
      - field: geometry
        description: the boundary of the area covered by the tree preservation zone in WKT format
        guidance: |
          The boundary for the tree preservation zone as a single polygon or multipolygon value. All points in the polygon must be in the WGS84 coordinate reference system.

          If you’re providing geometry in a CSV, geometry should be in well-known text (WKT).

          Example: `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

          If you’re providing geometry in a GeoJSON, GML or Geopackage, use the associated geometry format.
      - field: point
        description: the centre of the tree preservation zone if you cannot provide the full geometry
      - field: notes
        description: optional notes
        guidance: |
          Optional text on how this data was made or produced, or how it can be interpreted.
      - field: organisation
        description: the organisation responsible for this tree preservation order
      - field: entry-date
        description: the <a href="#date">date</a> this entry was created or amended
        guidance: |
          The date the entity was last updated.

          If the entity has never been updated, enter the same date as start-date.

          Write in `YYYY-MM-DD` format.

          Example: `2022-12-20`
      - field: start-date
        description: the <a href="#date">date</a> the tree preservation zone came into force
        guidance: |
          The date that the tree preservation order came into force, written in `YYYY-MM-DD` format.

          Example: `1984-03-28`
      - field: end-date
        description: the <a href="#date">date</a> the tree preservation zone ended or leave blank if the zone is still active
        guidance: |
          If applicable, the date that the tree preservation order was revoked, written in `YYYY-MM-DD` format. If it's still in effect, leave the cell blank.

          Example: `1999-01-20`
  - dataset: tree
    name: tree
    fields:
      - field: reference
        description: the number or reference for the tree which appears in the preservation order
        guidance: |
          A reference or ID for each tree that is:

          - unique within your dataset
          - permanent - it doesn't change when the dataset is updated
          If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

          Example: `T1`
      - field: name
        description: the name of the tree
        guidance: |
          This will be the title of the page hosting data about this tree preservation order on your website. This can be:

          - name
          - reference
          - address
          - blank
      - field: tree-preservation-order
        description: the <a href="#reference">reference</a> for the tree preservation order
        guidance: |
          The reference for the tree preservation order that affects this tree.

          Example: `TPO1`
      - field: uprn
        description: unique property reference number if the tree is located on an addressable property
        dataset-field: address
        guidance: |
          If the tree has one, you can provide the Unique Property Reference Number (UPRN). [Find the UPRN on GeoPlace](https://www.geoplace.co.uk/addresses-streets/location-data/the-uprn).

          If you provide the UPRN, you must also provide the address text.
      - field: address-text
        description: the address of the property
        guidance: |
          If the tree has one, you can provide the address, written as text.

          If you provide the address text, you must also provide the UPRN.

          Example: `100 High Street, Bath`
      - field: point
        description: the centre of the tree area if you cannot provide the full geometry
        guidance: |
          The approximate location of the centre of the tree.

          You must provide a point or geometry for each tree. You may provide both.

          The point must be in the WGS84 coordinate reference system. If you’re providing point in a CSV, geometry should be in well-known text (WKT).

          Example: `POINT (-0.681152 52.762892)`

          If you’re providing point in a GeoJSON, GML or Geopackage, use the associated geometry format.
      - field: geometry
        description: the boundary of the area covered by the tree in WKT format
        guidance: |
          The boundary of the tree as a single polygon or multipolygon value. All points in the polygon must be in the WGS84 coordinate reference system.

          If you’re providing geometry in a CSV, geometry should be in well-known text (WKT).

          You must provide a point or geometry for each tree. You may provide both.

          Example: `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

          If you’re providing geometry in a GeoJSON, GML or Geopackage, use the associated geometry format.
      - field: notes
        description: optional notes
        guidance: |
          Optional text on how this data was made or produced, or how it can be interpreted.
      - field: organisation
        description: the organisation responsible for this tree
      - field: felled-date
        description: the date the tree was felled
        guidance: |
          If applicable, the date that the tree was felled, written in `YYYY-MM-DD` format. If the tree hasn't been felled, leave this field blank.
      - field: entry-date
        description: the <a href="#date">date</a> this entry was created or amended
        guidance: |
          The date the entity was last updated.

          If the entity has never been updated, enter the same date as start-date.

          Write in `YYYY-MM-DD` format.

          Example: `2022-12-20`
      - field: start-date
        description: the <a href="#date">date</a> from which the tree preservation order affects the tree
        guidance: |
          The date from which the tree preservation order affects the tree, written in `YYYY-MM-DD` format.

          Example: `1984-03-28`
      - field: end-date
        description: the <a href="#date">date</a> the tree preservation order no longer affects the tree, or leave blank if the tree is still under the order. Use the felled-date if the tree has been felled.
        guidance: |
          Where the tree preservation order is [revoked](https://standards.planning-data.dev/principles/#we-shouldn%E2%80%99t-delete-entries-in-a-register), this should be the date that it was no longer in effect, written in `YYYY-MM-DD` format. If the TPO is still active, leave this field blank. If the tree has been felled, use the felled-date field.

          Example: `1999-01-20`
