#!/usr/bin/env python3

import sys
import csv

w = None
fields = ["field", "name", "datatype", "cardinality", "dataset", "parent-field", "replacement-field", "description", "entry-date", "start-date", "end-date"]
schemas = {}

for row in csv.DictReader(open("specification/schema.csv", newline="")):
    schemas[row["schema"]] = row

path = "specification/field.csv"
for row in csv.DictReader(open(path, newline="")):
    if not w:
        w = csv.DictWriter(open(path, "w"), fields)
        w.writeheader()

    field = row["field"]
    if field in schemas:
        dataset = field
    elif field.endswith("-field"):
        dataset = "field"
    else:
        dataset = ""
    row["dataset"] = dataset

    for field in fields:
        if field not in row:
            row[field] = ""

    w.writerow(row)
