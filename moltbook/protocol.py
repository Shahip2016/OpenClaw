from typing import Dict, List, Any
import datetime

class Message:
    def __init__(self, sender: str, recipient: str, content: Any, msg_type: str = "text"):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.msg_type = msg_type
        self.timestamp = datetime.datetime.now().isoformat()

class MoltbookNode:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.inbox: List[Message] = []
        self.outbox: List[Message] = []
        self.peers: List[str] = []

    def send_message(self, recipient: str, content: Any, msg_type: str = "text"):
        msg = Message(self.agent_id, recipient, content, msg_type)
        self.outbox.append(msg)
        return msg

    def receive_message(self, message: Message):
        self.inbox.append(message)
        # Auto-add sender to peers if not present
        if message.sender not in self.peers:
            self.peers.append(message.sender)

    def discover_peers(self, network: 'MoltbookNetwork'):
        """Discover other registered agents on the network."""
        for agent_id in network.nodes:
            if agent_id != self.agent_id and agent_id not in self.peers:
                self.peers.append(agent_id)

class BroadcastProtocol:
    def __init__(self, network: 'MoltbookNetwork'):
        self.network = network

    def announce_discovery(self, sender_id: str, topic: str, insight: str):
        """Broadcasts a scientific discovery to all peers."""
        content = {"topic": topic, "insight": insight}
        for agent_id, node in self.network.nodes.items():
            if agent_id != sender_id:
                msg = Message(sender_id, agent_id, content, msg_type="discovery_announcement")
                self.network.route_message(msg)

class MoltbookNetwork:
    def __init__(self):
        self.nodes: Dict[str, MoltbookNode] = {}

    def register_agent(self, agent_id: str):
        self.nodes[agent_id] = MoltbookNode(agent_id)

    def route_message(self, message: Message):
        if message.recipient in self.nodes:
            self.nodes[message.recipient].receive_message(message)
            return True
        return False

# Global instances
network = MoltbookNetwork()
broadcast_engine = BroadcastProtocol(network)
