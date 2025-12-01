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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 11:56] **swebench-astropy__astropy-14365**: Task completed: LimitsExceeded
## Interaction Log

- `11:56:35` ACTION: cp astropy/io/ascii/qdp.py astropy/io/ascii/qdp.py.bak && perl -0777 -pe 's/re\. [...]
- `11:56:10` ACTION: sed -n '1,140p' astropy/io/ascii/qdp.py
- `11:56:04` ACTION: grep -n "Unrecognized QDP line" astropy/io/ascii/qdp.py || true
- `11:55:44` ACTION: grep -n "Unrecognized QDP line" astropy/io/ascii/qdp. [...]
- `11:55:38` repro: ascii.read(format="qdp") with lower-case QDP commands raised ValueError: Unrecognized QDP line: title "Example with lower-case commands
- `11:55:27` ACTION: python3 - <<'PY'
- `11:55:07` ACTION: grep -n "Unrecognized QDP line" astropy/io/ascii/qdp. [...]
- `11:54:57` ACTION: python3 - <<'PY'
- `11:54:27` ACTION: grep -n -E "upper|isupper" astropy/io/ascii/qdp.py || true && sed -n '1,400p' astropy/io/ascii/qdp. [...]
- `11:54:07` ACTION: sed -n '1,240p' astropy/io/ascii/qdp.py
- `11:53:50` repro: get_lines initial TypeError: read() should return bytes; then TypeError: Input "table" must be a string (filename or data) or an iterable
- `11:53:32` ACTION: python3 - <<'PY'
- `11:53:21` ACTION: Reading file: <<'PY'
- `11:52:58` ACTION: sed -n '1,160p' astropy/io/ascii/qdp.py
- `11:52:51` ACTION: Reading file: <<'EOF'
- `11:52:31` ACTION: sed -n '1,400p' astropy/io/ascii/qdp.py
- `11:52:16` ACTION: grep -n "upper(" astropy/io/ascii/qdp.py || true && sed -n '1,400p' astropy/io/ascii/qdp.py
- `11:51:27` ACTION: sed -n '1,400p' astropy/io/ascii/qdp.py
- `11:51:14` ACTION: sed -n '1,240p' astropy/io/ascii/qdp.py
- `11:51:02` ACTION: sed -n '1,240p' astropy/io/ascii/qdp.py && sed -n '241,480p' astropy/io/ascii/qdp.py
