#!/usr/bin/env python3

import os
import os.path
import jinja2
import csv
import markdown

docs = "docs/"

keys = {
    "schema-field": ["schema", "field"],
    "dataset-schema": ["dataset", "schema"],
}
tables = {
    "dataset": {},
    "dataset-schema": {},
    "datatype": {},
    "field": {},
    "typology": {},
    "schema": {},
    "schema-field": {},
}


def render(template, path):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(env.get_template(template).render(tables=tables))


def load(table):
    for row in csv.DictReader(open("specification/%s.csv" % (table), newline="")):
        if table not in keys:
            key = table
            tables[table][row[key]] = row
        else:
            pkey, skey = keys[table]
            tables[table].setdefault(row[pkey], {})
            tables[table][row[pkey]][row[skey]] = row


def field_typology(f):
    if  f["parent-field"] == "" or f["field"] == f["parent-field"]:
        return f["parent-field"]

    return field_typology(tables["field"][f["parent-field"]])


def index_typologies():
    for field, f in tables["field"].items():
        tables["field"][field]["typology"] = field_typology(f)


if __name__ == "__main__":
    loader = jinja2.FileSystemLoader(searchpath="./templates")
    env = jinja2.Environment(loader=loader)

    md = markdown.Markdown()
    env.filters["markdown"] = lambda text: jinja2.Markup(md.convert(text).replace("<p>", '<p class="govuk-body">'))
    env.filters['commanum'] = lambda v: "{:,}".format(v)

    for table in tables:
        load(table)

    index_typologies()

    render("specifications.html", "index.html")
    render("datatypes.html", "datatype/index.html")
    render("fields.html", "field/index.html")
