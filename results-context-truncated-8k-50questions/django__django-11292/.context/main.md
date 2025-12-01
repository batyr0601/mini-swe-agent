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

- [2025-12-03 03:19] **swebench-django__django-11292**: Task completed: Submitted
## Interaction Log

- `03:19:03` ACTION: Submitting solution
- `03:18:58` verification: BaseCommand parser has --skip-checks option (HAS_SKIP_CHECKS: True)
- `03:18:47` RESULT: HAS_SKIP_CHECKS: True
- `03:18:31` patched base.create_parser: added --skip-checks arg in django/core/management/base.py (python script printed: patched)
- `03:18:10` ACTION: python3 - <<'PY'
- `03:17:44` ACTION: grep -nE "base_stealth_options|create_parser|add_arguments" django/core/management/base. [...]
- `03:17:16` ACTION: nl -ba django/core/management/__init__.py | sed -n '1,240p'
- `03:17:10` ACTION: grep -nR "base_stealth_options\|stealth_options\|skip_checks" django/core/management || true
- `03:17:03` ACTION: nl -ba django/core/management/base.py | sed -n '1,260p'
- `03:16:57` ACTION: grep -nR "skip_checks\|skip-checks\|skipchecks" django || true
- `03:16:53` ACTION: ls -la
- `03:16:44` TASK STARTED: Add --skip-checks option to management commands.
