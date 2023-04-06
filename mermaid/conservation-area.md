---
title: Conservation area datasets
---
```mermaid
erDiagram
    conservation-area {
        reference
        name
        geometry
        documentation-url
        notes
        start-date
        end-date
        entry-date
    }
    conservation-area-document {
        reference
        conservation-area
        name
        documentation-url
        document-url
        document-type
        notes
        start-date
        end-date
        entry-date
    }
    conservation-area-document |--o{ conservation-area
```
