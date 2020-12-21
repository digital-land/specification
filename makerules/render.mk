.PHONY: \
	render\
	server

ifneq ($(DATASET),)
ifeq ($(DATASET_DIR),)
DATASET_DIR=dataset/
endif

ifeq ($(DATASET_PATH),)
DATASET_PATH=$(DATASET_DIR)$(DATASET).csv
endif
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
	digital-land --pipeline-name $(DATASET) render --dataset-path $(DATASET_PATH)
endif
	@touch ./docs/.nojekyll

# serve docs for testing
server:
	cd docs && python3 -m http.server

clobber clean::
	rm -rf $(DATASET_PATH) $(DOCS_DIR)

makerules::
	curl -qsL '$(SOURCE_URL)/makerules/main/render.mk' > makerules/render.mk

commit-docs::
	git add docs
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt docs $(shell date +%F)"; git push origin $(BRANCH))
