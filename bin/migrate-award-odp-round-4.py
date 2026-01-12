#!/usr/bin/env python3

import csv

names = [
        Bedford Borough Council 
Blaby District Council 
Bournemouth, Christchurch and Poole Council 
Broads Authority 
Burnley Borough Council 
Cherwell District Council 
Cheshire East Council 
Chorley Borough Council 
City of Bradford Metropolitan Council 
Cornwall Council 
Dartmoor National Park Authority 
Dudley Metropolitan Borough Council 
East Suffolk Council 
Fareham Borough Council 
Gravesham Borough Council 
Kirklees Council 
Lancaster City Council 
Lichfield District Council 
London Borough of Ealing 
London Borough of Hammersmith and Fulham 
London Borough of Merton 
London Borough of Richmond upon Thames 
London Borough of Sutton 
Luton Borough Council 
Middlesbrough Council 
Newcastle under Lyme Borough Council 
North West Leicestershire District Council 
North York Moors National Park Authority 
Norwich City Council 
Nuneaton and Bedworth Borough Council 
Peak District National Park Authority 
Portsmouth City Council 
Preston City Council 
Reading Borough Council 
Ribble Valley Council 
Royal Borough of Greenwich 
Rushcliffe Borough Council 
Sevenoaks District Council 
Slough Borough Council 
South Ribble Borough Council 
Stroud District Council 
Sunderland City Council 
Telford and Wrekin Council 
Tonbridge and Malling Borough Council 
Tunbridge Wells Borough Council 
West Lancashire Borough Council 
Woking Borough Council 
Wokingham Borough Council 
Wyre Forest District Council
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
                "start-date": "2026-09-23",
                "fund": "odp-round-4.1",
                "intervention": "improvement",
                "amount": "50000",
                "organisation": organisation,
                "documentation-url": "https://mhclgdigital.blog.gov.uk/2025/09/23/digital-planning-transformation-gains-momentum/",
        }
        w.writerow(row)
