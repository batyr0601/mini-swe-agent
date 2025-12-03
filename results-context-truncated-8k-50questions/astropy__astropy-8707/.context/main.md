# Project Goals

**Current Task:** Header.fromstring does not accept Python 3 bytes

<details>
<summary>Full description</summary>

Header.fromstring does not accept Python 3 bytes
According to [the docs](http://docs.astropy.org/en/stable/_modules/astropy/io/fits/header.html#Header.fromstring), the method `Header.fromstring` "...creates an HDU header from a byte string containing the entire header data."

By "byte string" here it really means the `str` type which on Python 2 could be raw binary data, but on Python 3 explicitly is not.   In fact it does work on Python 3's unicode `str`s, but here it assumes that the data can be ASCII-encoded.

Its counterpart, `Header.fromfile` will work with files opened in text or binary mode.  So probably the simplest solution for now (as opposed to adding new methods or something like that) is to change `Header.fromstring` to accept unicode or bytes string types.

`Card.fromst...
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

- [2025-12-03 03:10] **swebench-astropy__astropy-8707**: Task completed: Submitted
## Interaction Log

- `03:10:48` ACTION: Submitting solution
- `03:10:43` Repro: Header.fromstring with bytes: REPRO_OK 1
- `03:10:17` ACTION: python3 - <<'PY'
- `03:09:52` Found: Card.fromstring and Card._pad expect str; Header.fromstring must decode bytes/bytearray inputs (data and sep) to str (ascii) before using strin...
- `03:09:43` RESULT: case1: OK - Header len=1
case2: OK - Header len=1
case3: OK - Header len=1
- `03:09:33` ACTION: python3 - <<'PY'
- `03:09:08` ACTION: awk '/^def _pad/ {print; for(i=0;i<200;i++) { if(getline) print; else exit }}' astropy/io/fits/card. [...]
- `03:08:53` ACTION: sed -n '520,620p' astropy/io/fits/card.py
- `03:08:48` ACTION: grep -nR -E "^class\s+Card\b|def\s+fromstring\b" astropy/io/fits || true
- `03:08:36` ACTION: ln=$(grep -n "^class Card" astropy/io/fits/header.py | cut -d: -f1) && [ -n "$ln" ] && sed -n "${ln} [...]
- `03:08:19` ACTION: awk 'found && count-->0 {print} /^class Card/ {found=1; count=400; print}' astropy/io/fits/header.py
- `03:08:09` RESULT: sed: -e expression #1, char 1: unknown command: `,'
- `03:08:06` ACTION: ln=$(grep -n "^class Card" astropy/io/fits/header.py | cut -d: -f1) && sed -n "${ln},$((ln+300))p" a [...]
- `03:07:51` ACTION: grep -n "^class Card" astropy/io/fits/header.py && line=$(grep -n "^class Card" astropy/io/fits/head [...]
- `03:07:19` ACTION: sed -n '320,420p' astropy/io/fits/header.py
- `03:07:11` Found error source: Header.fromstring in astropy/io/fits/header.py; bytes input caused TypeError due to operations assuming str (e.g. ''.join and stri...
- `03:07:03` RESULT: method_replaced
IMPORT_OK: Header 1
