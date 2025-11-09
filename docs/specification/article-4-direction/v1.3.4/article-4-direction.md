---
specification: article-4-direction
name: Article 4 direction
plural: article 4 directions
specification-status: candidate-standard
specification-reason: digital-planning-funding
start-date: ''
end-date: ''
entry-date: '2025-11-08'
github-discussion: 30
version: 1.3.4
datasets:
    - dataset: article-4-direction
      name: article 4 direction
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the article 4 direction
          guidance: |
            A reference or ID for each article 4 direction that is:

            - unique within your dataset
            - permanent - it doesn’t change when the dataset is updated
            If you don’t use a reference already, you will need to create one. This can be a short set of letters or numbers.

            Example: `A4D1`
        - field: name
          description: the name of the article 4 direction
          guidance: |
            The official name of the article 4 direction.

            Example: `Old Market`"
        - field: description
          description: a brief description of the article 4 direction
          guidance: |
            Optional short description of the article 4 direction’s purpose.

            Example: The railways arches should not be demolished or have their use changed from commercial to residential.
        - field: documentation-url
          description: the URL of the web page where you can find information about the article 4 direction
          guidance: |
            The URL of the webpage on your website that introduces the document.

            Each document should be linked to from a documentation webpage that includes a short description of the data and the document you’re linking to. Each article 4 direction should have a unique URL. This means you can create a separate page for each one, or you could list several on one page. If you do that, there must be a separate anchor link (fragment identifier) for each one.

            This means each section of your page should have its own URL. Most publishing systems will allow you to use a hashtag to create the identifiers for each article 4 direction you list - as in the examples shown.

            Example:

            One article 4 direction per page:

            `http://www.LPAwebsite.org.uk/data/article4directions/smithroad`

            More than one article 4 direction per page with an anchor link for each one:

            `http://www.LPAwebsite.org.uk/data/article4directions#smithroad`

            `http://www.LPAwebsite.org.uk/data/article4directions#broadhousepark`
        - field: document-url
          description: the URL of the web page where you can find the document for the article 4 direction
          guidance: |
            The URL of an authoritative order or notice designating the article 4 direction.

            Example: `http://www.LPAwebsite.org.uk/article4direction1.pdf`
        - field: notes
          description: optional notes
          guidance: |
            Optional text on how this data was made or produced, or how it can be interpreted.
        - field: organisation
          description: the organisation responsible for this article 4 direction
        - field: entry-date
          description: the date this information has been entered as a record
          guidance: |
            The date the entity was last updated.

            If the entity has never been updated, enter the same date as start-date.

            Write in `YYYY-MM-DD` format.

            Example: `2022-12-20`
        - field: start-date
          description: the date the validity of the record starts
          guidance: |
            The date that the article 4 direction came into force, written in `YYYY-MM-DD` format.

            Example: `1984-03-28`
        - field: end-date
          description: the date the validity of the record ends
          guidance: |
            Where the article 4 direction is [no longer valid](https://standards.planning-data.dev/principles/#we-shouldn%E2%80%99t-delete-entries-in-a-register), this should be the date that it was no longer in effect, written in `YYYY-MM-DD` format. If this does not apply, leave the cell blank.

            Example: `1999-01-20`
    - dataset: article-4-direction-area
      name: article 4 direction area
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the article 4 direction area
          guidance: |
            A reference or ID for each article 4 direction area that is:

            - unique within your dataset
            - permanent - it doesn’t change when the dataset is updated
            If you don’t use a reference already, you will need to create one. This can be a short set of letters or numbers.

            Example: `A4Da1`
        - field: name
          description: the name of the article 4 direction area
          guidance: |
            The official name of the article 4 direction. Example: `Old Market`
        - field: article-4-direction
          description: the <a href="#reference">reference</a> for the <a href="article-4-direction-dataset">article 4 direction</a> entry
          guidance: |
            The reference for the article 4 direction used in the article 4 direction dataset.

            Example: `A4D1`
        - field: permitted-development-rights
          description: a list of one or more <a href="#reference">reference</a> values for <a href="article-4-direction-rule-dataset">permitted development right</a> entries, separated by a semi-colon ';'.
          dataset: permitted-development-right
          guidance: |
            A list of the permitted development rights withdrawn by the article 4 direction.

            Separate the rights in the list using semicolons.

            Only use rights from our [permitted development right dataset](https://www.planning.data.gov.uk/dataset/permitted-development-right). If the area withdraws a permitted development right that is not in our dataset, email digitalland@communities.gov.uk.

            Example: `3D;3M;11B`
        - field: uprns
          description: unique property reference numbers for any addressable properties, separated by `;`
          guidance: |
            If the geometry is the boundary of a building, you can provide the Unique Property Reference Number (UPRN). Find the UPRN on GeoPlace.

            If you provide the UPRN, you must also provide the address text.
        - field: address-texts
          description: the addresses of any properties reference. The addresses should be written as address-text (a single line separated by commas). To write multiple addresses end each address with `;`
          guidance: |
            If the geometry is the boundary of a building, you can provide the address of the article 4 direction, written as text.

            If you provide the address text, you must also provide the UPRN.

            Example: `100 High Street, Bath`
        - field: geometry
          description: the boundary of the area covered by the article 4 direction in WKT format
          guidance: |
            The boundary for the article 4 direction area as a single polygon or multipolygon value. All points in the polygon must be in the WGS84 coordinate reference system.

            If you’re providing geometry in a CSV, geometry should be in well-known text (WKT).

            Example: `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

            If you’re providing geometry in a GeoJSON, GML or Geopackage, use the associated geometry format.
        - field: point
          description: centre point of the area
        - field: notes
          description: optional notes
          guidance: |
            Optional text on how this data was made or produced, or how it can be interpreted.
        - field: organisation
          description: the organisation responsible for article 4 direction area
        - field: entry-date
          description: the date this information has been entered as a record
          guidance: |
            The date the entity was last updated.

            If the entity has never been updated, enter the same date as start-date.

            Write in `YYYY-MM-DD` format.

            Example: `2022-12-20`
        - field: start-date
          description: the date the validity of the record starts
          guidance: |
            The date that the article 4 direction came into force, written in YYYY-MM-DD format.

            Example: `1984-03-28`
        - field: end-date
          description: the date the validity of the record ends
          guidance: |
            If applicable, the date that the article 4 direction was no longer in effect, written in `YYYY-MM-DD` format. If this does not apply, leave the cell blank.

            Example: `1999-01-20`
---
