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
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:06] **swebench-astropy__astropy-7606**: Task completed: Submitted
## Interaction Log

- `03:06:21` ACTION: Submitting solution
- `03:06:14` Verified: UnrecognizedUnit('not_a_real_unit') == None -> False (no exception raised)
- `03:06:14` Patched __eq__: inserted 'if other is None: return False' before Unit(...) conversion
- `03:06:14` Located UnrecognizedUnit.__eq__ at lines 1712-1717 in astropy/units/core.py; it previously converted other = Unit(other, parse_strict='silent')
- `03:05:43` ACTION: python3 - <<'PY'
- `03:05:13` ACTION: nl -ba astropy/units/core.py | sed -n '1708,1718p'
- `03:04:45` ACTION: git checkout -- astropy/units/core.py && python3 -m py_compile astropy/units/core. [...]
- `03:03:41` ACTION: git checkout -- astropy/units/core.py && python3 - <<'PY'
- `03:03:17` ACTION: sed -n '700,740p' astropy/units/core.py && sed -n '1688,1736p' astropy/units/core. [...]
- `03:02:29` ACTION: python3 - <<'PY'
- `03:01:55` ACTION: awk 'BEGIN{inclass=0}
- `03:01:01` Reproduced: UnrecognizedUnit('not_a_real_unit') == None raises TypeError 'None is not a valid Unit
- `03:00:45` ACTION: python3 - <<'PY'
- `03:00:20` ACTION: nl -ba astropy/units/core.py | sed -n '700,760p' && nl -ba astropy/units/core. [...]
- `03:00:13` ACTION: nl -ba astropy/units/core.py | sed -n '1,260p'
- `03:00:05` ACTION: grep -RIn "UnrecognizedUnit\|None is not a valid Unit\|class Unit\|def __eq__" astropy || true
- `02:59:58` ACTION: ls -la && grep -RIn "UnrecognizedUnit\|class Unit\|def __eq__\|None is not a valid Unit" -n testbed  [...]
- `02:59:51` TASK STARTED: Unit equality comparison with None raises TypeError for UnrecognizedUnit
