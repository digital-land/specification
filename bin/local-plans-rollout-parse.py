import sys
import csv
from datetime import datetime
from pyquery import PyQuery

organisations = {}
for row in csv.DictReader(open("var/cache/organisation.csv", newline="")):
    organisations[row["name"]] = row

# Match names
# TBD: create and use a recociliation dataset
for o, n in [
     ("Amber Valley", "Amber Valley Borough Council"),
     ("Bristol, City of", "Bristol City Council"),
     ("Cannock Chase", "Cannock Chase District Council"),
     ("Chichester", "Chichester District Council"),
     ("Dacorum", "Dacorum Borough Council"),
     ("Dudley", "Dudley Metropolitan Borough Council"),
     ("East Riding of Yorkshire", "East Riding of Yorkshire Council"),
     ("Epsom and Ewell", "Epsom and Ewell Borough Council"),
     ("Erewash", "Erewash Borough Council"),
     ("Great Yarmouth", "Great Yarmouth Borough Council"),
     ("Horsham", "Horsham District Council"),
     ("Hyndburn", "Hyndburn Borough Council"),
     ("Isle of Wight", "Isle of Wight Council"),
     ("King’s Lynn and West Norfolk", "Borough Council of King's Lynn and West Norfolk"),
     ("Malvern Hills", "Malvern Hills District Council"),
     ("Newcastle-under-Lyme", "Newcastle-under-Lyme Borough Council"),
     ("North Norfolk", "North Norfolk District Council"),
     ("Nuneaton and Bedworth", "Nuneaton and Bedworth Borough Council"),
     ("Pendle", "Pendle Borough Council"),
     ("Rutland", "Rutland County Council"),
     ("Sandwell", "Sandwell Metropolitan Borough Council"),
     ("South Oxfordshire", "South Oxfordshire District Council"),
     ("South Staffordshire", "South Staffordshire Council"),
     ("South Tyneside", "South Tyneside Council"),
     ("Spelthorne", "Spelthorne Borough Council"),
     ("St Albans", "St Albans City and District Council"),
     ("Stroud", "Stroud District Council"),
     ("Surrey Heath", "Surrey Heath Borough Council"),
     ("Teignbridge", "Teignbridge District Council"),
     ("Tunbridge Wells", "Tunbridge Wells Borough Council"),
     ("Vale of White Horse", "Vale of White Horse District Council"),
     ("West Berkshire", "West Berkshire Council"),
     ("Wiltshire", "Wiltshire Council"),
     ("Winchester", "Winchester City Council"),
     ("Wirral", "Wirral Borough Council"),
     ("Wokingham", "Wokingham Borough Council"),
     ("Wolverhampton", "City of Wolverhampton Council"),
     ("Worcester", "Worcester City Council"),
     ("Wychavon", "Wychavon District Council"),
]:
    organisations[o] = organisations[n]


def find_organisation(name):
    name = name.strip()
    if name in organisations:
        return organisations[name]["organisation"]
    raise NameError(name)


pq = PyQuery(filename=sys.argv[1])

fieldnames = ["project", "organisation", "name", "start-date"]

w = csv.DictWriter(open(sys.argv[2], "w", newline=""), fieldnames)
w.writeheader()

errors = 0
for li in pq('h2#local-planning-authorities-required-to-start-plan-making-by-30-june-2026 ~ ul > li').items():
    row = {}
    row["project"] = "local-plans-rollout"
    row["start-date"] = "2026-06-30"
    row["name"] = li.text()
    try:
        row["organisation"] = find_organisation(row["name"])
        if row["organisation"]:
            w.writerow(row)
    except NameError as e:
        print(f"Unknown organisation: {e}")
        errors += 1

if errors:
    sys.exit(2)
