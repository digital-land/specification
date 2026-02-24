---
title: development plan datasets
---
```mermaid
erDiagram
    development-plan {
        string reference
        string name
        string dataset
        date period-start-date
        date period-end-date
        string local-planning-authorities
        string mineral-planning-authorities
        string waste-planning-authorities
        url documentation-url
        url document-url
        string required-housing
        date entry-date
        string notes
    }
    development-plan-timetable {
        string reference
        ref development-plan
        string development-plan-event
        date committed-date
        date entry-date
        date start-date
        string notes
    }
    development-plan-timetable ||--o{ development-plan : references
```
