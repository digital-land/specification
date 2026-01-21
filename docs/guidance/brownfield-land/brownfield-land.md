---
title: Provide your Brownfield land data
name: Brownfield land
url: https://www.gov.uk/government/publications/brownfield-land-registers-data-standard/publish-your-brownfield-land-data
summary: 
entry-date: 2022-06-09
updated: 9 June 2022
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
attachments:
- url: https://www.gov.uk/government/publications/brownfield-land-registers-data-standard/publish-your-brownfield-land-data
  name: 'Brownfield land technical specification (9 June 2022)'
  attachment-type: HTML
  start-date: 
---

^Follow this guidance when providing your Brownfield land data.^

<p><a href="http://www.legislation.gov.uk/uksi/2017/403/contents/made">The Town and Country Planning (Brownfield Land Register) Regulations 2017</a>
require local planning authorities to maintain a register of their brownfield sites that are suitable for housing.</p>

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can find it, 
understand its quality, and trust it will be sustained.
[Help design this and other data standards to ensure they your needs](https://design.planning.data.gov.uk). 

## Providing your Brownfield land data

Take the following steps to provide your Brownfield land data:

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
so start by providing the best Brownfield land information you have,
and continue to iterate and improve it over time.

### Files


For Brownfield land you need to provide 1 dataset:

* [Brownfield land](#Brownfieldland-dataset)





The dataset needs to be provided
in a  CSV file 
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



## Brownfield land dataset



The Brownfield land dataset contains the following fields:



### OrganisationURI

[Find your organisation in this list](https://www.planning.data.gov.uk/organisation)
and enter the corresponding `Open Data Communities URI` value.


### SiteReference

Enter the unique reference your organisation uses to identify the site.

If one doesn’t exist, you need to create one. It should not be used by your organisation
to identify any other sites, but can be borrowed from another data set listing
the site. You could use the strategic site identifier from your local plan.
 For example:

* <code class="value">EH/141</code>


### SiteNameAddress

Enter the site name and address in a single line of text, for example:
 For example:

* <code class="value">Parcel of land behind, 221B Baker Street, Marylebone, London, NW1 6XE</code>


### GeoX

Enter the longitude of a point close to the centre of the site. The value
should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate systems
specified by the [open standards for government guidance](https://www.gov.uk/government/publications/open-standards-for-government/exchange-of-location-point).

$CTA
Be sure you do not mix up the latitude (Geo Y) and longitude (Geo X) values.
Any location in the UK will have a latitude (Geo Y) from about 49 to 57 and a
longitude (Geo X) from about -7 to 2.
$CTA


### GeoY

Enter the latitude of a point close to the centre of the site. The value
should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate systems
specified by the [open standards for government guidance](https://www.gov.uk/government/publications/open-standards-for-government/exchange-of-location-point).


### SiteplanURL

Enter the URL of a web page hosting the site plan, beginning with either “http://” or “https://”.

### Hectares

Enter the land area of the site in hectares, up to 2 decimal places.
Use digits (2) rather than words (two).


### OwnershipStatus

Indicate the site’s ownership by entering one of the following values:

* `owned by a public authority`
* `not owned by a public authority`
* `mixed ownership`

For more information see paragraph 5 of [Schedule 2 of the 2017 Regulations](http://www.legislation.gov.uk/uksi/2017/403/schedule/2/made).


### PlanningStatus

Choose one of the following to indicate what stage of the planning process the site is at:

* `permissioned`
* `not permissioned`
* `pending decision`

When part of a site is permissioned, it should be recorded as `permissioned` and
you should explain in the `Notes` field why it’s only partly permissioned.

For more information see paragraph 5 of [Schedule 2 of the 2017 Regulations](http://www.legislation.gov.uk/uksi/2017/403/schedule/2/made).&#39;


### PermissionType

Choose one of the following to indicate what permission type the site has:

* `full planning permission`
* `outline planning permission`
* `reserved matters approval`
* `permission in principle`
* `technical details consent`
* `planning permission granted under an order`
* `other`

The value `planning permission granted under an order` means planning permission granted
under a local development order, a mayoral development order or a neighbourhood
development order.

Where more than one permission exists for the site, identify the latest permission
granted. List any other permissions, including the date that each permission was
granted or deemed to have been granted, in the ’Notes’ column.&#39;


### PermissionDate

Enter the date the most recent permission was granted on the site, in
the format `YYYY-MM-DD`. If no permission has been granted leave this blank.


### PlanningHistory

Enter links to any web pages that give information on the site’s planning history (include the “http://” or “https://” prefix). Fields in this column can contain more than one link, as long as you separate multiple links with the pipe character (‘|’). You can leave this field blank.

### Deliverable

Enter ‘yes’ if there is a reasonable prospect that residential development
will take place on the land within 5 years of the date you enter this site in
the register. Otherwise leave this field blank.


### NetDwellingsRangeFrom

Enter the minimum number of dwellings that the local planning authority
estimates the site should support, as defined in 
[regulation 2 of the 2017 Regulations](http://www.legislation.gov.uk/uksi/2017/403/regulation/2/made).


### NetDwellingsRangeTo

Enter the maximum number of dwellings that the local planning authority
estimates the site should support, as defined in 
[regulation 2 of the 2017 Regulations](http://www.legislation.gov.uk/uksi/2017/403/regulation/2/made).


### HazardousSubstances

Enter ‘yes’ if the local planning authority is required by regulation
26(3) of the [Planning (Hazardous Substances) Regulations 2015](https://www.legislation.gov.uk/uksi/2015/627/regulation/26/made)
to conduct an environmental impact assessment on the proposed development. Otherwise leave this blank.


### Notes

Enter any general information about a site that developers might find
useful, including a description of any housing development proposed for the site.

You may include links to any web pages that give:

* information on planning decisions related to any environmental impact assessments
* the results of any related consultations
* an explanation of how they were taken into account when making the decisions

You may also describe any non-housing development proposed for the site. Indicate
how the buildings or land will be used, and the scale of any such development.

Content in this field does not need to be on a single line, but should be no longer
than 4,000 characters. You can leave this field blank.


### FirstAddedDate

Enter the date that the site was first added to this register, in the format `YYYY-MM-DD`.

### LastUpdatedDate

Enter the date this entry in the register was updated, in the format YYYY-MM-DD.

### EndDate

If the site no longer needs to be listed (for example, if the site has
been built on), it should remain on the register for historical reasons and not
be deleted. Enter the date the site was developed or determined to no longer be
brownfield land, in the format `YYYY-MM-DD`. This field should only be filled in
once the site is no longer classified as brownfield land.




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

You also need to update and republish your data whenever there's a change to your Brownfield land information.

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
[improving the design of this data](https://design.planning.data.gov.uk/consideration/brownfield-land),
and help ensure planning data meets your needs at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 

## Technical specifications