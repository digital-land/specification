#!/usr/bin/env python3

#  check integrity of specification CSV files

import sys
import csv

dialect = csv.excel
dialect.strict = True

errors = 0
schema = {}


def check(name, field, value, lineno):
    global errors
    if value not in schema[field]:
        print("[ERROR] %s: line %d unknown %s '%s'" % (name, lineno, field, value), file=sys.stderr)
        errors += 1


def load(name, fields=[], key=None, lineno=1):
    if not key:
        key = name
    schema.setdefault(name, {})
    for row in csv.DictReader(open("specification/%s.csv" % (name), newline=""), dialect=dialect):
        schema[name][row[key]] = row

        if lineno == 1:
            for field in row:
                check(name, "field", field, lineno)

        lineno += 1

        for field in fields:
            check(name, field, row[field], lineno)


load("field", lineno=2)
load("datatype")
load("field", ["datatype"])
load("schema", ["field"])
load("dataset")

# key could come from schema.csv field ..

load("schema-field", ["schema", "field"], key="schema")
load("dataset-schema", ["dataset", "schema"], key="dataset")

if errors > 0:
    sys.exit(1)
