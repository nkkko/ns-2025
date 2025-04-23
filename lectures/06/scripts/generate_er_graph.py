import networkx as nx
import matplotlib.pyplot as plt
import os

# Parameters
n = 30  # Number of nodes
p = 0.1  # Probability of edge creation
seed = 42  # Seed for reproducibility

# Create output directory if it doesn't exist
output_dir = "../images"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "er_graph_n30_p01.png")

# Create G(n, p) graph
G_np = nx.erdos_renyi_graph(n, p, seed=seed)

# --- Visualization ---
plt.figure(figsize=(8, 6))

# Use a layout algorithm to position nodes
# Use the same seed for layout for reproducibility
pos = nx.spring_layout(G_np, seed=seed)

nx.draw(
    G_np,
    pos,
    with_labels=False,
    node_size=100,
    node_color='lightblue',
    edge_color='gray',
    width=0.5
)

plt.title(f"Erdos-Renyi G(n={n}, p={p}) Graph")
plt.axis('off')  # Hide axes
plt.tight_layout()

# Save the figure
plt.savefig(output_path, bbox_inches='tight', dpi=150)
plt.close()  # Close the plot to free memory

print(f"Image saved to {output_path}")