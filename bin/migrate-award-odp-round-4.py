#!/usr/bin/env python3

import csv

names = [
    "Blackpool Council",
    "Braintree District Council",
    "Brighton and Hove City Council",
    "Chelmsford Council",
    "County of Herefordshire District Council",
    "Dartford Borough Council",
    "Derby City Council",
    "Fenland District Council",
    "Gedling Borough Council",
    "Harlow Borough Council",
    "Kings Lynn and West Norfolk Borough",
    "Kingston Upon Thames Council",
    "London Borough of Bexley",
    "London Borough of Brent",
    "London Borough of Hackney",
    "Malvern Hills District Council",
    "North Devon District Council",
    "Nottingham City Council",
    "Rotherham Metropolitan Borough Council",
    "Swale Brough Council",
    "Westmorland and Furness Council",
    "Wiltshire Council",
    "Worcester City Council",
    "Wychavon District Council",
]

organisations = {}
lookups = {}

# patch made-up names
patches = {
    "Blackpool Council": "Blackpool Borough Council",
    "Chelmsford Council": "Chelmsford City Council",
    "County of Herefordshire District Council": "Herefordshire Council",
    "Harlow Borough Council": "Harlow District Council",
    "Kings Lynn and West Norfolk Borough": "Borough Council of King's Lynn and West Norfolk",
    "Kingston Upon Thames Council": "Royal Borough of Kingston upon Thames",
    "Swale Brough Council": "Swale Borough Council",
}

if __name__ == "__main__":

    for row in csv.DictReader(open("var/cache/organisation.csv", newline="")):
        organisation = row["organisation"]
        organisations[organisation] = row
        lookups[row["name"]] = organisation

    r = csv.DictReader(open("content/award.csv", newline=""))
    w = csv.DictWriter(open("tmp/award.csv", "w"), fieldnames=r.fieldnames)
    w.writeheader()

    award = 0
    for row in r:
        award = int(row["award"])
        w.writerow(row)

    # append latest round
    for name in names:
        name = patches.get(name, name)
        organisation = lookups[name]
        award = award + 1
        row = {
                "award": award,
                "start-date": "2025-09-23",
                "fund": "odp-round-4.2",
                "intervention": "improvement",
                "amount": "50000",
                "organisation": organisation,
                "documentation-url": "https://mhclgdigital.blog.gov.uk/2025/09/23/digital-planning-transformation-gains-momentum/",
        }
        w.writerow(row)
