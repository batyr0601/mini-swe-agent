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

- [2025-12-02 23:27] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `23:27:31` ACTION: Submitting solution
- `23:27:25` Before fix: c.prop raised AttributeError for 'prop'. Change: in SkyCoord.__getattr__ added check for attr in class MRO and delegate to object.__getatt...
- `23:27:09` ACTION: awk 'NR==874{print " # If attribute is defined on the class (e.g. [...]
- `23:25:54` ACTION: grep -n "def __getattribute__" astropy/coordinates/sky_coordinate.py || true
- `23:25:17` ACTION: nl -ba astropy/coordinates/baseframe.py | sed -n '1680,1780p'
- `23:25:06` ACTION: python3 - <<'PY'
- `23:24:40` ACTION: nl -ba astropy/utils/shapes.py | sed -n '1,240p'
- `23:24:37` ACTION: grep -n "class ShapedLikeNDArray" -R astropy | sed -n '1,200p'
- `23:24:32` ACTION: python3 - <<'PY'
- `23:24:08` ACTION: grep -n "__getattribute__" -R astropy || true
- `23:23:59` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '1,220p'
- `23:23:52` ACTION: grep -n "__getattribute__" -R astropy/coordinates || true
- `23:23:43` ACTION: Reading file: repro_prop.py
- `23:23:27` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '840,920p'
- `23:23:21` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `23:23:17` ACTION: ls -la
- `23:23:09` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
