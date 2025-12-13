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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:24] **swebench-astropy__astropy-13236**: Task completed: Submitted
## Interaction Log

- `00:24:28` ACTION: Submitting solution
- `00:24:24` repro.py: printed 'is NdarrayMixin: NdarrayMixin' and issued FutureWarning 'Adding a structured numpy.ndarray to a Table currently auto-converts it to...
- `00:24:24` patched astropy/table/table.py: inserted FutureWarning before viewing structured ndarray as NdarrayMixin
- `00:24:06` ACTION: Reading file: <<'PY'
- `00:24:02` RESULT: patched
- `00:24:01` ACTION: python3 - <<'PY'
- `00:23:46` RESULT: error: unrecognized input
- `00:23:45` ACTION: git apply -p0 <<'PATCH'
- `00:23:36` ACTION: nl -ba astropy/table/table.py | sed -n '1200,1260p'
- `00:23:32` ACTION: grep -nR "NdarrayMixin" .
- `00:23:30` ACTION: grep -nR "NdarrayMixin" -S .
- `00:23:19` TASK STARTED: Consider removing auto-transform of structured column into NdarrayMixin
