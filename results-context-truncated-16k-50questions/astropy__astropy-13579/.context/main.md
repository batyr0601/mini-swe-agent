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
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:25] **swebench-astropy__astropy-13579**: Task completed: Submitted
## Interaction Log

- `23:25:49` ACTION: Submitting solution
- `23:25:44` Verified fix by running repro.py once: sliced world_to_pixel_values matches full WCS spatial components (array(49.5), array(12.))
- `23:25:44` Implemented fix: SlicedLowLevelWCS.world_to_pixel_values now uses default world values from _pixel_to_world_values_all for dropped axes instead of con...
- `23:25:31` Verified that using default world values for dropped axes fixes the world_to_pixel_values behavior for the provided 3D WCS example; sliced and unslice...
- `23:25:29` Found bug in SlicedLowLevelWCS.world_to_pixel_values: dropped world dims were filled with 1.0 causing incorrect results; fix: use default world values...
- `23:25:23` repro.py: full world_to_pixel_values -> (array(49.5), array(12.), array(0.)); sliced world_to_pixel_values -> (array(49.5), array(12)) after patching ...
- `23:24:39` ACTION: Reading file: repro.py
- `23:24:24` ACTION: sed -n '1,999p' astropy/wcs/wcsapi/wrappers/sliced_wcs. [...]
- `23:23:28` ACTION: nl -ba astropy/wcs/wcsapi/wrappers/sliced_wcs.py | sed -n '240,520p'
- `23:23:25` ACTION: nl -ba astropy/wcs/wcsapi/wrappers/sliced_wcs.py | sed -n '1,240p'
- `23:23:22` ACTION: grep -R --line-number "SlicedLowLevelWCS" astropy || true
- `23:23:19` ACTION: ls -la
- `23:23:16` RESULT: ls: cannot access 'testbed': No such file or directory
- `23:23:16` ACTION: ls -la testbed
- `23:23:09` TASK STARTED: Inconsistent behavior of `world_to_pixel` in `SlicedLowLevelWCS`
