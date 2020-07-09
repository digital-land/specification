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


def render(template, path, name=None, item=None):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(env.get_template(template).render(tables=tables, name=name, item=item))


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
    if f["parent-field"] == "" or f["field"] == f["parent-field"]:
        return f["parent-field"]

    return field_typology(tables["field"][f["parent-field"]])


def index_typologies():
    tables["typology-datatype"] = {}
    tables["typology-field"] = {}
    tables["typology-schema"] = {}
    for field, f in tables["field"].items():
        typology = field_typology(f)
        tables["field"][field]["typology"] = typology
        tables["typology-field"].setdefault(typology, [])
        tables["typology-field"][typology].append(field)

        datatype = f["datatype"]
        tables["typology-datatype"].setdefault(typology, [])
        if datatype not in tables["typology-datatype"][typology]:
            tables["typology-datatype"][typology].append(datatype)

        if field in tables["schema"]:
            tables["typology-schema"].setdefault(typology, [])
            tables["typology-schema"][typology].append(field)


def index_datatype():
    tables["datatype-field"] = {}
    tables["datatype-schema"] = {}
    for field, f in tables["field"].items():
        datatype = f["datatype"]
        tables["datatype-field"].setdefault(datatype, [])
        tables["datatype-field"][datatype].append(field)

        if field in tables["schema"]:
            tables["datatype-schema"].setdefault(datatype, [])
            tables["datatype-schema"][datatype].append(field)


def base_field(field):
    f = tables["field"][field]
    if f["cardinality"] == "1":
        return field
    return f["parent-field"]


def index_schema():
    tables["schema-dataset"] = {}
    for dataset, d in tables["dataset-schema"].items():
        for schema in d:
            tables["schema-dataset"].setdefault(schema, [])
            tables["schema-dataset"][schema].append(dataset)

    tables["schema-to"] = {}
    tables["schema-from"] = {}
    for schema, s in tables["schema-field"].items():
        for name in s:
            field = base_field(name)
            if field != schema and field in tables["schema"]:
                tables["schema-to"].setdefault(schema, [])
                if field not in tables["schema-to"][schema]:
                    tables["schema-to"][schema].append(field)

                tables["schema-from"].setdefault(field, [])
                if schema not in tables["schema-from"][field]:
                    tables["schema-from"][field].append(schema)


def index_field():
    tables["field-schema"] = {}
    for schema, s in tables["schema-field"].items():
        for field in s:
            tables["field-schema"].setdefault(field, [])
            tables["field-schema"][field].append(schema)


def index_dataset():
    tables["field-dataset"] = {}
    for dataset, d in tables["dataset-schema"].items():
        for schema in d:
            for field in tables["schema-field"][schema]:
                tables["field-dataset"].setdefault(field, [])
                if dataset not in tables["field-dataset"][field]:
                    tables["field-dataset"][field].append(dataset)


def default_names():
    for schema, s in tables["schema"].items():
        if not s.get("name", ""):
            s["name"] = tables["field"][schema]["name"]
        if not s.get("description", "") and schema in tables["field"]:
            s["description"] = tables["field"][schema]["description"]


if __name__ == "__main__":
    loader = jinja2.FileSystemLoader(searchpath="./templates")
    env = jinja2.Environment(loader=loader)

    md = markdown.Markdown()
    env.filters["markdown"] = lambda text: jinja2.Markup(
        md.convert(text)
        .replace("<p>", '<p class="govuk-body">')
        .replace("<ul>", '<ul class="govuk-list govuk-list--bullet">')
    )
    env.filters["commanum"] = lambda v: "{:,}".format(v)

    for table in tables:
        load(table)

    default_names()
    index_typologies()
    index_datatype()
    index_field()
    index_schema()
    index_dataset()

    for template in ["dataset", "schema", "field", "datatype", "typology"]:
        for name, item in tables[template].items():
            render(
                template + ".html", "%s/%s/index.html" % (template, name), name, item
            )

    render("specifications.html", "index.html")
    render("datasets.html", "dataset/index.html")
    render("schemas.html", "schema/index.html")
    render("fields.html", "field/index.html")
    render("datatypes.html", "datatype/index.html")
    render("typologies.html", "typology/index.html")
