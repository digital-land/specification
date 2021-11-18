#!/usr/bin/env python3

import frontmatter
import sys
import csv

d = frontmatter.load("content/dataset/collection.md")
fieldnames = [field["field"] for field in d.metadata["fields"]]

w = csv.DictWriter(open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction='ignore')
w.writeheader()

seen = {}
for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    row["schema"] = row["dataset"]
    if row.get("collection", None) and row["collection"] not in seen:
        w.writerow(row)
        seen[row["collection"]] = True
