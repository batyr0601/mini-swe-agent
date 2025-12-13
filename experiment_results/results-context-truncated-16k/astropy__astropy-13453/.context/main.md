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

- [2025-12-02 23:32] **swebench-astropy__astropy-13453**: Task completed: Submitted
## Interaction Log

- `23:32:08` ACTION: Submitting solution
- `23:31:53` HTML.write patched: set self.data.cols = cols and call self.data._set_col_formats(); verification shows formatted HTML cell values '1.234' and '2.346'...
- `23:31:01` ACTION: python3 - <<'PY'
- `23:30:46` ACTION: cp astropy/io/ascii/html.py astropy/io/ascii/html.py.bak && \
- `23:30:17` ACTION: nl -ba astropy/io/ascii/html.py | sed -n '380,700p'
- `23:29:56` ACTION: nl -ba astropy/io/ascii/html.py | sed -n '200,380p'
- `23:28:58` ACTION: grep -nE "class (HTML|HTMLData)|def _set_col_formats|def iter_str_vals|def str_vals|def write" astro [...]
- `23:28:32` ACTION: python3 - <<'PY'
- `23:28:05` ACTION: nl -ba astropy/io/ascii/core.py | sed -n '1660,1760p'
- `23:27:58` RESULT: astropy/io/ascii/core.py:1727:        writer.data.formats = kwargs['formats']
- `23:27:57` ACTION: grep -nR "writer.data.formats" astropy/io/ascii || true
- `23:27:44` ACTION: python3 - <<'PY'
- `23:27:17` astropy/io/ascii/core.py:_set_col_formats sets per-column formats by assigning col.info.format = self.formats[col.info.name] (lines 934-939)
- `23:27:03` ACTION: sed -n '930,940p' astropy/io/ascii/core.py
- `23:26:49` ACTION: nl -ba astropy/io/ascii/core.py | sed -n '720,960p'
- `23:26:44` ACTION: grep -nR "\bformats\b" astropy/io/ascii || true
- `23:26:30` HTML writer (astropy.io.ascii.html.HTML.write) respects col.info.format: output contained '<td>1.23</td>' and '<td>2.35</td>' for format '{:.2f}
- `23:26:05` ACTION: python3 - <<'PY'
- `23:25:36` ACTION: nl -ba astropy/table/pprint.py | sed -n '420,760p'
- `23:25:29` ACTION: nl -ba astropy/table/pprint.py | sed -n '240,420p'
