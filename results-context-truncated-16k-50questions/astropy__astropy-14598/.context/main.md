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

- [2025-12-02 23:28] **swebench-astropy__astropy-14598**: Task completed: Submitted
## Interaction Log

- `23:28:16` ACTION: Submitting solution
- `23:28:01` Reproduced bug with reproduce.py: trailing '' mismatches at n=65-69 and embedded '' mismatches for many n; inspected astropy/io/fits/card.py and found...
- `23:27:44` ACTION: PYTHONPATH=. python3 reproduce.py
- `23:27:38` RESULT: patched
- `23:27:05` ACTION: python3 - <<'PY'
- `23:26:47` ACTION: Reading file: reproduce.py
- `23:26:20` ACTION: nl -ba astropy/io/fits/card.py | sed -n '720,900p'
- `23:26:14` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1,200p' && nl -ba astropy/io/fits/card. [...]
- `23:26:00` ACTION: grep -nR --line-number -E "class Card|def fromstring|single quote|double quote|''|fromstring" astrop [...]
- `23:25:55` ACTION: ls -la
- `23:25:47` TASK STARTED: Inconsistency in double single-quote ('') management in FITS Card
