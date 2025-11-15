#!/usr/bin/env python3

import sys
import csv
import frontmatter
import datetime


def json_serialize(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError(f"{type(obj)} not serializable")


specifications = {}
for row in csv.DictReader(open("specification/specification.csv", newline="")):
    specifications[row["specification"]] = row

# create dataset-field.csv
fieldnames = ["specification", "dataset", "field", "datasets", "requirement-level", "description", "guidance", "hint", "notes", "start-date", "end-date"]

w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

for specification, item in specifications.items():
    path = f"content/specification/{specification}.md"

    post = frontmatter.load(path)

    if post.metadata["specification"] != specification:
        raise ValueError(f"{path}: unexpected specification: {specification}")

    for d in post.metadata["datasets"]:
        dataset = d["dataset"]
        for f in d["fields"]:

            datasets = f.get("datasets", "")
            if datasets:
                datasets = ";".join(datasets)

            w.writerow(
                {
                    "specification": specification,
                    "dataset": dataset,
                    "datasets": datasets,
                    "field": f["field"],
                    "description": f.get("description", ""),
                    "guidance": f.get("guidance", ""),
                    "requirement-level": f.get("requirement-level"),
                    "notes": f.get("notes", ""),
                    "start-date": f.get("start-date", ""),
                    "end-date": f.get("end-date", ""),
                }
            )
