# Project Goals

**Current Task:** float16 quantities get upgraded to float64 automatically

<details>
<summary>Full description</summary>

float16 quantities get upgraded to float64 automatically
When trying to create a `Quantity` from a `np.float16` (not something I actually intended to do, I was experimenting while investigating other issue) it gets upgraded automatically to `np.float64`, which is something that does not happen with other float types:

```
In [73]: np.float16(1)
Out[73]: 1.0

In [74]: (np.float16(1) * u.km)
Out[74]: <Quantity 1. km>

In [75]: (np.float16(1) * u.km).dtype
Out[75]: dtype('float64')
```

However:

```
In [76]: (np.float32(1) * u.km).dtype
Out[76]: dtype('float32')

In [77]: (np.float64(1) * u.km).dtype
Out[77]: dtype('float64')

In [78]: (np.float128(1) * u.km).dtype
Out[78]: dtype('float128')

In [79]: (np.float(1) * u.km).dtype
Out[79]: dtype('float64')

In [80]: ...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce: create a small script that multiplies np.float16 by u.km and prints the resulting Quantity dtype to confirm upgrade to float64
- [ ] 2. Locate: find the code in the testbed source that constructs Quantity objects or handles dtype promotion (likely files dealing with units/quantity creation)
- [ ] 3. Analyze: determine where np.float16 is being upcast to float64 and why (check dtype handling and numpy/asarray calls)
- [ ] 4. Implement fix: modify the Quantity construction/dtype handling to preserve float16 dtype (or document/explicitly cast) ensuring consistent behavior with np.float32/np.float64
- [ ] 5. Verify: run the reproduction script and existing tests to ensure float16 is preserved and no regressions occur

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:44] **swebench-astropy__astropy-8872**: Task completed: Submitted
## Interaction Log

- `20:44:05` ACTION: Submitting solution
- `20:43:58` TESTED: reproduced and observed dtypes
- `20:43:57` TEST: running reproduction of float16 behavior
- `20:43:38` TEST: running reproduction of float16 behavior
- `20:43:27` Decision: swap can_cast args to np.can_cast(value.dtype, np.float32) so float16 is preserved
- `20:43:27` Found issue: in astropy/units/quantity.py the np.can_cast call uses (np.float32, value.dtype) which is reversed and causes np.float16 to be upcast to ...
- `20:43:05` RESULT: (400 lines of output) First: 1	# -*- coding: utf-8 -*-...
- `20:43:04` ACTION: nl -ba astropy/units/quantity.py | sed -n '1,400p'
- `20:43:00` RESULT: astropy/coordinates/attributes.py:261:class QuantityAttribute(Attribute): astropy/coordinates/attributes. [...]
- `20:42:59` ACTION: grep -nR "class Quantity" astropy || true
- `20:42:56` RESULT: (37 lines of output) First: total 544...
- `20:42:55` ACTION: ls -la
- `20:42:45` TASK STARTED: float16 quantities get upgraded to float64 automatically
