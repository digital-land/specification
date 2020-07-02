COLLECTION=specification

#-include makerules/$(COLLECTION).mk

all::	check

include makerules/makerules.mk
include makerules/collection.mk

check:
	python3 bin/check.py
