# Project Goals

**Current Task:** `io.fits.FITSDiff` may sometimes report differences between identical files

<details>
<summary>Full description</summary>

`io.fits.FITSDiff` may sometimes report differences between identical files
### Description

In some scenarios, `io.fits.FITSDiff` may report differences between identical files, even when comparing the same file to itself. This may be caused by improper handling of VLAs (variable-length arrays).

### Expected behavior

`io.fits.FITSDiff` only reports differences in files if they exist. Comparing a file to itself should never yield a difference.

### How to Reproduce

```python
from astropy.io import fits
col = fits.Column('a', format='QD', array=[[0], [0, 0]])
hdu = fits.BinTableHDU.from_columns([col])
hdu.writeto('diffbug.fits', overwrite=True)

print(fits.FITSDiff('diffbug.fits', 'diffbug.fits').identical)
fits.printdiff('diffbug.fits', 'diffbug.fits')

```
Prints out:
```
F...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: run reproduction script that writes a VLA column and compare file to itself with FITSDiff
- [ ] 2. Locate FITSDiff code: search for FITSDiff class or function in testbed source files
- [ ] 3. Inspect VLA handling: find functions handling variable-length arrays (VLA) and table column comparisons
- [ ] 4. Implement fix: modify comparison logic to correctly handle VLA shapes/lengths so identical files are considered identical
- [ ] 5. Verify fix: run reproduction and tests to ensure FITSDiff reports identical for same file

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:43] **swebench-astropy__astropy-14539**: Task completed: Submitted
## Interaction Log

- `20:43:02` ACTION: Submitting solution
- `20:42:57` repro_vla.py: FITSDiff returned True and printdiff reported 'No differences found' after treating 'Q' as a VLA format in TableDataDiff
- `20:42:51` ACTION: python3 -u repro_vla.py
- `20:42:48` diff.py: updated TableDataDiff to treat 'Q' as VLA like 'P' (changed conditional at lines ~1452-1461 to 'elif (\"P\" in col.format) or (\"Q\" in col.f...
- `20:42:37` ACTION: sed -i 's/elif "P" in col.format:/elif ("P" in col.format) or ("Q" in col. [...]
- `20:42:21` repro_vla.py: ValueError 'The truth value of an array with more than one element is ambiguous' at diff.py:1463 (np.where(arra != arrb))
- `20:42:07` ACTION: Reading file: repro_vla.py
- `20:41:56` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1220,1500p'
- `20:41:53` RESULT: 1227:  1227	class TableDataDiff(_BaseDiff):
- `20:41:52` ACTION: nl -ba astropy/io/fits/diff.py | grep -n "class TableDataDiff" -n || true
- `20:41:48` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1,320p'
- `20:41:41` ACTION: grep -nR "FITSDiff\|printdiff\|variable-length\|variable length\|VLA\|vla\|variable_length" astropy/ [...]
- `20:41:38` ACTION: ls -la
- `20:41:35` grep FITSDiff: failed - testbed not found (grep: testbed: No such file or directory)
- `20:41:18` RESULT: grep: testbed: No such file or directory
- `20:41:18` ACTION: grep -nR "FITSDiff" -n testbed || true
- `20:41:07` TASK STARTED: `io.fits.FITSDiff` may sometimes report differences between identical files
