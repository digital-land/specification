NO_DATASET=true
RENDER_COMMAND=python3 ./bin/render.py

include makerules/makerules.mk
include makerules/collection.mk
include makerules/specification.mk
include makerules/render.mk
