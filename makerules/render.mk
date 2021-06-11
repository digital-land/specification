.PHONY: \
	render\
	server


ifeq ($(DATASET),)
DATASET=$(REPOSITORY)
endif

ifeq ($(COLLECTION),)
COLLECTION=$(DATASET)
endif

ifeq ($(DATASET_PATH),)
ifeq ($(NO_DATASET),)
DATASET_PATH=$(DATASET_DIR)$(DATASET).sqlite3
endif
endif

ifeq ($(DATASET_URL),)
DATASET_URL='https://collection-dataset.s3.eu-west-2.amazonaws.com/$(COLLECTION)-collection/dataset/$(DATASET).sqlite3'
endif

ifeq ($(DATASET_DIR),)
DATASET_DIR=dataset/
endif

ifeq ($(DOCS_DIR),)
DOCS_DIR=./docs/
endif

TEMPLATE_FILES=$(wildcard templates/*)

second-pass:: render

render:: $(TEMPLATE_FILES) $(SPECIFICATION_FILES) $(DATASET_FILES) $(DATASET_PATH)
	@-rm -rf $(DOCS_DIR)
	@-mkdir -p $(DOCS_DIR)
ifneq ($(RENDER_COMMAND),)
	$(RENDER_COMMAND)
else
	digital-land --pipeline-name $(DATASET) render --dataset-path $(DATASET_PATH) $(RENDER_FLAGS)
endif
	@touch ./docs/.nojekyll

# serve docs for testing
server:
	cd docs && python3 -m http.server

clobber clean:: clobber-dataset clobber-docs
	
clobber-dataset::
	rm -rf $(DATASET_PATH)
	
clobber-docs::
	rm -rf $(DOCS_DIR)

makerules::
	curl -qfsL '$(SOURCE_URL)/makerules/main/render.mk' > makerules/render.mk

commit-docs::
	git add docs
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt docs $(shell date +%F)"; git push origin $(BRANCH))

ifneq ($(DATASET_PATH),)
$(DATASET_PATH):
	mkdir -p $(DATASET_DIR)
	curl -qfsL $(DATASET_URL) > $(DATASET_PATH)
endif

# TBD: remove this rule
# -- templates should have relative links to ensure we are testing deployed pages locally
local::
	@rm -rf $(DOCS_DIR)
	@mkdir $(DOCS_DIR)
	digital-land --pipeline-name $(DATASET) render --dataset-path $(DATASET_PATH) --local
