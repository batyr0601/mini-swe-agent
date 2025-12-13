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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:25] **swebench-astropy__astropy-13977**: Task completed: Submitted
## Interaction Log

- `00:25:24` ACTION: Submitting solution
- `00:25:18` Verified fix by running repro.py: all three cases produce expected outcomes without raising ValueError
- `00:25:16` Implemented fix: Quantity.__array_ufunc__ now returns NotImplemented on ValueError/TypeError from converters_and_unit or converter application
- `00:25:05` Root cause: converters_and_unit or converter application can raise ValueError/TypeError when inputs are incompatible (e.g., duck-typed objects). Fix: ...
- `00:24:55` ACTION: python3 repro.py
- `00:24:53` repro.py output: Case A OK, Case B OK, Case C now returns DuckArray result instead of raising ValueError
- `00:24:50` ACTION: Reading file: repro.py
- `00:24:30` Modified Quantity.__array_ufunc__ to return NotImplemented on ValueError/TypeError from converters_and_unit and converter application
- `00:24:28` RESULT: patched
- `00:24:27` ACTION: python3 - <<'PY'
- `00:23:58` ACTION: nl -ba astropy/units/quantity.py | sed -n '1,120p'
- `00:23:49` ACTION: nl -ba astropy/units/quantity_helper/converters.py | sed -n '1,260p'
- `00:23:44` ACTION: grep -nR "def converters_and_unit" -n astropy || true
- `00:23:39` ACTION: nl -ba astropy/units/quantity.py | sed -n '560,740p'
- `00:23:32` ACTION: grep -nR "__array_ufunc__" . || true
- `00:23:28` RESULT: grep: testbed: No such file or directory
- `00:23:28` ACTION: grep -nR "__array_ufunc__" testbed || true
- `00:23:19` TASK STARTED: Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?
