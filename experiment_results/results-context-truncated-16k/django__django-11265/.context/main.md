# Project Goals

**Current Task:** Using exclude on annotated FilteredRelation doesn't work

<details>
<summary>Full description</summary>

Using exclude on annotated FilteredRelation doesn't work
Description
	
It looks like using exclude on queryset with annotated FilteredRelation give a FieldError on the annotation name.
For exemple, in Django tests (django/tests/filtered_relation/tests.py) if we change this :
def test_with_join(self):
	self.assertSequenceEqual(
		Author.objects.annotate(
			book_alice=FilteredRelation('book', condition=Q(book__title__iexact='poem by alice')),
		).filter(book_alice__isnull=False),
		[self.author1]
	)
to this
def test_with_join(self):
	self.assertSequenceEqual(
		Author.objects.annotate(
			book_alice=FilteredRelation('book', condition=Q(book__title__iexact='poem by alice')),
		).exclude(book_alice__isnull=False),
		[]
	)
You get the error :
Traceback (most recent call last):
 File "/usr/lib/...
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

- [2025-12-02 23:37] **swebench-django__django-11265**: Task completed: Submitted
## Interaction Log

- `23:37:46` ACTION: Submitting solution
- `23:37:37` ACTION: python -m py_compile django/db/models/sql/query.py
- `23:37:22` Edited split_exclude: added 'query._filtered_relations = self._filtered_relations.copy()' before 'query.add_filter' and removed duplicated 'query = Qu...
- `23:37:08` ACTION: perl -0777 -i.bak2 -pe 's/query\._filtered_relations = self\._filtered_relations\. [...]
- `23:36:50` split_exclude: inserted 'query._filtered_relations = self._filtered_relations.copy()' before 'query.add_filter'; observed duplicate 'query = Query(sel...
- `23:36:33` ACTION: perl -0777 -i.bak -pe "s/(query = Query\\(self\\.model\\)\\n\\s*)query\\.add_filter\\(/\\1query. [...]
- `23:36:11` ACTION: nl -ba django/db/models/sql/query.py | sed -n '400,520p'
- `23:36:05` ACTION: grep -nR "annotation_select" -n django || true
- `23:35:54` ACTION: nl -ba django/db/models/sql/query.py | sed -n '300,360p'
- `23:35:47` ACTION: nl -ba django/db/models/sql/query.py | sed -n '1340,1460p'
- `23:35:43` ACTION: grep -nR "_filtered_relations\|add_filtered_relation\|add_filtered_relation" django | sed -n '1,200p [...]
- `23:35:31` ACTION: nl -ba django/db/models/sql/query.py | sed -n '1680,1760p'
- `23:35:23` ACTION: nl -ba django/db/models/sql/query.py | sed -n '1600,1680p'
- `23:35:20` ACTION: nl -ba django/db/models/sql/query.py | sed -n '1,260p'
- `23:35:16` ACTION: echo '---split_exclude---' && grep -nR "split_exclude" . [...]
- `23:35:02` TASK STARTED: Using exclude on annotated FilteredRelation doesn't work
