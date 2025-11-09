
---
title: Provide your Article 4 direction data
name: Article 4 direction
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
- url: 
  name: 'Article 4 direction technical specification (2025-11-08)'
  attachment-type: HTML
  start-date: 
---

^Follow this guidance when providing your Article 4 direction data.^

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can find it, 
understand its quality, and trust it will be sustained.

<p>Local Planning Authorities and other organisations 
<a href="https://www.localdigital.gov.uk/digital-planning/funding/">funded by the Digital Planning Programme</a>
to join the <a href="https://opendigitalplanning.org/digital-planning-improvement">Open Digital Planning community</a>
are expected to provide data to this specification.</p>
<p>If you're a Local Planning Authority who is interested in becoming a member,
you can <a href="https://opendigitalplanning.org/join">join the community</a>.</p>
<p>Otherwise there is no obligation on any party to provide data to this specification.</p>
<p>A future version of this specification may be formally published on GOV.UK,
and cited as one of a number of official data standards for the provision of planning data 
by planning authorities under the 
<a href="https://www.legislation.gov.uk/ukpga/2023/55/part/3/chapter/1/enacted">Levelling-up and Regeneration Act 2023</a>.</p>

## Providing Article 4 direction data

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

The [fields and format](#data-fields-and-formats) of the data are documented below,
and formally defined in [Technical Specifications] attached to this page.

Your data does not need to be complete or perfect to start with.
For many purposes having some data is better than no data,
so start with the information you have, and continue to iterate and improve it over time.

## Check your data
Use the [check and provide service](https://provide.planning.data.gov.uk) to review your data before you publish it. 
The service will show you how the data will appear on [planning.data.gov.uk](https://planning.data.gov.uk) 
along with feedback on how you might improve your data.

## Publish your data
Publishing your data consists of two parts:

* An [endpoint](#endpoint) from where the data can be downloaded
* A [source](#source) where the information contained in the data is presented on your website

### Endpoint

The endpoint is a URL where a user can download the data.
Publish your data at a public endpoint, in a way which anyone can download and use it.

The endpoint is usually a single file hosted on your website.
Alternatively, you can provide your data using a WFS or other API,
or using a third-party service such as GitHub or ArcGIS which allows the data to be downloaded.

Ensure your endpoint is documented on a public webpage to help people find and use the data.

The documentation webpage for your endpoint should include a clear statement that the data is provided as open data under
the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

### Source

The source page is a URL where a user can see the same information in the data.
This is usually existing planning policy, or other webpages on your official website.

It is important that the source page links to the endpoint documentation webpage to 
help users trust the authenticity of the data.

## Tell us about your data
Once you have published the data, tell us about it so we can index and quickly make it available 
nationally on [planning.data.gov.uk](https://planning.data.gov.uk).

Use the [check and provide service](https://provide.planning.data.gov.uk/) to tell us where it is. 

You will need to provide for each dataset:

* the source URL where the information in the data is presented on your website
* the endpoint URL from which the data can be collected

The provide service also asks for your name and email address as a point of contact in case of any issues.

## Keep your data up-to-date
You should continue to improve your data, and act on the feedback from the [check and provide service](https://provide.planning.data.gov.uk) 
to ensure your data meets the specification.

You will also need to update and republish your data whenever there's a change to your article 4 directions information.

We look for changes to the data at all of the endpoint URLs we know about every night,
so we can quickly update [planning.data.gov.uk](https://planning.data.gov.uk).

It is simpler if you publish your changes to the same endpoint URL.
If you create a new endpoint you will need to [tell us where it is](#tell-us-about-your data) again.

## Data files, fields and formats

$CTA
If you need any help at any stage of the process, let us know by emailing <digitalland@communities.gov.uk> and a member of our team will be in touch.
$CTA