# Project Goals

**Current Task:** Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?

<details>
<summary>Full description</summary>

Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?
### Description
I'm trying to implement a duck type of `astropy.units.Quantity`. If you are interested, the project is available [here](https://github.com/Kankelborg-Group/named_arrays). I'm running into trouble trying to coerce my duck type to use the reflected versions of the arithmetic operators if the left operand is not an instance of the duck type _and_ they have equivalent but different units. Consider the following minimal working example of my duck type.

```python3
import dataclasses
import numpy as np
import astropy.units as u


@dataclasses.dataclass
class DuckArray(np.lib.mixins.NDArrayOperatorsMixin):
    ndarray: u.Quantity

    @property
...
</details>


## TODO List

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create repro script using DuckArray and perform (1 * u.m) + DuckArray(1 * u.mm) to trigger the ValueError
- [ ] 2. Locate the __array_ufunc__ implementation in Quantity: search files for
- [ ] 3. Root cause analysis: inspect converter lambda and _condition_arg usage to see where ValueError is raised during array coercion
- [ ] 4. Implement fix: modify Quantity.__array_ufunc__ to return NotImplemented instead of letting conversion raise ValueError when input is incompatible
- [ ] 5. Verify fix: run repro script and ensure DuckArray.__radd__ is invoked and no ValueError is raised
- [ ] 6. Commit and log findings

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:03:56` ACTION: sed -n '600,740p' astropy/units/quantity.py
- `01:03:52` grep __array_ufunc__: astropy/units/quantity.py:620,672,673,678; astropy/coordinates/angles.py:582,682; astropy/coordinates/spectral_quantity.py:86; a...
- `01:03:40` ACTION: grep -R --line-number "__array_ufunc__" . || true
- `01:03:35` RESULT: grep: testbed: No such file or directory
- `01:03:35` ACTION: grep -R --line-number "__array_ufunc__" -n testbed || true
- `01:03:18` TASK STARTED: Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?
