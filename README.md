# Planning Data Specification

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/digital-land/brownfield-land/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)
[![Run pipeline](https://github.com/digital-land/specification/actions/workflows/run.yml/badge.svg)](https://github.com/digital-land/specification/actions/workflows/run.yml)

Specifications and other data used to model the data for https://planning.data.gov.uk

* [content](content/) – source data as Frontmatter Markdown and CSV files
* [content/specification](content/specification) – Frontmatter Markdown for technical specifications for providing the data
* [content/dataset](content/dataset) – Frontmatter Markdown for each dataset on the platform
* [content/field](content/field) – Frontmatter Markdown for each dataset field
* [content/datatype](content/datatype) – Frontmatter Markdown for field datatypes

This content is used to build:

* [specification](specification/) – the model as CSV files, built from the content available at https://datasette.planning.data.gov.uk/digital_land
* [doc](doc/) – documentation GitHub pages https://digital-land.github.io/specification/ which we expect to move to https://planning.data.gov.uk

# Updating the collection

We recommend working in [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) before installing the python dependencies:

    $ make init
    $ make

# Licence

The software in this project is open source and covered by LICENSE file.

Individual datasets copied into this repository may have specific [copyright](collection/attribution/) and [licensing](collection/licence/),
otherwise all content and data in this repository is
[© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
