from typing import Callable, Dict, Any, List
import inspect

class Tool:
    def __init__(self, name: str, func: Callable, description: str):
        self.name = name
        self.func = func
        self.description = description
        self.signature = inspect.signature(func)

    def execute(self, **kwargs) -> Any:
        return self.func(**kwargs)

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Tool] = {}

    def register_tool(self, name: str, description: str):
        def decorator(func: Callable):
            self.tools[name] = Tool(name, func, description)
            return func
        return decorator

    def get_tool_descriptions(self) -> List[Dict[str, str]]:
        return [{"name": name, "description": tool.description} for name, tool in self.tools.items()]

    def call_tool(self, name: str, **kwargs) -> Any:
        if name not in self.tools:
            raise ValueError(f"Tool {name} not found")
        return self.tools[name].execute(**kwargs)

# Global registry
registry = ToolRegistry()

@registry.register_tool("search", "Search the web for information")
def search(query: str) -> str:
    return f"Search results for: {query}"

@registry.register_tool("calculator", "Perform mathematical calculations")
def calculate(expression: str) -> str:
    return f"Result of {expression}"
