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

- [2025-12-02 20:58] **swebench-astropy__astropy-8872**: Task completed: Submitted
## Interaction Log

- `20:58:47` ACTION: Submitting solution
- `20:58:41` repro output: quantity dtype after construction: float16
- `20:58:34` RESULT: quantity dtype after construction: float16
- `20:58:33` ACTION: python3 - <<'PY'
- `20:58:14` Root cause: code checked can_cast(np.float32, value.dtype) which is false for float16, causing an unnecessary upcast; fix: swap args to check if value...
- `20:58:14` repro output: quantity dtype after construction: float16
- `20:58:14` sed confirmed code now uses np.can_cast(value.dtype, np.float32)
- `20:58:14` Replaced np.can_cast(np.float32, value.dtype) with np.can_cast(value.dtype, np.float32) in astropy/units/quantity.py
- `20:57:53` ACTION: grep -n "np.can_cast(np.float32, value.dtype)" astropy/units/quantity. [...]
- `20:57:09` ACTION: sed -n '340,400p' astropy/units/quantity.py
- `20:57:03` ACTION: grep -nE "astype\(|np\.asarray\(|np\.array\(|np\.asanyarray\(|dtype\s*=" astropy/units/quantity. [...]
- `20:56:45` ACTION: sed -n '260,420p' astropy/units/quantity.py
- `20:56:38` ACTION: grep -nE "astype\(|np\.asarray\(|np\.array\(|np\.asanyarray\(|dtype\s*=" astropy/units/quantity.py
- `20:56:16` ACTION: sed -n '260,400p' astropy/units/quantity.py
- `20:56:05` ACTION: grep -nE "dtype|astype\(|np\.asarray\(|np\.array\(" astropy/units/quantity.py || true
- `20:55:49` ACTION: grep -nR -E "float16|float64|astype\(|\bdtype\b|np\.asarray\(|np\.array\(" astropy/units || true
- `20:55:36` ACTION: grep -nR -E "float16|float64|astype\(|\bdtype\s*=|np\.asarray\(|np\.array\(" astropy/units || true
- `20:55:20` ACTION: grep -nR -E "astype\(|\bdtype\b|np\.asarray\(|np\.array\(|np\. [...]
- `20:55:06` ACTION: grep -nR -E "astype\(|np\.asarray\(|np\.array\(|dtype\s*=|float16|float64" astropy/units || true
- `20:54:51` ACTION: grep -nR -E "astype\(|\bdtype\s*=|float64|asarray\(|np\.array\(|np\.asarray\(" astropy/units || true
