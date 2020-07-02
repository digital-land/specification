#!/usr/bin/env python3

#  check integrity of specification CSV files

import sys
import csv


errors = 0
schema = {}


def load(name, fields=[]):
    global errors
    schema.setdefault(name, {})
    for row in csv.DictReader(open("specification/%s.csv" % (name))):
        schema[name][row[name]] = row
        for field in fields:
            if row[field] not in schema[field]:
                print("%s: unknown %s '%s'" % (name, field, row[field]), file=sys.stderr)
                errors += 1


load("datatype")
load("field", ["datatype"])

if errors > 0:
    sys.exit(1)
