import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def generate_density_example():
    """Generate visualization of network density on the default graph."""
    print("Generating density visualization...")

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

    # Calculate graph properties
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()
    max_possible_edges = n_nodes * (n_nodes - 1) // 2  # For undirected graph

    # Calculate density
    density = nx.density(G)

    # Use the same layout as the other visualizations
    pos = nx.spring_layout(G, seed=3)  # Using the same seed for consistent layout

    # Set up the figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Create a complete graph with the same nodes to show all possible edges
    K = nx.complete_graph(n_nodes)

    # Map the complete graph nodes to our actual node labels
    mapping = {i: list(G.nodes())[i] for i in range(n_nodes)}
    K = nx.relabel_nodes(K, mapping)

    # First, draw all possible edges (from complete graph) as very light gray
    nx.draw_networkx_edges(
        K, pos,
        width=0.5,
        alpha=0.1,
        edge_color='gray',
        style='dashed',
        ax=ax
    )

    # Then draw actual edges in blue
    nx.draw_networkx_edges(
        G, pos,
        width=2.0,
        alpha=0.7,
        edge_color='blue',
        ax=ax
    )

    # Draw all nodes
    nx.draw_networkx_nodes(
        G, pos,
        node_size=500,
        node_color='lightblue',
        edgecolors='black',
        ax=ax
    )

    # Add node labels
    nx.draw_networkx_labels(
        G, pos,
        font_size=12,
        font_weight='bold',
        ax=ax
    )

    # Add density calculation as text
    density_text = (
        f"Network Density Calculation\n\n"
        f"Number of nodes: {n_nodes}\n"
        f"Number of edges: {n_edges}\n"
        f"Maximum possible edges: {max_possible_edges}\n\n"
        f"Density = $\\frac{{2|E|}}{{|V|(|V|-1)}}$ = $\\frac{{2 \\times {n_edges}}}{{{n_nodes} \\times ({n_nodes}-1)}}$ = {density:.4f}"
    )

    # Position the text in the upper left corner
    plt.text(
        0.02, 0.98,
        density_text,
        transform=ax.transAxes,
        fontsize=14,
        verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8)
    )

    # Add a title
    ax.set_title("Network Density", fontsize=16)

    # Remove axis
    ax.axis('off')
    plt.tight_layout()

    # Save the image
    plt.savefig('images/density_example.png', dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Graph density: {density:.4f}")
    print(f"Number of nodes: {n_nodes}")
    print(f"Number of edges: {n_edges}")
    print(f"Maximum possible edges: {max_possible_edges}")

    return G, density

if __name__ == "__main__":
    generate_density_example()