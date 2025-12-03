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

- [2025-12-02 18:34] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `18:34:47` ACTION: Submitting solution
- `18:34:42` repro.py: AttributeError 'inner foo property error' raised from property foo (traceback: repro.py line 9 -> astropy/coordinates/sky_coordinate.py:884 ...
- `18:34:32` Changed inspect.getattr_static(self, attr) to inspect.getattr_static(type(self), attr) in astropy/coordinates/sky_coordinate.py; __getattr__ now calls...
- `18:34:16` ACTION: perl -0777 -pe 's/inspect\.getattr_static\(\s*self\s*,\s*attr\s*\)/inspect. [...]
- `18:33:41` ACTION: grep -n "getattr_static" astropy/coordinates/sky_coordinate.py && \
- `18:33:06` ACTION: sed -n '840,920p' astropy/coordinates/sky_coordinate.py
- `18:32:42` repro.py: AttributeError 'inner foo property error' raised from property 'foo' (traceback: repro.py line 6) when __getattr__ called desc.__get__(self,...
- `18:32:35` ACTION: python3 repro.py
- `18:32:27` sky_coordinate.py: __getattr__ contains descriptor handling: uses inspect.getattr_static and calls desc.__get__(self, type(self)) before other attribu...
- `18:32:19` ACTION: sed -n '860,940p' astropy/coordinates/sky_coordinate.py
- `18:32:03` ACTION: python3 - <<'PY'
- `18:31:25` ACTION: grep -n "__getattr__" astropy/coordinates/sky_coordinate. [...]
- `18:31:16` repro.py: AttributeError \"'MyCoord' object has no attribute 'foo'\" from astropy/coordinates/sky_coordinate.py:898 (in __getattr__) when accessing c....
- `18:31:05` ACTION: Reading file: <<'PY'
- `18:30:42` ACTION: sed -n '840,980p' astropy/coordinates/sky_coordinate.py
- `18:30:37` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `18:30:26` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
