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

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:29] **swebench-astropy__astropy-7606**: Task completed: Submitted
## Interaction Log

- `23:29:09` ACTION: Submitting solution
- `23:29:04` Repro: UnrecognizedUnit('asdf', parse_strict='silent') == None -> False
- `23:29:03` RESULT: COMPARE_RESULT: False
- `23:29:01` ACTION: python3 - <<'PY'
- `23:28:51` Patched astropy/units/core.py: added guard in UnrecognizedUnit.__eq__ to return False if other is None
- `23:28:35` RESULT: Patched astropy/units/core.py
- `23:28:25` ACTION: python3 - <<'PY'
- `23:28:08` ACTION: nl -ba astropy/units/core.py | sed -n '1688,1718p'
- `23:28:00` ACTION: nl -ba astropy/units/core.py | sed -n '1680,1735p'
- `23:27:45` ACTION: grep -n "def __eq__" astropy/units -R
- `23:27:36` ACTION: ls -la
- `23:27:33` TASK STARTED: Unit equality comparison with None raises TypeError for UnrecognizedUnit
