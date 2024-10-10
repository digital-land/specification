#!/usr/bin/env python3

import sys
import csv
from pathlib import Path

tables = {
    "dataset": {},
    "dataset-field": {},
    "field": {},
}

skip_links = [
    "geography",
    "company",
    "local-authority-type",
    "local-resilience-forum",
    "local-resilience-forum-boundary",
    "local-planning-authority",
    "local-authority-district",
    "national-park",
    "region",
]

realms = {
    "dataset": ["organisation"],
    "collection": [],
    "specification": [],
    "pipeline": [],
    "provenance": [],
    "entity": [],
    "configuration":[],
    "log":[]
}

for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    tables["dataset"][row["dataset"]] = row

for row in csv.DictReader(open("specification/dataset-field.csv", newline="")):
    dataset = row["dataset"]
    tables["dataset-field"].setdefault(dataset, {})
    tables["dataset-field"][dataset][row["field"]] = row

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


def svg_spline(c, _id, title, from_x, from_y, to_x, to_y, gap_x):
    if from_x == to_x:
        mid_x = from_x + gap_x / 2
    else:
        mid_x = min(from_x, to_x) + abs(from_x - to_x) / 2

    return (
        f'<path class="{c}" id="{_id}" fill="none" stroke-width="2"'
        f' marker-start="url(#start-dot)" marker-end="url(#end-dot)"'
        f' d="M {from_x} {from_y} C {mid_x} {from_y} {mid_x} {to_y} {to_x} {to_y}">'
        f"<title>{title}</title>"
        f"</path>"
    )


def sort_fields(fields):
    upfront = ["dataset", "prefix", "reference", "entity", "name", "description"]
    upfront.reverse()
    for field in upfront:
        if field in fields:
            fields.pop(fields.index(field))
            fields = [field] + fields

    # move default register fields to end, order is same as in list
    for field in [
        "geometry",
        "point",
        "documentation-url",
        "document-url",
        "notes",
        "organisation",
        "entry-date",
        "start-date",
        "end-date",
    ]:
        if field in fields:
            fields.append(fields.pop(fields.index(field)))
    return fields


row_height = 20
text_y = int(row_height / 2)
padding = 5

field_width = 162
datatype_width = 55
x_gap = 80
y_gap = 80

row_width = field_width + datatype_width

datasets = tables["dataset"].keys()

X = x_gap
points = {}
links = []
boxes = []
max_Y = 0

for realm in realms:
    Y = 0
    for dataset, d in tables["dataset"].items():
        if d["realm"] != realm or realms[realm] and dataset not in realms[realm]:
            continue

        box = []
        box.append(svg_rect("name", X, Y, row_width, row_height))
        box.append(svg_text("name", dataset, X + int(row_width / 2), Y + text_y))

        fields = list(tables["dataset-field"][dataset].keys())
        for field in sort_fields(fields):
            datatype = field_datatype(field)

            Y = Y + row_height

            box.append(svg_rect("field", X, Y, field_width, row_height))
            box.append(
                svg_rect("datatype", X + field_width, Y, datatype_width, row_height)
            )

            box.append(svg_text("field", field, X + padding, Y + text_y))
            box.append(
                svg_text("datatype", datatype, X + field_width + padding, Y + text_y)
            )

            points[f"{dataset}_{field}"] = (X, Y + text_y)

            link_dataset = (
                tables["field"][field].get("dataset", "")
                or tables["dataset-field"][dataset][field].get("field-dataset", "")
                or field
            )

            # TBD: key field should be defined in the dataset.md
            # TBD: links to come from a field-dataset.csv of generated links
            if link_dataset in datasets:
                link_field = (
                    tables["dataset"][link_dataset].get("key-field", "") or "reference"
                )
                if not (dataset == link_dataset and field == link_field):
                    links.append(
                        {
                            "from": f"{dataset}_{field}",
                            "to": f"{link_dataset}_{link_field}",
                        }
                    )

        boxes.append(box)
        Y = Y + y_gap

    if Y > max_Y:
        max_Y = Y

    X = X + row_width + x_gap


ncols = len(realms)
ngaps = ncols + 2
canvas_width = ncols * row_width + ngaps * x_gap
canvas_height = max_Y

print(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}">'
)
print(
    """<defs>
<style>
text{font-family:sans-serif; font-size:10px; dominant-baseline:middle;}
text.name{fill:#fff;font-weight:700;text-anchor:middle}
rect.name{fill:#0b0c0c; stroke:#0b0c0c;}
rect{fill:#fff;stroke:#b1b4b6; opacity: 0.8;}
text.field{fill:#0b0c0c;}
text.datatype{fill:#0b0c0c;}
.line{stroke:#000; opacity:0.2;}
.line:hover{stroke:#f00; opacity:1;}
</style>
<marker id="start-dot" markerWidth="6" markerHeight="6" refX="3" refY="3" markerUnits="strokeWidth">
  <circle cx="3" cy="3" r="2" fill="#fff" stroke="#0b0c0c"/>
</marker>
<marker id="end-dot" markerWidth="6" markerHeight="6" refX="3" refY="3" markerUnits="strokeWidth">
  <circle cx="3" cy="3" r="2" fill="#0b0c0c" />
</marker>
</defs>"""
)

for l in links:
    if l["to"].removesuffix("_reference") in skip_links:
        continue

    from_x, from_y = points[l["from"]]
    to_x, to_y = points[l["to"]]

    if to_x == from_x:
        from_x = from_x + row_width
        to_x = to_x + row_width
    elif to_x > from_x:
        from_x = from_x + row_width
    else:
        to_x = to_x + row_width

    _id = f'from_{l["from"]}_to_{l["to"]}'
    title = _id.replace("_", " ")
    print(svg_spline("line", _id, title, from_x, from_y, to_x, to_y, x_gap))

for box in boxes:
    print("<g>")
    print("\n".join(box))
    print("</g>")

print("</svg>")
