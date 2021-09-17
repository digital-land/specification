#!/usr/bin/env python3

import sys
import csv

# add missing name fields ..

for table in ["schema", "pipeline", "collection"]:
    path = "specification/%s.csv"%table
    w = None
    for row in csv.DictReader(open(path, newline="")):
        if not w:
            fields = row.keys()
            w = csv.DictWriter(open(path, "w"), fields)
            w.writeheader()

        if "name" not in row or not row["name"]:
            row["name"] = row[table].replace("-", " ").capitalize()

        w.writerow(row)
