# Project Goals

**Current Task:** In v5.3, NDDataRef mask propagation fails when one of the operand does not have a mask

<details>
<summary>Full description</summary>

In v5.3, NDDataRef mask propagation fails when one of the operand does not have a mask
### Description

This applies to v5.3. 

It looks like when one of the operand does not have a mask, the mask propagation when doing arithmetic, in particular with `handle_mask=np.bitwise_or` fails.  This is not a problem in v5.2.

I don't know enough about how all that works, but it seems from the error that the operand without a mask is set as a mask of None's and then the bitwise_or tries to operate on an integer and a None and fails.

### Expected behavior

When one of the operand does not have mask, the mask that exists should just be copied over to the output.  Or whatever was done in that situation in v5.2 where there's no problem.

### How to Reproduce

This is with v5.3.   With v5.2, there a...
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

- [2025-12-03 03:02] **swebench-astropy__astropy-14995**: Task completed: Submitted
## Interaction Log

- `03:02:38` ACTION: Submitting solution
- `03:02:32` repro_mask2.py after fix c.mask matches a.mask: [[ True False] [False False]]
- `03:02:32` Fix implemented in astropy/nddata/mixins/ndarithmetic.py: replaced 'elif operand is None' with 'elif operand.mask is None' in _arithmetic_mask
- `03:02:32` repro_mask2.py before fix produced c.mask with None entries: [[True None] [None None]]
- `03:02:04` ACTION: perl -0777 -i -pe "s/elif operand is None:/elif operand. [...]
- `03:01:37` ACTION: Reading file: <<'PY'
- `03:01:12` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '480,560p'
- `03:01:03` ACTION: grep -n "handle_mask\|mask =" -n astropy/nddata/mixins/ndarithmetic.py || true
- `03:00:57` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '1,140p'
- `03:00:42` ACTION: Reading file: <<'PY'
- `03:00:19` ACTION: nl -ba astropy/nddata/nddata_withmixins.py | sed -n '1,400p'
- `03:00:08` ACTION: grep -nR "class NDDataRef" astropy || true
- `02:59:54` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '300,560p'
- `02:59:47` ACTION: grep -n "handle_mask" -n astropy/nddata/mixins/ndarithmetic.py || true
- `02:59:43` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '1,320p'
- `02:59:35` ACTION: nl -ba astropy/nddata/nddata_withmixins.py | sed -n '1,240p'
- `02:59:26` ACTION: grep -nR "class NDDataRef" astropy || true
- `02:59:21` ACTION: ls -la
- `02:59:15` TASK STARTED: In v5.3, NDDataRef mask propagation fails when one of the operand does not have a mask
