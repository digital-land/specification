---
title: Development policy datasets
---
```mermaid
erDiagram
    development-policy {
        string reference
        string name
        string organisation
        string development-plan-document
        string development-policy-categories
        date start-date
        date end-date
        date entry-date
    }
    development-policy-area {
        string reference
        string name
        string organisation
        string geometry
        string development-policies
        date start-date
        date end-date
        date entry-date
    }
```
