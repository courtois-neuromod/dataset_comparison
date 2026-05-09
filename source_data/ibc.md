# Individual Brain Charting (IBC) — Data Provenance

Primary reference: Ponce et al. (2026), "Individual Brain Charting: fifth release of high-resolution fMRI data for cognitive mapping," *Scientific Data* 13, 593. https://doi.org/10.1038/s41597-026-06869-1

This sidecar covers the cumulative IBC dataset as of v4.0 (fifth release). Earlier releases are documented in:
- 1st release: Pinho et al. (2018), *Scientific Data* 5, 180105. https://doi.org/10.1038/sdata.2018.105
- 2nd release: Pinho et al. (2020), *Scientific Data* 7(1). https://doi.org/10.1038/s41597-020-00670-4
- 3rd release: Pinho et al. (2024), *Scientific Data* 11, 590. https://doi.org/10.1038/s41597-024-03390-1
- 4th release: deposited on EBRAINS without a standalone paper as of the 5th release

---

## subjects_n: 12

> "The present release of the IBC dataset consists of fMRI data from twelve individuals (two females), acquired between October 2019 and November 2022." (Methods > Participants, p. 2)

The original cohort comprised thirteen participants (sub-01 to sub-15, excluding sub-03 and sub-10 which were never assigned). Sub-02 withdrew after the first release; sub-01, sub-07, and sub-13 completed only subsets of the fifth-release tasks. The active participant count across all five releases is 12.

---

## neuroimaging.fmri

### total_h: 480.0 | per_subject_h: 40.0

> "extending the 1.5mm-resolution task-fMRI dataset for eleven participants to complete **up to 40 hours** of fMRI data per participant, with a target of 50 hours in the final release." (Abstract, p. 1)

> "the IBC project has incorporated 67 tasks, encompassing over 340 unique conditions and 530 independent contrasts, resulting in **approximately 40 hours of fMRI data per participant**." (Data Availability, p. 16)

**Computation:** 40 h × 12 subjects = 480 h total.

**Caveat:** "Up to 40 hours" is the maximum; subjects with partial participation (sub-01, sub-07, sub-13, sub-02) have fewer hours. The exact per-subject mean is not reported in the 5th release paper. The 480 h total figure is therefore an upper bound; the true total is likely slightly lower.

All BOLD fMRI data were acquired on a Siemens 3T Magnetom Prisma with a 64-channel head-neck coil at 1.5 mm isotropic resolution using a Multiband GE-EPI sequence (16-fold acceleration).

> "The fMRI data were acquired using an MRI scanner Siemens 3T Magnetom Prisma along with a Siemens Head/Neck 64-channel coil." (MRI Equipment, p. 3)

DWI (diffusion-weighted imaging) data are also available on EBRAINS but are not captured in the schema, which tracks BOLD fMRI only.

---

## tasks.resting_state

### total_h: 12.0 | per_subject_h: 1.0

From the IBC online documentation (https://individual-brain-charting.github.io/docs/mri_acquisitions.html):
- Resting-state BOLD: TR = 760 ms, 1,120 repetitions → 851 s ≈ 14.2 min per run.
- Resting state was collected as approximately 2 runs in dedicated sessions.

The IBC documentation lists resting state as "approximately 1 hour total per subject" across all sessions. With 12 subjects: 12 h total.

**Caveat:** The exact number of resting-state sessions per subject across all five releases is not specified in the 5th release paper. The value of 1 h per subject is taken from the IBC online documentation and may underestimate the true total if resting state was collected in multiple releases.

---

## tasks.video

### total_unique: 5.83 | per_subject_unique: 5.83 | total_with_repetition: 69.96 | per_subject_with_repetition: 5.83

All movie/video content is unique across runs (no within-subject repetitions) and identical across subjects (total_unique = per_subject_unique). total_with_repetition = 5.83 h × 12 subjects = 69.96 h.

Four naturalistic video tasks are present across the five IBC releases (Table 5, p. 7):

### Raiders (from 3rd release)
> "Clips, WedgeClock, WedgeAnti, Ring, Raiders" (Table 5, Third release, p. 7)

The Raiders task consists of 10 contiguous chapters of the 1981 film *Raiders of the Lost Ark* (2009 French-dubbed DVD edition). Chapter onset times from the IBC GitHub protocol README (https://github.com/individual-brain-charting/public_protocols/blob/master/raiders/protocol/README.md):

```
Chapter 1 - 00:00 | Chapter 2 - 12:29 | Chapter 3 - 22:22 | Chapter 4 - 32:50
Chapter 5 - 45:27 | Chapter 6 - 57:00 | Chapter 7 - 01:08:32 | Chapter 8 - 01:20:11
Chapter 9 - 01:31:57 | Chapter 10 - 01:41:19
```

The film's total runtime is approximately 115 min; Chapter 10 ends at ~115 min (duration ~13.7 min). **Total: ≈ 115 min = 1.92 h per subject.**

### Clips (from 3rd release)
> "Clips, WedgeClock, WedgeAnti, Ring, Raiders" (Table 5, Third release, p. 7)

The Clips task was adapted from the Gallant Lab (UCB, 2012). Each run consists of 9,750 image frames presented at 15 fps → 650 s = 10.83 min per run (computed from protocol scripts at https://github.com/individual-brain-charting/public_protocols/blob/master/clips/protocol/showmovie.py, default `show_hz = 15`; index files contain 9,750 lines each).

From the IBC online documentation: 12 training runs + 9 validation runs = 21 runs total.
**Total: 21 runs × 10.83 min = 227.5 min ≈ 3.79 h per subject.**

**Important:** The Clips task is a **silent** (audio-free) visual presentation. The protocol (showmovie.py) displays image frames only with no audio output. Therefore Clips is counted under `video` but NOT under `speech_listening`.

**Caveat:** The website value of "10.5 min per run" differs slightly from the calculated value of 10.83 min. The run count of 21 (12 training + 9 validation) is from the IBC website documentation; the protocol README examples suggest a slightly different structure. The 3.79 h estimate may carry ±10% uncertainty.

### Bang (from 2nd release)
> "PreferenceFood, PreferencePaintings, PreferenceFaces, PreferenceHouses, MTTWE, MTTNS, HcpMotor, HcpLanguage, HcpRelational, EmotionalPain, PainMovie, Self, **Bang**" (Table 5, Second release, p. 7)

From the IBC documentation: "edited version of the episode 'Bang! You're Dead' from the TV series 'Alfred Hitchcock Presents'." Duration: **7 min 55 sec = 0.13 h per subject.** This is a naturalistic movie with dialogue (speech present).

### PainMovie (from 2nd release)
> "EmotionalPain, **PainMovie**, Self, Bang" (Table 5, Second release, p. 7)

From the IBC documentation: the Pixar short film "Partly Cloudy." Duration: **~6 min ≈ 0.10 h per subject.** This animated film contains some dialogue (speech present).

**Summary of video durations (per subject):**
- Raiders: 1.92 h
- Clips: 3.79 h (silent)
- Bang: 0.13 h
- PainMovie: 0.10 h
- **Total: 5.94 h → rounded to 5.83 h in YAML (using IBC website's 10.5 min/run for Clips → 3.68 h; total = 1.92 + 3.68 + 0.13 + 0.10 = 5.83 h)**

---

## tasks.speech_listening

### total_unique: 2.15 | per_subject_unique: 2.15 | total_with_repetition: 25.8 | per_subject_with_repetition: 2.15

Speech is present in three of the four naturalistic video tasks:
- Raiders: 1.92 h (full movie with extensive French-dubbed dialogue)
- Bang: 0.13 h (TV episode with dialogue)
- PainMovie: 0.10 h (Pixar short with some dialogue)
- Clips: excluded (silent visual-only stimuli)

**Total unique speech content = 1.92 + 0.13 + 0.10 = 2.15 h per subject.** Since all subjects watch the same films, total_unique = per_subject_unique = 2.15 h. With 12 subjects: total_with_repetition = 25.8 h.

**Caveat:** The 4th release includes tasks named "Lec1" and "Lec2" (Table 5, p. 7), which may represent naturalistic lecture audio (passive listening to academic lectures, a paradigm used in several cognitive neuroscience studies). If so, they would add additional speech_listening hours. This could not be confirmed from available documentation; the IBC protocols repository does not include a separate directory for Lec1/Lec2, suggesting they may be part of another battery. **These potential additional hours are NOT included here and should be verified against the 4th release data/paper.**

---

## tasks.controlled

### total_h: 398.0 | per_subject_h: 33.2

Computed as a remainder:
- Total fMRI per subject: 40.0 h
- Resting state: −1.0 h
- Naturalistic video: −5.83 h
- **Controlled: 40.0 − 1.0 − 5.83 = 33.17 h ≈ 33.2 h per subject; 33.2 × 12 = 398 h total.**

The IBC dataset includes 67 tasks across five releases (Table 5, p. 7), the vast majority being controlled experimental paradigms with fixed trial or block structures. These include:
- ARCHI battery (Standard, Spatial, Social, Emotional)
- HCP battery (Emotion, Gambling, Motor, Language, Relational, Social, WM)
- CamCAN battery (EmoMem, EmoReco, StopNogo, Catell, FingerTapping, VSTMC)
- FBIRN battery (BreathHolding, Checkerboard, FingerTap, ItemRecognition)
- 5th-release tasks: BiologicalMotion, MathLanguage, SpatialNavigation, EmoMem, EmoReco, Catell, FingerTapping, VSTMC, StopNogo, NARPS, FaceBody, Scene, VisualSearch
- Plus retinotopic mapping (WedgeClock, WedgeAnti, Ring), preference tasks, mental time travel, discourse tasks, and others (see Table 5 for full list)

**Caveat:** The controlled hours include a small contribution (~2 min per session) from spin-echo EPI field maps acquired alongside task runs (Table 3, p. 5). With approximately 40 sessions across all releases, this amounts to ~1.4 h of non-task BOLD acquisition. This is not subtracted above (negligible relative to uncertainty in the 40 h total).

---

## tasks.contrasts

### total: 530 | per_subject: 530

> "the IBC project has incorporated 67 tasks, encompassing over 340 unique conditions and **530 independent contrasts**, resulting in approximately 40 hours of fMRI data per participant." (Data Availability, p. 16)

Since IBC is a within-subject, dense cognitive mapping dataset, all 530 contrasts are computed per subject. GLM-derived contrast maps (z-score maps) are available for each subject and each contrast.

> "Up to this release, the dataset includes 67 tasks, comprising 530 contrasts described on the basis of 188 cognitive concepts extracted from the Cognitive Atlas." (Background & Summary, p. 2)

The 5th release alone adds 18 new tasks with 180 contrasts (p. 2: "18 tasks with 180 contrasts were added, and 54 cognitive components were included in the description of the ensuing contrasts").

---

## Fields not populated

- **physiology**: No dedicated physiological recording modalities (ECG, respiration, EDA, plethysmograph) are reported in the 5th release paper. The preprocessing pipeline corrects for physiological noise, but it is unclear whether raw physiological signals were recorded. **Needs verification against the EBRAINS data repository.**
- **eye_tracking**: No eye-tracking data reported.
- **tasks.images**: Many controlled tasks use image stimuli, but image counts are not tracked as a primary metric in this dataset (the focus is on contrast maps and cognitive coverage, not image inventory).
