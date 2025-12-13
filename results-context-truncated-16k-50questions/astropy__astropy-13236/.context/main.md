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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:25] **swebench-astropy__astropy-13236**: Task completed: Submitted
## Interaction Log

- `23:25:02` ACTION: Submitting solution
- `23:24:56` repro_structured_array.py: showed FutureWarning and column is NdarrayMixin; dtype preserved
- `23:24:52` ACTION: Reading file: repro_structured_array.py
- `23:24:39` Rewrote structured-array handling block in astropy/table/table.py; added FutureWarning advising users to wrap structured arrays in astropy.table.Colum...
- `23:24:27` RESULT: Rewrote structured-array handling block in astropy/table/table.py
- `23:24:26` ACTION: python3 - <<'PY'
- `23:23:57` ACTION: sed -n '1,1400p' astropy/table/table.py | sed -n '1228,1252p' && sed -i '/if (not isinstance(data, C [...]
- `23:23:29` ACTION: nl -ba astropy/table/table.py | sed -n '1,120p'
- `23:23:24` ACTION: nl -ba astropy/table/table.py | sed -n '1200,1260p'
- `23:23:17` ACTION: grep -R "NdarrayMixin" -n || true
- `23:23:09` TASK STARTED: Consider removing auto-transform of structured column into NdarrayMixin
