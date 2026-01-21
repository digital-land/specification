{%- set ds = specification["datasets"] -%}
{%- set ds_m = specification["datasets"]|selectattr("requirement-level", "eq", "MUST")|list -%}
{%- set ds_o = specification["datasets"]|rejectattr("requirement-level", "eq", "MUST")|list -%}

### Files

{% if ds_m|length > 0 %}
For {{ specification["plural"]}} you need to provide {{ ds_m|length }} dataset{{ "s" if ds_m|length > 1  else "" }}:

{% for d in ds_m|sort(attribute='priority') %}
{%- set name = tables["dataset"][d["dataset"]]["name"] -%}
* [{{ name | sentence_case }}](#{{ name.replace(" ", "")  }}-dataset)
{% endfor %}
{% endif %}

{% if ds_o|length > 0 %}
{% if ds_m|length == 0 %}
For {{ specification["plural"]}} you may provide the following dataset{{ "s" if ds_m|length > 1  else "" }}:
{% else %}
You may also provide the following dataset{{ "s" if ds_o|length > 1  else "" }}:
{% endif %}

{% for d in ds_o|sort(attribute='priority') %}
{%- set name = tables["dataset"][d["dataset"]]["name"] -%}
* [{{ name | sentence_case }}](#{{ name.replace(" ", "-") }}-dataset)
{% endfor %}
{% endif %}

{{ "Each" if ds|length > 1  else "The" }} dataset needs to be provided
in a {{ "separate" if ds|length > 1  else "" }} CSV file 
following the government 
[tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).
{% if specification["is-geospatial"] %}
Where your dataset contains geospatial fields, you may use one of the following formats: 

* CSV
* GeoJSON
* GML
* KML
* Geopackage
{% endif %}

The fields and format of the data you need to
prepare are documented below, and formally defined in the
[technical specifications](#technical-specifications) attached to this page.

### Field names

You can use uppercase or lowercase names for your fields, and any punctuation characters are ignored,
meaning the following examples are all valid ways of naming the `start-date` field in your data:

* `StartDate`
* `Start Date`
* `START_DATE`
* `start.date`

### Reference values

Each dataset has a `reference` field.
Reference values are important to help people find and link to the data.
Where you don’t have a reference for an item, you will need to create one that is:

* unique within your data
* persistent — it doesn’t change when the data is updated

A good reference is something you already use.
Where these aren't unique, you make them unique by appending the year, or even the full date.
Great references are short, easy to read, to pronounce and remember.

### Date values

All dates must be in the format `YYYY-MM-DD`, following the guidance for [formatting dates and times in data](https://www.gov.uk/government/publications/open-standards-for-government/date-times-and-time-stamps-standard).

Where you don't know the precise date you can enter just the month `YYYY-MM` or even just the year `YYYY`.
The platform will default a `start-date` to the first of the month, or the first of January, and an `end-date` to the last day of the month, or the last day of December. For example:

* `2025-04-19`
* `2025-04`
* `2025`

{% if specification["is-geospatial"] %}
### Geometry and point fields

All coordinates in any geospatial data you provide must be in the WGS84 (ETRS89) coordinate reference system following the government guidance on the [Exchange of a location point](https://www.gov.uk/government/publications/open-standards-for-government/exchange-of-location-point).

A `geometry` field may contain a single `POLYGON` or a `MULTIPOLYGON` object. A `point` field may only contain a single `POINT` object.

If you’re providing geospatial data in a CSV, the field must be encoded as well-known text (WKT), for example:

* `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,...` 
* `POLYGON ((1.188829 51.23478,1.188376 51.234909,...`
* `POINT (-3.466788 50.58151)`

When providing geospatial data as GeoJSON, GML, KML or in a Geopackage, use the native format for the geospatial data. 
That is there is no need to duplicate the geospatial data into a `point` or `geometry` property or field.
{% endif %}

{% for d in specification["datasets"]|sort(attribute='priority') -%}
{%- set _d = tables["dataset"][d["dataset"]] -%}
{%- set name = tables["dataset"][d["dataset"]]["name"] -%}

## {{ name | sentence_case }} dataset

{% if _d["guidance"] -%}
{{_d["guidance"]}}
{%- endif %}

### Fields

{% for requirement_level in ["MUST", "SHOULD", "MAY"] -%}
{% if requirement_level == "MUST" %}Your {{ name }} data must {% elif requirement_level == "SHOULD" %}should {% else %}and may also {% endif  %}
contain the following fields:

{% for f in d["fields"] -%}{% if f["requirement-level"] == requirement_level %}
* `{{ f["field"] }}`
{% endif %}{% endfor %}
{% endfor %}

{% for f in d["fields"] -%}
{%- set field = f["field"] -%}
{%- set sf = tables["specification-field"][specification["specification"]][d["dataset"]][field] -%}

{%- if field in tables["dataset-field"][d["dataset"]] -%}
{%- set df = tables["dataset-field"][d["dataset"]][field] -%}
{%- else -%}
{%- set df = tables["dataset-field"][sf["datasets"][0]][field] -%}
{% endif %}

### {{ field }}

{% if df["guidance"] %}{{ df["guidance"] }}{% elif tables["field"][field]["guidance"] %}{{ tables["field"][field]["guidance"]| trim }}{%- endif -%}{%- if df["examples"]|length > 0 %} For example:

{% for ex in df["examples"] -%}
* <code class="value">{{ ex["value"] }}</code>{%- if ex["description"] %} — {{ ex["description"] }}{% endif %}
{% endfor -%}
{%- endif -%}

{%- endfor %}
{% endfor %}
