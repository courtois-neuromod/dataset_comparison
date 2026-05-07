import yaml
import pandas as pd
from pathlib import Path


COLUMN_GROUPS_PER_SUBJECT = [
    ("Neuroimaging", "#4472C4", [
        ("fMRI",  "neuroimaging.fmri.per_subject_h",  "h"),
        ("EEG",   "neuroimaging.eeg.per_subject_h",   "h"),
        ("MEG",   "neuroimaging.meg.per_subject_h",   "h"),
        ("iEEG",  "neuroimaging.ieeg.per_subject_h",  "h"),
    ]),
    ("Passive", "#538135", [
        ("Images", "passive.images.per_subject_unique",           "#img"),
        ("Video",  "passive.video.per_subject_unique",            "h"),
        ("Audio",  "passive.audio.per_subject_unique",            "h"),
        ("Speech", "passive.speech_listening.per_subject_unique", "h"),
        ("Text",   "passive.text_reading.per_subject_unique",     "h"),
        ("Rest",   "passive.resting_state.per_subject_unique",    "h"),
    ]),
    ("Active", "#C55A11", [
        ("Controlled", "active.controlled.per_subject_unique", "h"),
        ("Games",      "active.game_actions.per_subject_unique",  "h"),
    ]),
    ("Physiology", "#7030A0", [
        ("ECG",   "physiology.ecg.per_subject_h",            "h"),
        ("Resp.", "physiology.respiration.per_subject_h",    "h"),
        ("PPG",   "physiology.plethysmograph.per_subject_h", "h"),
        ("EDA",   "physiology.eda.per_subject_h",            "h"),
        ("Eye",   "physiology.eye_tracking.per_subject_h",   "h"),
    ]),
]

COLUMN_GROUPS_TOTAL = [
    ("Neuroimaging", "#4472C4", [
        ("fMRI",  "neuroimaging.fmri.total_h",  "h"),
        ("EEG",   "neuroimaging.eeg.total_h",   "h"),
        ("MEG",   "neuroimaging.meg.total_h",   "h"),
        ("iEEG",  "neuroimaging.ieeg.total_h",  "h"),
    ]),
    ("Passive", "#538135", [
        ("Images", "passive.images.total_unique",           "#img"),
        ("Video",  "passive.video.total_unique",            "h"),
        ("Audio",  "passive.audio.total_unique",            "h"),
        ("Speech", "passive.speech_listening.total_unique", "h"),
        ("Text",   "passive.text_reading.total_unique",     "h"),
        ("Rest",   "passive.resting_state.total_unique",    "h"),
    ]),
    ("Active", "#C55A11", [
        ("Controlled", "active.controlled.total_unique", "h"),
        ("Games",      "active.game_actions.total_unique",  "h"),
    ]),
    ("Physiology", "#7030A0", [
        ("ECG",   "physiology.ecg.total_h",            "h"),
        ("Resp.", "physiology.respiration.total_h",    "h"),
        ("PPG",   "physiology.plethysmograph.total_h", "h"),
        ("EDA",   "physiology.eda.total_h",            "h"),
        ("Eye",   "physiology.eye_tracking.total_h",   "h"),
    ]),
]


def _get_nested(d, path):
    for key in path.split("."):
        if not isinstance(d, dict) or key not in d:
            return None
        d = d[key]
    return d


def _build_rows(datasets: list, column_groups: list) -> list:
    rows = []
    for ds in datasets:
        for group_name, group_color, fields in column_groups:
            for label, dotpath, unit in fields:
                value = _get_nested(ds, dotpath)
                rows.append({
                    "dataset": ds.get("short_name", ds.get("name", "?")),
                    "group": group_name,
                    "group_color": group_color,
                    "modality": label,
                    "dotpath": dotpath,
                    "unit": unit,
                    "value": value,
                })
    return rows


def build_tidy_table(source_dir: Path, column_groups: list, extra_yaml_files=None) -> pd.DataFrame:
    """Load all dataset YAMLs and return a tidy long-format DataFrame."""
    datasets = []
    for yaml_file in sorted(Path(source_dir).glob("*.yaml")):
        with open(yaml_file) as f:
            datasets.append(yaml.safe_load(f))
    for yaml_file in (extra_yaml_files or []):
        with open(yaml_file) as f:
            datasets.append(yaml.safe_load(f))
    return pd.DataFrame(_build_rows(datasets, column_groups))


def aggregate_cneuromod_yaml(cneuromod_dir: Path) -> dict:
    """Aggregate all cneuromod dataset_info.yaml stats into one schema-compatible dict."""
    raw = []
    for info_file in sorted(Path(cneuromod_dir).glob("*/dataset_info.yaml")):
        with open(info_file) as f:
            raw.append(yaml.safe_load(f).get("stats", {}))

    def _sum_dicts(dicts):
        result = {}
        for key in set(k for d in dicts for k in d):
            values = [d[key] for d in dicts if key in d]
            if all(isinstance(v, dict) for v in values):
                result[key] = _sum_dicts(values)
            elif all(isinstance(v, (int, float)) for v in values):
                result[key] = sum(values)
        return result

    combined = _sum_dicts([{k: v for k, v in d.items() if k != "subjects_n"} for d in raw])
    combined["subjects_n"] = raw[0].get("subjects_n", 6) if raw else 6
    combined["name"] = "CNeuroMod"
    return combined


def load_cneuromod_datasets(cneuromod_dir: Path) -> list:
    """Load datasets from cneuromod.all submodule dataset_info.yaml files.

    Each file's `stats` block is used as the dataset dict; the folder name
    becomes the `name` field.
    """
    datasets = []
    for info_file in sorted(Path(cneuromod_dir).glob("*/dataset_info.yaml")):
        with open(info_file) as f:
            data = yaml.safe_load(f)
        stats = data.get("stats", {})
        stats["name"] = info_file.parent.name
        datasets.append(stats)
    return datasets


def build_cneuromod_tidy_table(cneuromod_dir: Path, column_groups: list) -> pd.DataFrame:
    """Load cneuromod datasets and return a tidy long-format DataFrame."""
    return pd.DataFrame(_build_rows(load_cneuromod_datasets(cneuromod_dir), column_groups))
