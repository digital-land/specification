#!/usr/bin/env python3

import sys
import csv
from digital_land.specification import Specification

spec = Specification()

org_fields = {
    "billing-authority",
    "combined-authority",
    "company",
    "end-date",
    "entity",
    "entry-date",
    "name",
    "opendatacommunities-area",
    "opendatacommunities-organisation",
    "organisation",
    "region",
    "start-date",
    "statistical-geography",
    "twitter",
    "website",
    "wikidata",
    "wikipedia",
}

la_fields = {
    "addressbase-custodian",
    "esd-inventory",
    "local-authority-type",
    "local-resilience-forum",
}

w = csv.DictWriter(open("/tmp/schema-field.csv", "w"), fieldnames=["schema", "field"])
w.writeheader()

for schema in sorted(spec.schema):
    fields = set(spec.schema_field[schema])
    if schema in spec.field:
        if spec.field_typology(schema) == "organisation":
            fields = fields.union(org_fields)

        if schema == "local-authority-eng":
            fields = fields.union(la_fields)

    for field in sorted(list(fields)):
        row = { "schema": schema, "field": field }
        w.writerow(row)
