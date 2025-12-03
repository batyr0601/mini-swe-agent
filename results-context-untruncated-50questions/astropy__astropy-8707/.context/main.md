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

- [2025-12-03 00:32] **swebench-astropy__astropy-8707**: Task completed: Submitted
## Interaction Log

- `00:32:30` ACTION: Submitting solution
- `00:32:11` repro_header_bytes.py passed: Header.fromstring accepts bytes and returns Header len 0
- `00:31:53` Implemented fix: Header.fromstring and Card.fromstring now call decode_ascii on inputs to accept Python 3 bytes
- `00:31:38` Root cause: Header.fromstring and Card.fromstring assumed text str input; Card._pad and other operations do string concatenation so passing bytes on P...
- `00:31:08` Found fromstring methods: header.py:330, card.py:548
- `00:31:06` ACTION: grep -n "def fromstring" astropy/io/fits/header.py astropy/io/fits/card.py
- `00:30:52` repro_header_bytes.py: output: \"<class 'astropy.io.fits.header.Header'> 0\
- `00:30:32` RESULT: <class 'astropy.io.fits.header.Header'> 0
- `00:30:31` ACTION: Reading file: repro_header_bytes.py
- `00:30:15` Updated header.py and card.py: Header.fromstring and Card.fromstring now decode bytes via decode_ascii
- `00:30:07` RESULT: Updated header.py
Updated card.py
- `00:30:07` ACTION: python3 - <<'PY'
- `00:29:31` ACTION: nl -ba astropy/io/fits/util.py | sed -n '276,360p'
- `00:29:01` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1260,1308p'
- `00:28:34` RESULT: 1269:def _pad(input):
- `00:28:33` ACTION: grep -n "def _pad" astropy/io/fits/card.py || true
- `00:28:25` ACTION: nl -ba astropy/io/fits/util.py | sed -n '256,296p'
- `00:28:16` RESULT: 262:def encode_ascii(s):
277:def decode_ascii(s):
