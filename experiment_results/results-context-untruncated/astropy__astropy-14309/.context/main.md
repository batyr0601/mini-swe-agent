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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:24] **swebench-astropy__astropy-14309**: Task completed: Submitted
## Interaction Log

- `00:24:45` ACTION: Submitting solution
- `00:24:40` Root cause: is_fits accessed args[0] without checking args length causing IndexError when no extra positional args; fix: guard access with len(args) >...
- `00:24:40` identify_format('write', Table, 'bububu.ecsv', None, [], {}) returned: ['ascii.ecsv']
- `00:24:31` RESULT: identify_format returned: ['ascii.ecsv']
- `00:24:29` ACTION: python3 - <<'PY'
- `00:24:21` astropy/io/fits/connect.py:72: replaced 'return isinstance(args[0], (HDUList, TableHDU, BinTableHDU, GroupsHDU))' with 'return len(args) > 0 and isins...
- `00:24:06` ACTION: sed -i 's/return isinstance(args\[0\], (HDUList, TableHDU, BinTableHDU, GroupsHDU))/return len(args) [...]
- `00:23:33` ACTION: nl -ba astropy/io/fits/connect.py | sed -n '1,220p'
- `00:23:30` ACTION: grep -n "def is_fits" -R astropy | sed -n '1,200p'
- `00:23:22` ACTION: ls -la
- `00:23:19` TASK STARTED: IndexError: tuple index out of range in identify_format (io.registry)
