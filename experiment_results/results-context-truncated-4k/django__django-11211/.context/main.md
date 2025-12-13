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

<!-- 
Add detailed, specific TODOs when starting a task. Good examples:
- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 21:19] **swebench-django__django-11211**: Task completed: LimitsExceeded
## Interaction Log

- `21:19:16` django test runner: error: unrecognized arguments: -q
- `21:19:11` ACTION: DJANGO_SETTINGS_MODULE=test_settings python -m django test tests.test_prefetch_gfk_uuid. [...]
- `21:18:59` ACTION: sed -n '1,240p' tests/test_prefetch_gfk_uuid.py
- `21:18:40` ACTION: DJANGO_SETTINGS_MODULE=test_settings python - <<'PY'
- `21:18:14` ACTION: Reading file: <<'PY'
- `21:17:54` pytest error while running tests/test_prefetch_gfk_uuid.py: django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but setting...
- `21:17:44` ACTION: python -m pytest -q tests/test_prefetch_gfk_uuid.py::PrefetchGFKTest::test_prefetch_does_not_error
- `21:17:30` ACTION: sed -n '1,260p' django/contrib/contenttypes/fields.py && sed -n '520,640p' django/contrib/contenttyp [...]
- `21:17:24` ACTION: grep -n -e "class GenericForeignKey" -e "def get_prefetch" -e "get_prefetch" -e "get_prefetch_querys [...]
- `21:17:11` ACTION: python -m pytest -q tests/test_prefetch_gfk_uuid.py::PrefetchGFKTest::test_prefetch_does_not_error
- `21:17:02` ACTION: sed -n '1,240p' tests/test_prefetch_gfk_uuid.py
- `21:16:05` ACTION: python - <<'PY'
- `21:15:40` ACTION: Reading file: <<'PY'
- `21:15:02` ACTION: sed -n '1,240p' tests/test_prefetch_gfk_uuid.py
- `21:14:49` ACTION: python -m pip install -q pytest && python -m pytest -q tests/test_prefetch_gfk_uuid. [...]
- `21:14:24` ACTION: sed -n '1,800p' django/contrib/contenttypes/fields.py
- `21:14:20` ACTION: grep -n -e "class GenericForeignKey" -e "get_prefetch" django/contrib/contenttypes/fields.py
- `21:14:10` ACTION: sed -n '1,240p' tests/test_prefetch_gfk_uuid.py
- `21:14:03` pytest not found: /opt/miniconda3/envs/testbed/bin/python: No module named pytest
- `21:13:56` RESULT: /opt/miniconda3/envs/testbed/bin/python: No module named pytest
