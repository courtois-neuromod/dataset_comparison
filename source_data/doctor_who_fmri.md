# Doctor Who fMRI (Seeliger et al.)

**Reference:** Seeliger, K., Sommers, R. P., Güçlü, U., Bosch, S. E., & van Gerven, M. A. J. (2019). A large single-participant fMRI dataset for probing brain responses to naturalistic stimuli in space and time. *Scientific Data*, 6, 167. https://doi.org/10.1038/s41597-019-0172-7

Preprint: https://doi.org/10.1101/687681. Data at Donders Repository: http://hdl.handle.net/11633/di.dcc.DSC_2018.00082_134

---

## subjects_n: 1

> "Data recording was done on a single participant (male, age 27.5) between April 2017 and December 2017." (Methods, "Experiment design", p. 2)

---

## neuroimaging.fmri

### per_subject_h / total_h: 28.5

Total fMRI recording time for the one participant combines the training set and the test set (all repetitions), both at TR = 700 ms.

- Training: 120,830 volumes × 0.700 s ÷ 3600 = **23.49 h**
- Test (all repetitions, including fadeout): 25,927 volumes × 0.700 s ÷ 3600 = **5.04 h**
- Total: ≈ **28.5 h**

> "The data consists of 120.830 whole-brain volumes (approx. 23 h) of single-presentation data (full episodes, training set) and 1.178 volumes (11 min) of repeated narrative short episodes (test set, 22 repetitions), recorded with fixation over a period of six months." (Abstract, p. 1)

> "The functional scans used a T2*-weighted echo planar imaging pulse sequence at 700 ms TR." ("fMRI data acquisition", p. 6)

> "In total 25.927 volumes were recorded including fadeout." (Data Records, "Test fMRI responses", p. 9)

**fMRI acquisition parameters:**

> "The data was collected in a Siemens 3T MAGNETOM Prisma with a Siemens 32-channel head coil (Siemens, Erlangen, Germany). The functional scans used a T2*-weighted echo planar imaging pulse sequence at 700 ms TR. Volumes were recorded with 64 transversal slices at 2.4 mm³ voxel size (slice dimension 88 × 88 at field of view 211 × 211 mm²). They were measured with a multiband acceleration factor of 8. TE was 39 ms and the flip angle 75 degrees." ("fMRI data acquisition", p. 6)

**Anatomical scan:**

> "The structural scans at the end of most sessions used a T1-weighted MP RAGE pulse sequence, with 192 sagittal slices with a field of view of 256 × 256 and 1 mm³ voxel size. The TE was 3.03 ms, the TR 2300 ms and the flip angle 8 degrees." (p. 6)

---

## naturalistic_stimuli.video

### per_subject_unique / total_unique: 23.7 h

Unique video content = training set (30 Doctor Who episodes, each shown once) plus 7 short test clips (first presentation).

- Training unique: 120,830 volumes × 0.700 s ÷ 3600 = **23.49 h**
- Test unique: 5 × 60 s + 2 × 180 s = 660 s = **0.18 h**
- Total unique: ≈ **23.7 h**

> "We recorded a densely sampled large fMRI dataset (TR=700 ms) in a single individual exposed to spatio-temporal visual and auditory naturalistic stimuli (30 episodes of BBC's Doctor Who)." (Abstract, p. 1)

> "For the training set we used episodes from Seasons 2, 3 and 4 after the 2005 relaunch of the series (Tenth Doctor). We started with Episode 6 from Season 2 and presented all following episodes in serial order until and including Season 4, Episode 10." ("Training stimuli", p. 4)

> "The test set consisted of seven variable length videos. We used Pond Life, a mini-series of 5 narrative 1-minute-episodes; and Space / Time, two mini-episodes of 3 minutes each." ("Test stimuli", p. 5)

Note: rrun[005] was omitted from the public release due to a known video buffering problem, but was included for internal analysis and is counted in the volume totals above.

### per_subject_with_repetition / total_with_repetition: 27.9 h

Training episodes were each presented once; the 7 test clips were repeated 22–26 times across sessions.

- Training: 23.49 h (no within-subject repetition)
- Test with repetitions (video content only, excluding fadeout): 5 × 26 × 60 s + 2 × 22 × 180 s = 7,800 + 7,920 = 15,720 s = **4.37 h**
- Total: ≈ **27.9 h**

> "In every session, one full Doctor Who episode was presented. In most sessions, this episode was followed by a presentation of the seven test set clips in random order." ("Experiment design", p. 2)

Table 3 (p. 6) gives the repetition counts per test clip:
- Pond Life episodes 1–5: **26 repetitions** each, 60 s each
- Space/Time episodes 6–7: **22 repetitions** each, 180 s each

---

## naturalistic_stimuli.audio

### per_subject_unique / total_unique: 23.7 h
### per_subject_with_repetition / total_with_repetition: 27.9 h

Doctor Who episodes are audiovisual — all video content has a full audio soundtrack. `audio` therefore equals `video` identically.

> "We recorded a densely sampled large fMRI dataset (TR=700 ms) in a single individual exposed to spatio-temporal visual and **auditory** naturalistic stimuli (30 episodes of BBC's Doctor Who)." (Abstract, p. 1)

Values are identical to `naturalistic_stimuli.video` above.

---

## naturalistic_stimuli.speech_listening

### per_subject_unique / total_unique: 23.7 h
### per_subject_with_repetition / total_with_repetition: 27.9 h

Doctor Who episodes are audiovisual — the stimulus includes both video and spoken-language audio. `speech_listening` therefore equals `video` identically.

> "We recorded a densely sampled large fMRI dataset (TR=700 ms) in a single individual exposed to spatio-temporal visual and **auditory** naturalistic stimuli (30 episodes of BBC's Doctor Who)." (Abstract, p. 1)

Values are identical to `naturalistic_stimuli.video` above.

---

## Fields not included / flagged

- **Localizer sessions:** Three separate sessions collected retinotopy (V1, V2, V3) and functional localizers (LOC, FFA, OFA, AC, M1, MT). These add additional fMRI time not counted above; exact volume counts are not reported in the paper.
- **Physiology:** No physiological data (cardiac, respiration, EDA) are mentioned in the paper.
- **Eye tracking:** Not reported.
- **Structural MRI:** T1-weighted anatomical scans were acquired at the end of most sessions; not included in fMRI totals.
