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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Analyze parse_duration implementation in django/utils/dateparse.py to identify how signs and microseconds are handled for negative durations
- [ ] 2. Create a minimal reproduction script repro_duration.py that calls parse_duration with negative duration examples (e.g.
- [ ] 3. Edit django/utils/dateparse.py to ensure negative sign is consistently applied to all timedelta components (days, hours, minutes, seconds, microseconds) without incorrectly double-negating microseconds
- [ ] 4. Run the minimal reproduction script once to verify the fix
- [ ] "5.

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 21:02] **swebench-django__django-10999**: Task completed: Submitted
## Interaction Log

- `21:02:46` ACTION: Submitting solution
- `21:02:38` patched django/utils/dateparse.py: removed microseconds '-' prefix and changed return to 'return sign * (days + datetime.timedelta(**kw))'. repro_dura...
- `21:02:03` ACTION: python3 - <<'PY'
- `21:01:18` ACTION: Reading file: <<'PY'
- `21:01:00` parse_duration in django/utils/dateparse.py: builds 'kw' from regex groups; sets sign = -1 if kw.pop('sign', '+') == '-' else 1; pads microseconds to ...
- `21:00:41` ACTION: grep -n "def parse_duration" django/utils/dateparse. [...]
- `21:00:23` ACTION: grep -n "def parse_duration" django/utils/dateparse.py && sed -n '1,240p' django/utils/dateparse.py
- `20:59:24` ACTION: grep -n "def parse_duration" django/utils/dateparse.py && sed -n '1,400p' django/utils/dateparse.py
- `20:59:07` ACTION: grep -n "def parse_duration" django/utils/dateparse.py && sed -n '1,240p' django/utils/dateparse.py
- `20:58:50` ACTION: grep -n "def parse_duration" django/utils/dateparse.py && sed -n '1,400p' django/utils/dateparse.py
- `20:58:40` parse_duration outputs: '-1 day' -> datetime.timedelta(-1); '-1 day, 0:00:00' -> datetime.timedelta(-1); '-1 00:00:00' -> datetime.timedelta(-1); '-1 ...
- `20:58:24` ACTION: python3 - <<'PY'
- `20:58:02` ACTION: sed -n '1,400p' django/utils/dateparse.py
- `20:57:48` ACTION: grep -n "def parse_duration" django/utils/dateparse.py && sed -n '1,400p' django/utils/dateparse.py
- `20:57:39` ACTION: Reading file: <<'PY'
- `20:57:20` ACTION: grep -n "def parse_duration" django/utils/dateparse.py && sed -n '1,400p' django/utils/dateparse.py
- `20:57:03` ACTION: grep -n "def parse_duration" django/utils/dateparse. [...]
- `20:56:36` ACTION: sed -n '1,400p' django/utils/dateparse.py
- `20:56:16` ACTION: sed -n '1,240p' django/utils/dateparse.py
- `20:56:10` ACTION: grep -R -n "parse_duration" . || true
