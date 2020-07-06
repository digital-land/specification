.PHONY: \
	check\
	render\
	server

TEMPLATE_FILES=$(wildcard templates/*)
SPECIFICATION_FILES=$(wildcard specification/*.csv)

second-pass::	check render

check:	bin/check.py $(SPECIFICATION_FILES)
	python3 bin/check.py

render:	bin/render.py $(TEMPLATE_FILES) $(SPECIFICATION_FILES)
	@-rm -rf ./docs/
	@-mkdir ./docs/
	python3 bin/render.py
	@touch ./docs/.nojekyll

server:
	cd docs && python3 -m http.server

clobber clean::
	rm -rf docs .cache
