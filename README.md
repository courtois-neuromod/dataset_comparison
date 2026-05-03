# Dense NeuroAI Dataset Comparison

A systematic comparison of dense neuroAI datasets in terms of the volume and depth of neural data and cognitive states available. Built on the [`invoke`](https://www.pyinvoke.org/) task runner and [`airoh`](https://pypi.org/project/airoh/).

---

## Quick Start

```bash
uv sync
uv run invoke fetch
uv run invoke run
```

---

## Setup

```bash
uv sync
```

This creates a `.venv` and installs all dependencies from `pyproject.toml`.

---

## Tasks

| Task | Description |
|---|---|
| `fetch` | Validate all dataset YAML files in `source_data/datasets/` against the JSON schema |
| `run-notebooks` | Execute `summary.ipynb`, saving figures and tables to `output_data/` |
| `run` | Full pipeline: `fetch` → `run-notebooks` |
| `run-smoke` | Minimal end-to-end pass to verify the pipeline is wired correctly |
| `clean` | Remove generated outputs from `output_data/` |

Use `uv run invoke --list` or `uv run invoke --help <task>` for details.

---

## Data

- **Source data**: see [`source_data/CONTENT.md`](source_data/CONTENT.md)
- **Output data**: see [`output_data/CONTENT.md`](output_data/CONTENT.md)

---

## Folder Structure

| Folder / File | Description |
|---|---|
| `notebooks/` | Jupyter notebooks (one per figure/table group) |
| `source_data/` | Manually curated inputs — see [`source_data/CONTENT.md`](source_data/CONTENT.md) |
| `output_data/` | Generated figures and tables — see [`output_data/CONTENT.md`](output_data/CONTENT.md) |
| `tasks.py` | Invoke task definitions |
| `invoke.yaml` | Path configuration |
