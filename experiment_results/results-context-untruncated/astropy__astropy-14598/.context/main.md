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

- [2025-12-03 00:33] **swebench-astropy__astropy-14598**: Task completed: Submitted
## Interaction Log

- `00:33:33` ACTION: Submitting solution
- `00:33:10` Fix: removed per-fragment unescape; now join fragments and let parser handle \"''\" -> \"'\" conversion. Repro shows all cases equal.
- `00:33:01` ACTION: python3 repro.py
- `00:32:53` ACTION: python3 - <<'PY'
- `00:32:02` ACTION: Reading file: debug.py
- `00:30:01` ACTION: python3 - <<'PY'
- `00:29:23` ACTION: nl -ba astropy/io/fits/card.py | sed -n '720,820p'
- `00:29:07` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1260,1300p'
- `00:29:03` RESULT: 961:    def _format_value(self):
1270:def _format_value(value):
- `00:29:03` ACTION: grep -n "def _format_value" astropy/io/fits/card.py
- `00:28:54` ACTION: nl -ba astropy/io/fits/card.py | sed -n '980,1100p'
- `00:28:51` ACTION: grep -n "_format_image" astropy/io/fits/card.py
- `00:28:46` ACTION: grep -n --line-number "replace(\"''\"\\|replace(\"'\"\\|\"''\"\\|\"'\"'\" -n astropy/io/fits/card. [...]
- `00:28:18` repro.py: SyntaxError unexpected character after line continuation character at line 17
- `00:28:00` ACTION: Reading file: repro.py
- `00:27:44` RESULT: patched
- `00:27:44` ACTION: python3 - <<'PY'
- `00:27:39` RESULT: patched
- `00:27:39` ACTION: python3 - <<'PY'
