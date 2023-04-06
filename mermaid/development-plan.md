---
title: Development plan datasets
---
```mermaid
erDiagram
    development-plan {
        reference
        name
        organisation
        development-plan-type
        documentation-url
        period-start-date
        period-end-date
        start-date
        end-date
        entry-date
    }
    development-plan-timetable {
        reference
        name
        organisation
        development-plan
        development-plan-event
        event-date
        start-date
        end-date
        entry-date
    }
    development-plan-document {
        reference
        name
        organisation
        development-plan
        development-plan-document-type
        documentation-url
        document-url
        start-date
        end-date
        entry-date
    }
    development-plan-timetable |--o{ development-plan
    development-plan-document |--o{ development-plan
```
