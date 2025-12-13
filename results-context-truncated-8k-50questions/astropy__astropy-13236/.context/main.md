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

- [2025-12-03 02:59] **swebench-astropy__astropy-13236**: Task completed: Submitted
## Interaction Log

- `02:59:39` ACTION: Submitting solution
- `02:59:33` Table(structured_ndarray) emits FutureWarning: Structured numpy arrays added to Table are currently automatically viewed as astropy.table.NdarrayMixin...
- `02:58:54` patched: inserted FutureWarning + data.view(NdarrayMixin) into astropy/table/table.py in _init_from_ndarray so Table(structured_ndarray) will emit the...
- `02:58:38` ACTION: python3 - <<'PY'
- `02:58:21` Root cause: Table(np.structured_array) uses _init_from_ndarray which splits the structured array into fields and then calls _init_from_list; thus _con...
- `02:57:56` ACTION: nl -ba astropy/table/table.py | sed -n '1204,1260p'
- `02:57:40` ACTION: nl -ba astropy/table/table.py | sed -n '1300,1370p'
- `02:57:28` ACTION: grep -n "def _init_from" astropy/table/table.py || true && grep -n "isinstance(data, np. [...]
- `02:57:12` ACTION: nl -ba astropy/table/table.py | sed -n '600,740p'
- `02:56:50` ACTION: grep -n "NdarrayMixin" astropy/table/table.py || true && grep -n "data\.view" astropy/table/table. [...]
- `02:56:35` ACTION: nl -ba astropy/table/table.py | sed -n '1140,1218p'
- `02:56:16` ACTION: nl -ba astropy/table/table.py | sed -n '1180,1240p'
- `02:56:12` RESULT: default captured warnings: 0
forced captured FutureWarning warnings: 0
- `02:56:01` ACTION: python3 - <<'PY'
- `02:55:50` Found auto-view of structured ndarray at astropy/table/table.py:1244-1248 (data.view(NdarrayMixin)); inserted FutureWarning before view to warn about ...
- `02:55:38` ACTION: nl -ba astropy/table/table.py | sed -n '1236,1250p'
- `02:55:32` Repro script Table(a): no FutureWarning emitted; output was 'DONE
- `02:55:24` RESULT: DONE
- `02:55:06` ACTION: python3 - <<'PY'
