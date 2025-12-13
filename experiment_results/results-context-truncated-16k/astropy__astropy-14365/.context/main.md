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

- [2025-12-02 23:26] **swebench-astropy__astropy-14365**: Task completed: Submitted
## Interaction Log

- `23:26:52` ACTION: Submitting solution
- `23:26:46` verification: READ_OK on test.qdp; lowercase QDP commands are now accepted
- `23:26:40` ACTION: python3 - <<'PY'
- `23:26:32` Patched astropy/io/ascii/qdp.py: compile _type_re with re.IGNORECASE to accept case-insensitive QDP commands
- `23:26:23` ACTION: sed -i 's/re.compile(_type_re)/re.compile(_type_re, re.IGNORECASE)/' astropy/io/ascii/qdp. [...]
- `23:26:00` Root cause: _line_type uses re.compile(_type_re) without re.IGNORECASE; commands like 'read serr' don't match. Plan: compile regex with re.IGNORECASE ...
- `23:25:51` Found _line_type in astropy/io/ascii/qdp.py: command regex _command_re = r\"READ [TS]ERR(\\s+[0-9]+)+\" compiled without re.IGNORECASE; causes lowerca...
- `23:25:40` repro: ValueError Unrecognized QDP line: read serr 1 2
- `23:25:24` ACTION: Reading file: <<'EOF'
- `23:25:06` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '1,480p'
- `23:24:51` ACTION: grep -RIn "qdp" .
- `23:24:44` TASK STARTED: ascii.qdp Table format assumes QDP commands are upper case
