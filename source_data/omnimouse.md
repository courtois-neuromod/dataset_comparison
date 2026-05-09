# OmniMouse

**Reference:** Willeke, K. F., Turishcheva, P., Gilbert, A., Chakrabarty, G., Bedel, H. A., Fahey, P. G., Qiu, Y., Weis, M. A., Vystrčilová, M., Muhammad, T., Ntanavara, L., Froebe, R. E., Ponder, K., Tan, Z. H., Orhan, E., Cobos, E., Sanborn, S., Franke, K., Sinz, F. H., Ecker, A. S., & Tolias, A. S. (2026). OmniMouse: Scaling properties of multi-modal, multi-task brain models on 150B neural tokens. *ICLR 2026*. https://arxiv.org/abs/2604.18827

---

## ⚠ Data provenance note

The OmniMouse paper reports aggregate statistics (total animals, total recording hours, total image and video frames) in Figure 2B, but does not provide a complete breakdown of data sources, stimulus structures, or unique stimulus counts. The annex identifies five published source datasets — Sensorium 2022, Sensorium 2023, MICrONS, Wang et al. (2025), and Fahey et al. (2019) — which together account for approximately **33 of the 69 training animals**. The remaining **~36 training animals (~52%) come from unpublished sources** that are not described in the paper.

This makes it impossible to independently verify the stimulus composition, unique image or video content, or cross-animal overlap for the majority of the training data. Fields derived from these totals — particularly `tasks.images.total_unique`, `tasks.images.per_subject_unique`, `tasks.video.total_unique`, and `tasks.video.per_subject_unique` — should be treated as rough approximations at best. A dataset presented at this scale, and used to support claims about neural scaling laws, would ordinarily be expected to provide this accounting transparently.

The entries below document what could be established from the published sources. Estimates for the remaining fields reflect the best available inference and are flagged accordingly.

---

## Dataset source breakdown

From the OmniMouse paper annex:
> "Model evaluation was performed on neurophysiological data from Sensorium 2022 (Willeke et al., 2022), Mouse 1 and 2, evaluation animals for Sensorium and Sensorium Plus tracks) and Sensorium 2023 (Turishcheva et al., 2024), all animals). Model training was performed on historical data, including data from MICrONS Consortium (2025), Wang et al. (2025), Ding et al. (2025b), Ding et al. (2025a), Fahey et al. (2019), Willeke et al. (2022), Turishcheva et al. (2024), but also included data not previously published."

**Figure 2B totals (OmniMouse paper, p. 4):**

| Split | Animals | Sessions | Duration | Image frames | Video frames |
|-------|--------:|--------:|---------:|-------------:|-------------:|
| Train | 69 | 316 | 543 h | 743,130 | 38.6 M |
| Eval | 7 | 7 | 14.6 h | 17,391 | 1.1 M |
| **Total** | **73** | **323** | **557.6 h** | **760,521** | **39.7 M** |

**Known data sources per split (from annex quote + source papers):**

| Split | Source | Animals | Stimulus structure (from source paper) |
|-------|--------|--------:|----------------------------------------|
| Eval | Sensorium 2022 Mouse 1 & 2 (Willeke et al., 2022) | 2 | 5,000 training images ×1 + 100 test images ×10 per animal; static images only |
| Eval | Sensorium 2023 — competition animals (Turishcheva et al., 2024) | 5 ⚠ | 60 min training video ×1 + val/test clips ×10; some static images (OOD track) |
| Train | Sensorium 2022 — pre-training mice 3–7 (Willeke et al., 2022) | 5 | 5,000 training images ×1 + 100 test images ×10 per animal |
| Train | Sensorium 2023 — pre-training animals (Turishcheva et al., 2024) | 5 ⚠ | Same structure as competition animals |
| Train | MICrONS (2025), Wang et al. (2025), Ding et al. (2025a, 2025b), Fahey et al. (2019), unpublished | ~59 ⚠ | Unknown — to be investigated |

⚠ = estimated, not explicitly stated in OmniMouse paper. The annex says Sensorium 2023 "all animals" for eval; if all 10 are in eval that would give 2+10=12 eval animals, contradicting Figure 2B's count of 7. Most likely interpretation: 5 Sensorium 2023 competition animals → eval, 5 pre-training animals → train.

**Ding et al. (2025a, 2025b):** Both are analysis papers using the same MICrONS mouse and recordings — no additional animals or stimulus data beyond what is already documented under MICrONS Consortium (2025).

**Still to investigate:** animal count and stimulus details for unpublished sources.

---

### Fahey et al. (2019) — training source detail

**Reference:** Fahey, P. G., Muhammad, T., Smith, C., et al. (2019). A global map of orientation tuning in mouse visual cortex. *bioRxiv*. https://doi.org/10.1101/745323

| Property | Value |
|----------|-------|
| Animals | **8 mice** (5 male, 3 female, aged 56–97 days) |
| Neurons per animal | ~49,000–68,000 (soma masks) |
| Visual areas | V1 + AM, PM, RL, AL, LM (layers 2–4) |
| Sessions per animal | 2–5 sessions, 9–14 scans per depth |
| Stimulus type | **Parametric only** — dynamic directional Gaussian noise (coherent orientation/motion) |

**Stimulus structure:** Directional Gaussian noise movie used to map orientation and direction tuning. Each scan: 72 blocks × 15 s = ~18 min, each block containing 16 directions of motion (0–360°). No natural images or natural videos.

> "A stimulus using smoothed Gaussian noise with coherent orientation and motion was used to probe neuronal orientation and direction tuning." (Methods, p. 5)

> "over 49,000–68,000 somas were segmented per animal" (Methods, p. 5)

**Implication for OmniMouse:** Fahey et al. contributes **8 training mice** with **parametric stimuli only** — no contribution to natural image or natural video frame counts. These frames fall in the "parametric movie" category (visible in OmniMouse Fig. 2C) rather than the natural image/video categories counted in `tasks.images` and `tasks.video`.

---

### Wang et al. (2025) — training source detail

**Reference:** Wang, E. Y., Fahey, P. G., Ding, Z., et al. (2025). Foundation model of neural activity predicts response to new stimulus types. *Nature* 640, 470–477. https://doi.org/10.1038/s41586-025-08829-y

| Property | Value |
|----------|-------|
| Animals (total dataset) | **14 mice** |
| Animals (foundation cohort, used to train core) | **8 mice** |
| Animals (new mice, used to test transfer) | **6 mice** |
| Neurons (foundation cohort) | ~66,000, layers 2–5 |
| Neurons (total) | ~135,000 |
| Visual areas | V1, LM, AL, RL, AM, PM (6 areas) |
| Total natural video (foundation cohort) | **>900 min** |
| Stimulus type | **Video only** (natural videos for training) |

**Stimulus structure:**

| Component | Used for | Notes |
|-----------|----------|-------|
| Natural videos (Sports1M, ecological) | Training | Shown in sessions of 4–76 min per mouse |
| Static natural images | Evaluation only | Not used in training |
| Drifting Gabors, flashing dots, directional pink noise, random dot kinematograms | Evaluation only | Out-of-distribution generalization test |

> "We recorded responses to ecological videos from approximately 135,000 neurons across multiple visual cortex areas in 14 awake, behaving mice. With a subset of these data, we trained a deep neural network on recordings from eight mice, producing a 'foundation core'..." (Abstract, p. 470)

> "combining data from multiple recording sessions, resulting in a total of more than 900 min of natural video responses from 8 mice, 6 visual areas (V1, LM, AL, RL, anteromedial (AM) and posteromedial (PM)) and around 66,000 neurons" (p. 472)

**Implication for OmniMouse:** Wang et al. is **video-only** → contributes to `tasks.video` frames, not `tasks.images` frames. Contributes **14 training mice**. Estimated total video: >900 min for 8 mice; full 14-mouse total not explicitly stated. Note: Wang et al. and MICrONS are **separate datasets** from the same lab group — MICrONS is 1 mouse with EM co-registration; Wang et al. is 14 different mice without EM.

---

### MICrONS Consortium (2025) — training source detail

**Reference:** MICrONS Consortium et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. *Nature* 640, 435–447. https://doi.org/10.1038/s41586-025-08790-w

| Property | Value |
|----------|-------|
| Animals | **1 mouse** |
| Sessions (scans) | **14** (postnatal day 75–81) |
| Neurons | ~75,909 excitatory neurons, layers 2–5, VISp + VISrl + VISal + VISlm |
| Duration per scan | ~84 min |
| Total recording time | ~19.6 h (14 × 84 min) |
| Stimulus type | **Video only** (no static images) |

**Stimulus structure per scan (~84 min total):**

| Component | Duration | Repeats | Unique content |
|-----------|--------:|--------:|---------------:|
| Natural video clips (cinematic, Sports1M, rendered POV; 10 s clips) | ~64 min total | ×1 each (except oracle) | ~55 min/scan |
| Oracle clips (6 natural film clips) | 10 min total | ×10 per scan | 1 min |
| Monet2 (parametric) | 10 min | ×1 per scan | 10 min ⚠ |
| Trippy (parametric) | 10 min | ×1 per scan | 10 min ⚠ |

⚠ Unclear whether Monet2/Trippy stimuli are the same or different across scans.

> "The majority of the stimulus (64 min) was made up of 10 s clips drawn from films, the Sports-1M dataset or rendered first-person point of view (POV) movement through a virtual environment... 6 natural film stimuli clips totalling 1 min (oracle natural videos) were repeated in the same order 10 times per scan... Monet2 and Trippy, 10 min each." (p. 437)

**Implication for OmniMouse:** MICrONS is **video-only** → contributes to OmniMouse `tasks.video` frames, not `tasks.images` frames. Estimated contribution: ~14 × 84 min × 60 s × 30 fps ≈ **2.1 M video frames** out of 38.6 M training video frames. Within-animal repetitions confirmed (oracle clips ×10 per scan).

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

### total_unique: 10,769 ⚠ approximate — likely a significant overestimate

**Uncertain — not directly reported in the paper.** Derived under the assumption that the same image set was shown to all training animals (as is typical in SENSORIUM-style experiments) AND that images were shown only once per animal. Under these assumptions:
- Unique images in training ≈ 743,130 / 69 ≈ 10,769
- Unique images in eval ≈ 17,391 / 7 ≈ 2,484

Value uses 10,769 as total_unique, assuming eval images are a subset of the training image set. If eval images are entirely disjoint, total_unique would be ~13,253.

The paper does not report the number of unique image identities or the cross-animal stimulus overlap structure.

**Evidence from Sensorium 2022 (Willeke et al., 2022; arXiv:2206.08666) — the dataset likely underlying the OmniMouse eval set:**
- Each of the 7 Sensorium animals was shown **5,000 single presentations** of training images plus **100 test images × 10 repetitions** per recording.
- Total per animal: ~6,000 image presentations; unique per animal: ~5,100 (5,000 training + 100 test).
- The OmniMouse eval set has 17,391 frames / 7 animals ≈ 2,484 frames/animal — consistent with only the test portion (~200 unique images × 10 repeats = 2,000 frames) being included in the OmniMouse eval split.
- This implies eval unique images ≈ 200 per animal (not 2,484), making `total_unique` for the eval split ≈ 200, not 2,484.

**Consequence:** The `total_unique` and `per_subject_unique` estimates are very likely overestimates. The true per-subject unique image count is probably ~5,100 for training animals and ~200 for eval animals. These fields should be revisited once the OmniMouse paper's stimulus structure is confirmed.

### per_subject_unique: 10,418 ⚠ approximate — likely a significant overestimate

Average across 73 mice under the same assumptions as above. Sensorium 2022 evidence (see above) suggests:
- Training animals: ~5,100 unique images each (5,000 single-presentation training images + 100 repeated test images)
- Eval animals: ~200 unique images each (test images only, shown 10× per animal)
- Weighted average: (69 × 5,100 + 7 × 200) / 73 ≈ 4,833

The paper does not report within-animal repetition counts for images. The current YAML value of 10,418 assumes zero within-animal repetition, which contradicts the Sensorium 2022 design.

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

### total_unique: 6.6 h ⚠ approximate — likely a significant overestimate

**Uncertain — not directly reported.** Estimated under two assumptions: (1) the same video stimuli are shown to all animals within each split; (2) training and eval video libraries are disjoint; (3) no within-animal repetition.

Under these assumptions:
- Unique video in training ≈ 357.4 h / 69 ≈ 5.2 h
- Unique video in eval ≈ 10.2 h / 7 ≈ 1.5 h
- Total unique ≈ 5.2 + 1.5 = **6.6 h**

**Evidence from Dynamic Sensorium 2023 (Turishcheva et al., 2023; NeurIPS 2024) — the dataset likely underlying the OmniMouse eval set:**
- Each of 10 animals received: **60 min training** (natural movies, one repeat each), **1 min validation** (10 repeats), **1 min live test** (10 repeats) + 1 min OOD (10 repeats), **1 min final test** (10 repeats) + 2 min OOD (10 repeats). Total: ~120 min per animal.
- Unique video per training animal: **60 min** (no within-session repeats for training).
- Unique video per eval animal (test portions only): **~3–5 min** (1–3 min of unique clips, rest are repeats).
- The OmniMouse eval set (1.1M frames / 7 animals ≈ 87 min/animal total) appears to include more than just test clips, possibly full recordings including training portions.
- If eval animals each have ~87 min total with a Sensorium 2023-like structure (60 min training unique + ~9 min test unique from 10× repeats), unique per eval animal ≈ ~1.2 h, and total eval unique ≈ 1.2 h (not 1.5 h).

**Consequence:** Training split estimate (5.2 h unique) is likely reliable if training videos are shown once per animal. Eval estimate (1.5 h) may be modestly overestimated due to 10× repeats in val/test portions. The total_unique of 6.6 h could reasonably be revised to ~6.2–6.5 h, pending confirmation of the OmniMouse stimulus structure.

### per_subject_unique: 5.0 h ⚠ approximate

Weighted average across 73 mice. Dynamic Sensorium 2023 evidence (see above) suggests unique video per animal is approximately:
- Training animals: ~5.2 h (60 min per session, multiple sessions, assuming different clips per session — unconfirmed)
- Eval animals: ~1.2 h (60 min training unique + ~9 min test unique)
- Weighted average: (69 × 5.2 + 7 × 1.2) / 73 ≈ 5.0 h

The current estimate may be reasonable for training animals if sessions show non-overlapping clips, but is uncertain. The paper does not describe the within-session or cross-session repetition structure for video stimuli.

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
