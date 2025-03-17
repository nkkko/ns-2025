import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# Function to save figures with consistent styling
def save_figure(G, filename, pos=None, node_color='skyblue', edge_color='gray',
                node_size=300, width=1.0, with_labels=True, font_size=10,
                node_colors=None, edge_colors=None, node_sizes=None,
                edge_widths=None, title=None, figsize=(10, 8), dpi=100):
    plt.figure(figsize=figsize)

    if title:
        plt.title(title, fontsize=16)

    if pos is None:
        pos = nx.spring_layout(G, seed=42)

    # Draw with custom node colors if provided
    if node_colors is not None:
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_size)
    else:
        nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size)

    # Draw with custom edge colors if provided
    if edge_colors is not None:
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=width)
    else:
        nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=width)

    # Draw labels
    if with_labels:
        nx.draw_networkx_labels(G, pos, font_size=font_size)

    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f'images/{filename}', dpi=dpi)
    plt.close()

# 1. Create a graph with multiple connected components
def create_components_graph():
    G = nx.Graph()

    # Add nodes for three components
    G.add_nodes_from(range(1, 21))

    # Component 1 (nodes 1-8)
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 5)])

    # Component 2 (nodes 9-15)
    G.add_edges_from([(9, 10), (9, 11), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 12)])

    # Component 3 (nodes 16-20)
    G.add_edges_from([(16, 17), (17, 18), (18, 19), (19, 20), (20, 16)])

    # Generate positions
    pos = nx.spring_layout(G, seed=42)

    # Color nodes by component
    components = list(nx.connected_components(G))
    node_colors = []
    for node in G.nodes():
        if node in components[0]:
            node_colors.append('skyblue')
        elif node in components[1]:
            node_colors.append('lightgreen')
        else:
            node_colors.append('salmon')

    save_figure(G, 'connected_components.png', pos=pos, node_colors=node_colors,
                title='Connected Components in an Undirected Graph', with_labels=True)

    return G, pos

# 2. Create a graph with articulation points (cut vertices)
def create_articulation_points_graph():
    G = nx.Graph()

    # Create a graph with clear articulation points
    G.add_edges_from([
        (1, 2), (1, 3), (2, 3),  # Triangle
        (3, 4),  # Articulation point at 3
        (4, 5), (4, 6), (5, 6),  # Triangle
        (6, 7),  # Articulation point at 6
        (7, 8), (7, 9), (8, 9),  # Triangle
        (9, 10), (9, 11), (10, 11)  # Triangle
    ])

    pos = nx.spring_layout(G, seed=42)

    # Identify articulation points
    articulation_points = list(nx.articulation_points(G))

    # Color articulation points differently
    node_colors = ['red' if node in articulation_points else 'skyblue' for node in G.nodes()]

    save_figure(G, 'articulation_points.png', pos=pos, node_colors=node_colors,
                title='Articulation Points (Cut Vertices)', with_labels=True)

    return G, pos, articulation_points

# 3. Create a graph with bridges (cut edges)
def create_bridges_graph():
    G = nx.Graph()

    # Create a graph with clear bridges
    G.add_edges_from([
        (1, 2), (1, 3), (2, 3),  # Triangle
        (3, 4),  # Bridge
        (4, 5), (4, 6), (5, 6),  # Triangle
        (6, 7),  # Bridge
        (7, 8), (7, 9), (8, 9)  # Triangle
    ])

    pos = nx.spring_layout(G, seed=42)

    # Identify bridges
    bridges = list(nx.bridges(G))

    # Color bridges differently
    edge_colors = ['red' if edge in bridges or (edge[1], edge[0]) in bridges else 'gray' for edge in G.edges()]

    save_figure(G, 'bridges.png', pos=pos, edge_colors=edge_colors,
                title='Bridges (Cut Edges)', with_labels=True)

    return G, pos, bridges

# 4. Create a directed graph with strongly connected components
def create_strongly_connected_components():
    G = nx.DiGraph()

    # Add edges to create strongly connected components
    G.add_edges_from([
        (1, 2), (2, 3), (3, 1),  # SCC 1
        (4, 5), (5, 6), (6, 4),  # SCC 2
        (3, 4),  # Connection between SCCs
        (7, 8), (8, 9), (9, 7),  # SCC 3
        (6, 7)   # Connection between SCCs
    ])

    pos = nx.spring_layout(G, seed=42)

    # Identify strongly connected components
    sccs = list(nx.strongly_connected_components(G))

    # Color nodes by SCC
    node_colors = []
    for node in G.nodes():
        if node in sccs[0]:
            node_colors.append('skyblue')
        elif node in sccs[1]:
            node_colors.append('lightgreen')
        else:
            node_colors.append('salmon')

    save_figure(G, 'strongly_connected_components.png', pos=pos, node_colors=node_colors,
                title='Strongly Connected Components in a Directed Graph', with_labels=True)

    return G, pos

# 5. Create a graph before and after removing a critical node
def create_critical_node_removal():
    G = nx.Graph()

    # Create a graph with a critical node
    G.add_edges_from([
        (1, 2), (1, 3), (2, 3), (3, 4),
        (4, 5), (4, 6), (5, 6), (5, 7),
        (7, 8), (7, 9), (8, 9)
    ])

    pos = nx.spring_layout(G, seed=42)

    # Save the original graph
    save_figure(G, 'before_removal.png', pos=pos,
                title='Network Before Removing Critical Node', with_labels=True)

    # Remove the critical node (node 4)
    critical_node = 4
    G.remove_node(critical_node)

    # Color nodes by component after removal
    components = list(nx.connected_components(G))
    node_colors = []
    for node in G.nodes():
        if node in components[0]:
            node_colors.append('skyblue')
        else:
            node_colors.append('salmon')

    save_figure(G, 'after_removal.png', pos=pos, node_colors=node_colors,
                title=f'Network After Removing Node {critical_node}', with_labels=True)

    return G, pos

# Generate all images
if __name__ == "__main__":
    print("Generating connected components image...")
    create_components_graph()

    print("Generating articulation points image...")
    create_articulation_points_graph()

    print("Generating bridges image...")
    create_bridges_graph()

    print("Generating strongly connected components image...")
    create_strongly_connected_components()

    print("Generating critical node removal images...")
    create_critical_node_removal()

    print("All images generated successfully!")