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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [x] 1. Reproduce the issue using a minimal script based on the PR description
- [ ] 2. Locate Quantity.__array_ufunc__ implementation in testbed source files
- [ ] 3. Analyze code path: inspect how converters are applied and why ValueError is raised instead of returning NotImplemented
- [ ] 4. Implement fix: catch conversion ValueError in __array_ufunc__ and return NotImplemented to allow reflected ops
- [ ] 5. Run reproduction script and tests to verify behavior and edge cases
- [ ] 6. Log findings and mark todos complete as steps finish

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:41] **swebench-astropy__astropy-13977**: Task completed: Submitted
## Interaction Log

- `20:41:04` ACTION: Submitting solution
- `20:40:48` ACTION: pytest -q astropy/units -q
- `20:40:46` repro.py after patch: (1*m) + DuckArray(1 mm) returned DuckArray(ndarray=<Quantity 1.001 m>)
- `20:40:45` Change: astropy/units/quantity.py arrays conversion loop now catches ValueError from converter(input_) and returns NotImplemented to allow reflected _...
- `20:40:45` repro.py before patch: (1*m) + DuckArray(1 mm) raised ValueError from astropy/units/core.py:2629
- `20:40:18` ACTION: python3 - <<'PY'
- `20:39:59` ACTION: Reading file: repro.py
- `20:39:46` astropy/units/quantity.py:666-671: arrays built with converter(input_) which can raise ValueError; need to catch conversion failure and return NotImpl...
- `20:39:38` ACTION: nl -ba astropy/units/quantity.py | sed -n '580,760p'
- `20:39:33` ACTION: grep -nR "def __array_ufunc__" astropy || true
- `20:39:30` ACTION: ls -la
- `20:39:18` TASK STARTED: Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?
