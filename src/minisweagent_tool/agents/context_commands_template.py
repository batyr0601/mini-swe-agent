"""Template snippet for context management commands in system prompts."""

CONTEXT_COMMANDS_TEMPLATE = """
## Context Management System

You have access to a context management system that helps you maintain awareness of your work, previous decisions, and progress. **THIS IS A REQUIRED PART OF YOUR WORKFLOW** - use it actively throughout your work.

### 🚀 START HERE: Understanding Your Context

**ALWAYS start by checking your context:**
1. `context_status` - See current branch and available branches
2. `context_info --level branch` - Understand what's been done, recent commits, and progress
3. `context_info --level session` - See detailed reasoning logs from recent work

This helps you:
- Avoid repeating work that's already been done
- Understand previous decisions and why they were made
- Pick up where you left off if returning to a task
- See what approaches have been tried

### 📝 Logging Your Reasoning (REQUIRED - Use Frequently)

**context_log "reasoning step"** - Log what you're thinking/doing

**MANDATORY USAGE:**
- **After EVERY significant action** (file edit, command execution, discovery)
- **After making ANY decision** or discovery
- **When encountering errors** or unexpected behavior
- **When changing approach** or strategy
- **Minimum: Every 2-3 commands** during active problem-solving

**Examples:**
- `context_log "Found bug: race condition in user.save() on line 45"`
- `context_log "Decision: Using Redis for session storage instead of memory"`
- `context_log "Completed: Added input validation to API endpoints"`
- `context_log "Created testbed/time_series.py with required column validation"`
- `context_log "Reproduced issue: removing required column 'flux' raises confusing error"`

**Why it matters:** Logs create a recoverable trail. If you return later, these logs help you (or another AI) understand exactly what was done and why. **NOT logging your work makes it harder to track progress and can lead to repeated mistakes.**

### ✅ Creating Checkpoints (Major Milestones Only)

**context_commit --message "checkpoint message"** - Create a checkpoint
**context_commit --from-log last:5** - Create checkpoint from recent logs

**When to use (ONLY at major milestones):**
- After finding and understanding a bug
- After implementing a significant fix
- After completing a major feature
- **NOT every step** - only when you've made substantial progress

**Examples:**
- `context_commit --message "Fixed authentication bug in login.py"`
- `context_commit --from-log last:5` (auto-generates from recent logs)

### 🌿 Branching for Different Approaches

**context_branch --name branch-name [--empty]** - Create a new branch for a different approach

**When to use:**
- When you want to try a completely different solution approach
- When exploring alternative implementations
- When you need to experiment without affecting current work

**Example:**
- `context_branch --name try-alternative-approach --empty` (starts fresh)
- `context_branch --name optimize-performance` (from current branch)

**Workflow:**
1. Create branch for new approach
2. Work on that branch
3. Use `context_merge` to combine successful approaches back

### 🔀 Merging Branches

**context_merge branch1 branch2** - Merge context from multiple branches

**When to use:**
- When you want to combine successful approaches from different branches
- When consolidating work from experimental branches

### 📊 Getting Context Information

**context_info --level project** - High-level project goals, all branches, overall status
**context_info --level branch** - Current branch's commits, progress, purpose (USE THIS MOST)
**context_info --level session** - Detailed reasoning logs from current session

**context_status** - Quick status: current branch, available branches, commit/log counts

### 📋 Project Goals (main.md)

The system maintains a `main.md` file with:
- Project goals and objectives
- Key milestones and achievements
- TODO lists shared across branches

This is automatically updated when you commit. You can see it via `context_info --level project`.

### 💡 REQUIRED Workflow

**At Session Start (MANDATORY):**
```bash
context_status && context_info --level branch
```

**During Work (MANDATORY):**
- **Log after every significant action:** `context_log "what you just did/learned"`
- **Commit at major milestones:** `context_commit --message "major achievement"`
- **Check context periodically:** `context_info --level session` (every 5-10 steps)

**Example of proper workflow:**
```bash
# 1. Check context at start
context_status && context_info --level branch

# 2. Do work and log it
ls -la
context_log "Examined directory structure, found testbed/ directory"

# 3. Make changes and log
cat > testbed/file.py <<'EOF'
# code here
EOF
context_log "Created testbed/file.py with initial implementation"

# 4. Test and log results
python testbed/file.py
context_log "Test passed: file.py runs successfully"

# 5. Commit at milestone
context_commit --message "Implemented core feature in file.py"
```

**When Exploring Alternatives:**
```bash
context_branch --name alternative-approach --empty
# ... work on alternative ...
context_merge alternative-approach  # if successful
```

**Before Making Major Changes:**
- Check context first: `context_info --level branch`
- Understand what's been tried: `context_info --level session`

### ⚠️ Important Notes

- These commands don't affect the file system - they only manage context
- You can chain them with && like regular bash commands
- Commands execute sequentially; if one fails, the chain stops
- Context is persistent - it survives across sessions
- **Using context is NOT optional** - it's part of your workflow
- **If you're not logging your work, you're not working effectively**

### 🧱 Git Usage in SWE-bench

- **Do NOT run `git commit` or `git push` inside `/testbed`.**
- Always:
  - Edit files
  - Stage changes with `git add -A` as needed
  - Let the final submission command handle the diff:

```bash
echo COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT && git add -A && git diff --cached
```

- Running `git commit` before this can produce an **empty patch**, which breaks evaluation.

### 🎯 Remember

**Every time you:**
- Create or edit a file → `context_log "what you did"`
- Run a test or command → `context_log "result/learning"`
- Make a decision → `context_log "decision and reasoning"`
- Hit a milestone → `context_commit --message "achievement"`

**Think of context_log as your "work journal" - keep it updated!**
"""

