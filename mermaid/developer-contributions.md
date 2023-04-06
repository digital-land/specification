---
title: Developer contributions datasets
---
```mermaid
erDiagram
developer-agreement {
    reference
    name
    developer-agreement-type
    planning-application
    document-url
    organisation
    entry-date
    start-date
    end-date
}
developer-agreement-contribution {
    reference
    developer-agreement
    contribution-purpose
    amount
    units
    organisation
    entry-date
    start-date
    end-date
}
developer-agreement-transaction {
    reference
    contribution-funding-status
    amount
    units
    developer-agreement-contribution
    organisation
    entry-date
    start-date
    end-date
}
developer-agreement-contribution |--o{ developer-agreement
developer-agreement-transaction |--o{ developer-agreement-contribution
```
