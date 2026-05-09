# Natural Language fMRI (LeBel et al.) — Data Provenance

**Reference:** LeBel, A., Wagner, L., Jain, S. et al. "A natural language fMRI dataset for voxelwise encoding models." *Scientific Data* 10, 555 (2023). https://doi.org/10.1038/s41597-023-02437-z

**OpenNeuro:** ds003020

---

## subjects_n: 8

> "Eight participants (3 female, ages 21–34) were recruited from the University of Texas at Austin community."

Source: PMC full text (PMC10447563), Methods — Participants section.

---

## neuroimaging.fmri

### total_h: 81.0 ⚠️ approximate
### per_subject_h: 10.1 ⚠️ heterogeneous subjects

> "Participants completed 5 scanning sessions [...] totaling approximately 370 minutes of story listening" (primary dataset, all 8 subjects).
> "Three participants completed additional scanning sessions [...] totaling approximately 629 minutes of additional story listening" (extended dataset).

Source: PMC full text (PMC10447563).

Derivation:
- Primary (8 subjects): 8 × 370 min = 2,960 min = 49.3 h
- Extended (3 subjects extra): 3 × 629 min = 1,887 min = 31.5 h
- Combined total ≈ 81 h (confirmed by PMC: "approximately 81 hours")
- per_subject_h = 81.0 / 8 = 10.1 h (average; 5 subjects had ~6.2 h, 3 had ~16.7 h)

Note: this counts story-listening fMRI time only; additional scanning time for localizer tasks (visual category, motor, auditory cortex) is not included.

**Scanner specs (3T Siemens Skyra, TR = 2.0 s, voxel = 2.6 mm isotropic)** documented in paper but not in schema.

---

## tasks.speech_listening and tasks.audio

The stimuli are spoken narrative stories from *The Moth* podcast and *New York Times Modern Love* podcast — pure spoken-word audio with no music or video. Values for `audio` and `speech_listening` are therefore identical.

### per_subject_with_repetition: 10.1 h  (= total / subjects_n)
### total_with_repetition: 81.0 h

Same derivation as fmri.total_h above (all fMRI time is spent on story listening).

> "Each of the 5 scanning sessions began with a single test story that was repeated across all sessions to allow for test-retest reliability assessment."

Source: PMC full text (PMC10447563).

This means one story out of 27 primary stories was heard 5 times per primary subject (once per session), producing within-subject repetition. The 370 min total per primary subject includes these 5 repetitions of the test story.

### per_subject_unique: 9.3 h ⚠️ approximate and heterogeneous

Derivation:
- Primary subjects (n=5): unique listening ≈ 370 min − 4 × test_story_duration. Stories range from 8:24 to 16:53 min; assuming test story ≈ 12 min → ~322 min ≈ 5.4 h unique per primary subject. ⚠️ Test story duration not stated in paper.
- Extended subjects (n=3): ~5.4 h (primary unique) + 629 min (10.5 h additional, all unique) ≈ 15.9 h unique.
- Average across all 8 subjects: (5 × 5.4 + 3 × 15.9) / 8 = 9.3 h.

### total_unique: 15.9 h ⚠️ approximate

> "The primary dataset contains 27 unique narrative stories [...] The extended dataset adds 55 additional stories."

Source: PMC full text (PMC10447563).

Derivation:
- 27 primary stories (heard by all 8 subjects): unique duration ≈ 5.4 h (as above)
- 55 extended stories (heard by 3 subjects, all unique content): 629 min = 10.5 h
- total_unique ≈ 5.4 + 10.5 = 15.9 h

Note: both values depend on the unknown test story duration; flagged as approximate.

---

## Fields not populated

- `tasks.controlled`: localizer tasks were run (visual category localizer ×6, motor localizer ×2, auditory cortex localizer ×1) but durations were not reported in the accessible text; omitted.
- `tasks.resting_state`: not mentioned in the dataset description.
- `physiology`: no physiological recordings mentioned.
