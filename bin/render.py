#!/usr/bin/env python3

import os
import csv
import shutil
import jinja2
import importlib
import frontmatter

from glob import glob
from digital_land_frontend.jinja import setup_jinja
from markdown import Markdown
from markupsafe import Markup

specification_svg = importlib.import_module("specification-svg")

docs = "docs/"
content = "content/"
staticPath = "https://digital-land.github.io"
assetPath = "https://digital-land.github.io"
specification_repo_url = "/specification"

keys = {
    "dataset-field": ["dataset", "field"],
    "datapackage-dataset": ["datapackage", "dataset"],
}
tables = {
    "datapackage": {},
    "datapackage-dataset": {},
    "datatype": {},
    "field": {},
    "typology": {},
    "dataset": {},
    "dataset-field": {},
    "specification": {},
    "specification-status": {},
}


def render(path, template, docs="docs", **kwargs):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, "w") as f:
        print(f"creating {path}")
        f.write(template.render(**kwargs))


def load_csv(table):
    for row in csv.DictReader(open(f"specification/{table}.csv", newline="")):
        if table not in keys:
            key = table
            tables[table][row[key]] = row
        else:
            pkey, skey = keys[table]
            tables[table].setdefault(row[pkey], {})
            tables[table][row[pkey]][row[skey]] = row


def load_content(table):
    for path in glob(f"content/{table}/*.md"):
        post = frontmatter.load(path)
        tables[table][post[table]] = post


def field_typology(f):
    if f["parent-field"] == "" or f["field"] == f["parent-field"]:
        return f["parent-field"]

    return field_typology(tables["field"][f["parent-field"]])


def index_typologies():
    tables["typology-datatype"] = {}
    tables["typology-field"] = {}
    tables["typology-dataset"] = {}
    for field, f in tables["field"].items():
        typology = field_typology(f)
        tables["field"][field]["typology"] = typology
        tables["typology-field"].setdefault(typology, [])
        tables["typology-field"][typology].append(field)

        datatype = f["datatype"]
        tables["typology-datatype"].setdefault(typology, [])
        if datatype not in tables["typology-datatype"][typology]:
            tables["typology-datatype"][typology].append(datatype)

        if field in tables["dataset"]:
            tables["typology-dataset"].setdefault(typology, [])
            tables["typology-dataset"][typology].append(field)


def index_datatype():
    tables["datatype-field"] = {}
    tables["datatype-dataset"] = {}
    for field, f in tables["field"].items():
        datatype = f["datatype"]
        tables["datatype-field"].setdefault(datatype, [])
        tables["datatype-field"][datatype].append(field)

        if field in tables["dataset"]:
            tables["datatype-dataset"].setdefault(datatype, [])
            tables["datatype-dataset"][datatype].append(field)


def base_field(field):
    f = tables["field"][field]
    if f["cardinality"] == "1":
        return field
    return f["parent-field"]


def index_dataset():
    tables["dataset-datapackage"] = {}
    for datapackage, d in tables["datapackage-dataset"].items():
        for dataset in d:
            tables["dataset-datapackage"].setdefault(dataset, [])
            tables["dataset-datapackage"][dataset].append(datapackage)

    tables["dataset-to"] = {}
    tables["dataset-from"] = {}
    for dataset, s in tables["dataset-field"].items():
        for name in s:
            field = base_field(name)
            if field != dataset and field in tables["dataset"]:
                tables["dataset-to"].setdefault(dataset, [])
                if field not in tables["dataset-to"][dataset]:
                    tables["dataset-to"][dataset].append(field)

                tables["dataset-from"].setdefault(field, [])
                if dataset not in tables["dataset-from"][field]:
                    tables["dataset-from"][field].append(dataset)


def index_field():
    tables["field-dataset"] = {}
    for dataset, s in tables["dataset-field"].items():
        for field in s:
            tables["field-dataset"].setdefault(field, [])
            tables["field-dataset"][field].append(dataset)


def index_datapackage():
    tables["field-datapackage"] = {}
    for datapackage, d in tables["datapackage-dataset"].items():
        for dataset in d:
            for field in tables["dataset-field"][dataset]:
                tables["field-datapackage"].setdefault(field, [])
                if datapackage not in tables["field-datapackage"][field]:
                    tables["field-datapackage"][field].append(datapackage)


def index_specification():
    return


def default_names():
    for dataset, s in tables["dataset"].items():
        if not s.get("key-field", ""):
            s["key-field"] = dataset
        if not s.get("name", ""):
            s["name"] = tables["field"][dataset]["name"]
        if not s.get("description", "") and dataset in tables["field"]:
            s["description"] = tables["field"][dataset]["description"]


def dataset_sort(dataset):
    fields = sorted(tables["dataset-field"][dataset])
    if dataset in fields:
        fields.pop(fields.index(dataset))
        fields = [dataset] + fields
    # move default register fields to end, order is same as in list
    for field in ["entry-date", "start-date", "end-date"]:
        fields.append(fields.pop(fields.index(field)))
    return fields


if __name__ == "__main__":
    env = setup_jinja()

    md = Markdown()
    env.filters["markdown"] = lambda text: Markup(
        md.convert(text)
        .replace("<p>", '<p class="govuk-body">')
        .replace("<ul>", '<ul class="govuk-list govuk-list--bullet">')
    )
    env.filters["commanum"] = lambda v: "{:,}".format(v)
    env.filters["dataset_sort"] = dataset_sort

    for table in tables:
        if table in ["specification"]:
            load_content(table)
        else:
            load_csv(table)

    default_names()
    index_typologies()
    index_datatype()
    index_field()
    index_dataset()
    index_datapackage()
    index_specification()


    def version_exists(parent_dir, version):
        version_dir = os.path.join(parent_dir, version)
        # Check if the directory_to_check exists within the parent_directory
        if os.path.exists(parent_dir) and os.path.exists(version_dir):
            # Check if directory_to_check is a subdirectory of parent_directory
            if os.path.commonpath([parent_dir, version_dir]) == parent_dir:
                return True
        return False


    # generate versions of specification and dataset pages
    for template in ["specification"]:
        for name, item in tables[template].items():
            # only if version in frontmatter
            if 'version' in item.metadata:
                latest_version = item.metadata['version']
                parent_dir = os.path.join(docs, template, name)
                if not version_exists(parent_dir, f'v{latest_version}'):
                    # render the html page
                    version_dir = f"{template}/{name}/v{latest_version}"
                    render(
                        f"{version_dir}/index.html",
                        env.get_template(f"{template}.html"),
                        name=name,
                        item=item,
                        tables=tables,
                        staticPath=staticPath,
                        assetPath=assetPath,
                        sectionPath=f"{specification_repo_url}/{template}",
                        version=f'v{latest_version}'
                    )
                    # make a copy of .md
                    source_file = os.path.join(content, template, f'{name}.md')
                    try:
                        shutil.copy(source_file, os.path.join(docs, version_dir))
                    except Exception as e:
                        print(f"An error occurred: {e}")
                    # generate svg for the version
                    diagram_version_path = os.path.join(docs, version_dir, "diagram.svg")
                    specification_svg.generate(source_file, diagram_version_path)



    for template in ["datapackage", "dataset", "field", "datatype", "specification", "typology"]:
        for name, item in tables[template].items():
            if name in ["Deliverable", "Hectares", "Notes"]:
                print(f"skipping deprecated field: {name}")
                continue
            versions = []
            if template == "specification":
                specification_dir = os.path.join(docs, template, name)
                versions = [v for v in os.listdir(specification_dir) if os.path.isdir(os.path.join(specification_dir, v))]
                versions.sort(reverse=True)
            render(
                f"{template}/{name}/index.html",
                env.get_template(f"{template}.html"),
                name=name,
                item=item,
                tables=tables,
                staticPath=staticPath,
                assetPath=assetPath,
                sectionPath=f"{specification_repo_url}/{template}",
                versions=versions
            )

    for path, template in [
        ("index.html", "indexes.html"),
        ("datapackage/index.html", "datapackages.html"),
        ("dataset/index.html", "datasets.html"),
        ("field/index.html", "fields.html"),
        ("datatype/index.html", "datatypes.html"),
        ("typology/index.html", "typologies.html"),
        ("specification/index.html", "specifications.html"),
        ("specification/diagrams.html", "diagrams.html"),
    ]:
        render(
            path,
            env.get_template(template),
            tables=tables,
            staticPath=staticPath,
            assetPath=assetPath,
        )
