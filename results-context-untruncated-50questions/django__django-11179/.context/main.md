# Project Goals

**Current Task:** delete() on instances of models without any dependencies doesn't clear PKs.

<details>
<summary>Full description</summary>

delete() on instances of models without any dependencies doesn't clear PKs.
Description
	
Deleting any model with no dependencies not updates the PK on the model. It should be set to None after .delete() call.
See Django.db.models.deletion:276-281. Should update the model line 280.

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

- [2025-12-03 00:37] **swebench-django__django-11179**: Task completed: Submitted
## Interaction Log

- `00:37:25` ACTION: Submitting solution
- `00:37:20` Repro successful: obj.pk is None after delete()
- `00:37:16` RESULT: pk before: 1
pk after: None
OK: PK cleared after delete
- `00:37:15` ACTION: python3 - <<'PY'
- `00:36:40` ACTION: Reading file: <<'PY'
- `00:36:28` ACTION: Reading file: repro.py
- `00:36:00` Patched deletion.py: ensure instance PK cleared in fast-delete path; added setattr(instance, model._meta.pk.attname, None) before return
- `00:35:50` RESULT: patched
- `00:35:50` ACTION: python3 - <<'PY'
- `00:35:20` ACTION: nl -ba django/db/models/deletion.py | sed -n '1,400p'
- `00:35:16` RESULT: ./django/db/models/deletion.py
- `00:35:15` ACTION: find . -type f -name "deletion.py" -print
- `00:34:54` TASK STARTED: delete() on instances of models without any dependencies doesn't clear PKs.
