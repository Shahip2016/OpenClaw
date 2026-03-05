from typing import List, Dict, Any, Optional
import json
import os

class KnowledgeItem:
    def __init__(self, topic: str, content: str, evidence: List[str]):
        self.topic = topic
        self.content = content
        self.evidence = evidence
        self.timestamp = os.popen("date /T").read().strip() # Simplified timestamp for Windows

class KnowledgeDistiller:
    def __init__(self, store_path: str = "knowledge_base"):
        self.store_path = store_path
        if not os.path.exists(store_path):
            os.makedirs(store_path)

    def distill_from_results(self, topic: str, results: Dict[str, Any]) -> KnowledgeItem:
        # Simplified distillation logic: extracting key insights from experiment results
        content = f"Insights on {topic}: {json.dumps(results)}"
        evidence = [f"Result: {k}={v}" for k, v in results.items()]
        ki = KnowledgeItem(topic, content, evidence)
        self.save_ki(ki)
        return ki

    def save_ki(self, ki: KnowledgeItem):
        file_path = os.path.join(self.store_path, f"{ki.topic.replace(' ', '_')}.json")
        with open(file_path, "w") as f:
            json.dump(ki.__dict__, f, indent=4)

    def get_knowledge_graph(self) -> Dict[str, Any]:
        """Exports all distilled knowledge as a node-link graph for visualization."""
        nodes = []
        links = []
        if not os.path.exists(self.store_path):
            return {"nodes": [], "links": []}
            
        for filename in os.listdir(self.store_path):
            if filename.endswith(".json"):
                with open(os.path.join(self.store_path, filename), "r") as f:
                    data = json.load(f)
                    nodes.append({"id": data["topic"], "group": 1})
                    # Simple link logic: link to 'Research Root' or based on evidence references
                    links.append({"source": "Research Root", "target": data["topic"]})
        
        if nodes:
            nodes.append({"id": "Research Root", "group": 0})
            
        return {"nodes": nodes, "links": links}

# Global distiller
distiller = KnowledgeDistiller()
