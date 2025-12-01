"""Template snippet for context management commands in system prompts."""

# Warning shown when context is artificially limited
LIMITED_CONTEXT_WARNING = """
## ⚠️ Limited Context Window

Your context window is limited to {max_context_tokens} tokens. As the conversation grows, older messages will be dropped.

**CRITICAL: Your context persists outside the conversation window. Use it!**

Your TODO list, logs, and commits are stored in `.context/` and survive context truncation.
When you feel lost or the conversation seems incomplete, run `context_summary` to recall your progress.
"""

CONTEXT_COMMANDS_TEMPLATE = """
## Context Management - TODO-Driven Workflow

You have a persistent context system that survives conversation truncation. **Follow this workflow strictly.**

### 🎯 Task Focus & Boundaries

- **Primary goal:** Fix the specific bug / implement the behavior described in the task, nothing more.
- **Only modify code that is directly required** to satisfy the task description or PR diff.
- **Do NOT:**
  - Refactor unrelated modules or error messages.
  - Chase generic test infrastructure or environment issues unless the task explicitly asks.
  - Introduce new features beyond what the task requires.
- **When the minimal patch is implemented and sanity-checked, STOP and submit** instead of exploring additional improvements.

### ⚡ REQUIRED Workflow

**STEP 1: ANALYZE & PLAN (First thing after receiving a task)**
**CRITICAL: Check if TODOs already exist before creating new ones!**

1. **First, check existing TODOs:**
   ```
   context_todos
   ```
   If TODOs already exist, use `context_summary` to see your current progress and continue from there. **DO NOT create duplicate TODOs.**

2. **Only if no TODOs exist, create a detailed TODO list:**
   ```
   context_todos --add "1. Analyze the codebase: find and read relevant files"
   context_todos --add "2. Create a minimal script to reproduce the issue"
   context_todos --add "3. Edit source code to resolve the issue"
   context_todos --add "4. Verify fix works by running the reproduction script once"
   context_todos --add "5. Submit immediately if verification passes"
   ```

**Note:** The verification script should be MINIMAL - just enough to confirm the fix works. Do NOT test extensive edge cases unless the task explicitly requires it.

**STEP 2: WORK ON EACH TODO**
For each TODO:
1. **After each command**, log a summary of what you learned
2. Log your findings and decisions
3. When done, mark complete: `context_todos --complete N` (saves progress to context)

**CRITICAL: Log in a SEPARATE step AFTER seeing output.**

The `context_log` command is intercepted before bash runs, so `$(...)` and `$VAR` will NOT be expanded.

✗ **WRONG** - bash variables won't work:
```bash
result=$(grep foo file.py) && context_log "found: $result"  # $result is literal text!
```

✓ **RIGHT** - run command first, then log separately:
```bash
# Step N: run command and see output
grep -n "__getattr__" astropy/coordinates/*.py
```
Then in your NEXT response, after seeing the output:
```bash
# Step N+1: log with actual values you observed
context_log "grep __getattr__: sky_coordinate.py:869,898 frame.py:234"
```

**Always use literal values you saw in the output, never bash variables or substitutions.**

**STEP 3: VERIFY & SUBMIT (Critical - Do This Once, Then STOP)**
Following the recommended workflow, after implementing your fix:
1. **Run your reproduction script ONCE** to verify the fix works (this is the script you created in STEP 1)
2. **If verification passes, IMMEDIATELY submit ONCE** - do NOT:
   - Run the script multiple times
   - Create additional verification scripts
   - Run echo/printf commands to "confirm" completion
   - Test extensive edge cases (unless task explicitly requires)
   - Add extra TODOs after the fix is done
   - Run `context_summary` or other commands after submission
3. **Use the exact submission command from the task instructions as a STANDALONE command** (typically `echo COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT && git add -A && git diff --cached`)

**CRITICAL: The submission command must be run ALONE, not combined with context commands!**

✗ **WRONG** - Don't combine submission with context commands:
```bash
context_log "..." && context_todos --complete 5 && echo COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT && git add -A && git diff --cached
```

✓ **RIGHT** - Run submission as a standalone command:
```bash
echo COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT && git add -A && git diff --cached
```

**If you need to mark TODOs complete or log before submitting, do that in a SEPARATE command first, then submit in the NEXT response.**

**CRITICAL: Submission is FINAL - After you see the diff output, the task is COMPLETE. DO NOT:**
- Submit again (you already submitted!)
- Run any more commands
- Check context_summary
- Add more TODOs
- Do anything else

**When verification passes, submit ONCE. After you see the diff output, STOP - the task is done.**

**STEP 4: RECOVER WHEN LOST**
If context was truncated and you feel lost:
```
context_summary
```
This shows your TODOs, milestones, and recent activity.

### Commands Reference

| Command | Purpose |
|---------|---------|
| `context_todos` | View your TODO list |
| `context_todos --add "task"` | Add a TODO (be specific!) |
| `context_todos --complete N` | Mark TODO #N done (saves to context) |
| `context_log "message"` | Log a finding, decision, or observation |
| `context_commit --message "..."` | Manual checkpoint at a milestone |
| `context_summary` | **Primary recovery command** - shows progress |

### What to Log (Real Values From Output)

**In a SEPARATE response after seeing command output, log what you found:**

| After seeing... | In NEXT response, log... |
|-----------------|--------------------------|
| grep output | `context_log "grep __getattr__: sky_coordinate.py:869,898 frame.py:234"` |
| file content | `context_log "sky_coordinate.py:860-920: __getattr__ catches AttributeError at 898"` |
| error message | `context_log "repro.py: AttributeError 'no attr prop' at line 898"` |
| test results | `context_log "test_sky_coord.py: 47 passed, 2 failed"` |

**Also log key insights:**
- `context_log "Root cause: __getattr__ catches property's AttributeError, re-raises with wrong attr"`
- `context_log "Fix: check class descriptors first, let their errors propagate"`

**NEVER use:** `$VAR`, `$(...)`, `${...}` - these won't be expanded!

### TODO Guidelines (Be Specific!)

**Good TODOs:**
- "Create a minimal script to reproduce the bug using SkyCoord subclass example from issue"
- "Find __getattr__ method in sky_coordinate.py causing AttributeError"
- "Update validators in django/contrib/auth/validators.py to use \\A...\\Z"
- "Verify fix by running the reproduction script once"

**Bad TODOs:**
- "Fix the bug" (too vague)
- "Look at code" (not actionable)
- "Debug" (not specific)
- "Improve generic error messages in unrelated modules"
- "Clean up test infrastructure not mentioned in the task"

### Example Session (Each box = one response)

```
# Response 1: ALWAYS check if TODOs exist first
context_todos
```

```
# Response 2a: If TODOs exist, use context_summary to see progress
context_summary
```

```
# Response 2b: If NO TODOs exist, create TODO list
context_todos --add "1. Reproduce bug" && context_todos --add "2. Locate __getattr__" && context_todos --add "3. Fix" && context_todos --add "4. Test"
```

```
# Response 3: Run grep (just the command, no context_log yet)
grep -n "__getattr__" astropy/coordinates/*.py
```

```
# Response 4: AFTER seeing grep output, log what you found with actual values
context_log "grep __getattr__: sky_coordinate.py:869,898,906 frame.py:234"
```

```
# Response 5: Read the file
sed -n '860,920p' astropy/coordinates/sky_coordinate.py  
```

```
# Response 6: AFTER seeing file content, log what you learned
context_log "sky_coordinate.py:869-920: __getattr__ catches AttributeError at 898, re-raises with wrong attr"
```

```
# Response 7: Run repro script
python3 repro.py
```

```
# Response 8: AFTER seeing error, log it and mark TODO complete
context_log "repro.py: AttributeError 'no attr prop' at line 898" && context_todos --complete 1
```

```
# Response 9: After fix is implemented, run the reproduction script ONCE to verify
python3 repro_script.py
```

```
# Response 10: If verification passes, mark final TODO complete (if needed) in a separate command
context_todos --complete 5
```

```
# Response 11: Submit as a STANDALONE command (do NOT combine with context commands)
echo COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT && git add -A && git diff --cached
```

**After Response 11: You see the diff output. The task is COMPLETE. DO NOT run any more commands.**

```
# If context truncated BEFORE submission, recover with:
context_summary
```

### Remember
- TODOs persist across context truncation - they're your roadmap
- **ALWAYS check `context_todos` first** - if TODOs exist, use `context_summary` to see progress. **DO NOT create duplicate TODOs.**
- Logs are your memory - be concise but capture key details
- Completing a TODO = automatic context checkpoint (NOT a git commit)
- When confused, `context_summary` is your friend
- **NEVER run `git commit` before the final submission** - it will cause your patch to be empty
- **After verification passes, submit ONCE** - do not run confirmation loops or extra checks
- **One verification is enough** - if it works, submit. If it fails, fix and verify once more, then submit
- **SUBMISSION IS FINAL** - After you see the diff output from the submission command, the task is COMPLETE. **DO NOT submit again or run any more commands.**
"""
