# Digital Land Specification dataset

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/digital-land/brownfield-land/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)
[![Run pipeline](https://github.com/digital-land/specification/actions/workflows/run.yml/badge.svg)](https://github.com/digital-land/specification/actions/workflows/run.yml)

Digital Land specifications, built upon the [GOV.UK Registers](https://www.registers.service.gov.uk/) data model.

This repository also builds the [specification](https://digital-land.github.io/specification/) pages, but we expect to split the dataset and pages into separate repositories.

# Updating the collection

We recommend working in [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) before installing the python dependencies:

    $ make init
    $ make

Files which can't be downloaded may be added to the collection manually:

    $ digital-land fetch file:cache/foo.zip


# Creating a new version of a specification

Use the script

        bin/new-version.py --specification [specification name] --version [major|minor|patch]

This will create a version directory "vn.n.n" in a subdirectory for the specification.

It will copy the current specifiation markdown to that directory and update the version number in the
top level specification markdown. You can then edit the top level file as required.

For example see article-4-direction which has three versions. 

    article-4-direction.md (this will be file you edit and is latest version)
    .
    ├── v1.1.1
    │   └── article-4-direction.md
    └── v1.2.2
    └── article-4-direction.md


# Licence

The software in this project is open source and covered by LICENSE file.

Individual datasets copied into this repository may have specific [copyright](collection/attribution/) and [licensing](collection/licence/),
otherwise all content and data in this repository is
[© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
