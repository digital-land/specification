---
title: Provide your local plan data
name: local plan
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
- url: https://digital-land.github.io/specification/specification/local-plan/
  name: 'Local plan technical specification (8 November 2025)'
  attachment-type: HTML
  start-date: 
---

^Follow this guidance when providing your local plan data.^

<p>Local planning authorities (LPAs) must create, publish and keep a timetable up to date for a 
local plan, minerals plan, waste plan, or supplementary plan <a href="https://www.gov.uk/government/collections/create-or-update-a-local-plan-using-the-new-system">created or updated using the new local plan system</a>.</p>

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can find it, 
understand its quality, and trust it will be sustained.
[Help design this and other data standards to ensure they your needs](https://design.planning.data.gov.uk). 

## Providing your local plan data

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
so start by providing the best local plans information you have,
and continue to iterate and improve it over time.

### Files





For local plans you may provide the following dataset:


* [Local plan](#Local-plan-dataset)
* [Local plan housing number](#local-plan-housing-number-dataset)
* [Local plan document](#Local-plan-document-dataset)



Each dataset needs to be provided
in a separate CSV file 
following the government 
[tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).


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



## Local plan dataset

List the local plans you are responsible for with one row for each current, emerging or historical local plan.


### Fields



Your Local plan data must contain the following fields:



* `reference`
* `documentation-url`
* `document-url`

It should also contain the following fields:



* `name`
* `dataset`
* `period-start-date`
* `period-end-date`
* `local-planning-authorities`
* `mineral-planning-authorities`
* `waste-planning-authorities`
* `local-plan-process`
* `entry-date`
* `start-date`

It may also contain the following fields:



* `end-date`
* `notes`



### reference

Give each local plan a unique reference.
 For example:

* <code class="value">LP-BRX-2024</code>
* <code class="value">34069/County-Durham-Plan</code>
* <code class="value">central-lincolnshire</code>
* <code class="value">barnet-local-plan-2021-2036</code>


### documentation-url

The URL of the webpage on your website for the local plan

Each entry in the local plan dataset should link to a documentation webpage that includes the information 
in the entry as well as links to where this data may be downloaded, and any other supporting documents.
Where there are several local plans listed on a single webpage, you can use use an anchor link (fragment identifier) 
to make the URL for each plan unique.
 For example:

* <code class="value">https://eastcambs.gov.uk/planning-and-building-control/planning-policy-and-guidance/adopted-local-plan/local-plan</code>
* <code class="value">https://example.com/local-plans/#example-local-plan-2011</code>
* <code class="value">https://example.com/local-plans/#example-local-plan-2024</code>


### document-url

Enter the URL for the main or core plan document. This is usually a PDF file.
 For example:

* <code class="value">https://www.walthamforest.gov.uk/sites/default/files/2024-02/LBWF_LocalPlan_LP1_Feb2024_compressed.pdf</code>


### name

Use the title of the adopted local plan document. For example:

* <code class="value">County Durham Plan</code>
* <code class="value">South Oxfordshire Joint Local Plan</code>


### dataset



### period-start-date

Enter the start of the plan period. This is usually just a year in `YYYY` format. For example:

* <code class="value">2026</code>


### period-end-date

Enter the end of the plan period. This is may be just the year in `YYYY` format. For example:

* <code class="value">2038</code>


### local-planning-authorities

Enter the reference (the GSS code) for the 
[Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)
area covered by this local plan.
For a joint local plan, enter the list of Local Planning Authority references, each separated by semi-colon &#39;;&#39; character.
 For example:

* <code class="value">E60000001</code>
* <code class="value">E60000132;E60000133;E60000135;E60000136</code>


### mineral-planning-authorities

Enter the reference for the
[Mineral Planning Authority](https://www.planning.data.gov.uk/dataset/mineral-planning-authority)
area covered by this minerals plan.
For a joint minerals plan, enter the list of Mineral Planning Authority references, each separated by semi-colon &#39;;&#39; character.
 For example:

* <code class="value">GMCA</code>


### waste-planning-authorities

Enter the reference for the
[Waste Planning Authority](https://www.planning.data.gov.uk/dataset/waste-planning-authority)
area covered by this waste plan.
For a joint waste plan, enter the list of Waste Planning Authority references, each separated by semi-colon &#39;;&#39; character.
 For example:

* <code class="value">NLWA</code>


### local-plan-process

Indicate the local plan examination process for the local plan using one of the following values:

* `2012` for plans prepared under the Town and Country Planning (Local Planning) (England) Regulations 2012, including transitional arrangements
* `2026` for plans prepared under *new Local Planning Regulations (TBD)*


### entry-date

Enter the date this data was created or modified.

### start-date

Enter the date when the plan was officially adopted. 
This value should match the relevant entry for when the plan was recoreded as being adopted in the `local-plan-timetable`.
Leave this value blank for plans which are being prepared, or haven&#39;t yet been adopted.


### end-date

Enter the date the local plan was withdrawn or revoked, otherwise leave this field blank.


### notes

You may provide notes on how this data was made, and help users differentiate the plan from others with a similar name. For example:

* <code class="value">Barnsley&#39;s Local Plan as adopted by Full Council on 3 January 2019</code>
## Local plan housing number dataset

Use this dataset to provide the individual `required-housing` number for each Local Planning Authority within a joint new local plan.
You may also use this dataset to provide additional housing numbers related to a local plan.
There is no need to provide this dataset for other kinds of plan.


### Fields



Your local plan housing number data must contain the following fields:



* `reference`
* `local-plan`

It should also contain the following fields:



* `local-planning-authority`
* `required-housing`
* `committed-housing`
* `allocated-housing`
* `broad-locations-housing`
* `windfall-housing`
* `entry-date`
* `start-date`

It may also contain the following fields:



* `end-date`
* `notes`



### reference

Give each set of housing numbers a unique reference value.
 For example:

* <code class="value">34069/County-Durham-Plan</code>
* <code class="value">central-lincolnshire</code>
* <code class="value">barnet-local-plan-2021-2036</code>


### local-plan

Enter the `reference` for the local plan which these numbers apply.


### local-planning-authority

This should be the GSS code (statistical geography) for the `local-planning-authority` area to which the housing numbers apply.
See the [Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority) dataset.
 For example:

* <code class="value">E60000001</code> — The GSS code for the County Durham LPA area


### required-housing

Enter the minimum number of homes that the plan seeks to provide
within this `local-planning-authority` area.
 For example:

* <code class="value">24852</code>


### committed-housing

Enter the amount of housing already committed for development
within this `local-planning-authority` area.


### allocated-housing

Enter the total number of homes planned for through local plan housing site allocations
including housing components of mixed-use site allocations
within this `local-planning-authority` area.
 For example:

* <code class="value">9239</code>


### broad-locations-housing

Enter the total number of homes expected towards the end of the local plan period and attributed to
‘broad locations for growth’, as opposed to site allocations
within this `local-planning-authority` area.
 For example:

* <code class="value">15660</code>


### windfall-housing

Enter the total number of homes expected to arise from housing sites not specifically identified in the local plan
within this `local-planning-authority` area.
 For example:

* <code class="value">160</code>


### entry-date

Enter the date this data was created or modified.

### start-date

Enter the date these numbers were finalised.


### end-date

Enter the date these numbers were withdrawn, otherwise leave this field blank.


### notes

You may provide a short description to help users differentiate the plan from others with a similar name. For example:

* <code class="value">Barnsley&#39;s Local Plan as adopted by Full Council on 3 January 2019</code>
## Local plan document dataset

Provide a list of documents associated with your local plan.
Add a separate row with a link to each document on your website.


### Fields



Your Local plan document data must contain the following fields:



* `reference`
* `name`
* `local-plan`
* `document-url`

It should also contain the following fields:



* `document-types`
* `documentation-url`
* `entry-date`
* `start-date`

It may also contain the following fields:



* `description`
* `end-date`
* `notes`



### reference

Give each document a unique reference.


### name

Enter the title of the document.


### local-plan

Enter the reference for the local plan which the document is associated with.
 For example:

* <code class="value">LP-BRX-2024</code>
* <code class="value">central-lincolnshire</code>


### document-url

Enter the URL for the document. This is often a PDF file.


### document-types

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


### documentation-url

Enter the URL of the webpage on your website which documents and links to this document.
 For example:

* <code class="value">https://calderdale.gov.uk/planning-and-building-control/planning-policy/local-plan</code>


### entry-date

Enter the date this data was created or modified.

### start-date

Enter the date the document was published.


### description



### end-date

Enter date when the document was archived. Otherwise leave this field blank.


### notes

Enter any notes or commentary which helps you or others understand how this data was made, or how it may be interpreted.

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
Continue to improve your data, and act on the feedback from the [the service](https://provide.planning.data.gov.uk) 
to ensure your data meets the specification.

You also need to update and republish your data whenever there's a change to your local plans information.

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
[improving the design of this data](https://design.planning.data.gov.uk/consideration/local-plans),
and help ensure planning data meets your needs at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 

## Technical specifications