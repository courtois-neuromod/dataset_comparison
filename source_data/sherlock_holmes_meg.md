# Sherlock Holmes MEG (Armeni et al.)

**Reference:** Armeni, K., Güçlü, U., van Gerven, M., & Schoffelen, J.-M. (2022). A 10-hour within-participant magnetoencephalography narrative dataset to test models of language comprehension. *Scientific Data*, 9, 278. https://doi.org/10.1038/s41597-022-01382-7

Data at Donders Repository: https://data.donders.nl/doc/dua/RU-DI-HD-1.0.html?3

---

## subjects_n: 3

> "A total of 3 (1 female) aged 35, 30, and 28 years were included in the study." (Methods, "Participants", p. 2)

---

## neuroimaging.meg

### total_h: 30.0 / per_subject_h: 10.0

The dataset title and abstract explicitly describe ~10 hours of MEG per participant, across 10 sessions of ~1 hour each.

> "A 10-hour within-participant magnetoencephalography narrative dataset to test models of language comprehension." (Title)

> "We recorded from 3 participants, 10 separate recording hour-long sessions each, while they listened to audiobooks in English." (Abstract, p. 1)

> "We recorded MEG data (275-channel axial gradiometer CTF system) while participants listened to audiobooks in English in a magnetically shielded room." (Methods, "MEG data acquisition", p. 5)

> "The MEG signals were digitized at a sampling rate of 1200 Hz (the cutoff frequency of the analog anti-aliasing low pass filter was 300 Hz)." (Methods, "MEG data acquisition", p. 5)

Total: 3 participants × 10 h = 30 h.

---

## tasks.speech_listening

### per_subject_unique: 10.0 / total_unique: 10.0

Participants listened to "The Adventures of Sherlock Holmes" — 10 stories from the same audiobook collection. All three participants listened to the same 10 stories in the same order. Unique content = ~10 h (one listening pass through the stories).

> "Here we describe a narrative comprehension magnetoencephalography (MEG) data record while three participants listened nearly 10 hours of audiobooks (see Fig. 1)." (Background & Summary, p. 2)

> "We used The Adventures of Sherlock Holmes by Arthur Conan Doyle as read by David Clarke and distributed through the LibriVox public library (https://librivox.org)." (Methods, "Stimulus materials", p. 2)

> "Each individual MEG session consisted of listening to a single story from the collection 'The Adventures of Sherlock Holmes'. Each recording session took place on a separate day." (Methods, "Task and experimental design", p. 3)

> "The order of story and run presentation were kept the same for all participants (see Table 1, supplementary information)." (Methods, "Task and experimental design", p. 3)

Since all three participants heard the same 10 stories (same order, same content), `total_unique = per_subject_unique = 10 h`.

### per_subject_with_repetition: 10.0 / total_with_repetition: 30.0

Each participant heard each story once (no within-subject repetition of the main story content). The between-run repeated stimulus ("noise_ceiling.wav") is a short ~30 s excerpt not part of the main stories, representing negligible additional content.

> "In between runs, we recorded MEG responses to a short (half minute) excerpt from The Adventures of Sherlock Holmes which was not used during the main task ('noise_ceiling.wav'). The stimulus was repeated twice between runs." (Methods, "MEG data acquisition", p. 5)

`per_subject_with_repetition = 10 h` (one pass through the 10 stories, no repetition).  
`total_with_repetition = 3 × 10 = 30 h`.

---

## physiology.eye_tracking

### total_h: 30.0 / per_subject_h: 10.0

Eye-tracking was recorded concurrently with MEG throughout all sessions.

> "Concurrently with the MEG, we recorded participants' eye-movements. We used the Eyelink 1000 Eyetracker (SR Research ©) at a sampling rate of 1000 Hz." (Methods, "Eye-tracking data acquisition", p. 7)

> "Along with the MEG data, we also tracked eye-movements and pupil dilations." (Fig. 1 caption, p. 3)

Coverage matches MEG sessions: 3 participants × 10 h = 30 h total.

---

## Fields not included / flagged

- **Structural MRI:** T1-weighted anatomical scans (3T MAGNETOM Skyra) were acquired for MEG-MRI coregistration purposes. These are not neuroimaging sessions in the neuroAI sense and are not included.
- **Audio field:** Not included separately — the stimulus is an audiobook (speech only), fully captured under `speech_listening`.
- **Repeated stimulus duration:** The ~30 s noise ceiling excerpt repeated twice between runs adds ~10 min per participant of additional MEG recording; this is negligible relative to the 10 h main recording and is not broken out separately.
- **Comprehension questions:** Brief multiple-choice comprehension checks were administered after each run but are not a separate experimental task.
