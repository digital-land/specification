#!/usr/bin/env python3

import csv

funds = {}


for row in csv.DictReader(open("content/fund.csv", newline="")):
    funds[row["reference"]] = row


fieldnames = ["award", "start-date", "fund", "intervention", "amount", "organisation", "organisations", "documentation-url", "notes"]

w = csv.DictWriter(open("tmp/award.csv", "w", newline=""), fieldnames=fieldnames, extrasaction='ignore')
w.writeheader()

for row in csv.DictReader(open("content/award.csv", newline="")):

    row['start-date'] = funds[row["fund"]]["start-date"]
    w.writerow(row)
