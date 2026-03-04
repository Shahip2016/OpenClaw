import hashlib
import time
from typing import Dict, Any, List

class AuditLog:
    def __init__(self):
        self.logs: List[Dict[str, Any]] = []

    def log_job(self, agent_id: str, tool_name: str, params: Dict[str, Any], result: Any):
        entry = {
            "timestamp": time.time(),
            "agent_id": agent_id,
            "tool": tool_name,
            "params": params,
            "result_hash": hashlib.sha256(str(result).encode()).hexdigest()
        }
        self.logs.append(entry)

class ProviderProxy:
    def __init__(self):
        self.audit = AuditLog()

    def call_provider(self, agent_id: str, tool_func: callable, tool_name: str, **kwargs) -> Any:
        # Audit job before and after execution
        result = tool_func(**kwargs)
        self.audit.log_job(agent_id, tool_name, kwargs, result)
        return result

# Global proxy
proxy = ProviderProxy()

class SecuritySandbox:
    def __init__(self):
        self.allowed_tools = ["search", "calculator", "distill"]

    def is_authorized(self, tool_name: str) -> bool:
        return tool_name in self.allowed_tools

# Global sandbox
sandbox = SecuritySandbox()
