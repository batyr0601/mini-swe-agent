# Project Goals

**Current Task:** Prefetch related is not working when used GFK for model that uses UUID field as PK.

<details>
<summary>Full description</summary>

Prefetch related is not working when used GFK for model that uses UUID field as PK.
Description
	
How to reproduce:
create model with UUID as primary key
class Foo(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	...
create another model with GFK to model Foo
class Bar(models.Model):
	foo_content_type = models.ForeignKey(
		ContentType, related_name='actor',
		on_delete=models.CASCADE, db_index=True
	)
	foo_object_id = models.CharField(max_length=255, db_index=True)
	foo = GenericForeignKey('foo_content_type', 'foo_object_id')
	...
and try to get queryset with prefetch related (django orm engine return None for attribute foo):
Bar.objects.all().prefetch_related('foo')
Thanks a lot for your attention! Also i wanna point out some related bug report...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:38] **swebench-django__django-11211**: Task completed: Submitted
## Interaction Log

- `23:38:52` ACTION: Submitting solution
- `23:38:46` Verification: minimal test with django.setup() returned OK; GenericForeignKey.get_prefetch_queryset prepares fk values via target model _meta.pk.get_p...
- `23:37:48` RESULT: OK
- `23:37:47` ACTION: Reading file: <<'PY'
- `23:37:16` ACTION: python3 - <<'PY'
- `23:36:18` ACTION: nl -ba tests/prefetch_related/tests.py | sed -n '1,260p'
- `23:36:08` ACTION: grep -nR "GenericForeignKey" tests | sed -n '1,200p'
- `23:35:57` Patched django/contrib/contenttypes/fields.py: replaced ct.get_all_objects_for_this_type(pk__in=fkeys) with prepared_fkeys built via model._meta.pk.ge...
- `23:35:37` RESULT: patched
- `23:35:36` ACTION: python3 - <<'PY'
- `23:35:07` ACTION: grep -nR "def get_prep_value" django | sed -n '1,200p'
- `23:35:02` ACTION: nl -ba django/db/models/fields/__init__.py | sed -n '2288,2336p'
- `23:34:59` ACTION: grep -nR "class UUIDField" -n django | sed -n '1,200p'
- `23:34:50` ACTION: nl -ba django/contrib/contenttypes/fields.py | sed -n '140,220p'
- `23:34:44` ACTION: grep -nR "prefetch" django | sed -n '1,200p'
- `23:34:38` ACTION: nl -ba django/contrib/contenttypes/fields.py | sed -n '1,420p'
- `23:34:33` ACTION: grep -nR "GenericForeignKey" -n django | sed -n '1,200p'
- `23:34:29` ACTION: ls -la
- `23:34:20` TASK STARTED: Prefetch related is not working when used GFK for model that uses UUID field as PK.
