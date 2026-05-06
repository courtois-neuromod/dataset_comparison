"""Shared bubble-chart visualisation helpers for dataset comparison notebooks."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bubble area = UNIT_SCALES[unit] * sqrt(value)
# MAX_S caps at ~1000 h or ~100k images; MIN_S sets the smallest visible dot.
UNIT_SCALES = {
    "h":     200,
    "#img":  19,
    "#cond": 50,
}
MIN_S = 60
MAX_S = 6000


def value_to_size(value, unit):
    """Return (scatter_s, fontsize); area ∝ sqrt(value), clamped to [MIN_S, MAX_S]."""
    s = min(MAX_S, max(MIN_S, UNIT_SCALES[unit] * np.sqrt(value)))
    if s < 300:
        fs = 5.5
    elif s < 800:
        fs = 7.0
    elif s < 2000:
        fs = 8.0
    else:
        fs = 9.0
    return s, fs


def fmt(value, unit):
    if unit in ("#img", "#cond"):
        return f"{value / 1000:.1f}k" if value >= 1000 else str(int(value))
    if value >= 10:
        return f"{value:.0f}h"
    if value >= 1:
        return f"{value:.1f}h"
    return f"{value * 60:.0f}m"


def make_bubble_chart(column_groups, pivot, datasets_list, title, out_path,
                      sort_by=None):
    """Draw and save a bubble chart.

    Parameters
    ----------
    column_groups : list of (group_name, color, [(label, dotpath, unit), ...])
    pivot         : DataFrame indexed by dataset name, columns are dotpaths
    datasets_list : list of dataset names to include
    title         : figure title string
    out_path      : Path to save the PNG
    sort_by       : dotpath to sort rows by (descending); defaults to first fMRI
                    per-subject column found, or alphabetical if none.
    """
    all_cols = []
    group_spans = []
    for group_name, color, fields in column_groups:
        start = len(all_cols)
        for label, path, unit in fields:
            all_cols.append((label, path, unit, color))
        group_spans.append((group_name, color, start, len(all_cols) - 1))
    n_cols = len(all_cols)

    if sort_by is None:
        sort_by = next(
            (p for _, p, _, _ in all_cols if "fmri" in p and "per_subject" in p),
            None,
        )
    if sort_by and sort_by in pivot.columns:
        datasets_sorted = sorted(
            datasets_list,
            key=lambda d: pivot.loc[d, sort_by] if d in pivot.index else 0,
            reverse=True,
        )
    else:
        datasets_sorted = sorted(datasets_list)
    n_ds = len(datasets_sorted)

    COL_W, ROW_H = 0.78, 0.80
    LABEL_W = 3.2
    HEADER_H = 1.6

    fig, ax = plt.subplots(figsize=(LABEL_W + n_cols * COL_W, HEADER_H + n_ds * ROW_H))

    for gname, color, c0, c1 in group_spans:
        ax.axvspan(c0 - 0.5, c1 + 0.5, color=color, alpha=0.07, zorder=0)

    for gname, color, c0, c1 in group_spans:
        ax.text((c0 + c1) / 2, n_ds + 0.55, gname,
                ha="center", va="center", fontsize=11, fontweight="bold", color=color)

    ax.set_xticks(range(n_cols))
    ax.set_xticklabels([c[0] for c in all_cols], rotation=45, ha="right", fontsize=9)
    for tick, (_, _, _, color) in zip(ax.get_xticklabels(), all_cols):
        tick.set_color(color)

    for row_i, ds_name in enumerate(datasets_sorted):
        y = n_ds - 1 - row_i
        ax.text(-0.52, y, ds_name, ha="right", va="center", fontsize=9)
        for col_j, (label, path, unit, color) in enumerate(all_cols):
            if path not in pivot.columns or ds_name not in pivot.index:
                continue
            value = pivot.loc[ds_name, path]
            if pd.isna(value) or value == 0:
                continue
            s, fs = value_to_size(value, unit)
            ax.scatter(col_j, y, s=s, color=color, alpha=0.75, linewidths=0, zorder=3)
            if s <= MIN_S:
                ax.text(col_j + 0.12, y, fmt(value, unit),
                        ha="left", va="center", fontsize=fs, fontweight="bold",
                        color="black", zorder=4)
            else:
                ax.text(col_j, y, fmt(value, unit),
                        ha="center", va="center", fontsize=fs, fontweight="bold",
                        color="white", zorder=4)

    ax.set_yticks([])
    ax.set_xlim(-0.5, n_cols - 0.5)
    ax.set_ylim(-0.55, n_ds + 1.0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(axis="x", linestyle=":", alpha=0.35, zorder=1)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)

    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Saved {out_path.name}")


def make_neuroimaging_depthvsbreadth(pivot_per_subject, pivot_total, datasets_list, out_path,
                      highlight="CNeuroMod"):
    """Scatter plot: neuroimaging hours per subject (x) vs number of subjects (y).

    Neuroimaging hours sum fMRI, EEG, MEG, and iEEG. Iso-hours lines show
    constant total neuroimaging hours: n_subjects = H / hours_per_subject.

    Parameters
    ----------
    pivot_per_subject : DataFrame indexed by dataset, columns are dotpaths
    pivot_total       : DataFrame indexed by dataset, columns are dotpaths
    datasets_list     : list of dataset names
    out_path          : Path to save the PNG
    highlight         : dataset name to highlight (drawn larger, distinct color)
    """
    PER_SUBJECT_PATHS = [
        "neuroimaging.fmri.per_subject_h",
        "neuroimaging.eeg.per_subject_h",
        "neuroimaging.meg.per_subject_h",
        "neuroimaging.ieeg.per_subject_h",
    ]
    TOTAL_PATHS = [
        "neuroimaging.fmri.total_h",
        "neuroimaging.eeg.total_h",
        "neuroimaging.meg.total_h",
        "neuroimaging.ieeg.total_h",
    ]

    def _sum_paths(pivot, ds, paths):
        total = 0.0
        for p in paths:
            if ds in pivot.index and p in pivot.columns:
                v = pivot.loc[ds, p]
                if pd.notna(v):
                    total += float(v)
        return total

    points = []
    for ds in datasets_list:
        x = _sum_paths(pivot_per_subject, ds, PER_SUBJECT_PATHS)
        y_total = _sum_paths(pivot_total, ds, TOTAL_PATHS)
        if x > 0 and y_total > 0:
            points.append((ds, x, float(y_total / x)))

    if not points:
        print("No neuroimaging data found — skipping scatter plot.")
        return

    fig, ax = plt.subplots(figsize=(6, 5))

    # Iso-hours hyperbolas: n_subjects = H / hours_per_subject
    x_min = min(p[1] for p in points)
    x_max = max(p[1] for p in points)
    x_pad = np.linspace(x_min * 0.4, x_max * 2.5, 200)
    for H in [50, 200, 1000, 5000, 10000]:
        label = f"{H}h" if H < 1000 else f"{H // 1000}kh"
        y_iso = H / x_pad
        ax.plot(x_pad, y_iso, color="grey", linewidth=0.7,
                linestyle="--", alpha=0.4, zorder=1)
        ax.text(x_pad[-1], y_iso[-1], f"  {label}",
                va="center", fontsize=7, color="grey", alpha=0.7)

    for ds, x, n_sub in points:
        is_highlight = ds == highlight
        color = "#e63946" if is_highlight else "#4472C4"
        marker_size = 120 if is_highlight else 60
        zorder = 4 if is_highlight else 3
        ax.scatter(x, n_sub, s=marker_size, color=color, zorder=zorder,
                   edgecolors="white", linewidths=0.8)
        va = "bottom" if not is_highlight else "top"
        offset = (0, 6) if not is_highlight else (0, -6)
        ax.annotate(ds, (x, n_sub), xytext=offset, textcoords="offset points",
                    ha="center", va=va, fontsize=8,
                    fontweight="bold" if is_highlight else "normal",
                    color=color, zorder=5)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Neuroimaging hours per subject (fMRI + EEG + MEG + iEEG)", fontsize=10)
    ax.set_ylabel("Number of subjects", fontsize=10)
    ax.set_title("Neuroimaging depth vs. breadth", fontsize=12, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Saved {out_path.name}")


def make_legend(out_path):
    """Save a standalone bubble-size legend figure."""
    LEGEND_SETS = [
        ("Hours (h)",      "h",      [1, 10, 50, 200, 1000], "#4472C4"),
        ("Images (#)",     "#img",   [1000, 10000, 50000, 100000], "#538135"),
        ("Conditions (#)", "#cond",  [10, 100, 500],               "#C55A11"),
    ]

    n_sets = len(LEGEND_SETS)
    max_n = max(len(vals) for _, _, vals, _ in LEGEND_SETS)
    COL_SP = 2.0
    ROW_SP = 2.2

    fig_w = 2.2 + max_n * COL_SP * 0.75
    fig_h = n_sets * ROW_SP * 0.65 + 0.7

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(-1.1, (max_n - 0.5) * COL_SP)
    ax.set_ylim(-0.8, n_sets * ROW_SP - 0.2)
    ax.set_axis_off()
    ax.set_title("Bubble size legend", fontsize=12, fontweight="bold", pad=8)

    for set_i, (set_name, unit, ref_values, color) in enumerate(LEGEND_SETS):
        y = (n_sets - 1 - set_i) * ROW_SP + ROW_SP / 2
        ax.text(-0.7, y, set_name, ha="right", va="center",
                fontsize=10, fontweight="bold", color=color)
        for col_j, val in enumerate(ref_values):
            x = col_j * COL_SP
            s, fs = value_to_size(val, unit)
            ax.scatter(x, y, s=s, color=color, alpha=0.75, linewidths=0, zorder=3)
            ax.text(x, y, fmt(val, unit),
                    ha="center", va="center", fontsize=fs, fontweight="bold",
                    color="white", zorder=4)

    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Saved {out_path.name}")
