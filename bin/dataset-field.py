#!/usr/bin/env python3

import sys
import csv
import frontmatter


datasets = {}
for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    datasets[row["dataset"]] = row

# create dataset-field.csv
fieldnames = ["dataset", "field", "field-dataset", "description", "guidance", "hint", "examples"]

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
        w.writerow(
            {
                "dataset": dataset,
                "field": field,
                "field-dataset": field_dataset,
                "description": row.get("description", ""),
                "guidance": row.get("guidance", ""),
                "examples": row.get("examples", ""),
                "hint": row.get("hint", ""),
            }
        )
