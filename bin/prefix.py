#!/usr/bin/env python3

import sys
import csv

fieldnames = ["prefix", "prefix-uri", "organisation"]

prefixes = {}

for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    dataset = row["dataset"]
    prefix = row.get("prefix", "") or dataset
    if row["typology"] in ["specification"]:
        continue
    print(prefix)
    prefixes[prefix] = row

for row in csv.DictReader(open("content/prefix.csv", newline="")):
    prefix = row.get("prefix", "")
    prefixes[prefix] = {**prefixes.get(prefix, {}), **row}

w = csv.DictWriter(open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction='ignore')
w.writeheader()

for prefix, row in prefixes.items():
    if prefix:
        row["prefix"] = prefix
        w.writerow(row)
