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


def field_typology(f):
    if f["parent-field"] == "" or f["field"] == f["parent-field"]:
        return f["parent-field"]
    if f["parent-field"] not in table["field"]:
        return ""
    return field_typology(table["field"][f["parent-field"]])


def add_dataset_field(dataset, field, row={}):
    fields = table["dataset"][dataset].setdefault("fields", [])
    fieldnames = [field["field"] for field in fields]
    if field not in fieldnames:
        f = { "field": field }
        for col in ["end-date", "guidance"]:
            value = row.get(col, "")
            if value:
                f[col] = value
        table["dataset"][dataset]["fields"].append(f)


def name(s):
    return s.replace("-", " ").capitalize()


# as-is
load("theme")
dump("theme")

load("typology")
dump("typology")

load("datatype")
dump("datatype")

load("datapackage")
for row in csv.DictReader(open("specification/datapackage-dataset.csv", newline="")):
    datapackage = row["datapackage"]
    table["datapackage"][datapackage].setdefault("datasets", [])
    table["datapackage"][datapackage]["datasets"].append(row["dataset"])
dump("datapackage")

load("project")
for project, row in table["project"].items():
    table["project"][project].setdefault("datasets", [])
dump("project")

load("project-status")
dump("project-status")

load("field")
load("dataset")
load("pipeline")

# add schema fields to schema and dataset with the same name
for row in csv.DictReader(open("specification/dataset-field.csv", newline="")):
    field = row["field"]
    add_dataset_field(row["dataset"], field, row)

# ensure all fields have a name
for field, row in table["field"].items():
    if not row.get("typology", ""):
        row["typology"] = field_typology(row)

    if not row.get("name", ""):
        row["name"] = name(field)

# harmonise dataset
for dataset, row in table["dataset"].items():

    # turn themes into a list ..
    themes = row.get("themes", "").split(";")
    if themes == ['']:
        if row["typology"] == "specification":
            themes = ["specification"]
        else:
            themes = []
    row["themes"] = themes

    if not row.get("fields", None):
        typology = row["typology"]
        for field in table["dataset"][typology]["fields"]:
            add_dataset_field(dataset, field)

    # remove defaulted key-field
    if row.get("key-field", "") == dataset:
        del row["key-field"]

    # ensure the key-field is in fields ..
    fields = [field["field"] for field in row["fields"]]
    if "entity" in fields:
        key_field = row.get("key-field", "") or dataset
        add_dataset_field(dataset, key_field)

        # default dataset typology from key-field typology
        if not row.get("typology", "") and key_field in table["field"]:
            row["typology"] = table["field"][key_field].get("typology", "")

        # ensure key-field exists as a field
        if key_field not in table["field"]:
            table["field"][key_field] = {
                "field": key_field,
                "typology": row.get("typology", ""),
                "name": name(key_field),
                "cardinality": "1",
                "datatype": "string",
                "description": row["description"],
                "parent-field": row.get("typology", ""),
            }

    # remove deprecated fields ..
    for field in ["schema", "pipeline"]:
        if field in row:
            del row[field]

dump("field")
dump("dataset")
