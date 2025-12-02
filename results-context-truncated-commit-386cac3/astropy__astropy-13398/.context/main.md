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
- [ ] 1. Reproduce: create a small script that demonstrates the ITRS->AltAz/HADec inaccuracy for nearby/topocentric objects (straight overhead example) and run it to reproduce the issue
- [ ] 2. Locate: find existing transform implementations for ITRS<->AltAz and ITRS<->HADec in astropy/coordinates to identify where to add/modify code
- [ ] 3. Analyze: inspect ITRS->ITRS time handling and confirm the cause (reference to SSB/geocentric vs topocentric aberration) and log findings
- [ ] 4. Implement fix: add new direct transforms ITRS->AltAz and ITRS->HADec (and reverse) that operate in ITRS: form topocentric ITRS via subtraction, apply rotation matrices, and adopt output frame obstime (treat ITRS as time-invariant)
- [ ] 5. Verify fix: run existing relevant tests and a reproduction script (including straight_overhead test) and adjust implementation if necessary
- [ ] 2. Locate: find any existing ITRS<->observed transform implementations and related helpers (check itrs_observed_transforms.py, cirs_observed_transforms.py, intermediate_rotation_transforms.py, earth.py)
- [ ] 3. Analyze: inspect rotation conventions, handedness, axis order, and EarthLocation.get_itrs/_get_gcrs_posvel to determine why direct ITRS->observed math gave large errors
- [ ] 4. Implement: based on analysis, implement corrected direct ITRS<->AltAz and ITRS<->HADec transforms (using proper topocentric subtraction and rotation matrices) or retain CIRS-delegation and document rationale
- [ ] 5. Verify: run reproduce_itrs_observed.py and coordinate-related test suite; add unit test for straight_overhead topocentric case
- [ ] Investigate: determine which transform path frame_transform_graph used for ITRS->AltAz in test; inspect itrs_observed_transforms.py and transform registry
- [ ] Investigate: inspect EarthLocation._get_gcrs_posvel and get_location_gcrs usage to verify matrix directions (ref_to_itrs, gcrs_to_ref), units, and whether obsgeoloc/obsgeovel are correct
- [ ] Investigate: inspect callers of get_location_gcrs to verify ordering/meaning of (ref_to_itrs, gcrs_to_ref) and detect any swapped/misused matrices
- [ ] Investigate: reproduce ITRS->CIRS step-by-step for straight-overhead case; print pmatrix, transformed vector, CIRS ra/dec, astrom atioq outputs to locate discrepancy
- [ ] Fix: inspect and correct ordering/meaning of (ref_to_itrs, gcrs_to_ref) passed to get_location_gcrs in intermediate_rotation_transforms (gcrs_to_tete, gcrs_to_cirs, cirs_to_gcrs) and relevant callers in cirs_observed_transforms/itrs_observed_transforms
- [ ] Inspect: review tests around get_location_gcrs usage in test_intermediate_transformations.py to determine expected behavior and correct matrix ordering/usage
- [ ] Locate: find EarthLocation._get_gcrs_posvel implementation to check expected matrix argument order and usage

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:52] **swebench-astropy__astropy-13398**: Task completed: LimitsExceeded
- [2025-12-01 19:34] **swebench-astropy__astropy-13398**: Analyze rotation conventions: document missing polar-motion/ERA/astrom as cause of direct-math failu...
- [2025-12-01 19:31] **swebench-astropy__astropy-13398**: Add direct ITRS<->observed transforms and register module
## Interaction Log

- `19:52:13` ACTION: Reading file: <<'PY'
- `19:51:32` RESULT: ERROR: bash: -c: line 31: syntax error near unexpected token `&&'
- `19:51:32` ACTION: Reading file: <<'PY'
- `19:50:44` RESULT: ERROR: bash: -c: line 31: syntax error near unexpected token `&&'
- `19:50:44` ACTION: Reading file: <<'PY'
- `19:50:00` RESULT: ✓ Logged to context NEXT STEPS: 1) Inspect callers of get_location_gcrs in intermediate_rotation_transforms. [...]
- `19:50:00` Planned fix: inspect/adjust matrix ordering for get_location_gcrs callers; save plan to /tmp/next_steps.txt
- `19:50:00` ACTION: echo "NEXT STEPS:
- `19:49:13` RESULT: bash: line 1: context_todos: command not found
✓ Logged to context
- `19:49:13` Saved EarthLocation._get_gcrs_posvel snippet to /tmp/get_gcrs_posvel_snip.txt for inspection
- `19:49:12` ACTION: N=$(context_todos | awk -F'.' '/Locate: find EarthLocation. [...]
- `19:48:37` RESULT: ERROR: except KeyError as err:
- `19:48:36` Displayed EarthLocation._get_gcrs_posvel implementation from astropy/coordinates/earth.py for inspection
- `19:48:36` ACTION: sed -n '678,920p' astropy/coordinates/earth.py && context_log "Displayed EarthLocation. [...]
- `19:48:02` Displayed tests around get_location_gcrs to determine expected behavior and matrix ordering
- `19:47:31` RESULT: orig loc_gcrs.obsgeoloc (m): [820807.2032113568, -4444028.216341462, 4485734.258594442] swapped loc_gcrs.obsgeoloc (m): [813717.9255412456, -4...
- `19:47:30` ACTION: python - <<'PY'
- `19:46:45` RESULT: matrix_transpose(gcrs_to_ref) (transpose_pmat): [[ 0.999998 0. 0.001911] [ 0. 1. -0.000012] [-0.001911 0.000012 0. [...]
- `19:46:43` ACTION: python - <<'PY'
