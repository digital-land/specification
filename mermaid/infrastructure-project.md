---
title: infrastructure project datasets
---
```mermaid
erDiagram
    infrastructure-project {
        string reference
        string name
        string description
        string applicant-organisation
        string infrastructure-project-decision
        date decision-date
        string decision-maker
        wkt geometry
        wkt point
        url documentation-url
        string infrastructure-project-type
        string notes
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    infrastructure-project-log {
        string reference
        ref infrastructure-project
        string infrastructure-project-event
        date event-date
        string notes
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    infrastructure-project-document {
        string reference
        ref infrastructure-project
        string document-type
        string name
        string notes
        string organisation
        url document-url
        url documentation-url
        date entry-date
        date start-date
        date end-date
    }
    infrastructure-project-log ||--o{ infrastructure-project : references
    infrastructure-project-document ||--o{ infrastructure-project : references
```
