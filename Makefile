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
	specification/severity.csv\
	specification/prefix.csv\
	specification/project.csv\
	specification/project-status.csv\
	specification/specification.csv\
	specification/specification-status.csv\
	specification/organisation-dataset.csv\
	specification/provision-reason.csv\
	specification/pipeline.csv\
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

specification/dataset-field.csv:	$(DATASET_CSV) bin/dataset-field.py
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

# hand-made for now, but could be inferred from the project/specification/LPA
specification/organisation-dataset.csv:	content/organisation-dataset.csv
	cp content/organisation-dataset.csv $@

specification/provision-reason.csv:	content/provision-reason.csv
	cp content/provision-reason.csv $@


DATAPACKAGE_CSV=specification/datapackage.csv
specification/datapackage-dataset.csv:	$(DATAPACKAGE_CSV) bin/datapackage-dataset.py
	python3 bin/datapackage-dataset.py $@

commit-specification::
	git add specification
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt specification $(shell date +%F)"; git push origin $(BRANCH))

clean clobber::
	rm -f specification/*.csv
