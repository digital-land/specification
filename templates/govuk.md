{%- set title = "Provide your " + specification["name"] + " data" %}
---
title: {{ title }}
name: {{ specification["name"] }}
url: {{ specification["documentation-url"] }}
updated: {{ specification["entry-date"] }}
summary: {{ specification["summary"] }}
breadcrumbs:
- name: "Housing, local and community"
  url: https://www.gov.uk/housing-local-and-community
- name: "Planning and building"
  url: https://www.gov.uk/housing-local-and-community/planning-and-building
- name: "Planning system"
  url: https://www.gov.uk/housing-local-and-community/planning-system
attachments:
- url: {{ specification["document-url"] }}
  name: '{{ specification["name"] }} technical specification ({{ specification["entry-date"] }})'
  attachment-type: HTML
  start-date: {{ specification["start-date"] }}
---

^Follow this guidance when providing your {{specification["name"]}} data.^

Providing planning data means making it available publicly to a standard so that
services such as <a href="https://planning.data.gov.uk">planning.data.gov.uk</a> can find it, 
understand its quality, and trust it will be sustained.

{{ tables["specification-reason"][specification["specification-reason"]]["guidance"] | markdown }}

## Providing {{ specification["name"] }} data

{% include "content/provide.md" %}

## Data files, fields and formats

$CTA
If you need any help at any stage of the process, let us know by emailing <digitalland@communities.gov.uk> and a member of our team will be in touch.
$CTA
