from environment.network import create_network
from environment.interaction import payoff


def run_experiment():
    G, agents = create_network()
    interactions = []

    for _ in range(50):
        for node in G.nodes():
            agent = agents[node]
            neighbors = list(G.neighbors(node))
            if not neighbors:
                continue

            peer_id = agent.select_peer([agents[n] for n in neighbors])
            peer = peer_id

            a_action = "C"
            b_action = "C"

            r1, r2 = payoff(a_action, b_action)

            agent.update_reward(r1)
            peer.update_reward(r2)

            interactions.append((a_action, b_action))

    print("Simulation complete")
