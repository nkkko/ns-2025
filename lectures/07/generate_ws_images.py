import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

# Function to create a Watts-Strogatz small-world network and visualize it
def create_ws_network(n=20, k=4, p=0.1, layout='circular', title=None, filename=None):
    """
    Creates and visualizes a Watts-Strogatz small-world network.
    
    Parameters:
    n (int): Number of nodes
    k (int): Each node is connected to k nearest neighbors in ring topology
    p (float): Probability of rewiring each edge
    layout (str): Layout for visualization ('circular' or 'spring')
    title (str): Title for the plot
    filename (str): Filename to save the plot
    """
    # Generate small-world network
    G = nx.watts_strogatz_graph(n, k, p)
    
    # Visualize
    plt.figure(figsize=(10, 8))
    
    if layout == 'circular':
        pos = nx.circular_layout(G)
    else:
        pos = nx.spring_layout(G, seed=42)
    
    nx.draw(G, pos, node_color='lightblue', node_size=500, with_labels=True, 
            font_weight='bold', width=2, edge_color='gray')
    
    if title:
        plt.title(title, fontsize=16)
    else:
        plt.title(f"Watts-Strogatz Small-World Network (n={n}, k={k}, p={p})", fontsize=16)
        
    plt.tight_layout()
    
    if filename:
        plt.savefig(f"images/{filename}", dpi=300, bbox_inches='tight')
        print(f"Saved {filename}")
    
    plt.close()

# Create visualizations for different rewiring probabilities
def create_rewiring_spectrum():
    """Create visualizations for different rewiring probabilities"""
    
    # Create different networks with varying rewiring probabilities
    probabilities = [0, 0.01, 0.1, 1.0]
    titles = [
        "Regular Lattice (p=0)",
        "Small-World Network (p=0.01)",
        "Small-World Network (p=0.1)",
        "Random Network (p=1.0)"
    ]
    filenames = [
        "regular_lattice.png",
        "small_world_p001.png",
        "small_world_p01.png",
        "random_network.png"
    ]
    
    # Generate individual networks
    for p, title, filename in zip(probabilities, titles, filenames):
        create_ws_network(n=20, k=4, p=p, title=title, filename=filename)
    
    # Create a combined visualization
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))
    axs = axs.flatten()
    
    for i, (p, title) in enumerate(zip(probabilities, titles)):
        G = nx.watts_strogatz_graph(20, 4, p)
        pos = nx.circular_layout(G)
        ax = axs[i]
        nx.draw(G, pos, ax=ax, node_color='lightblue', node_size=300, 
                with_labels=True, font_weight='bold', width=1.5, edge_color='gray')
        ax.set_title(title, fontsize=14)
    
    plt.tight_layout()
    plt.savefig("images/ws_rewiring_spectrum.png", dpi=300, bbox_inches='tight')
    print("Saved ws_rewiring_spectrum.png")
    plt.close()

# Create visualization of the rewiring process
def create_rewiring_process():
    """Create visualization of the rewiring process"""
    
    n = 10  # Smaller network for clarity
    k = 4
    
    # Create a regular ring lattice
    G = nx.watts_strogatz_graph(n, k, 0)
    
    # Create a figure with three panels
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    
    # Panel 1: Regular ring lattice
    pos = nx.circular_layout(G)
    nx.draw(G, pos, ax=axs[0], node_color='lightblue', node_size=500, 
            with_labels=True, font_weight='bold', width=2, edge_color='gray')
    axs[0].set_title("Regular Ring Lattice (p=0)", fontsize=14)
    
    # Panel 2: Small-world network (few rewired edges)
    G_sw = nx.watts_strogatz_graph(n, k, 0.1)
    nx.draw(G_sw, pos, ax=axs[1], node_color='lightblue', node_size=500, 
            with_labels=True, font_weight='bold', width=2)
    axs[1].set_title("Small-World Network (p=0.1)", fontsize=14)
    
    # Panel 3: Random network (all edges rewired)
    G_rand = nx.watts_strogatz_graph(n, k, 1.0)
    nx.draw(G_rand, pos, ax=axs[2], node_color='lightblue', node_size=500, 
            with_labels=True, font_weight='bold', width=2)
    axs[2].set_title("Random Network (p=1.0)", fontsize=14)
    
    plt.tight_layout()
    plt.savefig("images/ws_rewiring_process.png", dpi=300, bbox_inches='tight')
    print("Saved ws_rewiring_process.png")
    plt.close()

# Create plot showing small-world metrics as a function of rewiring probability
def create_small_world_metrics():
    """Create plot showing small-world metrics as a function of rewiring probability"""
    
    n = 100  # Larger network for better statistics
    k = 10
    
    # Range of probabilities (log scale)
    probs = np.logspace(-4, 0, 20)  # From 0.0001 to 1.0
    
    # Lists to store metrics
    clustering_values = []
    path_length_values = []
    
    # Reference values (p=0)
    G_reg = nx.watts_strogatz_graph(n, k, 0)
    C_reg = nx.average_clustering(G_reg)
    try:
        L_reg = nx.average_shortest_path_length(G_reg)
    except nx.NetworkXError:
        # In case the graph is not connected
        L_reg = np.mean([nx.average_shortest_path_length(G.subgraph(c)) 
                          for c in nx.connected_components(G_reg)])
    
    # Calculate metrics for each probability
    for p in probs:
        G = nx.watts_strogatz_graph(n, k, p)
        clustering_values.append(nx.average_clustering(G))
        try:
            path_length_values.append(nx.average_shortest_path_length(G))
        except nx.NetworkXError:
            # In case the graph is not connected
            path_length_values.append(np.mean([nx.average_shortest_path_length(G.subgraph(c)) 
                                               for c in nx.connected_components(G)]))
    
    # Normalize values relative to the regular lattice (p=0)
    norm_clustering = [c/C_reg for c in clustering_values]
    norm_path_length = [l/L_reg for l in path_length_values]
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.semilogx(probs, norm_clustering, 'bo-', label='Normalized Clustering C(p)/C(0)')
    plt.semilogx(probs, norm_path_length, 'ro-', label='Normalized Path Length L(p)/L(0)')
    plt.grid(True, alpha=0.3)
    plt.xlabel('Rewiring Probability (p)', fontsize=12)
    plt.ylabel('Normalized Metrics', fontsize=12)
    plt.title('Small-World Metrics as a Function of Rewiring Probability', fontsize=14)
    plt.legend(fontsize=12)
    plt.tight_layout()
    
    # Add vertical lines at interesting regions
    plt.axvspan(1/n, 10/n, alpha=0.2, color='gray')
    plt.text(5/n, 0.5, 'Small-World\nRegion', ha='center', fontsize=10)
    
    plt.savefig("images/small_world_metrics.png", dpi=300, bbox_inches='tight')
    print("Saved small_world_metrics.png")
    plt.close()

# Create visualization for small-world navigation
def create_navigation_example():
    """Create visualization for small-world navigation"""
    
    # Create a small-world network
    n = 40
    k = 4
    p = 0.1
    G = nx.watts_strogatz_graph(n, k, p)
    
    # Choose source and target nodes on opposite sides of the network
    source = 0
    target = 20
    
    # Find shortest path
    path = nx.shortest_path(G, source=source, target=target)
    
    # Create visualization
    plt.figure(figsize=(10, 8))
    pos = nx.circular_layout(G)
    
    # Draw the network with different colors for path nodes
    node_colors = ['red' if node == source else 'green' if node == target 
                    else 'orange' if node in path else 'lightblue' for node in G.nodes()]
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
    
    # Draw edges with different styles
    edge_colors = []
    edge_widths = []
    
    for u, v in G.edges():
        if u in path and v in path and abs(path.index(u) - path.index(v)) == 1:
            edge_colors.append('red')
            edge_widths.append(3.0)
        else:
            edge_colors.append('gray')
            edge_widths.append(1.0)
    
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_weight='bold')
    
    plt.title(f"Navigation in a Small-World Network (Path Length: {len(path)-1})", fontsize=14)
    plt.tight_layout()
    
    plt.savefig("images/small_world_navigation.png", dpi=300, bbox_inches='tight')
    print("Saved small_world_navigation.png")
    plt.close()

if __name__ == "__main__":
    # Create all the visualizations
    create_rewiring_process()
    create_rewiring_spectrum()
    create_small_world_metrics()
    create_navigation_example()
    
    # Create a basic small-world network visualization
    create_ws_network(n=30, k=4, p=0.1, filename="small_world_basic.png")