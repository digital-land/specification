#!/usr/bin/env python3

import sys
import csv


# load funds
funds = {}
webpages = {}

for row in csv.DictReader(open("content/fund.csv", newline="")):
    webpages[row['documentation-url']] = row['fund']
    funds[row["reference"]] = row['fund']
    funds[row["start-date"]] = row['fund']

fieldnames = ["fund", "reference", "cohort", "name", "project", "intervention", "documentation-url", "entry-date", "start-date", "end-date", "description", "notes"]

w = csv.DictWriter(open("tmp/cohort.csv", "w", newline=""), fieldnames=fieldnames)
w.writeheader()

for row in csv.DictReader(open("content/cohort.csv")):
    row["reference"] = row["cohort"]

    if not row['fund']:
        if row['documentation-url'] in webpages:
            row['fund'] = webpages[row['documentation-url']]

    key = row["start-date"]
    if key in funds:
        row['fund'] = funds[key]

    if row['project'] != 'localgov-drupal' and row['fund'] not in funds:
        print("unknown fund", row)
        sys.exit(2)

    w.writerow(row)
