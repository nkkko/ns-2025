import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
from community import best_partition  # python-louvain package for community detection

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def save_figure(G, filename, pos=None, title=None, figsize=(10, 8), dpi=100):
    """
    Save a network visualization with consistent styling.

    Args:
        G: NetworkX graph
        filename: Output filename
        pos: Node positions (optional)
        title: Plot title (optional)
        figsize: Figure size (width, height) in inches
        dpi: Resolution
    """
    plt.figure(figsize=figsize)

    if title:
        plt.title(title, fontsize=16)

    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f'images/{filename}', dpi=dpi)
    plt.close()

def generate_karate_club_graph():
    """
    Generate basic visualization of Zachary's Karate Club graph.
    """
    print("Generating basic Karate Club graph visualization...")

    # Create the graph
    G = nx.karate_club_graph()

    # Get positions using spring layout
    pos = nx.spring_layout(G, seed=42)

    # Set up the figure
    plt.figure(figsize=(10, 8))
    plt.title("Zachary's Karate Club Graph", fontsize=16)

    # Color nodes according to the known factions
    # Node 0 is the instructor, Node 33 is the administrator
    club_colors = ['#1f77b4' if G.nodes[node]['club'] == 'Mr. Hi' else '#ff7f0e'
                   for node in G.nodes()]

    # Draw the graph
    nx.draw(G, pos,
            with_labels=True,
            node_color=club_colors,
            node_size=700,
            font_size=10,
            font_weight='bold',
            edge_color='gray',
            width=0.5)

    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#1f77b4',
               label="Mr. Hi's group (Instructor)", markersize=10),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#ff7f0e',
               label="John A's group (Administrator)", markersize=10)
    ]
    plt.legend(handles=legend_elements, loc='upper right')

    # Save the figure
    plt.savefig('images/karate_club_graph.png', dpi=100)
    plt.close()

    print("Basic Karate Club graph visualization saved.")
    return G, pos

def generate_centrality_visualization(G=None, pos=None):
    """
    Generate visualization of the Karate Club graph with nodes sized by degree centrality.
    """
    print("Generating centrality visualization...")

    # Create the graph if not provided
    if G is None:
        G = nx.karate_club_graph()

    # Get positions if not provided
    if pos is None:
        pos = nx.spring_layout(G, seed=42)

    # Calculate degree centrality
    degree_centrality = nx.degree_centrality(G)

    # Set up the figure
    plt.figure(figsize=(10, 8))
    plt.title("Karate Club Graph - Degree Centrality", fontsize=16)

    # Color nodes according to the known factions
    club_colors = ['#1f77b4' if G.nodes[node]['club'] == 'Mr. Hi' else '#ff7f0e'
                   for node in G.nodes()]

    # Node sizes based on centrality (scaled for visibility)
    node_sizes = [degree_centrality[n] * 5000 for n in G]

    # Draw the graph
    nx.draw(G, pos,
            with_labels=True,
            node_color=club_colors,
            node_size=node_sizes,
            font_size=10,
            font_weight='bold',
            edge_color='gray',
            width=0.5)

    # Add centrality values as node labels
    centrality_labels = {node: f"{degree_centrality[node]:.2f}" for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=centrality_labels, font_size=8, verticalalignment='bottom',
                           bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=0.5))

    # Add legend for centrality
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#1f77b4',
               label="Mr. Hi's group", markersize=10),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#ff7f0e',
               label="John A's group", markersize=10),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',
               label="Node size = degree centrality", markersize=15)
    ]
    plt.legend(handles=legend_elements, loc='upper right')

    # Save the figure
    plt.savefig('images/karate_club_centrality.png', dpi=100)
    plt.close()

    print("Centrality visualization saved.")

def generate_community_visualization(G=None, pos=None):
    """
    Generate visualization of the Karate Club graph with community detection.
    """
    print("Generating community visualization...")

    # Create the graph if not provided
    if G is None:
        G = nx.karate_club_graph()

    # Get positions if not provided
    if pos is None:
        pos = nx.spring_layout(G, seed=42)

    # Detect communities using Louvain method
    partition = best_partition(G)

    # Set up the figure
    plt.figure(figsize=(10, 8))
    plt.title("Karate Club Graph - Community Detection", fontsize=16)

    # Color map for communities
    cmap = plt.cm.tab10

    # Draw the graph with communities
    nx.draw(G, pos,
            with_labels=True,
            node_color=[partition[n] for n in G.nodes()],
            cmap=cmap,
            node_size=700,
            font_size=10,
            font_weight='bold',
            edge_color='gray',
            width=0.5)

    # Calculate betweenness centrality
    betweenness = nx.betweenness_centrality(G)

    # Highlight high betweenness nodes (boundary spanners)
    high_betweenness_nodes = [n for n, b in betweenness.items() if b > 0.1]
    nx.draw_networkx_nodes(G, pos,
                          nodelist=high_betweenness_nodes,
                          node_color='white',
                          node_size=900,
                          alpha=0.3)

    # Add legend for communities
    from matplotlib.lines import Line2D

    # Get unique communities
    unique_communities = sorted(set(partition.values()))

    # Create legend elements
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=cmap(i),
               label=f"Community {i+1}", markersize=10)
        for i in unique_communities
    ]

    # Add boundary spanner element to legend
    legend_elements.append(Line2D([0], [0], marker='o', color='w', markerfacecolor='white',
                                  markeredgecolor='black', alpha=0.3,
                                  label="High betweenness node", markersize=15))

    plt.legend(handles=legend_elements, loc='upper right')

    # Save the figure
    plt.savefig('images/karate_club_communities.png', dpi=100)
    plt.close()

    print("Community visualization saved.")

# Main execution
if __name__ == "__main__":
    print("Generating Karate Club visualizations...")

    # Generate all visualizations
    G, pos = generate_karate_club_graph()
    generate_centrality_visualization(G, pos)
    generate_community_visualization(G, pos)

    print("All visualizations complete.")