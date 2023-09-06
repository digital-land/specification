#!/usr/bin/env python3

import sys
import csv
import frontmatter

# create dataset-field.csv
fieldnames = ["dataset", "field", "field-dataset", "guidance", "hint"]

w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    dataset = row["schema"] = row["dataset"]
    path = f"content/dataset/{dataset}.md"

    post = frontmatter.load(path)
    for field in post.metadata["fields"]:
        w.writerow(
            {
                "dataset": dataset,
                "field": field["field"],
                "guidance": field.get("guidance", ""),
                "field-dataset": field.get("dataset", ""),
            }
        )

# ----------------------------------------------------------------

# amend dataset-field-version.csv

new_rows = []
fieldnames_with_version = ["dataset", "field", "field-dataset", "guidance", "hint", "version"]

def row_exists(csv_file, subset_values):
    # lets open file each time
    with open(csv_file, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for r in csv_reader:
            # Check if the subset_values are present in the row
            if all(v == r[k] for k, v in subset_values.items()):
                return True
        return False

def version_major_number(version):
    return str(int(version))

def append_rows(csv_file, fieldnames, rows):
    with open(csv_file, 'a', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerows(rows)


csv_file = 'specification/dataset-field-version.csv'

for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    dataset = row["schema"] = row["dataset"]
    path = f"content/dataset/{dataset}.md"

    post = frontmatter.load(path)
    # check schema has version number
    if 'version' in post.metadata:
        version = version_major_number(post.metadata["version"])
        for field in post.metadata["fields"]:
            dataset_field_version_row = {
                'dataset': dataset,
                'field': field['field'],
                'version': version
            }
            if not row_exists(csv_file, dataset_field_version_row):
                new_rows.append(
                    {
                        "dataset": dataset,
                        "field": field["field"],
                        "guidance": field.get("guidance", ""),
                        "field-dataset": field.get("dataset", ""),
                        "hint": field.get("hint", ""),
                        "version": version
                    }
                )

if len(new_rows) > 0:
    append_rows(csv_file, fieldnames_with_version, new_rows)
