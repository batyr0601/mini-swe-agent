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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:26] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `00:26:51` ACTION: Submitting solution
- `00:26:46` Verified repro_prop.py: AttributeError correctly reports missing 'random_attr' (property 'prop' delegates to descriptor)
- `00:26:39` Root cause: SkyCoord.__getattr__ intercepted attributes that are defined on the class (e.g. @property), replacing descriptor-raised AttributeError wit...
- `00:26:32` Found causing function: __getattr__ in astropy/coordinates/sky_coordinate.py (lines ~869-900)
- `00:26:07` repro_prop.py: AttributeError: 'custom_coord' object has no attribute 'random_attr' (property 'prop' attempted to access missing attribute) observed
- `00:25:55` ACTION: python3 repro_prop.py
- `00:25:45` RESULT: replaced sys.exc_info() patch with class-attribute check
- `00:25:44` ACTION: python3 - <<'PY'
- `00:24:58` ACTION: Reading file: repro_prop.py
- `00:24:33` patched __getattr__: astropy/coordinates/sky_coordinate.py updated to re-raise existing AttributeError (preserves original attribute name in errors)
- `00:24:24` RESULT: patched __getattr__ to re-raise existing AttributeError
- `00:24:23` ACTION: python3 - <<'PY'
- `00:23:39` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '840,960p'
- `00:23:32` ACTION: grep -RIn "__getattr__\|class SkyCoord" . || true
- `00:23:27` RESULT: ls: cannot access 'testbed': No such file or directory
- `00:23:27` ACTION: ls -la testbed
- `00:23:19` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
