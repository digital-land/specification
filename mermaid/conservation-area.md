---
title: Conservation area datasets
---
```mermaid
erDiagram
    conservation-area {
        string reference
        string name
        string geometry
        url documentation-url
        string notes
        date start-date
        date end-date
        date entry-date
    }
    conservation-area-document {
        string reference
        string conservation-area
        string name
        url documentation-url
        url document-url
        string document-type
        string notes
        date start-date
        date end-date
        date entry-date
    }
    conservation-area-document ||--o{ conservation-area : references
```
