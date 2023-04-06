---
title: Tree preservation order datasets
---
```mermaid
erDiagram
tree-preservation-order {
    reference
    name
    documentation-url
    document-url
    notes
    start-date
    end-date
    entry-date
}
tree-preservation-zone {
    reference
    name
    tree-preservation-order
    geometry
    notes
    start-date
    end-date
    entry-date
}
tree {
    reference
    name
    point
    tree-preservation-order
    tree-preservation-order-tree
    geometry
    uprn
    address-text
    notes
    start-date
    end-date
    entry-date
}
tree-preservation-zone |--o{ tree-preservation-order
tree |--o{ tree-preservation-order
```
