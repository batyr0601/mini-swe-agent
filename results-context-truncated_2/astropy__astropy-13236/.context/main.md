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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the current behavior: find code where structured ndarray is auto-viewed as NdarrayMixin (search for
- [ ] 2. Locate the Table/Column creation code: open the file(s) implementing the logic that wraps structured numpy arrays (likely table/column factory functions)
- [ ] 3. Implement deprecation warning: add FutureWarning that advises wrapping data in Column and announces behavior change in version 5.2
- [ ] 4. Modify code to keep current behavior but emit warning now; plan to remove automatic view in 5.2 (documented TODO)
- [ ] 5. Create a small repro script to verify the warning and behavior and run it to confirm the fix

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:41] **swebench-astropy__astropy-13236**: Task completed: Submitted
## Interaction Log

- `20:41:06` ACTION: Submitting solution
- `20:41:02` RESULT: Inserted TODO note in astropy/table/table.py
Wrote CHANGES.rst
- `20:40:57` /testbed/astropy/table/table.py:1246: FutureWarning: Adding a structured numpy.ndarray to a Table currently causes it to be viewed as an NdarrayMixin....
- `20:40:43` ACTION: python3 - <<'PY'
- `20:40:27` ACTION: Reading file: repro_warning.py
- `20:40:20` astropy/table/table.py: inserted FutureWarning before data.view(NdarrayMixin) to warn users that structured arrays will be added as Column in v5.2; cu...
- `20:40:16` RESULT: Inserted FutureWarning before data.view(NdarrayMixin) in astropy/table/table.py
- `20:40:15` ACTION: python3 - <<'PY'
- `20:40:00` RESULT: Pattern not found, aborting
- `20:40:00` ACTION: python3 - <<'PY'
- `20:39:44` ACTION: nl -ba astropy/table/table.py | sed -n '1,120p'
- `20:39:35` ACTION: nl -ba astropy/table/table.py | sed -n '1200,1260p'
- `20:39:29` ACTION: grep -nR "NdarrayMixin" . || true
- `20:39:18` TASK STARTED: Consider removing auto-transform of structured column into NdarrayMixin
