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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:07] **swebench-astropy__astropy-8872**: Task completed: Submitted
## Interaction Log

- `03:07:17` ACTION: Submitting solution
- `03:06:41` Reproduced bug: Quantity(float16) was promoted to float64. Root cause: np.can_cast used with reversed args (np.can_cast(np.float32, value.dtype)) whic...
- `03:06:01` Reproduced bug: initial run showed Quantity(a, unit=u.m), a*u, and Quantity(..., copy=False) promoted float16 -> float64
- `03:05:31` ACTION: perl -0777 -pe 's/np\.can_cast\(\s*np\.float32\s*,\s*value\.dtype\s*\)/np.can_cast(value.dtype, np. [...]
- `03:05:07` ACTION: sed -n '280,420p' astropy/units/quantity.py
- `03:05:01` ACTION: grep -n "can_cast(np.float32" -n astropy/units/quantity.py || true
- `03:04:50` ACTION: python3 - <<'PY'
- `03:04:29` ACTION: sed -n '1,320p' astropy/units/quantity.py
- `03:04:20` ACTION: grep -n "class Quantity" astropy -R || true
- `03:04:12` ACTION: grep -RIn "float16\|float32\|float64\|dtype\|asarray\|Quantity" astropy | sed -n '1,200p'
- `03:04:06` ACTION: ls -la
- `03:04:03` RESULT: grep: testbed: No such file or directory
- `03:03:59` ACTION: grep -Rn "Quantity" testbed || true
- `03:03:50` TASK STARTED: float16 quantities get upgraded to float64 automatically
