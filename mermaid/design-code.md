---
title: Design code datasets
---
```mermaid
erDiagram
design-code {
    reference
    name
    description
    design-code-status
    design-code-categories
    design-code-rules
    documentation-url
    document-url
    notes
    start-date
    end-date
    entry-date
}
design-code-area {
    reference
    name
    geometry
    design-code
    documentation-url
    document-url
    notes
    start-date
    end-date
    entry-date
}
design-code-rule {
    reference
    name
    geometry
    design-code
    description
    documentation-url
    document-url
    notes
    start-date
    end-date
    entry-date
}
design-code-area |--o{ design-code
design-code-rule |--o{ design-code
```
