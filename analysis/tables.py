import yaml
import pandas as pd
from pathlib import Path


COLUMN_GROUPS = [
    ("Neuroimaging", "#4472C4", [
        ("fMRI",  "neuroimaging.fmri.per_subject_h",  "h"),
        ("EEG",   "neuroimaging.eeg.per_subject_h",   "h"),
        ("MEG",   "neuroimaging.meg.per_subject_h",   "h"),
        ("iEEG",  "neuroimaging.ieeg.per_subject_h",  "h"),
    ]),
    ("Stimuli", "#538135", [
        ("Images", "naturalistic_stimuli.images.per_subject_unique",           "#img"),
        ("Video",  "naturalistic_stimuli.video.per_subject_unique",            "h"),
        ("Audio",  "naturalistic_stimuli.audio.per_subject_unique",            "h"),
        ("Speech", "naturalistic_stimuli.speech_listening.per_subject_unique", "h"),
        ("Text",   "naturalistic_stimuli.text_reading.per_subject_unique",     "h"),
        ("Rest",   "naturalistic_stimuli.resting_state.per_subject_unique",    "h"),
    ]),
    ("Responses", "#C55A11", [
        ("Tasks", "responses.controlled_tasks.per_subject_unique", "#cond"),
        ("Games", "responses.game_actions.per_subject_unique",     "h"),
    ]),
    ("Physiology", "#7030A0", [
        ("ECG",   "physiology.ecg.per_subject_unique",            "h"),
        ("Resp.", "physiology.respiration.per_subject_unique",    "h"),
        ("PPG",   "physiology.plethysmograph.per_subject_unique", "h"),
        ("EDA",   "physiology.eda.per_subject_unique",            "h"),
        ("Eye",   "physiology.eye_tracking.per_subject_unique",   "h"),
    ]),
]


def _get_nested(d, path):
    for key in path.split("."):
        if not isinstance(d, dict) or key not in d:
            return None
        d = d[key]
    return d


def build_tidy_table(source_dir: Path) -> pd.DataFrame:
    """Load all dataset YAMLs and return a tidy long-format DataFrame."""
    datasets = []
    for yaml_file in sorted(Path(source_dir).glob("*.yaml")):
        with open(yaml_file) as f:
            datasets.append(yaml.safe_load(f))

    rows = []
    for ds in datasets:
        for group_name, group_color, fields in COLUMN_GROUPS:
            for label, dotpath, unit in fields:
                value = _get_nested(ds, dotpath)
                rows.append({
                    "dataset": ds.get("name", "?"),
                    "group": group_name,
                    "group_color": group_color,
                    "modality": label,
                    "dotpath": dotpath,
                    "unit": unit,
                    "value": value,
                })

    return pd.DataFrame(rows)
