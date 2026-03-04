from typing import List, Dict, Any
from .tools import registry

class Skill:
    def __init__(self, name: str, description: str, steps: List[Dict[str, Any]]):
        self.name = name
        self.description = description
        self.steps = steps

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        context = input_data.copy()
        for step in self.steps:
            tool_name = step["tool"]
            args = {k: context.get(v, v) if isinstance(v, str) and v.startswith("$") else v 
                    for k, v in step.get("args", {}).items()}
            
            # Resolve variable references
            for k, v in args.items():
                if isinstance(v, str) and v.startswith("$"):
                    args[k] = context.get(v[1:])

            result = registry.call_tool(tool_name, **args)
            if "output_var" in step:
                context[step["output_var"]] = result
        return context

class SkillManager:
    def __init__(self):
        self.skills: Dict[str, Skill] = {}

    def define_skill(self, name: str, description: str, steps: List[Dict[str, Any]]):
        self.skills[name] = Skill(name, description, steps)

    def execute_skill(self, name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        if name not in self.skills:
            raise ValueError(f"Skill {name} not found")
        return self.skills[name].run(input_data)

# Example skill: Research and Summarize
skill_manager = SkillManager()
skill_manager.define_skill(
    "research_topic",
    "Search for a topic and calculate impact",
    [
        {"tool": "search", "args": {"query": "$topic"}, "output_var": "raw_info"},
        {"tool": "calculator", "args": {"expression": "len('$raw_info') * 10"}, "output_var": "impact_score"}
    ]
)
