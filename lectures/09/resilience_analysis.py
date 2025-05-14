import networkx as nx
import random
import matplotlib.pyplot as plt

G = nx.barabasi_albert_graph(100, 2)
n_initial = G.number_of_nodes()
gcc_sizes = []

nodes_to_remove = list(G.nodes())
random.shuffle(nodes_to_remove)

for i in range(n_initial):
    if G.number_of_nodes() > 0:
        components = list(nx.connected_components(G))
        if components:
            gcc_size = len(max(components, key=len))
            gcc_sizes.append(gcc_size / n_initial)
        else:
            gcc_sizes.append(0)

        G.remove_node(nodes_to_remove[i]) # Remove one node at a time
    else:
        gcc_sizes.append(0)
# Plot gcc_sizes vs. fraction_removed
fraction_removed = [i / n_initial for i in range(n_initial)]
plt.figure(figsize=(8, 5))
plt.plot(fraction_removed, gcc_sizes, marker='o', linestyle='-')
plt.xlabel('Fraction of Nodes Removed')
plt.ylabel('Relative Size of GCC')
plt.title('Resilience of Barabási–Albert Network')
plt.grid(True)
plt.tight_layout()
plt.savefig('resilience_plot.png')
plt.show()