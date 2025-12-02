# Project Goals

**Current Task:** Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels

<details>
<summary>Full description</summary>

Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels
Consider the following model:

```python
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

cm = m.Linear1D(10) & m.Linear1D(5)
```

It's separability matrix as you might expect is a diagonal:

```python
>>> separability_matrix(cm)
array([[ True, False],
       [False,  True]])
```

If I make the model more complex:
```python
>>> separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5))
array([[ True,  True, False, False],
       [ True,  True, False, False],
       [False, False,  True, False],
       [False, False, False,  True]])
```

The output matrix is again, as expected, the outputs and inputs to th...
</details>


## TODO List

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create a small script showing separability_matrix difference between nested and non-nested CompoundModels
- [ ] 2. Locate the code: find implementation of separability_matrix and related helpers in the codebase
- [ ] 3. Root cause analysis: inspect how separability_matrix handles CompoundModel and whether it flattens nested compounds or incorrectly reuses child separability
- [ ] 4. Implement fix: modify separability_matrix to correctly traverse nested CompoundModels (flatten or handle recursively) and update related logic
- [ ] 5. Verify fix: run the reproduction script and existing tests, capture outputs and log findings
- [ ] 1. Understand the bug: create minimal repro scripts that call separability_matrix and is_separable on simple and compound models (e.g., Shift, Scale, Rotation2D, Mapping, Polynomial2D) and record unexpected outputs

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:03:39` ACTION: sed -n '1,400p' astropy/modeling/separable.py
- `01:03:33` ACTION: grep -nR "separability_matrix" -n || true
- `01:03:18` TASK STARTED: Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels
