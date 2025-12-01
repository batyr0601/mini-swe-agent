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
- [ ] 1. Reproduce: create a small script that adds a structured np.array to a Table to show current auto-conversion behavior
- [ ] 2. Locate: search for
- [ ] 3. Analyze: inspect the logic to decide where to insert FutureWarning and what behavior to change
- [ ] 4. Implement fix: add a FutureWarning advising users to wrap data in Column and change conversion logic so structured arrays are not auto-viewed as NdarrayMixin (prepare for removal in 5.2)
- [ ] 5. Verify fix: run the reproduction script and check that structured ndarray is added as Column (or appropriate behavior) and warning is emitted

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:31] **swebench-astropy__astropy-13236**: Task completed: Submitted
## Interaction Log

- `19:31:23` ACTION: Submitting solution
- `19:31:17` Verified: wrapping structured ndarray in Column yields a Column and does not produce FutureWarning
- `19:31:09` Decision: Insert FutureWarning and preserve existing view-to-NdarrayMixin behavior for now; plan to remove auto-view in 5.2
- `19:31:09` Analysis: The auto-conversion occurs in Table.__setitem__ where structured ndarrays are viewed as NdarrayMixin; best approach is to emit a FutureWarni...
- `19:30:44` RESULT: /testbed/astropy/table/table.py:1246: FutureWarning: Structured ndarray with a compound dtype is currently being viewed as an NdarrayMixin. [....
- `19:30:44` Reproduced structured ndarray auto-conversion: FutureWarning emitted and column viewed as NdarrayMixin
- `19:30:42` ACTION: Reading file: reproduce_structured_table.py
- `19:30:27` Found structured ndarray auto-view at astropy/table/table.py:1246 - data.view(NdarrayMixin)
- `19:29:52` RESULT: (160 lines of output) First: 1	# Licensed under a 3-clause BSD style license - ...
- `19:29:52` ACTION: nl -ba astropy/table/table.py | sed -n '1,160p'
- `19:29:48` RESULT: (41 lines of output) First: 1220	                          if issubclass(self....
- `19:29:47` ACTION: nl -ba astropy/table/table.py | sed -n '1220,1260p'
- `19:29:43` RESULT: (30 lines of output) First: ./docs/io/ascii/ecsv.rst:247:- `astropy.table.Ndar...
- `19:29:43` ACTION: grep -RIn "NdarrayMixin" .
- `19:29:27` TASK STARTED: Consider removing auto-transform of structured column into NdarrayMixin
