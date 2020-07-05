#!/usr/bin/env python3

#  check integrity of specification CSV files

import sys
import csv

dialect = csv.excel
dialect.strict = True

keys = {
    "schema-field": ["schema", "field"],
    "dataset-schema": ["dataset", "schema"],
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
    "typology": {},
    "schema-field": {},
    "dataset-schema": {},
}

errors = 0


def error(s):
    global errors
    print("[ERROR]: " + s, file=sys.stderr)
    errors += 1


def load(table):
    reader = csv.DictReader(
        open("specification/%s.csv" % (table), newline=""), dialect=dialect
    )
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
    if  f["parent-field"] == "" or f["field"] == f["parent-field"]:
        return f["parent-field"]

    return field_typology(tables["field"][f["parent-field"]])


def check_typologies():
    for field, f in tables["field"].items():
        typology = field_typology(f)
        if typology and typology not in tables["typology"]:
            error("field '%s' has an unknown typology '%s'" % (field, typology))


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

    for schema in tables["schema"]:
        if schema not in tables["schema-field"]:
            error("no fields for schema '%s'" % (schema))
        else:
            for field in mandatory_fields:
                if field not in tables["schema-field"][schema]:
                    error("schema '%s' missing '%s' field" % (schema, field))

    for key, row in tables["field"].items():
        for field in ["parent-field", "replacement-field"]:
            value = row.get(field)
            if value and value not in tables["field"]:
                error("unknown '%s' value '%s'" % (field, value))

    check_typologies()

    if errors > 0:
        sys.exit(1)
