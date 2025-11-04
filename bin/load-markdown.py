#!/usr/bin/env python3

import frontmatter
import sys
import csv
import json
from pathlib import Path

path = Path(sys.argv[1])
dataset = path.stem

d = frontmatter.load("content/dataset/%s.md" % dataset)
fieldnames = [field["field"] for field in d.metadata["fields"]]

w = csv.DictWriter(open(path, "w", newline=""), fieldnames=fieldnames, extrasaction='ignore')
w.writeheader()

for path in sys.argv[2:]:
    post = frontmatter.load(path)
    row = post.metadata
    row["themes"] = ";".join(row.get("themes", "") or [])
    row["specifications"] = ";".join(row.get("specifications", "") or [])
    row["schema"] = row["pipeline"] = row.get(dataset, "")
    row["text"] = post.content

    # handle specification datasets ..
    # TBD: use dataset-field / field/datatype to look for json fields ..
    if dataset == "specification":
        datasets = row["datasets"]
        row["json"] = json.dumps(datasets)
        row["datasets"] = ";".join([d["dataset"] for d in datasets])

    for field in ["examples"]:
        if row.get(field, ""):
            row[field] = json.dumps(row[field])

    w.writerow(row)
