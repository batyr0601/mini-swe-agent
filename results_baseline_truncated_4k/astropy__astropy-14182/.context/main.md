# Project Goals

**Current Task:** Please support header rows in RestructuredText output

<details>
<summary>Full description</summary>

Please support header rows in RestructuredText output
### Description

It would be great if the following would work:

```Python
>>> from astropy.table import QTable
>>> import astropy.units as u
>>> import sys
>>> tbl = QTable({'wave': [350,950]*u.nm, 'response': [0.7, 1.2]*u.count})
>>> tbl.write(sys.stdout,  format="ascii.rst")
===== ========
 wave response
===== ========
350.0      0.7
950.0      1.2
===== ========
>>> tbl.write(sys.stdout,  format="ascii.fixed_width", header_rows=["name", "unit"])
|  wave | response |
|    nm |       ct |
| 350.0 |      0.7 |
| 950.0 |      1.2 |
>>> tbl.write(sys.stdout,  format="ascii.rst", header_rows=["name", "unit"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3/dist-pack...
</details>


## TODO List

- [ ] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: run a small script writing QTable with format=
- [ ] 2. Locate the code: find the RST writer class (__init__) in the ascii writers (search for class RST or ascii.rst files)
- [ ] 3. Root cause analysis: inspect RST.__init__ signature and writer selection to see why header_rows isn
- [ ] 4. Implement fix: update RST writer __init__ to accept header_rows kwarg, store it, and ensure write_rows uses it; mimic fixed_width writer behavior
- [ ] 5. Verify fix: run the repro script and relevant tests to ensure header_rows works and no regressions
- [ ] 1. Reproduce the bug: run a small script calling identify_format(
- [ ] 2. Locate the code: search for is_fits and identify_format implementations in the testbed/io registry to find where args[0] is accessed
- [ ] 3. Root cause analysis: inspect function signatures and identify when args is empty and why args[0] is accessed without guard
- [ ] 4. Implement fix: modify is_fits to guard access to args[0] (check len(args) > 0 or use fileobj) and ensure filepath string handling is robust
- [ ] 5. Verify fix: run the reproduction script and run relevant tests, log results, and mark todos complete
- [ ] 1. Understand the bug: Reproduce IndexError when is_fits accesses args[0] with empty args
- [ ] 2. Locate the code: astropy/io/fits/connect.py is_fits function and its callers
- [ ] 3. Root cause analysis: Inspect control flow in is_fits to identify missing guard for empty args and check other branches (fileobj/filepath)
- [ ] 4. Implement fix: Modify is_fits to check if args is non-empty before accessing args[0] (e.g., use
- [ ] 5. Verify fix: Run a small repro script calling is_fits with no extra args and with an HDUList, and run relevant unit tests or targeted tests for astropy.io.fits

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:03:57` ACTION: sed -n '1,520p' astropy/io/ascii/fixedwidth.py
- `01:03:51` astropy/io/ascii/rst.py: RST class found; header_class=SimpleRSTHeader, data_class=SimpleRSTData; RST.__init__ has no parameters and calls super().__i...
- `01:03:46` ACTION: sed -n '1,220p' astropy/io/fits/connect.py
- `01:03:42` ACTION: sed -n '1,240p' astropy/io/ascii/rst.py
- `01:03:41` ACTION: grep -nR -e "is_fits" -e "identify_format" .
- `01:03:37` ACTION: grep -nR -e "class RST" -e "ascii.rst" -e "header_rows" . || true
- `01:03:18` TASK STARTED: IndexError: tuple index out of range in identify_format (io.registry)
