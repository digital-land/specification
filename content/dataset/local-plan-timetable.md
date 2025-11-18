---
attribution: crown-copyright
collection: 'local-plan'
consideration: development-plans-and-timetables
dataset: local-plan-timetable
description: log of past and predicted milestones and events when producing a local plan
end-date: ''
entity-maximum: '4299999'
entity-minimum: '4230000'
entry-date: '2024-10-22'
fields:
- field: local-plan
  description: "associated local plan"
  guidance: |
    Enter the reference of the local plan which this event forms part of its timetable.
  examples:
    - value: 'LP-BRX-2024'
    - value: 'central-lincolnshire'
- field: local-plan-event
  guidance: |
    Enter one of the following [Local Plan Event](https://www.planning.data.gov.uk/dataset/local-plan-event) values:

    * `timetable-published`
    * `reg-18-draft-local-plan-published`
    * `reg-18-public-consultation-start`
    * `reg-18-public-consultation-end`
    * `reg-19-publication-local-plan-published`
    * `reg-19-public-consultation-start`
    * `reg-19-public-consultation-end`
    * `submit-plan-for-examination`
    * `planning-inspectorate-examination-start`
    * `planning-inspectorate-examination-end`
    * `planning-inspectorate-found-sound`
    * `inspector-report-published`
    * `plan-adopted`
    * `plan-withdrawn`
    * `plan-revoked`
- field: document-url
  guidance: |
     Provide the URL of a webpage on your website where this information is documented.
     For older local plans, this is the Local Development Scheme, which is often a PDF or other document.
     This value may be left blank where the timetable information is published on the `document-url` webpage.
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
  notes: "deprecated field, the `start-date` records when the event happened"
- field: predicted-earliest-date
  description: earliest predicted date for the event
  guidance: |
      Enter the earliest date when this event is expected to happen.
  notes: |
      Older published schemes often use vaugue descriptions such as `Spring 2020` or `Q2 2018`.
      Using a range of full dates helps producing timetables and other charts and using the data to analyse the system.
  examples:
     - value: 2027-01-01
- field: predicted-latest-date
  description: latest predicted date for the event
  guidance: |
      Enter the latest date when this event is expected to happen.
  examples:
     - value: 2027-03-31
- field: name
- field: notes
- field: organisation
- field: prefix
- field: reference
  guidance: |
     Give each event a reference which is unique for the event within the dataset.
     Where the timetable contains events for different local plans you can distinguish the events by adding the `local-plan` reference.
     Where a timetable has more than one event of the same kind, you can add a date to make them unique.
  examples:
     - value: LP1-public-consultation
     - value: LP1-public-consultation-2025
- field: start-date
  description: date of the timetable event
  guidance: |
     Enter the date when the timetable event occured. Leave blank when predicting future events,
     such as when you expect a draft local plan to be adopted.
github-discussion: 26
guidance: |
   The local plan timetable is a record of the key dates when producing a local plan.
   Your data should include a row for each of the events listed in the [local plan event](https://www.planning.data.gov.uk/dataset/local-plan-event) dataset with the date when the event happened.
   Provide your predicted range of dates for events which are in the future.
key-field: ''
licence: ogl3
name: Local plan timetable
paint-options: ''
phase: alpha
plural: Local plan timetables
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
