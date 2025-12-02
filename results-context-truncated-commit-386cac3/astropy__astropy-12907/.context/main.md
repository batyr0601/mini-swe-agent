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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create a small script using astropy.modeling CompoundModels (e.g., Pix2Sky_TAN() & (Linear1D(10) & Linear1D(5))) and run separability_matrix to observe incorrect output
- [ ] 2. Locate the code: find the separability_matrix implementation in the modeling/separable module or equivalent file in the repository
- [ ] 3. Analyze root cause: inspect how separability_matrix enumerates inputs/outputs and how nested CompoundModels are flattened (or not), identify where nesting breaks mapping between parameters and component models
- [ ] 4. Implement fix: modify separability_matrix (or helper functions) to correctly flatten nested CompoundModel structures when computing separability, ensuring outputs/inputs mapping is per-leaf model
- [ ] 5. Verify fix: run the reproduction script, run the test suite, and add targeted tests for nested CompoundModel separability to prevent regressions

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:30] **swebench-astropy__astropy-12907**: Task completed: Submitted
## Interaction Log

- `19:30:58` ACTION: Submitting solution
- `19:30:54` TESTS: separability tests passed
- `19:30:52` Decision: replace assignment of 1 with copying the right ndarray into the cright block to preserve nested coord matrices; implemented change in separa...
- `19:30:52` Root cause: in astropy/modeling/separable.py::_cstack when right is an ndarray the code wrote 1s into the bottom-right block instead of copying the ri...
- `19:30:52` REPRO: Verified separability_matrix for cm, flat, and nested cases now produce expected outputs (nested case fixed)
- `19:30:37` RESULT: cm separability_matrix: [[ True False] [False True]] flat (Pix2Sky_TAN & Linear1D & Linear1D) separability_matrix: [[ True True False False] [...
- `19:30:35` ACTION: python - <<'PY'
- `19:30:21` RESULT: ✓ Logged to context
✓ Completed TODO #2: Find the function causing the error (look in X module)
- `19:30:21` Found issue in astropy/modeling/separable.py: _cstack assigns 1 for right ndarray instead of copying right matrix
- `19:30:21` ACTION: sed -i 's/cright\[-right.shape\[0\]:, -right.shape\[1\]:\] = 1/cright[-right.shape[0]:, -right. [...]
- `19:30:01` RESULT: (260 lines of output) First: 1	# Licensed under a 3-clause BSD style license - ...
- `19:30:00` ACTION: nl -ba astropy/modeling/core.py | sed -n '1,260p'
- `19:29:49` RESULT: (78 lines of output) First: 240	        cleft[: left.shape[0], : left.shape[1]...
- `19:29:48` ACTION: nl -ba astropy/modeling/separable.py | sed -n '240,520p'
- `19:29:47` RESULT: (240 lines of output) First: 1	# Licensed under a 3-clause BSD style license - ...
- `19:29:47` ACTION: nl -ba astropy/modeling/separable.py | sed -n '1,240p'
- `19:29:45` RESULT: (22 lines of output) First: ./CHANGES.rst:4535:- Add a ``separability_matrix``...
- `19:29:44` ACTION: grep -R --line-number "separability_matrix" . || true
- `19:29:42` RESULT: grep: testbed: No such file or directory
