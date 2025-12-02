"""Agent with context management framework integration."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from minisweagent_tool.agents.default import DefaultAgent, AgentConfig


@dataclass
class ContextAwareAgentConfig(AgentConfig):
    """Configuration for context-aware agent."""
    enable_context: bool = True
    context_branch: str | None = None  # Auto-generated if None


def _truncate_message(content: str, max_length: int = 200) -> str:
    """Truncate a message for logging, keeping it informative but concise."""
    if not content:
        return "(empty)"
    
    # Remove excessive whitespace
    content = ' '.join(content.split())
    
    if len(content) <= max_length:
        return content
    
    # Try to truncate at a sentence boundary
    truncated = content[:max_length]
    last_period = truncated.rfind('.')
    last_newline = truncated.rfind('\n')
    
    cut_point = max(last_period, last_newline)
    if cut_point > max_length // 2:
        return truncated[:cut_point + 1] + " [...]"
    
    return truncated + " [...]"


def _extract_action_summary(action: str) -> str:
    """Extract a concise summary from an agent action."""
    if not action:
        return "(no action)"
    
    # Clean up the action
    action = action.strip()
    
    # Get first line or command
    first_line = action.split('\n')[0].strip()
    
    # For common patterns, extract key info
    if first_line.startswith('context_'):
        return first_line[:100]
    elif 'cat ' in first_line or 'head ' in first_line:
        return f"Reading file: {first_line.split()[-1] if first_line.split() else first_line}"
    elif first_line.startswith('find ') or first_line.startswith('grep '):
        return _truncate_message(first_line, 100)
    elif first_line.startswith('edit '):
        return f"Editing file (edit command)"
    elif 'COMPLETE_TASK' in action or 'submit' in action.lower():
        return "Submitting solution"
    
    return _truncate_message(first_line, 100)


def _extract_observation_summary(output: str, max_length: int = 150) -> str:
    """Extract a concise summary from command output."""
    if not output:
        return "(no output)"
    
    output = output.strip()
    lines = output.split('\n')
    
    # If output is short, return it
    if len(output) <= max_length:
        return output
    
    # For file listings, summarize
    if len(lines) > 10 and all(l.strip() for l in lines[:5]):
        return f"({len(lines)} lines of output) First: {lines[0][:50]}..."
    
    # For errors, prioritize error messages
    for line in lines:
        if 'error' in line.lower() or 'exception' in line.lower():
            return f"ERROR: {_truncate_message(line, max_length)}"
    
    return _truncate_message(output, max_length)


class ContextAwareMixin:
    """Mixin class that can be added to any agent for context management."""
    
    def __init__(self, *args, context_manager=None, **kwargs):
        """Initialize context management (call this in your __init__)."""
        self.context_manager = context_manager
        self._step_count = 0
        self._context_initialized = False
        self._last_logged_action = None
        
        # Get config (works with any agent that has self.config)
        if hasattr(self, 'config'):
            # Ensure config has context settings
            if not hasattr(self.config, 'enable_context'):
                self.config.enable_context = getattr(self.config, 'enable_context', True)
    
    def _init_context(self, task: str):
        """Initialize context management for this task."""
        if not getattr(self.config, 'enable_context', True) or not self.context_manager:
            return
        
        # If a branch name is provided, ensure it's fresh (delete if exists for reruns)
        branch_name = getattr(self.config, 'context_branch', None)
        if branch_name:
            # Delete existing branch to start fresh on reruns
            self.context_manager.delete_branch(branch_name)
            # Create fresh empty branch
            self.context_manager.branch_command(
                name=branch_name,
                empty=True
            )
        else:
            # No branch specified - generate a unique default branch name
            default_branch = f"task-{hash(task) % 10000}"
            self.context_manager.delete_branch(default_branch)
            self.context_manager.branch_command(name=default_branch, empty=True)
        
        self._context_initialized = True
        
        # Initialize main.md with task description and prompt for TODOs
        self._initialize_task_context(task)
    
    def _initialize_task_context(self, task: str):
        """Initialize main.md with task info and create initial commit."""
        if not self.context_manager:
            return
        
        # Extract a concise task title (first line or first sentence)
        task_lines = task.strip().split('\n')
        task_title = task_lines[0][:150] if task_lines else "Unknown task"
        
        # Create initial commit with branch purpose
        try:
            from minisweagent_tool.agents.contextmanager.models import CommitEntry, generate_commit_id, get_current_timestamp
            
            initial_commit = CommitEntry(
                commit_id=generate_commit_id(),
                branch_purpose=task_title,
                commit_contribution=f"Task initialized: {task_title}",
                timestamp=get_current_timestamp(),
                parent_commit=None
            )
            
            branch = self.context_manager.filesystem.get_current_branch()
            if branch:
                self.context_manager.filesystem.append_commit(branch, initial_commit)
        except Exception:
            pass
        
        # Create initial log entry
        self._log_context(f"TASK STARTED: {task_title}")
        
        # Update main.md with the task description
        try:
            main_content = self.context_manager.filesystem.read_main_md()
            
            # Replace the template placeholder with actual task info
            task_section = f"**Current Task:** {task_title}\n"
            if len(task) > 150:
                task_section += f"\n<details>\n<summary>Full description</summary>\n\n{task[:800]}{'...' if len(task) > 800 else ''}\n</details>\n"
            
            # Replace placeholder or insert after Project Goals
            if "<!-- High-level description" in main_content:
                main_content = main_content.replace(
                    "<!-- High-level description of the project's purpose and objectives -->",
                    task_section
                )
            elif "# Project Goals" in main_content:
                main_content = main_content.replace(
                    "# Project Goals\n",
                    f"# Project Goals\n\n{task_section}\n"
                )
            
            self.context_manager.filesystem.write_main_md(main_content)
        except Exception:
            pass  # Non-critical, continue without main.md update
    
    def _log_interaction(self, direction: str, content: str, content_type: str = "message"):
        """Log an agent-user interaction with appropriate summarization."""
        if not self._context_initialized or not self.context_manager:
            return
        
        if direction == "agent_action":
            summary = _extract_action_summary(content)
            self._log_context(f"ACTION: {summary}")
        elif direction == "observation":
            summary = _extract_observation_summary(content)
            self._log_context(f"RESULT: {summary}")
        elif direction == "user":
            summary = _truncate_message(content, 150)
            self._log_context(f"USER: {summary}")
        elif direction == "thinking":
            # Only log substantial thinking
            if len(content) > 50:
                summary = _truncate_message(content, 200)
                self._log_context(f"THINKING: {summary}")
    
    def _log_context(self, reasoning_step: str):
        """Log a reasoning step to context management."""
        if not getattr(self.config, 'enable_context', True) or not self.context_manager:
            return
        
        # Avoid duplicate logs
        if hasattr(self, '_last_log') and self._last_log == reasoning_step:
            return
        self._last_log = reasoning_step
        
        self.context_manager.log_command(reasoning_step=reasoning_step)
    
    def _commit_context(self, message: str | None = None):
        """Create a checkpoint in context management."""
        if not getattr(self.config, 'enable_context', True) or not self.context_manager:
            return

        if message:
            self.context_manager.commit_command(message=message)
        else:
            # Auto-generate from recent logs
            self.context_manager.commit_command(from_log="last:5")


class ContextAwareAgent(DefaultAgent, ContextAwareMixin):
    """Agent that integrates with context management framework.
    
    The LM can call context management commands directly:
    - context_log "reasoning step"
    - context_commit --message "checkpoint message"
    - context_commit --from-log last:5
    - context_branch --name branch-name [--empty] [--from-branch name]
    - context_merge branch1 branch2 [branch3 ...]
    - context_info --level project|branch|session [--branch name]
    - context_status
    """
    
    def __init__(self, *args, context_manager=None, **kwargs):
        """Initialize with optional context manager.
        
        Args:
            context_manager: Context management framework instance (optional)
            **kwargs: Passed to DefaultAgent
        """
        super().__init__(*args, config_class=ContextAwareAgentConfig, **kwargs)
        ContextAwareMixin.__init__(self, context_manager=context_manager)
    
    def execute_action(self, action: dict) -> dict:
        """Override to handle context management commands and && chains."""
        action_str = action.get("action", "").strip()
        
        # Log the action (unless it's a context command - those are meta)
        if not action_str.startswith("context_"):
            self._log_interaction("agent_action", action_str)
        
        # Only intercept && chains if they contain context commands
        if " && " in action_str:
            commands = [cmd.strip() for cmd in action_str.split(" && ")]
            has_context_command = any(cmd.startswith("context_") for cmd in commands)
            if has_context_command:
                result = self._execute_command_chain(action_str)
            else:
                result = super().execute_action(action)
        elif action_str.startswith("context_"):
            result = self._execute_context_command(action_str)
        else:
            result = super().execute_action(action)
        
        # Log the observation/result (unless it's a context command)
        if not action_str.startswith("context_") and result.get("output"):
            self._log_interaction("observation", result.get("output", ""))
        
        return result
    
    def _execute_command_chain(self, command_chain: str) -> dict:
        """Execute a chain of commands separated by &&."""
        commands = [cmd.strip() for cmd in command_chain.split(" && ")]
        combined_output = []
        combined_returncode = 0

        for cmd in commands:
            # Check if this is a context command
            if cmd.startswith("context_"):
                result = self._execute_context_command(cmd)
            else:
                # Regular shell command – call env directly so we don't terminate
                # early on intermediate commands that might print the magic word.
                result = self.env.execute(cmd)
            
            # Collect output
            output = result.get("output", "")
            returncode = result.get("returncode", 0)
            
            if output:
                combined_output.append(output)
            combined_returncode = returncode
            
            # If command failed, stop chain (like bash && behavior)
            if returncode != 0:
                break

        result = {
            "output": "\n".join(combined_output),
            "returncode": combined_returncode,
            "action": command_chain,
        }
        # Only check for submission after the full chain has run so that
        # `echo COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT && git diff --cached`
        # captures the diff instead of terminating at the echo.
        self.has_finished(result)
        return result
    
    def _execute_context_command(self, command: str) -> dict:
        """Execute a context management command."""
        if not self.context_manager or not self._context_initialized:
            return {
                "output": "Context management not available",
                "returncode": 1,
                "action": command
            }
        
        # Track that a context command was used
        self._last_context_command_step = self._step_count
        
        parts = command.split(None, 1)
        cmd_name = parts[0] if parts else ""
        args_str = parts[1] if len(parts) > 1 else ""
        
        try:
            if cmd_name == "context_log":
                # Parse: context_log "reasoning step"
                if not args_str:
                    return {"output": "Error: context_log requires a reasoning step", "returncode": 1, "action": command}
                # Remove quotes if present
                reasoning = args_str.strip('"\'')
                self.context_manager.log_command(reasoning_step=reasoning)
                return {"output": f"✓ Logged to context", "returncode": 0, "action": command}
            
            elif cmd_name == "context_commit":
                # Parse: context_commit --message "msg" or context_commit --from-log last:5
                message = None
                from_log = None
                
                if "--message" in args_str:
                    # Extract message
                    import re
                    match = re.search(r'--message\s+["\']?([^"\']+)["\']?', args_str)
                    if match:
                        message = match.group(1)
                elif "--from-log" in args_str:
                    # Extract from_log
                    import re
                    match = re.search(r'--from-log\s+(\S+)', args_str)
                    if match:
                        from_log = match.group(1)
                
                self.context_manager.commit_command(message=message, from_log=from_log)
                return {"output": f"✓ Committed to context", "returncode": 0, "action": command}
            
            elif cmd_name == "context_branch":
                # Parse: context_branch --name branch-name [--empty] [--from-branch name]
                import re
                name_match = re.search(r'--name\s+(\S+)', args_str)
                if not name_match:
                    return {"output": "Error: context_branch requires --name", "returncode": 1, "action": command}
                
                name = name_match.group(1)
                empty = "--empty" in args_str
                from_branch = None
                from_match = re.search(r'--from-branch\s+(\S+)', args_str)
                if from_match:
                    from_branch = from_match.group(1)
                
                self.context_manager.branch_command(name=name, empty=empty, from_branch=from_branch)
                return {"output": f"✓ Switched to branch '{name}'", "returncode": 0, "action": command}
            
            elif cmd_name == "context_info":
                # Parse: context_info [--level project|branch|session] [--branch name] [--brief]
                import re
                level = "branch"
                branch_name = None
                brief = "--brief" in args_str
                
                level_match = re.search(r'--level\s+(\S+)', args_str)
                if level_match:
                    level = level_match.group(1)
                
                branch_match = re.search(r'--branch\s+(\S+)', args_str)
                if branch_match:
                    branch_name = branch_match.group(1)
                
                info_output = self.context_manager.info_command(level=level, branch_name=branch_name, brief=brief)
                return {"output": info_output, "returncode": 0, "action": command}
            
            elif cmd_name == "context_status":
                status_output = self.context_manager.status_command()
                return {"output": status_output, "returncode": 0, "action": command}
            
            elif cmd_name == "context_summary":
                # Quick summary of current progress - useful for recalling where you are
                summary_output = self.context_manager.summary_command()
                return {"output": summary_output, "returncode": 0, "action": command}
            
            elif cmd_name == "context_todos":
                # Parse: context_todos [--add "item"] [--complete N]
                import re
                action = "list"
                item = None
                todo_id = None
                
                if "--add" in args_str:
                    action = "add"
                    match = re.search(r'--add\s+["\']([^"\']+)["\']', args_str)
                    if match:
                        item = match.group(1)
                    else:
                        # Try without quotes
                        match = re.search(r'--add\s+(\S+)', args_str)
                        if match:
                            item = match.group(1)
                elif "--complete" in args_str:
                    action = "complete"
                    match = re.search(r'--complete\s+(\d+)', args_str)
                    if match:
                        todo_id = int(match.group(1))
                
                todos_output = self.context_manager.todos_command(action=action, item=item, todo_id=todo_id)
                return {"output": todos_output, "returncode": 0, "action": command}
            
            elif cmd_name == "context_merge":
                # Parse: context_merge branch1 branch2 [branch3 ...]
                branch_names = args_str.split()
                if not branch_names:
                    return {"output": "Error: context_merge requires at least one branch name", "returncode": 1, "action": command}
                
                self.context_manager.merge_command(branches=branch_names)
                return {"output": f"✓ Merged {len(branch_names)} branch(es) into current branch", "returncode": 0, "action": command}
            
            else:
                return {"output": f"Unknown context command: {cmd_name}", "returncode": 1, "action": command}
        
        except Exception as e:
            return {"output": f"Error: {str(e)}", "returncode": 1, "action": command}
    
    def run(self, task: str, **kwargs) -> tuple[str, str]:
        """Run with context management integration."""
        self._init_context(task)
        self._step_count = 0
        
        try:
            exit_status, result = super().run(task, **kwargs)
            
            # Final commit on completion (optional - LM can do this too)
            if self._context_initialized:
                self._commit_context(f"Task completed: {exit_status}")
            
            return exit_status, result
        except Exception as e:
            if self._context_initialized:
                self._log_context(f"Error occurred: {type(e).__name__}: {str(e)}")
            raise
    
    def add_message(self, role: str, content: str, **kwargs):
        """Override to inject context commands into system prompt only."""
        # Inject context commands into system template
        if (role == "system" and 
            getattr(self.config, 'enable_context', True) and 
            self.context_manager and
            "TODO-Driven Workflow" not in content):  # Check for new template marker
            from minisweagent_tool.agents.context_commands_template import CONTEXT_COMMANDS_TEMPLATE, LIMITED_CONTEXT_WARNING
            content = content.rstrip() + "\n\n" + CONTEXT_COMMANDS_TEMPLATE
            
            # Add limited context warning if max_context_tokens is set
            max_tokens = getattr(self.config, 'max_context_tokens', 0)
            if max_tokens > 0:
                content = LIMITED_CONTEXT_WARNING.format(max_context_tokens=max_tokens) + "\n" + content
        
        return super().add_message(role, content, **kwargs)
    
    def step(self) -> dict:
        """Override step - context commands are handled in execute_action."""
        self._step_count += 1
        result = super().step()
        
        # Log thinking/reasoning if present in the response
        if isinstance(result, dict):
            thought = result.get("thought") or result.get("thinking") or result.get("reasoning")
            if thought and len(str(thought)) > 30:
                self._log_interaction("thinking", str(thought))
        
        return result
    
    def get_observation(self, response: dict) -> dict:
        """Override to handle context commands."""
        return super().get_observation(response)
    
    def _extract_thought_from_response(self, text: str) -> str | None:
        """Extract thought/reasoning from model response."""
        if not text:
            return None
        
        # Look for thought patterns
        import re
        patterns = [
            r'<thought>(.*?)</thought>',
            r'<thinking>(.*?)</thinking>',
            r'THOUGHT:\s*(.*?)(?:\n\n|ACTION:)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None

