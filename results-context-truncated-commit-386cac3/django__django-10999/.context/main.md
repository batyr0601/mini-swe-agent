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

- [ ] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce: create a small script that uses parse_duration() with negative durations to reproduce the failure
- [ ] 2. Locate: find the file in /testbed that defines standard_duration_re or parse_duration to update the regex
- [ ] 3. Analyze: confirm the hours lookahead lacks
- [ ] 4. Implement fix: change the hours lookahead to (?=-?\\d+:-?\\d+) so negative durations are matched
- [ ] 5. Verify fix: run the repro script and any relevant tests to ensure negative durations parse correctly

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:47] **swebench-django__django-10999**: Task completed: Submitted
## Interaction Log

- `20:47:27` ACTION: Submitting solution
- `20:47:17` RESULT: (13 lines of output) First: '10:15:30' -> datetime.timedelta(0, 36930)...
- `20:47:17` VERIFIED: parse_duration parses negative component durations
- `20:47:16` ACTION: printf '%s\n' 'from django.utils.dateparse import parse_duration' 'cases = [' '"10:15:30",' '"1:15:3 [...]
- `20:47:01` RESULT: bash: -c: line 25: syntax error near unexpected token `&&'
bash: -c: line 25: `&& python3 verify_parse_duration.py'
- `20:47:00` ACTION: Reading file: <<'PY'
- `20:46:42` RESULT: bash: -c: line 25: syntax error near unexpected token `&&'
bash: -c: line 25: `&& python3 verify_parse_duration.py'
- `20:46:42` ACTION: Reading file: <<'PY'
- `20:46:19` Patched django/utils/dateparse.py: updated lookahead to allow negative hours/minutes
- `20:46:19` Found standard_duration_re in django/utils/dateparse.py: hours lookahead lacks '-?
- `20:46:00` Decision: update hours lookahead to (?=-?\\d+:-?\\d+)
- `20:46:00` Found standard_duration_re in django/utils/dateparse.py: hours lookahead lacks '-?
- `20:44:59` RESULT: (146 lines of output) First: 1	"""Functions to parse datetime objects."""...
- `20:44:59` ACTION: nl -ba django/utils/dateparse.py | sed -n '1,220p'
- `20:44:55` RESULT: (32 lines of output) First: ./tests/utils_tests/test_dateparse.py:5:    parse_...
- `20:44:55` ACTION: grep -RIn --line-number -E "standard_duration_re|parse_duration" . || true
- `20:44:52` RESULT: grep: testbed: No such file or directory
- `20:44:51` ACTION: grep -RIn --line-number -E "standard_duration_re|parse_duration" testbed || true
