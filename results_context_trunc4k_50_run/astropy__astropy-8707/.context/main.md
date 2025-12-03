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

- [2025-12-02 20:55] **swebench-astropy__astropy-8707**: Task completed: Submitted
## Interaction Log

- `20:55:30` ACTION: Submitting solution
- `20:55:25` Header.fromstring(bytes) test: 'Header parsed OK. Cards: 1
- `20:55:14` RESULT: Header parsed OK. Cards: 1
- `20:55:14` ACTION: python3 - <<'PY'
- `20:55:02` astropy/io/fits/header.py: Header.fromstring patched to accept bytes by decoding data = data.decode('ascii') at method start so card splitting and ''....
- `20:54:54` ACTION: sed -n '320,400p' astropy/io/fits/header.py
- `20:54:39` Patched astropy/io/fits/header.py; test: Header.fromstring(bytes) -> 'Header parsed OK. Cards: 1
- `20:54:27` RESULT: patched astropy/io/fits/header.py
Header parsed OK. Cards: 1
- `20:54:27` ACTION: python3 - <<'PY'
- `20:53:58` Header.fromstring located astropy/io/fits/header.py:330-420; uses ''.join(image) so bytes input causes TypeError 'expected str instance, bytes found
- `20:53:45` ACTION: grep -n "def fromstring" astropy/io/fits/header.py && sed -n '360,420p' astropy/io/fits/header.py
- `20:53:39` Header.fromstring: TypeError 'sequence item 0: expected str instance, bytes found' at astropy/io/fits/header.py:395
- `20:53:28` ACTION: python3 - <<'PY'
- `20:53:16` ACTION: sed -n '300,460p' astropy/io/fits/header.py
- `20:53:09` ACTION: grep -nR "class Header" . || true && grep -nR "def fromstring" . || true && grep -nR "Header. [...]
- `20:52:59` TASK STARTED: Header.fromstring does not accept Python 3 bytes
