import pytest
from core.tools import registry
from infra.memory import PersistentMemory, ContextManager
from clawdlab.knowledge import KnowledgeDistiller, KnowledgeItem
from moltbook.protocol import MoltbookNetwork, MoltbookNode, BroadcastProtocol
import os
import shutil

def test_numerical_integration():
    # Test integral of x^2 from 0 to 1 (should be ~0.333)
    result = registry.call_tool("numerical_integration", func_body="x**2", lower=0, upper=1, n=1000)
    assert abs(result - 1/3) < 0.001

def test_lru_cache():
    mem = PersistentMemory(cache_size=2)
    mem.commit_to_long_term("a", 1)
    mem.commit_to_long_term("b", 2)
    mem.commit_to_long_term("c", 3) # "a" should be evicted
    
    assert "a" not in mem.cache
    assert "b" in mem.cache
    assert "c" in mem.cache
    
    mem.query("b") # "b" becomes recent
    mem.commit_to_long_term("d", 4) # "c" should be evicted
    assert "c" not in mem.cache
    assert "b" in mem.cache

def test_knowledge_graph_export():
    test_store = "test_kb"
    if os.path.exists(test_store):
        shutil.rmtree(test_store)
        
    distiller = KnowledgeDistiller(store_path=test_store)
    distiller.distill_from_results("Fusion", {"energy": 100})
    distiller.distill_from_results("Fission", {"energy": 200})
    
    graph = distiller.get_knowledge_graph()
    assert len(graph["nodes"]) == 3 # 2 items + Research Root
    assert any(n["id"] == "Fusion" for n in graph["nodes"])
    assert any(n["id"] == "Research Root" for n in graph["nodes"])
    
    shutil.rmtree(test_store)

def test_broadcast_protocol():
    net = MoltbookNetwork()
    net.register_agent("agent1")
    net.register_agent("agent2")
    net.register_agent("agent3")
    
    be = BroadcastProtocol(net)
    be.announce_discovery("agent1", "Gravity", "It pulls things down.")
    
    assert len(net.nodes["agent2"].inbox) == 1
    assert len(net.nodes["agent3"].inbox) == 1
    assert net.nodes["agent2"].inbox[0].msg_type == "discovery_announcement"
