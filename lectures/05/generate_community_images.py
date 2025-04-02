#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import os
import community as community_louvain
from sklearn.cluster import SpectralClustering
from matplotlib.patches import Patch
from itertools import combinations
import matplotlib.colors as mcolors

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)


def generate_social_network_communities():
    """Generate an example social network with communities"""
    # Create a network with community structure
    G = nx.planted_partition_graph(4, 10, 0.8, 0.05, seed=42)
    
    # Get the ground truth communities
    communities = {node: i for i in range(4) for node in range(i*10, (i+1)*10)}
    
    # Visualize
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    
    # Color nodes based on community
    colors = [communities[node] for node in G.nodes()]
    
    nx.draw(G, pos, node_color=colors, cmap=plt.cm.rainbow,
            edge_color='gray', alpha=0.7, node_size=150, with_labels=False)
    
    # Add legend for communities
    legend_elements = [Patch(facecolor=plt.cm.rainbow(i/3), label=f'Community {i+1}')
                      for i in range(4)]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.title('Social Network Communities')
    plt.tight_layout()
    plt.savefig('images/social_network_communities.png', dpi=300, bbox_inches='tight')
    plt.close()


def generate_hierarchical_clustering():
    """Generate visualization of hierarchical clustering process"""
    # Create a network with clear communities
    G = nx.Graph()
    
    # Create three small clusters
    for i in range(3):
        # Create a 4-node cluster
        cluster_nodes = [f"{i}-{j}" for j in range(4)]
        G.add_nodes_from(cluster_nodes)
        
        # Connect all nodes in cluster (complete graph)
        for n1, n2 in combinations(cluster_nodes, 2):
            G.add_edge(n1, n2)
    
    # Add some inter-cluster edges
    G.add_edge("0-0", "1-0")
    G.add_edge("1-1", "2-1")
    G.add_edge("0-2", "2-2")
    
    # Compute a hierarchical clustering
    # In real applications we would use more sophisticated methods,
    # but for visualization we'll fake the process
    
    # Stage 1: 12 individual communities
    stage1 = {node: i for i, node in enumerate(G.nodes())}
    
    # Stage 2: Merge some close nodes
    stage2 = {
        "0-0": 0, "0-1": 0, "0-2": 0, "0-3": 0,
        "1-0": 1, "1-1": 1, "1-2": 2, "1-3": 2,
        "2-0": 3, "2-1": 3, "2-2": 4, "2-3": 4
    }
    
    # Stage 3: Merge into three main communities
    stage3 = {
        "0-0": 0, "0-1": 0, "0-2": 0, "0-3": 0,
        "1-0": 1, "1-1": 1, "1-2": 1, "1-3": 1,
        "2-0": 2, "2-1": 2, "2-2": 2, "2-3": 2
    }
    
    # Final stage: All merged
    final = {node: 0 for node in G.nodes()}
    
    # Set up the figure for visualizing the stages
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    axes = axes.flatten()
    
    # Compute a layout that will be used for all subplots
    pos = nx.spring_layout(G, seed=42)
    
    # Plot each stage
    stages = [stage1, stage2, stage3, final]
    stage_names = ['Initial', 'Early Stage', 'Middle Stage', 'Final Stage']
    
    for i, (stage, name) in enumerate(zip(stages, stage_names)):
        ax = axes[i]
        colors = [stage[node] for node in G.nodes()]
        nx.draw(G, pos, ax=ax, node_color=colors, cmap=plt.cm.tab20,
                edge_color='gray', alpha=0.7, node_size=150, with_labels=True,
                font_size=8)
        ax.set_title(name)
    
    # Create a dendrogram in the last subplot
    ax = axes[4]
    
    # Manually create a simple dendrogram for visualization
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)
    
    # Draw vertical lines for each node
    for i, node in enumerate(sorted(G.nodes())):
        ax.plot([i, i], [0, 1], 'k-')
        ax.text(i, -0.1, node, ha='center', va='top', fontsize=8)
    
    # Draw horizontal merges for stage 2
    ax.plot([0, 1], [1, 1], 'k-')
    ax.plot([2, 3], [1, 1], 'k-')
    ax.plot([4, 5], [1, 1], 'k-')
    ax.plot([6, 7], [1, 1], 'k-')
    ax.plot([8, 9], [1, 1], 'k-')
    ax.plot([10, 11], [1, 1], 'k-')
    
    # Draw vertical lines to level 2
    ax.plot([0.5, 0.5], [1, 2], 'k-')
    ax.plot([2.5, 2.5], [1, 2], 'k-')
    ax.plot([4.5, 4.5], [1, 2], 'k-')
    ax.plot([6.5, 6.5], [1, 2], 'k-')
    ax.plot([8.5, 8.5], [1, 2], 'k-')
    ax.plot([10.5, 10.5], [1, 2], 'k-')
    
    # Draw horizontal merges for stage 3
    ax.plot([0.5, 2.5], [2, 2], 'k-')
    ax.plot([4.5, 6.5], [2, 2], 'k-')
    ax.plot([8.5, 10.5], [2, 2], 'k-')
    
    # Draw vertical lines to level 3
    ax.plot([1.5, 1.5], [2, 3], 'k-')
    ax.plot([5.5, 5.5], [2, 3], 'k-')
    ax.plot([9.5, 9.5], [2, 3], 'k-')
    
    # Draw final merge
    ax.plot([1.5, 9.5], [3, 3], 'k-')
    ax.plot([5.5, 5.5], [3, 3.5], 'k-')
    
    ax.set_title('Dendrogram')
    ax.set_yticks([])
    ax.set_xticks([])
    
    # Remove the unused subplot
    axes[5].axis('off')
    
    plt.tight_layout()
    plt.savefig('images/hierarchical_clustering.png', dpi=300, bbox_inches='tight')
    plt.close()


def generate_louvain_method():
    """Generate visualization of the Louvain method execution"""
    # Create a network with clear community structure
    G = nx.Graph()
    
    # Add 15 nodes in 3 clusters
    for i in range(3):
        for j in range(5):
            G.add_node(f"{i}-{j}")
    
    # Add intra-cluster edges (higher density within clusters)
    for i in range(3):
        for j in range(5):
            for k in range(j+1, 5):
                if np.random.random() < 0.8:  # 80% chance of edge within cluster
                    G.add_edge(f"{i}-{j}", f"{i}-{k}")
    
    # Add some inter-cluster edges (lower density between clusters)
    for i in range(3):
        for j in range(i+1, 3):
            # Add 1-2 edges between clusters i and j
            for _ in range(np.random.randint(1, 3)):
                node1 = f"{i}-{np.random.randint(0, 5)}"
                node2 = f"{j}-{np.random.randint(0, 5)}"
                G.add_edge(node1, node2)
    
    # Create a layout for the original graph
    pos = nx.spring_layout(G, seed=42)
    
    # Phase 1: Local optimization (initial modularity optimization)
    # This would be computed by the Louvain algorithm, but for visualization
    # we'll just use the ground truth communities with some noise
    phase1 = {}
    for i in range(3):
        for j in range(5):
            # Assign most nodes to their correct community
            # but add some noise for the visualization
            if np.random.random() < 0.8:
                phase1[f"{i}-{j}"] = i
            else:
                # Randomly assign to a different community
                phase1[f"{i}-{j}"] = (i + np.random.randint(1, 3)) % 3
    
    # Phase 2: Create a new graph where nodes are communities from phase 1
    # We'll visualize this as the "collapsed" network
    community_to_nodes = {}
    for node, comm in phase1.items():
        if comm not in community_to_nodes:
            community_to_nodes[comm] = []
        community_to_nodes[comm].append(node)
    
    # Create the collapsed graph
    collapsed_G = nx.Graph()
    collapsed_G.add_nodes_from(community_to_nodes.keys())
    
    # Add edges between communities if there's an edge between any of their nodes
    for comm1, nodes1 in community_to_nodes.items():
        for comm2, nodes2 in community_to_nodes.items():
            if comm1 < comm2:  # Avoid duplicates
                # Check if there's any edge between communities
                for n1 in nodes1:
                    for n2 in nodes2:
                        if G.has_edge(n1, n2):
                            collapsed_G.add_edge(comm1, comm2)
                            break
                    else:
                        continue
                    break
    
    # Phase 3: Final output (after iterative application)
    # For visualization, we'll just show the ground truth communities
    final = {}
    for i in range(3):
        for j in range(5):
            final[f"{i}-{j}"] = i
    
    # Set up the figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Plot original graph with phase 1 communities
    ax = axes[0]
    colors = [phase1[node] for node in G.nodes()]
    nx.draw(G, pos, ax=ax, node_color=colors, cmap=plt.cm.rainbow,
            edge_color='gray', alpha=0.7, node_size=300, with_labels=True)
    ax.set_title('Phase 1: Local Optimization')
    
    # Plot the collapsed graph
    ax = axes[1]
    collapsed_pos = {i: np.mean([pos[node] for node in nodes], axis=0) 
                    for i, nodes in community_to_nodes.items()}
    
    # Draw the collapsed graph
    nx.draw(collapsed_G, collapsed_pos, ax=ax, node_color=list(collapsed_G.nodes()),
            cmap=plt.cm.rainbow, node_size=800, with_labels=True,
            edge_color='black', width=2)
    ax.set_title('Phase 2: Community Aggregation')
    
    # Plot final result
    ax = axes[2]
    colors = [final[node] for node in G.nodes()]
    nx.draw(G, pos, ax=ax, node_color=colors, cmap=plt.cm.rainbow,
            edge_color='gray', alpha=0.7, node_size=300, with_labels=True)
    ax.set_title('Final Result after Modularity Optimization')
    
    plt.tight_layout()
    plt.savefig('images/louvain_method.png', dpi=300, bbox_inches='tight')
    plt.close()


def generate_overlapping_communities():
    """Generate visualization of overlapping communities"""
    # Create a network with overlapping communities
    G = nx.Graph()
    
    # Add nodes (using single letters for simplicity)
    nodes = list('abcdefghijklmnopqrs')
    G.add_nodes_from(nodes)
    
    # Define overlapping communities
    communities = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  # blue
        ['f', 'g', 'h', 'i', 'j', 'k'],       # green
        ['j', 'k', 'l', 'm', 'n', 'o'],       # orange
        ['m', 'n', 'p', 'q', 'r', 's']        # red
    ]
    
    # Add edges within communities (with high probability)
    for community in communities:
        for n1, n2 in combinations(community, 2):
            if np.random.random() < 0.8:  # 80% chance of edge within community
                G.add_edge(n1, n2)
    
    # Add a few random edges
    for _ in range(5):
        n1, n2 = np.random.choice(nodes, 2, replace=False)
        G.add_edge(n1, n2)
    
    # Set up colors for visualization
    community_colors = [
        'tab:blue',
        'tab:green',
        'tab:orange', 
        'tab:red'
    ]
    
    # Create a node-to-communities mapping
    node_communities = {node: [] for node in nodes}
    for i, comm in enumerate(communities):
        for node in comm:
            node_communities[node].append(i)
    
    # Set up the figure
    plt.figure(figsize=(12, 10))
    
    # Use a layout that separates the communities well
    pos = nx.spring_layout(G, seed=42)
    
    # Draw the edges
    nx.draw_networkx_edges(G, pos, alpha=0.3, width=1)
    
    # Draw nodes that belong to multiple communities with pie charts
    for node in G.nodes():
        if len(node_communities[node]) > 1:
            # Draw a pie chart node
            pie_colors = [community_colors[comm] for comm in node_communities[node]]
            size = 800  # larger size for overlapping nodes
            
            # Calculate the size of each pie slice
            sizes = [1] * len(pie_colors)
            
            # Create a pie chart
            x, y = pos[node]
            plt.pie(sizes, colors=pie_colors, center=(x, y), radius=0.05)
            
            # Draw the node label
            plt.text(x, y, node, fontsize=12, ha='center', va='center',
                     bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
        else:
            # Single community node - draw with regular style
            nx.draw_networkx_nodes(G, pos, nodelist=[node], 
                                  node_color=[community_colors[node_communities[node][0]]],
                                  node_size=300, alpha=0.8)
            
            # Draw the node label
            x, y = pos[node]
            plt.text(x, y, node, fontsize=12, ha='center', va='center')
    
    # Add a legend
    legend_elements = [Patch(facecolor=color, label=f'Community {i+1}')
                       for i, color in enumerate(community_colors)]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.title('Network with Overlapping Communities')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('images/overlapping_communities.png', dpi=300, bbox_inches='tight')
    plt.close()


def generate_collaboration_network():
    """Generate a visualization of a scientific collaboration network"""
    # Create a collaboration network
    G = nx.Graph()
    
    # Generate researchers by department/topic
    departments = ['Physics', 'CS', 'Biology', 'Chemistry', 'Math']
    
    researchers = {}
    for dept in departments:
        # Create researchers for each department
        researchers[dept] = [f"{dept}{i}" for i in range(1, 11)]
        G.add_nodes_from(researchers[dept])
    
    # Add intra-department collaborations (high probability)
    for dept, members in researchers.items():
        for n1, n2 in combinations(members, 2):
            if np.random.random() < 0.6:  # 60% chance of collaboration within department
                G.add_edge(n1, n2)
    
    # Add inter-department collaborations (interdisciplinary, lower probability)
    for dept1, dept2 in combinations(departments, 2):
        # Number of interdisciplinary collaborations depends on department pairs
        if (dept1 == 'Physics' and dept2 == 'Math') or (dept1 == 'CS' and dept2 == 'Math'):
            # More collaborations between related fields
            num_collabs = np.random.randint(3, 7)
        else:
            num_collabs = np.random.randint(1, 4)
        
        for _ in range(num_collabs):
            researcher1 = np.random.choice(researchers[dept1])
            researcher2 = np.random.choice(researchers[dept2])
            G.add_edge(researcher1, researcher2)
    
    # Apply community detection (Louvain method)
    try:
        import community as community_louvain
        communities = community_louvain.best_partition(G)
    except ImportError:
        # If community package is not available, fake it
        communities = {}
        for dept_idx, dept in enumerate(departments):
            for researcher in researchers[dept]:
                if np.random.random() < 0.9:  # 90% correct classification
                    communities[researcher] = dept_idx
                else:
                    # Assign to a random different department
                    other_dept = np.random.choice([d for d in range(len(departments)) if d != dept_idx])
                    communities[researcher] = other_dept
    
    # Set up the visualization
    plt.figure(figsize=(14, 10))
    
    # Use a layout that separates the communities well
    pos = nx.spring_layout(G, k=0.3, seed=42)
    
    # Draw the network
    community_colors = list(mcolors.TABLEAU_COLORS)
    node_colors = [community_colors[communities[node] % len(community_colors)] for node in G.nodes()]
    
    nx.draw_networkx_edges(G, pos, alpha=0.3, width=0.8)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=100, alpha=0.8)
    
    # Draw researcher labels for a few key nodes
    # (in a real visualization we might not show all labels)
    central_nodes = sorted(G.degree, key=lambda x: x[1], reverse=True)[:15]
    central_nodes = [node for node, _ in central_nodes]
    
    nx.draw_networkx_labels(G, pos, {node: node for node in central_nodes},
                           font_size=8, font_color='black')
    
    # Add a legend
    legend_elements = [Patch(facecolor=community_colors[i % len(community_colors)], 
                           label=f'Community {i+1}')
                       for i in range(len(set(communities.values())))]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.title('Scientific Collaboration Network with Communities')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('images/collaboration_network.png', dpi=300, bbox_inches='tight')
    plt.close()


def generate_karate_club_communities():
    """Generate Zachary's Karate Club network with community visualization"""
    # Create the karate club graph
    G = nx.karate_club_graph()
    
    # Apply community detection (Louvain method)
    try:
        import community as community_louvain
        communities = community_louvain.best_partition(G)
    except ImportError:
        # If community package is not available, create a simplified version
        # where community assignment roughly matches the actual split
        communities = {}
        for node in G.nodes():
            if node in [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 21]:
                communities[node] = 0  # Mr. Hi's group
            else:
                communities[node] = 1  # John A's group
    
    # Set up the visualization
    plt.figure(figsize=(10, 8))
    
    # Use a layout that displays the community structure well
    pos = nx.spring_layout(G, seed=4)
    
    # Get a list of unique communities
    community_values = set(communities.values())
    
    # Create a color map
    colors = plt.cm.rainbow(np.linspace(0, 1, len(community_values)))
    color_map = {com: colors[i] for i, com in enumerate(sorted(community_values))}
    
    # Draw the network
    for community in sorted(community_values):
        # Get nodes in the community
        community_nodes = [node for node in G.nodes() if communities[node] == community]
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, 
                             nodelist=community_nodes,
                             node_color=[color_map[community]],
                             node_size=300,
                             alpha=0.8)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
    # Add a legend
    legend_elements = [Patch(facecolor=color_map[com], label=f'Community {com+1}')
                     for com in sorted(community_values)]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.title("Zachary's Karate Club with Detected Communities")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('images/karate_club_communities.png', dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    print("Generating community detection images...")
    
    # Generate all the images
    generate_social_network_communities()
    generate_hierarchical_clustering()
    generate_louvain_method()
    generate_overlapping_communities()
    generate_collaboration_network()
    generate_karate_club_communities()
    
    print("All images generated successfully!")