{%- set ds = specification["datasets"] -%}

You need to provide {{ ds|length }} dataset{{ "s" if ds|length > 1  else "" }}:

{% for d in specification["datasets"]|sort(attribute='priority') %}
{%- set name = tables["dataset"][d["dataset"]]["name"] -%}
* [{{ name | sentence_case }}](#{{ name.replace(" ", "-")  }}-dataset)
{% endfor %}

You can provide each dataset in one of the following formats:

* CSV
* GeoJSON
* GML
* Geopackage

### Field names

You can use upper or lowcase names for your fields, and punctuation characters are ignored, meaning
'<code class="value">StartDate</code>',
'<code class="value">Start Date</code>'
'<code class="value">START_DATE</code>' and
'<code class="value">start.date</code>',
are all valid ways of naming the '<code class="field">start-date</code>' field.

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

All dates are in the [ISO format](https://www.gov.uk/government/publications/open-standards-for-government/date-times-and-time-stamps-standard)
`YYYY-MM-DD`. Where you don't know the precise date you can enter just the month `YYYY-MM` or even just the year `YYYY`.
The platform will default a `start-date` to the first of the month, or the first of January, and an `end-date` to the last day of the month, or the last day of December.

{% for d in specification["datasets"]|sort(attribute='priority') -%}
{%- set _d = tables["dataset"][d["dataset"]] -%}
{%- set name = tables["dataset"][d["dataset"]]["name"] -%}

### {{ name | sentence_case }} dataset

{% if _d["guidance"] -%}
{{_d["guidance"]}}
{%- endif %}

The {{ name }} dataset contains the following fields:

{% for f in d["fields"] -%}
{%- set field = f["field"] -%}
{%- for _f, df in tables["dataset-field"][d["dataset"]].items() -%}
{%- if _f == field -%}
#### {{ field }}

{% if df["guidance"] %}
{{ df["guidance"] }}

{% elif tables["field"][field]["guidance"] -%}
{{ tables["field"][field]["guidance"] }}
{%- endif -%}
{%- if df["examples"]|length > 0 -%}
{%- if df["examples"]|length == 1 %}
{%- set ex = df["examples"][0] -%}
(for example <code class="value">{{ ex["value"] }}</code>{%- if ex["description"] %} — {{ ex["description"] }}{% endif %})
{% else %}
Examples:

{% for ex in df["examples"] -%}
* <code class="value">{{ ex["value"] }}</code>{%- if ex["description"] %} — {{ ex["description"] }}{% endif %}
{% endfor -%}
{%- endif -%}
{%- endif -%}

{%- endif -%}
{%- endfor -%}
{%- endfor %}

{% endfor %}
