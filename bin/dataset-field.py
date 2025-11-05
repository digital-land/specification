#!/usr/bin/env python3

import sys
import csv
import frontmatter
import json
import datetime


def json_serialize(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError(f"{type(obj)} not serializable")


datasets = {}
for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    datasets[row["dataset"]] = row

# create dataset-field.csv
fieldnames = ["dataset", "field", "field-dataset", "description", "guidance", "hint", "notes", "examples", "start-date", "end-date"]

w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

for dataset, item in datasets.items():
    path = f"content/dataset/{dataset}.md"

    post = frontmatter.load(path)
    for row in post.metadata["fields"]:
        field = row["field"]
        field_dataset = row.get("dataset", "")
        if not field_dataset: 
            if field in datasets and field != dataset:
                field_dataset = field

        examples = row.get("examples", "")
        if examples:
            examples = json.dumps(examples, default=json_serialize)

        w.writerow(
            {
                "dataset": dataset,
                "field": field,
                "field-dataset": field_dataset,
                "description": row.get("description", ""),
                "guidance": row.get("guidance", ""),
                "examples": examples,
                "hint": row.get("hint", ""),
                "notes": row.get("notes", ""),
                "start-date": row.get("start-date", ""),
                "end-date": row.get("end-date", ""),
            }
        )
