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
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:26] **swebench-astropy__astropy-14096**: Task completed: LimitsExceeded
- [2025-12-02 14:15] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `14:26:07` ACTION: grep -n "__getattr__" astropy/coordinates/sky_coordinate. [...]
- `14:25:25` ACTION: sed -n '820,940p' astropy/coordinates/sky_coordinate.py
- `14:25:05` ACTION: grep -n -E "(__getattr__|inspect.getattr_static|getattr\\(type\\(self\\)|getattr\\(type\\(self\\),)" [...]
- `14:24:47` ACTION: python3 - <<'PY'
- `14:24:12` ACTION: grep -n "__getattr__" astropy/coordinates/sky_coordinate. [...]
- `14:23:53` ACTION: grep -R -n -E -e "MySkyCoord" -e "repro_subclass" -e "repro" -e "class .*SkyCoord" . || true
- `14:23:44` RESULT: sed: can't read repro_subclass.py: No such file or directory
- `14:23:43` ACTION: sed -n '1,240p' repro_subclass.py
- `14:23:24` ACTION: sed -n '840,920p' astropy/coordinates/sky_coordinate.py
- `14:23:09` ACTION: grep -R --line-number -e "repro_subclass" -e "MySkyCoord" -e "repro" . || true
- `14:23:02` ACTION: python3 repro_subclass.py
- `14:22:54` ACTION: sed -n '860,920p' astropy/coordinates/sky_coordinate.py
- `14:22:37` ACTION: git diff -- astropy/coordinates/sky_coordinate.py || true
- `14:22:05` ACTION: grep -n "__getattr__" astropy/coordinates/sky_coordinate. [...]
- `14:21:38` ACTION: git diff -- astropy/coordinates/sky_coordinate.py && sed -n '840,920p' astropy/coordinates/sky_coord [...]
- `14:21:22` ACTION: grep -R --line-number -e "repro_subclass" -e "MySkyCoord" -e "repro" . || true
- `14:21:14` ACTION: python3 repro_subclass.py
- `14:21:04` ACTION: git diff -- astropy/coordinates/sky_coordinate.py
- `14:20:50` ACTION: sed -n '920,1200p' astropy/coordinates/sky_coordinate.py
- `14:20:43` ACTION: sed -n '840,920p' astropy/coordinates/sky_coordinate.py
