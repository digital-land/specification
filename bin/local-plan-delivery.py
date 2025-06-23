#!/usr/bin/env python3

import sys
import re
import csv
from pyquery import PyQuery


errors = 0
award = 385
defaults = {
    "start-date": "2025-03-19",
    "fund": "local-plans-delivery",
    "intervention": "plan-making",
    "documentation-url": "https://www.gov.uk/guidance/funding-to-support-local-authorities-with-the-costs-of-local-plan-delivery-successful-local-authorities",
}

organisations = {}
for row in csv.DictReader(open("var/cache/organisation.csv", newline="")):
    organisations[row["name"]] = row

# Match names
# TBD: create and use a recociliation dataset
for o, n in [
    ("Barking & Dagenham", "London Borough of Barking and Dagenham"),
    ("Basildon District Council", "Basildon Borough Council"),
    ("Barnet", "London Borough of Barnet"),
    ("Camden", "London Borough of Camden"),
    ("Ealing", "London Borough of Ealing"),
    ("Haringey", "London Borough of Haringey"),
    ("Harrow", "London Borough of Harrow"),
    ("Hounslow", "London Borough of Hounslow"),
    ("Newham", "London Borough of Newham"),
    ("Redbridge", "London Borough of Redbridge"),
    ("Richmond-upon-Thames", "London Borough of Richmond upon Thames"),
    ("Sutton", "London Borough of Sutton"),
    ("Waltham Forest", "London Borough of Waltham Forest"),
    ("Harlow Council", "Harlow District Council"),
    ("Blackpool Council", "Blackpool Borough Council"),
    ("Haringey Council", "London Borough of Haringey"),
    ("Kingston upon Hull City Council", "Hull City Council"),
    ("Lambeth Council", "London Borough of Lambeth"),
    ("Milton Keynes Council", "Milton Keynes City Council"),
    ("Sutton Council", "London Borough of Sutton"),
    ("York City Council", "City of York Council"),
    ("Southwark Council", "London Borough of Southwark"),
    ("Bexley London Borough", "London Borough of Bexley"),
    ("Bromley London Borough", "London Borough of Bromley"),
    ("Central Bedfordshire UA", "Central Bedfordshire Council"),
    ("Cheshire East UA", "Cheshire East Council"),
    ("Cheshire West and Chester UA", "Cheshire West and Chester Council"),
    ("Durham County UA", "Durham County Council"),
    ("Enfield London Borough", "London Borough of Enfield"),
    ("Havering London Borough", "London Borough of Havering"),
    ("Hillingdon London Borough", "London Borough of Hillingdon"),
    ("Kingston upon Thames Royal Borough", "Royal Borough of Kingston upon Thames"),
    ("Kirklees Metropolitan Borough Council", "Kirklees Council"),
    ("North Tyneside Metropolitan Borough Council", "North Tyneside Council"),
    ("Northumberland County UA", "Northumberland County Council"),
    ("Salford Metropolitan District Council", "Salford City Council"),
    ("Shropshire County UA", "Shropshire Council"),
    ("South Staffordshire District Council", "South Staffordshire Council"),
    ("South Tyneside Metropolitan Borough Council", "South Tyneside Council"),
    ("St. Albans City & District Council", "St Albans City and District Council"),
    ("Welwyn Hatfield District Council", "Welwyn Hatfield Borough Council"),
    ("West Lancashire District Council", "West Lancashire Borough Council"),
    ("Wolverhampton Metropolitan Borough Council", "City of Wolverhampton Council"),
    ("Wyre Forest", "Wyre Forest District Council"),
    ("Halton", "Halton Borough Council"),
    ("Knowsley", "Knowsley Metropolitan Borough Council"),
    ("Liverpool", "Liverpool City Council"),
    ("Sefton", "Sefton Metropolitan Borough Council"),
    ("St Helens Councils", "St Helens Council"),
    ("Newcastle upon Tyne Metropolitan District Council", "Newcastle City Council"),
    ("Gateshead Council", "Gateshead Metropolitan Borough Council"),
    ("Windsor and Maidenhead Royal Borough Council", "Royal Borough of Windsor and Maidenhead"),
    ("Eastbourne Local Planning Authority", "Eastbourne Borough Council"),
    ("Greenwich London Borough", "Royal Borough of Greenwich"),
    ("Hackney London Borough", "London Borough of Hackney"),
    ("Lewes Local Planning Authority", "Lewes District Council"),
    ("North West Leicestershire Local Planning Authority", "North West Leicestershire District Council"),
    ("Peak District National Park Local Planning Authority", "Peak District National Park Authority"),
    ("Slough Local Planning Authority", "Slough Borough Council"),
    ("Southend-on-Sea City Council", "Southend-on-Sea Borough Council"),
    ("Yorkshire Dales National Park Local Planning Authority", "Yorkshire Dales National Park Authority"),
]:
    try:
        organisations[o] = organisations[n]
    except KeyError as e:
        print(f"Unknown lookup: {o}: {n}")
        errors += 1


def parse_list(line, organisations):
    sorted_authorities = sorted(organisations, key=len, reverse=True)

    # Split into main part and joint part
    if "(joint with" in line:
        parts = line.split("(joint with", 1)
        main_part = parts[0].strip()
        joint_part = parts[1].rstrip(")")
    else:
        main_part = line.strip()
        joint_part = ""

    # Find main authority
    main_authority = None
    for authority in sorted_authorities:
        if authority in main_part:
            main_authority = authority
            break

    if main_authority is None:
        raise NameError(main_part)

    # Find joint authorities
    joint_authorities = []
    if joint_part:
        remaining = joint_part
        for authority in sorted_authorities:
            if authority in remaining:
                joint_authorities.append(authority)
                # Remove matched text to prevent partial re-matches
                remaining = remaining.replace(authority, "", 1)

        remaining = remaining.strip()
        _remaining = remaining.replace(",", "")
        _remaining = re.sub(r"\band\b", "", _remaining, flags=re.UNICODE)
        _remaining = re.sub(r"\s+", "", _remaining, flags=re.UNICODE)
        if _remaining != "":
            raise NameError(remaining)

    return main_authority, joint_authorities


def find_organisation(name):
    name = name.strip()
    if name in organisations:
        return organisations[name]["organisation"]
    raise NameError(name)


pq = PyQuery(filename="var/cache/local-plan-delivery.html")

fieldnames = [
    "award",
    "start-date",
    "fund",
    "intervention",
    "amount",
    "organisation",
    "organisations",
    "documentation-url",
    "notes",
]

w = csv.DictWriter(
    open("tmp/award.csv", "w", newline=""), fieldnames, extrasaction="ignore"
)
w.writeheader()


for tr in pq("tr").items():
    cols = list(tr("td"))
    if cols:
        row = defaults
        award += 1
        row["award"] = str(award)

        line = cols[0].text
        name, names = parse_list(line, organisations)
        try:
            row["organisation"] = find_organisation(name)
            joints = []
            for n in names:
                joints.append(find_organisation(n))
            row["organisations"] = ";".join(joints)
        except NameError as e:
            print(f"Unknown organisation: {e}", file=sys.stderr)
            errors += 1

            row["organisations"] = find_organisation(name)

        row["amount"] = str(cols[1].text).replace("£", "").replace(",", "").strip().replace(".00", "").replace(".50", "")
        w.writerow(row)
        #print(row, file=sys.stderr)

if errors:
    sys.exit(2)
