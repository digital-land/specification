---
title: Provide your Planning condition data
name: Planning condition
url: 
summary: 
entry-date: 2023-11-09
updated: 9 November 2023
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
attachments:
- url: /specification/specification/planning-condition
  name: 'Planning condition technical specification (9 November 2023)'
  attachment-type: HTML
  start-date: 
---

^Follow this guidance when providing your Planning condition data.^

<p>There are currently no obligations on any party to provide data in conformance to this specification. 
A future version of this specification may be published on GOV.UK,
and cited as one of a number of official data standards for the provision of planning data under the 
<a href="https://www.legislation.gov.uk/ukpga/2023/55/part/3/chapter/1/enacted">Levelling-up and Regeneration Act 2023</a>,
other regulations, contracts, and agreements.</p>

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can find it, 
understand its quality, and trust it will be sustained.

## Providing Planning condition data

Take the following steps to provide your Planning condition data:

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

We will take the most recent data you provide as being more authoritative
than any data we have collected from you previously, or found in other sources.

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
so start by providing the best Planning conditions information you have,
and continue to iterate and improve it over time.


### Files





For Planning conditions you may provide the following dataset:


* [Planning condition](#Planningcondition-dataset)
* [Planning application condition](#Planningapplicationcondition-dataset)



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



### Planning condition dataset



The Planning condition dataset contains the following fields:



#### reference

Enter reference to help people find and link to the data.
If you don’t have a reference for this item, you will need to create one that is:

* unique within your data
* persistent — it doesn’t change when the data is updated

A good reference is something you already use.
Where these aren&#39;t unique, you make them unique by appending the year, or even the full date.
Great references are short, easy to read, to pronounce and remember.

#### name



#### description



#### reason



#### organisation

Enter a CURIE value for the organisation from [this list](https://www.planning.data.gov.uk/organisation/).

#### notes

Enter any notes or commentary which helps you or others understand how this data was made, or how it may be interpreted.

#### entry-date

Enter the date this data was created or modified.

#### start-date



#### end-date



### Planning application condition dataset



The Planning application condition dataset contains the following fields:



#### reference

Enter reference to help people find and link to the data.
If you don’t have a reference for this item, you will need to create one that is:

* unique within your data
* persistent — it doesn’t change when the data is updated

A good reference is something you already use.
Where these aren&#39;t unique, you make them unique by appending the year, or even the full date.
Great references are short, easy to read, to pronounce and remember.

#### planning-application



#### planning-condition



#### document-url



#### documentation-url



#### description



#### organisation

Enter a CURIE value for the organisation from [this list](https://www.planning.data.gov.uk/organisation/).

#### notes

Enter any notes or commentary which helps you or others understand how this data was made, or how it may be interpreted.

#### entry-date

Enter the date this data was created or modified.

#### start-date



#### end-date





## Check your data
Use the [check and provide service](https://provide.planning.data.gov.uk) to review your data before you publish it. 
The service will show you how the data will appear on [planning.data.gov.uk](https://planning.data.gov.uk) 
along with feedback on how you might improve your data.

## Publish your data
Publishing your data consists of two parts:

* An **endpoint** where the data can be downloaded from
* A **source webpage** where the information contained in the data is presented on your website

### Endpoint

Publish your data at a public endpoint, in a way in which anyone can download and use it.

The endpoint is a URL from which the data can be downloaded.
This can be a single file hosted on your website.
Or, you can serve your data using an OGC WFS or other API
using a third-party service such as GitHub or ArcGIS.

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

You also need to update and republish your data whenever there's a change to your Planning conditions information.

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
[improving the design of this data](https://design.planning.data.gov.uk/consideration/planning-conditions),
and help ensure planning data meets your needs at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 


## Technical specifications