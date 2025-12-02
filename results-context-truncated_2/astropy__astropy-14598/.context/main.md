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
- [x] 1. Reproduce bug using the PR reproducer script to observe when
- [ ] 2. Locate Card class and Card.fromstring/str handling in source (search for
- [ ] 3. Inspect code handling single-quote escaping/unescaping and FITS card wrapping/truncation logic
- [ ] 4. Implement fix to preserve empty quoted strings (
- [ ] 5. Add reproducer script and run it to verify the fix; run test suite for regressions
- [ ] 1. Understand the bug: observe when Card.fromstring loses a trailing single quote in string values containing two single quotes
- [ ] 2. Locate serialization code: inspect _format_long_image and CONTINUE handling in astropy/io/fits/card.py
- [ ] 3. Root cause analysis: examine how quotes are handled during wrapping and CONTINUE card generation
- [ ] 4. Implement fix: modify _format_long_image to not collapse adjacent quotes when breaking strings across CONTINUE cards
- [ ] 5. Verify fix: run repro.py to ensure round-trip preserves
- [ ] 1. Reproduce the VerifyError for n=65 and capture detailed formatting diagnostics (str(card), _format_long_image, words from _words_group, headstr+value lengths, and padded chunk lengths)
- [ ] 2. Locate the code: inspect Card._format_long_image, _words_group usage, Card._itersubcards, and any places that manipulate quotes or pad card images (astropy/io/fits/card.py around lines 1040-1100 and 1200-1260)
- [ ] 3. Root cause analysis: determine why output length is not a multiple of 80 and why an extra single-quote chunk is produced (is escaping done before/after splitting, is padding/truncation misapplied?)
- [ ] 4. Implement fix: modify _format_long_image to produce exact 80-byte CONTINUE card images (escape appropriately and ensure no per-chunk escaping increases chunk length; ensure output pieces are exactly 80 bytes and no stray remainder is returned)
- [ ] 5. Verify fix: run repro.py for trailing and embedded cases, run any related unit tests, and log results; mark TODOs complete when verified
- [ ] 2. Reproduce _strg_comment_RE behavior for CONTINUE subcards: generate the two 80-byte subcard images for n=65 case and run re.match to log m.group(
- [ ] 3. Inspect Card.fromstring and _parse_value to determine whether subcard parsing already unescapes doubled quotes before _split is used
- [ ] 4. Implement fix: modify _split reconstruction to unescape concatenated escaped words exactly once without collapsing adjacent quotes incorrectly (consider using a re-based unescape or operating on the raw escaped image instead of per-piece replace)
- [ ] 5. Verify fix: run repro.py for trailing and embedded cases and run FITS header unit tests; log results and mark TODOs complete as appropriate
- [ ] 6. Reproduce failing test: create Header(), append((
- [ ] 7. Inspect Card._split commentary branch: review code around lines 840-876 to determine why commentary keywords return quoted valuecomment and what the expected behavior is
- [ ] 8. Implement fix: modify _split to return the raw unquoted concatenated value for commentary keywords (remove surrounding quotes and trailing
- [ ] 9. Verify fix: run pytest astropy/io/fits/tests/test_header.py::TestHeaderFunctions::test_long_commentary_card_appended_to_header and re-run card-related tests
- [ ] 1. Investigate NameError in _check_if_rvkc: undefined
- [ ] 2. Ensure len(args)==2 branch always returns by inserting an indented
- [ ] 3. Compile and run test_long_commentary_card_appended_to_header to verify fix
- [ ] 1. Locate _split method in astropy/io/fits/card.py
- [ ] 2. If _split is missing, search the repo for a previous definition to restore
- [ ] 3. Restore _split in card.py and run test_long_commentary_card_appended_to_header to verify
- [ ] 4. Patch Card._split fallback to format booleans as FITS
- [x] 1. Review edits to astropy/io/fits/card.py (inspect git diff)
- [x] 2. Run astropy/io/fits/tests/test_header.py to ensure no other header regressions
- [x] 1. Revert astropy/io/fits/card.py to git HEAD to restore missing methods (_parse_keyword, etc.)
- [x] 2. Insert Card._split if missing (insert before _fix_keyword) without modifying other methods
- [x] 3. Run pytest on astropy/io/fits/tests/test_header.py to verify header tests
- [x] 1. Locate Card.fromstring and Card._format_long_image in astropy/io/fits sources
- [x] 2. Inspect Card.fromstring, _format_long_image, _words_group, and _itersubcards implementations for quote/CONTINUE handling
- [x] 1. Reproduce splitting behavior for values with adjacent single quotes near chunk boundaries (n≈64-67); gather _words_group, _format_long_image, and _itersubcards outputs
- [ ] 2. Inspect how quotes are escaped/unescaped across CONTINUE pieces to identify collapsing/duplication issues
- [ ] 1. Inspect Card.fromstring parsing of first 80-byte chunk for len64_post

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:16] **swebench-astropy__astropy-14598**: Task completed: LimitsExceeded
- [2025-12-01 21:01] **swebench-astropy__astropy-14598**: Fix Card CONTINUE parsing: remove premature unescape in Card._split to avoid double-unescaping of do...
## Interaction Log

- `21:16:54` Card.fromstring on len64_post'' CHUNK0 repr: \"len64_post''= 'AAAAAAAA...''''B\" (len=80, '=' index=12). card0._image repr: \"len64_post''= 'AAAAAAAA....
- `21:15:38` Tested 4 cases (len64_post'', len65_post'', len66_post'', embedded_quotes). Observations: values are escaped via value.replace(\"'\",\"''\"); escaped ...
- `21:14:16` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1000,1100p' && nl -ba astropy/io/fits/card. [...]
- `21:13:59` ACTION: nl -ba astropy/io/fits/card.py | sed -n '520,640p' && nl -ba astropy/io/fits/card. [...]
- `21:13:24` Reverted astropy/io/fits/card.py to git HEAD; def _split present; compiled successfully; ran astropy/io/fits/tests/test_header.py -> 175 passed; backu...
- `21:12:10` ACTION: pytest -q astropy/io/fits/tests/test_header.py --maxfail=1
- `21:11:34` Patched _split boolean formatting; backup saved as .py.bak3; Compilation successful; test astropy/io/fits/tests/test_header.py::TestHeaderFunctions::t...
- `21:10:52` ACTION: grep -n "def _split" astropy/io/fits/card.py || true && nl -ba astropy/io/fits/card. [...]
- `21:10:42` RESULT: Expected fallback snippet not found; aborting
- `21:09:31` ACTION: python3 - <<'PY'
- `21:08:57` ACTION: grep -nR "def _split(" . || true && grep -nR "Card._split" . || true
- `21:08:45` RESULT: Installed astropy Card has no _split method
- `21:08:44` ACTION: python3 - <<'PY'
- `21:08:17` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1,400p'
- `21:07:30` Inserted indented 'return False' into len(args)==2 branch of _check_if_rvkc(); Compilation successful; test run: 1 failure - AttributeError: 'Card' ob...
- `21:06:06` ACTION: python3 - <<'PY'
- `21:05:30` ACTION: nl -ba astropy/io/fits/card.py | sed -n '600,720p'
- `21:04:47` ACTION: python3 - <<'PY'
- `21:04:26` ACTION: nl -ba astropy/io/fits/card.py | sed -n '600,720p'
- `21:03:48` ACTION: python3 - <<'PY'
