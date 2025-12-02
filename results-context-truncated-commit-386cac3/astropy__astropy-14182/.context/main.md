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
- [ ] 1. Reproduce: run example that writes QTable with header_rows to ascii.rst to reproduce TypeError
- [ ] 2. Locate: find the RST writer class definition (search for
- [ ] 3. Analyze: inspect RST.__init__ signature and handling of writer kwargs to see why
- [ ] 4. Implement fix: modify RST.__init__ to accept header_rows and handle it similarly to fixed_width writer (preserve behavior for no header_rows)
- [ ] 5. Verify: run the reproduction script and run tests for ascii writers if available

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:31] **swebench-astropy__astropy-14182**: Task completed: Submitted
## Interaction Log

- `19:31:27` ACTION: Submitting solution
- `19:31:20` RESULT: [main 95b3db2f3] ascii.rst: accept header_rows and forward to FixedWidth
 1 file changed, 2 insertions(+), 2 deletions(-)
astropy/io/ascii/rst...
- `19:31:20` ACTION: git add astropy/io/ascii/rst.py && git commit -m "ascii. [...]
- `19:31:17` RESULT: (20 lines of output) First: === ascii.rst without header_rows ===...
- `19:31:17` TESTED: reproduction succeeded for ascii.rst with and without header_rows
- `19:31:14` ACTION: printf '%s\n' "from astropy.table import QTable" "import astropy. [...]
- `19:30:49` RESULT: bash: -c: line 11: syntax error near unexpected token `&&'
bash: -c: line 11: `&& python /tmp/test_rst.py'
- `19:30:49` ACTION: Reading file: /tmp/test_rst.py
- `19:30:36` Implemented fix: RST.__init__ now accepts header_rows and forwards to FixedWidth
- `19:30:19` RESULT: ERROR: ✓ Completed TODO #2: Find the function causing the error (look in X module)
- `19:30:18` Decision: add header_rows parameter to RST.__init__ and forward to FixedWidth via super().__init__
- `19:30:18` Root cause: RST.__init__ did not accept header_rows while FixedWidth.__init__ does; unexpected kw causes TypeError
- `19:30:18` Found RST.__init__ at astropy/io/ascii/rst.py:60 - missing header_rows parameter
- `19:30:17` ACTION: sed -i "s/def __init__(self):/def __init__(self, header_rows=None):/" astropy/io/ascii/rst. [...]
- `19:29:53` RESULT: (251 lines of output) First: 240	                ends = [x + 1 for x in self.co...
- `19:29:52` ACTION: nl -ba astropy/io/ascii/fixedwidth.py | sed -n '240,520p'
- `19:29:50` RESULT: (240 lines of output) First: 1	# Licensed under a 3-clause BSD style license - ...
