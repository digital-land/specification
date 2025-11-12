---
title: Provide your Developer contributions data
name: Developer contributions
url: 
updated: 2022-06-09
summary: 
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
attachments:
- url: /specification/specification/developer-contributions
  name: 'Developer contributions technical specification (9 June 2022)'
  attachment-type: HTML
  start-date: 
---

^Follow this guidance when providing your Developer contributions data.^

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can find it, 
understand its quality, and trust it will be sustained.

<p>The Community Infrastructure Levy (CIL) regulations require all local planning authorities that 
issue a CIL liability notice or enter into section 106 planning obligations during a reporting year 
to publish an infrastructure funding statement (IFS) at least annually. 
The infrastructure funding statement should, as a minimum, include the information set out in 
<a href="https://www.legislation.gov.uk/ukdsi/2010/9780111492390/contents">Schedule 2 to the Community Infrastructure Levy regulations 2010</a>
(as inserted by the 2019 regulations).</p>
<p>In addition, it is recommended that local authorities also publish the raw data that informed the infrastructure funding statement.
This guidance sets out a data format and approach that you can follow in order to publish data that sits behind the infrastructure statement.</p>
<p>The data format and infrastructure funding statements will give policy makers and communities better insight into how developer contributions
are supporting new development and local infrastructure.
We have designed the data format to cause as little disruption as possible to existing processes.</p>

## Providing Developer contributions data

Take the following steps to provide your Developer contributions data:

s1. [Prepare your data](#prepare-your-data)
s2. [Check your data](#check-your-data)
s3. [Publish your data](#publish-your-data)
s4. [Tell us about your data](#tell-us-about-your-data)
s5. [Keep your data up-to-date](#keep-your-data-up-to-date)

## Prepare your data
Start by reviewing any data we may already have about your organisation
on [planning.data.gov.uk](https://planning.data.gov.uk)
using the [check and provide service](https://provide.planning.data.gov.uk).
This may include any data you have provided in the past, along with
information found on your website, or in other open data.

The most recent data you provide will be treated as being more authoritative
than any data we have collected from you previously, or found in other sources.

You can download tabular data we have for your organisation as a CSV file
from the [check and provide service](https://provide.planning.data.gov.uk)
and modify it using a spreadsheet or other CSV editor.

Similarly, you can download geospatial data we have for your organisation as
CSV or GeoJSON from [planning.data.gov.uk](https://planning.data.gov.uk)
and modify it using QGIS or other GIS tools.

The [files, fields and format](#files-fields-and-formats) of the data you need to
provide are documented below, and formally defined in the
[technical specifications](#technical-specifications) attached to this page.

Your data does not need to be complete or perfect to start with.
For many purposes having some data is better than no data,
so start by providing the Developer contributions information you have,
and continue to iterate and improve it over time.

## Check your data
Use the [check and provide service](https://provide.planning.data.gov.uk) to review your data before you publish it. 
The service will show you how the data will appear on [planning.data.gov.uk](https://planning.data.gov.uk) 
along with feedback on how you might improve your data.

## Publish your data
Publishing your data consists of two parts:

* An [endpoint](#endpoint) where the data can be downloaded from
* A [source](#source) where the information contained in the data is presented on your website

### Endpoint

Publish your data at a public endpoint, in a way in which anyone can download and use it.

The endpoint is a URL from which the data can be downloaded.
This can be a single file hosted on your website.
Alternatively, you can serve your data using an OGC WFS or other API
using a third-party service such as GitHub or ArcGIS.

Ensure your endpoint URL is documented and linked to from a public webpage to help people easily find and download the data.

The documentation webpage for your endpoint should include a clear statement that the data is provided as open data under
the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

### Source

The source is a webpage where a user can see the same information that is shown in the data.
This is usually one of your existing planning policy pages on your official <code>.gov.uk</code> website.

It is important that the source page links to the endpoint documentation webpage to 
help users trust the authenticity of the data.

## Tell us about your data
Once you have published the data, tell us about it so we can index and quickly make it available 
nationally on [planning.data.gov.uk](https://planning.data.gov.uk).

Use the [check and provide service](https://provide.planning.data.gov.uk/) to tell us where it is. 

You will need to provide for each dataset:

* the [source](#source) URL where the information in the data is presented on your website
* the [endpoint](#endpoint) URL from which the data can be collected

The provide service also asks for your name and email address as a point of contact in case of any issues.

## Keep your data up-to-date
You should continue to improve your data, and act on the feedback from the [check and provide service](https://provide.planning.data.gov.uk) 
to ensure your data meets the specification.

You will also need to update and republish your data whenever there's a change to your Developer contributions information.

We look for changes to the data at all of the endpoint URLs we know about every night,
so we can quickly update [planning.data.gov.uk](https://planning.data.gov.uk).

It is simpler if you publish your changes to the same endpoint URL.
If you create a new endpoint you will need to [tell us about your data](#tell-us-about-your-data) again.

## Files, fields and formats

You need to provide 3 datasets:

* [Developer agreement](#Developer-agreement-dataset)
* [Developer agreement contribution](#Developer-agreement-contribution-dataset)
* [Developer agreement transaction](#Developer-agreement-transaction-dataset)


You need to provide each dataset 
as a separate CSV file 
following the government 
[tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).
Where your dataset contains geospatial fields, you may use one of the following formats: 

* CSV
* GeoJSON
* GML
* KML
* Geopackage

### Field names

You can use upper- or lower-case names for your fields, and any punctuation characters are ignored,
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

### Developer agreement dataset



The Developer agreement dataset contains the following fields:



#### reference

Enter reference to help people find and link to the data.
If you don’t have a reference for this item, you will need to create one that is:

* unique within your data
* persistent — it doesn’t change when the data is updated

A good reference is something you already use.
Where these aren&#39;t unique, you make them unique by appending the year, or even the full date.
Great references are short, easy to read, to pronounce and remember.

#### name



#### developer-agreement-type



#### planning-application



#### document-url



#### notes

Enter any notes or commentary which helps you or others understand how this data was made, or how it may be interpreted.

#### organisation

Enter a CURIE value for the organisation from [this list](https://www.planning.data.gov.uk/organisation/).

#### entry-date

Enter the date this data was created or modified.

#### start-date



#### end-date



### Developer agreement contribution dataset



The Developer agreement contribution dataset contains the following fields:



#### reference

Enter reference to help people find and link to the data.
If you don’t have a reference for this item, you will need to create one that is:

* unique within your data
* persistent — it doesn’t change when the data is updated

A good reference is something you already use.
Where these aren&#39;t unique, you make them unique by appending the year, or even the full date.
Great references are short, easy to read, to pronounce and remember.

#### developer-agreement



#### contribution-purpose



#### amount



#### units



#### notes

Enter any notes or commentary which helps you or others understand how this data was made, or how it may be interpreted.

#### organisation

Enter a CURIE value for the organisation from [this list](https://www.planning.data.gov.uk/organisation/).

#### entry-date

Enter the date this data was created or modified.

#### start-date



#### end-date



### Developer agreement transaction dataset



The Developer agreement transaction dataset contains the following fields:



#### reference

Enter reference to help people find and link to the data.
If you don’t have a reference for this item, you will need to create one that is:

* unique within your data
* persistent — it doesn’t change when the data is updated

A good reference is something you already use.
Where these aren&#39;t unique, you make them unique by appending the year, or even the full date.
Great references are short, easy to read, to pronounce and remember.

#### developer-agreement-contribution



#### contribution-funding-status



#### amount



#### units



#### notes

Enter any notes or commentary which helps you or others understand how this data was made, or how it may be interpreted.

#### organisation

Enter a CURIE value for the organisation from [this list](https://www.planning.data.gov.uk/organisation/).

#### entry-date

Enter the date this data was created or modified.

#### start-date



#### end-date





## Contact us

$CTA
If you need any help at any stage of the process,
let us know by emailing <digitalland@communities.gov.uk> and a member of our team will be in touch.
$CTA

You can participate in
improving the design of this data 
,
and help ensure planning data meets your needs at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 


## Technical specifications