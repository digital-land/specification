---
consideration: assets-of-community-value
datasets:
- dataset: asset-of-community-value
  description: Buildings or pieces of land that are used for the social wellbeing
    and interests of the local community
  fields:
  - description: a unique code for this asset of community value, for example `A-CV-1`
    field: reference
  - description: a name for the asset of community value, for example, Magdala Public
      House
    field: name
  - description: an address for the asset
    field: address-text
  - description: a description of the asset of community value
    field: description
  - description: coordinates, in WGS84, of the asset
    field: point
  - description: if available, a boundary for the asset in WKT format
    field: geometry
  - description: a code for the authority whose register it is on, e.g. local-authority:CMD
    field: organisation
  - description: the date the asset was nominated to go on the register
    field: nomination-date
  - description: the group who nominated the asset, for example, Friends of the Magdala
    field: nominating-group
  - description: the decision whether successful or unsuccessful
    field: decision
  - description: the date the decision was published, in `YYYY-MM-DD` format
    field: decision-date
  - description: the date the listing on the register expires, usually 5 years after
      the decision date, for example 2029-12-01
    field: expiry-date
  - description: the date the owner informs the authority of their wish to sell the
      asset
    field: notification-to-sell-date
  - description: the group that has registered an interest, triggering the moratorim
      period
    field: interested-group
  - description: the date the protection period starts. It will last 18 months from
      this date.
    field: protected-period-start-date
  - description: optional notes
    field: notes
  - description: the date this record was created
    field: entry-date
  - description: the date the asset was nominated
    field: start-date
  - description: the date this assets was removed from the asset register
    field: end-date
end-date: ''
entry-date: '2025-03-04'
github-discussion: 100
name: Asset of community value
plural: Assets of community value
specification: asset-of-community-value
specification-reason: prospective
specification-status: working-draft
start-date: ''
---
