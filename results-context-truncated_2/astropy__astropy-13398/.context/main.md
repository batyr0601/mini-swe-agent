# Project Goals

**Current Task:** A direct approach to ITRS to Observed transformations that stays within the ITRS.

<details>
<summary>Full description</summary>

A direct approach to ITRS to Observed transformations that stays within the ITRS.
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

### Description
<!-- Provide a general description of the feature you would like. -->
<!-- If you want to, you can s...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: reproduce and document the apparent inaccuracy of ITRS->AltAz transforms (geocentric vs topocentric aberration) using a small script
- [ ] 2. Locate the code: find existing transformation implementations and frame definitions for ITRS, AltAz, HADec, and frame_transform_graph in the testbed codebase
- [ ] 3. Create repro: write a small script under testbed/ to demonstrate the discrepancy and expected behavior (based on PR example)
- [ ] 4. Implement fix: add direct ITRS<->AltAz and ITRS<->HADec transforms that operate in topocentric ITRS (time-invariant ITRS position, adopt output obstime) and include optional refraction handling
- [ ] 5. Verify fix: run the repro script and existing relevant tests, inspect results, and iterate until behavior matches expected
- [ ] 6. Log and commit: record findings after each command with context_log, mark TODOs complete as tasks finish
- [ ] 1. Understand requirement: add direct transforms ITRS<->AltAz and ITRS<->HADec to avoid slow intermediate frame broadcasting and redundant transforms
- [ ] 2. Locate code: identify files to inspect/modify/create: astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py, cirs_observed_transforms.py, icrs_observed_transforms.py, and create astropy/coordinates/builtin_frames/itrs_observed_transforms.py
- [ ] 3. Root cause analysis: analyze cirs_to_observed and itrs_to_cirs implementations to find where frame.transform_to triggers broadcasting and what matrices/erfa calls are needed for a direct transform
- [ ] 4. Implement fix: add FunctionTransformWithFiniteDifference transforms for ITRS->AltAz, ITRS->HADec, AltAz->ITRS, HADec->ITRS in itrs_observed_transforms.py using cirs_to_itrs_mat/matrix_transpose, erfa.atioq/atoiq, erfa_astrom.apio, and avoid constructing intermediate CIRS frames
- [ ] 5. Verify fix: run small repro transforming sample coordinates ITRS<->AltAz and ITRS<->HADec to ensure correctness and run relevant coordinates tests (e.g., tests for observed transforms) to confirm no regressions
- [ ] 2. Find duplicate _add_merged_transform calls causing ValueError on import (search repository for usages)
- [ ] Run observed transforms unit tests: pytest -q astropy/coordinates/tests/test_observed_transforms.py
- [ ] Run coordinates transform tests for frames: pytest -q astropy/coordinates/tests/test_transformations.py
- [x] Create and run randomized round-trip ITRS<->AltAz/HADec test (many random positions and times) and log results
- [ ] Run observed transforms and coordinates tests in CI or developer environment (pytest -q astropy/coordinates/tests/test_observed_transforms.py and pytest -q astropy/coordinates/tests/test_transformations.py); capture and log outputs
- [ ] Add unit tests: create astropy/coordinates/tests/test_itrs_observed_transforms.py with coverage for AltAz/HADec roundtrips, broadcasting and edge cases (vectorized obstime/location), and include small repro cases
- [ ] Prepare PR: create branch, ensure itrs_observed_transforms.py is documented, add changelog entry under CHANGES.rst/whatsnew, run linters/flake8 locally, and produce a clear PR description referencing issue #13398
- [ ] Run full CI/tests in developer/CI environment: push branch and open PR to run pytest -q and capture logs for astropy/coordinates tests and the full test suite; record results in context_log
- [x] Investigate unit mismatch in itrs_observed_transforms.py: inspect topo_cirs and obs_cirs types/units (around line 58), ensure both are CartesianRepresentation with compatible units or apply explicit unit conversions; create small repro printing units/shapes and run targeted tests
- [x] Fix unit mismatch in itrs_observed_transforms.py: at line ~58 before topo_cirs = geoc_cirs - obs_cirs, convert obs_cirs to geoc_cirs units (e.g., obs_cirs = obs_cirs.to(geoc_cirs.x.unit)) or convert geoc_cirs to meters; add unit tests covering this case and run targeted pytest on astropy/coordinates/tests/test_itrs_observed_transforms.py
- [x] Fix unit mismatch in observed_to_itrs: ensure topo_cirs + obs_cirs addition only for non-unit-spherical cases or convert obs_cirs to matching units; update code and tests accordingly
- [ ] Prepare PR: create branch
- [ ] Run coordinates transform tests: pytest -q astropy/coordinates/tests/test_transformations.py -k
- [ ] Identify transformations tests related to ITRS/AltAz/HADec: inspect test_transformations.py around AltAz occurrences to find specific test function names to run
- [x] Run specific transformation test: pytest -q astropy/coordinates/tests/test_transformations.py::test_vel_transformation_obstime_err with IERS/Astropy warnings suppressed
- [x] Run broader coordinates tests: pytest -q astropy/coordinates/tests with Astropy/IERS warnings suppressed; capture results
- [ ] 1. Analyze failing tests: rerun pytest -x on astropy/coordinates/tests to stop at first failure and capture full traceback for root-cause analysis
- [x] 1. Analyze failure: investigate AttributeError
- [x] 2. Locate code: display astropy/coordinates/builtin_frames/itrs_observed_transforms.py lines 1-220 to inspect is_unitspherical logic and distance usage
- [x] Implement fix: in itrs_to_observed, obtain distance via getattr(itrs_coo,
- [ ] 18. Run observed transforms unit tests: pytest -q astropy/coordinates/tests/test_observed_transforms.py with Astropy/IERS warnings suppressed; capture results
- [x] Run observed-related tests: pytest -q astropy/coordinates/tests/test_itrs_observed_transforms.py astropy/coordinates/tests/test_icrs_observed_transformations.py with Astropy/IERS warnings suppressed; capture results
- [ ] 32. Run broader coordinates tests: pytest -q astropy/coordinates/tests with Astropy/IERS warnings suppressed; capture results
- [ ] 1. Analyze TestHCRS setup error: rerun pytest -x for astropy/coordinates/tests/test_celestial_transformations.py::TestHCRS::test_from_hcrs to capture full setup traceback for root-cause analysis

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:12] **swebench-astropy__astropy-13398**: Task completed: LimitsExceeded
- [2025-12-01 21:02] **swebench-astropy__astropy-13398**: Fix itrs_observed_transforms unit mismatch: convert obs_cirs to matching units for Cartesian cases a...
- [2025-12-01 20:45] **swebench-astropy__astropy-13398**: Add direct ITRS<->AltAz and ITRS<->HADec transforms in itrs_observed_transforms.py; implement itrs_t...
## Interaction Log

- `21:12:04` pytest -q astropy/coordinates/tests: 4 failed, 1419 passed, 67 skipped, 22 xfailed, 85 errors in 22.75s; representative error locations include repres...
- `21:11:10` astropy/coordinates/tests/test_itrs_observed_transforms.py and test_icrs_observed_transformations.py: 6 passed in 0.43s
- `21:10:25` ACTION: find astropy/coordinates/tests -maxdepth 1 -type f \( -iname "*observed*.py" -o -iname "*itrs*. [...]
- `21:10:09` Implemented fallback distance in itrs_observed_transforms: test_regression_5133 passed (1 passed). Patched astropy/coordinates/builtin_frames/itrs_obs...
- `21:09:40` ACTION: pytest -q astropy/coordinates/tests/test_regression.py::test_regression_5133 -W ignore::astropy. [...]
- `21:09:30` ACTION: git add astropy/coordinates/builtin_frames/itrs_observed_transforms.py && git status --porcelain
- `21:08:53` itrs_observed_transforms.itrs_to_observed: AttributeError 'ITRS' object has no attribute distance at astropy/coordinates/builtin_frames/itrs_observed_...
- `21:08:05` ACTION: pytest -q astropy/coordinates/tests -x -W ignore::pytest.PytestRemovedIn8Warning -W ignore::astropy. [...]
- `21:06:34` ACTION: git --no-pager diff --staged astropy/coordinates/builtin_frames/itrs_observed_transforms. [...]
- `21:06:22` ACTION: Reading file: <<'EOF'
- `21:06:05` ACTION: git add -- astropy/coordinates/builtin_frames/itrs_observed_transforms. [...]
- `21:05:37` ACTION: git status --porcelain && git --no-pager diff -- astropy/coordinates/builtin_frames/itrs_observed_tr [...]
- `21:05:10` test_transformations::test_vel_transformation_obstime_err: 1 passed
- `21:04:29` ACTION: Reading file: 200
- `21:04:19` ACTION: grep -n -E 'itrs|observed' astropy/coordinates/tests/test_transformations.py | sed -n '1,200p'
- `21:03:47` ACTION: pytest -q astropy/coordinates/tests/test_icrs_observed_transformations. [...]
- `21:03:30` ACTION: ls -la astropy/coordinates/tests
- `21:03:23` ACTION: pytest -q astropy/coordinates/tests/test_observed_transforms.py -W ignore::astropy.utils.exceptions. [...]
- `21:02:55` ACTION: (git rev-parse --verify fix/itrs-unit-mismatch >/dev/null 2>&1 || git checkout -b fix/itrs-unit-mism [...]
- `21:01:58` itrs_observed_transforms tests: 4 passed in 0.30s when run with IERS/Astropy warnings ignored; confirmed unit-mismatch fixes for both ITRS->observed a...
