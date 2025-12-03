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

- [2025-12-03 00:27] **swebench-astropy__astropy-14365**: Task completed: Submitted
## Interaction Log

- `00:27:11` ACTION: Submitting solution
- `00:27:06` Final verification: test.qdp read OK; FINAL_VERIFICATION_OK ['col1', 'col1_err', 'col2', 'col2_err']
- `00:26:43` Change implemented: astropy/io/ascii/qdp.py line 63 _command_re changed to case-insensitive '(?i:READ [TS]ERR(\\s+[0-9]+)+)
- `00:26:35` ACTION: python - <<'PY'
- `00:26:14` Root cause: _command_re was case-sensitive (only matched uppercase 'READ SERR'), causing lowercase commands like 'read serr' to be unrecognized; chang...
- `00:26:02` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '60,76p'
- `00:25:49` astropy/io/ascii/qdp.py:63 _command_re set to r\"(?i:READ [TS]ERR(\\s+[0-9]+)+)\"; case-insensitive command matching added
- `00:25:44` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '60,90p'
- `00:25:39` Repro: test.qdp read OK; output: READ_OK; colnames: ['col1', 'col1_err', 'col2', 'col2_err']
- `00:25:26` ACTION: printf '%s\n' "read serr 1 2 " "1 0.5 1 0.5" > test.qdp && python - <<'PY'
- `00:25:09` RESULT: patched
- `00:25:08` ACTION: python - <<'PY'
- `00:24:47` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '1,260p'
- `00:24:43` ACTION: grep -nR "qdp" astropy | sed -n '1,200p'
- `00:24:38` ACTION: ls -la
- `00:24:30` TASK STARTED: ascii.qdp Table format assumes QDP commands are upper case
