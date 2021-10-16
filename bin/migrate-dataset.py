#!/usr/bin/env python3

import sys
import csv

w = None
fields = ["dataset", "collection", "name", "plural", "wikidata", "wikipedia", "typology", "themes", "description", "text", "entry-date", "start-date", "end-date"]

collection = {}
for row in csv.DictReader(open("specification/collection.csv", newline="")):
    collection[row["collection"]] = row

path = "specification/dataset.csv"
for row in csv.DictReader(open(path, newline="")):
    if not w:
        w = csv.DictWriter(open("x.csv", "w"), fields)
        w.writeheader()

    for field in fields:
        if field not in row:
            row[field] = ""

    dataset = row["dataset"]
    if dataset in ["dataset", "organisation", "geography", "the-broads"]:
        continue

    if dataset in ["ancient-monument-not-scheduled-yet", "attribution", "licence", "archelogy-area-type", "best-and-most-versatile-agricultural-land", "biodiversity-net-gain-off-site", "buffer-zone", "coastal-change-management-area", "common-land-and-village-green", "contaminated-land", "control-of-major-accident-hazards-site", "flood-zone-1", "flood-zone-2", "flood-zone-3", "guardianship-site-and-english-heritage-site", "gypsy-and-traveller-site", "heritage-action-zone", "historic-non-designed-rural-landscape-local-landscape-area", "historic-stone-quarry", "housing-number", "housing-allocation", "hs2-safeguarded-area", "local-green-space", "local-nature-recovery-strategy", "london-square", "long-established-woodland", "long-protected-woodland", "main-river", "metropolitan-open-land", "mineral-safeguarding-area", "nature-improvement-area", "non-designated-archeology-asset-of-national-importance", "non-designated-and-locally-listed-historic-asset", "asset-of-community-value", "nuclear-safety-zone", "planning-decision", "proposed-ramsar-site", "protected-land", "protected-site-strategy", "protected-view", "public-safety-zone-around-airport", "safeguarded-aerodrome", "safeguarded-military-explosives-site", "safeguarded-wharf", "safety-hazard-area", "self-and-custom-buildarea", "site-of-nature-conservation-importance", "special-protection-area", "suitable-alternative-green-space", "transport-under-tcpa-route", "tree-preservation-order", "use-class-order", "wildbelt", "wildlife" ]:
        row["collection"] = ""
    else:
        if dataset in ["national-park-authority", "local-authority-eng", "government-organisation", "development-corporation", "internal-drainage-board"]:
            row["collection"] = "organisation"
        elif dataset in ["contribution-funding-status", "contribution-purpose", "developer-agreement-contribution", "developer-agreement-transaction", "developer-agreement-type", "developer-agreement"]:
            row["collection"] = "developer-contributions"
        elif dataset in ["battlefield", "building-preservation-notice", "certificate-of-immunity", "heritage-at-risk", "listed-building-grade", "park-and-garden", "park-and-garden-grade", "protected-wreck-site", "scheduled-monument", "world-heritage-site"]:
            row["collection"] = "historic-england"
        else:
            row["collection"] = row["dataset"]

        if row["collection"] not in collection:
            print("unknown collection", row["collection"], file=sys.stderr)
            sys.exit(2)

    w.writerow(row)
