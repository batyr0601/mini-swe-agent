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

- [2025-12-03 00:26] **swebench-astropy__astropy-13579**: Task completed: Submitted
## Interaction Log

- `00:26:35` ACTION: Submitting solution
- `00:26:30` repro.py after fix: full world_to_pixel_values -> (array(1.90909091e+11), array(12.), array(1.90909091e+11)); sliced world_to_pixel_values -> (array(4...
- `00:26:13` Fix implemented: use dropped_world_dimensions values in world_to_pixel_values for dropped world axes (astropy/wcs/wcsapi/wrappers/sliced_wcs.py)
- `00:26:10` Root cause analysis: SlicedLowLevelWCS.world_to_pixel_values inserted a literal 1.0 for dropped world axes instead of using the actual world values fo...
- `00:26:01` Root cause: SlicedLowLevelWCS.world_to_pixel_values (astropy/wcs/wcsapi/wrappers/sliced_wcs.py) inserted 1.0 for dropped world axes, leading to incorr...
- `00:25:51` repro.py: full world_to_pixel_values -> (array(1.90909091e+11), array(12.), array(1.90909091e+11)); sliced world_to_pixel_values -> (array(49.5), arra...
- `00:24:59` ACTION: Reading file: <<'PY'
- `00:24:51` ACTION: sed -i 's/^world_arrays_new = np.broadcast_arrays/ world_arrays_new = np. [...]
- `00:24:41` ACTION: nl -ba astropy/wcs/wcsapi/wrappers/sliced_wcs.py | sed -n '240,276p'
- `00:24:36` ACTION: python3 - <<'PY'
- `00:24:09` RESULT: error: unrecognized input
- `00:24:09` ACTION: git apply -p0 <<'PATCH'
- `00:23:48` ACTION: nl -ba astropy/wcs/wcsapi/wrappers/sliced_wcs.py | sed -n '100,200p'
- `00:23:37` ACTION: nl -ba astropy/wcs/wcsapi/wrappers/sliced_wcs.py | sed -n '1,320p'
- `00:23:33` ACTION: grep -nR "SlicedLowLevelWCS\|class SlicedLowLevelWCS\|world_to_pixel" astropy || true
- `00:23:31` ACTION: ls -la
- `00:23:28` RESULT: grep: testbed: No such file or directory
- `00:23:28` ACTION: grep -nR "SlicedLowLevelWCS\|world_to_pixel\|Sliced" testbed || true
- `00:23:19` TASK STARTED: Inconsistent behavior of `world_to_pixel` in `SlicedLowLevelWCS`
