---
title: Article 4 direction datasets
---
```mermaid
erDiagram
    article-4-direction {
        reference
        name
        description
        documentation-url
        document-url
        notes
        start-date
        end-date
        entry-date
    }
    article-4-direction-area {
        reference
        name
        geometry
        uprn
        address-text
        article-4-direction
        article-4-direction-rules
        document-url
        notes
        start-date
        end-date
        entry-date
    }
    article-4-direction-area |--o{ article-4-direction
```
