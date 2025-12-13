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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:24] **swebench-astropy__astropy-14182**: Task completed: Submitted
## Interaction Log

- `23:24:48` ACTION: Submitting solution
- `23:24:46` Verified writing QTable with format=rst and header_rows=['name','unit'] produced reStructuredText output
- `23:24:46` Patched astropy/io/ascii/rst.py: RST.__init__ now accepts header_rows and forwards to FixedWidth
- `23:24:13` ACTION: python3 - <<'PY'
- `23:24:09` RESULT: patched
- `23:24:09` ACTION: python3 - <<'PY'
- `23:23:46` ACTION: grep -n "class FixedWidth" -n astropy/io/ascii/fixedwidth.py && nl -ba astropy/io/ascii/fixedwidth. [...]
- `23:23:41` ACTION: nl -ba astropy/io/ascii/fixedwidth.py | sed -n '1,260p'
- `23:23:37` ACTION: nl -ba astropy/io/ascii/rst.py | sed -n '1,240p'
- `23:23:33` ACTION: (grep -Rin "class RST" . || true) && (grep -Rin "ascii.rst" . || true) && (grep -Rin "header_rows" . [...]
- `23:23:24` RESULT: ls: cannot access 'testbed': No such file or directory
- `23:23:23` ACTION: ls -la testbed && grep -Rin "rst" testbed || true
- `23:23:09` TASK STARTED: Please support header rows in RestructuredText output
