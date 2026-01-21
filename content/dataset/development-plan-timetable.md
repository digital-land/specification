---
attribution: crown-copyright
collection: ''
consideration: development-plans-and-timetables
dataset: development-plan-timetable
description: log of past and predicted milestones and events when producing a development plan
end-date: ''
entity-maximum: '5199999'
entity-minimum: '5100000'
entry-date: '2026-01-19'
fields:
- field: development-plan
  description: "associated development plan"
  guidance: |
    Enter the reference of the development plan which this event forms part of its timetable.
  examples:
    - value: 'LP-BRX-2024'
    - value: 'central-lincolnshire'
- field: development-plan-event
  guidance: |
    Enter a [Development Plan Event](https://www.planning.data.gov.uk/dataset/development-plan-event) reference.
  examples:
     - value: commenced
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
     Give each event a reference which is unique for the event within the dataset.
     Where a timetable has more than one event of the same type, you can add a date to make them unique.
  examples:
     - value: LP1-public-consultation
     - value: LP1-public-consultation-2025
- field: start-date
  description: date of the timetable event
  guidance: |
     Enter the date when the timetable event occured. Leave this field blank when the event is in the future.
github-discussion: 26
guidance: |
    Record the key events and milestones in the timetable when producing your development plan.
    For new local plans your timetable must include a precise `predicted-date` against each entry.
    Update the entry to include the actual date in the `start-date` field when the event takes place.

    For local plans, minerals plans, and waste plans being produced under the new local plans process,
    your timetable must include a entry for each of the the following events:

    * `commenced`
    * `scoping-consultation-start`
    * `scoping-consultation-end`
    * `gateway-1-self-assessment`
    * `content-consultation-start`
    * `content-consultation-end`
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

    Supplimentary plans being produced under the new local plans process must contain a row for each of the following events:

    * `commenced`
    * `proposed-plan-consultation-start`
    * `proposed-plan-consultation-end`
    * `examination-submitted`
    * `adopted`
    
    Your development plan timetable may also include rows with dates for each of the following events:

    * `main-modification-consultation-start`
    * `main-modification-consultation-end`
    * `examination-pause-start`
    * `examination-pause-end`
    * `additional-consultation-start`
    * `additional-consultation-end`
    * `annual-monitoring-report-published`
    * `plan-evaluation-report-published`
    * `withdrawn`
    * `revoked`
key-field: ''
licence: ogl3
name: development plan timetable
paint-options: ''
phase: alpha
plural: development plan timetables
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
