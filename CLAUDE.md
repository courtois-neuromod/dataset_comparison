# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This project systematically compares dense neuroAI datasets in terms of the volume and depth of neural data and cognitive states available. It is built on the [`invoke`](https://www.pyinvoke.org/) task runner. The `airoh` pip package provides reusable invoke tasks; this repo customizes them via `tasks.py` and `invoke.yaml`.

**Package manager:** `uv` (see `pyproject.toml`).

**Pipeline:** `fetch` validates all YAML files in `source_data/datasets/` against `source_data/schema.json`; `run-notebooks` executes `notebooks/summary.ipynb` to produce figures and tables in `output_data/`. All source data is manually curated and version-controlled via git.

## Dataset Assets

Each dataset has two files in `source_data/datasets/`:

- `<name>.yaml` — structured data entry, validated against `source_data/schema.json`. Only populate fields that are relevant to the dataset (e.g. omit `neuroimaging.meg` entirely if the dataset has no MEG).
- `<name>.md` — markdown sidecar that justifies every value in the YAML with direct quotes from the corresponding publication(s) or official documentation.

The markdown sidecar should:
- Cover each field present in the YAML
- Justify every number with a direct quote from the publication or documentation
- Cite the source of each quote (paper title/DOI or URL)
- Flag any values that could not be confirmed or are approximate

When asked to work on a dataset entry:
1. Identify which schema fields are relevant to the dataset
2. Search for the paper(s) and/or documentation to find supporting quotes
3. Draft or update `<name>.yaml` with only the relevant fields
4. Draft or update `<name>.md` with quoted evidence for each field
5. Flag any fields where information could not be found or is ambiguous

## Setup

```bash
# uv (recommended):
uv sync

# pip:
pip install -r requirements.txt
```

## Common Commands

With `uv`:
```bash
uv run invoke fetch           # Validate dataset YAML files against schema
uv run invoke run             # Full pipeline (fetch → run-notebooks)
uv run invoke run-notebooks   # Execute notebooks, save figures to output_data/
uv run invoke clean           # Remove output_data/ contents
uv run invoke --list          # Show all available tasks
```

Without `uv` (activate your environment first):
```bash
invoke fetch              # Validate dataset YAML files against schema
invoke run                # Full pipeline
invoke run-notebooks      # Execute notebooks, save figures to output_data/
invoke clean              # Remove output_data/ contents
invoke --list             # Show all available tasks
```

## Architecture

**Execution flow:** `invoke run` triggers the project's analysis pipeline via `pre=` dependencies declared in `tasks.py`. The three permanent tasks — `fetch`, `run`, `clean` — are always present; intermediate steps are project-specific.

- `invoke.yaml` — all path config (`output_data_dir`, `source_data_dir`, `notebooks_dir`)
- `tasks.py` — project-specific invoke tasks; imports reusable tasks from `airoh.utils`
- `source_data/schema.json` — JSON Schema for dataset YAML files; edit here to add new modalities or fields
- `notebooks/` — Jupyter notebooks executed by `run_notebooks` via `airoh.utils.run_notebooks`; notebooks receive `OUTPUT_DATA_DIR` and `SOURCE_DATA_DIR` as environment variables
- `source_data/CONTENT.md` and `output_data/CONTENT.md` — authoritative docs for what each data folder contains; update these when data assets change, do not duplicate their content elsewhere

**Adding a new schema field:** edit `source_data/schema.json`, then update any existing YAML files that should carry the new field.

**Adding a new analysis step:** create or extend a notebook in `notebooks/`, add an invoke task in `tasks.py`, and wire it into the `pre=` chain on `run`.

**README.md** is the user-facing documentation for this project. Any structural or workflow changes — new tasks, renamed folders, updated commands, new dependencies — must be reflected there. For data folder contents, point to `source_data/CONTENT.md` and `output_data/CONTENT.md` rather than duplicating their content inline.
