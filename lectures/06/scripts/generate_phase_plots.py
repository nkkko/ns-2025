import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np

# Parameters
seed = 123  # Seed for reproducibility
nodes = 100  # Common number of nodes for better comparison

# Calculate p values based on average degree <k> = p*(n-1)
p_subcritical = 0.5 / (nodes - 1)    # <k> = 0.5
p_critical = 1.0 / (nodes - 1)    # <k> = 1.0
p_supercritical = 3.0 / (nodes - 1)  # <k> = 3.0
# For connected, use <k> slightly above ln(N), e.g., 1.5 * ln(N)
p_connected = 1.5 * np.log(nodes) / (nodes - 1)
connected_k = 1.5 * np.log(nodes)

# Phase parameters (n, p, name, title_suffix)
phases = [
    (nodes, p_subcritical, "subcritical", "<k> = 0.5 (Subcritical)"),
    (nodes, p_critical, "critical",    "<k> = 1.0 (Critical)"),
    (nodes, p_supercritical, "supercritical", "<k> = 3.0 (Supercritical)"),
    (nodes, p_connected, "connected",
     f"<k> = {connected_k:.1f} (> ln(N), Connected)")
]

# Create output directory if it doesn't exist
output_dir = "../images"
os.makedirs(output_dir, exist_ok=True)

# --- Generate and Plot Each Phase ---
for n, p, name, title_suffix in phases:
    output_path = os.path.join(output_dir, f"er_phase_{name}.png")
    print(f"Generating {output_path} (n={n}, p={p:.4f})...")

    # Generate graph
    G = nx.erdos_renyi_graph(n, p, seed=seed)

    plt.figure(figsize=(8, 6))

    # Use a layout algorithm
    # Fruchterman-Reingold often separates components well
    pos = nx.spring_layout(G, seed=seed, k=0.5 / np.sqrt(n))

    # Find connected components
    components = list(nx.connected_components(G))
    largest_cc = max(components, key=len) if components else set()

    # Draw nodes
    node_colors = ['red' if node in largest_cc else 'lightblue'
                   for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_size=50, node_color=node_colors,
                           alpha=0.8)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5, width=0.5)

    plt.title(f"ER Phase Transition: {title_suffix}")
    plt.axis('off')
    plt.tight_layout()

    # Save the figure
    plt.savefig(output_path, bbox_inches='tight', dpi=150)
    plt.close()

print("Phase transition images generated.")