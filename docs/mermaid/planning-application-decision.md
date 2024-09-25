---
title: Planning application decision datasets
---
```mermaid
erDiagram
    planning-application-decision {
        string reference
        string name
        string description
        string address-text
        string uprn
        wkt geometry
        wkt point
        url documentation-url
        string planning-application-type
        string planning-decision
        string planning-decision-type
        string notes
        string organisation
        date entry-date
        date start-date
        date decision-date
        date end-date
    }
    planning-application-log {
        string reference
        string planning-application
        string planning-application-status
        url documentation-url
        url document-url
        string notes
        string organisation
        date event-date
        date entry-date
        date start-date
        date end-date
    }
    planning-application-document {
        string reference
        string name
        string description
        string planning-application
        string document-type
        url documentation-url
        url document-url
        string notes
        string organisation
        date entry-date
        date start-date
    }
```
