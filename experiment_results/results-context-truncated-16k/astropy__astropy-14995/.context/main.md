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

- [2025-12-02 23:27] **swebench-astropy__astropy-14995**: Task completed: Submitted
## Interaction Log

- `23:27:40` ACTION: Submitting solution
- `23:27:38` Root cause: _arithmetic_mask called handle_mask with operand.mask == None when one operand had no mask; fixed by treating operand.mask is None same as...
- `23:27:38` found _arithmetic_mask in astropy/nddata/mixins/ndarithmetic.py (around lines 485-528)
- `23:27:38` repro: no mask * const: None; no mask * no mask: None; mask * const: mask array; mask * no mask: mask array; mask * mask: mask array
- `23:27:19` ACTION: Reading file: repro_nddata_mask.py
- `23:27:04` Replaced 'elif operand is None:' with 'elif operand is None or operand.mask is None:' in astropy/nddata/mixins/ndarithmetic.py
- `23:26:45` ACTION: sed -n '500,536p' astropy/nddata/mixins/ndarithmetic. [...]
- `23:26:20` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '1,600p'
- `23:26:11` ACTION: grep -nR "handle_mask" astropy || true
- `23:26:08` ACTION: grep -nR "NDDataRef" astropy || true
- `23:26:05` ACTION: ls -la
- `23:26:02` ACTION: grep -nR "class NDDataRef" testbed || grep -nR "NDDataRef" testbed
- `23:25:51` TASK STARTED: In v5.3, NDDataRef mask propagation fails when one of the operand does not have a mask
