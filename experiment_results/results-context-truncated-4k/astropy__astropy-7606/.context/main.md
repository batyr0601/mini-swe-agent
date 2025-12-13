# Project Goals

**Current Task:** Unit equality comparison with None raises TypeError for UnrecognizedUnit

<details>
<summary>Full description</summary>

Unit equality comparison with None raises TypeError for UnrecognizedUnit
```
In [12]: x = u.Unit('asdf', parse_strict='silent')

In [13]: x == None  # Should be False
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-13-2486f2ccf928> in <module>()
----> 1 x == None  # Should be False

/Users/aldcroft/anaconda3/lib/python3.5/site-packages/astropy/units/core.py in __eq__(self, other)
   1699 
   1700     def __eq__(self, other):
-> 1701         other = Unit(other, parse_strict='silent')
   1702         return isinstance(other, UnrecognizedUnit) and self.name == other.name
   1703 

/Users/aldcroft/anaconda3/lib/python3.5/site-packages/astropy/units/core.py in _...
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

- [2025-12-02 20:53] **swebench-astropy__astropy-7606**: Task completed: Submitted
## Interaction Log

- `20:53:07` ACTION: Submitting solution
- `20:52:47` UnrecognizedUnit('foo') == None returned False; no exception; comparison fixed
- `20:52:34` RESULT: False
- `20:52:33` ACTION: python3 - <<'PY'
- `20:52:21` patched UnrecognizedUnit.__eq__: replaced Unit(other, parse_strict='silent') with try/except catching TypeError, ValueError; write succeeded (printed ...
- `20:52:13` RESULT: patched
- `20:52:13` ACTION: python3 - <<'PY'
- `20:51:41` ACTION: sed -n '1704,1724p' astropy/units/core.py
- `20:51:36` RESULT: 724:    def __eq__(self, other):
1712:    def __eq__(self, other):
- `20:51:35` ACTION: grep -n "def __eq__" astropy/units/core.py
- `20:51:29` ACTION: grep -n "class UnrecognizedUnit" astropy/units/core.py && sed -n '1660,1710p' astropy/units/core.py
- `20:51:22` Failed to read astropy/units/core.py with pathlib.read_text: UnicodeDecodeError: 'ascii' codec can't decode byte 0xce in position 73708; patch attempt...
- `20:51:12` ACTION: python3 - <<'PY'
- `20:50:48` Found: UnrecognizedUnit.__eq__ (core.py:1713) calls Unit(other) without guarding None; Unit(None) raises TypeError 'None is not a valid Unit' at core....
- `20:50:36` ACTION: grep -n "class UnrecognizedUnit" astropy/units/core.py && sed -n '1688,1736p' astropy/units/core. [...]
- `20:50:28` repro: created UnrecognizedUnit(foo); comparing to None raised TypeError 'None is not a valid Unit' (Traceback: __eq__ at /testbed/astropy/units/core....
- `20:50:19` ACTION: python3 - <<'PY'
- `20:50:01` ACTION: sed -n '740,820p' astropy/units/core.py && sed -n '1656,1728p' astropy/units/core.py
- `20:49:53` ACTION: grep -nR "UnrecognizedUnit" . || true
