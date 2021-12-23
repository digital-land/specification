#!/usr/bin/env python3

#  check integrity of specification CSV files

import sys
import csv
from decimal import Decimal

dialect = csv.excel
dialect.strict = True

keys = {
    "dataset-field": ["dataset", "field"],
    # "datapackage-dataset": ["datapackage", "dataset"],
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
    "collection": {},
    "dataset": {},
    "project": {},
    "project-status": {},
    "typology": {},
    "theme": {},
    "dataset-field": {},
    "datapackage": {},
    # "datapackage-dataset": {},
}

empty_reference = {"collection"}

errors = 0
warnings = 0


def error(s):
    global errors
    print("[ERROR]: " + s, file=sys.stderr)
    errors += 1


def warning(s):
    global warnings
    print("[WARNING]: " + s, file=sys.stderr)
    warnings += 1


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
            if value and table not in empty_reference:
                error("%s: unknown '%s' value '%s'" % (table, field, value))


def field_typology(f):
    if f["parent-field"] == "" or f["field"] == f["parent-field"]:
        return f["parent-field"]

    if f["parent-field"] not in tables["field"]:
        error("%s: unknown parent-field '%s'" % (f["field"], f["parent-field"]))
        return ""

    return field_typology(tables["field"][f["parent-field"]])


def check_field_typology():
    for field, f in tables["field"].items():
        typology = field_typology(f)
        if typology != f.get("typology", ""):
            error(
                "field '%s' has typology '%s' parent-field is '%s'"
                % (field, f.get("typology", ""), typology)
            )
        if typology not in tables["typology"]:
            error("field '%s' has an unknown typology '%s'" % (field, typology))


def check_datasets():
    for dataset, d in tables["dataset"].items():
        if not d.get("plural", ""):
            error("dataset '%s' missing plural" % (dataset))

        typology = d.get("typology", "")
        if typology == "" or typology not in tables["typology"]:
            error("dataset '%s' has an unknown typology '%s'" % (dataset, typology))

        # typology datasets don't have a theme:
        if dataset not in tables["typology"]:
            for theme in d["themes"].split(";"):
                if theme not in tables["theme"]:
                    error("dataset '%s' has an unknown theme '%s'" % (dataset, theme))

        # check entity ranges .. O(n2)
        if "specification" != d["typology"] and "entity" != dataset:
            minimum = Decimal(d.get("entity-minimum", "") or 0)
            if not minimum:
                error("dataset '%s' is missing an entity-minimum value" % (dataset))

            maximum = Decimal(d.get("entity-maximum", "") or 0)
            if not maximum:
                error("dataset '%s' is missing an entity-maximum value" % (dataset))

            if minimum and maximum:
                for _dataset, _d in tables["dataset"].items():
                    _minimum = Decimal(_d.get("entity-minimum", "") or 0)
                    _maximum = Decimal(_d.get("entity-maximum", "") or 0)
                    if (
                        _dataset != dataset
                        and _minimum
                        and _maximum
                    ):
                        if (
                            minimum <= _minimum <= maximum
                            or minimum <= _maximum <= maximum
                        ):
                            error(
                                "dataset '%s' entity range [%d,%d] overlaps with '%s' [%d,%d]"
                                % (dataset, minimum, maximum, _dataset, _minimum, _maximum)
                            )


def check_projects():
    for project, p in tables["project"].items():
        for dataset in p["datasets"].split(";"):
            if dataset and dataset not in tables["dataset"]:
                error("project '%s' has an unknown dataset '%s'" % (project, dataset))

        for status in p["project-status"].split(";"):
            if status not in tables["project-status"]:
                error(
                    "project '%s' has an unknown project-status '%s'"
                    % (project, status)
                )


def check(table):
    if table not in tables["dataset"]:
        return error("no dataset for table %s" % (table))

    if table not in tables["dataset-field"]:
        return error("no dataset-field values for table %s" % (table))

    for field in fields[table]:
        if field not in tables["field"]:
            return error("%s: column '%s' not defined as a field" % (table, field))

    for field in tables["dataset-field"][table]:
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

    for t in ["dataset", "field", "datatype", "typology"]:
        for name, item in tables[t].items():
            if (not item.get("name", "")) and (
                t == "dataset"
                and not (
                    name in tables["field"] and tables["field"][name].get("name", "")
                )
            ):
                error("no name for %s '%s'" % (t, name))

    for dataset, d in tables["dataset"].items():
        if dataset not in tables["dataset-field"]:
            error("no fields for dataset '%s'" % (dataset))
        else:
            for field in mandatory_fields:
                if field not in tables["dataset-field"][dataset]:
                    error("dataset '%s' missing '%s' field" % (dataset, field))

    for key, row in tables["field"].items():
        if not row.get("name", ""):
            error("no name for field '%s'" % (key))
        for field in ["parent-field", "replacement-field"]:
            value = row.get(field)
            if value and value not in tables["field"]:
                error("unknown '%s' value '%s'" % (field, value))

    for table in fields:
        for field in fields[table]:
            if field not in tables["dataset-field"][table]:
                error("unexpected field '%s' in table '%s'" % (field, table))

    check_field_typology()
    check_datasets()
    check_projects()

    if errors > 0:
        sys.exit(1)
