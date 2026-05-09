# Narratives dataset — data provenance

**Reference:** Nastase, S. A., et al. (2021). The "Narratives" fMRI dataset for evaluating models of naturalistic language comprehension. *Scientific Data*, 8, 250. https://doi.org/10.1038/s41597-021-01033-3

---

## subjects_n: 345

> "Across all datasets, 345 adults participated in data collection (ages 18–53 years, mean age 22.2 ± 5.1 years, 204 reported female)."

— Methods, Participants section, p. 2

---

## neuroimaging.fmri

### total_h: 154.0

Derived from the total TRs reported across all subjects and the TR of 1.5 s:

> "Concatenating across all subjects, this amounts to roughly 6.4 days worth of story-listening fMRI data, or 369,496 TRs."

— Methods, Stimuli section, p. 3

> "All studies used a repetition time (TR) of 1.5 seconds."

— Methods, MRI data acquisition, p. 5

Calculation: 369,496 TRs × 1.5 s / 3600 = **154.0 h**

### per_subject_h: 0.45

Calculation: 154.0 h / 345 subjects = **0.447 h ≈ 0.45 h**

---

## tasks.speech_listening

All scans involved passive listening to spoken story stimuli; therefore `speech_listening` matches the fMRI acquisition volume.

### total_unique: 4.65 h

> "In total, the auditory story stimuli sum to roughly 4.6 hours of unique stimuli corresponding to 11,149 TRs (excluding TRs acquired with no auditory story stimulus)."

— Methods, Stimuli section, p. 3

Also confirmed by Table 1: "Total: 4.6 hours, 11,149 TRs, 42,989 words"

Calculation: 11,149 TRs × 1.5 s / 3600 = **4.65 h** (the ~4.6 h figure in the paper is rounded)

The unique content consists of 27 distinct spoken stories ranging from ~3 to ~56 minutes:

> "The collection includes 345 unique subjects, 891 functional scans, and 27 diverse stories of varying duration totaling ~4.6 hours of unique stimuli (~43,000 words)."

— Abstract, p. 1

### per_subject_unique: 0.45 h

Different subjects participated in different story subsets (Table 1 shows per-story subject counts ranging from 16 to 82). Each subject heard each story at most once (with rare exceptions for the "Pie Man" story with run-1/run-2 sessions). Therefore per_subject_unique ≈ per_subject_with_repetition.

Calculation: 154.0 h / 345 subjects = **0.447 h ≈ 0.45 h**

**Flag:** This is an approximation. A small number of subjects contributed run-1 and run-2 data for the "Pie Man" story, meaning they heard the same story twice; this introduces a minor inflation in per_subject_with_repetition relative to per_subject_unique, but the effect is negligible at the dataset scale.

### total_with_repetition: 154.0 h

Same as fMRI total, as all functional scans involved story listening:

> "Concatenating across all subjects, this amounts to roughly 6.4 days worth of story-listening fMRI data, or 369,496 TRs."

Calculation: 369,496 TRs × 1.5 s / 3600 = **154.0 h**

### per_subject_with_repetition: 0.45 h

Calculation: 154.0 h / 345 subjects = **0.447 h ≈ 0.45 h**
