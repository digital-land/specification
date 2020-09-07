.PHONY: \
	collection\
	collect\
	clobber-today

# data sources
COLLECTION_DIR=collection/
SOURCE_CSV=$(COLLECTION_DIR)source.csv
ENDPOINT_CSV=$(COLLECTION_DIR)endpoint.csv

# collection log
LOG_DIR=$(COLLECTION_DIR)log/
LOG_FILES:=$(wildcard $(LOG_DIR)*/*.json)
LOG_FILES_TODAY:=$(LOG_DIR)$(shell date +%Y-%m-%d)/

# collected resources
RESOURCE_DIR=$(COLLECTION_DIR)resource/
RESOURCE_FILES:=$(wildcard $(RESOURCE_DIR)*)

first-pass:: collect

collect:	$(SOURCE_CSV) $(ENDPOINT_CSV)
	digital-land collect $(ENDPOINT_CSV)

clobber-today::
	rm -rf $(LOG_FILES_TODAY)

# create a link to the pipleline source
dev::
ifndef VIRTUAL_ENV
	$(error not in a virtual environment)
endif
	rm -rf ${VIRTUAL_ENV}/src/digital-land
	ln -s ${PWD}/../pipeline/ ${VIRTUAL_ENV}/src/digital-land

# update makerules from source
update::
	curl -qsL '$(SOURCE_URL)/makerules/master/collection.mk' > makerules/collection.mk
