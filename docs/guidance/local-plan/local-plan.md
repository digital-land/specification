---
title: Provide your local plan data
name: local plan
url: 
updated: 2025-11-08
summary: 
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
attachments:
- url: https://digital-land.github.io/specification/specification/local-plan/
  name: 'Local plan technical specification (8 November 2025)'
  attachment-type: HTML
  start-date: 
---

^Follow this guidance when providing your local plan data.^

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can find it, 
understand its quality, and trust it will be sustained.

<p>There are currently no obligations on anyone to follow this guidance, however a
future version of the technical specification may be formally published on GOV.UK,
and cited as one of a number of official data standards for the provision of planning data under the 
<a href="https://www.legislation.gov.uk/ukpga/2023/55/part/3/chapter/1/enacted">Levelling-up and Regeneration Act 2023</a>
or other legislation.</p>

## Providing local plan data

Take the following steps to provide your local plan data:

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
from the [check and provide service](https://provide.planning.data.gov.uk) service
and modify it using a spreadsheet or other CSV editor.

Similarly, you can download geospatial data we have for your organisation as
CSV or GeoJSON from [planning.data.gov.uk](https://planning.data.gov.uk)
and modify it using QGIS or other GIS tool.

The [files, fields and format](#files-fields-and-formats) of the data you need to 
provide are documented below, and formally defined in the 
[technical specifications](#technical-specifications) attached to this page.

Your data does not need to be complete or perfect to start with.
For many purposes having some data is better than no data,
so start by providing the local plans information you have,
and continue to iterate and improve it over time.

## Check your data
Use the [check and provide service](https://provide.planning.data.gov.uk) to review your data before you publish it. 
The service will show you how the data will appear on [planning.data.gov.uk](https://planning.data.gov.uk) 
along with feedback on how you might improve your data.

## Publish your data
Publishing your data consists of two parts:

* An [endpoint](#endpoint) from where the data can be downloaded
* A [source](#source) where the information contained in the data is presented on your website

### Endpoint

Publish your data at a public endpoint, in a way which anyone can download and use it.

The endpoint is a URL from which the data can be downloaded.
This can be a single file hosted on your website.
Alternatively, you can serve your data using an OGC WFS or other API
using a third-party service such as GitHub or ArcGIS.

Ensure your endpoint URL is documented and linked to from a public webpage to help people easily find and download the data.

The documentation webpage for your endpoint should include a clear statement that the data is provided as open data under
the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

### Source

The source is a webpage where a user can see the same information in the data.
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

You will also need to update and republish your data whenever there's a change to your local plans information.

We look for changes to the data at all of the endpoint URLs we know about every night,
so we can quickly update [planning.data.gov.uk](https://planning.data.gov.uk).

It is simpler if you publish your changes to the same endpoint URL.
If you create a new endpoint you will need to [tell us about your data](#tell-us-about-your-data) again.

## Files, fields and formats

You need to provide 3 datasets:

* [Local plan](#local-plan-dataset)
* [Local plan housing number](#local-plan-housing-number-dataset)
* [Local plan document](#Local-plan-document-dataset)


You need to provide each dataset as a CSV file following the government 
[Tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).
Where a dataset contains geospatial fields, you may use one of the following formats: 

* CSV
* GeoJSON
* GML
* KML
* Geopackage


### Field names

You can use upper or lowcase names for your fields, and any punctuation characters are ignored,
meaning the following examples all valid ways of naming the `start-date` field in your data:

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

* `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`
* `POLYGON ((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`
* `POINT (-3.466788 50.58151)`

When providing geospatial data as GeoJSON, GML, KML or in a Geopackage, use the native for the geospatial data. 
That is there is no need to duplicate the geospatial data into a `point` or `geometry` property or field.

### Local plan dataset

List the local plans you are responsible for with one row for each current, emerging or historical local plan.


The local plan dataset contains the following fields:



#### reference

Give each local plan a unique reference.
 For example:

* <code class="value">LP-BRX-2024</code>
* <code class="value">34069/County-Durham-Plan</code>
* <code class="value">central-lincolnshire</code>
* <code class="value">barnet-local-plan-2021-2036</code>


#### name

Use the title of the adopted local plan document. For example:

* <code class="value">County Durham Plan</code>
* <code class="value">South Oxfordshire Joint Local Plan</code>


#### period-start-date

Enter the start of the plan period. This is usually just a year in `YYYY` format.

#### period-end-date

Enter the end of the plan period. This is may be just the year in `YYYY` format.

#### local-planning-authorities

Enter the reference (the GSS code) for the 
[Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)
area covered by the plan.
For a joint local plan, enter the list of Local Planning Authority references, each separated by semi-colon &#39;;&#39; character.
 For example:

* <code class="value">E60000001</code>
* <code class="value">E60000132;E60000133;E60000135;E60000136</code>


#### local-plan-process

Indicate the local plan examination process for the local plan using one of the following values:

* `2012` for plans prepared under the Town and Country Planning (Local Planning) (England) Regulations 2012, including transitional arrangements
* `2025` for plans prepared under *new Local Planning Regulations (TBD)*


#### documentation-url

The URL of the webpage on your website for the local plan

Each entry in the local plan dataset should link to a documentation webpage that includes the information 
in the entry as well as links to where this data may be downloaded, and any other supporting documents.
Where there are several local plans listed on a single webpage, you can use use an anchor link (fragment identifier) 
to make the URL for each plan unique.
 For example:

* <code class="value">https://eastcambs.gov.uk/planning-and-building-control/planning-policy-and-guidance/adopted-local-plan/local-plan</code>
* <code class="value">https://example.com/local-plans/#example-local-plan-2011</code>
* <code class="value">https://example.com/local-plans/#example-local-plan-2024</code>


#### document-url

Enter the URL for the main or core plan document. This is usually a PDF file.
 For example:

* <code class="value">https://www.walthamforest.gov.uk/sites/default/files/2024-02/LBWF_LocalPlan_LP1_Feb2024_compressed.pdf</code>


#### entry-date

Enter the date this data was created or modified.

#### start-date

Enter the date when the plan was officially adopted. 
This value should match the relevant entry for when the plan was recoreded as being adopted in the `local-plan-timetable`.
Leave this value blank for plans which are being prepared, or haven&#39;t yet been adopted.


#### end-date

Enter the date the local plan was withdrawn or revoked, otherwise leave this field blank.


#### notes

You may provide notes on how this data was made, and help users differentiate the plan from others with a similar name. For example:

* <code class="value">Barnsley&#39;s Local Plan as adopted by Full Council on 3 January 2019</code>


### Local plan housing number dataset

Create a row containing the housing numbers for each local plan.
For a joint local plan, break the numbers down further by providing a separate row for each Local Planning Authority.


The local plan housing number dataset contains the following fields:



#### reference

Give each set of housing numbers a unique reference value.
 For example:

* <code class="value">34069/County-Durham-Plan</code>
* <code class="value">central-lincolnshire</code>
* <code class="value">barnet-local-plan-2021-2036</code>


#### local-plan

Enter the `reference` for the local plan which these numbers apply.


#### local-planning-authority

This should be the GSS code (statistical geography) for the `local-planning-authority` area to which the housing numbers apply.
See the [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority) dataset.
 For example:

* <code class="value">E60000001</code> — The GSS code for the County Durham LPA area


#### required-housing

Enter the amount of housing required (net additional housing)
within this `local-planning-authority` area for this `local-plan`.
 For example:

* <code class="value">24852</code>


#### committed-housing

Enter the amount of housing already committed for development
by the local plan within this `local-planning-authority` area by the `local-plan`.


#### allocated-housing

Enter the amount of net additional housing which have been allocated to sites 
by the local plan within this `local-planning-authority` area by the `local-plan`.
 For example:

* <code class="value">9239</code>


#### broad-locations-housing

Enter the amount of net additional housing expected to be delivered from broad locations for development 
by the local plan within this `local-planning-authority` area by the `local-plan`.
 For example:

* <code class="value">15660</code>


#### windfall-housing

Enter the amount of housing (net additional housing) expected to be delivered by windfall sites
within this `local-planning-authority` area for this `local-plan`.


#### entry-date

Enter the date this data was created or modified.

#### start-date

Enter the date these numbers were finalised.


#### end-date

Enter the date these numbers were withdrawn, otherwise leave this field blank.


#### notes

You may provide a short description to help users differentiate the plan from others with a similar name. For example:

* <code class="value">Barnsley&#39;s Local Plan as adopted by Full Council on 3 January 2019</code>


### Local plan document dataset

Provide a list of documents associated with your local plan.
Add a separate row with a link to each document on your website.


The Local plan document dataset contains the following fields:



#### reference

Give each document a unique reference.


#### name

Enter the title of the document.


#### description



#### local-plan

Enter the reference for the local plan which the document is associated with.
 For example:

* <code class="value">LP-BRX-2024</code>
* <code class="value">central-lincolnshire</code>


#### document-types

Enter at least one of the following [local-plan-document-type](https://www.planning.data.gov.uk/dataset/local-plan-document-type) values:

* `adoption-statement`
* `area-action-plan`
* `core-strategy`
* `financial-viability-study`
* `inspectors-report`
* `local-development-scheme`
* `local-plan`
* `local-plan-review`
* `policies-map`
* `strategic-flood-risk-assessment`
* `strategic-housing-market-assessment`
* `supplementary-planning-document`
* `sustainability-apprasial`
* `site-allocations`
* `viability-assessment`
* `sustainability-appraisal`

You can list more than one category, separated by a semi-colon &#39;;&#39; character.
 For example:

* <code class="value">local-plan</code>
* <code class="value">local-plan;core-strategy;site-allocations</code>


#### documentation-url

Enter the URL of the webpage on your website which documents and links to this document.
 For example:

* <code class="value">https://calderdale.gov.uk/planning-and-building-control/planning-policy/local-plan</code>


#### document-url

Enter the URL for the document. This is often a PDF file.


#### entry-date

Enter the date this data was created or modified.

#### start-date

Enter the date the document was published.


#### end-date

Enter date when the document was archived. Otherwise leave this field blank.


#### notes

Enter any notes or commentary which helps you or others understand how this data was made, or how it may be interpreted.



## Contact us

$CTA
If you need any help at any stage of the process,
let us know by emailing <digitalland@communities.gov.uk> and a member of our team will be in touch.
$CTA

You can participate in
[improving the design of this data](https://design.planning.data.gov.uk/consideration/local-plans),
and help ensure planning data meets your needs at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 


## Technical specifications