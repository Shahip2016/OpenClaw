from enum import Enum
from typing import List, Dict, Any, Optional

class Role(Enum):
    PI = "Principal Investigator"
    RESEARCHER = "Researcher"
    REVIEWER = "Reviewer"

class ResearchProject:
    def __init__(self, title: str, pi_id: str):
        self.title = title
        self.pi_id = pi_id
        self.members: Dict[str, Role] = {pi_id: Role.PI}
        self.tasks: List[Dict[str, Any]] = []
        self.status = "Proposed"

    def add_member(self, agent_id: str, role: Role):
        self.members[agent_id] = role

    def add_task(self, description: str, assigned_to: str):
        if assigned_to not in self.members:
            raise ValueError(f"Agent {assigned_to} is not a member of the project")
        self.tasks.append({
            "description": description,
            "assigned_to": assigned_to,
            "status": "Pending"
        })

class GovernanceEngine:
    def __init__(self):
        self.projects: Dict[str, ResearchProject] = {}

    def create_project(self, title: str, pi_id: str) -> ResearchProject:
        project = ResearchProject(title, pi_id)
        self.projects[title] = project
        return project

    def validate_action(self, project_title: str, agent_id: str, action_type: str) -> bool:
        project = self.projects.get(project_title)
        if not project:
            return False
        role = project.members.get(agent_id)
        
        # Simple role-based access control
        if action_type == "approve_task":
            return role == Role.PI
        if action_type == "submit_results":
            return role == Role.RESEARCHER
        if action_type == "critique":
            return role == Role.REVIEWER
        return True

# Global governance instance
governance = GovernanceEngine()
