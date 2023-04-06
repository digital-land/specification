---
title: Development plan datasets
---
```mermaid
erDiagram
    development-plan {
        string reference
        string name
        string organisation
        string development-plan-type
        url documentation-url
        date period-start-date
        date period-end-date
        date start-date
        date end-date
        date entry-date
    }
    development-plan-timetable {
        string reference
        string name
        string organisation
        string development-plan
        string development-plan-event
        date event-date
        date start-date
        date end-date
        date entry-date
    }
    development-plan-document {
        string reference
        string name
        string organisation
        string development-plan
        string development-plan-document-type
        url documentation-url
        url document-url
        date start-date
        date end-date
        date entry-date
    }
    development-plan-timetable ||--o{ development-plan : references
    development-plan-document ||--o{ development-plan : references
```
