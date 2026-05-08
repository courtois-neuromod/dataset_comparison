"""Parse a BibTeX file and produce a tidy table of papers using CNeuroMod data, by year and entry type."""

import re
from pathlib import Path

import pandas as pd


_PREPRINT = re.compile(r"biorxiv|arxiv|psyarxiv", re.IGNORECASE)
_THESIS = re.compile(
    r"scholaris|theses\.hal|repozitorij|teses\.|umontreal\.ca|thesis", re.IGNORECASE
)
_CONFERENCE = re.compile(r"openreview\.net|proceedings|neurips|icml|iclr", re.IGNORECASE)


def _classify(entry_type: str, fields: dict) -> str:
    etype = entry_type.upper()
    if etype == "INPROCEEDINGS":
        return "Conference"
    if etype == "INCOLLECTION":
        return "Book Chapter"
    if etype == "MISC":
        return "Theses & Other"
    if etype != "ARTICLE":
        return "Theses & Other"

    combined = " ".join([
        fields.get("journal", ""),
        fields.get("institution", ""),
        fields.get("publisher", ""),
    ])
    if _PREPRINT.search(combined):
        return "Preprint"
    if _THESIS.search(combined):
        return "Thesis"
    if _CONFERENCE.search(combined):
        return "Conference"
    return "Journal"


def _parse_fields(fields_text: str) -> dict:
    """Extract key=value pairs from a BibTeX entry body (handles nested braces)."""
    fields: dict = {}
    # Match field_name = { ... } | "..." | digits
    for m in re.finditer(
        r"(\w+)\s*=\s*(?:\{((?:[^{}]|\{[^{}]*\})*)\}|\"([^\"]*)\"|(\d+))",
        fields_text,
        re.DOTALL,
    ):
        key = m.group(1).lower()
        value = m.group(2) or m.group(3) or m.group(4) or ""
        fields[key] = value.strip()
    return fields


def parse_bib_to_table(bib_path: Path) -> pd.DataFrame:
    """Parse *bib_path* and return a tidy DataFrame with columns year, type, count."""
    text = Path(bib_path).read_text(encoding="utf-8")

    records = []
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", text, re.DOTALL):
        entry_type = m.group(1)
        fields = _parse_fields(m.group(3))

        year_raw = fields.get("year", "")
        try:
            year = int(year_raw)
        except (ValueError, TypeError):
            year = None

        ptype = _classify(entry_type, fields)
        records.append({"year": year, "type": ptype})

    df = pd.DataFrame(records)
    tidy = (
        df.groupby(["year", "type"], dropna=False)
        .size()
        .reset_index(name="count")
    )
    return tidy
