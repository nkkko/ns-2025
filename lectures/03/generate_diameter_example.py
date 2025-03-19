import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def generate_diameter_example():
    """Generate visualization of the network diameter on the default graph."""
    print("Generating diameter example visualization...")

    # Create the default graph based on the existing visualizations
    G = nx.Graph()

    # Adding nodes (based on the default graph shown in other examples)
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
    G.add_nodes_from(nodes)

    # Add edges (using the same edges as in generate_centrality_images.py)
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

    # Calculate eccentricity for each node
    eccentricity = nx.eccentricity(G)

    # Calculate the diameter of the graph
    diameter = nx.diameter(G)

    # Find one of the diameter paths
    # Get all shortest paths between all pairs of nodes
    diameter_path = None
    for u in G.nodes():
        for v in G.nodes():
            if u != v:
                path = nx.shortest_path(G, u, v)
                if len(path) - 1 == diameter:
                    diameter_path = path
                    break
        if diameter_path:
            break

    # Use the same layout as the other centrality visualizations
    pos = nx.spring_layout(G, seed=3)  # Using the same seed for consistent layout

    # Draw the graph
    plt.figure(figsize=(12, 8))

    # Draw all nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')

    # Highlight nodes in the diameter path
    nx.draw_networkx_nodes(G, pos, nodelist=diameter_path, node_size=500, node_color='orange')

    # Draw all edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')

    # Highlight edges in the diameter path
    diameter_edges = [(diameter_path[i], diameter_path[i+1]) for i in range(len(diameter_path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=diameter_edges, width=3.0, edge_color='red')

    # Add node labels
    nx.draw_networkx_labels(G, pos, font_size=12)

    # Add a title with diameter value
    plt.title(f"Graph Diameter = {diameter}\nLongest shortest path: {' → '.join(diameter_path)}", fontsize=16)

    # Remove axis
    plt.axis('off')
    plt.tight_layout()

    # Save the image
    plt.savefig('images/diameter_example.png', dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Diameter of the graph: {diameter}")
    print(f"One diameter path: {' → '.join(diameter_path)}")

    return G, diameter, diameter_path

if __name__ == "__main__":
    generate_diameter_example()