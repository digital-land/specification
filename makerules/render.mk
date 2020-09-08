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

# update makerules from source
update::
	curl -qsL '$(SOURCE_URL)/makerules/master/render.mk' > makerules/render.mk

# update frontend base templates
update::
	@-mkdir -p templates/
	curl -qsL '$(FRONTEND_URL)templates/base.html' > templates/base.html
	curl -qsL '$(FRONTEND_URL)templates/dlf-base.html' > templates/dlf-base.html
	curl -qsL '$(FRONTEND_URL)templates/dl-base.html' > templates/dl-base.html

# update frontend partial templates
update::
	@-mkdir -p templates/dl-partials/
	curl -qsL '$(FRONTEND_URL)templates/dl-partials/cookie-banner.html' > templates/dl-partials/cookie-banner.html
	curl -qsL '$(FRONTEND_URL)templates/dl-partials/dl-footer-code.html' > templates/dl-partials/dl-footer-code.html
	curl -qsL '$(FRONTEND_URL)templates/dl-partials/dl-header.html' > templates/dl-partials/dl-header.html
	curl -qsL '$(FRONTEND_URL)templates/dl-partials/dl-heading.html' > templates/dl-partials/dl-heading.html
	curl -qsL '$(FRONTEND_URL)templates/dl-partials/dl-page-feedback.html' > templates/dl-partials/dl-page-feedback.html
	curl -qsL '$(FRONTEND_URL)templates/dl-partials/phase-banner.html' > templates/dl-partials/phase-banner.html

# update fontend macros
update::
	@-mkdir -p templates/dl-macros/page-feedback/
	curl -qsL '$(FRONTEND_URL)templates/dl-macros/page-feedback/macro.jinja' > templates/dl-macros/page-feedback/macro.jinja
ifneq ("$(wildcard templates/dl-macros/heatmap/macro.jinja)","")
	curl -qsL '$(FRONTEND_URL)templates/dl-macros/heatmap/macro.jinja' > templates/dl-macros/heatmap/macro.jinja
endif
ifneq ("$(wildcard templates/dl-macros/data-item/)","")
	curl -qsL '$(FRONTEND_URL)templates/dl-macros/data-item/macro.jinja' > templates/dl-macros/data-item/macro.jinja
endif
