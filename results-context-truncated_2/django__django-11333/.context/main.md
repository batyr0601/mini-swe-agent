# Project Goals

**Current Task:** Optimization: Multiple URLResolvers may be unintentionally be constructed by calls to `django.urls.resolvers.get_resolver`

<details>
<summary>Full description</summary>

Optimization: Multiple URLResolvers may be unintentionally be constructed by calls to `django.urls.resolvers.get_resolver`
Description
	
Multiple URLResolvers may be constructed by django.urls.resolvers.get_resolver if django.urls.base.set_urlconf has not yet been called, resulting in multiple expensive calls to URLResolver._populate.
​`get_resolver` constructs a new URLResolver, and caches it using functools.lru_cache.
URLResolver instances can pre-compute a large amount of information about routes in ​`URLResolver._populate`, and they store those caches as instance variables.
​`set_urlconf` is called with when ​we first handle a request in `BaseHandler.get_response`.
get_resolver has a number of call-sites. Most notably, ​`reverse`. Like the other call-sites, reverse calls get_resolver w...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [x] 1. Understand the bug: Multiple URLResolver instances are constructed by django.urls.resolvers.get_resolver when set_urlconf hasn
- [ ] 2. Locate the get_resolver implementation: search for get_resolver in django/urls/resolvers.py and related call sites like django/urls/__init__.py and django/urls/base.py.
- [ ] 3. Reproduce the issue: create a small script that calls reverse (or get_resolver) before and after set_urlconf to observe multiple URLResolver constructions (or _populate calls).
- [ ] 4. Implement fix: modify get_resolver to consult settings.ROOT_URLCONF (via django.conf) before calling the memoized resolver factory, so both early and later calls use same key.
- [ ] 5. Verify fix: run the reproduction script and relevant tests to ensure only one URLResolver is constructed and caches are reused.
- [ ] 6. Log findings and mark TODOs complete as work progresses and create checkpoints with context_commit when milestones are reached.

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:22] **swebench-django__django-11333**: Task completed: Submitted
- [2025-12-01 21:22] **swebench-django__django-11333**: Move lru_cache to internal _get_resolver and resolve settings.ROOT_URLCONF in get_resolver so memoiz...
## Interaction Log

- `21:22:12` ACTION: Submitting solution
- `21:22:09` ACTION: git add -A && git --no-pager diff --staged
- `21:22:08` Checkpoint: implemented and tested fix to get_resolver
- `21:22:08` Root cause: get_resolver lru_cache used the original function argument (None) as cache key when called without urlconf; fix: resolve settings.ROOT_URL...
- `21:22:08` Reproduce: test_repro.py showed get_resolver(None) and get_resolver(settings.ROOT_URLCONF) returned same instance; only 1 URLResolver constructed
- `21:21:47` test_repro.py: get_resolver(None) and get_resolver(settings.ROOT_URLCONF) returned the same instance; only 1 URLResolver constructed
- `21:21:45` ACTION: Reading file: test_repro.py
- `21:21:11` ACTION: nl -ba django/urls/resolvers.py | sed -n '360,520p'
- `21:21:07` RESULT: django/urls/resolvers.py:369:class URLResolver:
- `21:21:06` ACTION: grep -nR "class URLResolver" -n django/urls || true
- `21:20:58` Patched get_resolver: moved lru_cache to _get_resolver and made get_resolver resolve settings.ROOT_URLCONF before calling the memoized helper
- `21:20:53` RESULT: patched get_resolver
- `21:20:52` ACTION: python3 - <<'PY'
- `21:20:32` ACTION: nl -ba django/urls/resolvers.py | sed -n '60,80p'
- `21:20:12` Found get_resolver at django/urls/resolvers.py:66; it is decorated with functools.lru_cache and sets urlconf = settings.ROOT_URLCONF inside the functi...
- `21:19:59` ACTION: nl -ba django/urls/resolvers.py | sed -n '1,260p'
- `21:19:53` ACTION: grep -nR "get_resolver" django/urls || true
- `21:19:37` ACTION: ls -la
- `21:19:35` TASK STARTED: Optimization: Multiple URLResolvers may be unintentionally be constructed by calls to `django.urls.resolvers.get_resolver`
