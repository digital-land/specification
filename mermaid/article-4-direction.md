---
title: Article 4 direction datasets
---
```mermaid
erDiagram
    article-4-direction {
        string reference
        string name
        string description
        url documentation-url
        url document-url
        string notes
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    article-4-direction-area {
        string reference
        string name
        string article-4-direction
        string article-4-direction-rules
        string uprn
        string address-text
        string geometry
        url document-url
        string notes
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    article-4-direction-area ||--o{ article-4-direction : references
```
