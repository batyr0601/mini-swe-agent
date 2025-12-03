# Project Goals

**Current Task:** Inconsistent behavior of `world_to_pixel` in `SlicedLowLevelWCS` 

<details>
<summary>Full description</summary>

Inconsistent behavior of `world_to_pixel` in `SlicedLowLevelWCS` 
<!-- This comments are hidden when you submit the issue,
so you do not need to remove them! -->

<!-- Please be sure to check out our contributing guidelines,
https://github.com/astropy/astropy/blob/main/CONTRIBUTING.md .
Please be sure to check out our code of conduct,
https://github.com/astropy/astropy/blob/main/CODE_OF_CONDUCT.md . -->

<!-- Please have a search on our GitHub repository to see if a similar
issue has already been posted.
If a similar issue is closed, have a quick look to see if you are satisfied
by the resolution.
If not please go ahead and open an issue! -->

<!-- Please check that the development version still produces the same bug.
You can install development version with
pip install git...
</details>


## TODO List

<!-- 
Add detailed, specific TODOs when starting a task. Good examples:
- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `18:35:48` RESULT: patched
- `18:35:48` ACTION: python3 - <<'PY'
- `18:35:17` ACTION: sed -n '230,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:35:03` ACTION: sed -n '200,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:34:43` ACTION: sed -n '1,220p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:34:26` ACTION: sed -n '220,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:34:03` sliced_wcs.py: world_to_pixel_values (around line 245): builds world_arrays_new, broadcasts, then does pixel_arrays = list(self._wcs.world_to_pixel_va...
- `18:33:50` ACTION: sed -n '230,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:33:45` RESULT: 245:    def world_to_pixel_values(self, *world_arrays):
- `18:33:44` ACTION: grep -n "def world_to_pixel" astropy/wcs/wcsapi/wrappers/sliced_wcs.py || true
- `18:33:23` ACTION: sed -n '1,400p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:33:08` ACTION: grep -nR "world_to_pixel" astropy || true
- `18:32:43` ACTION: sed -n '1,400p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:32:28` ACTION: sed -n '1,220p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:32:04` ACTION: sed -n '230,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:31:57` ACTION: grep -nR "world_to_pixel" astropy/wcs/wcsapi/wrappers || true
- `18:31:45` ACTION: sed -n '1,260p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:31:39` ACTION: grep -nR "class SlicedLowLevelWCS" . || true
- `18:31:29` ACTION: (grep -nR "class SlicedLowLevelWCS" . || true) && (grep -nR "SlicedLowLevelWCS" . || true)
- `18:31:17` ACTION: grep -nR "SlicedLowLevelWCS" .
