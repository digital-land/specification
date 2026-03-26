---
attribution: crown-copyright
collection: 'local-plan'
consideration: development-plans-and-timetables
dataset: plan-timetable
description: log of past and future milestones and events when producing a plan
end-date: ''
entity-maximum: '5199999'
entity-minimum: '5100000'
entry-date: '2026-03-24'
fields:
- field: plan
  description: "associated plan"
  guidance: |
    Enter the reference of the plan for which this event forms part of its timetable.
  examples:
    - value: 'LP-BRX-2024'
    - value: 'central-lincolnshire'
- field: plan-event
  guidance: |
    Enter a [plan event](https://www.planning.data.gov.uk/dataset/plan-event) reference
    for each key event or milestone.
  examples:
     - value: publish-notice-intention-commence
     - value: examination-submitted
     - value: adopted
- field: document-url
  guidance: |
     Provide the URL of a webpage on your website where this information is documented.
     For older plans, this is the Local Development Scheme, which is often a PDF or other document.
     This value may be left blank where the timetable information is published on the `documentation-url` webpage.
- field: documentation-url
  guidance: |
     Provide the URL of the webpage on your website where this information is documented.
- field: end-date
  description: date when this event was removed from the timetable
  guidance: |
     This field is currently unused in this dataset.
- field: entity
- field: entry-date
- field: event-date
  description: predicted date for the event
  guidance: |
      Enter the date when this event will happen.
- field: predicted-date
  description: predicted date for the event
  guidance: |
      Enter the date when this event is expected to happen.
  notes: |
      New local plans require a single, precise date.
      When recording events for older schemes where the predicted date is a range, you may record an approximate date for the period.
  examples:
     - value: 2027-01-01
- field: name
- field: notes
- field: organisation
- field: prefix
- field: reference
  guidance: |
     Give each event a unique reference.
  examples:
     - value: LP1-public-consultation
     - value: LP1-public-consultation-2025
- field: actual-date
  description: date of the timetable event
  guidance: |
     Enter the date when the timetable event happened. Leave this field blank when the event is in the future.
- field: start-date
  description: date of the timetable event
  notes: |
     This value is defaulted from the `actual-date` value.
github-discussion: 26
guidance: |
    Record the key events in the timetable when producing your plan, these are sometimes also called 'milestones'. 

    Your timetable must include an `event-date` for when you intend to meet the `plan-event`.
    Find out when you need to update the entry to include the actual date in the actual-date field. 

    For local plans or minerals and waste plans, your timetable must include an entry for each of the following `plan-event` field values: 

    * publish-notice-intention-commence 
    * scoping-consultation-start 
    * scoping-consultation-end 
    * gateway-1-self-assessment 
    * plan-content-evidence-consultation-start 
    * plan-content-evidence-consultation-end 
    * gateway-2-advice-sought 
    * proposed-plan-consultation-start 
    * proposed-plan-consultation-end 
    * gateway-3-advice-sought 
    * examination-submitted 
    * adopted 

    For minerals and waste plans with multiple documents, 
    your timetable must include an entry for each of the `plan-event` field values for each minerals and waste plan document. 

    For supplementary plans, your local plan timetable or minerals and waste plan timetable must include an entry with the following plan-event field values: 

    * publish-notice-intention-commence 
    * proposed-plan-consultation-start 
    * proposed-plan-consultation-end 
    * examination-submitted 
    * adopted 

    Your local plan timetable or minerals and waste plan timetable must also include rows with an `actual-date` value to set out when any of the following events happen: 

    * gateway-2-advice-published 
    * gateway-3-advice-published 
    * examination-recommendations-published 
    * main-modification-consultation-start 
    * main-modification-consultation-end 
    * examination-pause-start 
    * examination-pause-end 
    * additional-consultation-start 
    * additional-consultation-end 
    * withdrawn 
    * revoked 

    If you repeat Gateway 3, you must include these events in your timetable: 

    * gateway-3-further-advice-sought 
    * gateway-3-further-advice-published

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
