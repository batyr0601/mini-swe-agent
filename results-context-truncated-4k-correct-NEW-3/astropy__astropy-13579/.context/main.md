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

- [2025-12-02 15:57] **swebench-astropy__astropy-13579**: Task completed: LimitsExceeded
## Interaction Log

- `15:57:36` ACTION: grep -n "class SlicedLowLevelWCS" astropy/wcs/wcsapi/wrappers/sliced_wcs. [...]
- `15:57:22` ACTION: sed -n '240,340p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:57:17` RESULT: 245:    def world_to_pixel_values(self, *world_arrays):
- `15:57:17` ACTION: grep -n "def world_to_pixel" astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:57:05` ACTION: sed -n '1,260p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:56:44` ACTION: grep -n "def world_to_pixel" astropy/wcs/wcsapi/wrappers/sliced_wcs. [...]
- `15:55:35` ACTION: sed -n '1,420p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:55:13` ACTION: grep -n "def pixel_to_world_values" astropy/wcs/wcsapi/wrappers/sliced_wcs. [...]
- `15:54:56` ACTION: sed -n '230,340p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:54:49` RESULT: 245:    def world_to_pixel_values(self, *world_arrays):
- `15:54:48` ACTION: grep -n "def world_to_pixel" astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:54:31` ACTION: grep -n "def world_to_pixel" astropy/wcs/wcsapi/wrappers/sliced_wcs. [...]
- `15:54:10` ACTION: grep -nR "SlicedLowLevelWCS" astropy || true
- `15:53:48` ACTION: grep -nR "world_to_pixel" astropy || true
- `15:53:25` ACTION: sed -n '1,260p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:53:17` ACTION: sed -n '260,420p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:53:03` ACTION: sed -n '200,260p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `15:52:59` RESULT: 229:    def pixel_to_world_values(self, *pixel_arrays):
- `15:52:59` ACTION: grep -n "def pixel_to_world_values" astropy/wcs/wcsapi/wrappers/sliced_wcs.py || true
- `15:52:48` ACTION: sed -n '230,360p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
