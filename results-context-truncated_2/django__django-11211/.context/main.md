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
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [x] 1. Reproduce the bug: create models Foo(UUID PK) and Bar with GenericForeignKey, and a small script to call Bar.objects.all().prefetch_related(
- [ ] 2. Locate the code: search for GenericForeignKey/prefetch implementation and code that builds the prefetch map for generic relations in the testbed source
- [ ] 3. Root cause analysis: run the repro, inspect outputs and the prefetch mapping; check for type mismatches (UUID vs str) when matching object ids
- [ ] 4. Implement fix: modify prefetch/generic relation code to normalize object ids to strings or to the target field type (UUID) so matches succeed
- [ ] 5. Verify fix: run the repro script, ensure foo is populated after prefetch, and run tests for edge cases
- [ ] 1. Understand the bug: investigate prefetching of GenericRelation/GenericForeignKey when object_id types (UUID vs str/int) cause mismatches during prefetch
- [ ] 2. Locate the code: find GenericRelation.get_prefetch_queryset, GenericForeignKey.__get__, and prefetch_one_level usage to inspect matching logic
- [ ] 3. Inspect implementation: read django/contrib/contenttypes/fields.py get_prefetch_queryset and related helper code to see how rel_obj_attr and instance_attr values are produced
- [ ] 4. Root cause analysis: determine whether object_id values are normalized (to_python/get_prep_value) before building rel_obj_cache and when matching instance values
- [ ] 5. Implement fix: normalize object_id values (use model._meta.pk.to_python or get_prep_value appropriately) in rel_obj_attr and instance_attr or in prefetch matching code to ensure hashable, comparable keys
- [ ] 6. Add tests: create unit tests in tests/generic_relations/tests.py that reproduce prefetch mismatch for UUID PKs and assert prefetch_related returns related objects
- [ ] 7. Run targeted tests: run tests/generic_relations and tests/prefetch_related to verify fix
- [ ] 8. Log findings at each step and mark TODOs complete as they are finished
- [ ] 1. Fix test import: change
- [ ] 2. Run the single test via run_tests.py
- [ ] 3. After seeing output, log test results and complete TODOs
- [ ] 1. Run targeted test: tests.prefetch_related.test_uuid to verify UUID prefetch behavior
- [ ] 2. If targeted test passes, run individual generic_relations tests: tests.generic_relations.test_forms and tests.generic_relations.tests
- [ ] 1. Remove MIGRATION_MODULES override from tests/django_test_settings.py to allow test DB tables to be created
- [ ] 2. Run targeted test: tests.prefetch_related.test_uuid
- [ ] 3. After seeing output, log test results and mark TODOs complete
- [ ] 1. Re-add MIGRATION_MODULES override to tests/django_test_settings.py to avoid scanning tests/migrations
- [ ] 2. Run targeted test: tests.prefetch_related.test_uuid
- [x] 1. Inspect tests/prefetch_related/models.py to confirm model definitions (Pet, House, Flea) and any custom Meta options affecting table/app labels
- [x] Locate Pet and Flea model definitions in tests/prefetch_related/models.py and check for UUID PKs or custom Meta app_label
- [x] Inspect tests package init and AppConfig: check tests/__init__.py and tests/apps.py to see how models are imported/registered
- [ ] Inspect tests/models.py to see whether it imports models from subpackages (e.g., prefetch_related.models) so Django registers those models
- [ ] Add import in tests/__init__.py to register subpackage models (import tests.prefetch_related.models)
- [x] Create tests/models.py to import subpackage models (prefetch_related) and restore tests/__init__.py to empty to avoid early imports
- [x] Locate GenericRelation.get_prefetch_queryset and GenericForeignKey in django/contrib/contenttypes to inspect prefetch matching logic
- [ ] Run tests.generic_relations.test_forms to verify generic relations still pass after model registration fix
- [x] Make tests/models.py empty to avoid registering prefetch_related models globally (prevents model name conflicts like TaggedItem)
- [x] Inspect tests/generic_relations/models.py TaggedItem definition to check content_type ForeignKey and related_name
- [x] Inspect tests/prefetch_related/__init__.py for imports or side-effects that register models (could cause TaggedItem to be loaded globally)
- [x] Find duplicate TaggedItem definitions and locate
- [ ] Temporarily create tests/django_test_settings_no_test_models_app.py without
- [x] Inspect tests/django_test_settings.py and tests/django_test_settings_no_test_models_app.py to list INSTALLED_APPS entries and find references to
- [x] Inspect tests/test_models_app/models.py to see TaggedItem definition, app_label, and how it
- [x] Run tests/contenttypes/test_prefetch_gfk_uuid.py with original settings (tests.django_test_settings) to verify UUID prefetch behavior with test_models_app present
- [x] Run tests.contenttypes and tests.prefetch_related to validate no regressions after model-registration changes
- [ ] Inspect MultiDbTests.databases in tests/prefetch_related/tests.py and confirm required DB aliases exist in tests/django_test_settings.py
- [ ] Add a temporary settings module tests/django_test_settings_multi_db.py that defines DATABASES with both
- [ ] Run tests.contenttypes and tests.prefetch_related with the temporary multi-db settings module to validate fixes
- [ ] Inspect tests/prefetch_related/models.py for model Meta.app_label or db_table that could affect table creation
- [ ] Check for migrations in tests/prefetch_related/ (presence of migrations may interact with MIGRATION_MODULES={
- [ ] Inspect tests AppConfig and package init to determine app labels: check tests/apps.py, tests/__init__.py, tests/models.py and search for Meta.app_label usages in tests/
- [ ] Inspect for AppConfig/default_app_config that might set app_label
- [ ] Inspect tests/__init__.py and tests/apps.py for default_app_config/AppConfig that could change app label to
- [ ] Inspect tests/__init__.py, tests/apps.py, tests/prefetch_related/__init__.py for default_app_config or AppConfig that could change app labels
- [ ] List registered AppConfig.name, AppConfig.label, and AppConfig.path under tests.django_test_settings_multi_db to see if
- [ ] Check tests.prefetch_related models
- [ ] Inspect tests/prefetch_related/tests.py around lines 260-330 to see why the test expects table prefetch_related_book
- [ ] Add
- [ ] Run targeted test: tests.prefetch_related.test_uuid to verify UUID prefetch behavior
- [ ] 1. Locate GenericForeignKey.get_prefetch_queryset implementation: inspect django/contrib/contenttypes/fields.py around GenericForeignKey and its get_prefetch_queryset methods
- [ ] 2. Inspect prefetch matching logic: inspect django/db/models/query.py prefetch_one_level implementation for how rel_obj_attr and instance_attr are compared/normalized
- [ ] 3. Reproduce runtime values: plan to run a Python snippet under tests.django_test_settings to call get_prefetch_queryset and print rel_obj_attr/instance_attr for sample instances to check UUID vs str types
- [ ] Inspect GenericForeignKey.get_prefetch_queryset implementation in django/contrib/contenttypes/fields.py (around lines 140-220)
- [ ] Inspect alternate get_prefetch_queryset in django/contrib/contenttypes/fields.py (around lines 540-620)
- [ ] Inspect prefetch_one_level implementation in django/db/models/query.py (around lines 1688-1748)

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:43] **swebench-django__django-11211**: Task completed: LimitsExceeded
- [2025-12-01 21:24] **swebench-django__django-11211**: Fix GenericForeignKey prefetch ID normalization: use model._meta.pk.to_python in gfk_key to match Ge...
## Interaction Log

- `21:43:15` ACTION: grep -nR --line-number "def get_prefetch_queryset" django || true && grep -nR --line-number "class G [...]
- `21:43:06` tests.prefetch_related.test_uuid: 9 tests OK; sync created prefetch_related_* tables and test DBs were created/destroyed
- `21:42:14` Appended 'tests.prefetch_related' to tests/django_test_settings_multi_db INSTALLED_APPS; re-ran tests.contenttypes + tests.prefetch_related -> 95 test...
- `21:41:51` Appended 'tests.prefetch_related' to tests/django_test_settings_multi_db INSTALLED_APPS; re-ran tests.contenttypes + tests.prefetch_related -> 95 test...
- `21:41:51` ACTION: ID=$(context_todos | tail -n1 | sed -E 's/^[[:space:]]*([0-9]+). [...]
- `21:40:04` ACTION: sed -n '1,200p' tests/__init__.py 2>/dev/null || true && sed -n '1,400p' tests/apps. [...]
- `21:37:30` tests.contenttypes + tests.prefetch_related: created test DB; ran 91 tests -> FAILED (errors=4). Errors observed: MultiDbTests.setUpClass ImproperlyCo...
- `21:36:45` tests.contenttypes.test_prefetch_gfk_uuid: with tests.test_models_app in INSTALLED_APPS -> 1 test ran OK
- `21:36:24` tests/test_models_app/models.py: UUIDModel(id=UUIDField primary_key, tags=GenericRelation('test_models_app.TaggedItem', content_type_field='content_ty...
- `21:35:44` tests/django_test_settings.py: INSTALLED_APPS = ['django.contrib.contenttypes','django.contrib.auth','tests'] plus line \"INSTALLED_APPS += ['tests.te...
- `21:34:36` grep found TaggedItem definitions: tests/prefetch_related/models.py:142, tests/select_related/models.py:108, tests/generic_relations/models.py:19, tes...
- `21:34:07` tests/prefetch_related/__init__.py is empty; no side-effect imports that register models
- `21:33:57` ACTION: sed -n '1,240p' tests/prefetch_related/__init__.py || true
- `21:33:33` tests/generic_relations/models.py: TaggedItem (line 19) defines content_type = ForeignKey(ContentType, models.CASCADE) with no related_name, object_id...
- `21:31:54` django/contrib/contenttypes/fields.py: GenericForeignKey.get_forward_related_filter uses obj.pk; GenericRelation.get_prefetch_queryset builds query wi...
- `21:31:34` ACTION: sed -n '1,260p' django/contrib/contenttypes/fields.py && sed -n '520,680p' django/contrib/contenttyp [...]
- `21:31:13` tests/prefetch_related.test_uuid: created test DB, ran 9 tests -> OK; targeted test passed and test DB destroyed
- `21:29:50` tests/__init__.py is empty; tests/apps.py not present — no AppConfig or automatic model imports
- `21:29:25` ACTION: sed -n '1,240p' tests/__init__.py || true
- `21:28:50` tests/prefetch_related/models.py: class Pet at 287: id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False); class Flea at 293: id = UUID...
