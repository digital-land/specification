#!/usr/bin/env python3

import csv

projects = {
    "open-digital-planning": {
        "provision-reason": "expected",
        "specifications": {
            "article-4-direction": ["article-4-direction", "article-4-direction-area"],
            "conservation-area": ["conservation-area"],
            "listed-building": ["listed-building-outline"],
            "tree-preservation-order": [
                "tree",
                "tree-preservation-zone",
                "tree",
            ],
        },
        "organisations": [
            "local-authority:BUC",
            "local-authority:CAT",
            "local-authority:CMD",
            "local-authority:DAC",
            "local-authority:DNC",
            "local-authority:GLO",
            "local-authority:LBH",
            "local-authority:MDW",
            "local-authority:NBL",
            "local-authority:NED",
            "local-authority:NET",
            "local-authority:SWK",
        ],
    }
}


fields = ["organisation", "project", "provision-reason", "specification", "dataset"]

w = csv.DictWriter(open("content/organisation-dataset.csv", "w", newline=""), fields)
w.writeheader()

for project, p in sorted(projects.items()):
    for organisation in sorted(p["organisations"]):
        for specification, datasets in sorted(p["specifications"].items()):
            for dataset in sorted(datasets):
                w.writerow(
                    {
                        "organisation": organisation,
                        "project": project,
                        "provision-reason": p["provision-reason"],
                        "specification": specification,
                        "dataset": dataset,
                    }
                )
