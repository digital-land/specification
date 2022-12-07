#!/usr/bin/env python3

#  see content/organisation-data.csv

import csv
import frontmatter


projects = ["open-digital-planning", "design-codes"]

# TBD: create projects for these?
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
        "authoritative": [
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

# TBD: should these come from projects?
lpa_datasets = {
    "brownfield-land": {
        "specification": "brownfield-land",
        "provision-reason": "statutory",
    },
    "developer-agreement": {
        "specification": "developer-ageement",
        "provision-reason": "encouraged",
    },
    "developer-agreement-contribution": {
        "specification": "developer-ageement",
        "provision-reason": "encouraged",
    },
    "developer-agreement-transaction": {
        "specification": "developer-ageement",
        "provision-reason": "encouraged",
    },
    # others added from projects ..
}


seen_organisation = {}

def seen(organisation, dataset):
    global seen_organisation
    seen_organisation.setdefault(organisation, set())
    _seen = dataset in seen_organisation[organisation]
    seen_organisation[organisation].add(dataset)
    return _seen


fields = ["organisation", "project", "provision-reason", "specification", "dataset"]

w = csv.DictWriter(open("content/organisation-dataset.csv", "w", newline=""), fields)
w.writeheader()


# national datasets ..
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

# project expectations ..
for project in sorted(projects):
    proj = frontmatter.load(f"content/project/{project}.md")

    for organisation in sorted(proj["organisations"]):
        for specification in sorted(proj["specifications"]):
            spec = frontmatter.load(f"content/specification/{specification}.md")
            spec_datasets = [item["dataset"] for item in spec["datasets"]]
            for dataset in sorted(spec_datasets):
                if not seen(organisation, dataset):
                    row = {
                        "organisation": organisation,
                        "project": project,
                        "provision-reason": proj["provision-reason"],
                        "specification": specification,
                        "dataset": dataset,
                    }
                    w.writerow(row)
                    lpa_datasets[dataset] = row


# blank out all LPAs ..

lpas = set()
for row in csv.DictReader(open("var/cache/organisation.csv")):
    organisation = row["organisation"].replace("local-authority-eng:", "local-authority:")
    if not row["end-date"]:
        if organisation.startswith("development-corporation") or organisation.startswith("national-park"):
            lpas.add(organisation)
        elif organisation.startswith("local-authority"):
            if row["local-authority-type"] not in ["COMB", "CTY", "SRA"]:
                lpas.add(organisation)


for organisation in sorted(lpas):
    for dataset, row in lpa_datasets.items():
        if not seen(organisation, dataset):
            row["dataset"] = dataset
            row["organisation"] = organisation
            if row["provision-reason"] == "expected":
                row["provision-reason"] = "prospective"
            w.writerow(row)
