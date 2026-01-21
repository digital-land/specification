---
specification: brownfield-land
name: Brownfield land
plural: Brownfield land
specification-status: open-standard
specification-reason: brownfield-land-2017
consideration: brownfield-land
start-date: ''
end-date: ''
entry-date: '2022-06-09'
documentation-url: https://www.gov.uk/government/publications/brownfield-land-registers-data-standard/publish-your-brownfield-land-data
github-discussion: 28
datasets:
    - dataset: brownfield-land
      name: brownfield land
      priority: 1
      requirement-level: MUST
      fields:
          - field: OrganisationURI
            requirement-level: SHOULD
          - field: SiteReference
            requirement-level: MUST
            dataset-field: reference
          - field: SiteNameAddress
            requirement-level: MUST
            dataset-field: name
          - field: GeoX
            requirement-level: MUST
          - field: GeoY
            requirement-level: MUST
          - field: SiteplanURL
            requirement-level: MUST
          - field: Hectares
            requirement-level: MUST
          - field: OwnershipStatus
            requirement-level: MUST
          - field: PlanningStatus
            requirement-level: MUST
          - field: PermissionType
            requirement-level: SHOULD
          - field: PermissionDate
            requirement-level: SHOULD
          - field: PlanningHistory
            requirement-level: SHOULD
          - field: Deliverable
            requirement-level: MUST
          - field: NetDwellingsRangeFrom
            requirement-level: MUST
          - field: NetDwellingsRangeTo
            requirement-level: MUST
          - field: HazardousSubstances
            requirement-level: SHOULD
          - field: Notes
            requirement-level: MAY
          - field: FirstAddedDate
            requirement-level: MUST
            dataset-field: start-date
          - field: LastUpdatedDate
            requirement-level: MUST
            dataset-field: entry-date
          - field: EndDate
            dataset-field: end-date
            requirement-level: MAY
---
