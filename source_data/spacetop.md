# Spacetop Dataset — Evidence Sidecar

**Primary reference:** Jung et al. (2025). Spacetop: A multimodal fMRI dataset unifying naturalistic processes with a rich array of experimental tasks. *Scientific Data*, 12, 1465. https://doi.org/10.1038/s41597-025-05154-x

---

## name
`Spacetop`

> "Here, we present an open dataset with N = 101 participants and 6 hours of scanning per participant..."

Source: Abstract, p. 1.

---

## reference
DOI: https://doi.org/10.1038/s41597-025-05154-x

Published online 22 August 2025.

---

## subjects_n: 101

> "This dataset includes 101 adult participants (mean ± s.d. age: 24.7 ± 5.5 years; 69 males, 45 females, 2 others)."

Source: Methods / Participants, p. 3.

The consort diagram (Fig. 1) confirms: 116 enrolled, 106 completed session 2, 102 completed session 3, **101 completed all four sessions**.

---

## neuroimaging.fmri

### total_h: 606.0
### per_subject_h: 6.0

> "N = 101 participants and 6 hours of scanning per participant"

Source: Abstract, p. 1.

> Table 1 lists "606" functional isohours for Spacetop (101 subjects × 6 h/subject).

Source: Table 1, p. 2.

---

## naturalistic_stimuli.video

### total_unique: 1.44 h | per_subject_unique: 1.44 h
### total_with_repetition: 145.4 h | per_subject_with_repetition: 1.44 h

> "A variety of 49 unique videos were presented to participants, ranging from 20 seconds to 5 min 39 seconds in duration, amounting to **86 minutes and 9 seconds** across 4 sessions. Each video file was played once, with no repetitions. The sequence of the videos were identical across participants, purposefully designed for functional alignment purposes."

Source: Naturalistic video viewing task / task-alignvideo, p. 4–5.

86 min 9 sec = 5,169 s ÷ 3,600 = **1.436 h ≈ 1.44 h** per subject.  
Each of 101 subjects watched the same 49 unique videos once: total_with_repetition = 1.44 × 101 = **145.4 h**.  
No within-subject repetition, so per_subject_with_repetition = per_subject_unique = 1.44 h.

Detailed per-video durations are in Table 5 (pp. 9–10).

---

## naturalistic_stimuli.speech_listening

### total_unique: 0.14 h | per_subject_unique: 0.14 h
### total_with_repetition: 14.1 h | per_subject_with_repetition: 0.14 h

> "Participants were instructed to read or listen to 8 different narratives while in the scanner."

Source: Naturalistic narratives task / task-narratives, p. 8.

Table 6 (p. 10) lists the 8 narrative clips with durations. The 4 audio clips (run-01 stories 7 & 8; run-02 stories 5 & 6) have durations:
- Story 7: 2:01 = 121 s
- Story 8: 1:36 = 96 s
- Story 5: 2:30 = 150 s
- Story 6: 2:04 = 124 s

Total audio = 491 s ÷ 3,600 = **0.136 h ≈ 0.14 h** per subject.

> "The entire task consisted of four runs, with two narratives..."

All 101 subjects heard the same 4 audio narratives: total_with_repetition = 0.14 × 101 = **14.1 h**.

Source: Table 6, p. 10.

---

## naturalistic_stimuli.text_reading

### total_unique: 0.20 h | per_subject_unique: 0.20 h
### total_with_repetition: 20.2 h | per_subject_with_repetition: 0.20 h

The 4 text narrative clips (run-03 stories 3 & 4; run-04 stories 1 & 2) from Table 6 have durations:
- Story 3: 3:11 = 191 s
- Story 4: 3:29 = 209 s
- Story 1: 2:43 = 163 s
- Story 2: 2:40 = 160 s

Total text = 723 s ÷ 3,600 = **0.201 h ≈ 0.20 h** per subject.

All 101 subjects read the same 4 text narratives: total_with_repetition = 0.20 × 101 = **20.2 h**.

Source: Table 6, p. 10.

---

## responses.controlled_tasks

### total_unique: 7 | per_subject_unique: 5

The dataset contains 9 fMRI task paradigms (Table 1, "# of fMRI Tasks: 9"), of which 2 are naturalistic (task-alignvideo, task-narratives) captured separately above. The remaining 7 are controlled experimental paradigms:

1. **task-social** — 3 domains (somatic pain, vicarious pain, cognitive effort), 2-cue × 3-intensity factorial design
2. **task-faces** — 96 trial types (8 emotion × 2 sex × 3 race × 2 age), 288 dynamic face stimuli across 3 runs
3. **task-shortvideo** — 21 short video clips × 3 judgment types (likability, similarity, mental state attribution) = 63 trials per run
4. **task-fractional / runtype-posner** — Attention reorienting, 120 trials
5. **task-fractional / runtype-memory** — Memory encoding-retrieval, 120 trials
6. **task-fractional / runtype-tomspunt** — Image-based theory of mind, 256 image × 2 question combinations
7. **task-fractional / runtype-tomsaxe** — Text-based theory of mind, 10 false-belief + 10 false-photograph stories

> "Each participant was pseudo-randomly assigned to undergo two subtasks [of task-fractional], which were counterbalanced across participants."

Source: Cognitive and Theory-of-mind task, p. 10.

Per subject: task-social + task-faces + task-shortvideo + 2 of 4 fractional subtasks = **5 controlled paradigms**.

Source: Table 4, pp. 8–9; task descriptions pp. 5–12.

---

## physiology.eda

### total_unique: 585.8 | per_subject_unique: 5.8

> "participants were invited to the MRI scanning facility, in which they completed experimental tasks with concurrent fMRI and physiological recordings of skin conductance and photoplethysmography"

Source: Overview of experimental procedures, p. 3.

> Fig. 2 confirms EDA (electrodermal activity) was collected during scanning across all four sessions.

Sessions totaled 91 + 96 + 83 + 80 = **350 min ≈ 5.8 h** per subject (session durations from Fig. 3, p. 6).  
**Approximate:** the paper does not give a precise breakdown of physiology recording time separate from structural scan time (T1, DWI). Value estimated from session totals; actual functional EPI time may be slightly less.

Total: 5.8 × 101 = **585.8 h**.

---

## physiology.plethysmograph

### total_unique: 585.8 | per_subject_unique: 5.8

> "concurrent fMRI and physiological recordings of skin conductance and photoplethysmography (Fig. 2)"

Source: Overview of experimental procedures, p. 3.

Fig. 2 labels this as "PPG" (photoplethysmograph). Same concurrent recording as EDA; same duration estimate (5.8 h per subject, **approximate** — see EDA note above).
