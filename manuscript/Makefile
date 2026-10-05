# Manuscript build: compiled from the proof record and generated data, never hand-typed.
#   make all    generate data, figures, tables; render Markdown; PDF + HTML; run checks
#   make pdf    render Markdown and convert to PDF/HTML (needs pandoc + xelatex)
#   make check  run the build checks (fails on unresolved placeholders, hand-entered numbers,
#               missing provenance, internal vocabulary, or a modified record import)
PY := python3
T  := tools

.PHONY: all data figures tables md pdf check clean heavy second repro

all: pdf check

data/constants.json: $(T)/gen_constants.py
	cd $(T) && $(PY) gen_constants.py

data/t7_check.json: $(T)/check_t7.py data/constants.json
	cd $(T) && $(PY) check_t7.py

data/frozen_convergence.json: $(T)/extract_frozen_convergence.py
	cd $(T) && $(PY) extract_frozen_convergence.py

# second_path.json and repro_record.json are committed heavy outputs (make second / make repro);
# they are prerequisites only so that regenerating them refreshes the derived values.
data/values.json: $(T)/gen_values.py data/constants.json data/t7_check.json data/frozen_convergence.json \
                  data/second_path.json data/repro_record.json
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

check: md
	cd $(T) && $(PY) record_import.py && $(PY) test_firewalls.py && $(PY) check.py

# The BRI1 science is frozen. The build repairs the manuscript from the frozen evidence and does
# not re-open numerical verification. Reproducibility artifacts (committed; regenerate only deliberately):
#   make second   S6 manuscript-stage cross-check (second code path), a few minutes
#   make repro    S6 re-run of the record script behind the authoritative JSON, ~20 minutes
# tools/convergence_ladder.py is archived only (data/reproducibility/); it is not a build target.
heavy: second repro

second:
	cd $(T) && $(PY) second_path.py

repro:
	cd $(T) && $(PY) repro_record.py

# clean removes only the cheap generated outputs; the heavy outputs above are kept.
clean:
	rm -rf build/* figures/* data/tables data/values.json data/constants.json data/t7_check.json \
	       data/figures.json data/tables.json data/frozen_convergence.json
