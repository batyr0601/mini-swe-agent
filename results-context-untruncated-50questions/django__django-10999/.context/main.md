# Project Goals

**Current Task:** Fix parse_duration() for some negative durations

<details>
<summary>Full description</summary>

Fix parse_duration() for some negative durations
Description
	
The ​https://docs.djangoproject.com/en/2.1/_modules/django/utils/dateparse/ defines:
standard_duration_re = re.compile(
	r'^'
	r'(?:(?P<days>-?\d+) (days?, )?)?'
	r'((?:(?P<hours>-?\d+):)(?=\d+:\d+))?'
	r'(?:(?P<minutes>-?\d+):)?'
	r'(?P<seconds>-?\d+)'
	r'(?:\.(?P<microseconds>\d{1,6})\d{0,6})?'
	r'$'
)
that doesn't match to negative durations, because of the <hours> definition final (lookahead) part does not have '-?' in it. The following will work:
	r'((?:(?P<hours>-?\d+):)(?=-?\d+:-?\d+))?'
(Thanks to Konstantin Senichev for finding the fix.)

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

- [2025-12-03 00:33] **swebench-django__django-10999**: Task completed: Submitted
## Interaction Log

- `00:33:41` ACTION: Submitting solution
- `00:33:39` root cause: lookahead didn't allow negative signs for hour/minute parts; changed to accept - in lookahead
- `00:33:39` found standard_duration_re in django/utils/dateparse.py; changed lookahead '(?=\\d+:\\d+)' to '(?=-?\\d+:-?\\d+)
- `00:33:39` repro_parse_duration outputs: '30' -> 0:00:30; '15:30' -> 0:15:30; '5:30' -> 0:05:30; '10:15:30' -> 10:15:30; '-10:15:30' -> -1 day, 14:15:30; '1:-15:...
- `00:33:11` ACTION: Reading file: <<'PY'
- `00:32:54` RESULT: bash: line 1: pytest: command not found
- `00:32:54` ACTION: pytest -q tests/utils_tests/test_dateparse.py tests/utils_tests/test_duration.py
- `00:32:47` replaced standard_duration_re lookahead: '(?=\\d+:\\d+)' -> '(?=-?\\d+:-?\\d+)
- `00:32:33` RESULT: replaced
- `00:32:32` ACTION: python3 - <<'PY'
- `00:32:07` ACTION: nl -ba django/utils/dateparse.py | sed -n '1,220p'
- `00:32:00` ACTION: grep -nR -e "parse_duration" -e "standard_duration_re" . || true
- `00:31:45` RESULT: grep: testbed: No such file or directory
- `00:31:45` ACTION: grep -nR -e "parse_duration" -e "standard_duration_re" testbed || true
- `00:31:29` TASK STARTED: Fix parse_duration() for some negative durations
