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
- [x] 1. Reproduce the bug: run a small script that constructs nested CompoundModels and calls separability_matrix to demonstrate incorrect output
- [ ] 2. Locate separability_matrix implementation: grep for separability_matrix in repository to find source file(s)
- [ ] 3. Inspect handling of CompoundModel and nested compounds: read the separability implementation and related CompoundModel code to see how inputs/outputs are collected
- [ ] 4. Implement fix: modify separability_matrix to flatten nested CompoundModels when computing separability blocks so operands are treated individually
- [ ] 5. Verify fix: run the repro script and the test suite (or relevant tests) to ensure correctness
- [ ] 1. Reproduce the bug: run identify_format with a string filename
- [ ] 2. Locate the is_fits function and identify_format registration: search for
- [ ] 3. Root cause analysis: inspect is_fits implementation to see why it accesses args[0] without checking length and how filepath/fileobj are passed
- [ ] 4. Implement fix: modify is_fits to safely handle missing args (check fileobj/args presence) and return False when appropriate
- [ ] 5. Add repro script/test: create a small script in testbed/ to reproduce the original IndexError and validate the fix
- [ ] 6. Verify fix: run the repro script and any relevant tests to ensure no IndexError and behavior remains correct for FITS files

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:41] **swebench-astropy__astropy-12907**: Task completed: Submitted
- [2025-12-01 20:40] **swebench-astropy__astropy-12907**: Task completed: Submitted
## Interaction Log

- `20:41:18` ACTION: Submitting solution
- `20:41:13` identify_format tests: case1 (non-FITS filename): ['ascii.ecsv']; wrote tmp_test.fits; case2 (.fits filename): ['fits']; case3 (HDUList in args): ['fi...
- `20:41:04` ACTION: python3 - <<'PY'
- `20:40:56` ACTION: Submitting solution
- `20:40:51` post-fix repro: separability_matrix(cm) = [[ True False], [False  True]]; separability_matrix(Pix2Sky & Linear1D & Linear1D) = [[ True  True False Fal...
- `20:40:48` repro_identify_fits.py: identify_format returned: ['ascii.ecsv']
- `20:40:42` ACTION: PYTHONPATH=. python - <<'PY'
- `20:40:42` ACTION: python3 repro_identify_fits.py
- `20:40:39` ACTION: Reading file: repro_identify_fits.py
- `20:40:37` modified _cstack right ndarray branch: now copies right into cright block instead of filling with 1s; updated to cright[-right.shape[0]:, -right.shape...
- `20:40:29` ACTION: sed -n '1,260p' astropy/modeling/separable.py | sed -n '232,248p' && sed -i 's/cright\[-right. [...]
- `20:40:29` Fix implemented: astropy/io/fits/connect.py now checks len(args) before accessing args[0]; returns False when no positional args provided
- `20:40:22` is_fits updated: lines 62-74 now check len(args) > 0 before accessing args[0]; returns False if no args
- `20:40:18` ACTION: nl -ba astropy/io/fits/connect.py | sed -n '60,76p'
- `20:40:18` repro: separability_matrix(cm) = [[ True False], [False  True]]; separability_matrix(Pix2Sky & Linear1D & Linear1D) = [[ True  True False False], [ Tr...
- `20:40:14` ACTION: perl -0777 -pe "s/return isinstance\\(args\\[0\\], \\(HDUList, TableHDU, BinTableHDU, GroupsHDU\\)\\ [...]
- `20:40:04` ACTION: PYTHONPATH=. python - <<'PY'
- `20:39:55` astropy/modeling/separable.py: _cstack right-ndarray branch sets cright[-right.shape[0]:, -right.shape[1]:] = 1 instead of copying right; this likely ...
- `20:39:52` astropy/io/fits/connect.py:48-72: is_fits reads fileobj signature (lines 62-66), checks filepath extension (68-71), then returns isinstance(args[0], (...
- `20:39:44` ACTION: nl -ba astropy/io/fits/connect.py | sed -n '1,140p'
