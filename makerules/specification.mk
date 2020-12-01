.PHONY: \
	check

SPECIFICATION_FILES=$(wildcard specification/*.csv)

second-pass::	check

# check specification files are coherent
check::	bin/check.py $(SPECIFICATION_FILES)
	python3 bin/check.py

makerules::
	curl -qsL '$(SOURCE_URL)/makerules/main/specification.mk' > makerules/specification.mk
