import networkx as nx
import matplotlib.pyplot as plt
import os
import collections
import numpy as np
from scipy.stats import poisson

# Parameters
n_er = 1000  # Number of nodes for ER graph
p_er = 0.05  # Probability for ER graph

n_ba = 1000  # Number of nodes for BA graph
m_ba = 5     # Edges to attach from a new node in BA
seed = 42    # Seed for reproducibility

# Create output directory if it doesn't exist
output_dir = "../images"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "degree_dist_comparison.png")

# Generate graphs
G_er = nx.erdos_renyi_graph(n_er, p_er, seed=seed)
G_ba = nx.barabasi_albert_graph(n_ba, m_ba, seed=seed)

# Calculate degree sequences
degree_sequence_er = sorted([d for n, d in G_er.degree()], reverse=True)
degree_sequence_ba = sorted([d for n, d in G_ba.degree()], reverse=True)

# Calculate degree counts
degree_counts_er = collections.Counter(degree_sequence_er)
degree_counts_ba = collections.Counter(degree_sequence_ba)

# Prepare data for plotting
deg_er, cnt_er = zip(*degree_counts_er.items())
deg_ba, cnt_ba = zip(*degree_counts_ba.items())

# Normalize counts to get probability density
cnt_er = np.array(cnt_er) / n_er
cnt_ba = np.array(cnt_ba) / n_ba

# --- Visualization ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot ER Degree Distribution (Linear Scale)
ax1.bar(deg_er, cnt_er, width=0.80, color='skyblue', label='ER Actual')
ax1.set_title("ER Degree Distribution (G(1000, 0.05))")
ax1.set_xlabel("Degree (k)")
ax1.set_ylabel("P(k)")

# Add Poisson theoretical curve
avg_k_er = p_er * (n_er - 1)
k_min = int(poisson.ppf(0.001, avg_k_er))
k_max = int(poisson.ppf(0.999, avg_k_er))
x_poisson = np.arange(k_min, k_max + 1)
ax1.plot(x_poisson, poisson.pmf(x_poisson, avg_k_er), 'r--', ms=8,
         label='Poisson Approx.')
ax1.legend()
ax1.grid(axis='y', alpha=0.7)

# Plot BA Degree Distribution (Log-Log Scale)
ax2.loglog(deg_ba, cnt_ba, 'bo', markersize=5, label='BA Actual')
ax2.set_title("BA Degree Distribution (N=1000, m=5)")
ax2.set_xlabel("Degree (k) [Log Scale]")
ax2.set_ylabel("P(k) [Log Scale]")
ax2.grid(True, which="both", ls="--", alpha=0.5)
ax2.legend()

plt.tight_layout()

# Save the figure
plt.savefig(output_path, bbox_inches='tight', dpi=150)
plt.close()  # Close the plot to free memory

print(f"Image saved to {output_path}")