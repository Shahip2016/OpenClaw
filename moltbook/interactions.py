from .protocol import network, Message
from .social_graph import graph
from typing import List, Any

class AgentCommunicator:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        network.register_agent(agent_id)

    def broadcast(self, content: Any, msg_type: str = "broadcast"):
        peers = graph.get_peers(self.agent_id)
        messages = []
        for peer in peers:
            msg = network.route_message(Message(self.agent_id, peer, content, msg_type))
            messages.append(msg)
        return messages

    def negotiate(self, peer_id: str, proposal: Any):
        msg = Message(self.agent_id, peer_id, proposal, "negotiation")
        network.route_message(msg)
        graph.add_interaction(self.agent_id, peer_id)
        return msg

    def check_inbox(self) -> List[Message]:
        node = network.nodes.get(self.agent_id)
        if node:
            messages = node.inbox[:]
            node.inbox.clear()
            return messages
        return []

# Agent interaction utilities
def establish_connection(agent_a: str, agent_b: str):
    graph.add_interaction(agent_a, agent_b)
    graph.add_interaction(agent_b, agent_a)
