import networkx as nx
import matplotlib.pyplot as plt
import os

# Create the images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Create a graph
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
G.add_nodes_from(nodes)

# Add ALL edges from the original image
edges = [
    # Top cluster (a-g)
    ('a', 'b'), ('a', 'd'), ('a', 'f'),
    ('b', 'd'), ('b', 'e'), ('b', 'g'),
    ('c', 'f'), ('c', 'h'),
    ('d', 'f'), ('d', 'e'),  # Added d-e connection
    ('e', 'g'),
    ('f', 'g'), ('f', 'h'),  # Added f-h connection
    ('g', 'h'),

    # Middle section
    ('h', 'i'), ('h', 'r'),

    # Bottom cluster
    ('i', 'j'), ('i', 'n'), ('i', 'p'),
    ('j', 'k'), ('j', 'l'), ('j', 'n'), ('j', 'o'), ('j', 'p'),
    ('k', 'l'), ('k', 'p'),
    ('l', 'm'),
    ('m', 'q'),
    ('n', 'o'),
    ('q', 's')
]
G.add_edges_from(edges)

# Use the same layout for all visualizations
pos = nx.spring_layout(G, seed=3)  # Using a seed for reproducibility

# Draw the default graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=500,
        width=1,
        with_labels=True,
        font_size=12)
plt.title('Default Network Graph', fontsize=16)
plt.axis('off')
plt.savefig('images/default_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# Calculate and visualize degree centrality
degree_centrality = nx.degree_centrality(G)
plt.figure(figsize=(12, 8))
node_sizes = [degree_centrality[n] * 5000 + 100 for n in G]
nx.draw(G, pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=node_sizes,
        width=1,
        with_labels=True,
        font_size=12)

# Add centrality value labels
for node, (x, y) in pos.items():
    plt.text(x, y-0.08, f"{degree_centrality[node]:.2f}",
             ha='center', fontsize=9)

plt.title('Degree Centrality', fontsize=16)
plt.axis('off')
plt.savefig('images/degree_centrality.png', dpi=300, bbox_inches='tight')
plt.close()

# Calculate and visualize eigenvector centrality with increased max_iter
try:
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000, tol=1e-6)
except nx.PowerIterationFailedConvergence:
    # If still fails, use a simpler approximation
    eigenvector_centrality = {node: sum(degree_centrality[nbr] for nbr in G.neighbors(node))
                             for node in G.nodes()}
    # Normalize
    max_val = max(eigenvector_centrality.values())
    eigenvector_centrality = {k: v/max_val for k, v in eigenvector_centrality.items()}

plt.figure(figsize=(12, 8))
node_sizes = [eigenvector_centrality[n] * 5000 + 100 for n in G]
nx.draw(G, pos,
        node_color='#90ee90',  # light green
        edge_color='gray',
        node_size=node_sizes,
        width=1,
        with_labels=True,
        font_size=12)

# Add centrality value labels
for node, (x, y) in pos.items():
    plt.text(x, y-0.08, f"{eigenvector_centrality[node]:.2f}",
             ha='center', fontsize=9)

plt.title('Eigenvector Centrality', fontsize=16)
plt.axis('off')
plt.savefig('images/eigenvector_centrality.png', dpi=300, bbox_inches='tight')
plt.close()

# Calculate and visualize betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)
plt.figure(figsize=(12, 8))
node_sizes = [betweenness_centrality[n] * 10000 + 100 for n in G]  # Scale for visibility
nx.draw(G, pos,
        node_color='#f08080',  # light coral
        edge_color='gray',
        node_size=node_sizes,
        width=1,
        with_labels=True,
        font_size=12)

# Add centrality value labels
for node, (x, y) in pos.items():
    plt.text(x, y-0.08, f"{betweenness_centrality[node]:.2f}",
             ha='center', fontsize=9)

plt.title('Betweenness Centrality', fontsize=16)
plt.axis('off')
plt.savefig('images/betweenness_centrality.png', dpi=300, bbox_inches='tight')
plt.close()

# Calculate and visualize closeness centrality
closeness_centrality = nx.closeness_centrality(G)
plt.figure(figsize=(12, 8))
node_sizes = [closeness_centrality[n] * 5000 + 100 for n in G]
nx.draw(G, pos,
        node_color='#87cefa',  # light sky blue
        edge_color='gray',
        node_size=node_sizes,
        width=1,
        with_labels=True,
        font_size=12)

# Add centrality value labels
for node, (x, y) in pos.items():
    plt.text(x, y-0.08, f"{closeness_centrality[node]:.2f}",
             ha='center', fontsize=9)

plt.title('Closeness Centrality', fontsize=16)
plt.axis('off')
plt.savefig('images/closeness_centrality.png', dpi=300, bbox_inches='tight')
plt.close()

# Print centrality values for reference
print("Degree Centrality:")
for node, centrality in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {centrality:.3f}")

print("\nEigenvector Centrality:")
for node, centrality in sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {centrality:.3f}")

print("\nBetweenness Centrality:")
for node, centrality in sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {centrality:.3f}")

print("\nCloseness Centrality:")
for node, centrality in sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {centrality:.3f}")

print("\nImages have been saved to the 'images' directory.")