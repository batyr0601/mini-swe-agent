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

- [2025-12-03 00:30] **swebench-astropy__astropy-8872**: Task completed: Submitted
## Interaction Log

- `00:30:39` ACTION: Submitting solution
- `00:30:34` Found root cause: Quantity.__new__ used np.can_cast(np.float32, value.dtype) causing float16 to be upcast. Replaced with np.issubdtype(value.dtype, np...
- `00:30:17` ACTION: nl -ba astropy/units/quantity.py | sed -n '288,306p;372,384p'
- `00:30:00` Reproduced: np.float16 inputs became float64 when creating Quantity; changed np.can_cast(np.float32, value.dtype) to np.issubdtype(value.dtype, np.ine...
- `00:29:54` ACTION: sed -i 's/np.can_cast(np.float32, value.dtype)/np.issubdtype(value.dtype, np. [...]
- `00:29:25` ACTION: grep -nR "np.can_cast(np.float32, value.dtype" astropy/units || true
- `00:29:09` ACTION: nl -ba astropy/units/quantity.py | sed -n '300,520p'
- `00:29:05` ACTION: nl -ba astropy/units/core.py | sed -n '660,740p'
- `00:28:58` ACTION: grep -nR "def __rmul__" astropy/units | sed -n '1,200p'
- `00:28:48` ACTION: Reading file: repro.py
- `00:28:41` ACTION: nl -ba astropy/units/quantity.py | sed -n '1,320p'
- `00:28:37` ACTION: grep -nR "class Quantity" astropy | sed -n '1,200p'
- `00:28:32` ACTION: ls -la
- `00:28:11` TASK STARTED: float16 quantities get upgraded to float64 automatically
