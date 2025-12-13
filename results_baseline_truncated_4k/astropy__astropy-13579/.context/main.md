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
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce bug: create a script reproducing SlicedLowLevelWCS world_to_pixel discrepancy using the provided example
- [ ] 2. Locate code: find SlicedLowLevelWCS and HighLevelWCSWrapper implementations in testbed
- [ ] 3. Investigate root cause: inspect slicing handling and world_to_pixel mapping of axes and shape of outputs
- [ ] 4. Implement fix: adjust SlicedLowLevelWCS world_to_pixel to correctly handle fixed axes and preserve axis ordering/units
- [ ] 5. Verify fix: run reproduction script and existing tests; add edge-case tests for various axis orderings
- [ ] 1. Understand the bug: run the repro script or failing test to capture the exact error message and full traceback (e.g., run python3 repro.py or pytest -k <failing_test>)
- [ ] 2. Locate the code: search the repository for keywords from the traceback (e.g., grep -n
- [ ] 3. Root cause analysis: inspect the identified functions/files, read surrounding code to see where exceptions are caught or re-raised, and identify why the wrong attribute name/message is produced
- [ ] 4. Implement fix: modify the code to let descriptor/property exceptions propagate correctly or to construct the correct missing-attribute message; add a focused unit test demonstrating the expected behavior
- [ ] 5. Verify fix: run the repro and the full test suite (pytest) to confirm the bug is fixed and no regressions introduced; iterate if failures remain

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:03:57` ACTION: pytest -q
- `01:03:35` ACTION: grep -Rn --line-number "SlicedLowLevelWCS" . || true && grep -Rn --line-number "HighLevelWCSWrapper" [...]
- `01:03:18` TASK STARTED: Inconsistent behavior of `world_to_pixel` in `SlicedLowLevelWCS`
