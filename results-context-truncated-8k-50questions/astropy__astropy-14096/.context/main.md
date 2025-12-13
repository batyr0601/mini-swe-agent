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

- [2025-12-03 02:58] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `02:58:39` ACTION: Submitting solution
- `02:58:36` repro_skycoord_attr.py: after patch, sc.foo raises AttributeError \"'SkyCoord' object has no attribute 'foo'\" at astropy/coordinates/sky_coordinate.p...
- `02:57:51` PATCH introduced IndentationError in astropy/coordinates/sky_coordinate.py at line 904 when importing; need to inspect lines 860-920
- `02:56:51` ACTION: python3 - <<'PY'
- `02:56:23` ACTION: ln=$(grep -n "def frame(" astropy/coordinates/sky_coordinate. [...]
- `02:56:04` ACTION: grep -nE "def (_is_name|__getattr__)" astropy/coordinates/sky_coordinate. [...]
- `02:55:57` repro_skycoord_attr.py: AttributeError \"'BadFrame' object has no attribute 'name'\" raised at astropy/coordinates/sky_coordinate.py line 865 (_is_nam...
- `02:55:28` ACTION: Reading file: <<'PY'
- `02:54:48` ACTION: grep -nR "SkyCoord" -n astropy | sed -n '1,200p'
- `02:54:24` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '840,980p'
- `02:54:14` ACTION: grep -nR "__getattr__" astropy | sed -n '1,200p'
- `02:54:03` ACTION: ls -la
- `02:54:01` RESULT: ls: cannot access 'testbed': No such file or directory
- `02:53:57` ACTION: ls -la testbed
- `02:53:50` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
