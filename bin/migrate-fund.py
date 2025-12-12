#!/usr/bin/env python3

import csv

fieldnames = ["start-date", "project", "reference", "fund", "name", "documentation-url", "notes"]

w = csv.DictWriter(open("tmp/fund.csv", "w", newline=""), fieldnames=fieldnames)
w.writeheader()

for row in csv.DictReader(open("content/fund.csv")):
    row["reference"] = row["fund"]

    if row["reference"] in ["local-plan-pathfinders"]:
        row["project"] = "local-plan-pathfinders"
    elif row["reference"] in ["green-belt-reviews", "local-plan-delivery"]:
        row["project"] = "planning-reform"
    else:
        row["project"] = "open-digital-planning"

    w.writerow(row)
