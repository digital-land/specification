SOURCE_URL=https://raw.githubusercontent.com/digital-land/

.PHONY: \
	makerules\
	init\
	first-pass\
	second-pass\
	clobber\
	clean\
	commit-makerules\
	prune

# keep intermediate files
.SECONDARY:

# don't keep targets build with an error
.DELETE_ON_ERROR:

# work in UTF-8
LANGUAGE := en_GB.UTF-8
LANG := C.UTF-8

# for consistent collation on different machines
LC_COLLATE := C.UTF-8

# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

all:: first-pass second-pass

first-pass::
	@:

# restart the make process to pick-up collected files
second-pass::
	@:

# initialise
init::
ifneq (,$(wildcard requirements.txt))
	pip3 install --upgrade -r requirements.txt
endif
ifneq (,$(wildcard setup.py))
	pip install -e .
endif

submodules::
	git submodule update --init --recursive --remote

# remove targets, force relink
clobber::
	@:

# remove intermediate files
clean::
	@:

# prune back to source code
prune::
	rm -rf ./var $(VALIDATION_DIR)

# update makerules from source
makerules::
	curl -qsL '$(SOURCE_URL)/makerules/main/makerules.mk' > makerules/makerules.mk

ifeq (,$(wildcard ./makerules/specification.mk))
# update local copies of specification files
init::
	@mkdir -p specification/
	curl -qsL '$(SOURCE_URL)/specification/main/specification/dataset.csv' > specification/dataset.csv
	curl -qsL '$(SOURCE_URL)/specification/main/specification/dataset-schema.csv' > specification/dataset-schema.csv
	curl -qsL '$(SOURCE_URL)/specification/main/specification/schema.csv' > specification/schema.csv
	curl -qsL '$(SOURCE_URL)/specification/main/specification/schema-field.csv' > specification/schema-field.csv
	curl -qsL '$(SOURCE_URL)/specification/main/specification/field.csv' > specification/field.csv
	curl -qsL '$(SOURCE_URL)/specification/main/specification/datatype.csv' > specification/datatype.csv
	curl -qsL '$(SOURCE_URL)/specification/main/specification/typology.csv' > specification/typology.csv
	curl -qsL '$(SOURCE_URL)/specification/main/specification/pipeline.csv' > specification/pipeline.csv
endif

commit-makerules::
	git add makerules
	git diff --quiet && git diff --staged --quiet || (git commit -m "Updated makerules $(shell date +%F)"; git push origin $(BRANCH))

commit-collection::
	@:
