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

- [2025-12-03 03:09] **swebench-django__django-10999**: Task completed: Submitted
## Interaction Log

- `03:09:25` ACTION: Submitting solution
- `03:09:19` Root cause: standard_duration_re's lookahead required only unsigned digits ('(?=\\d+:\\d+)'), so strings with negative minute/second parts when hours ...
- `03:09:02` parse_duration tests: '1:-5:30' -> datetime.timedelta(0, 3330); '1:5:-30' -> datetime.timedelta(0, 3870); '1:-5:-30' -> datetime.timedelta(0, 3270); '...
- `03:08:42` ACTION: python3 - <<'PY'
- `03:08:14` ACTION: perl -0777 -i -pe 's/\(\?\=\\d\+\:\\d\+\)/(?=-?\\d+:-?\\d+)/' django/utils/dateparse. [...]
- `03:07:53` ACTION: nl -ba django/utils/dateparse.py | sed -n '1,240p'
- `03:07:45` ACTION: grep -nR -E "parse_duration|standard_duration_re" . || true
- `03:07:41` RESULT: grep: testbed: No such file or directory
- `03:07:40` ACTION: grep -nR -E "parse_duration|standard_duration_re" testbed || true
- `03:07:29` TASK STARTED: Fix parse_duration() for some negative durations
