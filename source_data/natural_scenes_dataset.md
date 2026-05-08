# Natural Scenes Dataset (NSD)

**Reference:** Allen, E. J., St-Yves, G., Wu, Y., Breedlove, J. L., Prince, J. S., Dowdle, L. T., Nau, M., Caron, B., Pestilli, F., Charest, I., Hutchinson, J. B., Naselaris, T., & Kay, K. (2022). A massive 7T fMRI dataset to bridge cognitive neuroscience and artificial intelligence. *Nature Neuroscience*, 25, 116–126. https://doi.org/10.1038/s41593-021-00962-x

---

## subjects_n: 8

> "The NSD consists of high-resolution (1.8-mm) whole-brain 7T functional magnetic resonance imaging (fMRI) of **eight carefully screened human participants**." (p. 116)

> "We recruited 14 individuals to participate in an initial 7T fMRI screening session … We then invited the **top eight individuals** to participate in the full NSD experiment (all individuals accepted)." (p. 117)

---

## neuroimaging.fmri

### per_subject_h: 35.5

> "the NSD still has substantially more participants (eight versus four), more trials per participant (26,625 versus 4,718, on average) and **more hours of fMRI per participant (35.5 versus 13.7, on average)** than BOLD5000." (p. 121)

Corroborated by:
> "**30–40 h of data for each of eight participants** on the core NSD experiment." (p. 125)

Session structure supporting the 35.5h figure: "Each run lasted **5 min** and consisted of 62 or 63 stimulus trials … One NSD scan session: **12 NSD runs**, 750 stimulus trials total" (Fig. 1b caption, p. 118), giving 12 × 5 min = 60 min per session.

> "The NSD experiment was split across **40 scan sessions** for each participant … we completed the **full set of 40 NSD scan sessions for four** of the participants … we completed **30–32 NSD scan sessions** for each of the other participants." (p. 117)

### total_h: 284.0

Derived: 35.5 h/subject × 8 subjects = 284 h. This covers the core NSD fMRI sessions only; additional fMRI time from the screening session (pRF + fLoc) and the two auxiliary experiments (nsdsynthetic, nsdimagery) is not included.

---

## passive.resting_state

### per_subject_unique: 2.3, total_unique: 18.7, per_subject_with_repetition: 2.3, total_with_repetition: 18.7

> "**substantial amounts of resting-state data (minimum 100 min per participant)**" (p. 119)

> Fig. 2b caption: resting-state data "totaling **100 or 180 min per participant**."

Four participants who completed all 40 sessions received 180 min of resting-state scans; four partial completers received 100 min. Average = (4 × 180 + 4 × 100) / 8 = 140 min = 2.33 h per subject; total = 2.33 × 8 ≈ 18.7 h. Values are reported as averages across participants. No meaningful unique/repetition distinction applies to resting state, so `with_repetition` equals `unique`.

---

## passive.images

### total_unique: 70,566

> "Aggregated across participants, NSD includes responses to **70,566 distinct natural scene images**—this is more than an order of magnitude larger than similar datasets." (p. 116)

### per_subject_unique: 10,000

> "eight carefully screened human participants who **each viewed 9,000–10,000 color natural scenes** (22,000–30,000 trials)." (p. 116)

> "Our experimental design specified that each of eight participants would view **10,000 distinct images**, and a special set of **1,000 images would be shared** across participants (eight participants × 9,000 unique images + 1,000 shared images = 73,000 images)." (p. 117)

Note: the design target was 10,000 per participant. Four participants completed all 40 sessions (10,000 images); four completed 30–32 sessions and therefore saw 9,000–10,000 images. The value 10,000 is used as per_subject_unique per the stated design; `total_unique` (70,566) reflects the actual data collected.

### total_with_repetition: 213,000

> "the total size of the NSD dataset is **213,000 trials**." (p. 121)

### per_subject_with_repetition: 26,625

> "more trials per participant (**26,625** versus 4,718, on average) than BOLD5000." (p. 121)

> "**each image would be presented three times** to a given participant." (p. 117)

At full completion (40 sessions × 750 trials = 30,000 trials per participant); the average of 26,625 reflects participants with incomplete sessions.

---

## active.controlled

### per_subject_unique: 1.0, total_unique: 1.0

> "we incorporated a **continuous recognition task** in which participants were instructed to indicate whether they have seen each presented image at any point in the past." (p. 117)

The recognition paradigm (old/new judgment) is identical across all NSD sessions for all subjects. Per the schema rule for controlled tasks, the same paradigm repeated across sessions counts once: one session = 1.0 h of unique task content. All subjects run the same paradigm, so `total_unique = per_subject_unique = 1.0 h`.

### per_subject_with_repetition: 35.5, total_with_repetition: 284.0

The recognition task runs throughout all NSD fMRI sessions. Per-subject average is 35.5 h (see `neuroimaging.fmri`); total across 8 subjects is 284.0 h.

---

## tasks.contrasts: 22 per subject and total

The NSD contrasts come from three sources, totalling 22 per subject. All 8 participants completed both localizer experiments in the initial prfloc screening session (p. 117).

**pRF / retinotopy — 12 contrasts**

> "We adapted the experiment used in the **Human Connectome Project 7T Retinotopy Dataset**. … Two run types were used. The first, termed 'multibar', involves bars sweeping in multiple directions (same as RETBAR in the Human Connectome Project 7T Retinotopy Dataset). The second, termed 'wedging', involves a combination of rotating wedges and expanding and contracting rings. … A total of **six runs** (three multibar and three wedging) were collected in the first 7T fMRI session (prfloc)." (Methods, p. 129)

This is the same protocol as the CNeuroMod retinotopy dataset, which yields 12 visual area maps (V1–V3, hV4, VO1/2, LO1/2, TO1/2, V3a/b); the same count is used here.

**fLoc — 9 contrasts**

> "This experiment was developed by the **Grill-Spector laboratory** (stimuli and presentation code available at http://vpnl.stanford.edu/fLoc/). The experiment consisted of the presentation of grayscale images depicting different stimulus categories (Fig. 2a). There were **ten categories, grouped into five stimulus domains**: characters (word and number), bodies (body and limb), faces (adult and child), places (corridor and house) and objects (car and instrument). … In total, **six runs** were collected in the first 7T fMRI session (prfloc)." (Methods, p. 129)

This is the same fLoc protocol as the CNeuroMod floc dataset, which yields 9 GLM contrasts (subject-specific ROIs for FFA, OFA, pSTS, PPA, OPA, MPA, and EBA); the same count is used here.

**Recognition memory task — 1 contrast**

The old/new recognition judgment is the single contrast from the core NSD experiment (see `active.controlled` above).

`total = per_subject = 22` because all 8 subjects run identical localizers and the same recognition task, so no unique content accumulates across subjects.

---

## physiology.eye_tracking

### per_subject_h: 3.0, total_h: 24.0

> "**eye-tracking data (2–4 sessions per participant)** were also collected." (p. 117)

Each NSD session is ~1 h (12 runs × 5 min); using the midpoint of 3 sessions gives ~3 h/subject and 24 h total across 8 subjects.

---

## Fields not included / flagged

- **Physiological modalities (cardiac, respiration):** The paper states "**physiological data (ten sessions per participant)**" and "**external physiological measures during the resting-state scan sessions**" (p. 117, 119), but does not enumerate the specific modalities (cardiac, respiration, pulse oximeter) in the main text. These fields are omitted pending review of the supplementary materials or NSD data documentation.

- **Diffusion / anatomical MRI:** T1, T2, diffusion, venogram, and angiogram data were collected (Fig. 2b) but are structural measures not covered by the current schema.
