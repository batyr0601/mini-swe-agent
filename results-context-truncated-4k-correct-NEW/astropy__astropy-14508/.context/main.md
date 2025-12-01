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

- [2025-12-02 11:53] **swebench-astropy__astropy-14508**: Task completed: Submitted
## Interaction Log

- `11:53:30` ACTION: Submitting solution
- `11:53:16` ACTION: git log -p -1 -- astropy/io/fits/card.py
- `11:53:05` ACTION: git status --porcelain=2 -b && echo "=== STAGED DIFF (git diff --cached) ===" && git --no-pager diff [...]
- `11:52:45` ACTION: git --no-pager diff --cached -- astropy/io/fits/card.py
- `11:52:27` repro: 1.234567890123457
- `11:52:12` ACTION: Submitting solution
- `11:51:56` Replaced f"{value:.15G}" with f"{value:.16G}" in astropy/io/fits/card.py
- `11:51:39` ACTION: python3 - <<'PY' && sed -n '1296,1310p' astropy/io/fits/card.py
- `11:51:14` ACTION: grep -nR --line-number -E "\\.15G|\\.16G" .
- `11:50:32` ACTION: sed -n '1200,1360p' astropy/io/fits/card.py
- `11:50:10` ACTION: python3 - <<'PY'
- `11:49:36` ACTION: sed -n '1320,1400p' astropy/io/fits/card.py
- `11:49:30` ACTION: sed -n '1200,1320p' astropy/io/fits/card.py
- `11:49:14` ACTION: Reading file: 50
- `11:49:00` Found _format_float: uses f\"{value:.16G}\"; if no '.' and no 'E' appends '.0'; if 'E' present it splits on 'E', preserves sign, and rebuilds as f\"{s...
- `11:48:48` ACTION: sed -n '1260,1320p' astropy/io/fits/card.py
- `11:48:37` _format locations: _int_or_float at 1246; _format_value at 1265 with float branch at 1287-1289; _format_float at 1300 with exponent normalization at 1...
- `11:48:29` ACTION: grep -nE "value_to_card|value_to_string|_format|format_float|%f|%g|exponent|E-?\\d+|repr|float" astr [...]
- `11:48:23` repro: INPUT repr 0.1 -> Card str 'TEST    =                  0.1' ; 1.2345678901234567 -> Card str 'TEST    =    1.234567890123457' ; 1.2e-10 -> Card...
- `11:48:14` ACTION: python3 - <<'PY'
