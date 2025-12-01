# Context Management Framework Integration

This guide shows how to integrate the context management framework with mini-swe-agent to improve performance and debugging.

## Overview

The context management framework allows the agent to:
- **Log reasoning steps** during problem-solving
- **Create checkpoints** at milestones
- **Track progress** across instances
- **Resume work** from checkpoints if interrupted

## Installation

1. Install the context management framework in your environment
2. Ensure it's accessible via CLI or MCP

## Basic Usage

### Using ContextAwareAgent

```python
from minisweagent.agents.context_aware import ContextAwareAgent, get_context_manager
from minisweagent.models import get_model
from minisweagent.environments import get_environment

# Get context manager (optional - will gracefully degrade if unavailable)
context_manager = get_context_manager(enable=True)

# Create agent with context management
agent = ContextAwareAgent(
    get_model(model_name="openai/gpt-5-mini"),
    get_environment(),
    context_manager=context_manager,
    enable_context=True,
    context_commit_interval=10,  # Commit every 10 steps
)

# Run task - context will be automatically logged
exit_status, result = agent.run("Fix the bug in auth.py")
```

### Configuration

In your config YAML:

```yaml
agent:
  enable_context: true  # Turn context management on
```

## Integration with SWE-bench

`src/minisweagent/run/extra/swebench.py` already integrates the context framework:

- It calls `get_context_manager(enable=agent.enable_context)` to obtain a context manager.
- When available, it uses `ContextProgressAgent`, which combines:
  - The normal SWE-bench progress reporting, and
  - The context-aware behavior from `ContextAwareAgent`.
- Each SWE-bench instance uses a dedicated branch:

```python
class ContextProgressAgent(ContextAwareAgent):
    def __init__(..., instance_id: str = "", context_manager=None, **kwargs):
        super().__init__(*args, context_manager=context_manager, **kwargs)
        self.instance_id = instance_id
        if instance_id and not getattr(self.config, "context_branch", None):
            self.config.context_branch = f"swebench-{instance_id}"
```

To enable context on SWE-bench runs, just set in your config:

```yaml
agent:
  enable_context: true
```

## Benefits

### 1. Better Debugging
- See reasoning steps in `.context/branches/<branch>/log.yaml`
- Review checkpoints in `.context/branches/<branch>/commits.yaml`

### 2. Resume Capability
- If an instance fails, you can review context and resume
- Checkpoints show what was tried and what worked

### 3. Cross-Instance Learning
- Merge context from successful instances
- Track patterns: "What approaches work for similar bugs?"

### 4. Performance Analysis
- See which reasoning steps lead to solutions
- Identify bottlenecks in problem-solving

## Example Workflow

1. **Start SWE-bench run:**
   ```bash
   mini-extra swebench --model openai/gpt-5-mini --subset verified --slice 0:5
   ```

2. **Check context during run:**
   ```bash
   # View current branch context
   python3 -m src.cli info --level branch
   
   # View reasoning logs
   cat .context/branches/swebench-astropy__astropy-12907/log.yaml
   ```

3. **Review checkpoints:**
   ```bash
   # See commit history
   python3 -m src.cli info --level branch
   ```

4. **Merge successful patterns:**
   ```bash
   # After successful instances, merge their context
   python3 -m src.cli merge swebench-successful-1 swebench-successful-2
   ```

## Graceful Degradation

The integration is designed to gracefully degrade:
- If context framework is unavailable, agent works normally
- If context operations fail, they're silently skipped
- No breaking changes to existing code

## Configuration

Add to `swebench.yaml`:

```yaml
agent:
  enable_context: true
  context_commit_interval: 10
  context_log_reasoning: true
  # ... other agent config
```

Or disable per-run:
```bash
mini-extra swebench --model ... --config custom-config.yaml
```

Where `custom-config.yaml` has `enable_context: false`.

