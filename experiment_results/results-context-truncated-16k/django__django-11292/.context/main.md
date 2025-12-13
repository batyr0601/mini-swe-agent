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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:37] **swebench-django__django-11292**: Task completed: Submitted
## Interaction Log

- `23:37:40` ACTION: Submitting solution
- `23:37:32` create_parser check: FOUND True; option actions: [['--skip-checks']]
- `23:37:22` RESULT: FOUND True
[['--skip-checks']]
- `23:37:21` ACTION: python3 - <<'PY'
- `23:37:04` Inserted parser.add_argument('--skip-checks', action='store_true', help='Skip system checks.') into django/core/management/base.py before self.add_arg...
- `23:36:47` ACTION: sed -i "/self.add_arguments(parser)/i\ parser.add_argument('--skip-checks', action='store_true', hel [...]
- `23:36:33` ACTION: nl -ba django/core/management/__init__.py | sed -n '1,260p'
- `23:36:30` ACTION: nl -ba django/core/management/base.py | sed -n '200,380p'
- `23:36:27` ACTION: nl -ba django/core/management/base.py | sed -n '1,520p'
- `23:36:21` ACTION: grep -RIn --line-number -E "skip_checks|skip-checks|class BaseCommand|def add_arguments" . || true
- `23:36:16` RESULT: grep: testbed: No such file or directory
- `23:36:15` ACTION: grep -RIn --line-number -E "skip_checks|skip-checks|class BaseCommand|def add_arguments" testbed ||  [...]
- `23:36:02` TASK STARTED: Add --skip-checks option to management commands.
