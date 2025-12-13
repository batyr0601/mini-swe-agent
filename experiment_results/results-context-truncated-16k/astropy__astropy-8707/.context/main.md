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

- [2025-12-02 23:31] **swebench-astropy__astropy-8707**: Task completed: Submitted
## Interaction Log

- `23:31:32` ACTION: Submitting solution
- `23:31:26` repro_fromstring_bytes.py: Parsed header successfully; Input type bytes; output starts with 'FOO     =                    1 / test\\nEND\\n
- `23:31:05` ACTION: python3 repro_fromstring_bytes.py
- `23:30:55` patched header.py; patched card.py; attempted to run repro in same command previously but got shell error: syntax error near unexpected token `&&
- `23:30:19` ACTION: python - <<'PY'
- `23:29:39` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1240,1290p'
- `23:29:27` ACTION: nl -ba astropy/io/fits/card.py | grep -n "def _pad\|def _" -n | sed -n '1,120p'
- `23:29:23` repro_fromstring_bytes.py: TypeError 'sequence item 0: expected str instance, bytes found' at astropy/io/fits/header.py:395
- `23:29:04` ACTION: Reading file: repro_fromstring_bytes.py
- `23:28:36` ACTION: nl -ba astropy/io/fits/card.py | sed -n '520,760p'
- `23:28:33` ACTION: nl -ba astropy/io/fits/card.py | sed -n '1,220p'
- `23:28:23` ACTION: nl -ba astropy/io/fits/header.py | sed -n '300,420p'
- `23:28:17` ACTION: grep -R -n "fromstring" . --exclude-dir .git || true
- `23:28:11` RESULT: grep: testbed: No such file or directory
- `23:28:11` ACTION: grep -R -n "fromstring" -n testbed || true
- `23:27:58` TASK STARTED: Header.fromstring does not accept Python 3 bytes
