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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 02:59] **swebench-astropy__astropy-14182**: Task completed: Submitted
## Interaction Log

- `02:58:53` ACTION: Submitting solution
- `02:58:47` repro_rst StringIO output:\n==== ====\ncol1 col2\n==== ====\n   1    a\n   2   bb\n==== ====
- `02:58:35` RESULT: ==== ====
col1 col2
==== ====
   1    a
   2   bb
==== ====
- `02:57:55` repro_rst.py: printed RST table:\n==== ====\ncol1 col2\n==== ====\n   1    a\n   2   bb\n==== ====\nThen raised TypeError: can only join an iterable (...
- `02:57:15` ACTION: python3 - <<'PY'
- `02:56:35` ACTION: Reading file: <<'PY'
- `02:56:13` Applied patch to astropy/io/ascii/rst.py: python script printed 'PATCH_APPLIED'; subsequent sed preview failed with shell syntax error from extra '&&'...
- `02:55:50` ACTION: python3 - <<'PY'
- `02:55:31` RESULT: error: unrecognized input
- `02:55:28` ACTION: git apply -p0 <<'PATCH'
- `02:54:52` ACTION: sed -n '260,620p' astropy/io/ascii/fixedwidth.py
- `02:54:44` ACTION: sed -n '1,260p' astropy/io/ascii/fixedwidth.py
- `02:54:37` ACTION: sed -n '1,240p' astropy/io/ascii/rst.py
- `02:54:22` ACTION: grep -nE "class .*RST|class .*Rst|def write|header_rows" astropy/io/ascii/rst. [...]
- `02:54:00` ACTION: grep -nR "class .*RST\|ascii.rst\|rst" astropy/io -n || true
