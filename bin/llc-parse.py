import sys
import csv
from datetime import datetime
from pyquery import PyQuery

organisations = {}
for row in csv.DictReader(open("var/cache/organisation.csv", newline="")):
    organisations[row["name"]] = row

# Skip Welsh councils
for o in [
    "Blaenau Gwent County Borough Council",
    "Carmarthenshire County Council",
    "Caerphilly County Borough Council",
    "City and County of Swansea Council",
    "Merthyr Tydfil County Borough Council",
    "Torfaen County Borough Council",
    "Pembrokeshire County Council",
    "Bridgend County Borough Council",
]:
    organisations.setdefault(o, {"organisation": ""})

# Match names
# TBD: create and use a recociliation dataset
for o, n in [
    ("Blackpool Council", "Blackpool Borough Council"),
    ("Haringey Council", "London Borough of Haringey"),
    ("Kingston upon Hull City Council", "Hull City Council"),
    ("Lambeth Council", "London Borough of Lambeth"),
    ("Milton Keynes Council", "Milton Keynes City Council"),
    ("Sutton Council", "London Borough of Sutton"),
    ("York City Council", "City of York Council"),
    ("Southwark Council", "London Borough of Southwark"),
]:
    organisations[o] = organisations[n]


def find_organisation(name):
    name = name.strip()
    if name in organisations:
        return organisations[name]["organisation"]
    raise NameError(name)


pq = PyQuery(filename=sys.argv[1])

fieldnames = ["organisation", "name", "start-date"]

w = csv.DictWriter(open(sys.argv[2], "w", newline=""), fieldnames)
w.writeheader()

errors = 0
for tr in pq("tr").items():
    cols = list(tr("td"))
    if cols:
        row = {}
        row["name"] = cols[0].text
        row["start-date"] = datetime.strptime(cols[1].text.strip(), "%d %B %Y").strftime(
            "%Y-%m-%d"
        )
        print(row, file=sys.stderr)
        try:
            row["organisation"] = find_organisation(row["name"])
            if row["organisation"]:
                w.writerow(row)
        except NameError as e:
            print(f"Unknown organisation: {e}")
            errors += 1

if errors:
            sys.exit(2)
