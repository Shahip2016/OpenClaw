from typing import Dict, List, Set

class SocialGraph:
    def __init__(self):
        self.relationships: Dict[str, Set[str]] = {}
        self.interaction_counts: Dict[str, int] = {}

    def add_interaction(self, agent_a: str, agent_b: str):
        if agent_a not in self.relationships:
            self.relationships[agent_a] = set()
        self.relationships[agent_a].add(agent_b)
        
        pair = tuple(sorted((agent_a, agent_b)))
        self.interaction_counts[str(pair)] = self.interaction_counts.get(str(pair), 0) + 1

    def get_peers(self, agent_id: str) -> List[str]:
        return list(self.relationships.get(agent_id, []))

    def get_influence_score(self, agent_id: str) -> int:
        # Simplified influence based on number of connections
        return len(self.relationships.get(agent_id, []))

# Global social graph
graph = SocialGraph()
