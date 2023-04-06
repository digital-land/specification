---
title: Development policy datasets
---
```mermaid
erDiagram
    development-policy {
        string reference
        string name
        string development-plan-document
        string development-policy-categories
        string organisation
        date entry-date
        date start-date
        date end-date
    }
    development-policy-area {
        string reference
        string name
        wkt geometry
        string development-policies
        string organisation
        date entry-date
        date start-date
        date end-date
    }
```
