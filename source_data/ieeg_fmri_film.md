# Open multimodal iEEG-fMRI dataset (naturalistic film)

**Reference:** Berezutskaya, J., Vansteensel, M. J., Aarnoutse, E. J., Freudenburg, Z. V., Piantoni, G., Branco, M. P., & Ramsey, N. F. (2022). Open multimodal iEEG-fMRI dataset from naturalistic stimulation with a short audiovisual film. *Scientific Data*, 9, 91. https://doi.org/10.1038/s41597-022-01173-0

Data: https://openneuro.org/datasets/ds003688

---

## subjects_n: 63

Total unique participants across both modalities: 51 iEEG + 12 fMRI-only = 63. (18 subjects participated in both iEEG and fMRI; Table 1 lists sub-01 through sub-63.)

> "it includes a large amount of intracranial electroencephalography (iEEG) data (51 participants, age range of 5–55 years, who all performed the same task). Second, it includes functional magnetic resonance imaging (fMRI) recordings (30 participants, age range of 7–45 years) during the same task. Eighteen participants performed both iEEG and fMRI versions of the task, non-simultaneously." (Abstract, p. 1)

Unique subject count: 51 iEEG + 30 fMRI − 18 with both = 63.

---

## neuroimaging.fmri

### total_h: 3.25 / per_subject_h: 0.05

30 fMRI subjects × 6.5 min movie = 195 min = 3.25 h. per_subject_h = 3.25 / 63 = 0.052 ≈ 0.05.

> "In addition, there were twelve more patients who only participated in the fMRI version of the movie-watching task. In total, thirty participants were included (average age is 22, standard deviation is 11, 14 females)." (Methods, "fMRI participants", p. 2)

> "A 6.5-minute short movie, made of fragments from 'Pippi on the Run' (Pärymmen med Pippi Långstrump, 1970) was edited together to form a coherent plot with limited task duration." (Methods, "Movie stimulus", p. 4)

No resting-state fMRI was collected:
> "No resting state recordings during fMRI experiments were available." (Methods, "Resting state experiment", p. 4)

---

## neuroimaging.ieeg

### total_h: 8.03 / per_subject_h: 0.13

- Movie-watching (51 iEEG subjects): 51 × 6.5/60 = 5.53 h
- Resting state (50 subjects × 3 min): 50 × 3/60 = 2.50 h
- Total: 8.03 h; per_subject_h = 8.03 / 63 = 0.127 ≈ 0.13

> "Data from fifty-one iEEG patients (average age is 25, standard deviation is 15, 32 females) are included in the present dataset." (Methods, "iEEG participants", p. 2)

> "During iEEG recordings twenty-six iEEG patients participated in a three-minute resting state experiment." (Methods, "Resting state experiment (iEEG)", p. 4)

> "twenty-four patients did not participate in a separate resting state task. In order to provide some form of baseline neural activity for the these iEEG patients, we selected a 3-minute fragment of 'natural rest' from each of these patients' continuous 24/7 clinical iEEG recordings." (Methods, "Natural resting state data (iEEG)", p. 4)

Note: 26 (task rest) + 24 (natural rest) = 50 subjects with rest data. Sub-32 is missing resting state (noted in Usage Notes).

---

## tasks.video and tasks.speech_listening

### total_unique: 0.11 / per_subject_unique: 0.11

The movie is 6.5 min = 0.108 h of unique audiovisual content. All subjects watched the same stimulus, so total_unique = per_subject_unique = 0.11 h.

> "A 6.5-minute short movie, made of fragments from 'Pippi on the Run' [...] the movie consisted of 13 interleaved blocks of speech and music, 30 seconds each (seven blocks of music, six blocks of speech)." (Methods, "Movie stimulus", p. 4)

### total_with_repetition: 8.78 / per_subject_with_repetition: 0.14

All 51 iEEG subjects and all 30 fMRI subjects each watched the film once in their respective experiment sessions = 81 total viewings × 0.108 h = 8.75 h ≈ 8.78 h. The 18 subjects with both modalities watched the film twice (fMRI first, iEEG later).

per_subject_with_repetition = 8.78 / 63 = 0.139 ≈ 0.14 h.

> "Participants who performed the task with both recording modalities: first – with fMRI, and several days or weeks later – with iEEG." (Background & Summary, p. 2)

The same values apply to `speech_listening`: the film is a speech/language paradigm and contains dialogue throughout.

> "the movie consisted of 13 interleaved blocks of speech and music, 30 seconds each (seven blocks of music, six blocks of speech)" (p. 4)

---

## tasks.resting_state

### total_h: 2.50 / per_subject_h: 0.04

50 iEEG subjects × 3 min = 2.50 h. per_subject_h = 2.50 / 63 = 0.040 ≈ 0.04.

> "During iEEG recordings twenty-six iEEG patients participated in a three-minute resting state experiment." (p. 4)

> "we selected a 3-minute fragment of 'natural rest' from each of these [24] patients' continuous 24/7 clinical iEEG recordings." (p. 4)

> "No resting state recordings during fMRI experiments were available." (p. 4)

---

## Fields not included / flagged

- **Physiology (ECG, breathing, EMG, EOG):** Available for some iEEG subjects as part of the clinical trajectory; exact subject counts and durations not reported. Omitted.
  > "Additional behavioral recordings including electrocardiogram, electromyography, electrooculogram and respiration rate were collected as part of the clinical trajectory and are available for some patients." (Data acquisition, p. 5)
- **HD ECoG:** 6 subjects had high-density ECoG grids (up to 2000 Hz). These are part of the same iEEG sessions and are included in the iEEG totals.
- **Structural MRI:** T1-weighted scans acquired for most participants; not included in fMRI totals.
- **tasks.contrasts:** The block structure (speech vs. music) supports a 1-contrast language localizer. Not included here because the stimulus is a naturalistic film rather than a controlled experimental paradigm.
