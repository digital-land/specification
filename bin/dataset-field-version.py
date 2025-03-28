#!/usr/bin/env python3

import csv
import frontmatter
import shutil


# TBD: review this code. specifications are controlled documents, but datasets shouldn't need to be versioned
# amend dataset-field-version.csv

new_rows = []
fieldnames_with_version = [
    "dataset",
    "field",
    "field-dataset",
    "guidance",
    "hint",
    "version",
]


def row_exists(csv_file, subset_values):
    with open(csv_file, "r", newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for r in csv_reader:
            # Check if the subset_values are present in the row
            if all(v == r[k] for k, v in subset_values.items()):
                return True
        return False


def version_major_number(version):
    return str(int(version))


def append_rows(csv_file, fieldnames, rows):
    with open(csv_file, "a", newline="") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerows(rows)


# get current dataset-field-version.csv - otherwise build process deletes field version history
shutil.copyfile(
    "data/dataset-field-version.csv", "specification/dataset-field-version.csv"
)

dataset_field_version_file = "specification/dataset-field-version.csv"

# determine if new dataset-field-version rows need to be added
for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    dataset = row["schema"] = row["dataset"]
    path = f"content/dataset/{dataset}.md"

    post = frontmatter.load(path)
    # check schema has version number
    if "version" in post.metadata:
        version = version_major_number(post.metadata["version"])
        for field in post.metadata["fields"]:
            dataset_field_version_row = {
                "dataset": dataset,
                "field": field["field"],
                "version": version,
            }
            if not row_exists(dataset_field_version_file, dataset_field_version_row):
                new_rows.append(
                    {
                        "dataset": dataset,
                        "field": field["field"],
                        "guidance": field.get("guidance", ""),
                        "field-dataset": field.get("dataset", ""),
                        "hint": field.get("hint", ""),
                        "version": version,
                    }
                )

if len(new_rows) > 0:
    append_rows(dataset_field_version_file, fieldnames_with_version, new_rows)
    # store copy of dataset-field-version.csv in data directory to maintain history
    shutil.copyfile(
        "specification/dataset-field-version.csv", "data/dataset-field-version.csv"
    )
