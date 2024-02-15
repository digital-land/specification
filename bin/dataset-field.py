#!/usr/bin/env python3

import sys
import csv
import frontmatter
import requests

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

# TBD: review this code. specifications are controlled documents, but datasets shouldn't need to be versioned
# amend dataset-field-version.csv

new_rows = []
fieldnames_with_version = ["dataset", "field", "field-dataset", "guidance", "hint", "version"]

def fetch_current_pubished_csv():
    #TODO remove this once version number is moved to dataset-field.csv
    github_url = 'https://raw.githubusercontent.com/digital-land/specification/main'
    version_file_url = f'{github_url}/specification/dataset-field-version.csv'

    # TBD: replace this, it doesn't work offline
    resp = requests.get(version_file_url)
    with open('specification/dataset-field-version.csv', 'w', newline='') as csvfile:
        csvfile.write(resp.text)


def row_exists(csv_file, subset_values):
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

# set dataset-field-version.csv to latest version
fetch_current_pubished_csv()
csv_file = 'specification/dataset-field-version.csv'

# determine if new dataset-field-version rows need to be added
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
