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
- [x] 1. Reproduce the bug with a minimal script demonstrating nested CompoundModel separability mismatch
- [ ] 2. Locate separability_matrix implementation in the repository source files (search for function name)
- [ ] 3. Analyze how CompoundModel and nested compounds are handled by separability_matrix (inspect relevant files)
- [ ] 4. Implement fix: ensure separability_matrix correctly handles nested CompoundModels by flattening or properly mapping inputs/outputs across nested compounds
- [ ] 5. Add a regression script/test that reproduces the original PR example and asserts expected separability
- [ ] 6. Run the reproduction script and any unit tests to verify the fix

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:42] **swebench-astropy__astropy-12907**: Task completed: Submitted
## Interaction Log

- `19:42:06` ACTION: Submitting solution
- `19:42:01` pytest astropy/modeling/tests/test_separable.py: 11 passed in 0.17s; RuntimeWarning: numpy.ndarray size changed, may indicate binary incompatibility
- `19:41:45` ACTION: python -m pytest -q astropy/modeling/tests/test_separable.py
- `19:41:39` Added repro.py that constructs the models from the PR and prints separability matrices for cm, flat complex, and nested (Pix2Sky_TAN & cm)
- `19:41:26` Analysis: _separable recurses for CompoundModel; _cstack builds cleft and cright and previously set cright slice to 1 when right was ndarray (separabl...
- `19:41:16` ACTION: nl -ba astropy/modeling/separable.py | sed -n '216,260p'
- `19:41:11` Located separability_matrix in astropy/modeling/separable.py: lines 66-102; helper _compute_n_outputs at 105-126; _cstack at 219-247; _separable at 29...
- `19:41:03` ACTION: nl -ba astropy/modeling/separable.py | sed -n '60,110p'
- `19:40:57` repro.py: cm: [[ True False],[False  True]]; flat complex: [[ True  True False False],[ True  True False False],[False False  True False],[False False...
- `19:40:47` ACTION: Reading file: <<'PY'
- `19:40:37` Updated astropy/modeling/separable.py: in _cstack when right is ndarray, replaced cright[-right.shape[0]:, -right.shape[1]:] = 1 with cright[-right.sh...
- `19:40:29` ACTION: sed -i "s/cright\\[-right.shape\\[0\\]:, -right.shape\\[1\\]:\\] = 1/cright[-right. [...]
- `19:40:08` ACTION: nl -ba astropy/modeling/separable.py | sed -n '1,400p'
- `19:40:05` grep separability_matrix: astropy/modeling/separable.py:66,86,90,93,304; Model._calculate_separability_matrix in astropy/modeling/core.py:808; tests r...
- `19:39:56` ACTION: grep -nR "separability_matrix" . || true
- `19:39:45` TASK STARTED: Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels
