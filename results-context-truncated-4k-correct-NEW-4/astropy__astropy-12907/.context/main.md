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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `18:35:38` ACTION: sed -n '1,420p' astropy/modeling/separable.py
- `18:35:31` ACTION: grep -nR "separability_matrix" astropy || true
- `18:35:16` ACTION: ls -la astropy
- `18:35:08` ACTION: ls -la
- `18:34:52` ACTION: grep -n "def separability_matrix" astropy/modeling/separable. [...]
- `18:34:41` repro: Model repr: <CompoundModel(amplitude_0=1., mean_0=0., stddev_0=1., c0_1=0., c1_1=0., c0_2=0., c1_2=0.)>; separability_matrix output: [[ True]]
- `18:34:33` ACTION: python3 - <<'PY'
- `18:34:11` ACTION: grep -n "def separability_matrix" astropy/modeling/separable. [...]
- `18:33:33` ACTION: sed -n '1,400p' astropy/modeling/separable.py
- `18:33:27` ACTION: grep -R --line-number "separability_matrix" .
- `18:31:48` ACTION: grep -n "def separability_matrix" astropy/modeling/separable. [...]
- `18:31:15` ACTION: pytest -q
- `18:31:05` ACTION: sed -n '66,400p' astropy/modeling/separable.py
- `18:30:58` RESULT: 66:def separability_matrix(transform):
- `18:30:57` ACTION: grep -n "def separability_matrix" astropy/modeling/separable.py || true
- `18:30:47` ACTION: sed -n '1,400p' astropy/modeling/separable.py
- `18:30:41` ACTION: grep -R --line-number "separability_matrix" -n .
- `18:30:26` TASK STARTED: Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels
