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

### total_unique: 739 | per_subject_unique: 554

Unique experimental conditions summed across all controlled tasks (naturalistic stimuli already counted above):

| Task | Conditions | Derivation |
|---|---|---|
| task-social | 18 | 2 cue × 3 intensity × 3 domain |
| task-faces | 288 | 96 unique face stimuli/run × 3 runs |
| task-shortvideo | 63 | 21 clips × 3 judgment types |
| fractional-posner | 2 | valid vs invalid cue |
| fractional-memory | 92 | 52 encoding images + 40 new distractors |
| fractional-tomspunt | 256 | 64 images × 2 questions × 2 mediums |
| fractional-tomsaxe | 20 | 10 false-belief + 10 false-photo stories |
| **Total** | **739** | |

Key quotes per task:

**task-social:** > "Each task was designed as a 2 cue (high/low) × 3 stimulus intensity (high/med/low) factorial design. The three tasks were conducted repeatedly on average, one week apart across three sessions." (3 domains: somatic pain, vicarious pain, cognitive effort) → 2 × 3 × 3 = 18 conditions.  
Source: Multimodal negative affect task, p. 5.

**task-faces:** > "Participants were presented with 288 dynamic faces of varying race, age, sex, and facial expression." and "96 trials in total (8 emotion x 2 sex x 3 race x 2 age)" per run × 3 runs = 288 unique face stimuli.  
Source: Dynamic faces task, p. 8.

**task-shortvideo:** > "63 trials (21 short videos x 3 judgments)" — likability, similarity, mental state attribution.  
Source: Video-based multiattribute social judgement task, Fig. 4, p. 7.

**task-fractional / posner:** > "A total of 120 trials were performed on this task." Primary manipulation: valid vs invalid cue = **2 conditions**.  
Source: Cognitive/ToM task A, p. 10–11.

**task-fractional / memory:** > "with a total of 26 × 2, i.e., 52 images" (encoding) + "40 × 2 images" for test (40 old + 40 new distractors) = **92 unique images**.  
Source: Cognitive/ToM task B, p. 11.

**task-fractional / tomspunt:** > "256 images, with 64 images crossed with 2 questions (why/how) and 2 mediums (face/hand)" = 64 × 2 × 2 = **256 unique conditions**.  
Source: Cognitive/ToM task C, p. 11.

**task-fractional / tomsaxe:** > "10 false belief stories" + "10 false photograph stories" = **20 unique stories**.  
Source: Cognitive/ToM task D, p. 11–12.

**Per subject (554):** All subjects complete social(18) + faces(288) + shortvideo(63) = 369 fixed conditions. For fractional, each subject gets 2 of 4 subtasks:

> "Each participant was pseudo-randomly assigned to undergo two subtasks, which were counterbalanced across participants."  
Source: Cognitive and Theory-of-mind task, p. 10.

Average conditions from 2 random subtasks drawn from {posner=2, memory=92, tomspunt=256, tomsaxe=20}: mean of all C(4,2)=6 pairs = (94+258+22+348+112+276)/6 = 185. Per subject: 369 + 185 = **554**.

Source: Table 4, pp. 8–9; task descriptions pp. 5–12.

---

## physiology.eda

### total_h: 585.8 | per_subject_h: 5.8

> "participants were invited to the MRI scanning facility, in which they completed experimental tasks with concurrent fMRI and physiological recordings of skin conductance and photoplethysmography"

Source: Overview of experimental procedures, p. 3.

> Fig. 2 confirms EDA (electrodermal activity) was collected during scanning across all four sessions.

Sessions totaled 91 + 96 + 83 + 80 = **350 min ≈ 5.8 h** per subject (session durations from Fig. 3, p. 6).  
**Approximate:** the paper does not give a precise breakdown of physiology recording time separate from structural scan time (T1, DWI). Value estimated from session totals; actual functional EPI time may be slightly less.

Total: 5.8 × 101 = **585.8 h**.

---

## physiology.plethysmograph

### total_h: 585.8 | per_subject_h: 5.8

> "concurrent fMRI and physiological recordings of skin conductance and photoplethysmography (Fig. 2)"

Source: Overview of experimental procedures, p. 3.

Fig. 2 labels this as "PPG" (photoplethysmograph). Same concurrent recording as EDA; same duration estimate (5.8 h per subject, **approximate** — see EDA note above).
