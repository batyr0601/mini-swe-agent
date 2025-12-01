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
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:10] **swebench-astropy__astropy-14508**: Task completed: Submitted
## Interaction Log

- `03:10:35` ACTION: Submitting solution
- `03:10:30` Verification passed: repro output: repr: ('ESO IFM CL RADIUS', 0.009125, '[m] radius arround actuator to avoid'); str: HIERARCH ESO IFM CL RADIUS = 0....
- `03:10:05` ACTION: python3 repro.py
- `03:09:57` Observed: f\"{val:.16G}\": 0.009124999999999999; repr(val): 0.009125; str(val): 0.009125. Root cause: _format_float used f\"{value:.16G}\" which can p...
- `03:09:46` ACTION: python3 - <<'PY'
- `03:09:33` Found _format_float in astropy/io/fits/card.py: defined at line 1300; used at lines 1288 and 1291 in _format_value
- `03:09:09` ACTION: grep -n "_format_float" astropy/io/fits/card.py
- `03:08:57` ACTION: nl -ba astropy/io/fits/card.py | sed -n '200,240p'
- `03:08:49` RESULT: 41:class Card(_Verify):
209:    def __repr__(self):
212:    def __str__(self):
- `03:08:48` ACTION: grep -nE "class Card|def __str__|def __repr__" astropy/io/fits/card.py
- `03:08:30` Patched astropy/io/fits/card.py:_format_float to use repr(); repro output now: repr: ('ESO IFM CL RADIUS', 0.009125, '[m] radius arround actuator to a...
- `03:08:09` ACTION: python3 - <<'PY' && nl -ba astropy/io/fits/card.py | sed -n '1296,1332p' && python3 repro.py
- `03:07:49` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1240,1310p'
- `03:07:31` ACTION: grep -n "def _format_float" astropy/io/fits/card.py && grep -nR "_format_float" || true
- `03:05:05` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1296,1332p' && python3 repro.py
- `03:04:25` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1240,1310p'
- `03:04:06` ACTION: grep -n "_format_float" astropy/io/fits/card.py && nl -ba astropy/io/fits/card. [...]
- `03:03:58` repro.py: repr: ('ESO IFM CL RADIUS', 0.009125, '[m] radius arround actuator to avoid'); str: 'HIERARCH ESO IFM CL RADIUS = 0.009124999999999999 / [m]...
