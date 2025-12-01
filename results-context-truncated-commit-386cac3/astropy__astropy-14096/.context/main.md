# Project Goals

**Current Task:** Subclassed SkyCoord gives misleading attribute access message

<details>
<summary>Full description</summary>

Subclassed SkyCoord gives misleading attribute access message
I'm trying to subclass `SkyCoord`, and add some custom properties. This all seems to be working fine, but when I have a custom property (`prop` below) that tries to access a non-existent attribute (`random_attr`) below, the error message is misleading because it says `prop` doesn't exist, where it should say `random_attr` doesn't exist.

```python
import astropy.coordinates as coord


class custom_coord(coord.SkyCoord):
    @property
    def prop(self):
        return self.random_attr


c = custom_coord('00h42m30s', '+41d12m00s', frame='icrs')
c.prop
```

raises
```
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    c.prop
  File "/Users/dstansby/miniconda3/lib/python3.7/site-packa...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce: create a minimal subclass of SkyCoord that defines a property which accesses a non-existent attribute, and run it to reproduce the misleading AttributeError message
- [ ] 2. Locate: find the __getattr__ method in sky_coordinate.py (or equivalent file) that handles attribute access for SkyCoord
- [ ] 3. Analyze: inspect __getattr__ to see where AttributeError is caught and re-raised with the wrong attribute name; determine how to preserve the original missing attribute name and traceback
- [ ] 4. Implement fix: modify __getattr__ to only translate AttributeError when the missing attribute actually pertains to SkyCoord internals; otherwise re-raise the original AttributeError (or include the original attribute name) so properties raise accurate messages
- [ ] 5. Verify: run the reproduction script and existing tests to ensure the AttributeError message now correctly indicates the real missing attribute and that no other behaviors regress

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:31] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `19:31:34` ACTION: Submitting solution
- `19:31:25` RESULT: (161 lines of output) First: <frozen importlib._bootstrap>:228: RuntimeWarning:...
- `19:31:00` ACTION: pytest -q astropy/coordinates -q
- `19:30:58` TESTED: reproduction script run; after patch AttributeError now reports 'random_attr' as missing
- `19:30:58` Decision: detect descriptors in the MRO (has __get__) and call object.__getattribute__(self, attr) to let the descriptor run and propagate its own Att...
- `19:30:58` Analysis: __getattr__ should allow descriptors (e.g., properties) defined on the class to execute so AttributeError raised inside them shows the actua...
- `19:30:58` Found __getattr__ at astropy/coordinates/sky_coordinate.py:869 - it raises AttributeError for attr without allowing class descriptors to run
- `19:30:58` Reproduced: initially c.prop raised AttributeError mentioning 'prop' instead of the internal 'random_attr
- `19:30:43` RESULT: ERROR: raise AttributeError(
- `19:30:42` ACTION: python3 - <<'PY'
- `19:29:59` RESULT: ERROR: raise AttributeError(
- `19:29:57` ACTION: python3 - <<'PY'
- `19:29:45` RESULT: (141 lines of output) First: 840	            pm_ra=u.Quantity(starpm[2], u.radi...
- `19:29:45` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '840,980p'
- `19:29:42` RESULT: (67 lines of output) First: grep: astropy/timeseries/periodograms/lombscargle/...
- `19:29:42` ACTION: grep -nR "__getattr__" -n astropy | sed -n '1,200p'
- `19:29:38` RESULT: (36 lines of output) First: total 704...
- `19:29:38` ACTION: ls -la
- `19:29:27` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
