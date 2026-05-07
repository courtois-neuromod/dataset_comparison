# UK Biobank Brain Imaging

**Reference:** Miller, K.L., Alfaro-Almagro, F., Bangerter, N.K., Thomas, D.L., Yacoub, E., Xu, J., Bartsch, A.J., Jbabdi, S., Sotiropoulos, S.N., Andersson, J.L.R., Griffanti, L., Douaud, G., Okell, T.W., Weale, P., Dragonu, I., Garratt, S., Hudson, S., Collins, R., Jenkinson, M., Matthews, P.M., & Smith, S.M. (2016). Multimodal population brain imaging in the UK Biobank prospective epidemiological study. *Nature Neuroscience*, 19(11), 1523–1536. https://doi.org/10.1038/nn.4393

Documentation: UK Biobank Brain Imaging Documentation v1.10, May 2024. Smith, Alfaro-Almagro & Miller. https://biobank.ndph.ox.ac.uk/showcase/showcase/docs/brain_mri.pdf

---

## subjects_n: 94930

As of May 2026, the UK Biobank data fields report the following participant counts:

- **Field 20225** — Functional brain images (resting): **94,930 participants** — https://biobank.ctsu.ox.ac.uk/crystal/field.cgi?id=20225
- **Field 20217** — Functional brain images (task): **80,662 participants** — https://biobank.ctsu.ox.ac.uk/crystal/field.cgi?id=20217

`subjects_n` is set to 94,930, the number of subjects with resting-state fMRI data (the larger and primary fMRI measure). Note that 80,662 of these also have task fMRI; the remaining ~14,268 have resting fMRI only.

For reference, the v1.10 May 2024 brain imaging documentation reported: "67k subjects total and 5k second-scans total." The current counts reflect ongoing data collection since that release.

---

## neuroimaging.fmri

### per_subject_h: 0.167

Each subject undergoes both resting-state fMRI (rfMRI) and task fMRI (tfMRI) within a single 35-minute brain imaging session.

**rfMRI:**
> "Resting-state functional MRI … Duration: **6 minutes (490 timepoints)**. TR: 0.735 s. TE: 39ms. GE-EPI with x8 multislice acceleration, no iPAT, flip angle 52°, fat saturation." (Section 2.5)

**tfMRI:**
> "Task functional MRI … As for rfMRI, except: Duration: **4 minutes (332 timepoints)**." (Section 2.9)

Combined fMRI per subject: 6 + 4 = 10 minutes = 10/60 ≈ 0.167 h.

### total_h: 14871.0

Derived from the current UK Biobank participant counts (see `subjects_n` above):
- 94,930 subjects × 6 min rfMRI = 569,580 min
- 80,662 subjects × 4 min tfMRI = 322,648 min
- Total = 892,228 min ÷ 60 = 14,871 h

---

## naturalistic_stimuli.resting_state

### per_subject_unique: 0.1, total_unique: 6700.0

> "Resting-state functional MRI … Duration: **6 minutes (490 timepoints)**." (Section 2.5)

> "rfMRI Resting-state functional MRI timeseries data. Resting-state functional MRI measures changes in blood oxygenation associated with **intrinsic brain activity (i.e., in the absence of an explicit task or sensory stimulus)**." (Section 1.3)

Per subject: 6 min = 0.1 h. Total unique: 94,930 × 0.1 = 9,493 h. Each subject's resting-state data is distinct (no shared stimulus content, so total_unique = total_with_repetition).

### per_subject_with_repetition: 0.1, total_with_repetition: 6700.0

Each subject has one 6-minute resting-state scan. No within-subject repetition of resting-state runs is described in the standard protocol.

---

## active.controlled

### per_subject_unique: 0.067, per_subject_with_repetition: 0.067

> "Task functional MRI … As for rfMRI, except: Duration: **4 minutes (332 timepoints)**." (Brain Imaging Documentation v1.10, Section 2.9)

4 min = 4/60 ≈ 0.067 h per subject.

> "The task is the Hariri faces/shapes 'emotion' task [Hariri et al., 2002, Barch et al., 2013], as implemented in the HCP, but with shorter overall duration and hence fewer total stimulus block repeats. The participants are presented with **blocks of trials and asked to decide either which of two faces** presented on the bottom of the screen **match the face at the top of the screen, or which of two shapes** presented at the bottom of the screen match the shape at the top of the screen. The faces have either angry or fearful expressions." (Section 2.9)

All subjects perform the identical task (same stimuli, same conditions), so `total_unique = per_subject_unique = 0.067 h`.

### total_unique: 0.067

All 80,662 subjects with task fMRI run the same paradigm — no unique content is added by additional subjects.

### total_with_repetition: 5377.0

80,662 subjects × 0.067 h/subject = 5,377 h.

---

## Fields not included / flagged

- **Hardware:** Siemens Skyra 3T, standard 32-channel RF receive head coil, three scanning sites (Cheadle Manchester, Newcastle, Reading). Not captured in schema.

- **Diffusion MRI (dMRI):** Acquired at 2×2×2 mm resolution, 7 minutes, 100 diffusion directions (50×b=1000, 50×b=2000 s/mm²). Not in schema (no dMRI field).

- **Structural MRI (T1, T2_FLAIR):** T1 at 1×1×1 mm (5 min), T2_FLAIR at 1.05×1×1 mm (6 min). Not in schema.

- **Susceptibility-weighted imaging (SWI):** 0.8×0.8×3 mm, 2.5 minutes. Not in schema.

- **Arterial spin labelling (ASL):** Added post-COVID restart; 3.4×3.4×4.5 mm, 2 minutes. Not in schema.

- **Second-scan subjects:** 5,000 participants have a second imaging session. This adds ~833 h of additional fMRI data not included in total_h.

- **Imaging-derived phenotypes (IDPs):** The pipeline generates thousands of summary brain measures; these are not neuroimaging data in the raw sense and are not represented in the schema.
