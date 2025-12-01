# Project Goals

**Current Task:** ASCII table output to HTML does not support supplied "formats"

<details>
<summary>Full description</summary>

ASCII table output to HTML does not support supplied "formats"
<!-- This comments are hidden when you submit the issue,
so you do not need to remove them! -->

<!-- Please be sure to check out our contributing guidelines,
https://github.com/astropy/astropy/blob/main/CONTRIBUTING.md .
Please be sure to check out our code of conduct,
https://github.com/astropy/astropy/blob/main/CODE_OF_CONDUCT.md . -->

<!-- Please have a search on our GitHub repository to see if a similar
issue has already been posted.
If a similar issue is closed, have a quick look to see if you are satisfied
by the resolution.
If not please go ahead and open an issue! -->

<!-- Please check that the development version still produces the same bug.
You can install development version with
pip install git+ht...
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

- [2025-12-03 03:07] **swebench-astropy__astropy-13453**: Task completed: Submitted
## Interaction Log

- `03:07:07` ACTION: Submitting solution
- `03:07:02` Verification: HTML.write with formats {'a':'%.2f'} produced formatted values 1.23 and 2.35 in output
- `03:07:02` Fix implemented: added 'self.data.cols = cols' in astropy/io/ascii/html.py after assigning header.cols
- `03:07:02` Root cause: HTMLData had header.cols set but not HTMLData.cols; _set_col_formats expects self.cols so formats were not applied
- `03:05:59` repro: calling HTMLSplitter.write produced AttributeError 'HTMLSplitter' object has no attribute \"data\" when used standalone; HTMLSplitter expects t...
- `03:05:15` html.py: added 'self.data.cols = cols' after 'self.data.header.cols = cols' so HTMLData has self.cols before calling _set_col_formats
- `03:05:01` ACTION: python3 - <<'PY'
- `03:04:40` ACTION: sed -n '180,260p' astropy/io/ascii/html.py
- `03:04:31` ACTION: grep -n "class HTMLData" astropy/io/ascii/html.py || true && sed -n '420,740p' astropy/io/ascii/html [...]
- `03:04:12` ACTION: sed -n '880,980p' astropy/io/ascii/core.py
- `03:03:58` ACTION: grep -nR "_set_col_formats" astropy || true
- `03:03:36` ACTION: sed -n '1,120p' astropy/io/ascii/html.py && sed -n '320,420p' astropy/io/ascii/html.py
- `03:03:29` RESULT: 40:    def write(self, data):
342:    def write(self, table):
- `03:03:27` ACTION: grep -n "def write" -n astropy/io/ascii/html.py && sed -n '560,760p' astropy/io/ascii/html.py
- `03:03:22` ACTION: sed -n '1,320p' astropy/io/ascii/html.py
- `03:03:08` ACTION: python3 - <<'PY'
- `03:02:40` patched; subsequent grep/sed not executed due to bash error: 'bash: -c: line 14: syntax error near unexpected token `&&
- `03:02:25` ACTION: python - <<'PY'
- `03:01:51` ACTION: sed -n '840,912p' astropy/io/ascii/core.py
