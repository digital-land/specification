---
title: Planning condition datasets
---
```mermaid
erDiagram
    planning-condition {
        string reference
        string name
        string description
        string reason
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
        url document-url
        url documentation-url
        string description
        string notes
        date entry-date
        date start-date
        date end-date
    }
    planning-application-condition ||--o{ planning-condition : references
```
