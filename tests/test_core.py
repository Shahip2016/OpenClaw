from core.agent import OpenClawAgent
from core.tools import registry
from core.skills import skill_manager
from clawdlab.governance import governance, Role
from clawdlab.experiment_engine import experiment_engine
import unittest

class TestOpenClaw(unittest.TestCase):
    def test_agent_loop(self):
        agent = OpenClawAgent("TestAgent")
        agent.run_step("Hello World")
        self.assertEqual(len(agent.state.history), 3)

    def test_governance(self):
        proj = governance.create_project("TestProj", "PI_Agent")
        self.assertTrue(governance.validate_action("TestProj", "PI_Agent", "approve_task"))
        self.assertFalse(governance.validate_action("TestProj", "OtherAgent", "approve_task"))

    def test_skill_execution(self):
        # Tools are already registered in core.tools
        input_data = {"topic": "AI security"}
        result = skill_manager.execute_skill("research_topic", input_data)
        self.assertIn("raw_info", result)
        self.assertIn("impact_score", result)

if __name__ == "__main__":
    unittest.main()
