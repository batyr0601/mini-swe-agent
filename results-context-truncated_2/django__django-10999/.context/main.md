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
- [ ] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: identify where standard_duration_re is defined and why negative hours are not matched (hours lookahead lacks
- [ ] 2. Locate the code: search repository for
- [ ] 3. Implement fix: update the hours lookahead in the regex to accept optional leading
- [ ] 4. Verify fix: add or run a small repro script and/or unit tests exercising negative durations such as
- [ ] 5. Log findings and mark TODOs complete as tasks finish (use context_log and context_todos --complete N)

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:57] **swebench-django__django-10999**: Task completed: Submitted
## Interaction Log

- `20:57:37` ACTION: Submitting solution
- `20:57:11` parse_duration tests: '-1:23:45' -> datetime.timedelta(-1, 84225); '-1 2:03:04' -> datetime.timedelta(-1, 7384); '1:-2:03' -> datetime.timedelta(0, 34...
- `20:56:54` ACTION: python3 - <<'PY'
- `20:56:45` Replaced lookahead (?=\\d+:\\d+) with (?=-?\\d+:-?\\d+) in django/utils/dateparse.py
- `20:56:37` RESULT: REPLACED
- `20:56:37` ACTION: python3 - <<'PY'
- `20:56:13` django/utils/dateparse.py:29-36: standard_duration_re uses lookahead (?=\\d+:\\d+) which doesn't allow negative minutes/seconds; hours group allows -?...
- `20:56:00` ACTION: nl -ba django/utils/dateparse.py | sed -n '1,240p'
- `20:55:55` ACTION: grep -nR -E "standard_duration_re|parse_duration" . || true
- `20:55:51` RESULT: grep: testbed: No such file or directory
- `20:55:51` ACTION: grep -nR -E "standard_duration_re|parse_duration" testbed || true
- `20:55:26` TASK STARTED: Fix parse_duration() for some negative durations
