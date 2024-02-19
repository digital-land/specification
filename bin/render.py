#!/usr/bin/env python3

from datetime import datetime
from functools import total_ordering
import os
import csv
from pathlib import Path
import shutil
import jinja2
import importlib
import frontmatter
import glob

from glob import glob
from digital_land_frontend.jinja import setup_jinja
from markdown import Markdown
from markupsafe import Markup

from typing import Dict, List


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


def get_changes(current_frontmatter, previous_frontmatter) -> Dict[str, List[str]]:
    changes = []
    for dataset in current_frontmatter.metadata["datasets"]:
        current_fields = set([field["field"] for field in dataset["fields"]])
        previous_dataset = [ds for ds in previous_frontmatter.metadata["datasets"] if ds["dataset"] == dataset["dataset"]]
        if previous_dataset:
            previous_dataset = previous_dataset[0]
            previous_fields = set([field["field"] for field in previous_dataset["fields"]])
            added_fields = list(current_fields - previous_fields)
            removed_fields = list(previous_fields - current_fields)
            # sort fields so that the changelog is consistent
            added_fields.sort()
            removed_fields.sort()
            if added_fields or removed_fields:
                changes.append({"dataset": dataset, "added": added_fields, "removed": removed_fields})

    current_datasets = set([ds["dataset"] for ds in current_frontmatter.metadata["datasets"]])
    previous_datasets = set([ds["dataset"] for ds in previous_frontmatter.metadata["datasets"]])
    datasets_added = list(current_datasets - previous_datasets)
    datasets_removed = list(previous_datasets - current_datasets)
    # sort datasets so that the changelog is consistent
    datasets_added.sort()
    datasets_removed.sort()

    return changes, {"added": datasets_added, "removed": datasets_removed}


@total_ordering
class Version:

    def __init__(self, version_str, version_date) -> None:
        self.version_str = version_str
        numbers = self.version_str.replace("v", "")
        major, minor, patch = numbers.split(".")
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)
        self.date = version_date

    def __eq__(self, other):
        self.major == other.major and self.minor == other.minor and self.patch == other.patch

    def __lt__(self, other):
        if self.major < other.major:
            return True
        elif self.major == other.major and self.minor < other.minor:
            return True
        elif (
            self.major == other.major
            and self.minor == other.minor
            and self.patch < other.patch
        ):
            return True
        else:
            return False


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

    placeholder_html = "<!-- [Replace with warning banner if version is updated] -->"
    replacement_html = '''
<div class="app-version-banner">
  <p class="govuk-body">There is a newer version of this specification. View the <a href=".." class="govuk-link">latest version</a>.</p>
</div>
'''

    # in old static version of specs, insert a banner
    def inject_version_banner(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        modified_content = html_content.replace(placeholder_html, replacement_html)

        # Update the HTML file with the modified content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

    def check_for_old_versions(specification_path, latest_version):
        for root, dirs, files in os.walk(specification_path):
            if root == specification_path:
                # Exclude the index.html file in the specification root
                if 'index.html' in files:
                    files.remove('index.html')
            if f'v{latest_version}' in dirs:
                # Exclude latest version directory
                 dirs.remove(f'v{latest_version}')
            for file_name in files:
                if file_name.endswith('.html'):
                    file_path = os.path.join(root, file_name)
                    inject_version_banner(file_path)


    # generate versions of specification and dataset pages
    for template in ["specification"]:
        for name, item in tables[template].items():
            # only if version in frontmatter
            if "version" in item.metadata:
                latest_version = item.metadata["version"]
                parent_dir = os.path.join(docs, template, name)
                check_for_old_versions(parent_dir, latest_version)
                if not version_exists(parent_dir, f"v{latest_version}"):
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
                        version=f"v{latest_version}",
                    )
                    # make a copy of .md
                    source_file = os.path.join(content, template, f"{name}.md")
                    try:
                        shutil.copy(source_file, os.path.join(docs, version_dir))
                    except Exception as e:
                        print(f"An error occurred: {e}")
                    # generate svg for the version
                    diagram_version_path = os.path.join(
                        docs, version_dir, "diagram.svg"
                    )
                    specification_svg.generate(source_file, diagram_version_path)
                    # make copy of new diagram.svg to unversioned directory - i.e. latest
                    parent_dir = Path(diagram_version_path).parent.parent
                    shutil.copy(diagram_version_path, parent_dir)

    for template in [
        "datapackage",
        "dataset",
        "field",
        "datatype",
        "specification",
        "typology",
    ]:
        for name, item in tables[template].items():
            if name in ["Deliverable", "Hectares", "Notes"]:
                print(f"skipping deprecated field: {name}")
                continue
            versions = []
            if template == "specification":
                specification_dir = os.path.join(docs, template, name)
                versions = [
                    v
                    for v in os.listdir(specification_dir)
                    if os.path.isdir(os.path.join(specification_dir, v))
                ]
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
                versions=versions,
            )

    # generated changelog pages
    for specification in tables["specification"]:
        specification_docs_dir = os.path.join(docs, "specification", specification)
        versions = glob(f"{specification_docs_dir}/v*", recursive=True)
        if len(versions) > 1:
            version_dates = {}
            version_numbers = []

            for version in versions:
                version_path = Path(version)
                version_date = datetime.fromtimestamp(version_path.stat().st_ctime)
                version_dates[version_path.name] = version_date
                version_numbers = [Version(Path(f).name, version_date) for f in versions]

            sorted_versions = sorted(version_numbers, reverse=True)
            changelog = []

            for i, current_version in enumerate(sorted_versions):
                if i + 1 < len(sorted_versions):
                    previous_version = sorted_versions[i + 1]
                    current_version_path = os.path.join(specification_docs_dir, current_version.version_str)
                    next_version_path = os.path.join(specification_docs_dir, previous_version.version_str)

                    with open(os.path.join(current_version_path, f"{specification}.md"), "r") as f:
                        current_frontmatter = frontmatter.load(f)

                    with open(os.path.join(next_version_path, f"{specification}.md"), "r") as f:
                        next_frontmatter = frontmatter.load(f)

                    dataset_field_changes, dataset_change = get_changes(current_frontmatter, next_frontmatter)
                    changelog.append({"current": current_version.version_str,
                                      "previous": previous_version.version_str,
                                      "changes": dataset_field_changes,
                                      "dataset_change": dataset_change})

            render(f"specification/{specification}/changelog.html",
                   env.get_template("changelog.html"),
                   specification=tables["specification"][specification].metadata,
                   changelog=changelog,
                   tables=tables,
                   staticPath=staticPath,
                   assetPath=assetPath,
                   sectionPath=f"{specification_repo_url}/specification")

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
