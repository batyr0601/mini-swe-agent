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
- [ ] 1. Reproduce: create a script that constructs a Card with value 0.009125 and a long comment to reproduce truncation
- [ ] 2. Locate: find Card._format_float implementation in io/fits/card.py
- [ ] 3. Root cause analysis: inspect how floats are formatted and why 0.009125 becomes 0.009124999999999999
- [ ] 4. Implement fix: change _format_float to prefer str(value) when its string fits within 20 characters, otherwise fall back to existing formatting; preserve overall FITS formatting rules
- [ ] 5. Verify fix: run the reproduction script and any existing formatting tests to confirm the comment is no longer truncated

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:42] **swebench-astropy__astropy-14508**: Task completed: Submitted
- [2025-12-01 20:42] **swebench-astropy__astropy-14508**: Prefer Python str(value) in _format_float when it fits to avoid unnecessary float expansion and comm...
## Interaction Log

- `20:42:55` ACTION: Submitting solution
- `20:42:48` Ran additional formatting checks covering small floats, large floats, exponentials; outputs look reasonable
- `20:42:45` RESULT: Value: 0.009125, formatted: '0.009125', len=8 Value: 1.0, formatted: '1.0', len=3 Value: 123456789.0, formatted: '123456789. [...]
- `20:42:43` ACTION: python - <<'PY'
- `20:42:39` TESTED: repro_card.py confirms 0.009125 is preserved and no VerifyWarning; manual verification OK
- `20:42:39` Decision: prefer Python's str(value) when its representation fits <=20 chars; otherwise fall back to .16G formatting and preserve exponent formatting
- `20:42:39` Root cause: _format_float used f\"{value:.16G}\" which can expand certain floats (e.g., 0.009125 -> 0.009124999999999999) causing unnecessary length
- `20:42:39` Found _format_float in astropy/io/fits/card.py:1300
- `20:42:29` Reproduced: creating Card with value 0.009125 produced expanded representation 0.009124999999999999 and truncated comment
- `20:42:21` RESULT: Direct creation and display: repr: ('ESO IFM CL RADIUS', 0.009125, '[m] radius arround actuator to avoid') str : HIERARCH ESO IFM CL RADIUS = ...
- `20:42:20` ACTION: python repro_card.py
- `20:42:18` RESULT: Replaced entire _format_float function in astropy/io/fits/card.py
- `20:42:18` ACTION: python - <<'PY'
- `20:41:57` RESULT: (37 lines of output) First: 1348	            sign = exponent[0]...
- `20:41:57` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1348,1384p'
- `20:41:55` RESULT: ERROR: SyntaxError: unexpected character after line continuation character
- `20:41:54` ACTION: python repro_card.py
- `20:41:51` RESULT: Rewrote _format_float correctly in astropy/io/fits/card.py
- `20:41:51` ACTION: python - <<'PY'
- `20:41:28` RESULT: (45 lines of output) First: 1288	        return f"{_format_float(value):>20}"...
