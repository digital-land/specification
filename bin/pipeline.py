#!/usr/bin/env python3

import sys
import csv

fieldnames = ["pipeline", "name", "plural", "schema", "scope-field", "slug-prefix"]

w = csv.DictWriter(open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction='ignore')
w.writeheader()

for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    row["pipeline"] = row["dataset"]
    row["schema"] = row["dataset"]
    w.writerow(row)
