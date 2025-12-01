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
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce: create a small script that constructs an UnrecognizedUnit via u.Unit(
- [ ] 2. Locate: search the codebase for the Unit class and its __eq__ implementation (search for
- [ ] 3. Analyze: inspect Unit.__eq__ to see why Unit(other) is called on None and causes TypeError; determine best place to handle None
- [ ] 4. Implement fix: update Unit.__eq__ to explicitly return False when other is None (or otherwise avoid calling Unit(None)) and add a small regression test script
- [ ] 5. Verify: run the reproduction script and run tests to ensure no regressions
- [ ] 1. Understand the bug: InheritDocstrings metaclass does not inherit docstrings for properties because inspect.isfunction returns False for properties
- [ ] 2. Locate the code: find InheritDocstrings metaclass definition in repository under testbed
- [ ] 3. Root cause analysis: inspect.isfunction is used to detect functions; properties and other descriptors are not functions so they are skipped
- [ ] 4. Implement fix: update detection logic to include property (and possibly other descriptors with fget) so their docstrings are inherited
- [ ] 5. Verify fix: create reproduction script and run tests to confirm property docstrings are inherited

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:44] **swebench-astropy__astropy-7166**: Task completed: Submitted
- [2025-12-01 20:42] **swebench-astropy__astropy-7166**: Task completed: Submitted
## Interaction Log

- `20:44:32` ACTION: Submitting solution
- `20:44:28` VERIFIED: reproduction test passed; InheritDocstrings now inherits docstrings for method/property/classmethod/staticmethod
- `20:44:21` RESULT: patched property doc_target method: subdoc='method doc' basedoc='method doc' property: subdoc='property doc' basedoc='property doc' classmetho...
- `20:44:20` ACTION: python - <<'PY'
- `20:43:55` RESULT: method: subdoc='method doc' basedoc='method doc' property: subdoc=None basedoc='property doc' FAIL: property docstring not inherited classmeth...
- `20:43:54` ACTION: python - <<'PY'
- `20:43:40` RESULT: patched
bash: -c: line 45: syntax error near unexpected token `&&'
bash: -c: line 45: `&& python - <<'PY''
- `20:43:40` ACTION: python - <<'PY'
- `20:43:15` RESULT: ERROR: return codecs.ascii_decode(input, self.errors)[0]
- `20:43:14` ACTION: python - <<'PY'
- `20:42:35` ACTION: Submitting solution
- `20:42:30` TESTED: x==None returns False
- `20:42:28` Decision: Wrap Unit(other) in try/except and return False on ValueError/UnitsError/TypeError
- `20:42:26` RESULT: Base.__dict__['cm']: <class 'classmethod'> <classmethod object at 0x7fffff333c88> doc: classmethod(function) -> method Convert a function to b...
- `20:42:25` ACTION: python - <<'PY'
- `20:42:10` RESULT: method: subdoc='method doc' basedoc='method doc' property: subdoc='property doc' basedoc='property doc' classmethod: subdoc=None basedoc='clas...
- `20:42:09` ACTION: python - <<'PY'
- `20:42:07` Attempting patch of UnrecognizedUnit.__eq__ with UTF-8 read/write
