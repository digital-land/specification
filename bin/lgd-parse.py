#!/usr/bin/env python3

import sys
import csv
import re
from datetime import datetime
from pyquery import PyQuery

organisations = {}
for row in csv.DictReader(open("var/cache/organisation.csv", newline="")):
    organisations[row["name"]] = row

# Match names
# TBD: create and use a recociliation dataset
for o, n in [
    ("North Devon Council", "North Devon District Council"),
    ("Wirral Council", "Wirral Borough Council"),
    ("Bath & North East Somerset Council", "Bath and North East Somerset Council"),
    ("Brighton and Hove Council", "Brighton and Hove City Council"),
    ("Croydon London Borough Council", "London Borough of Croydon"),
    ("Cumberland", "Cumberland Unitary Authority"),
    ("Hammersmith & Fulham Council", "London Borough of Hammersmith & Fulham"),
    ("Haringey Council", "London Borough of Haringey"),
    ("Waltham Forest Council", "London Borough of Waltham Forest"),
    ("Westmoreland & Furness", "Westmorland and Furness Council"),
    ("Barking & Dagenham Council", "London Borough of Barking and Dagenham"),
    ("Greenwich Council", "Royal Borough of Greenwich"),
    ("Kensington and Chelsea London Borough Council", "Royal Borough of Kensington and Chelsea"),
    ("Lambeth Council", "London Borough of Lambeth"),
    ("Redcar and Cleveland Council", "Redcar and Cleveland Borough Council"),
    ("Isles of Scilly", "Council of the Isles of Scilly"),
    ("Islington Council", "London Borough of Islington"),
]:
    organisations[o] = organisations[n]


def find_organisation(name):
    name = name.strip()
    if name in organisations:
        return organisations[name]["organisation"]
    raise NameError(name)


pq = PyQuery(filename=sys.argv[1])

fieldnames = ["organisation", "name", "cohort"]

w = csv.DictWriter(open(sys.argv[2], "w", newline=""), fieldnames)
w.writeheader()

for h3 in pq("h3").items():
    if h3.text() in ["Members", "Subscribers", "Contributors"]:
        cohort = "LGD-" + h3.text()[:-1]
        for name in h3.next("p").text().split("\n"):
            if name in ["London Councils", "Tipperary County Council", "Argyll & Bute Council"]:
                continue;
            name = re.sub("\s*\(.*$", "", name)
            row = {}
            row["name"] = name
            row["cohort"] = cohort
            row["organisation"] = find_organisation(row["name"])
            w.writerow(row)
