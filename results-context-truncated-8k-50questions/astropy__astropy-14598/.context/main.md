# Project Goals

**Current Task:** Inconsistency in double single-quote ('') management in FITS Card

<details>
<summary>Full description</summary>

Inconsistency in double single-quote ('') management in FITS Card
### Description

The management of single-quotes in FITS cards seem correct, except *sometimes* when dealing with null strings, i.e. double single quotes (`''`), which sometimes are transformed into single single quotes (`'`).

E.g.:
```python
In [39]: from astropy.io import fits
In [40]: for n in range(60, 70):
    ...:     card1 = fits.Card('CONFIG', "x" * n + "''")
    ...:     card2 = fits.Card.fromstring(str(card1))  # Should be the same as card1
    ...:     print(n, card1.value == card2.value)
    ...:     if card1.value != card2.value:
    ...:         print(card1.value)
    ...:         print(card2.value)
```
gives
```
60 True
61 True
62 True
63 True
64 True
65 False
xxxxxxxxxxxxxxxxxxxxxxxxxx...
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

- [2025-12-03 03:04] **swebench-astropy__astropy-14598**: Task completed: Submitted
## Interaction Log

- `03:04:21` ACTION: Submitting solution
- `03:04:15` Patched astropy/io/fits/card.py around line 835: replaced undoubling replace with rstrip
- `03:04:15` Fix implemented: preserve doubled quotes by using (m.group(\"strg\") or \"\").rstrip() in Card._split
- `03:04:15` Found root cause: Card._split in astropy/io/fits/card.py used .replace(\"''\",\"'\") which undoubles doubled single-quotes
- `03:04:15` repro.py: wrote repro.fits and read header; original and readback identical, equal: True
- `03:03:41` ACTION: perl -0777 -i -pe 's/^\Qvalue = (m.group("strg") or "").rstrip()\E/ value = (m.group("strg") or ""). [...]
- `03:03:19` ACTION: sed -n '820,900p' astropy/io/fits/card.py
- `03:03:05` ACTION: awk '{
- `03:02:15` ACTION: sed -n '1,120p' astropy/io/fits/card.py
- `03:02:04` ACTION: grep -n "_strg_comment_RE" -n astropy/io/fits/card.py && sed -n '1,220p' astropy/io/fits/card. [...]
- `03:01:55` ACTION: grep -n "replace(\"''\",\"'\"" astropy/io/fits/card.py || true && grep -n "re. [...]
- `03:01:31` ACTION: Reading file: repro.py
- `03:01:13` ACTION: Reading file: <<'PY'
- `03:00:45` RESULT: 861:                value = m.group("strg") or ""
- `03:00:42` ACTION: grep -n "value = m.group(\"strg\") or \"\"" astropy/io/fits/card.py
- `03:00:18` ACTION: sed -n '930,1020p' astropy/io/fits/card.py && sed -n '1240,1300p' astropy/io/fits/card.py
- `03:00:10` ACTION: grep -n "def _format_value" astropy/io/fits/card.py && sed -n '1,220p' astropy/io/fits/card. [...]
- `02:59:53` ACTION: sed -n '760,1200p' astropy/io/fits/card.py
- `02:59:37` ACTION: sed -n '520,760p' astropy/io/fits/card.py
- `02:59:26` ACTION: egrep -nR "class Card|fromstring\\(|Card\\.fromstring|Card\\(" astropy || true
