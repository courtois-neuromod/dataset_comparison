# OmniMouse

**Reference:** Willeke, K. F., Turishcheva, P., Gilbert, A., Chakrabarty, G., Bedel, H. A., Fahey, P. G., Qiu, Y., Weis, M. A., Vystrčilová, M., Muhammad, T., Ntanavara, L., Froebe, R. E., Ponder, K., Tan, Z. H., Orhan, E., Cobos, E., Sanborn, S., Franke, K., Sinz, F. H., Ecker, A. S., & Tolias, A. S. (2026). OmniMouse: Scaling properties of multi-modal, multi-task brain models on 150B neural tokens. *ICLR 2026*. https://arxiv.org/abs/2604.18827

---

## subjects_n: 73

> "We compiled a dataset of more than 3 million single-unit neuronal recordings from **73 animals** (Fig. 2)." (Section 3, p. 3)

> Figure 1A caption: "**323 recording sessions from 73 mice**." (p. 1)

Note: Figure 2B breaks the dataset into Train (69 animals, 316 sessions) and Eval (7 animals, 7 sessions), totalling 76 animal-split entries but 73 unique animals — consistent with the eval mice overlapping partially with the training pool (73 unique animals total as stated in text).

---

## neuroimaging.calcium_imaging

> "The dataset contains excitatory neurons' responses in visual cortex recorded via **wide-field two-photon calcium imaging at 6–14 Hz** in awake, head-fixed, behaving mice (Sofroniew et al., 2016), with spiking activity extracted by CAIMAN (Giovannucci et al., 2019)." (Section 3, p. 3)

### total_h: 557.6

Derived from Figure 2B table (p. 4):
- Train: Duration = **543 h** (69 animals, 316 sessions)
- Eval: Duration = **14.6 h** (7 animals, 7 sessions)
- Total: 543 + 14.6 = **557.6 h**

> Figure 2B: "Duration (h): [Train] **543**, [Eval] **14.6**" (p. 4)

### per_subject_h: 7.6

Derived: 557.6 h / 73 animals ≈ 7.6 h per animal (mean). Session durations vary substantially across animals.

> "session durations and population sizes varying across animals (Fig. S4)" (Section 3, p. 3)

---

## tasks.images

Mice were shown static natural images (ImageNet) and parametric static stimuli (model-generated stimuli, static Gabors).

> "The mice were presented with **naturalistic images sampled from ImageNet** (Russakovsky et al., 2015)" (Section 3, p. 3)

> "parametric stimuli such as **static and drifting Gabors** (Petkov & Subramanian, 2007), directional pink noise, flashing Gaussian dots, random dot kinematograms (Morrone et al., 2000), and **model-generated stimuli** (similar to Walker et al., 2019)." (Section 3, p. 3)

### total_with_repetition: 760,521

Derived from Figure 2B:
- Train image frames: **743,130**
- Eval image frames: **17,391**
- Total: 743,130 + 17,391 = **760,521** image presentations across all 73 mice

> Figure 2B: "Image frames: [Train] **743,130**, [Eval] **17,391**" (p. 4)

### per_subject_with_repetition: 10,418

Derived: 760,521 / 73 = 10,418 image presentations per mouse on average. Note that training mice average ~10,769 (743,130 / 69) and eval mice average ~2,484 (17,391 / 7).

### total_unique: 10,769 ⚠ approximate

**Uncertain — not directly reported in the paper.** Derived under the assumption that the same image set was shown to all training animals (as is typical in SENSORIUM-style experiments). Under this assumption:
- Unique images in training ≈ 743,130 / 69 ≈ 10,769
- Unique images in eval ≈ 17,391 / 7 ≈ 2,484

Value uses 10,769 as total_unique, assuming eval images are a subset of the training image set. If eval images are entirely disjoint, total_unique would be ~13,253.

The paper does not report the number of unique image identities or the cross-animal stimulus overlap structure.

### per_subject_unique: 10,418 ⚠ approximate

Average across 73 mice under the same assumption (same images for all animals in each split): training mice each see ~10,769 unique images; eval mice each see ~2,484. Weighted average ≈ 10,418.

The paper does not report within-animal repetition counts for images. If images were shown multiple times per animal (as is common for reliability estimation), per_subject_unique would be lower than the 10,769 / 2,484 estimates above.

---

## tasks.video

Mice were shown natural movies (cinematic movies and Sports-1M) and parametric animated stimuli (drifting Gabors, random dot kinematograms, etc.).

> "videos sampled from **cinematic movies** and the **Sports-1M dataset** (Karpathy et al., 2014)" (Section 3, p. 3)

> "All stimuli were presented at **30–60 Hz**, at varying resolutions with images presented for 500 ms and preceded by a 300–500 ms blank screen." (Section 3, p. 3)

> Figure 2C shows average stimulus composition per session: ~31% **natural video**, ~17% **parametric movie** (animated parametric stimuli), ~17% natural images, ~35% other images. Both video categories are counted here.

### total_with_repetition: 367.6 h

Derived from Figure 2B video frame counts at 30 fps:
- Train: 38.6M frames / 30 fps / 3600 = **357.4 h**
- Eval: 1.1M frames / 30 fps / 3600 = **10.2 h**
- Total: **367.6 h** of video presentations across all 73 mice

> Figure 2B: "Video frames: [Train] **38.6 M**, [Eval] **1.1 M**" (p. 4)

> Table S1: "Frame rate: **30 fps**" (p. 20)

### per_subject_with_repetition: 5.0 h

Derived: 367.6 h / 73 animals ≈ 5.0 h per animal on average (training animals average ~5.2 h, eval animals ~1.5 h).

### total_unique: 6.6 h ⚠ approximate

**Uncertain — not directly reported.** Estimated under two assumptions: (1) the same video stimuli are shown to all animals within each split (as is typical in SENSORIUM-style experiments, so unique content per split ≈ per-animal content); (2) the training and eval video libraries are disjoint.

Under these assumptions:
- Unique video in training ≈ 357.4 h / 69 ≈ 5.2 h
- Unique video in eval ≈ 10.2 h / 7 ≈ 1.5 h
- Total unique ≈ 5.2 + 1.5 = **6.6 h**

If training and eval share the same video library, total_unique ≈ 5.2 h.

### per_subject_unique: 5.0 h ⚠ approximate

Under assumption (1) above, each animal sees roughly the same set of unique video content: ~5.2 h for training animals, ~1.5 h for eval animals, weighted average ~5.0 h.

This also assumes no within-animal repetition of video clips. The paper does not describe the within-session repetition structure for video stimuli.

---

## physiology.eye_tracking

Pupil position (x, y), pupil dilation, and its derivative were recorded continuously throughout all sessions.

> "Our dataset contains **five behavior variables: running speed**, recorded at 50-100 Hz, and **four pupil variables: pupil center x and y positions, pupil dilation and its derivative**, all recorded at 20 Hz." (Section 3, p. 4)

> "We reconstruct the visual stimulus presented throughout the **entire recording**, enabling continuous representation of the full experimental timeline." (Section 3, p. 4)

> Table S1: "Behavior sampling rate: **20 Hz**; Channels: **Eye tracker (4) + treadmill (1)**" (p. 20)

### total_h: 557.6

Behavioral traces are recorded throughout the full recording (same duration as calcium imaging): 543 + 14.6 = 557.6 h.

### per_subject_h: 7.6

Derived: 557.6 / 73 ≈ 7.6 h per animal on average (same as calcium imaging, since recording is continuous).

---

## Fields not included / flagged

- **neuroimaging.fmri / .eeg / .meg / .ieeg**: OmniMouse uses two-photon calcium imaging of mouse visual cortex, not any of the human neuroimaging modalities covered by the schema. A `calcium_imaging` subfield is assumed to exist (see above).

- **passive.resting_state**: The recording timeline includes blank inter-stimulus intervals (300–500 ms between images; see Section 3), but there is no structured resting-state protocol. These blank periods are part of the continuous recording rather than a dedicated rest condition.

- **passive.audio / .speech_listening / .text_reading**: No auditory or linguistic stimuli are used; mice are shown visual stimuli only.

- **active.controlled / .game_actions**: Mice perform no explicit behavioral task. They are head-fixed on a treadmill and run spontaneously; running speed is recorded as a behavioral covariate, not as a task response.

- **physiology.ecg / .respiration / .plethysmograph / .eda**: The paper reports only running speed and four pupil variables as behavioral measurements; no cardiac, respiratory, or electrodermal recordings are described.

- **Unique stimulus counts (images and video)**: The paper does not report the number of unique image identities or the cross-animal stimulus overlap structure. The values entered for `total_unique` and `per_subject_unique` are approximations derived under the assumption that the same stimuli were shown to all animals within each dataset split (train/eval), which is typical for SENSORIUM-style experiments but is not explicitly confirmed for the training set.
