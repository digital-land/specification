---
specification: conservation-area
name: Conservation area
plural: conservation areas
specification-status: candidate-standard
start-date: ''
end-date: ''
entry-date: '2023-09-08'
github-discussion: 33
version: 1.4.3
datasets:
    - dataset: conservation-area
      fields:
        - field: reference
          description: provide a reference such as CA01
          guidance: |
            A reference or ID for each conservation area that is:

            - unique within your dataset
            - permanent - it doesn't change when the dataset is updated
            If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

            Example: `CA01`
        - field: name
          description: the official name for the conservation area
          guidance: |
            The official name of the conservation area.

            Example: `Old Market`
        - field: designation-date
          description: the date that the conservation area was officially designated
          guidance: |
            The date that the conservation area was officially designated, written in YYYY-MM-DD format.

            Example:

            `1984-03-28`

            With dates, some data is better than no data, so:

            - `1984` is fine
            - `1984-03` is better
            - `1984-04-28` is brilliant
        - field: document-url
          description: a URL to the authoritative source for the area, this is often a PDF containing a map with the area drawn on it
          guidance: |
            A URL to the document containing the authoritative source for the area. This is usually a PDF containing the area drawn on a map.

            Example: `http://www.LPAwebsite.org.uk/data/conservationareas/smithroad-area.pdf`
        - field: documentation-url
          description: a URL to a page on the local planning authority website that provides information about the conservation area
          guidance: |
            The URL of the webpage on your website that introduces the document.

            Each document should be linked to from a documentation webpage that includes a short description of the data and the document you’re linking to. Each conservation area should have a unique URL. This means you can create a separate page for each one, or you could list several on one page. If you do that, there must be a separate anchor (fragment identifier) for each one. This means each section of your page should have its own URL. Most publishing systems will allow you to use a hashtag to create the identifiers for each conservation area you list - as in the examples shown.

            Examples:

            One conservation area per page: `http://www.LPAwebsite.org.uk/conservationareas/smithroad`

            More than one conservation area per page with an anchor link for each one:

            `http://www.LPAwebsite.org.uk/conservationareas#smithroad`

            `http://www.LPAwebsite.org.uk/conservationareas#broadhousepark`

            ![](https://digital-land.github.io/images/diagrams/document-documentation-url.png)
        - field: geometry
          description: the boundary of a designated conservation area
          guidance: |
            The boundary for the designated conservation area. The boundary may be a single polygon or a multipolygon value. All points should be in the WGS84 coordinate reference system if possible. If you can’t do this, give us what you have and then we can transform it into WGS84. However, this could mean there’s a small loss of precision when we do the transformation. If you’re providing geometry in a CSV, geometry should be in well-known text (WKT).

            Example: `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

            If you’re providing geometry in a GeoJSON, GML or Geopackage, use the associated geometry format.
        - field: point
          description: provide the centre point of the conservation area if you do not have a full geometry available
        - field: notes
          description: provide any extra information if needed
          guidance: |
            Optional text on how this data was made or produced, or how it can be interpreted.
        - field: organisation
          description: the organisation responsible for conservation areas
          guidance: |
            The code for the organisation responsible for the conservation area. If the responsible organisation is your local authority, leave this field blank and we will default to that. If another organisation is responsible, for example Historic England, then enter the code for that organisation.

            Example: `local-authority:BUC`

            Create this code by using the relevant prefix, a colon (:), and the reference for your organisation from this [list of organisations](https://www.planning.data.gov.uk/organisation/).
        - field: entry-date
          description: the date the information has been entered as a record
          guidance: |
            The date the record was last updated.

            If the entity has never been updated, enter the same date as start-date.

            Write in `YYYY-MM-DD` format.

            Example:

            `2022-12-20`

            With dates, some data is better than no data, so:

            - `2022` is fine
            - `2022-12` is better
            - `2022-12-20` is brilliant
        - field: start-date
          description: the date the validity of the record starts
          guidance: |
            The date the validity of the record starts, written in YYYY-MM-DD format. Usually, this will be the same as the designation date. If anything about the conservation area has changed, for example, the boundary, it should be the date of that change.

            Example:

            `1984-04-25`

            With dates, some data is better than no data, so:

            - `1984` is fine
            - `1984-04` is better
            - `1984-04-25` is brilliant
        - field: end-date
          description: the date the validity of the record ends
          guidance: |
            Where the conservation area is no longer valid, this should be the date that it was no longer in effect, written in YYYY-MM-DD format. If this does not apply, leave the cell blank.

            Example:

            `1999-01-20`

            With dates, some data is better than no data, so:

            - `1999` is fine
            - `1999-01` is better
            - `1984-01-20` is brilliant
    - dataset: conservation-area-document
      fields:
        - field: reference
          description: provide a reference such as CA01-decision-notice
          guidance: |
            A reference or ID for each document that is:

            - unique within your dataset
            - permanent - it doesn’t change when the dataset is updated
            If you don’t use a reference already, you will need to create one. This can be a short set of letters or numbers.

            Example: `CADOC01`
        - field: conservation-area
          description: the reference for the conservation area this document is about
          guidance: |
            The reference for the conservation area this document refers to, as used in the conservation area dataset.

            Example: `CA1`
        - field: name
          description: the title of the conservation area document
          guidance: |
            The title of the document.

            Example: `Notice of Old Market conservation area designation`
        - field: documentation-url
          description: the URL of the webpage citing the document
          guidance: |
            The URL of the webpage introducing the document.

            Each document should be linked to on a documentation webpage that includes a short description of the data. The website URL should be unique for each conservation area, either by creating a separate page or a separate anchor (fragment identifier) for each one.

            Example: `http://www.LPAwebsite.org.uk/data#conservationarea1`
        - field: document-url
          description: the URL of the document
          guidance: |
            The URL of the document.

            Example: `http://www.LPAwebsite.org.uk/conservationarea1.pdf`
        - field: document-type
          dataset: conservation-area-document-type
          description: "the type of the conservation area document which must be one of the following values: 'area-appraisal', 'notice', or leave blank"
          guidance: |
            The code for the type of document this record refers to. Find the code you need using this [finder tool](https://dluhc-datasets.planning-data.dev/dataset/conservation-area-document-type/finder).
        - field: notes
          description: provide any extra information if needed
          guidance: |
            Optional text on how this data was made or produced, or how it can be interpreted.
        - field: organisation
          description: the organisation that published the document
        - field: entry-date
          description: the date this information has been entered as a record
          guidance: |
            The date the entity was last updated.

            If the entity has never been updated, enter the same date as start-date.

            Write in YYYY-MM-DD format.

            Example:

            `1984-03-28`

            With dates, some data is better than no data, so:

            - `1984` is fine
            - `1984-03` is better
            - `1984-03-28` is brilliant
        - field: start-date
          description: the date the validity of the record starts
          guidance: |
            The date the document was published, written in YYYY-MM-DD format.

            Example:

            `1984-03-28`

            With dates, some data is better than no data, so:

            - `1984` is fine
            - `1984-03` is better
            - `1984-03-28` is brilliant
        - field: end-date
          description: the date the validity of the record ends
          guidance: |
            The date the document was withdrawn or superseded by another document, written in YYYY-MM-DD format. Leave this blank if the document is still relevant to planning.

            Example:

            `1984-03-28`

            With dates, some data is better than no data, so:

            - `1984` is fine
            - `1984-03` is better
            - `1984-03-28` is brilliant
---
