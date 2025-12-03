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
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `18:35:30` Found _format_float in astropy/io/fits/card.py at line 1300; it formats using value:.16G, ensures decimal point or exponent, normalizes exponent to tw...
- `18:35:10` ACTION: grep -n "def _format_float" astropy/io/fits/card.py && sed -n '1200,1360p' astropy/io/fits/card.py
- `18:34:43` ACTION: python3 - <<'PY'
- `18:34:22` Found _format_float in astropy/io/fits/card.py (~line 1300): uses f'{value:.16G}', normalizes exponent to two digits, then limits result to 20 chars (...
- `18:34:11` ACTION: grep -n "def _format_float" astropy/io/fits/card.py && lineno=$(grep -n "def _format_float" astropy/ [...]
- `18:33:29` ACTION: sed -n '1220,1320p' astropy/io/fits/card.py
- `18:33:25` ACTION: grep -nE "def .*(_float_to_str|format_float|_format_value|_value_to_str|_value_to_card|to_card|repr| [...]
- `18:33:07` ACTION: sed -n '920,1020p' astropy/io/fits/card.py && sed -n '1240,1310p' astropy/io/fits/card.py
- `18:33:03` RESULT: 956:    def _format_value(self):
1265:def _format_value(value):
- `18:33:03` ACTION: grep -nE "def (format_float|_format_value|_value_to_str|_float_to_str|_value_to_card|to_card)" astro [...]
- `18:32:47` ACTION: grep -nE "def .*format|format_float|_format_value|_value_to_str|to_card|float" astropy/io/fits/card. [...]
- `18:32:30` ACTION: grep -nE "def .*format|def .*float|def .*repr|format_float|_format_value|_value_to_str|to_card" astr [...]
- `18:32:18` ACTION: grep -nE "def .*format|def .*float|def .*repr|def .*to_card|format_float|_format_value|_value_to_str [...]
- `18:32:04` ACTION: grep -nE "def |float|format|repr" astropy/io/fits/card.py
- `18:31:50` ACTION: grep -nE "def |float|format|repr" astropy/io/fits/card. [...]
- `18:31:33` ACTION: grep -n "def " astropy/io/fits/card.py || true && sed -n '1,360p' astropy/io/fits/card.py
- `18:31:20` repro: Card value repr: 1.2345678901234567; Card string: "TEST    =    1.234567890123457 / a test float                                   "; Card stri...
- `18:31:07` ACTION: python3 - <<'PY'
- `18:30:53` ACTION: sed -n '1,400p' astropy/io/fits/card.py
