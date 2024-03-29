---
title: Design code datasets
---
```mermaid
erDiagram
    design-code {
        string reference
        string name
        string description
        string design-code-status
        string design-code-categories
        url documentation-url
        url document-url
        string notes
        date start-date
        date end-date
        date entry-date
    }
    design-code-rule {
        string reference
        string name
        ref design-code
        string description
        url documentation-url
        url document-url
        string notes
        date entry-date
        date start-date
        date end-date
    }
    design-code-area {
        string reference
        string name
        wkt geometry
        ref design-code
        string design-code-rules
        url documentation-url
        url document-url
        string notes
        date entry-date
        date start-date
        date end-date
    }
    design-code-rule ||--o{ design-code : references
    design-code-area ||--o{ design-code : references
```
