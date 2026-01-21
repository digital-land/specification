{%- set title = "Provide your " + specification["name"] + " data" -%}
---
title: {{ title }}
name: {{ specification["name"] }}
url: {{ specification["documentation-url"] }}
summary: {{ specification["summary"] }}
entry-date: {{ specification["entry-date"] }}
updated: {{ specification["entry-date"] | govuk_date }}
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
attachments:
- url: {{ specification["document-url"] or specification["documentation-url"] or "/specification/specification/"+specification["specification"] }}
  name: '{{ specification["name"] | sentence_case }} technical specification ({{ specification["entry-date"] | govuk_date }})'
  attachment-type: HTML
  start-date: {{ specification["start-date"] }}
---

^Follow this guidance when providing your {{specification["name"]}} data.^

{{ tables["specification-reason"][specification["specification-reason"]]["guidance"] | markdown }}

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can find it, 
understand its quality, and trust it will be sustained.
[Help design this and other data standards to ensure they your needs](https://design.planning.data.gov.uk). 

## Providing your {{ specification["name"] }} data

{% include "content/provide.md" %}

## Contact us

$CTA
If you need any help at any stage of the process,
let us know by emailing <digitalland@communities.gov.uk> and a member of our team will be in touch.
$CTA

You can participate in 
{%- if not specification["consideration"] %}
improving the design of this data 
{% else %}
[improving the design of this data](https://design.planning.data.gov.uk/consideration/{{ specification["consideration"] }})
{%- endif %},
and help ensure planning data meets your needs at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 

## Technical specifications
