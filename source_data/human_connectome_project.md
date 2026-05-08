# Human Connectome Project — Evidence Sidecar

**Primary reference (task-fMRI):** Barch, D.M., Burgess, G.C., Harms, M.P., Petersen, S.E., Schlaggar, B.L., Corbetta, M., … Van Essen, D.C., for the WU-Minn HCP Consortium (2013). Function in the human connectome: Task-fMRI and individual differences in behavior. *NeuroImage*, 80, 169–189. https://doi.org/10.1016/j.neuroimage.2013.05.033

**Secondary reference (resting-state fMRI):** Smith, S.M., Andersson, J., Auerbach, E.J., Beckmann, C.F., Bijsterbosch, J., Douaud, G., … Glasser, M.F., for the WU-Minn HCP Consortium (2013). Resting-state fMRI in the Human Connectome Project. *NeuroImage*, 80, 144–168. https://doi.org/10.1016/j.neuroimage.2013.05.039

---

## name
`Human Connectome Project`

> "The primary goal of the Human Connectome Project (HCP) is to delineate the typical patterns of structural and functional connectivity in the healthy adult human brain."

Source: Abstract, p. 169.

---

## reference
DOI: https://doi.org/10.1016/j.neuroimage.2013.05.033

---

## subjects_n: 1200

> "Phase II will generate a publicly available database on normative patterns of structural and functional brain connectivity, and relationships to individual differences in cognition, emotion, and function."

> "We present behavioral data from the 77 participants whose data will be part of the first quarter data release of Phase II."

Source: Methods / Overview, p. 172.

The paper describes the full planned Phase II sample as 1200 individuals. The pilot data reported in this paper covers 77 behavioral and 20 imaging participants.

> "All participants are between the ages of 22 and 35, with no previously documented history of psychiatric, neurological, or medical disorders known to influence brain function."

Source: Methods / Participants, p. 172.

---

## neuroimaging.fmri

### total_h: 2175.0
### per_subject_h: 1.81

Combines task-fMRI (0.81 h/subject) and resting-state fMRI (1.00 h/subject); see each section below for derivations.

total_h = 1.81 h/subject × 1200 subjects = 2175 h.

---

## tasks.resting_state

### total_h: 1200.0
### per_subject_h: 1.00

> "In each subject we acquire a total of 1 h of whole-brain rfMRI data at 3 T, with a spatial resolution of 2 × 2 × 2 mm and a temporal resolution of 0.7 s"

Source: Abstract, Smith et al. 2013, p. 1.

> "The four 15-minute rfMRI runs are acquired in the two separate fMRI sessions, following the general counter-balanced ordering: 1) in the first session, 15-minute R–L phase encoding rfMRI, 15-minute L–R, and then various task-fMRI runs; 2) in the second session, 15-minute L–R, 15-minute R–L, and then task-fMRI."

Source: Acquisition protocol, Smith et al. 2013, p. 5.

Figure 2 in Smith et al. 2013 also confirms the structure: "4 runs' concatenated grayordinate dataset: 1-hour rfMRI dataset" shown for each of subjects 1 through 1200.

total_h = 1.00 h/subject × 1200 subjects = 1200 h.

---

## tasks.controlled (task-fMRI)

### total_h: 976.0
### per_subject_h: 0.81

Computed from Table 4 (run durations × 2 runs per task, Barch et al. 2013):

| Task | Run duration | × 2 runs |
|---|---|---|
| Working memory | 5:01 min | 10.03 min |
| Gambling | 3:12 min | 6.40 min |
| Motor | 3:34 min | 7.13 min |
| Language | 3:57 min | 7.90 min |
| Social cognition | 3:27 min | 6.90 min |
| Relational processing | 2:56 min | 5.87 min |
| Emotion processing | 2:16 min | 4.53 min |
| **Total** | | **48.77 min = 0.813 h** |

> "Two runs of each task were acquired, one with a right-to-left and the other with a left-to-right phase encoding."

Source: fMRI data acquisition, p. 179.

total_h = 0.813 h × 1200 subjects = 975.6 h ≈ 976 h.

fMRI acquisition parameters:

> "whole-brain EPI acquisitions were acquired with a 32 channel head coil on a modified 3 T Siemens Skyra with TR = 720 ms, TE = 33.1 ms, flip angle = 52°, BW = 2290 Hz/Px, in-plane FOV = 208 × 180 mm, 72 slices, 2.0 mm isotropic voxels, with a multi-band acceleration factor of 8"

Source: fMRI data acquisition, p. 179.

---

## tasks.controlled

### total_h: 976.0
### per_subject_h: 0.81

Seven controlled task-fMRI paradigms (see run duration table above under `neuroimaging.fmri`).

Tasks described in this paper:
1. **Working memory / category-specific representations** — N-back task (2-back and 0-back) with faces, places, tools, and body parts as stimuli
2. **Incentive processing (Gambling task)** — card-guessing paradigm with mostly-reward and mostly-loss blocks
3. **Motor mapping** — tapping, squeezing, and tongue movements (right/left hand, right/left foot, tongue)
4. **Language processing (Story task)** — auditory story vs. math problem blocks
5. **Social cognition (Theory of Mind)** — short video clips of shapes with/without social interactions
6. **Relational processing** — shape/texture relational matching vs. control condition
7. **Emotion processing (Hariri task)** — matching fearful/angry faces vs. shapes

> "Our goal was to identify and utilize a reliable and well-validated battery of measures that assess a wide range of human functions and behaviors in a reasonable amount of time (3–4 h total, to satisfy subject burden considerations)."

Source: Individual differences in the HCP, p. 170.

---

## tasks.contrasts

### total: 36
### per_subject: 36

All 1200 subjects complete the same 7-task battery, so total = per_subject = 36.

Contrasts derived from the GLM design described in the paper (pp. 180–181):

**Working memory (11 contrasts):**
> "Linear contrasts for these predictors were computed to estimate effects of interest: 2-back (vs. fixation), 0-back, 2-back vs. 0-back, each stimulus type versus fixation (e.g., Body vs. fixation, collapsing across memory load), and each stimulus type versus all others."

- 2-back vs. fixation (1), 0-back vs. fixation (1), 2-back vs. 0-back (1)
- Body, Face, Place, Tool vs. fixation (4)
- Body, Face, Place, Tool vs. average of all others (4)
= 11 contrasts

**Gambling / Incentive processing (3 contrasts):**
> "Two predictors were included in the model for Incentive Processing — mostly reward and mostly loss blocks … linear contrasts of the parameter estimates were computed to compare each condition to baseline and to each other."

- Reward vs. baseline (1), Loss vs. baseline (1), Reward vs. Loss (1)
= 3 contrasts

**Motor (10 contrasts):**
> "Five predictors were included in the Motor model — right hand, left hand, right foot, left foot, and tongue. … Linear contrasts were computed to estimate activation for each movement type versus baseline and versus all other movement types."

- Right hand, Left hand, Right foot, Left foot, Tongue vs. baseline (5)
- Each movement type vs. average of all others (5)
= 10 contrasts

**Language (3 contrasts):**
> "Two predictors were included in the Language Processing model — Math and Story."

- Story vs. baseline (1), Math vs. baseline (1), Story vs. Math (1)
= 3 contrasts

**Social cognition (3 contrasts):**
> "Two predictors were included in the Social Cognition model — Social and Random motion."

- Social vs. baseline (1), Random vs. baseline (1), Social vs. Random (1)
= 3 contrasts

**Relational processing (3 contrasts):**
> "Two predictors were included in the Relational Processing model — Relational processing and a control Matching condition."

- Relational vs. baseline (1), Matching vs. baseline (1), Relational vs. Matching (1)
= 3 contrasts

**Emotion processing (3 contrasts):**
> "Two predictors were included in the Emotion Processing model — Emotional Faces and a Shape control condition."

- Faces vs. baseline (1), Shapes vs. baseline (1), Faces vs. Shapes (1)
= 3 contrasts

**Total: 11 + 3 + 10 + 3 + 3 + 3 + 3 = 36 contrasts**

**Note:** The official HCP S1200 data release is reported to document 47 standard contrasts. The additional 11 beyond the 36 here likely include per-category × per-memory-load contrasts for the WM task (e.g., 2-back-Body vs. fixation, 0-back-Face vs. fixation) derivable from the 8 WM predictors but not explicitly enumerated in the paper. The count of 36 reflects contrasts that are explicitly described in the Methods section of Barch et al. 2013 and correspond directly to canonical whole-brain localizer maps; the S1200 reference manual would be needed to confirm 47.

---

## physiology.respiration

### total_h: 2175.0
### per_subject_h: 1.81

> "To measure cardiac and respiratory signals, a pulse oximeter and respiratory bellows were fitted to the participants prior to the fMRI sessions. Those signals, along with the sync pulse from the scanner, were recorded by the scanner host computer at a sampling rate of 400 Hz."

Source: fMRI data acquisition, Barch et al. 2013, p. 179. The identical setup is described for resting-state sessions in Smith et al. 2013, p. 5.

Physiology was recorded concurrently with all fMRI runs (task and resting-state); duration matches total fMRI hours: 1.81 h/subject × 1200 = 2175 h.

---

## physiology.plethysmograph

### total_h: 2175.0
### per_subject_h: 1.81

See quote above under `physiology.respiration`. The pulse oximeter captures the peripheral pulse waveform (plethysmograph signal). Same coverage as respiration.

---

## Unconfirmed / approximate values

- **subjects_n = 1200**: This is the planned Phase II sample size stated in the paper. The actual HCP S1200 release (2017) included 1206 subjects; a secondary reference would be needed to update this count.
- **contrasts = 36**: Derived from the GLM design in Barch et al. 2013. The official HCP S1200 release documents 47 standard contrasts; the discrepancy likely reflects additional WM contrasts not explicitly listed here.
