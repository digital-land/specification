#!/usr/bin/env python3

#  check integrity of specification CSV files

import sys
import csv
import json
from decimal import Decimal

dialect = csv.excel
dialect.strict = True

keys = {
    "dataset-field": ["dataset", "field"],
    "specification-field": ["specification", "dataset", "field"],
    # "datapackage-dataset": ["datapackage", "dataset"],
}

fields = {}
mandatory_fields = [
    "entry-date",
    "start-date",
    "end-date",
]

dataset_expected_fields = ["entity", "prefix", "reference", "notes"]

# datasets
key_field = {"reference": []}

tables = {
    "field": {},
    "datatype": {},
    "collection": {},
    "dataset": {},
    "project": {},
    "project-status": {},
    "cohort": {},
    "intervention": {},
    "award": {},
    "fund": {},
    "specification": {},
    "specification-field": {},
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
            # TBD: use dataset key-field
            if "reference" in row:
                tables[table][row["reference"]] = row
            else:
                # TBD: migrate away from table name being key field
                tables[table][row[table]] = row
        elif len(keys[table]) == 2:
            pkey, skey = keys[table]
            tables[table].setdefault(row[pkey], {})
            tables[table][row[pkey]][row[skey]] = row
        elif len(keys[table]) == 3:
            pkey, skey, tkey = keys[table]
            tables[table].setdefault(row[pkey], {})
            tables[table][row[pkey]].setdefault(row[skey], {})
            tables[table][row[pkey]][row[skey]][row[tkey]] = row
        else:
            raise ValueError("unexpected number of key fields")


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
    print("Checking datasets...")
    for dataset, d in tables["dataset"].items():
        if not d.get("version"):
            error("dataset '%s' missing version number" % (dataset))

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
        if (
            "entity" in tables["dataset-field"][dataset]
            and dataset not in ["entity", "old-entity", "fact", "lookup", "reference"]
            and dataset != typology
        ):
            minimum = Decimal(d.get("entity-minimum", "") or 0)
            maximum = Decimal(d.get("entity-maximum", "") or 0)

            if not (minimum == 0 and maximum == 0):
                if not minimum:
                    error("dataset '%s' is missing an entity-minimum value" % (dataset))

                if not maximum:
                    error("dataset '%s' is missing an entity-maximum value" % (dataset))

                entity_range = maximum - minimum + 1
                if entity_range < 0:
                    error(
                        f"dataset '{dataset}' entity-maximum {maximum} less than entity-minimum '{minimum}'"
                    )
                elif entity_range % 100 != 0:
                    error(
                        f"dataset '{dataset}' entity range '{entity_range}' should be a multiple of 100"
                    )

            if minimum and maximum:
                for _dataset, _d in tables["dataset"].items():
                    _minimum = Decimal(_d.get("entity-minimum", "") or 0)
                    _maximum = Decimal(_d.get("entity-maximum", "") or 0)
                    if (
                        _dataset != dataset
                        and _minimum
                        and _maximum
                        and _d["end-date"] == ""
                    ):

                        if (
                            minimum <= _minimum <= maximum
                            or minimum <= _maximum <= maximum
                        ):
                            error(
                                "dataset '%s' entity range [%d,%d] overlaps with '%s' [%d,%d]"
                                % (
                                    dataset,
                                    minimum,
                                    maximum,
                                    _dataset,
                                    _minimum,
                                    _maximum,
                                )
                            )


def check_projects():
    for project, p in tables["project"].items():
        for specification in p["specifications"].split(";"):
            if specification and specification not in tables["specification"]:
                error(
                    "project '%s' has an unknown specification '%s'"
                    % (project, specification)
                )

        for status in p["project-status"].split(";"):
            if status not in tables["project-status"]:
                error(
                    "project '%s' has an unknown project-status '%s'"
                    % (project, status)
                )


def check_cohorts():
    for cohort, c in tables["cohort"].items():
        if c["intervention"] and c["intervention"] not in tables["intervention"]:
            error(
                f"cohort '{cohort}' has an unknown intervention '{c['intervention']}'"
            )


def check_specification_fields():
    for specification, s in tables["specification-field"].items():
        for dataset, d in s.items():
            if dataset not in tables["dataset"]:
                error(
                    "specificaton '%s' has an unknown dataset '%s'"
                    % (specification, dataset)
                )
            if not d:
                error(
                    "specificaton '%s' dataset '%s' has no fields"
                    % (specification, dataset)
                )
                continue

            for field, f in d.items():
                field = f.get("dataset-field", f["field"])
                if field not in tables["field"]:
                    error(
                        "specificaton '%s' dataset '%s' has unknown field '%s'"
                        % (specification, dataset, field)
                    )
                    continue
                # check field is in referenced datasets
                if f["datasets"]:
                    for sub in f["datasets"].split(';'):
                        if field not in tables["dataset-field"].get(sub, []):
                            error(
                                f"specificaton '{specification}' dataset '{dataset}' field {field} not in sub-dataset '{sub}'"
                            )
                elif field not in tables["dataset-field"].get(dataset, []):
                    error(
                        f"specificaton '{specification}' dataset '{dataset}' field {field} not in dataset '{dataset}'"
                    )


def check_specifications():
    check_specification_fields()


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
    elif len(keys[table]) == 2:
        for pkey in tables[table]:
            for key, row in tables[table][pkey].items():
                for field, value in row.items():
                    check_reference(table, field, value)
    else:
        for pkey in tables[table]:
            for skey in tables[table][pkey]:
                for tkey in tables[table][pkey][skey]:
                    for field, value in tables[table][pkey][skey][tkey].items():
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

    # TBD: review this thinking ..
    for dataset, d in tables["dataset"].items():
        if dataset not in tables["dataset-field"]:
            error("no fields for dataset '%s'" % (dataset))
        else:
            for field in mandatory_fields:
                if field not in tables["dataset-field"][dataset]:
                    error("dataset '%s' missing '%s' field" % (dataset, field))

            if d["realm"] in ["dataset"]:
                for field in dataset_expected_fields:
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
    check_cohorts()
    check_specifications()

    if errors > 0:
        sys.exit(1)
