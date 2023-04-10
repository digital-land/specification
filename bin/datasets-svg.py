#!/usr/bin/env python3

import sys
import csv
from pathlib import Path


tables = {
    "dataset": {},
    "field": {},
}

for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    tables["dataset"][row["dataset"]] = row

for row in csv.DictReader(open("specification/dataset-field.csv", newline="")):
    tables["dataset"][row["dataset"]].setdefault("fields", [])
    tables["dataset"][row["dataset"]]["fields"].append(row["field"])

for row in csv.DictReader(open("specification/field.csv", newline="")):
    tables["field"][row["field"]] = row


def field_datatype(field):
    f = tables["field"][field]

    if f["replacement-field"]:
        field = f["replacement-field"]
        f = tables["field"][field]

    if field in ["organisation", "geography"]:
        # references which also need the prefix
        datatype = "curie"
    elif field in tables["dataset"] and field not in ["reference", "geometry"]:
        # references which can default the prefix value, either from the field or within the organisation
        datatype = "reference"
    else:
        datatype = f["datatype"]

    # indicate cardinality with a *
    if f["cardinality"] == "n":
        return field_datatype(f["parent-field"]) + "*"
    else:
        return datatype


def svg_rect(c, X, Y, h, v):
    return f'<rect x="{X}" y="{Y}" width="{h}" height="{v}" class="{c}"/>'


def svg_text(c, text, X, Y):
    return f'<text x="{X}" y="{Y}" class="{c}">{text}</text>'


def svg_spline(c, from_x, from_y, to_x, to_y):
    mid_x = min(from_x, to_x) + abs(from_x - to_x) / 2
    return (
        f'<path class="{c}" fill="none" stroke-width="2"'
        f' marker-start="url(#start-dot)" marker-end="url(#end-dot)"'
        f' d="M {from_x} {from_y} C {mid_x} {from_y} {mid_x} {to_y} {to_x} {to_y}"/>'
    )


def sort_fields(dataset):
    fields = sorted(tables["dataset-field"][dataset])
    for field in ["dataset", "prefix", "reference", "entity", "name", "description"]:
        fields.append(fields.pop(fields.index(field)))

    # move default register fields to end, order is same as in list
    for field in ["documentation-url", "document-url", "notes", "organisation", "entry-date", "start-date", "end-date"]:
        fields.append(fields.pop(fields.index(field)))
    return fields


row_height = 20
text_y = int(row_height / 2)
padding = 5

field_width = 162
datatype_width = 55
gap = 80

row_width = field_width + datatype_width


datasets = tables["dataset"].keys()
maxrows = max([len(d["fields"]) for dataset, d in tables["dataset"].items()])
ndatasets = len(datasets)
ngaps = ndatasets - 1
canvas_width = ndatasets * row_width + ngaps * gap
canvas_height = (maxrows + 1) * row_height

X = 0
points = {}
links = []
boxes = []

for dataset, d in tables["dataset"].items():

    Y = 0
    box = []
    box.append(svg_rect("name", X, Y, row_width, row_height))
    box.append(svg_text("name", dataset, X + int(row_width / 2), Y + text_y))

    for field in tables["dataset"][dataset]["fields"]:
        datatype = field_datatype(field)

        Y = Y + row_height

        box.append(svg_rect("field", X, Y, field_width, row_height))
        box.append(svg_rect("datatype", X + field_width, Y, datatype_width, row_height))

        box.append(svg_text("field", field, X + padding, Y + text_y))
        box.append(
            svg_text("datatype", datatype, X + field_width + padding, Y + text_y)
        )

        points[f"from:{dataset}:{field}"] = (X, Y + text_y)
        points[f"to:{dataset}:{field}"] = (X + row_width, Y + text_y)

        if field in datasets:
            link_dataset = field

        # TBD: key field should be defined in the dataset.md
        if link_dataset in datasets:
            if link_dataset in ["attribution", "checksum", "collection", "column", "dataset", "datapackage", "dataset-schema", "datatype", "endpoint", "fact", "field", "issue-type", "licence", "prefix", "project", "project-status", "provenance", "provision-reason", "resource", "severity", "schema", "specification", "specification-status", "source", "theme", "typology"]:
                key = link_dataset
            elif link_dataset == "old-entity":
                key = "entity"
            elif link_dataset == "old-resource":
                key = "resource"
            else:
                key = "reference"

            links.append(
                {
                    "from": f"from:{dataset}:{field}",
                    "to": f"to:{link_dataset}:{key}",
                }
            )

    boxes.append(box)

    X = X + row_width + gap


print(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}">'
)
print(
    """<defs>
<style>
text{font-family:sans-serif; font-size:10px; dominant-baseline:middle;}
text.name{fill:#fff;font-weight:700;text-anchor:middle}
rect.name{fill:#0b0c0c; stroke:#0b0c0c;}
rect{fill:#fff;stroke:#b1b4b6;}
text.field{fill:#0b0c0c;}
text.datatype{fill:#0b0c0c;}
.line{stroke:#0b0c0c;}
</style>
<marker id="start-dot" markerWidth="6" markerHeight="6" refX="4" refY="3" markerUnits="strokeWidth">
  <circle cx="3" cy="3" r="2" fill="#fff" stroke="#0b0c0c"/>
</marker>
<marker id="end-dot" markerWidth="6" markerHeight="6" refX="2" refY="3" markerUnits="strokeWidth">
  <circle cx="3" cy="3" r="2" fill="#0b0c0c" />
</marker>
</defs>"""
)

for l in links:
    print(svg_spline("line", *points[l["from"]], *points[l["to"]]))

for box in boxes:
    print("<g>")
    print("\n".join(box))
    print("</g>")

print("</svg>")
