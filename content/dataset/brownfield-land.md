---
attribution: crown-copyright
collection: brownfield-land
consideration: brownfield-land
dataset: brownfield-land
description: Land that has been previously been developed
end-date: ''
entity-maximum: '1799999'
entity-minimum: '1700000'
entry-date: ''
fields:
- field: Deliverable
  guidance: Enter ‘yes’ if there is a reasonable prospect that residential development
    will take place on the land within 5 years of the date you enter this site in
    the register. Otherwise leave this field blank.
- field: EndDate
  guidance: If the site no longer needs to be listed (for example, if the site has
    been built on), it should remain on the register for historical reasons and not
    be deleted. Enter the date the site was developed or determined to no longer be
    brownfield land, in the format YYYY-MM-DD. This field should only be filled in
    once the site is no longer classified as brownfield land.
- field: FirstAddedDate
  guidance: Enter the date that the site was first added to this register, in the
    format YYYY-MM-DD.
- field: GeoX
  guidance: Enter the longitude of a point close to the centre of the site. The value
    should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate systems
    specified by the [open standards for government guidance](https://www.gov.uk/government/publications/open-standards-for-government/exchange-of-location-point).
    $CTA Be sure you do not mix up the latitude (Geo Y) and longitude (Geo X) values.
    Any location in the UK will have a latitude (Geo Y) from about 49 to 57 and a
    longitude (Geo X) from about -7 to 2. $CTA
- field: GeoY
  guidance: Enter the latitude of a point close to the centre of the site. The value
    should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate systems
    specified by the [open standards for government guidance](https://www.gov.uk/government/publications/open-standards-for-government/exchange-of-location-point).
- field: HazardousSubstances
  guidance: Enter ‘yes’ if the local planning authority is required by regulation
    26(3) of the [Planning (Hazardous Substances) Regulations 2015](https://www.legislation.gov.uk/uksi/2015/627/regulation/26/made)
    to conduct an environmental impact assessment on the proposed development. Otherwise
    leave this blank.
- field: Hectares
  guidance: Enter the land area of the site in hectares, up to 2 decimal places. Use
    digits (2) rather than words (two).
- field: LastUpdatedDate
  guidance: Enter the date this entry in the register was updated, in the format YYYY-MM-DD.
- field: MinNetDwellings
- field: NetDwellingsRangeFrom
  guidance: Enter the minimum number of dwellings that the local planning authority
    estimates the site should support, as defined in [regulation 2 of the 2017 Regulations](http://www.legislation.gov.uk/uksi/2017/403/regulation/2/made).
- field: NetDwellingsRangeTo
  guidance: Enter the maximum number of dwellings that the local planning authority
    estimates the site should support, as defined in [regulation 2 of the 2017 Regulations](http://www.legislation.gov.uk/uksi/2017/403/regulation/2/made).
- field: Notes
  guidance: 'Enter any general information about a site that developers might find
    useful, including a description of any housing development proposed for the site.

    You may include links to any web pages that give:

    * information on planning decisions related to any environmental impact assessments
    * the results of any related consultations * an explanation of how they were taken
    into account when making the decisions

    You may also describe any non-housing development proposed for the site. Indicate
    how the buildings or land will be used, and the scale of any such development.

    Content in this field does not need to be on a single line, but should be no longer
    than 4,000 characters. You can leave this field blank.'
- field: OrganisationLabel
- field: OrganisationURI
  guidance: '[Find your organisation in this list](https://www.digital-land.info/entity?typology=organisation)
    and enter the corresponding Open Data Communities URI.'
- field: OwnershipStatus
  guidance: 'Indicate the site’s ownership by entering one of the following values:

    * owned by a public authority * not owned by a public authority * mixed ownership

    For more information see paragraph 5 of [Schedule 2 of the 2017 Regulations](http://www.legislation.gov.uk/uksi/2017/403/schedule/2/made).'
- field: PermissionDate
  guidance: Enter the date the most recent permission was granted on the site, in
    the format YYYY-MM-DD. If no permission has been granted leave this blank.
- field: PermissionType
  guidance: 'Choose one of the following to indicate what permission type the site
    has:

    * full planning permission * outline planning permission * reserved matters approval
    * permission in principle * technical details consent * planning permission granted
    under an order * other

    ‘Planning permission granted under an order’ means planning permission granted
    under a local development order, a mayoral development order or a neighbourhood
    development order.

    Where more than one permission exists for the site, identify the latest permission
    granted. List any other permissions, including the date that each permission was
    granted or deemed to have been granted, in the ’Notes’ column.'
- field: PlanningHistory
  guidance: Enter links to any web pages that give information on the site’s planning
    history (include the “http://” or “https://” prefix). Fields in this column can
    contain more than one link, as long as you separate multiple links with the pipe
    character (‘|’). You can leave this field blank.
- field: PlanningStatus
  guidance: 'Choose one of the following to indicate what stage of the planning process
    the site is at:

    * permissioned * not permissioned * pending decision

    When part of a site is permissioned, it should be recorded as “permissioned” and
    you should explain in the ‘Notes’ field why it’s only partly permissioned.

    For more information see paragraph 5 of [Schedule 2 of the 2017 Regulations](http://www.legislation.gov.uk/uksi/2017/403/schedule/2/made).'
- field: SiteNameAddress
  guidance: 'Enter the site name and address in a single line of text, for example:

    ``` Parcel of land behind, 221B Baker Street, Marylebone, London, NW1 6XE ```'
- field: SiteReference
  guidance: 'Enter the unique reference your organisation uses to identify the site.

    If one doesn’t exist, you need to create one. It should not be used by your organisation
    to identify any other sites, but can be borrowed from another data set listing
    the site. You could use the strategic site identifier from your local plan, for
    example:

    ``` EH/141 ```'
- field: SiteplanURL
  guidance: Enter the URL of a web page hosting the site plan, beginning with either
    “http://” or “https://”.
- field: brownfield-land
- field: deliverable
- field: end-date
- field: entity
- field: entry-date
- field: hazardous-substances
- field: hectares
- field: latitude
- field: longitude
- field: maximum-net-dwellings
- field: minimum-net-dwellings
- field: name
- field: notes
- field: organisation
- field: ownership-status
- field: planning-permission-date
- field: planning-permission-history
- field: planning-permission-status
- field: planning-permission-type
- field: point
- field: prefix
- field: reference
- field: site
- field: site-address
- field: site-categories
- field: site-plan-url
- field: start-date
github-discussion: 28
key-field: site
licence: ogl3
name: Brownfield land
paint-options: '{ "colour": "#745729", "type": "point" }'
phase: live
plural: Brownfield land
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- development
typology: geography
version: 1.1
wikidata: Q896586
wikipedia: Brownfield_land
---

This dataset contains a register of Brownfield land sites in England that are suitable to be added to the Brownfield land register. 

Each site references the following categories:

* [ownership-status](/dataset/ownership-status)
* [planning-permission-status](/dataset/planning-permission-status)
* [planning-permission-type](/dataset/planning-permission-type)
* [site-category](/dataset/site-category)

It can be used for:
<ul>
<li>informing planning policies</li>
<li>identifying suitable sites for residential and other development</li>
<li>encouraging private investment</li>
<li>accelerating housing construction by providing clear, publicly available information on previously developed land with development potential</li>
</ul>
