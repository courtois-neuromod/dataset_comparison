# studyforrest — data provenance

Primary reference: Hanke et al. (2016), "A studyforrest extension, simultaneous fMRI and eye gaze recordings during prolonged natural stimulation," *Scientific Data* 3:160092. DOI: 10.1038/sdata.2016.92.

> **Note:** This entry covers the 2016 audio-visual fMRI extension of the studyforrest dataset (15 subjects, 3 Tesla). The broader studyforrest project includes additional data releases not covered here, including the original audio-only fMRI acquisition at 7 Tesla (Hanke et al. 2014) and retinotopic mapping data (Sengupta et al. 2016).

---

## subjects_n = 15

"All 15 participants described in Sengupta et al.⁷ also volunteered for the simultaneous fMRI and eye gaze recording in this study. Consequently, additional BOLD fMRI data for all participants have been made available previously²⁴ and participant IDs are matched across all studies."
— Methods > Participants

An additional 15 in-lab participants watched the movie for eye-tracking only (no fMRI): "15 additional participants (age 19–30, mean 22.4, 10 females) volunteered for a separate eye tracking-only experiment." These are not counted in subjects_n as no fMRI data were acquired from them.

---

## neuroimaging.fmri

### per_subject_h = 2.0 / total_h = 30.0

Volumes per segment (8 segments): 451, 441, 438, 488, 462, 439, 542, 338. Total = 3599 volumes.
"The number of volumes acquired per movie segment was 451, 441, 438, 488, 462, 439, 542, and 338 volumes (for movie segments 1–8 respectively), and was therefore identical to the audio-only movie study²."
— Methods > fMRI data acquisition

TR = 2 s: "T2*-weighted echo-planar images (gradient-echo, 2 s repetition time (TR), 30 ms echo time, 90° flip angle...)"
— Methods > fMRI data acquisition

3599 volumes × 2 s = 7198 s = 119.97 min ≈ 2.0 h per subject. 15 subjects × 2.0 h = 30.0 h total.

---

## tasks.video and tasks.speech_listening

### total_unique = 2.0 / per_subject_unique = 2.0

The stimulus is the audio-visual version of the Hollywood motion picture 'Forrest Gump', with a German dubbed soundtrack. The movie contains continuous dialogue, narration, and sound throughout, justifying entries in both `video` and `speech_listening`.

"Participants watched and listened to the movie 'Forrest Gump' (R. Zemeckis, Paramount Pictures, 1994, dubbed German soundtrack). The stimulus source was the commercially available high-resolution Blu-ray disk release of the movie from 2011 (EAN: 4010884250916)."
— Methods > Stimulus

"Subsequently, the movie stimulus was shortened and cut into the same eight segments, approximately 15 min long each."
— Methods > Movie segment stimulus creation

Duration computed from segment volumes: 3599 volumes × 2 s = 7198 s = 2.0 h. Each subject watches the full movie once with no within-subject repetition, so unique = with_repetition for a single subject.

### total_with_repetition = 30.0 / per_subject_with_repetition = 2.0

All 15 subjects each watched the full 2.0 h movie once: 15 × 2.0 h = 30.0 h. No within-subject repetitions are reported.

---

## physiology.plethysmograph and physiology.respiration

### total_h = 30.0 / per_subject_h = 2.0

"Pulse oximetry and respiratory trace were recorded simultaneously with BOLD fMRI acquisition for the entire duration of the movie. The acquisition setup and the properties of the released data are described in the companion article⁷."
— Methods > Physiological recordings

Coverage is co-extensive with fMRI acquisition: 2.0 h per subject × 15 subjects = 30.0 h each.

One participant (sub-01) has no physiological data for segments 1–8 due to a technical failure (Table 1, row "P, participant 1, 1-8"). This would reduce the actual total slightly, but the nominal expected coverage is 30.0 h.

---

## physiology.eye_tracking

### total_h = 30.0 / per_subject_h = 2.0

"we recorded participants eye gaze coordinates for the entire duration of the movie simultaneously with the fMRI acquisition."
— Background & Summary

"Eye tracking was performed using monocular corneal reflection and pupil tracking with an Eyelink 1000 (software version 4.594) equipped with an MR-compatible telephoto lens and illumination kit (SR Research Ltd., Mississauga, Ontario, Canada). The temporal resolution of the eye gaze recording was 1000 Hz."
— Methods > Stimulation and eye tracking setup for fMRI acquisition

Coverage is co-extensive with fMRI acquisition: 2.0 h per subject. Table 1 lists several participant/segment combinations with eye tracking anomalies (>30% no-signal samples or excessive spatial error), so actual usable coverage is somewhat less than 30.0 h. The value here reflects the nominal recorded duration.

This entry counts only the 15 fMRI subjects. The additional 15 in-lab participants also have 2.0 h of eye tracking each (same movie), but are excluded from physiology totals since subjects_n = 15 refers to the fMRI cohort.
