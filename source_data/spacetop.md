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

## naturalistic_stimuli.audio

### total_unique: 1.58 h | per_subject_unique: 1.58 h
### total_with_repetition: 159.5 h | per_subject_with_repetition: 1.58 h

`audio` covers all audio stimulation: (1) the 49 naturalistic video clips from `task-alignvideo` (1.44 h, which include spoken and other audio), and (2) the 4 audio narrative clips from `task-narratives` (0.14 h). All audio content in Spacetop is speech-bearing, so `audio` equals `speech_listening` (1.44 + 0.14 = 1.58 h).

> "in task-alignvideo, participants watch naturalistic videos and rate their emotional responses. Therefore, this task includes multimodal stimuli, incorporating both visual and auditory elements." (Overview of neuroimaging modalities and tasks, p. 3)

Values are identical to `naturalistic_stimuli.speech_listening` below.

---

## naturalistic_stimuli.speech_listening

### total_unique: 1.58 h | per_subject_unique: 1.58 h
### total_with_repetition: 159.5 h | per_subject_with_repetition: 1.58 h

`speech_listening` combines two sources: (1) the 49 naturalistic video clips from `task-alignvideo`, which include audio with spoken language, and (2) the 4 audio narrative clips from `task-narratives`.

**task-alignvideo (1.44 h per subject):**

> "in task-alignvideo, participants watch naturalistic videos and rate their emotional responses. Therefore, this task includes multimodal stimuli, incorporating both visual and auditory elements, and incorporates affective and social domains."

Source: Overview of neuroimaging modalities and tasks, p. 3.

Video duration: 86 min 9 sec = 1.44 h per subject (see `naturalistic_stimuli.video` above).

**task-narratives — audio clips (0.14 h per subject):**

> "Participants were instructed to read or listen to 8 different narratives while in the scanner."

Source: Naturalistic narratives task / task-narratives, p. 8.

Table 6 (p. 10) lists the 8 narrative clips. The 4 audio clips (run-01 stories 7 & 8; run-02 stories 5 & 6) have durations:
- Story 7: 2:01 = 121 s
- Story 8: 1:36 = 96 s
- Story 5: 2:30 = 150 s
- Story 6: 2:04 = 124 s

Total audio = 491 s ÷ 3,600 = **0.136 h ≈ 0.14 h** per subject.

**Combined:** 1.44 + 0.14 = **1.58 h** per subject unique.  
All 101 subjects received identical stimuli: total_with_repetition = 1.58 × 101 = **159.5 h** (= 145.4 + 14.1 h).

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

## tasks.contrasts

### total: 14 | per_subject: 12

Canonical neuroimaging contrasts for the four controlled tasks, as listed in Table 4 (p. 8):

> "We provide a detailed overview of the key contrasts inherent to each task (Table 4). These are the primary cognitive processes, or 'canonical' contrasts, which serve for understanding the core aspects of each tasks' design and its analytical focus."

Source: Overview of neuroimaging modalities and tasks, p. 3.

| Task | Contrasts | N |
|---|---|---|
| task-social | Somatic pain > baseline; Vicarious pain > baseline; Cognitive discomfort > baseline | 3 |
| task-faces | Age > baseline; Gender > baseline; Facial expression > baseline | 3 |
| task-shortvideo | Likeability > baseline; Similarity > baseline; Mental state attribution > baseline | 3 |
| Fractional "Why/how" (tomspunt) | Why > How | 1 |
| Fractional "False-belief" (tomsaxe) | False belief > False photograph | 1 |
| Fractional "Posner" | Invalid cue > Valid cue | 1 |
| Fractional "Memory" | Encoding > baseline; Retrieval > baseline | 2 |
| **Total** | | **14** |

Naturalistic tasks (task-alignvideo, task-narratives) are not included here — their contrasts (Video > baseline, Audio > Text, etc.) pertain to naturalistic stimuli already captured under `video`, `speech_listening`, and `text_reading`.

**Per subject (≈12):** All subjects complete the three non-fractional controlled tasks: social(3) + faces(3) + shortvideo(3) = 9 fixed contrasts. For task-fractional, each subject is pseudo-randomly assigned to 2 of 4 subtasks:

> "Each participant was pseudo-randomly assigned to undergo two subtasks, which were counterbalanced across participants."  
Source: Cognitive and Theory-of-mind task, p. 10.

Contrasts per fractional pair (6 combinations of 4 subtasks):
- {tomspunt, tomsaxe} = 2, {tomspunt, posner} = 2, {tomspunt, memory} = 3
- {tomsaxe, posner} = 2, {tomsaxe, memory} = 3, {posner, memory} = 3
- Average = (2+2+3+2+3+3)/6 = 2.5

Per subject: 9 + 2.5 = **11.5 ≈ 12**.

Source: Table 4, p. 8.

---

## active.controlled

### total_unique: 1.57 | per_subject_unique: 1.57
### total_with_repetition: 293.9 | per_subject_with_repetition: 2.91

Four controlled experimental tasks; durations from TR counts in Fig. 3 (TR = 0.46 s).

**Unique** counts each task once regardless of how many sessions or subjects ran it. task-social uses 3 sessions per subject (ses-01, ses-03, ses-04) but all three repeat the same 18-condition design, so unique = 1 session. task-fractional assigns each subject 2 of 4 subtasks but all subtasks share the same task environment, so unique = 2-subtask duration. All 101 subjects run the same task environment, so total_unique = per_subject_unique.

| Task | Unique runs | Unique duration | With-rep runs | With-rep duration |
|---|---|---|---|---|
| task-social | 6 × 872 TR | 2,407 s = 0.67 h | 18 × 872 TR | 7,220 s = 2.006 h |
| task-faces | 3 × 926 TR | 1,278 s = 0.355 h | same | same |
| task-shortvideo | 1 × 1,616 TR | 743 s = 0.206 h | same | same |
| task-fractional | 2 × 1,323 TR | 1,217 s = 0.338 h | same | same |
| **Total** | | **5,645 s ≈ 1.57 h** | | **10,459 s ≈ 2.91 h** |

> "In total, each run was designed to last 6 minutes and 41 seconds, i.e., 872 TRs."

Source: Multimodal negative affect task, p. 6.

> "The three tasks were conducted repeatedly on average, one week apart across three sessions."

Source: Multimodal negative affect task, p. 5 (justifying 3-session repetition counted once for unique).

Naturalistic tasks (task-alignvideo, task-narratives) are counted under `passive.*`, not here.

total_with_repetition: 2.91 × 101 = **293.9 h**.

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
