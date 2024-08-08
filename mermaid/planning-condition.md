---
title: Planning condition datasets
---
```mermaid
erDiagram
    planning-condition {
        string reference
        string name
        string description
        string organisation
        string notes
        date entry-date
        date start-date
        date end-date
    }
    planning-application-condition {
        string reference
        string planning-application
        ref planning-condition
        string description
        string organisation
        date activation-date
        date discharged-date
        string notes
        date entry-date
        date start-date
        date end-date
    }
    planning-application-condition ||--o{ planning-condition : references
```
