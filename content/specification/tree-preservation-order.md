---
specification: tree-preservation-order
name: Tree preservation order
plural: Tree preservation orders
specification-status: piloting
start-date: ''
end-date: ''
entry-date: '2023-09-08'
github-discussion: 43
version: 1.2.3
datasets:
    - dataset: tree-preservation-order
      name: tree preservation order
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the tree preservation order
        - field: name
          description: the name of the tree preservation order
        - field: documentation-url
          description: the URL of the web page where you can find information about the tree preservation order
        - field: document-url
          description: the URL of the tree preservation order document. If a TPO is revoked you can blank out this field.
        - field: made-date
          description: the date the tree preservation order was "made"
        - field: confirmed-date
          description: the date the tree preservation order was "confirmed"
        - field: notes
          description: optional notes
        - field: organisation
          description: the organisation responsible for this tree preservation order
        - field: entry-date
          description: the <a href="#date">date</a> this entry was created or amended
        - field: start-date
          description: the <a href="#date">date</a> the tree preservation order came into force
        - field: end-date
          description: the <a href="#date">date</a> the tree preservation order was revoked. Leave blank if the TPO is still active
    - dataset: tree-preservation-zone
      name: tree preservation zone
      fields:
        - field: reference
          description: the <a href="#reference">reference</a> for the tree preservation zone
        - field: name
          description: the name of the tree preservation zone
        - field: tree-preservation-order
          description: the <a href="#reference">reference</a> for the tree preservation order
        - field: tree-preservation-zone-type
          description: the type of zone, for example area, group or woodland
          dataset: tree-preservation-zone-type
        - field: geometry
          description: the boundary of the area covered by the tree preservation zone in WKT format 
        - field: point
          description: the centre of the tree preservation zone if you cannot provide the full geometry
        - field: notes
          description: optional notes
        - field: organisation
          description: the organisation responsible for this tree preservation order
        - field: entry-date
          description: the <a href="#date">date</a> this entry was created or amended
        - field: start-date
          description: the <a href="#date">date</a> the tree preservation zone came into force
        - field: end-date
          description: the <a href="#date">date</a> the tree preservation zone ended or leave blank if the zone is still active
    - dataset: tree
      name: tree
      fields:
        - field: reference
          description: the number or reference for the tree which appears in the preservation order
        - field: name
          description: the name of the tree
        - field: tree-preservation-order
          description: the <a href="#reference">reference</a> for the tree preservation order
        - field: uprn
          description: unique property reference number if the tree is located on an addressable property
          dataset-field: address
        - field: address-text
          description: the address of the property
        - field: point
          description: the centre of the tree area if you cannot provide the full geometry
        - field: geometry
          description: the boundary of the area covered by the tree in WKT format 
        - field: notes
          description: optional notes
        - field: organisation
          description: the organisation responsible for this tree 
        - field: entry-date
          description: the <a href="#date">date</a> this entry was created or amended
        - field: start-date
          description: the <a href="#date">date</a> from which the tree preservation order affects the tree
        - field: end-date
          description: the <a href="#date">date</a> the tree preservation order no longer affects the tree, or leave blank if the tree is still under the order
---
