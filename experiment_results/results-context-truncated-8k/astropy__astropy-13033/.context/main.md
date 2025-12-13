# Project Goals

**Current Task:** TimeSeries: misleading exception when required column check fails.

<details>
<summary>Full description</summary>

TimeSeries: misleading exception when required column check fails.
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
pip install gi...
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

- [2025-12-03 02:57] **swebench-astropy__astropy-13033**: Task completed: Submitted
- [2025-12-03 02:56] **swebench-astropy__astropy-13033**: timeseries: change TypeError to ValueError when 
## Interaction Log

- `02:56:56` ACTION: Submitting solution
- `02:56:52` post-fix reproduction: TimeSeries({'mjd':[1,2,3]}) now raises ValueError: Either 'time' or 'time_start' should be specified
- `02:56:52` found misleading TypeError in astropy/timeseries/sampled.py; replaced with ValueError to match required-column checks in core._check_required_columns
- `02:56:31` repro: initial run raised TypeError: Either 'time' or 'time_start' should be specified
- `02:56:06` RESULT: ValueError: Either 'time' or 'time_start' should be specified
- `02:55:39` ACTION: python3 - <<'PY'
- `02:55:12` RESULT: TypeError: Either 'time' or 'time_start' should be specified
- `02:54:54` ACTION: python3 - <<'PY'
- `02:54:32` ACTION: nl -ba astropy/timeseries/core.py | sed -n '1,300p'
- `02:54:24` ACTION: grep -nR "autocheck_required_columns" -n astropy -n || true
- `02:54:19` ACTION: nl -ba astropy/timeseries/sampled.py | sed -n '1,240p'
- `02:54:17` RESULT: ./astropy/timeseries/sampled.py:18:class TimeSeries(BaseTimeSeries):
- `02:54:01` ACTION: grep -nR "expected 'time' as the first" . || grep -nR "class TimeSeries" . || true
- `02:53:51` TASK STARTED: TimeSeries: misleading exception when required column check fails.
