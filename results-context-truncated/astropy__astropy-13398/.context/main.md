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
- [x] 1. Understand the bug: confirm that current ITRS<->AltAz/HADec transforms produce geocentric (SSB-referenced) artifacts for nearby/topocentric positions and that users expect topocentric behavior
- [x] 2. Locate the code: find coordinate frame and transformation implementations (files like testbed/itrs.py, testbed/altaz.py, testbed/hadec.py, and transformation registration code)
- [ ] 3. Root cause analysis: identify where ITRS->ITRS time-dependent transform references SSB/ITRF and why topocentric offset is not applied
- [ ] 4. Implement fix: add ITRS<->AltAz and ITRS<->HADec FunctionTransformWithFiniteDifference transforms that treat ITRS positions as time-invariant and perform topocentric offset using location.get_itrs()
- [x] 5. Verify fix: create repro script (repro_itrs_observed.py) to reproduce previous failing case (straight overhead), run it and update until results match expected topocentric output
- [x] 1. Reproduce round-trip discrepancy: write minimal script to do observer -> AltAz -> ITRS round-trip for unit-spherical, distance=0 m, and distance=1000 m cases; record alt/sep values
- [ ] 2. Locate offending code: inspect itrs_observed_transforms.py, intermediate_rotation_transforms.py, and erfa_astrom.apco/atioq/atoiq usage to find where observer position/velocity or distance handling causes negative altitude and non-zero round-trip offset
- [ ] 3. Implement fix: update transforms to use consistent observer position/velocity (consider using get_gcrs_posvel or ensuring proper units and offsets), and handle zero-distance/unit-spherical round-trips without introducing meter-valued offsets
- [ ] 4. Verify fix: run the reproduction script and existing tests; require round-trip difference < 1e-6 m for zero-distance and expected ~input distance for non-zero distances; log results
- [ ] 5. Inspect EarthLocation.get_itrs and _get_gcrs_posvel in astropy/coordinates/earth.py to check returned types/units and how obsgeoloc/obsgeovel are constructed
- [ ] 6. Compare astrometry context vs observer ITRS: compute astrom=erfa_astrom.get().apco(observed), call erfa.atoiq, build topocentric_cirs_cart, rotate to ITRS, add observer.get_itrs, and report component diffs and norm for distance=0 m case
- [ ] 7. Reproduce earlier non-zero round-trip (~379 m) and compare intermediate values (astrom, topocentric carts, observer_itrs) to current zero-diff case
- [ ] 8. Inspect itrs_to_observed implementation in astropy/coordinates/builtin_frames/itrs_observed_transforms.py to find why transforming an observer ITRS position to AltAz yields distance ~379.4859 m (check where distance is computed/assigned and if observer subtraction is happening correctly)
- [ ] 9. Inspect FunctionTransformWithFiniteDifference decorator implementation to see how ITRS->AltAz distance may be computed differently (finite difference path)
- [ ] 10. Inspect itrs_to_cirs implementation in astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py to see how distance is handled/propagated
- [ ] 11. Inspect cirs_to_observed implementation in astropy/coordinates/builtin_frames/cirs_observed_transforms.py to see how distances/units are set for observed frames
- [ ] 12. Inspect registration/priority of the direct ITRS->AltAz transform in astropy/coordinates/builtin_frames/itrs_observed_transforms.py and compare to ITRS->CIRS and CIRS->AltAz (both FunctionTransformWithFiniteDifference). Determine why composite path chosen and whether increasing direct transform priority or changing wrapper is appropriate to avoid finite-difference-induced non-zero distances

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:57] **swebench-astropy__astropy-13398**: Task completed: LimitsExceeded
## Interaction Log

- `19:57:14` inspected itrs_to_cirs: rotates ITRS cartesian via pmatrix transpose, builds CIRS(newrepr, obstime=...), then returns cirs.transform_to(cirs_frame) (m...
- `19:56:52` ACTION: sed -n '/def itrs_to_cirs/,/def /p' astropy/coordinates/builtin_frames/intermediate_rotation_transfo [...]
- `19:55:56` ACTION: python3 - <<'PY'
- `19:55:41` ACTION: sed -n '1040,1320p' astropy/coordinates/transformations.py
- `19:55:35` ACTION: sed -n '880,1040p' astropy/coordinates/transformations.py
- `19:54:55` ACTION: python3 - <<'PY'
- `19:54:15` ACTION: ln=$(grep -n "def itrs_to_observed" astropy/coordinates/builtin_frames/itrs_observed_transforms. [...]
- `19:54:07` Case B (Unit-spherical ITRS direction -> AltAz -> ITRS): initial unitless cart=(0.17771384691966347, -0.7697632404587502, 0.6130924418482574); derived...
- `19:54:07` Case A (Full ITRS -> AltAz -> ITRS): initial itrs cart (m)= (1132050.281788885, -4903448.484045137, 3905443.968419102); derived AltAz: az=203d53m37.46...
- `19:53:03` astrom.pmt=19.9986332669151; astrom.eb=[-0.17012717  0.8959947   0.38846176]; astrom.eh=[-0.1691517   0.9042703   0.39202415]; astrom.em=0.98330982194...
- `19:52:41` ACTION: python3 - <<'PY'
- `19:51:07` Inspected observed_to_itrs: is_unitspherical = (UnitSphericalRepresentation or cartesian.x.unit == u.one); uses erfa.atoiq(astrom) to get topocentric ...
- `19:50:42` ACTION: sed -n '90,200p' astropy/coordinates/builtin_frames/itrs_observed_transforms.py
- `19:49:53` ACTION: grep -nR "get_itrs\|_get_gcrs_posvel" astropy | sed -n '1,200p'
- `19:49:46` Inspected transforms and astrometry: cirs_to_itrs_mat uses erfa.pom00/sp00 and erfa.c2tcio with identity for CIRS->ITRS (ERA + p-matrix). observed_to_...
- `19:49:28` ACTION: ln=$(grep -n "def cirs_to_itrs_mat" astropy/coordinates/builtin_frames/intermediate_rotation_transfo [...]
- `19:49:12` ACTION: nl -ba astropy/coordinates/erfa_astrom.py | sed -n '314,420p' && nl -ba astropy/coordinates/builtin_ [...]
- `19:48:57` ACTION: nl -ba astropy/coordinates/builtin_frames/itrs_observed_transforms. [...]
- `19:48:44` Repro script output: AltAz from observer: az = 203d53m37.46260327s , alt = -0d10m37.03142158s; Case unit-spherical input: itrs cartesian.x unit: <none...
- `19:47:25` Test results: UNIT-SPHERICAL -> ITRS: cartesian.x unit: <none>, value: 0.17726265710270228; WITH DISTANCE=1000 m -> ITRS: separation (itrs - observer)...
