---
attribution: crown-copyright
collection: local-plan
consideration: development-plans-and-timetables
dataset: plan-timetable
description: log of past and future milestones and events when producing a plan
end-date: ''
entity-maximum: '5199999'
entity-minimum: '5100000'
entry-date: '2026-03-24'
fields:
- description: associated plan
  examples:
  - value: LP-BRX-2024
  - value: central-lincolnshire
  field: plan
  guidance: 'Enter the reference of the plan for which this event forms part of its
    timetable.

    '
- examples:
  - value: publish-notice-intention-commence
  - value: examination-submitted
  - value: adopted
  field: plan-event
  guidance: 'Enter a [plan event](https://www.planning.data.gov.uk/dataset/plan-event)
    reference

    for each key event or milestone.

    '
- field: document-url
  guidance: 'Provide the URL of a webpage on your website where this information is
    documented.

    For older plans, this is the Local Development Scheme, which is often a PDF or
    other document.

    This value may be left blank where the timetable information is published on the
    `documentation-url` webpage.

    '
- field: documentation-url
  guidance: 'Provide the URL of the webpage on your website where this information
    is documented.

    '
- description: date when this event was removed from the timetable
  field: end-date
  guidance: 'This field is currently unused in this dataset.

    '
- field: entity
- field: entry-date
- description: predicted date for the event
  field: event-date
  guidance: 'Enter the date when this event will happen.

    '
- description: predicted date for the event
  examples:
  - value: 2027-01-01
  field: predicted-date
  guidance: 'Enter the date when this event is expected to happen.

    '
  notes: 'New local plans require a single, precise date.

    When recording events for older schemes where the predicted date is a range, you
    may record an approximate date for the period.

    '
- field: name
- field: notes
- field: organisation
- field: prefix
- examples:
  - value: LP1-public-consultation
  - value: LP1-public-consultation-2025
  field: reference
  guidance: 'Give each event a unique reference.

    '
- description: date of the timetable event
  field: actual-date
  guidance: 'Enter the date when the timetable event happened. Leave this field blank
    when the event is in the future.

    '
- description: date of the timetable event
  field: start-date
  notes: 'This value is defaulted from the `actual-date` value.

    '
github-discussion: 26
guidance: "Record the key events in the timetable when producing your plan, these
  are sometimes also called 'milestones'. \n\nYour timetable must include an `event-date`
  for when you intend to meet the `plan-event`.\nFind out when you need to update
  the entry to include the actual date in the actual-date field. \n\nFor local plans
  or minerals and waste plans, your timetable must include an entry for each of the
  following `plan-event` field values: \n\n* publish-notice-intention-commence \n*
  scoping-consultation-start \n* scoping-consultation-end \n* gateway-1-self-assessment
  \n* plan-content-evidence-consultation-start \n* plan-content-evidence-consultation-end
  \n* gateway-2-advice-sought \n* proposed-plan-consultation-start \n* proposed-plan-consultation-end
  \n* gateway-3-advice-sought \n* examination-submitted \n* adopted \n\nFor minerals
  and waste plans with multiple documents, \nyour timetable must include an entry
  for each of the `plan-event` field values for each minerals and waste plan document.
  \n\nFor supplementary plans, your local plan timetable or minerals and waste plan
  timetable must include an entry with the following plan-event field values: \n\n*
  publish-notice-intention-commence \n* proposed-plan-consultation-start \n* proposed-plan-consultation-end
  \n* examination-submitted \n* adopted \n\nYour local plan timetable or minerals
  and waste plan timetable must also include rows with an `actual-date` value to set
  out when any of the following events happen: \n\n* gateway-2-advice-published \n*
  gateway-3-advice-published \n* examination-recommendations-published \n* main-modification-consultation-start
  \n* main-modification-consultation-end \n* examination-pause-start \n* examination-pause-end
  \n* additional-consultation-start \n* additional-consultation-end \n* withdrawn
  \n* revoked \n\nIf you repeat Gateway 3, you must include these events in your timetable:
  \n\n* gateway-3-further-advice-sought \n* gateway-3-further-advice-published\n"
key-field: ''
licence: ogl3
name: plan timetable
paint-options: ''
phase: alpha
plural: plan timetables
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- development
typology: timetable
wikidata: ''
wikipedia: ''
---
