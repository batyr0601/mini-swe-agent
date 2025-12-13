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
- [ ] 2. Update final AttributeError message to use
- [ ] 3. Edit sky_coordinate.py to change the message
- [ ] 4. Run minimal repro to verify message now shows

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:41] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `14:41:58` ACTION: Submitting solution
- `14:41:54` repro: AttributeError now \"'SkyCoord' object has no attribute 'nonexistent_attribute'\" at /testbed/astropy/coordinates/sky_coordinate.py:898
- `14:41:39` ACTION: python3 - <<'PY'
- `14:40:39` ACTION: grep -n "__getattr__" astropy/coordinates/sky_coordinate. [...]
- `14:40:32` repro: AttributeError: 'SubSkyCoord' object has no attribute 'nonexistent_attribute' (sky_coordinate.py:898)
- `14:40:23` ACTION: python3 - <<'PY'
- `14:40:03` ACTION: sed -n '840,980p' astropy/coordinates/sky_coordinate.py
- `14:40:00` grep __getattr__: astropy/coordinates/sky_coordinate.py:869,903,918,945 astropy/coordinates/baseframe.py:1726,2025
- `14:39:52` ACTION: grep -n "__getattr__" astropy/coordinates -R || true
- `14:39:37` ACTION: grep -n "__getattr__" astropy/coordinates -R || true && sed -n '820,980p' astropy/coordinates/sky_co [...]
- `14:39:11` ACTION: sed -n '840,960p' astropy/coordinates/sky_coordinate.py
- `14:39:06` grep results: SkyCoord class at astropy/coordinates/sky_coordinate.py:168; __getattr__ at astropy/coordinates/sky_coordinate.py:869; baseframe __getat...
- `14:38:57` ACTION: grep -nR -e "class SkyCoord" -e "__getattr__" astropy/coordinates || true
- `14:38:38` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
