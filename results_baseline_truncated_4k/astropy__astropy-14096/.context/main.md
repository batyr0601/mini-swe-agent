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

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create a minimal repro script using a custom SkyCoord subclass whose property accesses a non-existent attribute
- [ ] 2. Locate the __getattr__ implementation: grep repository for
- [ ] 3. Root cause analysis: inspect sky_coordinate.__getattr__ to see how it handles AttributeError and whether it masks errors originating inside property descriptors
- [ ] 4. Implement fix: modify __getattr__ to detect class descriptors/properties and let their AttributeError propagate; only raise
- [ ] 5. Verify fix: run the repro script and ensure the AttributeError message names the missing attribute accessed inside the property (e.g.,
- [ ] 1. Inspect SkyCoord __getattr__: open astropy/coordinates/sky_coordinate.py around lines 860-920 to understand current behavior
- [ ] 2. Compare with BaseFrame __getattr__: open astropy/coordinates/baseframe.py at lines ~1720 and ~2025 to compare handling
- [ ] 3. Root cause analysis: search for try/except blocks catching AttributeError in these files and determine if descriptor/property errors are being masked
- [ ] 4. Implement fix: modify sky_coordinate.__getattr__ to check class descriptors/properties first and avoid masking their AttributeError, updating exception handling accordingly
- [ ] 5. Add unit tests: create tests that reproduce AttributeError masking and assert correct exceptions/messages after fix
- [ ] 6. Run targeted tests: run pytest for the coordinates tests and the new tests to verify the fix

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:03:53` grep __getattr__: ./astropy/coordinates/sky_coordinate.py:869; ./astropy/coordinates/baseframe.py:1726,2025; other matches include astropy/cosmology/p...
- `01:03:39` ACTION: grep -nR "__getattr__" .
- `01:03:19` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
