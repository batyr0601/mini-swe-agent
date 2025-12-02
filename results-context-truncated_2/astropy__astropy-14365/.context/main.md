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
- [ ] 1. Understand the bug: reproduce behavior with lowercase QDP command
- [ ] 2. Locate the code: find file implementing ascii.qdp reader (search repository for
- [ ] 3. Root cause analysis: inspect parsing logic to see where commands are expected uppercase and determine how to make comparisons case-insensitive
- [ ] 4. Implement fix: modify parser to accept commands case-insensitively (e.g., normalize command tokens with .upper() or .lower()) and update code accordingly
- [ ] 5. Verify fix: create a test.qdp with

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:42] **swebench-astropy__astropy-14365**: Task completed: Submitted
- [2025-12-01 20:42] **swebench-astropy__astropy-14365**: Make QDP command parsing case-insensitive and make NO check case-insensitive
## Interaction Log

- `20:42:25` ACTION: Submitting solution
- `20:42:20` test.qdp read: Table.read succeeded. Colnames: ['col1', 'col1_err', 'col2', 'col2_err']
- `20:42:20` qdp.py: changed NO check to v.strip().upper() == \"NO\
- `20:42:20` qdp.py: changed _line_type_re to compile with re.IGNORECASE
- `20:42:09` ACTION: sed -i 's/_line_type_re = re.compile(_type_re)/_line_type_re = re.compile(_type_re, re. [...]
- `20:41:53` ACTION: grep -n -e "_line_type_re" -e "re.IGNORECASE" -e "strip(). [...]
- `20:41:43` ACTION: grep -n "re.IGNORECASE" astropy/io/ascii/qdp.py && grep -n "strip().upper()" astropy/io/ascii/qdp. [...]
- `20:40:59` qdp.py: _line_type uses _command_re = 'READ [TS]ERR...' and compiles without re.IGNORECASE; will change to compile with re.IGNORECASE to accept lowerc...
- `20:40:52` ACTION: nl -ba astropy/io/ascii/qdp.py | sed -n '1,420p'
- `20:40:47` ACTION: grep -RIn "qdp" . || true
- `20:40:32` TASK STARTED: ascii.qdp Table format assumes QDP commands are upper case
