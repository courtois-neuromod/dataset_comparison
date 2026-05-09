# MyConnectome

**Reference:** Poldrack et al. (2015). Long-term neural and physiological phenotyping of a single human. *Nature Communications*, 6, 8885. https://doi.org/10.1038/ncomms9885

---

## subjects_n: 1

> "We investigated the long-range dynamics of brain function and their relation to a broad set of psychological and biological variables in a single healthy human (author R.A.P.) over the course of 532 days."

One subject: the senior author R.A.P. (Russell A. Poldrack).

---

## neuroimaging.fmri.total_h: 14.0

**NOTE: This is a lower bound.** Only the confirmed resting-state fMRI hours are counted here. Table 1 reports additional task fMRI sessions (41 usable sessions across five paradigms) and breath-holding fMRI (18 usable sessions), but per-session run durations for these are not explicitly stated in the paper. Task session durations are estimated separately under `tasks.controlled`.

> "There were 84 usable 10-min rsfMRI runs during the study."

84 runs × 10 min = 840 min = **14.0 h** (resting fMRI only).

---

## tasks.resting_state: 14.0 h

> "There were 84 usable 10-min rsfMRI runs during the study, which were acquired [...] at consistent times of the day."

84 × 10 min = 840 min = **14.0 h**. Confirmed.

---

## tasks.controlled.total_h: 6.8 h  ⚠ APPROXIMATE

Table 1 lists the following usable task fMRI sessions:
- n-back (faces, scenes, Chinese characters): 15 sessions
- dot-motion stop signal: 8 sessions
- object localizer: 8 sessions
- spatial working-memory localizer: 4 sessions
- language localizer: 5 sessions
- retinotopic mapping: 1 session

Total: **41 sessions**. The paper does not state per-session run durations for tasks. Assuming ~10 min per session (consistent with the 10-min rsfMRI protocol):

41 × 10 min = 410 min ≈ **6.8 h**. Approximate — flag for verification.

> "Five different task activation paradigms were performed a varying number of times: an n-back task with faces, scenes and Chinese characters (15 sessions), a dot-motion stop signal task (eight sessions), an object localizer task with multiple-object classes (eight sessions), a spatial working-memory localizer (four sessions) and a language localizer (five sessions). In addition, we performed a single session of retinotopic visual mapping."

---

## tasks.contrasts: 12  ⚠ APPROXIMATE

The paper reports 237 statistical contrasts across sessions and tasks used for meta-analytic connectivity modelling, but these reflect across-session averages, not canonical condition contrasts. The approximate per-paradigm canonical contrast count is:

- n-back: face/scene/character categories × 2-back vs. 0-back → ~6 contrasts
- dot-motion stop signal: stop vs. go → ~2 contrasts
- object localizer: multiple object classes vs. baseline → ~2 contrasts
- spatial working-memory localizer: WM vs. control → ~1 contrast
- language localizer: language vs. visual baseline → ~1 contrast

Total: ~12 contrasts. **Approximate — not explicitly stated in the paper.**

> "Mean values for each parcel were extracted from statistical maps for each of the 237 statistical contrasts (across all sessions and tasks, except for retinotopy), and these were then used to generate a connectivity matrix reflecting the correlation of parcel activation across contrasts."
