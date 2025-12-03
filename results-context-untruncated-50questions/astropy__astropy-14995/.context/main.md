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

- [2025-12-03 00:28] **swebench-astropy__astropy-14995**: Task completed: Submitted
## Interaction Log

- `00:28:09` ACTION: Submitting solution
- `00:28:07` Verification: repro_nddata_mask.py now shows mask*constant and mask*no mask return the copied mask ([[0,1,64],[8,0,1],[2,1,0]]) and no TypeError
- `00:27:54` Implement fix: change _arithmetic_mask to copy existing mask when the other is None, and guard handle_mask None case.
- `00:27:52` Root cause: _arithmetic_mask called handle_mask(self.mask, operand.mask) even when one mask was None; bitwise_or fails on int|None. Fix: explicitly ha...
- `00:27:47` Found _arithmetic_mask: astropy/nddata/mixins/ndarithmetic.py:485 (referenced at 221,335)
- `00:27:39` ACTION: grep -n "_arithmetic_mask" astropy/nddata/mixins/ndarithmetic.py || true
- `00:27:29` Repro script: mask*constant raised TypeError before patch; after patch mask is copied as expected
- `00:27:27` ACTION: python3 repro_nddata_mask.py
- `00:27:15` ACTION: python3 - <<'PY'
- `00:26:36` ACTION: Reading file: repro_nddata_mask.py
- `00:26:16` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '240,320p'
- `00:26:03` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '440,780p'
- `00:26:00` ACTION: grep -nE "_arithmetic_mask|handle_mask|mask\s*=" astropy/nddata/mixins/ndarithmetic.py || true
- `00:25:45` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '1,240p'
- `00:25:43` ACTION: grep -nR "NDDataRef" astropy || true
- `00:25:39` ACTION: ls -la
- `00:25:26` TASK STARTED: In v5.3, NDDataRef mask propagation fails when one of the operand does not have a mask
