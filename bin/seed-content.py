#!/usr/bin/env python3

#  convert csv files to .md files with front-matter

import sys
import csv
import frontmatter
from pathlib import Path

table = {}


def dump(_table):
    for name, row in table[_table].items():
        directory = "content/%s" % _table
        Path(directory).mkdir(parents=True, exist_ok=True)
        with open("%s/%s.md" % (directory, name), "wb") as f:
            post = frontmatter.Post(row.get("text", ""))
            for field in row:
                if field not in ["text"]:
                    post[field] = row[field]
            frontmatter.dump(post, f)


def load(name):
    table.setdefault(name, {})
    for row in csv.DictReader(open("specification/%s.csv" % name, newline="")):
        table[name][row[name]] = row


# naturally sort a list of field records ..
def sorted_fields(fields):
    fields = sorted(fields, key=lambda d: d['field'])
    if schema in fields:
        fields.pop(fields.index(schema))
        fields = [schema] + fields

    # move default register fields to end, order is same as in list
    for field in ["entry-date", "start-date", "end-date"]:
        if field in fields:
            fields.append(fields.pop(fields.index(field)))

    return fields


def add_dataset_field(dataset, field):
    fields = table["dataset"][dataset].setdefault("fields", [])
    fieldnames = [field["field"] for field in fields]
    if field not in fieldnames:
        table["dataset"][dataset]["fields"].append({"field": field, "description": "", "text": "", "end-date": ""})


# as-is
load("field")
dump("field")
load("theme")
dump("theme")
load("typology")
dump("typology")
load("datatype")
dump("datatype")
load("project")
for project, row in table["project"].items():
    table["project"][project].setdefault("datasets", [])
dump("project")
load("project-status")
dump("project-status")

# merge schema, schema-field and pipeline into dataset ..
load("dataset")
load("schema")
load("pipeline")

# add schema info to dataset
for schema, row in table["schema"].items():
    if schema not in table["dataset"]:
        table["dataset"][schema] = {
            "dataset": row["schema"],
            "name": row["name"],
            "description": row["description"],
        }
    if not table["dataset"][schema].get("key-field", ""):
        table["dataset"][schema]["key-field"] = row["key-field"]

# add schema fields to schema and dataset with the same name
for row in csv.DictReader(open("specification/schema-field.csv", newline="")):
    schema = row["schema"]
    field = row["field"]
    table["schema"][schema].setdefault("fields", [])
    table["schema"][schema]["fields"].append(field)
    add_dataset_field(schema, field)

# default dataset fields from pipeline schema fields
for pipeline, row in table["pipeline"].items():
    dataset = pipeline
    schema = row["schema"]
    if not table["dataset"][dataset].get("fields", []):
        for field in table["schema"][schema]["fields"]:
            add_dataset_field(dataset, field)

# harmonise dataset
for dataset, row in table["dataset"].items():

    # turn themes into a list ..
    row["themes"] = row.get("themes", "").split(";")

    if not row.get("fields", None):
        typology = row["typology"]
        for field in table["schema"][typology]["fields"]:
            add_dataset_field(dataset, field)

    # ensure key-field is in fields ..
    fields = [field["field"] for field in row["fields"]]
    if "entity" in fields:
        key_field = row.get("key-field", "") or dataset
        add_dataset_field(dataset, key_field)

    # sort fields by name .. TBD: natural sort
    # row["fields"] = sorted_fields[row["fields"]

    # remove deprecated fields ..
    for field in ["schema", "pipeline"]:
        if field in row:
            del row[field]


dump("dataset")
