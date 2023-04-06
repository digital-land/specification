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
    print(f'{d["dataset"]} {{')
    for f in d["fields"]:
        print(f'    {f["field"]}')
        if f["field"] in datasets:
            links.append({"from": d["dataset"], "to": f["field"], "line": "|--o{"})

    print('}')

for l in links:
    print(l["from"], l["line"], l["to"])

print("```")
