# Midnight Scan Club (MSC)

**Reference:** Gordon et al., 2017, Neuron 95, 791–807. https://doi.org/10.1016/j.neuron.2017.07.011

**Data availability:** Freely available from openfmri.org and neurovault.org (stated in paper: "The complete MSC dataset is freely available from openfmri.org (Poldrack et al., 2013) and neurovault.org (Gorgolewski et al., 2015) as a resource for neuroscientists.")

---

## subjects_n: 10

From Table 1: "Gender M = 5, F = 5" — ten subjects total (MSC01–MSC10), ages 24–34 years (mean 29.1 ± 3.3).

---

## neuroimaging.fmri

### total_h: 110.0 / per_subject_h: 11.0

Each subject contributed 5 hr of resting-state fMRI and 6 hr of task fMRI, giving 11 hr per subject and 110 hr across 10 subjects.

From the Results section: "In each of the ten subjects, we collected 3.5 hr of structural MRI data; 5 hr of RSFC data; 6 hr of task-based fMRI data across three different tasks."

Confirmed in Figure 1 caption: "five hours of fMRI RSFC data, six hours of fMRI task data across three different tasks."

---

## tasks.resting_state

### total_h: 50.0 / per_subject_h: 5.0

From the Summary: "we assembled a novel MRI dataset containing 5 hr of RSFC data." Confirmed in Results: "5 hr of RSFC data."

All 10 subjects contributed 5 hr each → 50 hr total.

---

## tasks.controlled

### total_h: 60.0 / per_subject_h: 6.0

From the Summary: "6 hr of task-based fMRI data across three different tasks, including a blocked motor task, a mixed blocked and event-related perceptual and language task, and an event-related incidental memory task with multiple stimulus types."

From Figure 1: 20 runs of blocked motor (tongue/hand/foot), 20 runs of mixed block/event-related (noun/verb, coherence), and 30 runs of event-related memory (face M/F, scene in/out, abstract/concrete, puppy/not). All 10 subjects contributed 6 hr each → 60 hr total.

---

## tasks.contrasts

### total: 7 / per_subject: 7

From Figure 6 caption (p. 801): "Seven task contrasts were tested: 1) tongue motion > baseline; 2) left hand motion > right hand motion; 3) left leg motion > right leg motion; 4) face stimulus > word stimulus; 5) scene stimulus > face stimulus; 6) glass dot pattern > baseline; and 7) noun-verb stimulus > baseline."

All 10 subjects ran the same task battery, so per_subject = total = 7.
