# Manuscript build: compiled from the proof record and generated data, never hand-typed.
#   make all    generate data, figures, tables; render Markdown; PDF + HTML; run checks
#   make pdf    render Markdown and convert to PDF/HTML (needs pandoc + xelatex)
#   make check  run the build checks (fails on unresolved placeholders, hand-entered numbers,
#               missing provenance, internal vocabulary, or a modified record import)
PY := python3
T  := tools

.PHONY: all data figures tables md pdf check clean

all: pdf check

data/constants.json: $(T)/gen_constants.py
	cd $(T) && $(PY) gen_constants.py

data/t7_check.json: $(T)/check_t7.py data/constants.json
	cd $(T) && $(PY) check_t7.py

data/values.json: $(T)/gen_values.py data/constants.json data/t7_check.json
	cd $(T) && $(PY) gen_values.py

data: data/values.json

figures: data
	cd $(T) && $(PY) gen_figures.py

tables: data
	cd $(T) && $(PY) gen_tables.py

md: data figures tables
	cd $(T) && $(PY) render.py

pdf: data figures tables
	cd $(T) && $(PY) render.py --pdf

check:
	cd $(T) && $(PY) record_import.py && $(PY) check.py

clean:
	rm -rf build/* data/* figures/*
