# Project Goals

**Current Task:** `io.fits.Card` may use a string representation of floats that is larger than necessary

<details>
<summary>Full description</summary>

`io.fits.Card` may use a string representation of floats that is larger than necessary
### Description

In some scenarios, `io.fits.Card` may use a string representation of floats that is larger than necessary, which can force comments to be truncated. Due to this, there are some keyword/value/comment combinations that are impossible to create via `io.fits` even though they are entirely possible in FITS.

### Expected behavior

Being able to create any valid FITS Card via `io.fits.Card`.

### How to Reproduce

[This valid FITS file](https://github.com/astropy/astropy/files/10922976/test.fits.gz) contains the following card in the header:

`HIERARCH ESO IFM CL RADIUS = 0.009125 / [m] radius arround actuator to avoid`

We can read the header of this file and get this card without any iss...
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

- [2025-12-02 23:28] **swebench-astropy__astropy-14508**: Task completed: Submitted
## Interaction Log

- `23:28:39` ACTION: Submitting solution
- `23:28:34` verification: PASS actual: HIERARCH ESO IFM CL RADIUS = 0.009125 / [m] radius arround actuator to avoid    ; expected: HIERARCH ESO IFM CL RADIUS = 0....
- `23:28:02` Root cause analysis: using f\"{value:.16G}\" exposed the full binary float decimal expansion (e.g. 0.009124999999999999). Python's str(value) returns ...
- `23:27:45` Implemented fix: modified _format_float to try Python str(value) before using .16G formatting; kept fallback and exponent normalization
- `23:27:30` Found root cause: _format_float in astropy/io/fits/card.py produced oversized float strings (e.g. 0.009124999999999999). Patch: prefer Python str(valu...
- `23:27:15` repro test: repr: ('ESO IFM CL RADIUS', 0.009125, '[m] radius arround actuator to avoid') ; str: HIERARCH ESO IFM CL RADIUS = 0.009125 / [m] radius ar...
- `23:26:55` ACTION: python3 - <<'PY'
- `23:26:46` ACTION: sed -i 's/\\\"\\\"\\\"/"""/g' astropy/io/fits/card.py
- `23:26:34` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1288,1336p'
- `23:26:15` ACTION: python3 - <<'PY'
- `23:26:04` Patched _format_float in astropy/io/fits/card.py to prefer str(value) when it fits within 20 chars; fallback to .16G formatting retained
- `23:25:58` RESULT: Patched _format_float in astropy/io/fits/card.py
- `23:25:58` ACTION: python3 - <<'PY'
- `23:25:22` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1200,1360p'
- `23:25:19` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1,240p'
- `23:25:14` ACTION: ls -la
- `23:25:03` TASK STARTED: `io.fits.Card` may use a string representation of floats that is larger than necessary
