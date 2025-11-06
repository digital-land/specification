---
attribution: crown-copyright
collection: 'local-plan'
consideration: development-plans-and-timetables
dataset: local-plan-timetable
description: a log of past and predicted milestones and events when producing a local plan
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

    * `plan-adopted`
    * `inspector-report-published`
    * `submit-plan-for-examination`
    * `planning-inspectorate-examination-start`
    * `planning-inspectorate-examination-end`
    * `planning-inspectorate-found-sound`
    * `timetable-published`
    * `estimated-submit-plan-for-examination`
    * `reg-18-draft-local-plan-published`
    * `reg-18-public-consultation-start`
    * `reg-18-public-consultation-end`
    * `reg-19-publication-local-plan-published`
    * `reg-19-public-consultation-start`
    * `reg-19-public-consultation-end`
    * `estimated-reg-18-draft-local-plan-published`
    * `estimated-reg-18-public-consultation-end`
    * `estimated-reg-19-public-consultation-start`
    * `estimated-reg-19-public-consultation-end`
    * `estimated-reg-18-public-consultation-start`
    * `estimated-reg-19-publication-local-plan-published`
    * `estimated-plan-adoption-date`
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
     Give each event a reference which is unique within the dataset. Where the timetable contains events for different local plans.
     Where a timetable has multiple events, you can add a date to make them unique.
  examples:
     - value: LP1-plan-adopted
     - value: LP1-plan-adopted-2025
- field: start-date
  description: date of the timetable event
  guidance: |
     Enter the date when the timetable event occured. Leave blank when predicting future events,
     such as when you expect a draft local plan to be adopted.
github-discussion: 26
guidance: |
   The local plan timetable is a record of the key dates when producing a local plan.
   Your data should include a row for each of the events listed in the [Local Plan Event](https://www.planning.data.gov.uk/dataset/local-plan-event) dataset with the date when the event happened, or your estimated period for where an event is in the future.
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
version: 1.0
wikidata: ''
wikipedia: ''
---
