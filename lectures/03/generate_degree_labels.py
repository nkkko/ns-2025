import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def generate_default_graph():
    """
    Create the default graph from the lecture with node degrees as labels.
    Uses the same graph structure as in generate_centrality_images.py.
    """
    # Create graph
    G = nx.Graph()

    # Add nodes (based on the existing visualization in the slides)
    nodes = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
    ]
    G.add_nodes_from(nodes)

    # Add edges (matching exactly those in generate_centrality_images.py)
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

    # Calculate node degrees
    degrees = dict(G.degree())

    # Create a visualization with a spring layout for node positions
    plt.figure(figsize=(12, 10))
    # Use the same seed as in generate_centrality_images.py for consistent layout
    pos = nx.spring_layout(G, seed=3)

    # Draw the network
    nx.draw_networkx_edges(G, pos, alpha=0.3, width=1.5)

    # Draw nodes with custom colors and sizes
    nx.draw_networkx_nodes(
        G, pos,
        node_color='#a6dcef',
        node_size=700,
        edgecolors='black',
        linewidths=2
    )

    # Add node labels (node name)
    nx.draw_networkx_labels(G, pos, font_size=20, font_weight='bold')

    # Add degree labels below each node
    label_pos = {node: (pos[node][0], pos[node][1] - 0.08) for node in G.nodes()}
    degree_labels = {node: f"deg: {degrees[node]}" for node in G.nodes()}
    nx.draw_networkx_labels(
        G, label_pos, labels=degree_labels, font_size=14
    )

    plt.title("Default Graph with Node Degrees", fontsize=20)
    plt.axis('off')
    plt.tight_layout()

    # Save the image
    plt.savefig('images/degree_calculation.png', dpi=100)
    plt.close()

    return G, degrees

if __name__ == "__main__":
    G, degrees = generate_default_graph()
    print("Image generated: images/degree_calculation.png")

    # Print node degrees for reference
    sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
    print("\nNode degrees (sorted by degree):")
    for node, degree in sorted_degrees:
        print(f"Node {node}: {degree}")