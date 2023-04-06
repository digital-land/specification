#!/usr/bin/env python3

import sys
from pathlib import Path
import frontmatter

path = Path(sys.argv[1])
spec = frontmatter.load(path)
row = spec.metadata
links = []

print("---")
print(f'title: {spec["name"]} datasets')
print("---")
print("```mermaid")
print("erDiagram")

datasets = [d["dataset"] for d in row["datasets"]]

for d in row["datasets"]:
    print(f'    {d["dataset"]} {{')
    for f in d["fields"]:
        if f["field"].endswith("-date"):
            type = "date"
        elif f["field"].endswith("-url"):
            type = "url"
        else:
            type = "string"
        print(f'        {type} {f["field"]}')
        if f["field"] in datasets:
            links.append(
                {
                    "from": d["dataset"],
                    "to": f["field"],
                    "line": "|--o{",
                    "reference": "cites",
                }
            )

    print("    }")

for l in links:
    print(f'    {l["from"]} {l["line"]} {l["to"]} : {l["reference"]}')

print("```")
