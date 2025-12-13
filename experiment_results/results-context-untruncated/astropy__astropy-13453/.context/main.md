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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:33] **swebench-astropy__astropy-13453**: Task completed: Submitted
## Interaction Log

- `00:33:58` ACTION: Submitting solution
- `00:30:02` Reproduced and verified HTML writer applies formats: HTML output shows formatted a column values like 1.24e-24
- `00:24:57` ACTION: python3 - <<'PY'
- `00:24:48` Patched astropy/io/ascii/html.py: after self.data._set_fill_values(cols) set col.info.format from self.data.formats if present
- `00:24:42` RESULT: Patched html.py
- `00:24:41` ACTION: python3 - <<'PY'
- `00:24:15` ACTION: nl -ba astropy/io/ascii/core.py | sed -n '1680,1740p'
- `00:24:12` ACTION: grep -n "_get_writer" -n astropy/io/ascii/core.py && nl -ba astropy/io/ascii/core. [...]
- `00:24:06` ACTION: nl -ba astropy/io/ascii/core.py | sed -n '700,820p'
- `00:24:01` ACTION: nl -ba astropy/io/ascii/ui.py | sed -n '720,920p'
- `00:23:56` ACTION: nl -ba astropy/io/ascii/core.py | sed -n '880,980p'
- `00:23:53` ACTION: grep -RIn "formats" astropy/io/ascii | sed -n '1,200p'
- `00:23:49` ACTION: nl -ba astropy/io/ascii/core.py | sed -n '1,340p'
- `00:23:45` ACTION: nl -ba astropy/io/ascii/html.py | sed -n '340,460p'
- `00:23:42` ACTION: nl -ba astropy/io/ascii/html.py | sed -n '240,520p'
- `00:23:39` ACTION: nl -ba astropy/io/ascii/html.py | sed -n '1,240p'
- `00:23:36` ACTION: ls -la astropy/io/ascii
- `00:23:32` ACTION: Reading file: 200
- `00:23:29` ACTION: ls -la
- `00:23:19` TASK STARTED: ASCII table output to HTML does not support supplied "formats"
