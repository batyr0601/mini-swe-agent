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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:29] **swebench-astropy__astropy-14539**: Task completed: Submitted
## Interaction Log

- `23:29:17` ACTION: Submitting solution
- `23:29:04` repro_vla.py: verification passed; FITSDiff reported identical: True and fits.printdiff output 'No differences found.' for diffbug.fits vs itself.
- `23:29:04` Patched diff.py: extended 'P' branch to also handle object-dtype columns whose elements are ndarray/list/tuple by comparing per-row with np.asarray(.....
- `23:28:21` ACTION: python3 repro_vla.py
- `23:27:59` Patched diff.py: extended 'P' branch to also handle object-dtype columns whose elements are ndarray/list/tuple by comparing per-row with np.asarray(.....
- `23:27:06` TableDataDiff._diff: np.where(arra != arrb) fails for object-dtype variable-length array entries (col.format='QD(2)', arra.dtype=object, elements are ...
- `23:26:33` ACTION: python3 - <<'PY'
- `23:26:07` repro_vla.py: ValueError 'The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()' raised in astropy/io/fits/diff....
- `23:25:48` ACTION: Reading file: repro_vla.py
- `23:25:33` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1370,1600p'
- `23:25:30` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1216,1370p'
- `23:25:28` RESULT: 1227:class TableDataDiff(_BaseDiff):
- `23:25:28` ACTION: grep -n "class TableDataDiff" -n astropy/io/fits/diff.py || true
- `23:25:23` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '420,840p'
- `23:25:21` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1,420p'
- `23:25:18` RESULT: astropy/io/fits/diff.py:198:class FITSDiff(_BaseDiff):
- `23:25:18` ACTION: grep -n "class FITSDiff" -R astropy/io/fits || true
- `23:25:15` ACTION: ls -la
- `23:25:08` TASK STARTED: `io.fits.FITSDiff` may sometimes report differences between identical files
