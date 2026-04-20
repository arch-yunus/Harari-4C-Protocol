import random
import time

class Agent:
    def __init__(self, id, goal):
        self.id = id
        self.position = random.randint(0, 100)
        self.goal = goal
        self.knowledge = 0

    def move(self, swarm_knowledge):
        # Collaboration logic: Agents move faster if swarm knowledge is high
        step = random.randint(1, 5) + (swarm_knowledge // 10)
        if self.position < self.goal:
            self.position += step
        elif self.position > self.goal:
            self.position -= step
        
        # Contributing to knowledge
        if random.random() > 0.7:
            return 1
        return 0

def run_swarm_simulation():
    """
    Harari-4C-Protocol: Collaboration (Swarm Intelligence) Simulation
    Demonstrates how decentralized agents reach a collective goal faster through collaboration.
    """
    GOAL = 50
    NUM_AGENTS = 5
    agents = [Agent(i, GOAL) for i in range(NUM_AGENTS)]
    swarm_knowledge = 0
    ticks = 0

    print("--- Harari-4C: Collaboration (Swarm Sim) ---")
    print(f"Goal: {GOAL} | Agents: {NUM_AGENTS}\n")

    while any(abs(a.position - GOAL) > 2 for a in agents):
        ticks += 1
        contribution_this_turn = 0
        status_line = f"Tick {ticks:02d} | Knowledge: {swarm_knowledge:02d} | Positions: "
        
        for agent in agents:
            contribution_this_turn += agent.move(swarm_knowledge)
            status_line += f"A{agent.id}:{agent.position:02d} "
        
        swarm_knowledge += contribution_this_turn
        print(status_line)
        time.sleep(0.1)
        
        if ticks > 50: break # Safety break

    print(f"\n[Success] Tüm ajanlar hedefe {ticks} adımda ulaştı!")
    print(f"Toplam Kolektif Bilgi: {swarm_knowledge}")

if __name__ == "__main__":
    run_swarm_simulation()
