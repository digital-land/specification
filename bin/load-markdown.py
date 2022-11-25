#!/usr/bin/env python3

import frontmatter
import sys
import csv
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

    w.writerow(row)
