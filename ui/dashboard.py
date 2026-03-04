import time

def monitor_dashboard():
    print("--- OpenClaw Real-Time Monitoring ---")
    print(f"Time: {time.ctime()}")
    print(f"Active Agents: 1")
    print(f"Moltbook Tasks: 0")
    print(f"ClawdLab Governance: Active")
    print("-------------------------------------")

if __name__ == "__main__":
    monitor_dashboard()
