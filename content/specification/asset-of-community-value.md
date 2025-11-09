---
specification: asset-of-community-value
name: Asset of community value
plural: Assets of community value
specification-status: working-draft
specification-reason: prospective
consideration: assets-of-community-value
start-date: ''
end-date: ''
entry-date: '2025-03-04'
github-discussion: 100
version: 1.0.0
datasets:
    - dataset: asset-of-community-value
      description: "Buildings or pieces of land that are used for the social wellbeing and interests of the local community"
      fields:
        - field: reference
          description: a unique code for this asset of community value, for example `A-CV-1`
        - field: name
          description: a name for the asset of community value, for example, Magdala Public House
        - field: address-text
          description: an address for the asset
        - field: description
          description: a description of the asset of community value
        - field: point
          description: coordinates, in WGS84, of the asset
        - field: geometry
          description: if available, a boundary for the asset in WKT format
        - field: organisation
          description: 'a code for the authority whose register it is on, e.g. local-authority:CMD'
        - field: nomination-date
          description: the date the asset was nominated to go on the register
        - field: nominating-group
          description: the group who nominated the asset, for example, Friends of the Magdala
        - field: decision
          description: the decision whether successful or unsuccessful
        - field: decision-date
          description: the date the decision was published, in `YYYY-MM-DD` format
        - field: expiry-date
          description: the date the listing on the register expires, usually 5 years after the decision date, for example 2029-12-01
        - field: notification-to-sell-date
          description: the date the owner informs the authority of their wish to sell the asset
        - field: interested-group
          description: the group that has registered an interest, triggering the moratorim period
        - field: protected-period-start-date
          description: the date the protection period starts. It will last 18 months from this date.
        - field: notes
          description: optional notes
        - field: entry-date
          description: the date this record was created
        - field: start-date
          description: the date the asset was nominated
        - field: end-date
          description: the date this assets was removed from the asset register
---
