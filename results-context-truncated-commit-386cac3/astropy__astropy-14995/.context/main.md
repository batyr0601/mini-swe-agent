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

- [ ] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce: create minimal script to reproduce NDDataRef mask propagation error (multiply with handle_mask=np.bitwise_or when one operand has no mask)
- [ ] 2. Locate: search repository for NDDataRef/NDData implementation files and methods using
- [ ] 3. Analyze: inspect the mask-combining logic to determine why a None mask leads to attempting bitwise_or with None and identify where to guard or convert None to appropriate masked value
- [ ] 4. Implement fix: update mask propagation logic to treat a missing mask as an all-False (or copy the other operand
- [ ] 5. Verify: write and run a small reproduction script and run relevant tests to confirm that operations like nref_mask.multiply(1., handle_mask=np.bitwise_or) no longer raise TypeError

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:42] **swebench-astropy__astropy-14995**: Task completed: Submitted
## Interaction Log

- `20:42:18` ACTION: Submitting solution
- `20:42:01` Patched _arithmetic_mask to return existing mask when other operand mask is None
- `20:41:42` RESULT: Patched astropy/nddata/mixins/ndarithmetic.py
- `20:41:42` ACTION: python - <<'PY'
- `20:41:17` Found issue in ndarithmetic._arithmetic_mask: when operand.mask is None and self.mask exists, code falls through to handle_mask causing TypeError; nee...
- `20:40:39` RESULT: (122 lines of output) First: 300	            kwargs["uncertainty"] = None...
- `20:40:38` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '300,360p' && nl -ba astropy/nddata/mixins/nda [...]
- `20:40:35` RESULT: (752 lines of output) First: 1	# Licensed under a 3-clause BSD style license - ...
- `20:40:34` ACTION: nl -ba astropy/nddata/mixins/ndarithmetic.py | sed -n '1,220p' && nl -ba astropy/nddata/mixins/ndari [...]
- `20:40:31` RESULT: (31 lines of output) First: astropy/nddata/nddata_withmixins.py:16:class NDDat...
- `20:40:30` ACTION: grep -Rn "class NDDataRef" astropy || true && grep -Rn "class NDData" astropy || true && grep -Rn "h [...]
- `20:40:27` RESULT: (36 lines of output) First: total 740...
- `20:40:26` ACTION: ls -la
- `20:40:23` RESULT: grep: testbed: No such file or directory
grep: testbed: No such file or directory
grep: testbed: No such file or directory
- `20:40:22` ACTION: grep -Rn "NDDataRef" testbed || true && grep -Rn "handle_mask" testbed || true && grep -Rn "class ND [...]
- `20:40:02` TASK STARTED: In v5.3, NDDataRef mask propagation fails when one of the operand does not have a mask
