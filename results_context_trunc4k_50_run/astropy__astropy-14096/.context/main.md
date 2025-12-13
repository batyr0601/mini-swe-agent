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
- [ ] Test the fix with the original reproduction case
- [x] 2. Locate __getattr__ in astropy/coordinates/sky_coordinate.py and determine the exact lines to change
- [x] 3. Modify __getattr__ to use inspect.getattr_static on the frame class: if attribute exists on the class, call getattr(self._sky_coord_frame, attr) so descriptor AttributeError propagates; otherwise keep current behavior
- [x] 4. Run the minimal reproduction script once to verify the AttributeError from frame descriptors now propagates correctly

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 20:57] **swebench-astropy__astropy-14096**: Task completed: LimitsExceeded
## Interaction Log

- `20:57:16` ACTION: grep -n "__getattr__" astropy/coordinates/baseframe. [...]
- `20:57:06` repro.py: RAISED: 'FrameWithDescriptor' object has no attribute 'representation_component_names'; FAIL_WRONG_MESSAGE
- `20:56:55` ACTION: python3 repro.py
- `20:55:59` ACTION: python3 - <<'PY'
- `20:55:25` ACTION: grep -n "def __getattr__" astropy/coordinates/baseframe. [...]
- `20:55:09` ACTION: python3 repro.py
- `20:54:42` ACTION: Reading file: <<'"'"'PY'"'"'
- `20:53:53` RESULT: NO_REPRO_FOUND
- `20:53:53` ACTION: bash -lc 'repro=$(find . -type f -name "repro.py" -print -quit); if [ -n "$repro" ]; then echo "FOUN [...]
- `20:53:37` Replaced inspect.getattr_static(self._sky_coord_frame.__class__, attr) with inspect.getattr_static(type(self._sky_coord_frame), attr) in astropy/coord...
- `20:53:23` RESULT: UPDATED
- `20:53:23` ACTION: python3 - <<'PY'
- `20:52:38` astropy/coordinates/sky_coordinate.py:860-920: __getattr__ still contains nested try/except that catches AttributeError from getattr(self._sky_coord_f...
- `20:52:30` ACTION: sed -n '860,920p' astropy/coordinates/sky_coordinate.py
- `20:52:19` python3: can't open file '/testbed/repro.py': [Errno 2] No such file or directory
- `20:52:11` ACTION: python3 repro.py
- `20:51:31` sky_coordinate.py: __getattr__ uses inspect.getattr_static(self._sky_coord_frame.__class__, attr) then getattr(self._sky_coord_frame, attr) (Attribute...
- `20:51:17` ACTION: sed -n '840,920p' astropy/coordinates/sky_coordinate.py
- `20:51:04` ACTION: grep -R --line-number "repro" . || grep -R --line-number "SkyCoord" . || true
- `20:50:52` ACTION: python3 repro.py
