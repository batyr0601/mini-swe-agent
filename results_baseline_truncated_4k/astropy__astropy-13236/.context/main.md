# Project Goals

**Current Task:** Consider removing auto-transform of structured column into NdarrayMixin

<details>
<summary>Full description</summary>

Consider removing auto-transform of structured column into NdarrayMixin
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
<!-- If you want to, you can suggest a d...
</details>


## TODO List

- [ ] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create a minimal script that adds a structured np.ndarray to a Table-like object and observe it being converted to NdarrayMixin or similar
- [ ] 2. Locate the code: search repository for code that views structured numpy arrays as NdarrayMixin or related conversion (e.g., grep for
- [ ] 3. Root cause analysis: inspect the located code to determine why structured arrays are auto-viewed as NdarrayMixin and how unified I/O relies on that
- [ ] 4. Implement fix: add a FutureWarning telling users to wrap data in Column and modify code to stop auto-viewing structured arrays as NdarrayMixin (plan to remove clause in future release), keeping behavior backward-compatible for now
- [ ] 5. Verify fix: run the reproduction script and any relevant tests to confirm the warning appears and that structured arrays are added as Column (or not auto-converted) as intended

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:04:00` astropy/table/table.py:1200-1260: structured ndarray auto-viewed as NdarrayMixin at ~lines 1245-1246 via: if (not isinstance(data, Column) and not dat...
- `01:03:46` ACTION: sed -n '1200,1260p' astropy/table/table.py
- `01:03:42` ACTION: grep -RIn -e "NdarrayMixin" -e "len(data.dtype) > 1" . || true
- `01:03:37` RESULT: grep: testbed: No such file or directory
- `01:03:37` ACTION: grep -RIn --line-number -e "NdarrayMixin" -e "len(data.dtype) > 1" testbed || true
- `01:03:19` TASK STARTED: Consider removing auto-transform of structured column into NdarrayMixin
