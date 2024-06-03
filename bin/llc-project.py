import sys
import csv

print("""---
description: ''
end-date: ''
entry-date: ''
name: Local Land Charges Programme
parent-project: ''
project: local-land-charges
project-status: in-progress
provision-reason: 
documentation-url: https://www.gov.uk/government/publications/hm-land-registry-local-land-charges-programme/local-land-charges-programme
start-date: ''
specifications:
organisations:""")

for row in csv.DictReader(open(sys.argv[1], newline="")):
    print(f'- organisation: {row["organisation"]}')
    print(f'  start-date: {row["start-date"]}')

print("---")
