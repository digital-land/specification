.PHONY: \
	render\
	server

ifeq ($(DATASET),)
DATASET=$(PIPELINE_NAME)
endif

ifeq ($(DATASET_PATH),)
DATASET_PATH=$(DATASET_DIR)/$(DATASET).csv
endif

TEMPLATE_FILES=$(wildcard templates/*)

second-pass:: render

render: $(TEMPLATE_FILES) $(SPECIFICATION_FILES) $(DATASET_FILES)
	@-rm -rf ./docs/
	@-mkdir ./docs/
	digital-land --pipeline-name brownfield-land render --dataset-path $(DATASET_PATH)
	@touch ./docs/.nojekyll

# serve docs for testing
server:
	cd docs && python3 -m http.server

clobber clean::
	rm -rf ./docs/ .cache/

makerules::
	curl -qsL '$(SOURCE_URL)/makerules/main/render.mk' > makerules/render.mk

commit-docs::
	git add docs
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt docs $(shell date +%F)"; git push origin $(BRANCH))
