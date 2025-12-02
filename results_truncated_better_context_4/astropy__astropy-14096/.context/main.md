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
- [ ] 1. Reproduce the bug: create a minimal repro script using a SkyCoord subclass that triggers the misleading AttributeError
- [ ] 2. Locate __getattr__: search for __getattr__ implementations in /testbed to find the relevant file and lines
- [ ] 3. Analyze __getattr__ behaviour: inspect the code to see where AttributeError is caught and re-raised with the wrong attribute name
- [ ] 4. Implement fix: modify __getattr__ to detect descriptors defined on the class (check mro and __dict__) and re-raise the original AttributeError if a descriptor/property exists
- [ ] 5. Verify fix: run the repro script and related tests to ensure the AttributeError mentions the actual missing nested attribute rather than the property name

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:38] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `19:38:23` ACTION: Submitting solution
- `19:37:56` ACTION: pytest -q astropy/coordinates -q || true
- `19:37:54` repro.py: running repro produced AttributeError: 'custom_coord' object has no attribute 'random_attr' (traceback shows descriptor executed via object....
- `19:37:54` sky_coordinate.py:869-900: __getattr__ inspects _sky_coord_frame, checks frame_attributes and aliases, tries transforms, then (previously) uncondition...
- `19:37:54` grep __getattr__: astropy/coordinates/sky_coordinate.py:869
- `19:37:28` ACTION: Reading file: repro.py
- `19:37:20` Patched astropy/coordinates/sky_coordinate.py: inserted MRO-based descriptor check that calls object.__getattribute__(self, attr) so descriptor-raised...
- `19:37:12` RESULT: Patched file
- `19:37:11` ACTION: python3 - <<'PY'
- `19:36:45` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '840,980p'
- `19:36:41` ACTION: grep -RIn "__getattr__" astropy || true
- `19:36:37` ACTION: ls -la
- `19:36:30` RESULT: grep: testbed: No such file or directory
- `19:36:30` ACTION: grep -RIn "__getattr__" testbed || true
- `19:36:09` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
