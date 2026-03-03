---
title: Provide your development plan data
name: development plan
url: 
summary: 
entry-date: 2026-01-23
updated: 23 January 2026
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
attachments:
- url: https://digital-land.github.io/specification/specification/development-plan/
  name: 'Development plan technical specification (23 January 2026)'
  attachment-type: HTML
  start-date: 
---

^Follow this guidance when providing your development plan data.^

<p>Local planning authorities (LPAs) must create, publish and keep a plan timetable up to date.
This guidance applies to the following plans that you created or updated using the 
<a href="https://www.gov.uk/government/collections/create-or-update-a-local-plan-using-the-new-system">new plan-making system</a>:</p>
<ul>
<li>local plans</li>
<li>minerals and waste plans</li>
<li>supplementary plans</li>
</ul>
<p>All authorities must comply with the approved data standards set out in this guidance.</p>

Providing planning data means making it available publicly to a standard so that anyone using
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can:

* find it
* understand its meaning and purpose
* assess its quality
* trust it will be maintained

[You can help to design this and other data standards to ensure they your needs](https://design.planning.data.gov.uk). 

## Providing your development plan data

Take the following steps to provide your development plan data:

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

We treat the data you provide as being more authoritative than data 
we have previously collected from you previously or found that we find elsewhere.

You can download tabular data we have for your organisation as a CSV file
from the [check and provide service](https://provide.planning.data.gov.uk)
then edit it using a spreadsheet or other CSV editors.

You can download geospatial data we have for your organisation as
CSV or GeoJSON from [planning.data.gov.uk](https://planning.data.gov.uk)
then modify it using QGIS or other GIS tools.

You must provide data for the mandatory fields identified.

### Datasets


For development plans you need to provide 2 datasets:

* [Development plan](#developmentplan-dataset)
* [Development plan timetable](#developmentplantimetable-dataset)





You need to provide each dataset 
in a separate CSV file 
and follow the government 
[tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).


Follow this guidance to find out more about the fields and format of the data you need to prepare.

### Field names

You can use a field name with uppercase, lowercase and any punctuation characters. 
For example, you can use any of the following names for the `start-date` field in your data

* `StartDate`
* `Start Date`
* `START_DATE`
* `start.date`

### Reference values

Each dataset has a `reference` field.
Reference values are important to help people find and link to your data.
If you do not have a reference value for an item, you will need to create one that: 

* is unique within your data 
* does not change when the data is updated 

A good reference is something you already use.
If your reference is not unique, you can make them unique by adding the year or full date.
Great references are:  

* short  
* easy to read  
* easy to pronounce and remember

### Date values

All dates must be in the format `YYYY-MM-DD` as set out in[formatting dates and times in data](https://www.gov.uk/government/publications/open-standards-for-government/date-times-and-time-stamps-standard).






## Development plan dataset





### Mandatory fields

Your development plan data must contain the following fields:



* `reference`
* `name`
* `dataset`
* `period-start-date`
* `period-end-date`
* `documentation-url`
* `document-url`
* `required-housing`



### reference

Give each local plan a unique reference.
 For example:

* <code class="value">LP-BRX-2024</code>
* <code class="value">34069/County-Durham-Plan</code>
* <code class="value">central-lincolnshire</code>
* <code class="value">barnet-local-plan-2021-2036</code>


### name

Use the title of the local plan document. For example:

* <code class="value">County Durham Plan</code>
* <code class="value">South Oxfordshire Joint Local Plan</code>


### dataset

Enter one of the following values to show the type of development plan:

* `local-plan`
* `supplementary-plan`
* `minerals-plan`
* `waste-plan`


### period-start-date

Enter the start of the plan period. This is usually just a year in `YYYY` format. For example:

* <code class="value">2026</code>
* <code class="value">2027</code>


### period-end-date

Enter the end of the plan period. This is usually just a year in `YYYY` format. For example:

* <code class="value">2038</code>
* <code class="value">2040</code>


### documentation-url

The URL of the webpage on your website for the local plan

Each entry in the local plan dataset should link to a documentation webpage that includes:

* the information in the entry
* links to where you can download the data
* and any other supporting documents.

If there are several local plans listed on a single webpage, you can use an anchor link (fragment identifier) 
to make the URL for each plan unique.
 For example:

* <code class="value">https://eastcambs.gov.uk/planning-and-building-control/planning-policy-and-guidance/adopted-local-plan/local-plan</code>
* <code class="value">https://example.com/local-plans/#example-local-plan-2011</code>
* <code class="value">https://example.com/local-plans/#example-local-plan-2024</code>


### document-url

Enter the URL for the main or core plan document, which is usually a PDF file.
 For example:

* <code class="value">https://www.walthamforest.gov.uk/sites/default/files/2024-02/LBWF_LocalPlan_LP1_Feb2024_compressed.pdf</code>


### required-housing

Enter the minimum number of homes that the plan seeks to provide
during the plan period.
 For example:

* <code class="value">1024</code>
* <code class="value">24852</code>


### Recommended fields

Your development plan data should also contain the following fields if they apply:



* `local-planning-authorities`
* `mineral-planning-authorities`
* `waste-planning-authorities`
* `entry-date`



### local-planning-authorities

Enter the GSS code reference (the GSS code) for the 
[Local Planning Authority](https://www.planning.data.gov.uk/dataset/local-planning-authority)
area that this local or supplementary plan covers.
For a joint local plan, enter the list of Local Planning Authority references, and separate each separated of them by with a semi-colon &#39;;&#39; character. For example:
 For example:

* <code class="value">E60000001</code>
* <code class="value">E60000132;E60000133;E60000135;E60000136</code>


### mineral-planning-authorities

Enter the reference for the
[Mineral Planning Authority](https://www.planning.data.gov.uk/dataset/mineral-planning-authority)
area covered by this minerals plan.
For a joint minerals plan, enter the list of Mineral Planning Authority references and separate each of them with a semi-colon.
 For example:

* <code class="value">GMCA</code>
* <code class="value">NLWA;GMCA</code>


### waste-planning-authorities

Enter the reference for the
[Waste Planning Authority](https://www.planning.data.gov.uk/dataset/waste-planning-authority)
area covered by this waste plan.
For a joint waste plan, enter the list of Waste Planning Authority references and separate each of them with a semi-colon.
 For example:

* <code class="value">NLWA</code>
* <code class="value">NLWA;GMCA</code>


### entry-date

Enter the date this data was created or modified.

### Optional fields

Your development plan data may also contain the following fields:



* `notes`



### notes

You may provide notes on how this data was made, and help users differentiate the plan from others with a similar name. For example:

* <code class="value">Barnsley&#39;s Local Plan as adopted by Full Council on 3 January 2019</code>


## Development plan timetable dataset


Record the milestones and other events in the timetable when producing your development plan.
Your timetable must include a precise `committed-date` against each entry.
Update the entry to include the actual date in the `start-date` field when the event takes place.

For local plans, minerals plans, and waste plans 
your timetable must include an entry with one of the following `development-plan-event` field values where applicable:

* `publish-notice-intention-commence`
* `scoping-consultation-start`
* `scoping-consultation-end`
* `gateway-1-self-assessment`
* `plan-content-evidence-consultation-start`
* `plan-content-evidence-consultation-end`
* `gateway-2-advice-sought`
* `gateway-2-advice-published`
* `proposed-plan-consultation-start`
* `proposed-plan-consultation-end`
* `gateway-3-advice-sought`
* `gateway-3-advice-published`
* `gateway-3-further-advice-sought`
* `gateway-3-repeat-advice-published`
* `examination-submitted`
* `examination-recommendations-published`
* `adopted`

For supplementary plans 
your timetable must include an entry with one of the following `development-plan-event` field values where applicable:

* `publish-notice-intention-commence`
* `proposed-plan-consultation-start`
* `proposed-plan-consultation-end`
* `examination-submitted`
* `adopted`

For any plan 
your timetable may include an entry with one of the following `development-plan-event` field values where applicable:

* `main-modification-consultation-start`
* `main-modification-consultation-end`
* `examination-pause-start`
* `examination-pause-end`
* `additional-consultation-start`
* `additional-consultation-end`
* `withdrawn`
* `revoked`





### Mandatory fields

Your development plan timetable data must contain the following fields:



* `reference`
* `development-plan`
* `development-plan-event`
* `committed-date`
* `start-date`



### reference

Give each event a reference which is unique for the event within the dataset.
Where a timetable has more than one event of the same type, you can add a date to make them unique.
 For example:

* <code class="value">LP1-public-consultation</code>
* <code class="value">LP1-public-consultation-2025</code>


### development-plan

Enter the reference of the development plan which this event forms part of its timetable.
 For example:

* <code class="value">LP-BRX-2024</code>
* <code class="value">central-lincolnshire</code>


### development-plan-event

Enter a [Development Plan Event](https://www.planning.data.gov.uk/dataset/development-plan-event) reference.
 For example:

* <code class="value">publish-notice-intention-commence</code>
* <code class="value">examination-submitted</code>
* <code class="value">adopted</code>


### committed-date

Enter the date by which this event will happen.


### start-date

Enter the date when the timetable event occured. Leave this field blank when the event has yet to happen.


### Recommended fields

Your development plan timetable data should also contain the following fields if they apply:



* `entry-date`



### entry-date

Enter the date this data was created or modified.

### Optional fields

Your development plan timetable data may also contain the following fields:



* `notes`



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
Continue to improve your data, and act on the feedback from [the service](https://provide.planning.data.gov.uk) 
to ensure your data meets the specification.

You also need to update and republish your data whenever there's a change to your development plans information.

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
[improving the design of this data](https://design.planning.data.gov.uk/consideration/development-plans-and-timetables),
and help ensure planning data meets your needs at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 

## Technical specifications