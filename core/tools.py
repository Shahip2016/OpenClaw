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

@registry.register_tool("numerical_integration", "Integrate a function using the Trapezoidal rule")
def numerical_integration(func_body: str, lower: float, upper: float, n: int = 100) -> float:
    # A simple but powerful tool for scientific agents to perform calculus
    try:
        f = eval(f"lambda x: {func_body}", {"__builtins__": {}}, {"math": __import__("math")})
        h = (upper - lower) / n
        s = 0.5 * (f(lower) + f(upper))
        for i in range(1, n):
            s += f(lower + i * h)
        return s * h
    except Exception as e:
        return f"Error: {str(e)}"

@registry.register_tool("symbolic_differentiation", "Compute the derivative of an expression (simplified)")
def symbolic_differentiation(expression: str, variable: str = "x") -> str:
    # Stub for a more advanced symbolic engine
    return f"d/d{variable} [{expression}] computed (symbolic engine placeholder)"
