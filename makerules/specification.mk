.PHONY: \
	check

SPECIFICATION_FILES=$(wildcard specification/*.csv)

second-pass::	check

# check specification files are coherent
check::	bin/check.py $(SPECIFICATION_FILES)
	python3 bin/check.py

# update makerules from source
update::
	curl -qsL '$(SOURCE_URL)/makerules/master/specification.mk' > makerules/specification.mk
