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
- [x] 1. Understand the bug: reproduce adding a structured numpy.ndarray to a Table and confirm it gets viewed as NdarrayMixin
- [ ] 2. Locate the code: search repository for occurrences of
- [ ] 3. Implement warning: add a FutureWarning at that location informing users to wrap data in Column and that behavior will change in 5.2
- [ ] 4. Preserve current behavior for now: keep the automatic view(NdarrayMixin) behavior while adding the warning so behavior remains backwards compatible
- [ ] 5. Create a small repro script to validate the warning is emitted and the structured array is still handled; check class/type of the stored column
- [ ] 6. Run tests/smoke: run the repro and any nearby tests; log results and then mark TODOs complete and commit changes

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:42] **swebench-astropy__astropy-13236**: Task completed: Submitted
## Interaction Log

- `19:42:05` ACTION: Submitting solution
- `19:41:58` ACTION: git add -A && git commit -m "table: warn about structured ndarray auto-conversion to NdarrayMixin; a [...]
- `19:41:56` repro_structured.py run: FutureWarning at astropy/table/table.py:1246; Column repr: NdarrayMixin([(1, 2.), (3, 4.)], dtype=[('a', '<i4'), ('b', '<f8')...
- `19:41:45` ACTION: python3 repro_structured.py
- `19:41:35` Preserved behavior: inserted FutureWarning but left data.view(NdarrayMixin) intact at astropy/table/table.py:1246
- `19:41:26` repro_structured.py: FutureWarning at astropy/table/table.py:1246; Column repr: NdarrayMixin([(1, 2.), (3, 4.)], dtype=[('a', '<i4'), ('b', '<f8')]); ...
- `19:41:11` ACTION: Reading file: repro_structured.py
- `19:40:58` astropy/table/table.py:1238-1248: inserted FutureWarning before data.view(NdarrayMixin)
- `19:40:47` ACTION: nl -ba astropy/table/table.py | sed -n '1238,1248p'
- `19:40:42` ACTION: sed -i '/data = data.view(NdarrayMixin)/i\ warnings.warn("Adding a structured numpy. [...]
- `19:40:29` ACTION: nl -ba astropy/table/table.py | sed -n '1,80p'
- `19:40:22` ACTION: nl -ba astropy/table/table.py | sed -n '1210,1260p'
- `19:40:17` ACTION: grep -nR -e "view(NdarrayMixin)" -e "NdarrayMixin" -e "Structured ndarray gets viewed as a mixin" . [...]
- `19:40:14` grep testbed: No such file or directory; will search repo root for NdarrayMixin and view(NdarrayMixin)
- `19:40:07` RESULT: grep: testbed: No such file or directory
- `19:40:07` ACTION: grep -nR -e "view(NdarrayMixin)" -e "Structured ndarray gets viewed as a mixin" -e "NdarrayMixin" te [...]
- `19:39:45` TASK STARTED: Consider removing auto-transform of structured column into NdarrayMixin
