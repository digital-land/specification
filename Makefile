NO_DATASET=true
RENDER_COMMAND=python3 ./bin/render.py

second-pass::	specification

include makerules/makerules.mk
include makerules/specification.mk
include makerules/render.mk

SPECIFICATION_CSV=\
	specification/attribution.csv\
	specification/licence.csv\
	specification/collection.csv\
	specification/datapackage.csv\
	specification/datapackage-dataset.csv\
	specification/dataset.csv\
	specification/dataset-field.csv\
	specification/dataset-schema.csv\
	specification/schema.csv\
	specification/schema-field.csv\
	specification/field.csv\
	specification/datatype.csv\
	specification/typology.csv\
	specification/issue-type.csv\
	specification/include-exclude.csv\
	specification/severity.csv\
	specification/prefix.csv\
	specification/cohort.csv\
	specification/project.csv\
	specification/project-organisation.csv\
	specification/project-status.csv\
	specification/specification.csv\
	specification/specification-status.csv\
	specification/organisation-dataset.csv\
	specification/provision.csv\
	specification/provision-reason.csv\
	specification/provision-rule.csv\
	specification/pipeline.csv\
	specification/role.csv\
	specification/theme.csv

specification:: $(SPECIFICATION_CSV)

# made from dataset content ..
DATASET_MD=$(sort $(wildcard content/dataset/*.md))
specification/dataset.csv:	$(DATASET_MD) bin/load-markdown.py
	@mkdir -p specification/
	python3 bin/load-markdown.py $@ $(DATASET_MD)

ATTRIBUTION_MD=$(sort $(wildcard content/attribution/*.md))
specification/attribution.csv:	$(ATTRIBUTION_MD) bin/load-markdown.py
	@mkdir -p specification/
	python3 bin/load-markdown.py $@ $(ATTRIBUTION_MD)

LICENCE_MD=$(sort $(wildcard content/licence/*.md))
specification/licence.csv:	$(LICENCE_MD) bin/load-markdown.py
	@mkdir -p specification/
	python3 bin/load-markdown.py $@ $(LICENCE_MD)

DATATYPE_MD=$(sort $(wildcard content/datatype/*.md))
specification/datatype.csv:	$(DATATYPE_MD) bin/load-markdown.py
	python3 bin/load-markdown.py $@ $(DATATYPE_MD)

FIELD_MD=$(sort $(wildcard content/field/*.md))
specification/field.csv:	$(FIELD_MD) bin/load-markdown.py
	python3 bin/load-markdown.py $@ $(FIELD_MD)

PROJECT_MD=$(sort $(wildcard content/project/*.md))
specification/project.csv:	$(PROJECT_MD) bin/load-markdown.py
	python3 bin/load-markdown.py $@ $(PROJECT_MD)

PROJECT_STATUS_MD=$(sort $(wildcard content/project-status/*.md))
specification/project-status.csv:	$(PROJECT_STATUS_MD) bin/load-markdown.py
	python3 bin/load-markdown.py $@ $(PROJECT_STATUS_MD)

TYPOLOGY_MD=$(sort $(wildcard content/typology/*.md))
specification/typology.csv:	$(TYPOLOGY_MD) bin/load-markdown.py
	python3 bin/load-markdown.py $@ $(TYPOLOGY_MD)

THEME_MD=$(sort $(wildcard content/theme/*.md))
specification/theme.csv:	$(THEME_MD) bin/load-markdown.py
	python3 bin/load-markdown.py $@ $(THEME_MD)

DATAPACKAGE_MD=$(sort $(wildcard content/datapackage/*.md))
specification/datapackage.csv:	$(DATAPACKAGE_MD) bin/load-markdown.py
	python3 bin/load-markdown.py $@ $(DATAPACKAGE_MD)

SPECIFICATION_MD=$(sort $(wildcard content/specification/*.md))
specification/specification.csv:	$(SPECIFICATION_MD) bin/load-markdown.py
	@mkdir -p specification/
	python3 bin/load-markdown.py $@ $(SPECIFICATION_MD)


# made from the dataset.csv ..
DATASET_CSV=specification/dataset.csv
specification/collection.csv:	$(DATASET_CSV) bin/collection.py
	python3 bin/collection.py $@

specification/dataset-field.csv:	$(DATASET_MD) $(DATASET_CSV) bin/dataset-field.py
	python3 bin/dataset-field.py $@

specification/dataset-schema.csv:	$(DATASET_CSV) bin/dataset-schema.py
	python3 bin/dataset-schema.py $@

specification/schema.csv:	$(DATASET_CSV) bin/schema.py
	python3 bin/schema.py $@

specification/schema-field.csv:	$(DATASET_CSV) bin/schema-field.py
	python3 bin/schema-field.py $@

specification/pipeline.csv:	$(DATASET_CSV) bin/pipeline.py
	python3 bin/pipeline.py $@

specification/prefix.csv:	content/prefix.csv
	cp content/prefix.csv $@

specification/issue-type.csv:	content/issue-type.csv
	cp content/issue-type.csv $@

specification/severity.csv:	content/severity.csv
	cp content/severity.csv $@

specification/specification-status.csv:	content/specification-status.csv
	cp content/specification-status.csv $@

specification/provision-reason.csv:	content/provision-reason.csv
	cp content/provision-reason.csv $@

specification/provision-rule.csv:	content/provision-rule.csv
	cp content/provision-rule.csv $@

specification/include-exclude.csv:	content/include-exclude.csv
	cp content/include-exclude.csv $@

specification/role-organisation-rule.csv:	content/role-organisation-rule.csv
	cp content/role-organisation-rule.csv $@

specification/cohort.csv:	content/cohort.csv
	cp content/cohort.csv $@

specification/role.csv:	content/role.csv
	cp content/role.csv $@

# build organisations in a project
PROJECT_CSV=specification/project.csv
COHORT_CSV=specification/cohort.csv
specification/project-organisation.csv:	$(PROJECT_MD) $(PROJECT_CSV) $(COHORT_CSV) bin/project-organisation.py
	python3 bin/project-organisation.py $@

specification/role-organisation.csv:	bin/role-organisation.py specification/role-organisation-rule.csv $(CACHE_DIR)organisation.csv
	python3 bin/role-organisation.py $@

specification/provision.csv:	bin/provision.py specification/provision-rule.csv specification/project.csv specification/role-organisation.csv specification/project-organisation.csv
	python3 bin/provision.py $@

# LLC project from GOV.UK list
content/project/local-land-charges.md: var/llc.csv bin/llc-project.py
	python3 bin/llc-project.py var/llc.csv > $@

var/llc.csv: var/cache/llc.html var/cache/organisation.csv bin/llc-parse.py
	python3 bin/llc-parse.py var/cache/llc.html $@

var/cache/llc.html:
	curl -L 'https://www.gov.uk/government/publications/hm-land-registry-local-land-charges-programme/local-land-charges-programme' > $@

# localgov-drupal project from website list
content/project/localgov-drupal.md: var/lgd.csv bin/lgd-project.py
	@mkdir -p var/cache/
	python3 bin/lgd-project.py var/lgd.csv > $@

var/lgd.csv: var/cache/lgd.html var/cache/organisation.csv bin/lgd-parse.py
	python3 bin/lgd-parse.py var/cache/lgd.html $@

var/cache/lgd.html:
	@mkdir -p var/cache/
	curl -L 'https://localgovdrupal.org/community/our-councils' > $@

# deprecated
specification/organisation-dataset.csv:        specification/provision.csv
	cp specification/provision.csv $@

DATAPACKAGE_CSV=specification/datapackage.csv
specification/datapackage-dataset.csv:	$(DATAPACKAGE_CSV) bin/datapackage-dataset.py
	python3 bin/datapackage-dataset.py $@

commit-specification::
	git add specification
	git add data
	git add mermaid
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt specification $(shell date +%F)"; git push origin $(BRANCH))

clean clobber::
	rm -f specification/*.csv

# generate mermaid diagrams
MERMAID_MD=$(subst content/specification/,mermaid/,$(SPECIFICATION_MD))
render:: $(MERMAID_MD)

mermaid/%.md:	content/specification/%.md bin/specification-mermaid.py
	@mkdir -p mermaid/
	python3 bin/specification-mermaid.py $< > $@

clobber::
	rm -rf mermaid/

# generate SVG diagrams
SPECIFICATION_SVG=$(subst .md,/diagram.svg,$(subst content/,docs/,$(SPECIFICATION_MD)))
render:: $(SPECIFICATION_SVG)

docs/specification/%/diagram.svg:	content/specification/%.md bin/specification-svg.py
	@mkdir -p $(dir $@)
	python3 bin/specification-svg.py $< > $@

render:: docs/dataset/diagram.svg docs/model.svg

docs/dataset/diagram.svg: specification/dataset-field.csv bin/datasets-svg.py
	python3 bin/datasets-svg.py > $@

docs/model.svg: specification/dataset-field.csv bin/model-svg.py
	python3 bin/model-svg.py > $@

fields.json:
	python3 bin/dump-fields.py

extract-entity-ranges:
	python3 bin/extract-entity-ranges.py
