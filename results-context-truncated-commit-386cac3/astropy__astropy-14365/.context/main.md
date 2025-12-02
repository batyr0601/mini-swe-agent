# Project Goals

**Current Task:** ascii.qdp Table format assumes QDP commands are upper case

<details>
<summary>Full description</summary>

ascii.qdp Table format assumes QDP commands are upper case
### Description

ascii.qdp assumes that commands in a QDP file are upper case, for example, for errors they must be "READ SERR 1 2" whereas QDP itself is not case sensitive and case use "read serr 1 2". 

As many QDP files are created by hand, the expectation that all commands be all-caps should be removed.

### Expected behavior

The following qdp file should read into a `Table` with errors, rather than crashing.
```
read serr 1 2 
1 0.5 1 0.5
```

### How to Reproduce

Create a QDP file:
```
> cat > test.qdp
read serr 1 2 
1 0.5 1 0.5
<EOF>

 > python
Python 3.10.9 (main, Dec  7 2022, 02:03:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ...
</details>


## TODO List

- [ ] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: reproduce reading a qdp file with lowercase commands (e.g.,
- [ ] 2. Locate the code: find the ascii.qdp reader implementation file(s) (likely under astropy/io/ascii or similar) in the testbed repo
- [ ] 3. Root cause analysis: inspect the QDP parser to see where commands are matched and why matching is case-sensitive
- [ ] 4. Implement fix: modify parser to normalize QDP commands (e.g., upper() or lower()) before matching so commands become case-insensitive
- [ ] 5. Verify fix: create a test.qdp with lowercase

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:42] **swebench-astropy__astropy-14365**: Task completed: Submitted
## Interaction Log

- `20:42:00` ACTION: Submitting solution
- `20:41:54` RESULT: WARNING: table_id not specified. Reading the first available table [astropy.io.ascii. [...]
- `20:41:53` ACTION: python - <<'PY'
- `20:41:37` Reproducing: read qdp with lowercase commands
- `20:41:18` TESTED: _line_type recognizes lowercase command 'read serr 1 2
- `20:40:57` Decision: use re.IGNORECASE to make QDP command matching case-insensitive
- `20:40:57` Found issue: _line_type regex compiled without IGNORECASE causing commands like 'read serr' to be unrecognized
- `20:40:34` RESULT: (31 lines of output) First: 60	    ValueError: Unrecognized QDP line......
- `20:40:33` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '60,90p'
- `20:40:27` RESULT: (480 lines of output) First: 1	# Licensed under a 3-clause BSD style license - ...
- `20:40:25` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '1,480p'
- `20:40:21` RESULT: (55 lines of output) First: astropy/io/ascii/tests/test_qdp.py:5:from astropy....
- `20:40:19` ACTION: grep -RIn "qdp" astropy | sed -n '1,200p'
- `20:40:03` TASK STARTED: ascii.qdp Table format assumes QDP commands are upper case
