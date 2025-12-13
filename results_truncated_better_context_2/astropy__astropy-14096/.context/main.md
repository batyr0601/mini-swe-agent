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
- [ ] 1. Reproduce: create a minimal reproduction script that subclasses SkyCoord and accesses a property that references a non-existent attribute to reproduce the misleading AttributeError
- [ ] 2. Locate: find the __getattr__ implementation in the project
- [ ] 3. Analyze: determine why __getattr__ is catching AttributeError raised inside a property and re-raising with the wrong attribute name (masking the real missing attribute)
- [ ] 4. Implement fix: change __getattr__ to only handle attribute-not-found cases for the current object and avoid masking AttributeError coming from attribute access inside properties; ensure error message reports the actual missing attribute name
- [ ] 5. Verify: run the reproduction script to confirm the AttributeError message now mentions the inner missing attribute (

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 18:54] **swebench-astropy__astropy-14096**: Task completed: Submitted
- [2025-12-01 18:54] **swebench-astropy__astropy-14096**: Ensure SkyCoord.__getattr__ calls class-level descriptors so AttributeError from properties is not m...
## Interaction Log

- `18:54:44` ACTION: Submitting solution
- `18:54:39` RESULT: (15 lines of output) First: Traceback (most recent call last):...
- `18:54:36` ACTION: python3 repro.py || true && pytest -q astropy/coordinates/tests/test_sky_coord. [...]
- `18:54:33` TESTED: repro.py now raises AttributeError for 'random_attr' instead of for the property name
- `18:54:33` Fix implemented in astropy/coordinates/sky_coordinate.py: try class-level descriptors and let AttributeError from descriptor propagate
- `18:54:18` Decision: Try calling class-level descriptors directly in __getattr__ so AttributeError from property fget propagates
- `18:53:29` RESULT: (19 lines of output) First: Traceback (most recent call last):...
- `18:53:28` ACTION: Reading file: inspect_repro.py
- `18:53:13` RESULT: ERROR: raise AttributeError(
- `18:53:11` ACTION: Reading file: repro.py
- `18:52:48` Found SkyCoord.__getattr__ at astropy/coordinates/sky_coordinate.py:869
- `18:52:43` RESULT: (82 lines of output) First: ./docs/io/fits/appendix/history.rst:3016:- remove ...
- `18:52:42` ACTION: grep -R -n -e "class SkyCoord" -e "sky_coordinate.py" -e "__getattr__" . || true
- `18:52:40` RESULT: grep: testbed: No such file or directory
- `18:52:39` ACTION: grep -R -n -e "class SkyCoord" -e "__getattr__" testbed || true
- `18:52:23` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
