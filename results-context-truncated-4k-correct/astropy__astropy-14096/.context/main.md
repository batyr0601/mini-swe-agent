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

- [2025-12-02 11:30] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `11:30:00` ACTION: Submitting solution
- `11:29:55` repro.py: AttributeError 'custom ra failure from Sub.ra' propagated from Sub.ra via sky_coordinate.py:881
- `11:29:09` repro.py: AttributeError 'custom ra failure from Sub.ra' propagated from Sub.ra via sky_coordinate.py:881
- `11:28:52` ACTION: python3 repro.py
- `11:28:40` ACTION: sed -n '820,920p' astropy/coordinates/sky_coordinate.py
- `11:28:33` ACTION: sed -n '1,240p' repro.py && sed -n '1,240p' repro2.py
- `11:28:19` ACTION: sed -n '820,920p' astropy/coordinates/sky_coordinate.py
- `11:28:12` ACTION: sed -n '1,200p' repro.py && sed -n '1,200p' repro2.py
- `11:27:47` ACTION: sed -n '820,920p' astropy/coordinates/sky_coordinate.py
- `11:27:41` repro after patch: RA_ACCESS: NO_EXCEPTION — descriptor still masked; need to inspect astropy/coordinates/sky_coordinate.py __getattr__ (around lines ...
- `11:27:32` RESULT: RA_ACCESS: NO_EXCEPTION
- `11:27:31` ACTION: python3 - <<'PY'
- `11:27:17` ACTION: cp astropy/coordinates/sky_coordinate.py{,.bak} && python3 - <<'PY'
- `11:26:38` ACTION: python3 - <<'PY'
- `11:25:55` ACTION: sed -n '820,920p' astropy/coordinates/sky_coordinate.py
- `11:25:46` ACTION: sed -n '1,200p' repro.py && echo '---' && sed -n '1,200p' repro2.py
- `11:25:28` ACTION: for f in repro*.py; do [ -f "$f" ] && echo "=== $f ===" && python3 "$f"; done || true
- `11:25:02` sky_coordinate.py:__getattr__ (lines 869-920): checks class dict for attr and if a descriptor (has __get__) calls val.__get__(self, cls) so descriptor...
- `11:24:50` ACTION: sed -n '840,920p' astropy/coordinates/sky_coordinate.py
- `11:24:44` grep __getattr__: astropy/coordinates/baseframe.py:1726,2025; astropy/coordinates/sky_coordinate.py:869,912,927,954
