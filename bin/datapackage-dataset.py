#!/usr/bin/env python3

import sys
import csv
import frontmatter

fieldnames = ["datapackage", "dataset"]

w = csv.DictWriter(open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction='ignore')
w.writeheader()

for row in csv.DictReader(open("specification/datapackage.csv", newline="")):
    datapackage = row["datapackage"]
    path = "content/datapackage/%s.md" % datapackage
    post = frontmatter.load(path)
    for dataset in post.metadata.get("datasets", []):
        w.writerow({"datapackage": datapackage, "dataset": dataset})
