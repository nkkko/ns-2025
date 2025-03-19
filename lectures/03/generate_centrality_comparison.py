#!/usr/bin/env python3
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.colors import LinearSegmentedColormap

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Create the same graph as in generate_centrality_images.py
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
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
    eigenvector_centrality = {node: sum(degree_centrality[nbr] for nbr in G.neighbors(node))
                             for node in G.nodes()}
    # Normalize
    max_val = max(eigenvector_centrality.values())
    eigenvector_centrality = {k: v/max_val for k, v in eigenvector_centrality.items()}

pagerank = nx.pagerank(G, alpha=0.85)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# Create a DataFrame for comparison
data = {
    'Degree': [degree_centrality[n] for n in nodes],
    'Eigenvector': [eigenvector_centrality[n] for n in nodes],
    'PageRank': [pagerank[n] for n in nodes],
    'Betweenness': [betweenness_centrality[n] for n in nodes],
    'Closeness': [closeness_centrality[n] for n in nodes]
}
df = pd.DataFrame(data, index=nodes)

# Find top 3 nodes for each centrality measure
top_nodes = {}
for measure in df.columns:
    top_nodes[measure] = df[measure].nlargest(3).index.tolist()

# Print top nodes for each measure
print("Top 3 nodes by centrality measure:")
for measure, nodes_list in top_nodes.items():
    print(f"{measure}: {', '.join(nodes_list)}")

# Function to create a heatmap-style table figure
def create_centrality_comparison(df, filename, figsize=(12, 10), highlight_top=3):
    plt.figure(figsize=figsize)

    # Round values for display
    df_display = df.round(2)

    # Create a simpler table approach without the complex highlighting
    # Create the table
    ax = plt.gca()
    ax.axis('tight')
    ax.axis('off')

    # Create a different color for each column
    colors = ['#a6dcef', '#90ee90', '#ffd700', '#f08080', '#87cefa']
    cell_colors = []

    # Generate text for display with highlighting
    cell_text = []
    for i, row_idx in enumerate(df.index):
        row_values = []
        for j, col in enumerate(df.columns):
            value = df.loc[row_idx, col]
            # Get rank of this value in its column
            rank = df[col].rank(ascending=False)[row_idx]

            # Format with bold for top values
            if rank <= highlight_top:
                value_text = f"**{value:.2f}**"  # Bold for top values
            else:
                value_text = f"{value:.2f}"

            row_values.append(value_text)
        cell_text.append(row_values)

    # Create table
    table = ax.table(
        cellText=cell_text,
        rowLabels=df.index,
        colLabels=df.columns,
        loc='center',
        cellLoc='center'
    )

    # Adjust table style
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.5)

    plt.title('Comparison of Centrality Measures', fontsize=16)
    plt.tight_layout()
    plt.savefig(f'images/{filename}', dpi=300, bbox_inches='tight')
    plt.close()

# Generate the centrality comparison table
create_centrality_comparison(df, 'centrality_comparison.png')

print("Centrality comparison table has been saved to 'images/centrality_comparison.png'")