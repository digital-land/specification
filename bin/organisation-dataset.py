#!/usr/bin/env python3

#  see content/organisation-data.csv

import csv

# TBD: read these from content/project ..
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

# TBD: create projects for these ..
other = {
    "government-organisation:D1342": {
        "encouraged": [
            "design-code-category",
            "design-code-status",
            "green-belt-core",
            "local-authority",
            "local-authority-type",
            "article-4-direction-rule",
            "infrastructure-funding-statement",
            "planning-permission-status",
            "planning-permission-type",
            "contribution-funding-status",
            "contribution-purpose",
            "developer-agreement-type",
        ],
        "statutory": ["ownership-status", "site-category"],
        "alternative": [
            "area-of-outstanding-natural-beauty",
            "article-4-direction-rule",
            "battlefield",
            "public-authority",
            "ramsar",
            "regional-park-authority",
            "waste-authority",
            "world-heritage-site",
            "development-corporation",
            "government-organisation",
            "national-park-authority",
            "nonprofit",
            "passenger-transport-executive",
            "green-belt",
            "conservation-area",
        ],
        "prospective": ["development-plan-type"],
    },
    "government-organisation:D303": {
        "authoritative": [
            "local-authority-district",
            "local-planning-authority",
            "national-park",
            "parish",
            "region",
        ],
    },
    "government-organisation:PB1164": {
        "authoritative": [
            "battlefield",
            "building-preservation-notice",
            "certificate-of-immunity",
            "heritage-at-risk",
            "listed-building",
            "listed-building-grade",
            "park-and-garden",
            "park-and-garden-grade",
            "protected-wreck-site",
            "scheduled-monument",
            "world-heritage-site",
            "world-heritage-site-buffer-zone",
        ],
        "alternative": ["conservation-area"],
    },
    "government-organisation:PB202": {
        "authorititive": [
            "ancient-woodland",
            "ancient-woodland-status",
            "area-of-outstanding-natural-beauty",
            "heritage-coast",
            "site-of-special-scientific-interest",
            "special-area-of-conservation",
            "special-protection-area",
            "ramsar",
        ]
    },
    "nonprofit:Q180": {
        "alternative": [
            "development-corporation",
            "government-organisation",
            "local-authority",
            "national-park-authority",
            "nonprofit",
            "passenger-transport-executive",
            "public-authority",
            "regional-park-authority",
            "waste-authority",
        ]
    },
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

for organisation, reasons in sorted(other.items()):
    for reason in sorted(reasons):
        for dataset in sorted(reasons[reason]):
            w.writerow(
                {
                    "organisation": organisation,
                    "provision-reason": reason,
                    "dataset": dataset,
                }
            )
