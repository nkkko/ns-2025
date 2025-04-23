import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np

# Parameters
n = 1000  # Number of nodes
num_points = 50  # Number of points to plot for average degree
num_trials = 5   # Number of trials per point for averaging
max_avg_degree = 4.0

# Create output directory if it doesn't exist
output_dir = "../images"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "gcc_emergence.png")

# Average degrees to test
avg_degrees = np.linspace(0, max_avg_degree, num_points)
probs = avg_degrees / (n - 1)

# Store results
relative_lcc_sizes = []

print(f"Simulating LCC size for N={n} across {num_points} avg degrees...")

# --- Simulation ---
for i, p in enumerate(probs):
    avg_lcc_size = 0
    print(f"  Avg Degree: {avg_degrees[i]:.2f} (p={p:.4f}) - Trial: ", end="")
    for trial in range(num_trials):
        print(f"{trial+1}", end=" ")
        G = nx.erdos_renyi_graph(n, p)
        components = list(nx.connected_components(G))
        if components:
            largest_cc_size = len(max(components, key=len))
            avg_lcc_size += largest_cc_size
        # else: graph has no edges, LCC size is 0 or 1 depending on def.
        # We handle the case of no components (avg_lcc_size remains 0)
    avg_lcc_size /= num_trials
    relative_lcc_sizes.append(avg_lcc_size / n)
    print("Done")

# --- Visualization ---
plt.figure(figsize=(8, 5))
plt.plot(avg_degrees, relative_lcc_sizes, 'b-', marker='.',
         label='Simulation (Avg over 5 trials)')

# Add theoretical line for S (fraction in GCC) for <k> > 1
# Requires solving S = 1 - exp(-<k>S) numerically, or approximating
# For simplicity, we just show the simulation results

# Add vertical line at critical point <k>=1
plt.axvline(1.0, color='r', linestyle='--',
            label='<k> = 1 (Critical Point)')

plt.title(f"Emergence of the Giant Component in ER Graphs (N={n})")
plt.xlabel("Average Degree (<k>)")
plt.ylabel("Fraction of Nodes in Largest Component (S)")
plt.ylim(0, 1.05)
plt.xlim(0, max_avg_degree)
plt.grid(True, alpha=0.6)
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig(output_path, bbox_inches='tight', dpi=150)
plt.close()  # Close the plot to free memory

print(f"Image saved to {output_path}")