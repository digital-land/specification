FRONTEND_URL=$(SOURCE_URL)/digital-land-frontend/master/application/

.PHONY: \
	render\
	server

TEMPLATE_FILES=$(wildcard templates/*)

second-pass::	render

render:	bin/render.py $(TEMPLATE_FILES) $(SPECIFICATION_FILES) $(DATASET_FILES)
	@-rm -rf ./docs/
	@-mkdir ./docs/
	python3 bin/render.py
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
