# Project Goals

**Current Task:** IndexError: tuple index out of range in identify_format (io.registry)

<details>
<summary>Full description</summary>

IndexError: tuple index out of range in identify_format (io.registry)
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
pip install...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: run minimal script calling identify_format(
- [ ] 2. Locate the code: find is_fits in astropy/io/fits/connect.py and identify_format in astropy/io/registry/base.py
- [ ] 3. Root cause analysis: inspect is_fits signature and how args/fileobj are passed to identify why args is empty when filepath is string without FITS extension
- [ ] 4. Implement fix: update is_fits to safely check args length before accessing args[0] and return False if not present (so it won
- [ ] 5. Verify fix: run reproduction script and ensure identify_format no longer raises IndexError and returns appropriate formats

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 19:41] **swebench-astropy__astropy-14309**: Task completed: Submitted
## Interaction Log

- `19:41:31` ACTION: Submitting solution
- `19:41:26` patched astropy/io/fits/connect.py: replaced unconditional 'return isinstance(args[0], ...)' with guarded check 'if args: return isinstance(args[0], ....
- `19:41:14` RESULT: patched
Calling identify_format...
['ascii.ecsv']
- `19:41:13` ACTION: python3 - <<'PY'
- `19:40:50` repro_identify.py: calling identify_format('write', Table, 'bububu.ecsv', None, [], {}) raises IndexError: tuple index out of range at astropy/io/fits...
- `19:40:42` ACTION: Reading file: repro_identify.py
- `19:40:32` is_fits: astropy/io/fits/connect.py:48; returns isinstance(args[0], (HDUList, TableHDU, BinTableHDU, GroupsHDU)) at line 72
- `19:40:22` ACTION: nl -ba astropy/io/registry/base.py | sed -n '1,260p'
- `19:40:18` ACTION: nl -ba astropy/io/fits/connect.py | sed -n '1,200p'
- `19:40:13` ACTION: grep -nR "def is_fits" astropy || true
- `19:40:10` ACTION: ls -la
- `19:40:08` grep is_fits: grep: testbed: No such file or directory
- `19:40:02` RESULT: grep: testbed: No such file or directory
- `19:40:01` ACTION: grep -nR "is_fits" testbed || true
- `19:39:46` TASK STARTED: IndexError: tuple index out of range in identify_format (io.registry)
