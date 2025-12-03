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

- [2025-12-03 03:17] **swebench-astropy__astropy-14539**: Task completed: Submitted
## Interaction Log

- `03:17:44` ACTION: Submitting solution
- `03:17:39` Ran TestDiff::test_different_table_field_names and ::test_different_table_field_counts: 2 passed in 0.18s; patched astropy/io/fits/diff.py to initiali...
- `03:17:10` ACTION: pytest -q astropy/io/fits/tests/test_diff.py::TestDiff::test_different_table_field_names astropy/io/ [...]
- `03:16:57` ACTION: sed -n '1,200p' astropy/io/fits/tests/test_diff.py
- `03:16:46` pytest failed to run the two targeted tests: 'no tests ran'; RuntimeWarning: numpy.ndarray size changed, may indicate binary incompatibility; errors: ...
- `03:16:06` ACTION: pytest -q astropy/io/fits/tests/test_diff.py::test_different_table_field_names astropy/io/fits/tests [...]
- `03:15:42` ACTION: python3 - <<'PY'
- `03:14:54` context_summary: Pending TODOs 1-3; diff_column_names initialized to () at astropy/io/fits/diff.py:1336; reassigned to ([], []) at astropy/io/fits/dif...
- `03:14:20` ACTION: grep -n "\.append(" astropy/io/fits/diff.py
- `03:14:11` ACTION: sed -n '430,520p' astropy/io/fits/tests/test_diff.py
- `03:13:40` ACTION: grep -nR "diff_column_names" -n .
- `03:13:09` ACTION: sed -n '1488,1512p' astropy/io/fits/diff.py
- `03:12:54` ACTION: grep -n "diff_column_names" astropy/io/fits/diff.py
- `03:12:39` ACTION: sed -n '1360,1410p' astropy/io/fits/diff.py
- `03:12:28` ACTION: sed -n '1280,1360p' astropy/io/fits/diff.py
- `03:12:19` ACTION: grep -n "diff_keyword_values\|diff_keyword_comments" astropy/io/fits/diff. [...]
- `03:12:13` ACTION: sed -n '820,930p' astropy/io/fits/diff.py
- `03:11:52` ACTION: grep -n "diff_hdus" astropy/io/fits/diff.py && sed -n '340,392p' astropy/io/fits/diff.py
- `03:11:38` RESULT: grep: tests: No such file or directory
- `03:11:37` ACTION: grep -nR "TableDataDiff" -n tests || true
