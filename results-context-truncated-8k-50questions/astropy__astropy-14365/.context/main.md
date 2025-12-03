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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 02:59] **swebench-astropy__astropy-14365**: Task completed: Submitted
## Interaction Log

- `02:59:27` ACTION: Submitting solution
- `02:59:22` repro_qdp.py verification: _line_type('read serr 1 2') returned: command (lowercase QDP commands now recognized)
- `02:59:15` Implemented fix: changed re.compile(_type_re) to re.compile(_type_re, re.IGNORECASE) in astropy/io/ascii/qdp.py (confirmed at line 71)
- `02:58:59` astropy/io/ascii/qdp.py lines 62-71: _command_re = r"READ [TS]ERR(\s+[0-9]+)+"; _line_type_re = re.compile(_type_re, re.IGNORECASE) (confirmed at line...
- `02:58:42` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '60,76p'
- `02:58:33` repro_qdp.py: _line_type('read serr 1 2') returned: command
- `02:58:28` RESULT: command
- `02:58:13` ACTION: Reading file: <<'PY'
- `02:58:04` Replaced re.compile(_type_re) with re.compile(_type_re, re.IGNORECASE); _line_type('read serr 1 2') returned: command
- `02:57:56` RESULT: command
- `02:57:33` ACTION: sed -i "s/re.compile(_type_re)/re.compile(_type_re, re.IGNORECASE)/" astropy/io/ascii/qdp. [...]
- `02:57:15` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '1,240p'
- `02:57:04` ACTION: grep -RIn "ascii.qdp" . || true
- `02:57:01` RESULT: grep: testbed: No such file or directory
- `02:56:51` ACTION: grep -RIn "qdp" testbed || true
- `02:56:41` TASK STARTED: ascii.qdp Table format assumes QDP commands are upper case
