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

- [2025-12-03 00:30] **swebench-astropy__astropy-14539**: Task completed: Submitted
## Interaction Log

- `00:30:35` ACTION: Submitting solution
- `00:29:36` ACTION: pytest -q astropy/io/fits/tests/test_diff.py::test_basic_diff -q || true
- `00:29:21` ACTION: python3 - <<'PY'
- `00:28:34` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1444,1464p'
- `00:27:59` ACTION: perl -0777 -pe 's/elif\s+"P"\s+in\s+col\.format\s*:/elif ("P" in col.format) or ("Q" in col. [...]
- `00:27:29` ACTION: nl -ba astropy/io/fits/column.py | grep -n "self.format\\|def format\\|@property\\s*def format" | se [...]
- `00:27:16` ACTION: nl -ba astropy/io/fits/column.py | grep -n "format" | sed -n '1,200p'
- `00:27:13` ACTION: grep -n "class Column" -n astropy/io/fits/column.py && nl -ba astropy/io/fits/column. [...]
- `00:26:43` ACTION: nl -ba astropy/io/fits/column.py | sed -n '1,320p'
- `00:26:39` ACTION: grep -nR "class Column\\|def _get_format\\|variable-length\\|VLA\\|varia" astropy/io/fits || true
- `00:26:03` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1400,1800p'
- `00:25:53` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1220,1400p'
- `00:25:51` RESULT: 1227:  1227	class TableDataDiff(_BaseDiff):
- `00:25:50` ACTION: nl -ba astropy/io/fits/diff.py | grep -n "class TableDataDiff" -n
- `00:25:48` ACTION: nl -ba astropy/io/fits/diff.py | sed -n '1,400p'
- `00:25:33` ACTION: grep -nR -e "class FITSDiff" -e "def FITSDiff" -e "FITSDiff(" . || true
- `00:25:25` RESULT: grep: testbed: No such file or directory
- `00:25:24` ACTION: grep -nR "class FITSDiff\\|def FITSDiff\\|FITSDiff(" -n testbed || true
- `00:25:15` TASK STARTED: `io.fits.FITSDiff` may sometimes report differences between identical files
