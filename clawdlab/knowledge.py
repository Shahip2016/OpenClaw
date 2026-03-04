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

# Global distiller
distiller = KnowledgeDistiller()
