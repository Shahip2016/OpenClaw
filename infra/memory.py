from typing import List, Dict, Any, Optional

class PersistentMemory:
    def __init__(self, cache_size: int = 10):
        self.short_term: List[Dict[str, Any]] = []
        self.long_term: Dict[str, Any] = {}
        self.cache: Dict[str, Any] = {}
        self.cache_order: List[str] = []
        self.cache_size = cache_size

    def commit_to_long_term(self, key: str, value: Any):
        self.long_term[key] = value
        # Update cache
        if key in self.cache:
            self.cache_order.remove(key)
        elif len(self.cache) >= self.cache_size:
            oldest = self.cache_order.pop(0)
            del self.cache[oldest]
        
        self.cache[key] = value
        self.cache_order.append(key)

    def query(self, query_str: str) -> List[Any]:
        # Check cache first
        if query_str in self.cache:
            # Move to end (most recent)
            self.cache_order.remove(query_str)
            self.cache_order.append(query_str)
            return [self.cache[query_str]]
            
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

    def get_recent_context(self, n: int = 5) -> List[Dict[str, Any]]:
        return self.memory.short_term[-n:]

# Global memory instance
memory_system = PersistentMemory()
