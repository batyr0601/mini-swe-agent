# Project Goals

**Current Task:** CheckConstraint with OR operator generates incorrect SQL on SQLite and Oracle.

<details>
<summary>Full description</summary>

CheckConstraint with OR operator generates incorrect SQL on SQLite and Oracle.
Description
	 
		(last modified by Michael Spallino)
	 
Django is incorrectly including the fully qualified field name(e.g. “my_table”.”my_field”) in part of the check constraint. This only appears to happen when there is a combination of OR and AND clauses in the CheckConstraint.
Including the fully qualified field name fails the migration because when we drop the old table and swap the name of the staging table in place, the constraint fails with a malformed schema exception (on sqlite) saying that the field doesn’t exist on the table. It appears that this has to do with the AND clause items using Col while the OR clause uses SimpleCol. Here is an example of this behavior:
class TestConstraint(models.Model):
	...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [x] 1. Reproduce the bug: create a minimal repro that builds a CheckConstraint with mixed OR/AND and generates the CREATE TABLE SQL
- [x] 2. Locate the code: find the module(s) responsible for rendering CheckConstraint/Q objects to SQL (look for CheckConstraint, SimpleCol, Col, constraint SQL generation)
- [x] 3. Root cause analysis: inspect how column names are qualified in OR vs AND clauses and identify where SimpleCol vs Col handling diverges
- [x] 4. Implement fix: modify SQL generation to consistently avoid table-qualified column names in constraint definitions when creating staging tables (or ensure all column refs are rendered the same way)
- [x] 5. Verify fix: run the repro to show CREATE TABLE uses unqualified column names and run available tests related to constraints
- [ ] 1. Push branch fix/simplecol-query-add to the origin remote (requires remote configured and consent)
- [ ] 2. Run full test suite locally to verify no regressions (may require pytest and dependencies)
- [ ] 3. Create a PR from fix/simplecol-query-add using gh/hub after pushing (requires remote and credentials)

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:34] **swebench-django__django-11299**: Task completed: LimitsExceeded
- [2025-12-01 21:20] **swebench-django__django-11299**: Fix: pass simple_col through recursive Query._add_q to preserve SimpleCol (unqualified column names)...
## Interaction Log

- `21:34:29` ACTION: sed -n '1160,1370p' django/db/models/sql/query.py
- `21:34:19` ACTION: grep -n "simple_col=" django/db/models/sql/query.py || true
- `21:34:05` ACTION: sed -n '1328,1350p' django/db/models/sql/query.py
- `21:33:57` ACTION: git --no-pager show --name-status --pretty=format:"%h %ad %s" HEAD && git branch --show-current && l [...]
- `21:33:42` session_end: keep branch fix/simplecol-query-add and patch files local; no push/open-pr/tests performed
- `21:33:31` ACTION: git --no-pager show --name-status --pretty=format:"%h %ad %s" HEAD && echo "Current branch: $(git br [...]
- `21:33:04` user_chosen: done - keep branch fix/simplecol-query-add and patch files local; no push/open-pr/tests performed
- `21:32:27` ACTION: echo $'Please reply with exactly one word (no extra text):\n\npush - push branch fix/simplecol-query [...]
- `21:32:01` ACTION: git --no-pager show --name-status --pretty=format:"%h %ad %s" HEAD && git status --porcelain --branc [...]
- `21:31:37` action: done - left branch fix/simplecol-query-add and patches locally; no push/open-pr/tests performed
- `21:31:12` ACTION: echo $'Choose the next step and reply with exactly one word (no extra text):\n\npush - push branch f [...]
- `21:30:56` ACTION: git remote -v && echo "Current branch: $(git branch --show-current)" && (git rev-parse --abbrev-ref  [...]
- `21:30:41` ACTION: git branch --show-current && git --no-pager show --name-only --pretty=format:"%h %ad %s" HEAD && ls  [...]
- `21:30:02` ACTION: echo $'Choose the next step and reply with exactly one word (no extra text):\n\npush - push branch f [...]
- `21:29:52` ACTION: Reading file: pr_fix_simplecol.patch
- `21:29:46` ACTION: git checkout -B fix/simplecol-query-add && git format-patch -1 HEAD --stdout > pr_fix_simplecol. [...]
- `21:29:30` git show: 3c4679e9b0 Tue Dec 2 03:28:58 2025 +0000 Fix: pass simple_col through recursive Query._add_q to preserve SimpleCol (unqualified column names...
- `21:29:14` ACTION: git --no-pager show --name-status --pretty=format:"%h %ad %s" HEAD && git status --porcelain
- `21:29:07` git commit: 3c4679e9b0 - Fix: pass simple_col through recursive Query._add_q to preserve SimpleCol (unqualified column names) in CheckConstraint SQL; ...
- `21:28:58` ACTION: git commit -m "Fix: pass simple_col through recursive Query. [...]
