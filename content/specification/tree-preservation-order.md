---
specification: tree-preservation-order
name: Tree preservation order
plural: Tree preservation orders
specification-status: working-draft
start-date: ''
end-date: ''
entry-date: '2022-06-09'
datasets:
    - dataset: tree-preservation-order
      name: tree preservation order
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the tree preservation order
        - field: name
        - field: documentation-url
        - field: document-url
        - field: notes
        - field: organisation
        - field: entry-date
          description: the <a href="#date">date</a> this entry was created or amended
        - field: start-date
          description: the <a href="#date">date</a> the tree preservation order came into force
        - field: end-date
    - dataset: tree-preservation-zone
      name: tree preservation zone
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the tree preservation zone
        - field: name
        - field: tree-preservation-order
          description: the <a href="#reference">reference</a> for the tree preservation order
        - field: geometry
        - field: notes
        - field: organisation
        - field: entry-date
          description: the <a href="#date">date</a> this entry was created or amended
        - field: start-date
          description: the <a href="#date">date</a> the tree preservation zone came into force
        - field: end-date
          description: the <a href="#date">date</a> the tree preservation zone was disolved, or blank if the zone is active
    - dataset: tree
      name: tree
      fields:
        - field: reference
          description: the number or reference for the tree which appears in the preservation order
        - field: name
        - field: tree-preservation-order
          description: the <a href="#reference">reference</a> for the tree preservation order
        - field: uprn
          dataset-field: address
        - field: address-text
        - field: point
        - field: geometry
        - field: notes
        - field: organisation
        - field: entry-date
          description: the <a href="#date">date</a> this entry was created or amended
        - field: start-date
          description: the <a href="#date">date</a> from which the tree preservation order affects the tree
        - field: end-date
          description: the <a href="#date">date</a> the tree preservation order no longer affects the tree, or blank if the tree is still under the order
---
