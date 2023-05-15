---
title: Planning application datasets
---
```mermaid
erDiagram
    planning-application {
        string reference
        string name
        string description
        string address-text
        string address
        wkt geometry
        wkt point
        url documentation-url
        string notes
        string planning-application-type
        string planning-decision
        string planning-decision-type
        string notes
        string organisation
        date entry-date
        date start-date
        date end-date
    }
```
