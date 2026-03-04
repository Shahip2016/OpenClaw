from typing import List, Dict, Any
from .governance import governance
from core.skills import skill_manager

class Experiment:
    def __init__(self, project_title: str, researcher_id: str, skill_name: str, params: Dict[str, Any]):
        self.project_title = project_title
        self.researcher_id = researcher_id
        self.skill_name = skill_name
        self.params = params
        self.results: Optional[Dict[str, Any]] = None
        self.status = "Initialized"

    def execute(self):
        if not governance.validate_action(self.project_title, self.researcher_id, "submit_results"):
            raise PermissionError("Researcher not authorized for this project")
        
        self.status = "Running"
        self.results = skill_manager.execute_skill(self.skill_name, self.params)
        self.status = "Completed"
        return self.results

class ExperimentEngine:
    def __init__(self):
        self.active_experiments: List[Experiment] = []

    def launch_experiment(self, project_title: str, researcher_id: str, skill_name: str, params: Dict[str, Any]) -> Experiment:
        exp = Experiment(project_title, researcher_id, skill_name, params)
        self.active_experiments.append(exp)
        return exp

# Global experiment engine
experiment_engine = ExperimentEngine()
