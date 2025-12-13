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
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 21:18] **swebench-django__django-11179**: Task completed: Submitted
## Interaction Log

- `21:18:05` ACTION: Submitting solution
- `21:17:03` ACTION: sed -n '240,320p' django/db/models/deletion.py
- `21:16:34` ACTION: sed -n '240,320p' django/db/models/deletion.py && \
- `21:16:12` ACTION: cp -a django/db/models/deletion.py django/db/models/deletion.py.bak && \
- `21:15:24` ACTION: sed -n '240,320p' django/db/models/deletion.py
- `21:15:11` ACTION: grep -n "len(self.data) == 1" django/db/models/deletion. [...]
- `21:14:56` ACTION: cp -a django/db/models/deletion.py django/db/models/deletion.py.bak && python3 - <<'PY'
- `21:14:07` ACTION: sed -n '240,320p' django/db/models/deletion.py
- `21:13:54` ACTION: sed -n '1,260p' django/db/models/deletion.py
- `21:13:43` ACTION: grep -nR "can_fast_delete" || true
- `21:13:33` django/db/models/deletion.py: lines ~260-300 show added fast-delete block: 'if len(self.data) == 1: model, instances = next(iter(self.data.items())); ...
- `21:13:23` ACTION: sed -n '240,320p' django/db/models/deletion.py
- `21:13:08` ACTION: python3 - <<'PY'
- `21:12:24` ACTION: grep -n "len(self.data) == 1" django/db/models/deletion. [...]
- `21:12:04` ACTION: sed -n '1,320p' django/db/models/deletion.py
- `21:11:49` ACTION: python3 - <<'PY'
- `21:11:06` ACTION: grep -n "len(self.data) == 1" django/db/models/deletion. [...]
- `21:10:29` ACTION: sed -n '1,320p' django/db/models/deletion.py
- `21:10:22` repro_delete.py: before_delete_pk: 1; after_delete_pk: 1 - PK not cleared after delete
- `21:10:15` RESULT: before_delete_pk: 1
