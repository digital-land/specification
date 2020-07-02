.PHONY: \
	init\
	first-pass\
	second-pass\
	clobber\
	clean\
	prune

# keep intermediate files
.SECONDARY:

# don't keep targets build with an error
.DELETE_ON_ERROR:

# work in UTF-8
LANGUAGE := en_GB.UTF-8
LANG := C.UTF-8

# for consistent collation on different machines
LC_COLLATE := C.UTF-8

all:: first-pass second-pass

first-pass::
	@:

# restart the make process to pick-up collected files
second-pass::
	@:

# initialise
init::
	pip3 install --upgrade -r requirements.txt

# remove targets, force relink
clobber::
	@:

# remove intermediate files
clean::
	@:

# prune back to source code
prune::
	rm -rf ./var $(VALIDATION_DIR)
