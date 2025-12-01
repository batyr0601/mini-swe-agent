"""Adapter for context management framework integration."""

import sys
import importlib.util
from pathlib import Path


class ContextManagerAdapter:
    """Adapter to interface with context management framework."""
    
    def __init__(self, workspace_path: str | None = None):
        """Initialize adapter with direct framework imports.
        
        Args:
            workspace_path: Optional explicit workspace path for .context folder.
                          If not provided, auto-detects from git root or cwd.
        """
        try:
            framework_path = Path(__file__).parent / "contextmanager"
            if not framework_path.exists():
                self.commands = None
                self._available = False
                return
            
            # Add the parent directory to sys.path so we can import the package
            parent_dir = str(framework_path.parent)
            if parent_dir not in sys.path:
                sys.path.insert(0, parent_dir)
            
            # Import using the actual directory structure
            # Since the directory has a hyphen, we need to use importlib
            pkg_name = "context_manager"
            init_file = framework_path / "__init__.py"
            
            # Load the package
            spec = importlib.util.spec_from_file_location(
                pkg_name, 
                init_file,
                submodule_search_locations=[str(framework_path)]
            )
            if spec is None or spec.loader is None:
                self.commands = None
                self._available = False
                return
            
            pkg = importlib.util.module_from_spec(spec)
            sys.modules[pkg_name] = pkg
            spec.loader.exec_module(pkg)
            
            # Now load submodules - they'll use relative imports which will work now
            for mod_name in ["filesystem", "commands"]:
                mod_file = framework_path / f"{mod_name}.py"
                mod_spec = importlib.util.spec_from_file_location(
                    f"{pkg_name}.{mod_name}",
                    mod_file
                )
                if mod_spec and mod_spec.loader:
                    mod = importlib.util.module_from_spec(mod_spec)
                    mod.__package__ = pkg_name
                    sys.modules[f"{pkg_name}.{mod_name}"] = mod
                    mod_spec.loader.exec_module(mod)
                    setattr(pkg, mod_name, mod)
            
            self.commands = pkg.commands
            self.filesystem = pkg.filesystem
            self._available = True
            
            # Set workspace path if provided
            if workspace_path:
                self.set_workspace(workspace_path)
        except Exception as e:
            # Store error for debugging
            import traceback
            self._error = f"{str(e)}\n{traceback.format_exc()}"
            self.commands = None
            self.filesystem = None
            self._available = False
    
    def set_workspace(self, path: str):
        """Set the workspace root for .context folder."""
        if not self._available:
            return
        self.filesystem.set_workspace_root(path)
        self.filesystem.ensure_context_directory()
        
    def log_command(self, reasoning_step: str):
        """Log a reasoning step."""
        if not self._available:
            return
        self.commands.log_command(reasoning_step=reasoning_step)
    
    def commit_command(self, message: str | None = None, from_log: str | None = None):
        """Create a commit."""
        if not self._available:
            return
        self.commands.commit_command(message=message, from_log_range=from_log)
    
    def branch_command(self, name: str, empty: bool = False, from_branch: str | None = None):
        """Create or switch to a branch."""
        if not self._available:
            return
        # If branch exists, switch to it (like CLI does)
        if self.filesystem.branch_exists(name):
            self.filesystem.set_current_branch(name)
        else:
            # Create new branch
            self.commands.branch_command(branch_name=name, from_branch=from_branch, empty=empty)
    
    def delete_branch(self, name: str):
        """Delete a branch (for fresh starts on reruns)."""
        if not self._available:
            return
        import shutil
        
        if self.filesystem.branch_exists(name):
            # If it's the current branch, clear current branch
            current = self.filesystem.get_current_branch()
            if current == name:
                # Clear current branch file
                context_dir = Path(self.filesystem.get_context_dir())
                current_branch_file = context_dir / ".current_branch"
                if current_branch_file.exists():
                    current_branch_file.unlink()
            
            # Delete branch directory
            branch_dir = Path(self.filesystem.get_branch_dir(name))
            if branch_dir.exists():
                shutil.rmtree(branch_dir)
    
    def merge_command(self, branches: list[str]):
        """Merge branches."""
        if not self._available:
            return
        self.commands.merge_command(source_branches=branches)
    
    def info_command(self, level: str = "branch", branch_name: str | None = None, format: str = "markdown") -> str:
        """Get context information."""
        if not self._available:
            return "Context management not available"
        try:
            print(f"ContextManagerAdapter INFO command: level='{level}' (branch={branch_name})")
            import io
            from contextlib import redirect_stdout
            f = io.StringIO()
            with redirect_stdout(f):
                self.commands.info_command(level=level, branch_name=branch_name, format=format)
            return f.getvalue()
        except Exception as e:
            return f"Error: {str(e)}"
    
    def status_command(self) -> str:
        """Get context status."""
        if not self._available:
            return "Context management not available"
        try:
            current_branch = self.filesystem.get_current_branch()
            branches = self.filesystem.list_branches()
            
            status = []
            status.append(f"Current branch: {current_branch or 'None'}")
            status.append(f"Available branches: {', '.join(branches) if branches else 'None'}")
            
            if current_branch:
                commits = self.filesystem.read_commits(current_branch)
                logs = self.filesystem.read_logs(current_branch)
                status.append(f"Commits: {len(commits)}, Log entries: {len(logs)}")
            
            return "\n".join(status)
        except Exception as e:
            return f"Error: {str(e)}"


def get_context_manager(enable: bool = True, workspace_path: str | None = None):
    """Get a context manager adapter instance.
    
    Args:
        enable: Whether to enable context management
        workspace_path: Optional explicit workspace path for .context folder
    
    Returns:
        ContextManagerAdapter instance or None if disabled/unavailable
    """
    if not enable:
        return None
    
    try:
        adapter = ContextManagerAdapter(workspace_path=workspace_path)
        return adapter if adapter._available else None
    except Exception:
        return None

