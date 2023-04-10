#!/usr/bin/env python3

import sys
import glob
import frontmatter

# assert realm and phase to datasets ..

group_dataset = {
    "specification": [
        "attribution",
        "collection",
        "datatype",
        "datapackage",
        "datapackage-dataset",
        "dataset",
        "dataset-package",
        "dataset-field",
        "dataset-schema",
        "dataset-resource",
        "licence",
        "patch",
        "phase",
        "prefix",
        "project",
        "project-status",
        "provision-reason",
        "realm",
        "severity",
        "schema",
        "schema-field",
        "specification",
        "specification-status",
        "theme",
        "typology",
    ],
    "collection": [
        "source",
        "endpoint",
        "old-resource",

        "log",
        "resource", 
    ],
    "pipeline": [
        "column",
        "combine",
        "concat",
        "convert",
        "default-value",
        "default",
        "filter",
        "patch",
        "skip",
        "transform",

        "issue-type",
        "lookup",
        "reference",
        "old-entity",
    ],
    "provenance": [
        "checksum",
        "column-field",
        "entity",
        "field",
        "fact",
        "fact-resource",
        "issue",
        "organisation-dataset",
        "provenance",
    ],
    "live": [
        "brownfield-land",
        "ownership-status",
        "site-category",
        "planning-permission-status",
        "planning-permission-type",
    ],
    "public-beta": [
        "developer-agreement",
        "developer-agreement-contribution",
        "developer-agreement-transaction",
        "developer-agreement-type",
        "contribution-funding-status",
        "contribution-purpose",
    ],
    "private-beta": [
        "article-4-direction-area",
        "article-4-direction",
        "article-4-direction-rule",
        "conservation-area",
        "tree",
        "tree-preservation-order",
        "tree-preservation-type",
        "tree-preservation-zone",
        "listed-building-outline",
        "design-code-area",
        "design-code-category",
        "design-code",
        "design-code-rule",
        "design-code-status",
        "document-type",
    ],
    "national-dataset": [
        "ancient-woodland",
        "ancient-woodland-status",
        "area-of-outstanding-natural-beauty",
        "battlefield",
        "central-activities-zone",
        "certificate-of-immunity",
        "development-corporation",
        "listed-building-grade",
        "listed-building",
        "local-planning-authority",
        "local-resilience-forum",
        "nonprofit",
        "parish",
        "government-organisation",
        "site-category",
        "green-belt-core",
        "green-belt",
        "heritage-at-risk",
        "heritage-coast",
        "local-authority-district",
        "local-authority",
        "local-authority-type",
        "national-park-authority",
        "national-park",
        "park-and-garden",
        "park-and-garden-grade",
        "passenger-transport-executive",
        "protected-wreck-site",
        "public-authority",
        "ramsar",
        "regional-park-authority",
        "region",
        "scheduled-monument",
        "site-of-special-scientific-interest",
        "special-area-of-conservation",
        "special-protection-area",
        "waste-authority",
        "world-heritage-site-buffer-zone",
        "world-heritage-site",
    ],
    "alpha": [
        "development-plan-document",
        "development-plan",
        "development-plan-status",
        "development-plan-timetable",
        "development-plan-type",
        "infrastructure-funding-statement",
    ],
    "typology": [
        "category",
        "document",
        "organisation",
        "policy",
        "geography",
    ],
    "discovery": [
        "development-metric",
        "development-policy-area",
        "development-policy-category",
        "development-policy",
        "development-policy-metric",
        "planning-application",
        "planning-application-status",
        "planning-application-type",
        "planning-development-category",
        "permitted-development-right",

        "brownfield-site",
        "permitted-development-right-part",

        "internal-drainage-board",
        "internal-drainage-district",
        "local-enterprise-partnership",
        "conservation-area-document",
        "conservation-area-document-type",
    ],
    "prioritised": [
        "address",
        "asset-of-community-value",
        "best-and-most-versatile-agricultural-land",
        "biodiversity-net-gain-assessment",
        "buffer-zone",
        "building-preservation-notice",
        "coastal-change-management-area",
        "common-land-and-village-green",
        "company",
        "contaminated-land",
        "control-of-major-accident-hazards-site",
        "employment-allocation",
        "flood-zone-1",
        "flood-zone-2",
        "flood-zone-3",
        "guardianship-site-and-english-heritage-site",
        "gypsy-and-traveller-site",
        "heritage-action-zone",
        "historic-non-designed-rural-landscape-local-landscape-area",
        "historic-stone-quarry",
        "housing-allocation",
        "hs2-safeguarded-area",
        "local-green-space",
        "locally-listed-building",
        "local-nature-recovery-strategy",
        "london-square",
        "long-established-woodland",
        "long-protected-woodland",
        "main-river",
        "metropolitan-open-land",
        "mineral-safeguarding-area",
        "nature-improvement-area",
        "neighbourhood-forum",
        "non-designated-and-locally-listed-historic-asset",
        "non-designated-archeology-asset-of-national-importance",
        "nuclear-safety-zone",
        "open-space",
        "proposed-ramsar-site",
        "protected-land",
        "protected-view",
        "public-safety-zone-around-airport",
        "safeguarded-aerodrome",
        "safeguarded-military-explosives-site",
        "safeguarded-wharf",
        "safety-hazard-area",
        "self-and-custom-buildarea",
        "street",
        "suitable-alternative-green-space",
        "transport-under-tcpa-route",
        "wildbelt",
        "wildlife",
    ]
}

groups = {
        "collection" : {"realm": "collection", "phase": "alpha"},
        "pipeline" : {"realm": "pipeline", "phase": "alpha"},
        "provenance" : {"realm": "provenance", "phase": "alpha"},
        "specification" : {"realm": "specification", "phase": "alpha"},
        "live" : {"realm": "dataset", "phase": "live"},
        "public-beta" : {"realm": "dataset", "phase": "beta"},
        "private-beta" : {"realm": "dataset", "phase": "beta"},
        "national-dataset" : {"realm": "dataset", "phase": "beta"},
        "alpha" : {"realm": "dataset", "phase": "alpha"},
        "typology" : {"realm": "dataset", "phase": "alpha"},
        "discovery" : {"realm": "dataset", "phase": "discovery"},
        "prioritised" : {"realm": "dataset", "phase": "prioritised"},
}

dataset_group = {}
for group, l in group_dataset.items():
    for dataset in l:
        dataset_group[dataset] = group


for path in glob.glob("content/dataset/*.md"):
    post = frontmatter.load(path)

    dataset = post["dataset"]
    g = groups[dataset_group[dataset]]

    if not post.get("collection", ""):
        post["collection"] = ""

    if not post.get("realm", ""):
        post["realm"] = g["realm"]

    if not post.get("phase", ""):
        post["phase"] = g["phase"]

    with open(path, "wb") as f:
        frontmatter.dump(post, f)
        f.write("\n".encode("utf-8"))
