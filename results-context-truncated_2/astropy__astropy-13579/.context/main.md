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
- [ ] 1. Reproduce the bug using provided WCS example and SlicedLowLevelWCS
- [ ] 2. Locate SlicedLowLevelWCS and related world_to_pixel logic in testbed source
- [ ] 3. Identify cause: check coordinate axis ordering, unit handling, and world->pixel mapping for sliced WCS
- [ ] 4. Implement fix: adjust SlicedLowLevelWCS.world_to_pixel mapping to include fixed axis values and correct matrix application
- [ ] 5. Add/modify tests or reproduction script to verify behavior and run them

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:41] **swebench-astropy__astropy-13579**: Task completed: Submitted
## Interaction Log

- `20:41:46` ACTION: Submitting solution
- `20:41:39` Root cause: world_to_pixel_values used literal 1.0 for dropped world axes which breaks mappings when world and pixel axes are coupled; fix: use droppe...
- `20:41:39` Located SlicedLowLevelWCS implementation at astropy/wcs/wcsapi/wrappers/sliced_wcs.py; relevant methods: world_to_pixel_values, pixel_to_world_values,...
- `20:41:19` Reproducer shows sliced world_to_pixel now returns (49.5, 12.0) matching full WCS
- `20:40:37` ACTION: Reading file: <<'PY'
- `20:40:18` Patched sliced_wcs.py: replaced placeholder 1.0 with dropped value from dropped_world_dimensions in world_to_pixel_values
- `20:40:11` RESULT: Patched sliced_wcs.py
- `20:40:11` ACTION: python - <<'PY'
- `20:39:49` ACTION: nl -ba astropy/wcs/wcsapi/wrappers/sliced_wcs.py | sed -n '120,220p'
- `20:39:35` ACTION: nl -ba astropy/wcs/wcsapi/wrappers/sliced_wcs.py | sed -n '1,320p'
- `20:39:29` ACTION: grep -nR --line-number -E "SlicedLowLevelWCS|LowLevelWCS|world_to_pixel|pixel_to_world" .
- `20:39:18` TASK STARTED: Inconsistent behavior of `world_to_pixel` in `SlicedLowLevelWCS`
