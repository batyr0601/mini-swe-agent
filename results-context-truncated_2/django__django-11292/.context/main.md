# Project Goals

**Current Task:** Add --skip-checks option to management commands.

<details>
<summary>Full description</summary>

Add --skip-checks option to management commands.
Description
	
Management commands already have skip_checks stealth option. I propose exposing this option on the command line. This would allow users to skip checks when running a command from the command line. Sometimes in a development environment, it is nice to move ahead with a task at hand rather than getting side tracked fixing a system check.

</details>


## TODO List

- [ ] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: reproduce how management commands currently accept skip_checks (stealth option) and confirm it
- [ ] 2. Locate the code: grep the repo for
- [ ] 3. Root cause analysis: inspect the found files to see where skip_checks is accepted but not exposed via add_arguments or argument parser
- [ ] 4. Implement fix: add a
- [ ] 5. Verify fix: create a small management command or script to run a command with --skip-checks and run unit-style checks / reproduction to ensure the option is parsed and used

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:19] **swebench-django__django-11292**: Task completed: Submitted
## Interaction Log

- `21:19:56` ACTION: Submitting solution
- `21:19:51` create_parser parse_args(['--skip-checks']): parsed skip_checks = True
- `21:19:42` RESULT: parsed skip_checks = True
- `21:19:41` ACTION: python3 - <<'PY'
- `21:19:26` Added parser.add_argument('--skip-checks', action='store_true', dest='skip_checks', help='Skip system checks.') to django/core/management/base.py crea...
- `21:19:24` RESULT: Patched base.py: added --skip-checks argument
- `21:19:24` ACTION: python3 - <<'PY'
- `21:19:02` Root cause: create_parser in django/core/management/base.py does not add a --skip-checks argument; base_stealth_options includes 'skip_checks' so it's...
- `21:18:52` ACTION: grep -n "def create_parser" -n django/core/management/base. [...]
- `21:18:42` ACTION: nl -ba django/core/management/__init__.py | sed -n '1,220p'
- `21:18:30` django/core/management/base.py:226 base_stealth_options includes 'skip_checks'; execute() at 360 checks options.get('skip_checks') to decide running s...
- `21:18:09` ACTION: nl -ba django/core/management/base.py | sed -n '1,420p'
- `21:18:04` grep skip_checks: ./django/core/management/base.py:226,360; ./django/core/management/__init__.py:145,146; docs/releases/1.10.txt:790; docs/releases/1....
- `21:17:49` ACTION: grep -R --line-number --exclude-dir=.git "skip_checks" .
- `21:17:34` TASK STARTED: Add --skip-checks option to management commands.
