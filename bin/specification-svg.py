#!/usr/bin/env python3

import sys
import csv
from pathlib import Path
import frontmatter


def output_to_file(file_path, output_string):
    with open(file_path, "a") as file:
        file.write(output_string)


def generate(specification_path, output_path=None):
    svg_content = []

    tables = {
        "dataset": {},
        "field": {},
    }

    for row in csv.DictReader(open("specification/dataset.csv", newline="")):
        tables["dataset"][row["dataset"]] = row

    for row in csv.DictReader(open("specification/field.csv", newline="")):
        tables["field"][row["field"]] = row


    def field_datatype(field):
        f = tables["field"].get(field, None)

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
    
    def get_links(dataset, datasets):
        """
        Get links for a dataset.
        If the dataset has a field that is a reference to another dataset, return the link.
        If the field is a reference to a field in another
        dataset, return the link.
        """
        links = []
        for f in dataset["fields"]:
            field = f["field"]
            # find the dataset that this field references
            link_dataset = f.get("dataset", None)
            if not link_dataset:
                if field in datasets:
                    link_dataset = field

            if link_dataset == "tree-preservation-order":
                print('found it')
            if link_dataset in datasets:
                links.append(
                    {
                        "from": f"from:{dataset['dataset']}:{field}",
                        "to": f"to:{link_dataset}:reference",
                    }
                )
        return links

    # this is provided in makerule target
    path = specification_path
    spec = frontmatter.load(path)
    row = spec.metadata


    row_height = 20
    text_y = int(row_height / 2)
    padding = 5

    field_width = 162
    datatype_width = 64
    gap = 80

    row_width = field_width + datatype_width


    datasets = [d["dataset"] for d in row["datasets"]]
    maxrows = max([len(d["fields"]) for d in row["datasets"]])
    ndatasets = len(datasets)
    ngaps = ndatasets - 1
    canvas_width = ndatasets * row_width + ngaps * gap
    canvas_height = (maxrows + 1) * row_height

    X = 0
    Y_OFFSET = 0
    points = {}
    links = []
    boxes = []

    for d in row["datasets"]:
        dataset = d["dataset"]

        Y = 0

        # do linking logic first as it affects the original X and Y values
        dataset_links = get_links(d, datasets)
        if dataset_links:
            links.extend(dataset_links)
            linked_datasets = [link["to"].split(':')[1] for link in dataset_links]
            min_link_index = min(
                [datasets.index(link) for link in linked_datasets]
            )
            # if there is a link behind the current row then we need to offset  the Y further
            if datasets.index(dataset) - 1 > min_link_index:
                # offset the Y to put it under the  previous table
                Y = Y + Y_OFFSET
                X = X -row_width - gap
                canvas_height = canvas_height + (maxrows + 1) * row_height
                
        box = []
        box.append(svg_rect("name", X, Y, row_width, row_height))
        box.append(svg_text("name", dataset, X + int(row_width / 2), Y + text_y))

        for f in d["fields"]:
            field = f["field"]
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

        boxes.append(box)

        X = X + row_width + gap
        Y_OFFSET = Y + gap


    svg_content.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}">'
    )
    svg_content.append(
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
        svg_content.append(svg_spline("line", *points[l["from"]], *points[l["to"]]))

    for box in boxes:
        svg_content.append("<g>")
        svg_content.append("\n".join(box))
        svg_content.append("</g>")

    svg_content.append("</svg>")

    if output_path:
        # output to file
        output_to_file(output_path, "\n".join(svg_content))
    else:
        # output to stdout
        print("\n".join(svg_content))

if __name__ == "__main__":
    specification_path = Path(sys.argv[1])

    generate(specification_path)
