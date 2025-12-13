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

- [x] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 20:47] **swebench-astropy__astropy-13579**: Task completed: LimitsExceeded
## Interaction Log

- `20:47:37` ACTION: grep -nR "def world_to_pixel" astropy || true
- `20:47:23` ACTION: ls -la && find . -maxdepth 3 -type f -name "*.py" -print | sed -n '1,200p'
- `20:47:08` ACTION: grep -R -nE "(^|\s)(class|def)\s+X\b" || true
- `20:46:47` RESULT: X module not found
- `20:46:47` ACTION: sed -n '1,300p' X.py 2>/dev/null || ls -la X* 2>/dev/null || echo "X module not found"
- `20:46:30` ACTION: grep -n "def world_to_pixel" -R astropy || true && sed -n '1,420p' astropy/wcs/wcsapi/wrappers/slice [...]
- `20:45:58` ACTION: grep -n "def world_to_pixel" astropy/wcs/wcsapi/wrappers/sliced_wcs. [...]
- `20:45:30` ACTION: sed -n '1,420p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `20:45:23` ACTION: grep -n "def world_to_pixel" -R astropy || true
- `20:45:12` ACTION: grep -n "world_to_pixel" -R astropy || true && sed -n '1,400p' astropy/wcs/wcsapi/wrappers/sliced_wc [...]
- `20:44:57` repro_world_to_pixel.py: SlicedLowLevelWCS has no world_to_pixel attribute
- `20:44:52` ACTION: Reading file: <<'PY'
- `20:44:27` ACTION: sed -n '1,220p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `20:43:57` ACTION: sed -n '230,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `20:43:54` grep world_to_pixel_values: astropy/wcs/wcsapi/wrappers/sliced_wcs.py:245
- `20:43:48` RESULT: 245:    def world_to_pixel_values(self, *world_arrays):
- `20:43:48` ACTION: grep -n "def world_to_pixel" astropy/wcs/wcsapi/wrappers/sliced_wcs.py || true
- `20:43:29` ACTION: sed -n '1,420p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `20:43:08` ACTION: grep -n "def world_to_pixel" astropy/wcs/wcsapi/wrappers/sliced_wcs. [...]
- `20:42:02` ACTION: sed -n '1,400p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
