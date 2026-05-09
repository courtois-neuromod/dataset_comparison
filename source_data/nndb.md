# Naturalistic Neuroimaging Database (NNDb)

**Reference:** Aliko, S., Huang, J., Gheorghiu, F., Meliss, S., & Skipper, J. I. (2020). A naturalistic neuroimaging database for understanding the brain using ecological stimuli. *Scientific Data*, 7, 347. https://doi.org/10.1038/s41597-020-00680-2

Data: https://openneuro.org/datasets/ds002837

---

## subjects_n: 86

> "The final sample consisted of 86 participants (42 females, range of age 18–58 years, M = 26.81, SD = 10.09 years). These were pseudo-randomly assigned to a movie they had not previously seen (usually) from a genre they reported to be less familiar with." (Methods, "Participants", p. 3)

Each participant was assigned to exactly one movie. Participant counts per movie are given in Table 1: N = 20 (500 Days of Summer), 18 (Citizenfour), and 6 each for the remaining 8 movies; total = 86.

---

## neuroimaging.fmri

### total_h: 160.59 / per_subject_h: 1.87

Each participant watched one full-length movie while fMRI was acquired. Movie lengths (in seconds) and participant counts from Table 2 and Table 1:

| Movie | Length (s) | N | Subtotal (s) |
|---|---|---|---|
| 500 Days of Summer | 5470 | 20 | 109400 |
| Citizenfour | 6804 | 18 | 122472 |
| 12 Years a Slave | 7715 | 6 | 46290 |
| Back to the Future | 6674 | 6 | 40044 |
| Little Miss Sunshine | 5900 | 6 | 35400 |
| The Prestige | 7515 | 6 | 45090 |
| Pulp Fiction | 8882 | 6 | 53292 |
| The Shawshank Redemption | 8181 | 6 | 49086 |
| Split | 6739 | 6 | 40434 |
| The Usual Suspects | 6102 | 6 | 36612 |
| **Total** | | **86** | **578120** |

578120 s / 3600 = 160.59 h; per_subject_h = 160.59 / 86 = 1.87 h.

> "From 5,470 to 8,882 volumes were collected per participant depending on which movie was watched (Table 2)." (Methods, "Acquisition", p. 7)

> "Functional and anatomical MRI and a final questionnaire were completed during a second session." (Methods, "Procedures", p. 3)

Acquisition parameters:

> "Functional and anatomical images were acquired on a 1.5 T Siemens MAGNETOM Avanto with a 32 channel head coil (Siemens Healthcare, Erlangen, Germany). We used multiband EPI (TR = 1 s, TE = 54.8 ms, flip angle of 75°, 40 interleaved slices, resolution = 3.2 mm isotropic, with 4x multiband factor and no in-plane acceleration)." (Methods, "Acquisition", p. 7)

---

## tasks.video, tasks.audio, and tasks.speech_listening

### total_unique: 19.44 / per_subject_unique: 1.87

Total unique content = sum of the 10 distinct movie lengths = 5470+6804+7715+6674+5900+7515+8882+8181+6739+6102 = 69982 s = 19.44 h. Each movie is counted once regardless of how many subjects watched it.

per_subject_unique = average unique content per subject = 578120 / 86 / 3600 = 1.87 h. Each subject watched exactly one movie (no repeated content within a subject).

> "Our goal for the NNDb v1.0 was to create an initial dataset with 84 participants watching 10 full-length movies from 10 genres." (Methods, "Participants", p. 3)

> "The movies were chosen to be from 10 different cinematic genres and to have an average score of >70% on publicly available metrics of success." (Methods, "Movie stimuli", p. 3)

### total_with_repetition: 160.59 / per_subject_with_repetition: 1.87

Each of the 86 participant-movie pairs represents one uninterrupted viewing. No subject watched any movie more than once. total_with_repetition = total fMRI time = 578120 s = 160.59 h.

per_subject_with_repetition = per_subject_unique = 1.87 h (no within-subject repetitions).

The same values apply to `audio` and `speech_listening`: all 10 movies are narrative feature films with full audio soundtracks and extensive dialogue throughout.

> "They had not previously seen the movies they watched because multiple viewings might change the functional network architecture of the brain." (Methods, "Participants", p. 3)

---

## Fields not included / flagged

- **Physiology (ECG, respiration, eye tracking, EDA):** Not reported. Participants were monitored by camera during scanning, but no physiological signals are described as collected or available.
- **tasks.controlled:** No controlled fMRI task was performed inside the scanner. The NIH Toolbox battery was administered behaviorally in session 1, outside the scanner.
- **tasks.resting_state:** No resting-state fMRI runs are described.
- **Structural MRI (T1w MPRAGE):** Collected for all participants (TR = 2.73 s, TE = 3.57 ms, 176 sagittal slices, 1.0 mm isotropic) but not counted in fMRI totals.
