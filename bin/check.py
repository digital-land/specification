#!/usr/bin/env python3

#  check integrity of specification CSV files

import sys
import csv

dialect = csv.excel
dialect.strict = True

keys = {
    "schema-field": ["schema", "field"],
    "dataset-schema": ["dataset", "schema"],
    #"datapackage-dataset": ["datapackage", "dataset"],
}

fields = {}
mandatory_fields = [
    "entry-date",
    "start-date",
    "end-date",
]

tables = {
    "field": {},
    "datatype": {},
    "schema": {},
    "dataset": {},
    "project": {},
    "project-status": {},
    "typology": {},
    "theme": {},
    "schema-field": {},
    "dataset-schema": {},
    "datapackage": {},
    #"datapackage-dataset": {},
}

errors = 0


def error(s):
    global errors
    print("[ERROR]: " + s, file=sys.stderr)
    errors += 1


def load(table):
    path = "specification/%s.csv" % (table)
    reader = csv.DictReader(open(path, newline=""), dialect=dialect)
    fields[table] = reader.fieldnames
    for row in reader:
        if table not in keys:
            key = table
            tables[table][row[key]] = row
        else:
            pkey, skey = keys[table]
            tables[table].setdefault(row[pkey], {})
            tables[table][row[pkey]][row[skey]] = row


def check_reference(table, field, value):
    if field != table and field in tables:
        if value not in tables[field]:
            error("%s: unknown '%s' value '%s'" % (table, field, value))


def field_typology(f):
    if f["parent-field"] == "" or f["field"] == f["parent-field"]:
        return f["parent-field"]

    return field_typology(tables["field"][f["parent-field"]])


def check_typologies():
    for field, f in tables["field"].items():
        typology = field_typology(f)
        if typology not in tables["typology"]:
            error("field '%s' has an unknown typology '%s'" % (field, typology))


def check_datasets():
    for project, p in tables["project"].items():
        for dataset in p["datasets"].split(";"):
            if dataset and dataset not in tables["dataset"]:
                error("project '%s' has an unknown dataset '%s'" % (project, dataset))


def check_themes():
    for dataset, d in tables["dataset"].items():
        for theme in d["themes"].split(";"):
            if theme not in tables["theme"]:
                error("dataset '%s' has an unknown theme '%s'" % (dataset, theme))


def check_project_status():
    for project, p in tables["project"].items():
        for status in p["project-status"].split(";"):
            if status not in tables["project-status"]:
                error("project '%s' has an unknown project-status '%s'" % (project, status))


def check(table):
    if table not in tables["schema"]:
        return error("no schema for table %s" % (table))

    if table not in tables["schema-field"]:
        return error("no schema-field values for table %s" % (table))

    for field in fields[table]:
        if field not in tables["field"]:
            return error("%s: column '%s' not defined as a field" % (table, field))

    for field in tables["schema-field"][table]:
        if field not in fields[table] and field not in mandatory_fields:
            error("%s: missing '%s' column" % (table, field))

    if table not in keys:
        for key, row in tables[table].items():
            for field, value in row.items():
                check_reference(table, field, value)
    else:
        for pkey, skey in tables[table].items():
            for key, row in tables[table][pkey].items():
                for field, value in row.items():
                    check_reference(table, field, value)


if __name__ == "__main__":
    for table in tables:
        load(table)

    for table in tables:
        check(table)

    for t in ["dataset", "schema", "field", "datatype", "typology"]:
        for name, item in tables[t].items():
            if (not item.get("name", "")) and (
                t == "schema"
                and not (
                    name in tables["field"] and tables["field"][name].get("name", "")
                )
            ):
                error("no name for %s '%s'" % (t, name))

    for schema, s in tables["schema"].items():
        if schema not in tables["schema-field"]:
            error("no fields for schema '%s'" % (schema))
        else:
            for field in mandatory_fields:
                if field not in tables["schema-field"][schema]:
                    error("schema '%s' missing '%s' field" % (schema, field))

    for key, row in tables["field"].items():
        if not row.get("name", ""):
            error("no name for field '%s'" % (key))
        for field in ["parent-field", "replacement-field"]:
            value = row.get(field)
            if value and value not in tables["field"]:
                error("unknown '%s' value '%s'" % (field, value))

    for table in fields:
        for field in fields[table]:
            if field not in tables["schema-field"][table]:
                error("unexpected field '%s' in table '%s'" % (field, table))

    check_typologies()
    check_themes()
    check_datasets()
    check_project_status()

    if errors > 0:
        sys.exit(1)
