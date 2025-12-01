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
- [ ] 1. Reproduce the bug using the provided example: subclass SkyCoord and access a property that raises AttributeError (accessing random_attr)
- [ ] 2. Locate __getattr__ in testbed/astropy/coordinates/sky_coordinate.py and any related attribute access code (__getattribute__ or metaclass behavior)
- [ ] 3. Root cause analysis: inspect __getattr__ implementation to determine if it masks AttributeError raised inside property getters/descriptors
- [ ] 4. Implement fix: adjust __getattr__ to detect class descriptors/properties and let their AttributeError propagate; only raise
- [ ] 5. Verify fix: run the repro script to ensure AttributeError message refers to missing inner attribute (random_attr) and run relevant tests

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:42] **swebench-astropy__astropy-14096**: Task completed: Submitted
## Interaction Log

- `19:42:51` ACTION: Submitting solution
- `19:42:48` patched __getattr__: replaced final raise with class-dict check returning object.__getattribute__; repro shows AttributeError: 'custom_coord' object h...
- `19:42:34` ACTION: python3 - <<'PY'
- `19:42:00` ACTION: nl -ba astropy/utils/shapes.py | sed -n '1,260p'
- `19:41:43` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '1,220p'
- `19:41:33` ACTION: PYTHONPATH=. python3 - <<'PY'
- `19:41:02` ACTION: Reading file: inspect_repro.py
- `19:40:42` ACTION: grep -nR "def __getattribute__" astropy || true
- `19:40:34` ACTION: Reading file: repro.py
- `19:40:28` RESULT: bash: line 17: PY: command not found
- `19:40:28` ACTION: Reading file: repro.py
- `19:40:12` ACTION: nl -ba astropy/coordinates/sky_coordinate.py | sed -n '840,960p'
- `19:40:07` ACTION: grep -nR "__getattr__" . || true
- `19:40:04` RESULT: grep: testbed: No such file or directory
- `19:40:04` ACTION: grep -nR "__getattr__" testbed || true
- `19:39:46` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
