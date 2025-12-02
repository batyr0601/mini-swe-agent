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
- [ ] 1. Reproduce the bug using a minimal repro script in testbed
- [ ] 2. Locate __getattr__ implementation in the codebase (likely sky_coordinate.py or similar under testbed)
- [ ] 3. Analyze __getattr__ to see how it catches AttributeError and composes error messages
- [ ] 4. Implement fix: modify __getattr__ to let AttributeError from properties propagate or preserve the original missing attribute name in messages
- [ ] 5. Verify fix: run the repro script and any relevant tests to ensure correct error message and no regressions

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:43] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `20:43:09` ACTION: Submitting solution
- `20:43:02` repro.py traceback: File \"/testbed/repro.py\", line 10, in <module> c.prop; File \"/testbed/astropy/coordinates/sky_coordinate.py\", line 921, in __g...
- `20:42:48` ACTION: python3 repro.py
- `20:42:42` ACTION: python3 - <<'PY'
- `20:42:12` ACTION: python3 repro.py
- `20:42:06` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '908,920p'
- `20:42:04` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '902,912p'
- `20:42:01` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '888,908p'
- `20:41:53` ACTION: python3 - <<'PY'
- `20:41:01` ACTION: nl -ba astropy/utils/shapes.py | sed -n '1,320p'
- `20:40:53` ACTION: python3 - <<'PY'
- `20:40:42` ACTION: grep -nR "def __getattribute__" astropy || true
- `20:40:32` ACTION: Reading file: repro.py
- `20:40:22` Patched astropy/coordinates/sky_coordinate.py: replaced start of __getattr__ to import sys and re-raise existing AttributeError so property/descriptor...
- `20:40:13` RESULT: PATCHEd
- `20:40:13` ACTION: python3 - <<'PY'
- `20:39:37` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '840,980p'
- `20:39:31` ACTION: grep -nR "__getattr__" . || true
- `20:39:29` RESULT: grep: testbed: No such file or directory
- `20:39:28` ACTION: grep -nR "__getattr__" testbed || true
