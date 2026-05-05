# Natural Object Dataset (NOD-MEG+EEG)

**Reference:** Zhang, G., Zhou, M., Zhen, S., Tang, S., Li, Z., & Zhen, Z. (2025). A large-scale MEG and EEG dataset for object recognition in naturalistic scenes. *Scientific Data*, 12, 857. https://doi.org/10.1038/s41597-025-05174-7

---

## subjects_n: 30

> "A total of 30 healthy participants (18 females, mean age ± standard deviation [SD], 21.23 ± 1.98 years) took part in the NOD-MEG experiment. Among them, 19 participants (8 females, mean age ± SD, 21.26 ± 2.00 years) were involved in the NOD-EEG experiment." (p. 2)

30 unique individuals participated across the two modalities; the 19 EEG participants are a subset of the 30 MEG participants.

---

## neuroimaging.meg

### total_h: 25.0

> "In total, 25 hours MEG data (273 channels) were acquired from 30 participants." (Fig. 1 caption, p. 3)

> "we collected a total of 25 hours of MEG data on 30 participants with 57000 images as stimuli" (p. 2)

### per_subject_h: 0.83

Derived: 25 h / 30 subjects = 0.833 h/subject.

Session structure: 9 subjects completed 4 MEG sessions (ses-ImageNet01–04: 2+2+8+8 = 20 runs × ~390 s ≈ 2.17 h/subject); 21 subjects completed 1 MEG session (ses-ImageNet01: 5 runs × ~390 s ≈ 0.54 h/subject). The stated total of 25 h is used as authoritative.

---

## neuroimaging.eeg

### total_h: 24.0

> "In total, … 24 hours EEG data (64 channels) were acquired from 19 participants." (Fig. 1 caption, p. 3)

> "we collected a total of 24 hours of EEG data on 19 participants with 56000 images as stimuli" (p. 3)

### per_subject_h: 1.26

Derived: 24 h / 19 subjects = 1.263 h/subject.

Session structure: 9 subjects completed 4 EEG sessions (4,000 images, 8 runs/session); 10 subjects completed 2 EEG sessions (2,000 images, 8 runs/session). Each run lasted approximately 190 s.

---

## naturalistic_stimuli.images

### total_unique: 4000

> "9 participants completed 4 MEG sessions, each viewing a total of 4000 unique images (four images/category)." (p. 2)

The stimuli pool covers 1,000 ImageNet object categories with up to 4 images per category, giving 4,000 unique images maximum. EEG subjects saw the same stimuli pool (identical stimuli for MEG and EEG).

> "The stimuli images used for MEG and EEG are identical and are stored in the 'stimuli/ImageNet' directory." (p. 4)

### per_subject_unique: 1900

Derived from MEG session design: 9 subjects × 4,000 images + 21 subjects × 1,000 images = 57,000 total presentations across 30 subjects → 57,000 / 30 = 1,900 images on average per subject.

> "The remaining 21 participants completed only 1 MEG session, namely ses-ImageNet01 (5 runs), and each viewed 1000 unique images (one image/category)." (p. 2)

### total_with_repetition: 57000

> "we collected a total of 25 hours of MEG data on 30 participants with 57000 images as stimuli" (p. 2)

Cross-check: 9 subjects × 4,000 + 21 subjects × 1,000 = 36,000 + 21,000 = 57,000 ✓

### per_subject_with_repetition: 1900

Each image was presented once to each subject (no within-subject repetitions reported), so per_subject_with_repetition = per_subject_unique = 1,900.

---

## responses.controlled_tasks

### total_unique: 2, per_subject_unique: 2

> "participants were asked to press a button to indicate whether the object presented in the image was animate." (p. 2)

The task is a binary animate/inanimate judgment, yielding 2 response conditions.

> "the task in NOD asked participants to actively indicate whether each presented image was animate or inanimate, which differs from the tasks used in the THINGS (detecting a catch image) and NSD (detecting a new image)." (p. 8)

---

## Fields not included / flagged

- **fMRI:** The NOD-fMRI dataset (Zhang et al., 2022, *Scientific Data* 10, 559; https://doi.org/10.1038/s41597-023-02471-x) is a companion dataset from the same participants, described in a separate paper. It is not included here.
- **Structural MRI:** T1w anatomical images were collected for all 30 MEG participants for source localization. Not included in the current schema.
- **Physiology:** No physiological recording modalities (ECG, respiration, eye tracking) are described in this paper.
- **EEG per_subject statistics:** 19 EEG subjects saw either 2,000 or 4,000 images (average: 56,000 / 19 ≈ 2,947/subject). The images fields above use MEG numbers (30 subjects) as the primary count.
