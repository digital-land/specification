# Digital Land Specification dataset

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/digital-land/brownfield-land/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)

Digital Land specifications, built upon the [GOV.UK Registers](https://www.registers.service.gov.uk/) data model.

# Updating the collection

We recommend working in [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) before installing the python dependencies:

    $ make init
    $ make

Files which can't be downloaded may be added to the collection manually:

    $ digital-land fetch file:cache/foo.zip

# Licence

The software in this project is open source and covered by LICENSE file.

Individual datasets copied into this repository may have specific [copyright](collection/attribution/) and [licensing](collection/licence/),
otherwise all content and data in this repository is
[© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
