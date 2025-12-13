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

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 18:44] **swebench-astropy__astropy-13579**: Task completed: LimitsExceeded
## Interaction Log

- `18:44:05` ACTION: sed -n '1,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:43:59` repro_sliced_wcs.py: INIT_EXCEPTION: AttributeError 'DummyWCS' object has no attribute 'axis_correlation_matrix
- `18:43:49` ACTION: Reading file: <<'PY'
- `18:43:25` ACTION: grep -nR "world_to_pixel_values" . || true
- `18:42:55` ACTION: sed -n '1,240p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:42:40` ACTION: sed -n '230,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:42:27` unbound call error: DummyWCS missing world_n_dim; AttributeError: 'DummyWCS' object has no attribute 'world_n_dim' at astropy/wcs/wcsapi/wrappers/slic...
- `18:42:04` ACTION: python3 - <<'PY'
- `18:41:53` grep world_to_pixel_values: astropy/wcs/wcsapi/wrappers/sliced_wcs.py:245,257
- `18:41:46` ACTION: grep -n "world_to_pixel_values" astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:41:34` repro: USING_METHOD _pixel_to_world_values_all; AttributeError: can't set attribute when assigning attributes to SlicedLowLevelWCS instance
- `18:41:25` ACTION: python3 - <<'PY'
- `18:40:53` sliced_wcs.py contains 'pixel_arrays_result' and zero-dim ndarray guard (PATCH_PRESENT)
- `18:40:38` RESULT: PATCH_PRESENT
- `18:40:38` ACTION: python3 - <<'PY'
- `18:40:11` ACTION: git --no-pager diff -- astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:39:42` patched astropy/wcs/wcsapi/wrappers/sliced_wcs.py: capture raw_pixel_arrays from self._wcs.world_to_pixel_values, return 0-d ndarray if present, other...
- `18:38:29` ACTION: sed -n '200,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
- `18:38:23` ACTION: python3 - <<'PY'
- `18:36:11` ACTION: sed -n '200,320p' astropy/wcs/wcsapi/wrappers/sliced_wcs.py
