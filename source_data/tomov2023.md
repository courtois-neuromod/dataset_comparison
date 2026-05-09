# Atari Game Learning fMRI (Tomov 2023)

**Paper:** Tomov, M.S., Tsividis, P.A., Pouncy, T., Tenenbaum, J.B., and Gershman, S.J. (2023). The neural architecture of theory-based reinforcement learning. *Neuron 111*, 1331–1344.
**DOI:** https://doi.org/10.1016/j.neuron.2023.01.023
**Data:** https://doi.org/10.18112/openneuro.ds004323.v1.0.0

---

## subjects_n: 32

> "Thirty-two healthy participants were recruited from the Cambridge, MA community: 15 female, 17 male, 19-36 years of age, mean age 24 ± 4 years, all right-handed and with normal or corrected-to-normal vision."

— STAR Methods, Experimental Model and Subject Details

> "All 32 participants were included in the analysis."

— STAR Methods, fMRI Data Acquisition

---

## neuroimaging.fmri

### per_subject_h: 0.94

Computed from scanner run parameters:

> "Each run was 566 s in total."

> "We collected 6 functional runs for each participant"

— STAR Methods, fMRI Data Acquisition

6 runs × 566 s = 3396 s = 56.6 min ≈ **0.94 h per subject**.

Consistent with the paper's summary statement:

> "Overall, the entire scan session took 2.5 hrs per participant, 1.5 hrs of which was spent in the scanner, 1 hr of which was spent on BOLD acquisition and gameplay."

— STAR Methods, Experimental Design (the paper rounds 56.6 min to ~1 hr)

### total_h: 30.2

32 subjects × 0.94 h = **30.2 h** total.

---

## tasks.game

### per_subject_h: 0.94 / total_h: 30.2

The entire BOLD session was devoted to Atari-style gameplay. Participants played 6 games across 6 scanner runs:

> "Each participant played 6 different Atari-style games adapted from Tsividis et al. over the course of 6 scanner runs in a single session."

> "Each level was played on repeat for 1 minute total: if the episode ended before 1 minute had elapsed, a new episode began on the same level. Nine levels were played in total for each game."

> "Each run consisted of 3 blocks. Each block consisted of 3 levels of a given game."

— STAR Methods, Experimental Design

Game time per subject equals the BOLD scan time: 6 × 566 s = 3396 s ≈ **0.94 h** (this includes minimal fixation periods of 10 s at the start and end of each run).

Total across 32 subjects: **30.2 h**.

**Games played:** Chase, Helper, Bait, Zelda, Lemmings, Plaque Attack (participants 1–11) / Avoid George (participants 12–32). Games were presented in color-only mode with randomized colors and symbols across participants.
