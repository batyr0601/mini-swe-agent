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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 02:58] **swebench-astropy__astropy-13977**: Task completed: Submitted
## Interaction Log

- `02:58:06` ACTION: Submitting solution
- `02:58:01` EXCEPTION: TypeError - operand type(s) all returned NotImplemented from __array_ufunc__(<ufunc 'add'>, '__call__', <Quantity 1. m>, <__main__.Bad obje...
- `02:57:36` ACTION: python3 - <<'PY'
- `02:57:19` converters_and_unit located at astropy/units/quantity_helper/converters.py:141-240; raises UnitConversionError at lines 200-204, catches TypeError and...
- `02:56:54` ACTION: nl -ba astropy/units/quantity_helper/converters.py | sed -n '120,240p'
- `02:56:21` ACTION: python3 - <<'PY'
- `02:55:54` ACTION: nl -ba astropy/units/quantity_helper/converters.py | sed -n '1,240p'
- `02:55:40` ACTION: nl -ba astropy/units/quantity.py | sed -n '600,760p'
- `02:55:31` ACTION: grep -n "def __array_ufunc__" -R astropy | sed -n '1,200p'
- `02:55:03` ACTION: nl -ba astropy/units/quantity_helper/converters.py | sed -n '1,240p'
- `02:55:00` Found converters_and_unit at astropy/units/quantity_helper/converters.py:141
- `02:55:00` repro.py: TypeError: Unsupported operand type(s) for ufunc add: 'Quantity,str
- `02:54:44` ACTION: grep -n "def converters_and_unit" -R astropy | sed -n '1,200p'
- `02:54:40` RESULT: TypeError: Unsupported operand type(s) for ufunc add: 'Quantity,str'
- `02:54:29` ACTION: Reading file: <<'PY'
- `02:54:19` ACTION: nl -ba astropy/units/quantity.py | sed -n '560,740p'
- `02:54:07` ACTION: grep -n "def __array_ufunc__" -R astropy | sed -n '1,200p'
- `02:53:57` ACTION: ls -la
- `02:53:51` TASK STARTED: Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?
