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
        date start-date
        date end-date
        date entry-date
    }
    article-4-direction-area {
        string reference
        string name
        string geometry
        string uprn
        string address-text
        string article-4-direction
        string article-4-direction-rules
        url document-url
        string notes
        date start-date
        date end-date
        date entry-date
    }
    article-4-direction-area |--o{ article-4-direction : cites
```
