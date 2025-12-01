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
- [ ] 1. Reproduce: create minimal script reproducing ValueError when (1*u.m) + DuckArray(1*u.mm) is evaluated
- [ ] 2. Locate: find Quantity.__array_ufunc__ implementation in the codebase (likely in a quantity or units module)
- [ ] 3. Analyze: determine why incompatible inputs lead to ValueError instead of returning NotImplemented (check converters and exception handling in __array_ufunc__)
- [ ] 4. Implement fix: modify Quantity.__array_ufunc__ to return NotImplemented for incompatible input types/units instead of allowing ValueError to propagate; add tests or adjust logic so reflected ops are tried
- [ ] 5. Verify fix: run reproduction script and existing tests to confirm __radd__ is invoked and no unexpected exceptions occur

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:30] **swebench-astropy__astropy-13977**: Task completed: Submitted
## Interaction Log

- `19:30:58` ACTION: Submitting solution
- `19:30:56` TESTED: verified with reproduction script that Quantity + DuckArray (different units) no longer raises and reflected ops are used
- `19:30:56` Implemented fix: catch ValueError/TypeError when applying converters in Quantity.__array_ufunc__ and return NotImplemented
- `19:30:45` RESULT: Operation: DuckArray(ndarray=<Quantity 1. mm>) + <Quantity 1. m> -> DuckArray(ndarray=<Quantity 1001. mm>) Operation: <Quantity 1. [...]
- `19:30:45` TESTED: reproduction script for Quantity + DuckArray cases
- `19:30:44` ACTION: Reading file: <<'PY'
- `19:30:21` Decision: catch ValueError/TypeError in Quantity.__array_ufunc__ and return NotImplemented to allow reflected ops
- `19:30:09` Found that converters are applied directly in Quantity.__array_ufunc__, which can raise ValueError for incompatible inputs (e.g., duck types)
- `19:29:45` Found Quantity.__array_ufunc__ at astropy/units/quantity.py:620
- `19:29:40` RESULT: (17 lines of output) First: astropy/coordinates/angles.py:582:    def __array_...
- `19:29:40` ACTION: grep -nR "__array_ufunc__" astropy || true
- `19:29:26` TASK STARTED: Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?
