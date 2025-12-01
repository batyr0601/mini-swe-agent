"""Default templates for context files"""


def get_main_md_template() -> str:
    """Template for main.md"""
    return """# Project Goals

<!-- High-level description of the project's purpose and objectives -->

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

## Interaction Log

<!-- Recent agent actions and results are summarized here -->

"""


def get_commits_yaml_template() -> str:
    """Template for commits.yaml (empty initially, first commit will define branch purpose)"""
    return """# Branch Commit History
# Commits will be added here as the branch progresses

commits: []

"""


def get_log_yaml_template() -> str:
    """Template for log.yaml (empty initially)"""
    return """# Reasoning Log
# Fine-grained reasoning cycles will be logged here

logs: []

"""


def get_metadata_yaml_template() -> str:
    """Template for metadata.yaml"""
    return """# Branch Metadata

file_structure: {}
  # Example structure:
  # src/
  #   - main.py: "Main entry point"
  #   - utils.py: "Utility functions"

env_config: {}
  # Example:
  # python_version: "3.9+"
  # dependencies: ["click", "pyyaml"]

# Add custom metadata entries below as needed

"""

