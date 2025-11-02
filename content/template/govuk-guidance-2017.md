---
reference: govuk-guidance-2017
name: Publish your brownfield land data 2017
description: govspeak for a GOV.UK page structured in the same way as "Publish your Brownfield Land" page in 2017
notes: This template was originally designed to publish a single dataset
phase: live
entry-date: 2025-11-01
start-date: 2017-
end-date:
---

---
govuk-url: {{ guidance['govuk-url'] | yaml }}
name: {{ guidance['name'] | yaml }}
updated: {{ guidance['updated'] | yaml }}
summary: {{ guidance['summary'] | yaml }}
attachments: {{ guidance['attachment'] | yaml }}
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
---

{{ guidance['duty'] }}
This guidance helps ensure {{ guidance['data-plural'] }}  are:

* published in agreed format with required data
* kept up to date
* easily found online

$CTA
Email feedback to <DigitalLand@communities.gov.uk>
$CTA

### Make your data findable, usable and trustworthy

{{ guidance['data-pural'] | capitalise }} support:

* planning for housing-led development
* creating new digital services
* giving community members insight into local development

Data must be easy to find, use, understand and trust. Local planning authorities should review registers at least annually, but update them immediately when sites are identified or change status.

When adding a new {{ guidance['entry-name'] }}, append a row to your CSV file.
If a site no longer qualifies, do not delete it—fill in the "{{ gudiance["end-date-field"] }}" field instead.

### Publishing is a 3 step process

s1. Create a brownfield land CSV file
s2. Upload the file to your organisation's website with a persistent URL, linked clearly from your brownfield land web page
s3. Update the national brownfield land register on the Ministry website

Each step identifies required skills and authority.

## Step 1: Create your CSV file

You can create or amend CSV files using spreadsheet software (Microsoft Excel, Google Sheets, Apple Numbers).
Name your file "{{ guidance["csv"] }}.csv".

A [{{ guidance["data-name'] }} CSV template](https://digital-land.github.io/guidance/brownfield-sites/brownfield-sites.csv) is available.

{% if guidance['deprecated'] %}
The previous specification contained optional fields.

The 'MinNetDwellings' field has been replaced by 'NetDwellingsRangeFrom' and 'NetDwellingsRangeTo'.

These columns no longer exist (add their content to 'Notes'):
{% for fieldname in guidance['deprecated']['fields'] %}
* {{ fieldname }}
{% endif %}

### Field definitions and formatting

Your CSV file must include:

* a header row (first row, case sensitive, no spacing)
* 1 row per {{ guidance['entry-name'] }}

{% for specification in guidance['specifications'] -%}
    {%- for dataset in specifications['specification']['datasets'] -%}
    {%- for dataset in specifications['specification']['datasets'] -%}
#### 
    {%- endfor -%}
{%- endfor -%}

#### OrganisationURI

[Find your organisation in this list](https://www.planning.data.gov.uk/organisation/) and enter the corresponding Open Data Communities URI.

#### SiteReference

Enter your organisation's unique reference for the site. If one doesn't exist, create one. It should be unique to this site only. You could use a strategic site identifier from your local plan (e.g., EH/141).

#### SiteNameAddress

Enter site name and address as a single line (e.g., "Parcel of land behind, 221B Baker Street, Marylebone, London, NW1 6XE").

#### GeoY

Enter the latitude of a point near the site centre. Use 6 or fewer decimal places, with WGS84 or ETRS89 coordinate systems per open standards for government guidance.

#### GeoX

Enter the longitude of a point near the site centre. Use 6 or fewer decimal places, with WGS84 or ETRS89 coordinate systems.

**Note:** Do not confuse latitude (GeoY) and longitude (GeoX). UK locations have latitude around 49-57 and longitude around -7 to 2.

#### SiteplanURL

(Optional) Enter a URL hosting the site plan, beginning with "http://" or "https://".

#### Hectares

(Optional) Enter land area in hectares, up to 2 decimal places (use digits).

#### OwnershipStatus

(Optional) Enter one of:

* owned by a public authority
* not owned by a public authority
* mixed ownership
* unknown ownership

See paragraph 5 of Schedule 2 of the 2017 Regulations for more information.

#### PlanningStatus

(Optional) Choose one:

* permissioned
* not permissioned
* pending decision

For partially permissioned sites, mark as "permissioned" and explain in Notes. See paragraph 5 of Schedule 2 of the 2017 Regulations.

#### PermissionType

(Optional) Choose one:

* full planning permission
* outline planning permission
* reserved matters approval
* permission in principle
* technical details consent
* planning permission granted under an order
* other

'Planning permission granted under an order' means permission under a local development order, mayoral development order, or neighbourhood development order.

For multiple permissions, identify the latest. List others with dates in Notes.

#### PermissionDate

(Optional) Enter the most recent permission date as YYYY-MM-DD. Leave blank if no permission granted.

#### PlanningHistory

(Optional) Enter links to planning history pages. Separate multiple links with the pipe character (|).

#### Deliverable

(Optional) Enter 'yes' if residential development is likely within 5 years of register entry.

#### NetDwellingsRangeFrom

Enter the minimum estimated dwellings, per regulation 2 of the 2017 Regulations.

#### NetDwellingsRangeTo

Enter the maximum estimated dwellings, per regulation 2 of the 2017 Regulations.

#### HazardousSubstances

(Optional) Enter 'yes' if required by regulation 26(3) of the Planning (Hazardous Substances) Regulations 2015 to conduct environmental impact assessment.

#### Notes

(Optional) Enter general site information useful to developers, including housing development descriptions.

You may include links to pages showing:

* planning decisions related to environmental impact assessments
* consultation results
* how they influenced decisions

You may describe non-housing development, including use type and scale. Maximum 4,000 characters.

#### FirstAddedDate

Enter the register entry date as YYYY-MM-DD.

#### LastUpdatedDate

Enter the update date as YYYY-MM-DD.

#### EndDate

(Optional) If the site no longer qualifies (e.g., built on), keep the entry but fill in the end date as YYYY-MM-DD. Only populate once the site is no longer brownfield land.

### Check and provide your data

Use the online tool to check and provide your brownfield site data.

## Step 2: Update your {{ guidance["data-name"] }} web page

You must be able to edit (or create) your local planning authority's brownfield land web page. Consult someone with authority if needed.

Upload your CSV file to your local planning authority website with a persistent URL (unchanging web address). Example: https://www.norfolk.gov.uk/brownfield-land.csv

Update your brownfield land web page to publicly display the CSV file. List the persistent URL in full. If the URL changes, notify us.

### Licensing

State that data is provided under the Open Government Licence.

Before publishing, check whether you need to inform the Ordnance Survey that you are publishing this data.

## Step 3: Update the national brownfield land register

The Ministry of Housing, Communities and Local Government maintains a national brownfield land register using your published data.

When you first create and publish your CSV file, tell us its persistent URL. Notify us if it ever changes.

$CTA
Email the persistent URL to <DigitalLand@communities.gov.uk> and we will add it to the national register.
$CTA

We recommend adding the URL to data.gov.uk.

For questions or feedback, email <DigitalLand@communities.gov.uk>
