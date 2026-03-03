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

Providing planning data means making it available publicly to a standard so that anyone using
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can:

* find it
* understand its meaning and purpose
* assess its quality
* trust it will be maintained

[You can help to design this and other data standards to ensure they your needs](https://design.planning.data.gov.uk). 

## Providing your {{ specification["name"] }} data

{% include "content/provide.md" %}

## Contact us

$CTA
Email <digitalland@communities.gov.uk> to get help.
$CTA

You can help
{%- if not specification["consideration"] %}
improve the design of this and other planning data
{% else %}
[improve the design of this and other planning data](https://design.planning.data.gov.uk/consideration/{{ specification["consideration"] }})
{%- endif %}
at [design.planning.data.gov.uk](https://design.planning.data.gov.uk). 

## Technical specifications
