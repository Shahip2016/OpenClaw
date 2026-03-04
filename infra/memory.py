from typing import List, Dict, Any, Optional

class PersistentMemory:
    def __init__(self):
        self.short_term: List[Dict[str, Any]] = []
        self.long_term: Dict[str, Any] = {}

    def commit_to_long_term(self, key: str, value: Any):
        self.long_term[key] = value

    def query(self, query_str: str) -> List[Any]:
        # Simple substring search for simulation
        results = [v for k, v in self.long_term.items() if query_str.lower() in str(k).lower() or query_str.lower() in str(v).lower()]
        return results

class ContextManager:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.memory = PersistentMemory()
        self.current_context: Dict[str, Any] = {}

    def update_context(self, key: str, value: Any):
        self.current_context[key] = value
        self.memory.short_term.append({key: value})

# Global memory instance
memory_system = PersistentMemory()
