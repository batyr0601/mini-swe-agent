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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: RST writer raises TypeError when passed header_rows; reproduce and inspect error message
- [ ] 2. Locate the code: find the RST writer class (search for class RST or filename rst.py) in the project under testbed
- [ ] 3. Root cause analysis: inspect RST.__init__ signature and how writer kwargs are handled; find where header_rows should be used
- [ ] 4. Implement fix: update RST writer to accept header_rows in __init__ and use it when generating output (ensure compatibility with other writers)
- [ ] 5. Verify fix: create minimal repro script that writes a QTable with header_rows to ascii.rst and confirm no TypeError and correct output

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:40] **swebench-astropy__astropy-14182**: Task completed: Submitted
## Interaction Log

- `20:40:31` ACTION: Submitting solution
- `20:40:26` rst.py patched: RST.__init__ now accepts header_rows and passes to FixedWidth; repro writing QTable with header_rows=['name','unit'] produced lines in...
- `20:40:13` ACTION: python3 - <<'PY'
- `20:40:10` RESULT: rst.py patched
- `20:40:10` ACTION: python3 - <<'PY'
- `20:39:53` ACTION: nl -ba astropy/io/ascii/fixedwidth.py | sed -n '300,420p'
- `20:39:50` ACTION: nl -ba astropy/io/ascii/fixedwidth.py | grep -n "class FixedWidth" -n -n -n -n -n -n -n -n -n -n -n  [...]
- `20:39:46` ACTION: nl -ba astropy/io/ascii/fixedwidth.py | sed -n '1,260p'
- `20:39:43` ACTION: nl -ba astropy/io/ascii/rst.py | sed -n '1,240p'
- `20:39:38` ACTION: grep -R -n --line-number -e "class RST" -e "ascii.rst" -e "rst" astropy/io/ascii || true
- `20:39:35` ACTION: ls -la
- `20:39:31` RESULT: grep: testbed: No such file or directory
- `20:39:31` ACTION: grep -R -n --line-number -e "class RST" -e "ascii.rst" -e "rst" testbed || true
- `20:39:18` TASK STARTED: Please support header rows in RestructuredText output
