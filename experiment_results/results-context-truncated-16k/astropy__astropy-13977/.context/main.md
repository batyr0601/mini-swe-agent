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

- [2025-12-02 23:25] **swebench-astropy__astropy-13977**: Task completed: Submitted
## Interaction Log

- `23:25:07` ACTION: Submitting solution
- `23:25:01` repro ran: success output DuckArray(ndarray=<Quantity 1.001 m>)
- `23:25:00` ACTION: python3 repro.py && context_log "repro ran: success output DuckArray(ndarray=<Quantity 1. [...]
- `23:24:58` Patched astropy/units/quantity.py: catch ValueError from converter(input_) in __array_ufunc__ and return NotImplemented; repro now succeeds with DuckA...
- `23:24:54` ACTION: python3 - <<'PY'
- `23:24:21` ACTION: nl -ba astropy/units/core.py | sed -n '2580,2650p'
- `23:24:16` ACTION: nl -ba astropy/units/core.py | sed -n '1000,1100p'
- `23:24:12` repro.py: (1*u.m) + DuckArray(1*u.mm) raised ValueError in astropy/units/quantity.py during converters(input_) -> astropy/units/core.py:_condition_arg
- `23:24:01` ACTION: Reading file: repro.py
- `23:23:52` Found Quantity.__array_ufunc__ in astropy/units/quantity.py (lines 620-682). The conversion loop applies converters and can raise ValueError at conver...
- `23:23:32` ACTION: nl -ba astropy/units/quantity.py | sed -n '560,760p'
- `23:23:24` ACTION: grep -n "__array_ufunc__" -R astropy | sed -n '1,200p'
- `23:23:19` ACTION: ls -la
- `23:23:09` TASK STARTED: Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?
