# lectures/09/scripts/generate_resilience_visuals.py
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
import random

# Create images directory if it doesn't exist
output_dir = "lectures/09/images"
os.makedirs(output_dir, exist_ok=True)

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# --- 1. Resilience Comparison Plot (ER, WS, BA) ---
def simulate_attack(G_orig, attack_type='random', num_steps=20):
    """Simulates an attack on a graph and returns GCC size over removal steps."""
    G = G_orig.copy()
    n_initial = G_orig.number_of_nodes()
    if n_initial == 0:
        return [0.0] * num_steps

    gcc_sizes = [1.0] # Start with full GCC

    nodes_to_remove_per_step = max(1, n_initial // num_steps)

    for _ in range(num_steps):
        if G.number_of_nodes() == 0:
            gcc_sizes.append(0.0)
            continue

        nodes_removed_this_step = 0
        current_nodes_to_remove = []

        if attack_type == 'random':
            if G.number_of_nodes() > 0:
                current_nodes_to_remove = random.sample(list(G.nodes()), min(nodes_to_remove_per_step, G.number_of_nodes()))
        elif attack_type == 'targeted_degree':
            if G.number_of_nodes() > 0:
                degrees = dict(G.degree())
                sorted_nodes = sorted(degrees, key=degrees.get, reverse=True)
                current_nodes_to_remove = sorted_nodes[:min(nodes_to_remove_per_step, G.number_of_nodes())]

        if not current_nodes_to_remove: # no nodes left or no nodes to remove
             gcc_sizes.append(len(gcc_sizes) > 0 and gcc_sizes[-1] or 0.0) # maintain last size or 0
             continue


        G.remove_nodes_from(current_nodes_to_remove)

        if G.number_of_nodes() > 0:
            largest_cc = max(nx.connected_components(G), key=len, default=set())
            gcc_sizes.append(len(largest_cc) / n_initial)
        else:
            gcc_sizes.append(0.0)

    # Ensure the list has num_steps + 1 elements (including initial state)
    while len(gcc_sizes) < num_steps + 1:
        gcc_sizes.append(gcc_sizes[-1] if gcc_sizes else 0.0)
    return gcc_sizes[:num_steps+1]


def plot_resilience_comparison():
    print("Generating resilience comparison plot...")
    n = 200
    num_removal_steps = 20 # Number of removal iterations

    # ER Graph
    p_er = 4 / (n - 1) # avg degree approx 4
    G_er = nx.erdos_renyi_graph(n, p_er, seed=42)
    er_random = simulate_attack(G_er, 'random', num_removal_steps)
    er_targeted = simulate_attack(G_er, 'targeted_degree', num_removal_steps)

    # WS Graph
    k_ws = 4
    p_ws = 0.1
    G_ws = nx.watts_strogatz_graph(n, k_ws, p_ws, seed=42)
    ws_random = simulate_attack(G_ws, 'random', num_removal_steps)
    ws_targeted = simulate_attack(G_ws, 'targeted_degree', num_removal_steps)

    # BA Graph
    m_ba = 2
    G_ba = nx.barabasi_albert_graph(n, m_ba, seed=42)
    ba_random = simulate_attack(G_ba, 'random', num_removal_steps)
    ba_targeted = simulate_attack(G_ba, 'targeted_degree', num_removal_steps)

    fraction_removed = np.linspace(0, 1, num_removal_steps + 1)

    plt.figure(figsize=(12, 8))

    plt.plot(fraction_removed, er_random, 'b-', label='ER Random Attack', alpha=0.7)
    plt.plot(fraction_removed, er_targeted, 'b--', label='ER Targeted Attack', alpha=0.7)

    plt.plot(fraction_removed, ws_random, 'g-', label='WS Random Attack', alpha=0.7)
    plt.plot(fraction_removed, ws_targeted, 'g--', label='WS Targeted Attack', alpha=0.7)

    plt.plot(fraction_removed, ba_random, 'r-', label='BA Random Attack', alpha=0.7)
    plt.plot(fraction_removed, ba_targeted, 'r--', label='BA Targeted Attack', alpha=0.7)

    plt.xlabel('Fraction of Nodes Removed')
    plt.ylabel('Relative Size of Giant Connected Component (GCC)')
    plt.title('Network Resilience Comparison: ER, WS, BA Models')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 1.05)
    plt.xlim(0, 1.0)
    plt.savefig(os.path.join(output_dir, "resilience_comparison_ER_WS_BA.png"), dpi=150)
    plt.close()
    print("Saved resilience_comparison_ER_WS_BA.png")

# --- 2. Network Fragmentation Example ---
def plot_fragmentation_example():
    print("Generating fragmentation example...")
    n = 30
    m = 2
    G_orig = nx.barabasi_albert_graph(n, m, seed=42)
    pos = nx.spring_layout(G_orig, seed=42)

    # Initial state
    plt.figure(figsize=(6,5))
    nx.draw(G_orig, pos, node_color='lightblue', node_size=200, with_labels=True, font_size=8)
    plt.title("Initial BA Network")
    plt.savefig(os.path.join(output_dir, "fragmentation_initial.png"), dpi=100)
    plt.close()

    # Random removal (e.g., 5 nodes)
    G_rand_rem = G_orig.copy()
    nodes_to_remove_rand = random.sample(list(G_rand_rem.nodes()), 5)
    G_rand_rem.remove_nodes_from(nodes_to_remove_rand)
    plt.figure(figsize=(6,5))
    nx.draw(G_rand_rem, pos, node_color='lightgreen', node_size=200, with_labels=True, font_size=8)
    plt.title("After 5 Random Removals")
    plt.savefig(os.path.join(output_dir, "fragmentation_random.png"), dpi=100)
    plt.close()

    # Targeted removal (e.g., 3 highest degree nodes)
    G_targ_rem = G_orig.copy()
    degrees = dict(G_targ_rem.degree())
    nodes_to_remove_targ = sorted(degrees, key=degrees.get, reverse=True)[:3]
    G_targ_rem.remove_nodes_from(nodes_to_remove_targ)
    plt.figure(figsize=(6,5))
    nx.draw(G_targ_rem, pos, node_color='lightcoral', node_size=200, with_labels=True, font_size=8)
    plt.title("After 3 Targeted (Hub) Removals")
    plt.savefig(os.path.join(output_dir, "fragmentation_targeted.png"), dpi=100)
    plt.close()
    print("Saved fragmentation_*.png images.")

# --- 3. Percolation Threshold Example (ER Graph) ---
def plot_percolation_threshold():
    print("Generating percolation threshold plot...")
    n = 1000
    probs = np.linspace(0.0, 0.01, 50) # p for ER graph (edge probability)
    avg_degrees = probs * (n-1)
    gcc_sizes = []

    for p_val in probs:
        G = nx.erdos_renyi_graph(n, p_val)
        if G.number_of_nodes() == 0:
            gcc_sizes.append(0)
            continue
        largest_cc = max(nx.connected_components(G), key=len, default=set())
        gcc_sizes.append(len(largest_cc) / n)

    plt.figure(figsize=(8, 6))
    plt.plot(avg_degrees, gcc_sizes, 'o-', label='Simulated GCC Size')
    plt.axvline(x=1.0, color='r', linestyle='--', label='Critical Threshold (<k>=1)')
    plt.xlabel('Average Degree <k> = p(N-1)')
    plt.ylabel('Relative Size of GCC (S)')
    plt.title(f'Percolation Threshold in ER Graphs (N={n})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(output_dir, "percolation_threshold_er.png"), dpi=150)
    plt.close()
    print("Saved percolation_threshold_er.png")

# --- 4. Cascading Failure Conceptual Example ---
def plot_cascading_failure_concept():
    print("Generating cascading failure concept...")
    G = nx.Graph()
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    G.add_edges_from([('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E'), ('D','F')])
    pos = {'A': (0,1), 'B': (1,2), 'C': (1,0), 'D':(2,1), 'E':(3,2), 'F':(3,0)}

    # Initial state
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    nx.draw(G, pos, node_color='lightblue', node_size=500, with_labels=True, font_weight='bold')
    plt.text(pos['A'][0], pos['A'][1]+0.2, "Load:2", ha='center')
    plt.text(pos['D'][0], pos['D'][1]+0.2, "Load:4", ha='center')
    plt.title("Initial State (Node D Critical)")

    # After D fails and load redistributes
    G_fail = G.copy()
    G_fail.remove_node('D')
    # Simplistic: Assume load from D (4) goes to A (2 original + 2 from D via B,C)

    node_colors_fail = ['lightblue' if n!='A' else 'salmon' for n in G_fail.nodes()]
    plt.subplot(1,2,2)
    nx.draw(G_fail, pos, node_color=node_colors_fail, node_size=500, with_labels=True, font_weight='bold')
    # Node A is now overloaded
    plt.text(pos['A'][0], pos['A'][1]+0.2, "Load:4 (Overloaded!)", ha='center', color='red')
    plt.title("After Node D Fails (Node A Overloaded)")

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "cascading_failure_example.png"), dpi=100)
    plt.close()
    print("Saved cascading_failure_example.png")


if __name__ == "__main__":
    plot_resilience_comparison()
    plot_fragmentation_example()
    plot_percolation_threshold()
    plot_cascading_failure_concept()
    print("All resilience visuals generated.")
