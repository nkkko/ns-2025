import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
import community as community_louvain
import matplotlib.cm as cm

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def save_figure(G, filename, pos=None, title=None, figsize=(10, 8), dpi=100):
    """Helper function to save figures with consistent styling."""
    plt.figure(figsize=figsize)

    if title:
        plt.title(title, fontsize=16, pad=20)

    if pos is None:
        pos = nx.spring_layout(G, k=1, iterations=50)

    nx.draw(
        G, pos, with_labels=True, node_color='lightblue',
        node_size=500, font_size=12, font_weight='bold',
        edge_color='gray', width=2
    )

    plt.tight_layout()
    plt.savefig(f'images/{filename}', dpi=dpi, bbox_inches='tight')
    plt.close()

def generate_social_network_communities():
    """Generate a simple social network with clear community structure."""
    G = nx.Graph()

    # Create three communities
    community1 = ['A1', 'A2', 'A3', 'A4']
    community2 = ['B1', 'B2', 'B3', 'B4']
    community3 = ['C1', 'C2', 'C3', 'C4']

    # Add edges within communities (dense connections)
    for comm in [community1, community2, community3]:
        for i in range(len(comm)):
            for j in range(i+1, len(comm)):
                G.add_edge(comm[i], comm[j])

    # Add a few bridges between communities
    G.add_edge('A4', 'B1')
    G.add_edge('B4', 'C1')
    G.add_edge('A1', 'C4')

    # Position nodes to clearly show communities
    pos = nx.spring_layout(G, k=1, iterations=50)

    plt.figure(figsize=(10, 8))

    # Draw communities with different colors
    nx.draw_networkx_nodes(
        G, pos, nodelist=community1,
        node_color='lightblue', node_size=500
    )
    nx.draw_networkx_nodes(
        G, pos, nodelist=community2,
        node_color='lightgreen', node_size=500
    )
    nx.draw_networkx_nodes(
        G, pos, nodelist=community3,
        node_color='lightpink', node_size=500
    )

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    plt.title("Social Network Communities", fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig('images/social_network_communities.png', dpi=100, bbox_inches='tight')
    plt.close()

def generate_overlapping_communities():
    """Generate a network with overlapping communities."""
    G = nx.Graph()

    # Create communities with overlapping nodes
    community1 = ['A1', 'A2', 'A3', 'A4', 'AB']  # AB is shared
    community2 = ['B1', 'B2', 'B3', 'AB', 'BC']  # BC is shared
    community3 = ['C1', 'C2', 'C3', 'BC']

    # Add edges within communities
    for comm in [community1, community2, community3]:
        for i in range(len(comm)):
            for j in range(i+1, len(comm)):
                G.add_edge(comm[i], comm[j])

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=1, iterations=50)

    # Draw regular nodes
    nx.draw_networkx_nodes(
        G, pos, nodelist=['A1', 'A2', 'A3', 'A4'],
        node_color='lightblue', node_size=500
    )
    nx.draw_networkx_nodes(
        G, pos, nodelist=['B1', 'B2', 'B3'],
        node_color='lightgreen', node_size=500
    )
    nx.draw_networkx_nodes(
        G, pos, nodelist=['C1', 'C2', 'C3'],
        node_color='lightpink', node_size=500
    )

    # Draw overlapping nodes with different color
    nx.draw_networkx_nodes(
        G, pos, nodelist=['AB', 'BC'],
        node_color='yellow', node_size=500
    )

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    plt.title("Overlapping Communities", fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig('images/overlapping_communities.png', dpi=100, bbox_inches='tight')
    plt.close()

def generate_hierarchical_clustering():
    """Generate visualization of hierarchical clustering process."""
    fig, axes = plt.subplots(1, 4, figsize=(15, 4))

    # Create base graph
    G = nx.Graph()
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    G.add_nodes_from(nodes)
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, k=2)

    # Step 1: Individual nodes
    nx.draw(
        G, pos, ax=axes[0], with_labels=True,
        node_color='lightblue', node_size=500
    )
    axes[0].set_title("Step 1: Individual Nodes")

    # Step 2: First grouping
    colors = [
        'lightblue', 'lightblue', 'lightgreen', 'lightgreen',
        'lightpink', 'lightpink'
    ]
    nx.draw(
        G, pos, ax=axes[1], with_labels=True,
        node_color=colors, node_size=500
    )
    axes[1].set_title("Step 2: Initial Groups")

    # Step 3: Larger groups
    colors = [
        'lightblue', 'lightblue', 'lightblue',
        'lightgreen', 'lightgreen', 'lightgreen'
    ]
    nx.draw(
        G, pos, ax=axes[2], with_labels=True,
        node_color=colors, node_size=500
    )
    axes[2].set_title("Step 3: Larger Groups")

    # Step 4: Final group
    nx.draw(
        G, pos, ax=axes[3], with_labels=True,
        node_color='lightblue', node_size=500
    )
    axes[3].set_title("Step 4: Single Group")

    plt.tight_layout()
    plt.savefig('images/hierarchical_clustering.png', dpi=100, bbox_inches='tight')
    plt.close()

def generate_modularity_example():
    """Generate an example showing modularity calculation on a barbell graph"""
    # Create a simple network with two clear communities
    G = nx.barbell_graph(5, 0)  # Two complete graphs connected by a single edge
    
    # Use the Louvain method to detect communities
    communities = community_louvain.best_partition(G)
    
    # Calculate the modularity of this partition
    modularity = community_louvain.modularity(communities, G)
    
    # Visualize the communities
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)
    
    # Draw nodes with community colors
    colors = [communities[node] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, 
                         node_color=colors, 
                         cmap=plt.cm.Set1,
                         node_size=500)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7)
    
    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    # Add a title with modularity value
    plt.title(f"Network with Two Communities (Modularity: {modularity:.4f})", 
             fontsize=16)
    
    # Add annotation explaining modularity
    plt.figtext(0.5, 0.01, 
               "Modularity measures the quality of community division.\n"
               "Higher values (closer to 1.0) indicate better community structure.", 
               ha="center", fontsize=12, bbox={"facecolor":"lightgray", "alpha":0.5, "pad":5})
    
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('images/modularity_example.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_label_propagation_example():
    """Generate visualization of label propagation algorithm steps"""
    # Create a simple graph with community structure
    G = nx.Graph()
    
    # Create nodes with letters for better visualization
    communities = {
        'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
        'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
        'C': ['C1', 'C2', 'C3', 'C4', 'C5']
    }
    
    # Add all nodes
    for community in communities.values():
        G.add_nodes_from(community)
    
    # Add edges within communities (dense connections)
    for community in communities.values():
        for i, node1 in enumerate(community):
            for node2 in community[i+1:]:
                G.add_edge(node1, node2)
    
    # Add a few bridges between communities
    G.add_edge('A5', 'B1')
    G.add_edge('B5', 'C1')
    G.add_edge('C5', 'A1')
    
    # Create a layout for all stages
    pos = nx.spring_layout(G, seed=42)
    
    # Set up for 3-stage visualization
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Stage 1: Initial state, each node has its own label (color)
    colors = {}
    for i, node in enumerate(G.nodes()):
        colors[node] = i
    
    node_colors = [colors[node] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, ax=axes[0], 
                          node_color=node_colors, 
                          cmap=plt.cm.rainbow,
                          node_size=400)
    nx.draw_networkx_edges(G, pos, ax=axes[0], alpha=0.5)
    nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=9)
    axes[0].set_title("Step 1: Each Node Has Its Own Label", fontsize=14)
    axes[0].axis('off')
    
    # Stage 2: Intermediate state, labels start to propagate
    # This would be after a few iterations in a real algorithm
    mid_colors = {}
    for node in G.nodes():
        if node.startswith('A'):
            if node in ['A1', 'A2', 'A3']:
                mid_colors[node] = 0  # Same color for A1-A3
            else:
                mid_colors[node] = 1  # Different for A4-A5
        elif node.startswith('B'):
            if node in ['B1', 'B2', 'B3', 'B4']:
                mid_colors[node] = 2  # Same color for most B nodes
            else:
                mid_colors[node] = 3  # Different for B5
        elif node.startswith('C'):
            if node in ['C1', 'C2']:
                mid_colors[node] = 3  # C1-C2 match B5
            else:
                mid_colors[node] = 4  # Different for C3-C5
    
    node_colors = [mid_colors[node] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, ax=axes[1], 
                          node_color=node_colors, 
                          cmap=plt.cm.rainbow,
                          node_size=400)
    nx.draw_networkx_edges(G, pos, ax=axes[1], alpha=0.5)
    nx.draw_networkx_labels(G, pos, ax=axes[1], font_size=9)
    axes[1].set_title("Step 2: Labels Begin to Propagate", fontsize=14)
    axes[1].axis('off')
    
    # Stage 3: Final state, nodes in same community have same label
    final_colors = {}
    for node in G.nodes():
        if node.startswith('A'):
            final_colors[node] = 0  # All A nodes same color
        elif node.startswith('B'):
            final_colors[node] = 1  # All B nodes same color
        elif node.startswith('C'):
            final_colors[node] = 2  # All C nodes same color
    
    node_colors = [final_colors[node] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, ax=axes[2], 
                          node_color=node_colors, 
                          cmap=plt.cm.rainbow,
                          node_size=400)
    nx.draw_networkx_edges(G, pos, ax=axes[2], alpha=0.5)
    nx.draw_networkx_labels(G, pos, ax=axes[2], font_size=9)
    axes[2].set_title("Step 3: Final Communities Formed", fontsize=14)
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.savefig('images/label_propagation_example.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Generating visualizations for community detection lecture...")
    generate_social_network_communities()
    generate_overlapping_communities()
    generate_hierarchical_clustering()
    generate_modularity_example()
    generate_label_propagation_example()
    print("Done! Images saved in the 'images' directory.")