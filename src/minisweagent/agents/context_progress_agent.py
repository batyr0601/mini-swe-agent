"""Agent that combines context management with progress tracking for SWE-bench."""

from minisweagent.agents.context_aware import ContextAwareAgent


class ContextProgressAgent(ContextAwareAgent):
    """Agent that combines progress tracking with context management.
    
    This is designed for SWE-bench runs where you want both:
    - Progress updates (like ProgressTrackingAgent)
    - Context management (like ContextAwareAgent)
    
    The LM can call context management commands directly:
    - context_log "reasoning step"
    - context_commit --message "checkpoint message"
    - context_commit --from-log last:5
    - context_branch --name branch-name [--empty] [--from-branch name]
    - context_merge branch1 branch2 [branch3 ...]
    - context_info --level project|branch|session [--branch name]
    - context_status
    """
    
    def __init__(self, *args, progress_manager=None, instance_id: str = "", context_manager=None, **kwargs):
        """Initialize with progress tracking and context management.
        
        Args:
            progress_manager: Progress manager for batch runs
            instance_id: Instance ID for progress tracking
            context_manager: Context management framework instance
            **kwargs: Passed to ContextAwareAgent
        """
        super().__init__(*args, context_manager=context_manager, **kwargs)
        self.progress_manager = progress_manager
        self.instance_id = instance_id
        # Set default branch per instance if not already set
        if instance_id and not getattr(self.config, 'context_branch', None):
            self.config.context_branch = f"swebench-{instance_id}"
    
    def step(self) -> dict:
        """Override step to provide progress updates."""
        # Progress update
        if self.progress_manager:
            self.progress_manager.update_instance_status(
                self.instance_id, f"Step {self.model.n_calls + 1:3d} (${self.model.cost:.2f})"
            )
        
        # Call parent step (handles context commands)
        return super().step()

