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
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:38] **swebench-django__django-11292**: Task completed: Submitted
## Interaction Log

- `00:38:41` ACTION: Submitting solution
- `00:38:38` ACTION: python3 -c "from django.core.management import ManagementUtility; import sys; sys.argv=['manage. [...]
- `00:38:34` ACTION: python3 - <<'PY'
- `00:38:22` Added parser.add_argument('--skip-checks', action='store_true', dest='skip_checks', help='Skip system checks.') in django/core/management/base.py:289
- `00:38:09` ACTION: perl -0777 -pe "s/(\n\s*self.add_arguments\(parser\))/\n parser. [...]
- `00:37:46` ACTION: nl -ba django/core/management/__init__.py | sed -n '96,160p'
- `00:37:42` ACTION: grep -R --line-number "base_stealth_options" -n django || true
- `00:37:36` ACTION: nl -ba django/core/management/base.py | sed -n '249,420p'
- `00:37:19` ACTION: nl -ba django/core/management/__init__.py | sed -n '1,260p'
- `00:37:14` Found base_stealth_options includes 'skip_checks' in django/core/management/base.py:226; requires_system_checks defined at line 223; create_parser sta...
- `00:37:07` ACTION: nl -ba django/core/management/base.py | sed -n '1,260p'
- `00:37:02` ACTION: grep -R --line-number "skip_checks" django || true
- `00:36:58` ACTION: ls -la
- `00:36:40` TASK STARTED: Add --skip-checks option to management commands.
