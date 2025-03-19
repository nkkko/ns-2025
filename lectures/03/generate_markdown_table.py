#!/usr/bin/env python3
import networkx as nx
import pandas as pd

# Create the same graph as in generate_centrality_images.py
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
G.add_nodes_from(nodes)

# Add edges
edges = [
    # Top cluster (a-g)
    ('a', 'b'), ('a', 'd'), ('a', 'f'),
    ('b', 'd'), ('b', 'e'), ('b', 'g'),
    ('c', 'f'), ('c', 'h'),
    ('d', 'f'), ('d', 'e'),
    ('e', 'g'),
    ('f', 'g'), ('f', 'h'),
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

# Calculate all centrality measures
degree_centrality = nx.degree_centrality(G)
try:
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000, tol=1e-6)
except nx.PowerIterationFailedConvergence:
    # If it fails, use approximation
    eigenvector_centrality = {
        node: sum(degree_centrality[nbr] for nbr in G.neighbors(node))
        for node in G.nodes()
    }
    # Normalize
    max_val = max(eigenvector_centrality.values())
    eigenvector_centrality = {k: v/max_val for k, v in eigenvector_centrality.items()}

pagerank = nx.pagerank(G, alpha=0.85)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# Create lists of sorted (node, value) tuples for each measure
degree_sorted = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
eigen_sorted = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)
pagerank_sorted = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
between_sorted = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)
close_sorted = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)

# Function to generate markdown table with columns for each centrality measure
def generate_columnar_table(measures_data, num_rows=5):
    """
    Generate a markdown table with columns organized by centrality measure.
    Each measure has a node column and a value column.
    """
    # Unpack the data
    degree_data, eigen_data, pagerank_data, between_data, close_data = measures_data

    # Create header row with shorter names
    header = "| Deg | Val | Eigen | Val | PR | Val | Betw | Val | Close | Val |\n"
    separator = "| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |\n"

    # Generate rows
    rows = []
    for i in range(num_rows):
        row = []
        # Add data for each measure
        for data_list in measures_data:
            if i < len(data_list):
                node, value = data_list[i]
                # Use only 1 decimal place for better fit
                row.extend([f"**{node}**", f"{value:.1f}"])
            else:
                row.extend(["", ""])  # Empty cells if not enough data

        # Create the markdown row
        rows.append("| " + " | ".join(row) + " |")

    # Combine all parts
    return header + separator + "\n".join(rows)

# Generate the table
data_lists = [degree_sorted, eigen_sorted, pagerank_sorted, between_sorted, close_sorted]
md_table = generate_columnar_table(data_lists, num_rows=5)

# Save the markdown table to a file
with open('centrality_comparison_columns.md', 'w') as f:
    f.write(md_table)

# Print a preview of the sorted data
print("Top 5 nodes for each centrality measure:")
for name, data in [
    ("Degree", degree_sorted[:5]),
    ("Eigenvector", eigen_sorted[:5]),
    ("PageRank", pagerank_sorted[:5]),
    ("Betweenness", between_sorted[:5]),
    ("Closeness", close_sorted[:5])
]:
    print(f"{name}: {', '.join([f'{node}:{value:.2f}' for node, value in data])}")

print("\nColumnar markdown table has been saved to 'centrality_comparison_columns.md'")