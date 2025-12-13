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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:36] **swebench-django__django-11179**: Task completed: Submitted
## Interaction Log

- `23:35:59` ACTION: Submitting solution
- `23:35:54` Found deletion.py fast-delete optimized branch (lines ~274-281) returned early without clearing instance PK; patched to call setattr(instance, model._...
- `23:35:54` repro.py: before delete pk = 1; after delete pk = None (fast-delete path now clears PK)
- `23:35:34` RESULT: before delete, pk = 1
after delete, pk = None
- `23:35:33` ACTION: Reading file: repro.py
- `23:35:08` Patched django/db/models/deletion.py: fast-delete single-instance path now clears instance PK via setattr(instance, model._meta.pk.attname, None) at a...
- `23:34:54` ACTION: nl -ba django/db/models/deletion.py | sed -n '270,286p'
- `23:34:46` ACTION: python3 - <<'PY'
- `23:34:17` ACTION: nl -ba django/db/models/deletion.py | sed -n '260,290p'
- `23:34:02` ACTION: nl -ba django/db/models/deletion.py | sed -n '1,420p'
- `23:33:57` ACTION: ls -la
- `23:33:48` TASK STARTED: delete() on instances of models without any dependencies doesn't clear PKs.
