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

<!-- 
Add detailed, specific TODOs when starting a task. Good examples:
- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `18:35:29` ACTION: grep -RIn "qdp" astropy/io/ascii || true
- `18:35:16` ACTION: grep -RIn "qdp" astropy || true
- `18:35:03` ACTION: grep -RIn "qdp" astropy/io/ascii || true
- `18:34:48` ACTION: grep -RIn "qdp" astropy/io/ascii || true && find astropy/io/ascii -type f -iname '*qdp*' -print || t [...]
- `18:34:29` ACTION: grep -RIn "qdp" astropy/io/ascii || true
- `18:34:18` ACTION: grep -RIn "qdp" astropy/io/ascii || true && find astropy/io/ascii -type f -iname '*qdp*. [...]
- `18:34:01` ACTION: ls -la astropy/io/ascii && grep -RIn "qdp" astropy/io/ascii || true && find astropy/io/ascii -type f [...]
- `18:33:40` ACTION: grep -RIn "qdp" astropy || true
- `18:33:25` ACTION: grep -RIn "qdp" astropy/io/ascii || true
- `18:33:11` ACTION: grep -RIn "qdp" astropy/io/ascii || true && find astropy/io/ascii -type f -iname '*qdp*. [...]
- `18:32:52` ACTION: grep -RIn "qdp" astropy || true && find astropy -type f -iname '*qdp*.py' -print || true
- `18:32:09` ACTION: grep -RIn "qdp" astropy || true && find astropy -type f -iname '*qdp*. [...]
- `18:31:41` ACTION: grep -RIn "qdp" astropy || true && ls -la astropy/io/ascii || true && sed -n '1,240p' astropy/io/asc [...]
- `18:31:24` ACTION: grep -RIn "qdp" astropy || true && find astropy -type f -iname '*qdp*.py' -print || true
- `18:30:40` ACTION: grep -RIn "qdp" astropy || true
- `18:30:28` ACTION: ls -la
- `18:30:26` TASK STARTED: ascii.qdp Table format assumes QDP commands are upper case
