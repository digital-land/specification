---
title: Provide your Article 4 direction data
name: Article 4 direction
url: 
summary: 
entry-date: 2025-11-08
updated: 8 November 2025
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
attachments:
- url: /specification/specification/article-4-direction
  name: 'Article 4 direction technical specification (8 November 2025)'
  attachment-type: HTML
  start-date: 
---

^Follow this guidance when providing your Article 4 direction data.^

<p>Local Planning Authorities and other organisations 
<a href="https://www.localdigital.gov.uk/digital-planning/funding/">funded by the Digital Planning Programme</a>
to join the <a href="https://opendigitalplanning.org/digital-planning-improvement">Open Digital Planning community</a>
are expected to provide data to this specification.</p>
<p>If you're a Local Planning Authority who is interested in becoming a member,
you can <a href="https://opendigitalplanning.org/join">join the community</a>.</p>
<p>Otherwise there is no obligation on any party to provide data to this specification.</p>
<p>A future version of this specification may be published on GOV.UK,
and cited as one of a number of official data standards for the provision of planning data 
by planning authorities under the 
<a href="https://www.legislation.gov.uk/ukpga/2023/55/part/3/chapter/1/enacted">Levelling-up and Regeneration Act 2023</a>.</p>

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can:

* find it
* understand its meaning and purpose
* assess its quality
* trust it will be maintained

[You can help to design this and other data standards to ensure they your needs](https://design.planning.data.gov.uk). 

## Providing your Article 4 direction data

Take the following steps to provide your Article 4 direction data:

s1. [Prepare your data](#prepare-your-data)
s2. [Check your data](#check-your-data)
s3. [Publish your data](#publish-your-data)
s4. [Tell us about your data](#tell-us-about-your-data)
s5. [Keep your data up-to-date](#keep-your-data-up-to-date)

## Prepare your data
Start by reviewing any data we may already have about your organisation
on [planning.data.gov.uk](https://planning.data.gov.uk)
using the [check and provide service](https://provide.planning.data.gov.uk).
This might include: 

* any data you have provided in the past
* information found on your website
* open data from other public sources

We treat the data you provide as being more authoritative
than data we have collected from you previously, or found elsewhere.

You can download tabular data we have for your organisation as a CSV file
from the [check and provide service](https://provide.planning.data.gov.uk)
and edit it using a spreadsheet or other CSV editors.

Similarly, you can download geospatial data we have for your organisation as
CSV or GeoJSON from [planning.data.gov.uk](https://planning.data.gov.uk)
and modify it using QGIS or other GIS tools.

You must provide data containing the mandatory fields identified here where 
required by law.
Otherwise your data does not need to be complete or perfect to start with.
For many purposes having some data is better than no data,
so start by providing the best article 4 directions information you have,
and continue to iterate and improve it over time.

### Files





For article 4 directions you may provide the following dataset:


* [Article 4 direction](#Article-4-direction-dataset)
* [Article 4 direction area](#Article-4-direction-area-dataset)



Each dataset needs to be provided
in a separate CSV file 
following the government 
[tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).

Where your dataset contains geospatial fields, you may use one of the following formats: 

* CSV
* GeoJSON
* GML
* KML
* Geopackage


The fields and format of the data you need to
prepare are documented below, and formally defined in the
[technical specifications](#technical-specifications) attached to this page.

### Field names

You can use uppercase or lowercase names for your fields, and any punctuation characters are ignored,
meaning the following examples are all valid ways of naming the `start-date` field in your data:

* `StartDate`
* `Start Date`
* `START_DATE`
* `start.date`

### Reference values

Each dataset has a `reference` field.
Reference values are important to help people find and link to the data.
Where you don’t have a reference for an item, you will need to create one that is:

* unique within your data
* persistent — it doesn’t change when the data is updated

A good reference is something you already use.
Where these aren't unique, you make them unique by appending the year, or even the full date.
Great references are short, easy to read, to pronounce and remember.

### Date values

All dates must be in the format `YYYY-MM-DD`, following the guidance for [formatting dates and times in data](https://www.gov.uk/government/publications/open-standards-for-government/date-times-and-time-stamps-standard).

Where you don't know the precise date you can enter just the month `YYYY-MM` or even just the year `YYYY`.
The platform will default a `start-date` to the first of the month, or the first of January, and an `end-date` to the last day of the month, or the last day of December. For example:

* `2025-04-19`
* `2025-04`
* `2025`


### Geometry and point fields

All coordinates in any geospatial data you provide must be in the WGS84 (ETRS89) coordinate reference system following the government guidance on the [Exchange of a location point](https://www.gov.uk/government/publications/open-standards-for-government/exchange-of-location-point).

A `geometry` field may contain a single `POLYGON` or a `MULTIPOLYGON` object. A `point` field may only contain a single `POINT` object.

If you’re providing geospatial data in a CSV, the field must be encoded as well-known text (WKT), for example:

* `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,...` 
* `POLYGON ((1.188829 51.23478,1.188376 51.234909,...`
* `POINT (-3.466788 50.58151)`

When providing geospatial data as GeoJSON, GML, KML or in a Geopackage, use the native format for the geospatial data. 
That is there is no need to duplicate the geospatial data into a `point` or `geometry` property or field.




## Article 4 direction dataset





### Mandatory fields

Your Article 4 direction data must contain the following fields:






### Recommended fields

Your Article 4 direction data should also contain the following fields:






### Optional fields

Your Article 4 direction data may also contain the following fields:






## Article 4 direction area dataset





### Mandatory fields

Your Article 4 direction area data must contain the following fields:






### Recommended fields

Your Article 4 direction area data should also contain the following fields:






### Optional fields

Your Article 4 direction area data may also contain the following fields:






## Check your data
Use the [check and provide service](https://provide.planning.data.gov.uk) to review your data before you publish it. 
The service will show you how the data will appear on [planning.data.gov.uk](https://planning.data.gov.uk) 
along with feedback on how you might improve your data.

## Publish your data
Publishing your data consists of two parts:

* An **endpoint** where the data can be downloaded from
* A **source webpage** where the information contained in the data is presented on your website

### Endpoint

Make your data available at a public endpoint. 
An endpoint is a URL from which anyone can download the data. This can be either: 

* a single file hosted on your website 
* a file hosted on another public website including GitHub
* an Open Geospatial Consortium Web Feature Service (OGC WFS) 
* an open application programming interface (API) such as ArcGIS

Ensure your endpoint URL is documented and linked to from a public webpage to help people easily find and download the data.

The documentation webpage for your endpoint should include a clear statement that the data is provided as open data under
the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

### Source webpage

The source webpage is where a user can see the same information that is shown in the data.
This is usually one of your existing planning policy pages on your official <code>.gov.uk</code> website.

It is important that the source webpage links to the endpoint documentation webpage to 
help users trust the authenticity of the data.

## Tell us about your data
Once you have published the data, tell us about it so we can index and quickly make it available 
nationally on [planning.data.gov.uk](https://planning.data.gov.uk).

Use the [check and provide service](https://provide.planning.data.gov.uk/) to tell us where it is. 

You will need to provide for each dataset:

* the **source webpage** URL where the information in the data is presented on your website
* the **endpoint** URL from which the data can be collected

The service also asks for your name and email address as a point of contact in case of any issues.

## Keep your data up-to-date
Continue to improve your data, and act on the feedback from [the service](https://provide.planning.data.gov.uk) 
to ensure your data meets the specification.

You also need to update and republish your data whenever there's a change to your article 4 directions information.

We look for changes to the data at all of the endpoint URLs we know about every night,
so we can quickly update [planning.data.gov.uk](https://planning.data.gov.uk).

It is simpler if you publish your changes to the same endpoint URL.
If you create a new endpoint you need to [tell us about your data](#tell-us-about-your-data) again.

## Contact us

$CTA
If you need any help at any stage of the process,
let us know by emailing <digitalland@communities.gov.uk> and a member of our team will be in touch.
$CTA

You can participate in
[improving the design of this data](https://design.planning.data.gov.uk/consideration/article-4-directions),
and help ensure planning data meets your needs at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 

## Technical specifications