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
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create a small script using testbed frames to show ITRS->AltAz gives unexpected results for nearby objects (satellites/buildings) and compare to expected topocentric behavior
- [ ] 2. Locate the code: find files defining ITRS, AltAz, HADec frames and existing transforms in /testbed (search for class names and frame_transform_graph usage)
- [ ] 3. Root cause analysis: inspect current ITRS->AltAz/HADec transforms to see if they perform ITRS->ITRS time-dependent reprojections (geocentric vs topocentric) and identify where to change behavior
- [ ] 4. Implement fix: add direct ITRS<->AltAz and ITRS<->HADec transforms in /testbed using topocentric approach (treat ITRS positions as time-invariant, compute topocentric offset using location.get_itrs(), apply rotation matrices as in PR description), and ensure obstime adoption behavior is correct
- [ ] 5. Verify fix: add a reproduction script/test in /testbed to assert overhead object appears at zenith and run pytest or the script; log results and mark todos complete
- [ ] 1. Understand the long grep output: determine which grep produced the long output and what needs narrowing
- [ ] 2. Locate the definition of frame_transform_graph (likely in astropy/coordinates/baseframe.py)
- [ ] 3. Inspect astropy/coordinates/baseframe.py around the frame_transform_graph definition (~20 lines) to confirm creation/assignment
- [ ] 4. Search for uses of frame_transform_graph.frame_attributes and frame_transform_graph.lookup_name to find code paths handling frame attributes
- [ ] 5. Run focused greps and file views based on findings, log outputs after each command, and mark todos complete as progress is made

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:04:01` ACTION: grep -nR "frame_transform_graph" .
- `01:03:41` ACTION: grep -nR -E --exclude-dir=.git "(class\s+\w*(ITRS|AltAz|HADec))|frame_transform_graph|register_trans [...]
- `01:03:19` TASK STARTED: A direct approach to ITRS to Observed transformations that stays within the ITRS.
