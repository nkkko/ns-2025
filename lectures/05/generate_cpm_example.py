#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Patch
import matplotlib.colors as mcolors
from itertools import combinations

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def generate_cpm_example():
    """Generate visualization of Clique Percolation Method"""
    # Create a simple graph with overlapping communities based on triangles (3-cliques)
    G = nx.Graph()
    
    # Create nodes
    nodes = list('ABCDEFGH')
    G.add_nodes_from(nodes)
    
    # Add edges to create two overlapping communities
    # Community 1: A-B-C-D
    G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), 
                       ('B', 'D'), ('C', 'D')])
    
    # Community 2: D-E-F-G-H
    G.add_edges_from([('D', 'E'), ('D', 'F'), ('E', 'F'), 
                       ('E', 'G'), ('F', 'G'), ('F', 'H'), ('G', 'H')])
    
    # Set up the visualization with multiple stages
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.flatten()
    
    # Use a consistent layout
    pos = {
        'A': (0, 2),
        'B': (1, 3),
        'C': (2, 2),
        'D': (3, 3),
        'E': (4, 2),
        'F': (5, 3),
        'G': (6, 2),
        'H': (7, 3)
    }
    
    # Step 1: Original network
    ax = axes[0]
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=500, 
            node_color='lightblue', font_weight='bold', font_size=14)
    ax.set_title('Step 1: Original Network', fontsize=14)
    
    # Step 2: Find all 3-cliques (triangles)
    ax = axes[1]
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=500, 
            node_color='lightgray', font_weight='bold', font_size=14, alpha=0.4)
    
    # Highlight the triangles
    triangles = [
        ('A', 'B', 'C'),
        ('B', 'C', 'D'),
        ('D', 'E', 'F'),
        ('E', 'F', 'G'),
        ('F', 'G', 'H')
    ]
    
    triangle_colors = ['red', 'orange', 'green', 'blue', 'purple']
    
    for i, triangle in enumerate(triangles):
        # Draw the triangle edges with thicker lines
        for u, v in combinations(triangle, 2):
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], ax=ax, 
                                width=3, edge_color=triangle_colors[i], alpha=0.7)
        
        # Draw the triangle nodes
        nx.draw_networkx_nodes(G, pos, nodelist=triangle, ax=ax,
                              node_color=triangle_colors[i], node_size=500, alpha=0.6)
    
    # Add legend for triangles
    legend_elements = [Patch(facecolor=color, label=f'Triangle {i+1}')
                       for i, color in enumerate(triangle_colors)]
    ax.legend(handles=legend_elements, loc='upper right')
    ax.set_title('Step 2: Identify k-cliques (k=3, triangles)', fontsize=14)
    
    # Step 3: Build the clique graph
    ax = axes[2]
    
    # Create a new graph where nodes are the triangles
    clique_graph = nx.Graph()
    clique_graph.add_nodes_from(range(len(triangles)))
    
    # Connect triangles that share k-1 nodes
    for i, tri1 in enumerate(triangles):
        for j, tri2 in enumerate(triangles):
            if i < j:  # Avoid duplicates
                common_nodes = set(tri1) & set(tri2)
                if len(common_nodes) >= 2:  # For k=3, triangles share k-1=2 nodes
                    clique_graph.add_edge(i, j)
    
    # Position the triangle nodes
    tri_pos = {
        0: (1, 2),   # Triangle A-B-C
        1: (2.5, 2), # Triangle B-C-D
        2: (4, 2),   # Triangle D-E-F
        3: (5.5, 2), # Triangle E-F-G
        4: (7, 2),   # Triangle F-G-H
    }
    
    # Draw the clique graph
    nx.draw(clique_graph, tri_pos, ax=ax, with_labels=True, 
            node_color=[triangle_colors[i] for i in range(len(triangles))],
            node_size=800, font_weight='bold', font_color='white', font_size=14)
    
    # Label the nodes with triangle information
    labels = {i: f"{'-'.join(triangles[i])}" for i in range(len(triangles))}
    nx.draw_networkx_labels(clique_graph, tri_pos, labels=labels, ax=ax,
                          font_size=10, font_color='black',
                          bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    
    ax.set_title('Step 3: Build Clique Graph', fontsize=14)
    
    # Step 4: Find connected components and map back to original network
    ax = axes[3]
    
    # Get connected components from the clique graph
    components = list(nx.connected_components(clique_graph))
    
    # Map components back to original nodes
    community_nodes = []
    for comp in components:
        community = set()
        for i in comp:
            community.update(triangles[i])
        community_nodes.append(community)
    
    # Draw the original network with communities highlighted
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=500,
            node_color='lightgray', font_weight='bold', font_size=14, alpha=0.4)
    
    # Highlight communities
    community_colors = ['#ffcccc', '#ccffcc']  # Light red and light green
    
    for i, community in enumerate(community_nodes):
        # Draw community nodes
        node_color = community_colors[i] if i < len(community_colors) else 'lightblue'
        
        # Draw community as a background circle
        x_coords = [pos[node][0] for node in community]
        y_coords = [pos[node][1] for node in community]
        center_x = sum(x_coords) / len(x_coords)
        center_y = sum(y_coords) / len(y_coords)
        
        # Calculate radius with some padding
        radius = max([(pos[node][0] - center_x)**2 + (pos[node][1] - center_y)**2 
                      for node in community])**0.5 + 0.5
        
        community_circle = plt.Circle((center_x, center_y), radius, 
                                    color=node_color, alpha=0.3)
        ax.add_patch(community_circle)
    
    # Draw the nodes again on top
    for i, community in enumerate(community_nodes):
        # Highlight overlapping nodes
        overlap_nodes = set()
        for j, other_comm in enumerate(community_nodes):
            if i != j:
                overlap_nodes.update(community & other_comm)
        
        # Draw regular community nodes
        regular_nodes = community - overlap_nodes
        if regular_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=list(regular_nodes), ax=ax,
                                  node_color=community_colors[i] if i < len(community_colors) else 'lightblue',
                                  node_size=500)
        
        # Draw overlapping nodes with a special color
        if overlap_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=list(overlap_nodes), ax=ax,
                                  node_color='yellow', node_size=500)
    
    # Draw the edges
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray')
    
    # Draw labels again to make sure they're visible
    nx.draw_networkx_labels(G, pos, ax=ax, font_weight='bold', font_size=14)
    
    # Add a legend
    legend_elements = [
        Patch(facecolor=community_colors[0], alpha=0.3, label='Community 1'),
        Patch(facecolor=community_colors[1], alpha=0.3, label='Community 2'),
        Patch(facecolor='yellow', label='Overlap Node')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    ax.set_title('Step 4: Communities and Overlapping Nodes', fontsize=14)
    
    plt.tight_layout()
    plt.savefig('images/cpm_example.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Generating CPM example visualization...")
    generate_cpm_example()
    print("CPM example image generated successfully!")