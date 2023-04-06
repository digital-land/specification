---
title: Development plan datasets
---
```mermaid
erDiagram
    development-plan {
        string reference
        string name
        string development-plan-type
        date period-start-date
        date period-end-date
        url documentation-url
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    development-plan-timetable {
        string reference
        string name
        string development-plan
        string development-plan-event
        date event-date
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    development-plan-document {
        string reference
        string name
        string development-plan
        string development-plan-document-type
        url documentation-url
        url document-url
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    development-plan-timetable ||--o{ development-plan : references
    development-plan-document ||--o{ development-plan : references
```
