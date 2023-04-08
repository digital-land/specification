---
title: Tree preservation order datasets
---
```mermaid
erDiagram
    tree-preservation-order {
        string reference
        string name
        url documentation-url
        url document-url
        string notes
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    tree-preservation-zone {
        string reference
        string name
        ref tree-preservation-order
        wkt geometry
        string notes
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    tree {
        string reference
        string name
        ref tree-preservation-order
        string tree-preservation-order-tree
        string uprn
        string address-text
        wkt point
        wkt geometry
        string notes
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    tree-preservation-zone ||--o{ tree-preservation-order : references
    tree ||--o{ tree-preservation-order : references
```
