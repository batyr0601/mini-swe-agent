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

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:25] **swebench-astropy__astropy-13398**: Task completed: Submitted
## Interaction Log

- `00:25:49` ACTION: Submitting solution
- `00:25:26` repro_itrs_observed: AltAz and round-trip ITRS transformation succeeded, diff 0.0 m
- `00:25:21` ACTION: Reading file: repro_itrs_observed.py
- `00:24:52` Created itrs_observed_transforms.py with direct ITRS<->AltAz and ITRS<->HADec transforms (uses topocentric ITRS, treats ITRS positions as time invaria...
- `00:24:43` ACTION: Reading file: astropy/coordinates/builtin_frames/itrs_observed_transforms.py
- `00:24:20` ACTION: nl -ba astropy/coordinates/earth.py | sed -n '560,600p'
- `00:24:16` ACTION: grep -n "def to_geodetic\\|to_geodetic(" astropy -R || true
- `00:24:03` ACTION: nl -ba astropy/coordinates/earth.py | sed -n '1,260p'
- `00:23:54` ACTION: grep -R --line-number "@frame_transform_graph.transform.*ITRS.*AltAz\\|@frame_transform_graph. [...]
- `00:23:50` ACTION: nl -ba astropy/coordinates/builtin_frames/icrs_observed_transforms.py | sed -n '1,240p'
- `00:23:44` ACTION: grep -R -n "AltAz\\|HADec" astropy/coordinates/builtin_frames || true
- `00:23:41` RESULT: grep: astropy/coordinates/builtin_frames: Is a directory
- `00:23:41` ACTION: grep -n "AltAz\\|HADec" astropy/coordinates/builtin_frames || true
- `00:23:37` ACTION: nl -ba astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py | sed -n '1,240p'
- `00:23:32` ACTION: grep -R --line-number "ITRS" -n astropy/coordinates || true
- `00:23:27` ACTION: ls -la
- `00:23:19` TASK STARTED: A direct approach to ITRS to Observed transformations that stays within the ITRS.
