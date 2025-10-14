#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup

html_content = open(sys.argv[1]).read()
soup = BeautifulSoup(html_content, 'html.parser')

# Get all anchor links
anchors = soup.find_all('a', href=True)

errors = 0

# Check internal anchors
for anchor in anchors:
    href = anchor['href']
    if href.startswith('#'):
        target_id = href[1:]  # Remove the #
        target = soup.find(id=target_id)
        if not target:
            print(f"#{target_id}: not found", file=sys.stderr)
            errors += 1

if errors:
    sys.exit(1)
sys.exit(0)
