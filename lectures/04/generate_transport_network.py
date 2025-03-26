import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def create_transport_network():
    """Create a transportation network representing cities and connections."""
    G = nx.Graph()

    # Add cities (nodes) with their positions to create a realistic layout
    cities = {
        'A': (0, 0),      # Central hub
        'B': (-1, 1),     # Northern city
        'C': (1, 1),      # Northern city
        'D': (-2, 0),     # Western city
        'E': (2, 0),      # Eastern city
        'F': (-1, -1),    # Southern city
        'G': (1, -1),     # Southern city
        'H': (-1.5, 0.5), # Intermediate city
        'I': (1.5, 0.5),  # Intermediate city
        'J': (0, -1.5),   # Southern hub
    }

    # Add nodes with positions
    for city, pos in cities.items():
        G.add_node(city, pos=pos)

    # Add transportation links (edges)
    edges = [
        ('A', 'B'), ('A', 'C'),  # Northern connections
        ('A', 'F'), ('A', 'G'),  # Southern connections
        ('B', 'H'), ('C', 'I'),  # Intermediate connections
        ('H', 'D'), ('I', 'E'),  # Outer city connections
        ('F', 'J'), ('G', 'J'),  # Southern hub connections
        ('B', 'C'), ('F', 'G'),  # Cross connections
        ('H', 'I'), ('D', 'F')   # Additional connections
    ]
    G.add_edges_from(edges)

    return G, cities

def analyze_network(G, pos):
    """Analyze network vulnerability and create visualizations."""
    # Find critical elements
    articulation_points = list(nx.articulation_points(G))
    bridges = list(nx.bridges(G))

    # Create visualization of the original network with critical elements
    plt.figure(figsize=(12, 8))
    plt.title('Transportation Network Analysis\nArticulation Points (Red) and Bridges (Blue)',
              pad=20, fontsize=16)

    # Draw the base network
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightgray')
    nx.draw_networkx_edges(G, pos, width=2, edge_color='lightgray')

    # Highlight articulation points
    nx.draw_networkx_nodes(G, pos, nodelist=articulation_points,
                         node_size=1000, node_color='#FF7676')

    # Highlight bridges
    bridge_edges = list(bridges)
    nx.draw_networkx_edges(G, pos, edgelist=bridge_edges,
                         width=3, edge_color='#7676FF')

    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=14)

    # Add legend
    plt.plot([], [], 'o', color='#FF7676', label='Articulation Points', markersize=15)
    plt.plot([], [], '-', color='#7676FF', label='Bridges', linewidth=3)
    plt.legend(fontsize=12)

    plt.axis('off')
    plt.tight_layout()
    plt.savefig('images/transport_network_analysis.png',
                dpi=100, bbox_inches='tight', pad_inches=0.2)
    plt.close()

    return articulation_points, bridges

def simulate_node_removal(G, pos, critical_node):
    """Simulate the removal of a critical node and visualize the impact."""
    plt.figure(figsize=(15, 6))

    # Before removal
    plt.subplot(121)
    plt.title('Before Removing Node ' + critical_node, pad=20, fontsize=14)
    nx.draw(G, pos, with_labels=True, node_size=1000,
           node_color='lightgray', font_size=14)
    nx.draw_networkx_nodes(G, pos, nodelist=[critical_node],
                         node_size=1000, node_color='#FF7676')
    plt.axis('off')

    # After removal
    plt.subplot(122)
    G_removed = G.copy()
    G_removed.remove_node(critical_node)

    # Color nodes by component
    components = list(nx.connected_components(G_removed))
    colors = plt.cm.Set3(np.linspace(0, 1, len(components)))

    plt.title(f'After Removing Node {critical_node}\n{len(components)} Components Formed',
              pad=20, fontsize=14)

    # Draw each component with a different color
    for idx, component in enumerate(components):
        nx.draw_networkx_nodes(G_removed, pos, nodelist=list(component),
                             node_size=1000, node_color=[colors[idx]])
        nx.draw_networkx_edges(G_removed, pos,
                             edgelist=G_removed.edges(component),
                             width=2)

    nx.draw_networkx_labels(G_removed, pos, font_size=14)
    plt.axis('off')

    plt.tight_layout()
    plt.savefig(f'images/transport_network_removal_{critical_node}.png',
                dpi=100, bbox_inches='tight', pad_inches=0.2)
    plt.close()

def analyze_network_resilience(G):
    """Analyze network resilience metrics."""
    metrics = {
        'Average Degree': sum(dict(G.degree()).values()) / G.number_of_nodes(),
        'Clustering Coefficient': nx.average_clustering(G),
        'Number of Components': nx.number_connected_components(G),
        'Average Path Length': nx.average_shortest_path_length(G),
        'Articulation Points': len(list(nx.articulation_points(G))),
        'Bridges': len(list(nx.bridges(G)))
    }
    return metrics

if __name__ == "__main__":
    print("Generating transportation network analysis...")

    # Create and analyze the network
    G, pos = create_transport_network()
    articulation_points, bridges = analyze_network(G, pos)

    # Simulate removal of most critical node
    critical_node = 'A'  # Central hub
    simulate_node_removal(G, pos, critical_node)

    # Calculate resilience metrics
    metrics = analyze_network_resilience(G)

    print("Transportation network analysis completed!")