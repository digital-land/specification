.PHONY: \
	collection\
	collect\
	clobber-today

# data sources
COLLECTION_DIR=collection/
ENDPOINT_CSV=$(COLLECTION_DIR)endpoint.csv

# collection log
LOG_DIR=$(COLLECTION_DIR)log/
LOG_FILES:=$(wildcard $(LOG_DIR)*/*.json)
LOG_FILES_TODAY:=$(LOG_DIR)$(shell date +%Y-%m-%d)/

# collected resources
RESOURCE_DIR=$(COLLECTION_DIR)resource/
RESOURCE_FILES:=$(wildcard $(RESOURCE_DIR)*)

first-pass:: collect

collect:	$(ENDPOINT_CSV)
	digital-land collect $(ENDPOINT_CSV)

clobber-today::
	rm -rf $(LOG_FILES_TODAY)
