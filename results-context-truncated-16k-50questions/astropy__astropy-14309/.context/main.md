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

- [2025-12-02 23:25] **swebench-astropy__astropy-14309**: Task completed: Submitted
## Interaction Log

- `23:25:46` ACTION: Submitting solution
- `23:25:34` RESULT: ['ascii.ecsv']
- `23:25:32` ACTION: python3 - <<'PY'
- `23:25:21` Implemented fix: in astropy/io/fits/connect.py changed final return to 'isinstance(args[0], (...)) if args else False' to avoid IndexError
- `23:25:10` Root cause: is_fits in astropy/io/fits/connect.py accessed args[0] without checking if args was non-empty; when filepath is a non-FITS string and file...
- `23:24:49` Found culprit: is_fits in astropy/io/fits/connect.py accessed args[0] without checking args; patched to return False if args is empty
- `23:24:42` Updated is_fits to guard against empty args; identify_format('write', Table, 'bububu.ecsv', None, [], {}) now returns ['ascii.ecsv']
- `23:24:39` RESULT: ['ascii.ecsv']
- `23:24:37` ACTION: sed -i "72s/.*/ return isinstance(args[0], (HDUList, TableHDU, BinTableHDU, GroupsHDU)) if args else [...]
- `23:24:28` ACTION: python3 - <<'PY'
- `23:24:10` ACTION: nl -ba astropy/io/fits/connect.py | sed -n '60,80p'
- `23:24:03` ACTION: sed -i 's|return isinstance(args[0], (HDUList, TableHDU, BinTableHDU, GroupsHDU))|return isinstance( [...]
- `23:23:26` ACTION: nl -ba astropy/io/fits/connect.py | sed -n '1,240p'
- `23:23:20` ACTION: ls -la && ls -la testbed || true
- `23:23:09` TASK STARTED: IndexError: tuple index out of range in identify_format (io.registry)
