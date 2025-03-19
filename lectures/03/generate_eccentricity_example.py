import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def generate_eccentricity_example():
    """Generate visualization of node eccentricity on the default graph."""
    print("Generating eccentricity visualization...")

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

    # Calculate the radius of the graph (minimum eccentricity)
    radius = nx.radius(G)

    # Calculate the diameter of the graph (maximum eccentricity)
    diameter = nx.diameter(G)

    # Find the central nodes (nodes with eccentricity equal to radius)
    central_nodes = [n for n in G.nodes() if eccentricity[n] == radius]

    # Find the peripheral nodes (nodes with eccentricity equal to diameter)
    peripheral_nodes = [n for n in G.nodes() if eccentricity[n] == diameter]

    # Use the same layout as the other centrality visualizations
    pos = nx.spring_layout(G, seed=3)  # Using the same seed for consistent layout

    # Create a color map based on eccentricity values
    cmap = plt.cm.YlOrRd

    # Normalize eccentricity values for color mapping
    eccentricity_values = list(eccentricity.values())
    min_ecc = min(eccentricity_values)
    max_ecc = max(eccentricity_values)
    norm_ecc = {node: (ecc - min_ecc) / (max_ecc - min_ecc) for node, ecc in eccentricity.items()}

    # Set up the figure with subplot for the main plot and colorbar
    fig, ax = plt.subplots(figsize=(12, 8))

    # Draw nodes with color based on eccentricity
    for node in G.nodes():
        # Use node size based on inverse of eccentricity (smaller eccentricity = larger node)
        node_size = 700 - (eccentricity[node] - min_ecc) * 50
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=[node],
            node_size=node_size,
            node_color=[cmap(norm_ecc[node])],
            edgecolors='black',
            linewidths=0.5,
            ax=ax
        )

    # Draw all edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray', ax=ax)

    # Add node labels with eccentricity values
    labels = {node: f"{node}\n({eccentricity[node]})" for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold', ax=ax)

    # Add a title with radius and diameter values
    ax.set_title(f"Node Eccentricity\nRadius = {radius}, Diameter = {diameter}", fontsize=16)

    # Add a colorbar legend
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(min_ecc, max_ecc))
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, shrink=0.75)
    cbar.set_label('Eccentricity Value', fontsize=12)

    # Highlight central nodes with green border
    if central_nodes:
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=central_nodes,
            node_size=[700 - (eccentricity[n] - min_ecc) * 50 for n in central_nodes],
            node_color='none',
            edgecolors='green',
            linewidths=3,
            ax=ax
        )

    # Highlight peripheral nodes with blue border
    if peripheral_nodes:
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=peripheral_nodes,
            node_size=[700 - (eccentricity[n] - min_ecc) * 50 for n in peripheral_nodes],
            node_color='none',
            edgecolors='blue',
            linewidths=3,
            ax=ax
        )

    # Add a legend for central and peripheral nodes
    ax.plot([], [], color='green', linewidth=3, label='Central Nodes (eccentricity = radius)')
    ax.plot([], [], color='blue', linewidth=3, label='Peripheral Nodes (eccentricity = diameter)')
    ax.legend(loc='upper left', fontsize=10)

    # Remove axis
    ax.axis('off')
    plt.tight_layout()

    # Save the image
    plt.savefig('images/eccentricity_example.png', dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Radius of the graph: {radius}")
    print(f"Diameter of the graph: {diameter}")
    print(f"Central nodes (eccentricity = {radius}): {', '.join(central_nodes)}")
    print(f"Peripheral nodes (eccentricity = {diameter}): {', '.join(peripheral_nodes)}")

    # Print eccentricity values for all nodes
    print("\nEccentricity values:")
    for node, ecc in sorted(eccentricity.items()):
        print(f"Node {node}: {ecc}")

    return G, eccentricity, radius, diameter

if __name__ == "__main__":
    generate_eccentricity_example()