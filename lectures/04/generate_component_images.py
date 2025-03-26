import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Create images directory if it doesn't exist
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

def generate_connected_components_example():
    """Generate a clear visualization of connected components in a graph."""
    # Create a graph with multiple components
    G = nx.Graph()

    # Component 1: A small complete graph
    G.add_edges_from([(1, 2), (1, 3), (2, 3)])

    # Component 2: A star-like structure
    G.add_edges_from([(4, 5), (4, 6), (4, 7), (4, 8)])

    # Component 3: A path
    G.add_edges_from([(9, 10), (10, 11), (11, 12)])

    # Set up the figure
    plt.figure(figsize=(12, 8))
    title = "Connected Components in an Undirected Graph"
    plt.title(title, pad=20, fontsize=16)

    # Get connected components
    components = list(nx.connected_components(G))

    # Generate a spring layout for the entire graph
    pos = nx.spring_layout(G, k=1, seed=42)

    # Colors for different components
    colors = ['#FF9999', '#99FF99', '#9999FF']

    # Draw each component with a different color
    for idx, component in enumerate(components):
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=list(component),
            node_color=colors[idx],
            node_size=1000
        )
        edges = [(u, v) for u, v in G.edges() if u in component]
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=2)

    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=12)

    # Add component labels
    for idx, component in enumerate(components):
        center = np.mean([pos[node] for node in component], axis=0)
        plt.text(
            center[0],
            center[1] + 0.15,
            f"Component {idx + 1}",
            horizontalalignment='center',
            fontsize=14
        )

    plt.axis('off')
    plt.tight_layout()

    # Save the figure
    plt.savefig('images/connected_components.png', dpi=100, bbox_inches='tight')
    plt.close()

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
    """Generate a clear visualization of strongly connected components in a directed graph."""
    G = nx.DiGraph()

    # Create three distinct strongly connected components with clear structure
    # SCC 1: A directed cycle with three nodes
    G.add_edges_from([(1, 2), (2, 3), (3, 1)])

    # SCC 2: A more complex component with bidirectional edges
    G.add_edges_from([
        (4, 5), (5, 4),  # Bidirectional edge
        (5, 6), (6, 7), (7, 5)  # Cycle with additional edge
    ])

    # SCC 3: A small bidirectional pair
    G.add_edges_from([(8, 9), (9, 8)])

    # Add connections between components (non-SCC edges)
    G.add_edges_from([(3, 4), (7, 8)])

    # Set up the figure
    plt.figure(figsize=(12, 8))
    title = "Strongly Connected Components (SCCs) in a Directed Graph"
    plt.title(title, pad=20, fontsize=16)

    # Get strongly connected components
    sccs = list(nx.strongly_connected_components(G))

    # Generate a spring layout with more space between components
    pos = nx.spring_layout(G, k=2, seed=42)

    # Colors for different components
    colors = ['#FF9999', '#99FF99', '#9999FF']

    # Draw each component with a different color
    for idx, component in enumerate(sccs):
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=list(component),
            node_color=colors[idx],
            node_size=1000
        )

        # Draw edges within the component
        internal_edges = [(u, v) for (u, v) in G.edges()
                        if u in component and v in component]
        nx.draw_networkx_edges(
            G, pos,
            edgelist=internal_edges,
            edge_color=colors[idx],
            width=2,
            arrowsize=20
        )

    # Draw edges between components in gray
    external_edges = [(u, v) for (u, v) in G.edges()
                     if not any(u in c and v in c for c in sccs)]
    nx.draw_networkx_edges(
        G, pos,
        edgelist=external_edges,
        edge_color='gray',
        width=1,
        style='dashed',
        arrowsize=15
    )

    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=12)

    # Add component labels with descriptions
    descriptions = [
        "Directed Cycle",
        "Complex SCC\nwith Multiple Cycles",
        "Bidirectional Pair"
    ]

    for idx, component in enumerate(sccs):
        center = np.mean([pos[node] for node in component], axis=0)
        plt.text(
            center[0],
            center[1] + 0.2,
            f"SCC {idx + 1}:\n{descriptions[idx]}",
            horizontalalignment='center',
            verticalalignment='bottom',
            fontsize=12,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.7)
        )

    plt.axis('off')
    plt.tight_layout()

    # Save the figure
    plt.savefig('images/strongly_connected_components.png',
                dpi=100, bbox_inches='tight')
    plt.close()

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

def generate_maximal_subgraph_example():
    """Generate a visualization explaining maximal connected subgraphs."""
    # Create the example graph from the text explanation
    G = nx.Graph()
    G.add_edges_from([
        ('A', 'B'), ('B', 'F'),
        ('C', 'D')
    ])
    G.add_node('E')  # Isolated node

    # Set up the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # First subplot: Original graph with components highlighted
    pos = {
        'A': (-1, 0.5), 'B': (0, 0.5), 'F': (-0.5, -0.5),  # First component
        'C': (2, 0.5), 'D': (3, 0.5),                       # Second component
        'E': (4.5, 0.5)                                      # Third component
    }

    # Draw the graph in the first subplot
    ax1.set_title('Connected Components', pad=20, fontsize=16)

    # Draw components with better colors
    colors = ['#FF7676', '#76FF76', '#7676FF']  # Brighter, more distinct colors

    # Draw each component
    nx.draw_networkx_nodes(G, pos, nodelist=['A', 'B', 'F'],
                         node_color=colors[0], node_size=1200, ax=ax1)
    nx.draw_networkx_nodes(G, pos, nodelist=['C', 'D'],
                         node_color=colors[1], node_size=1200, ax=ax1)
    nx.draw_networkx_nodes(G, pos, nodelist=['E'],
                         node_color=colors[2], node_size=1200, ax=ax1)

    # Draw edges with increased width
    nx.draw_networkx_edges(G, pos, width=3, ax=ax1)

    # Draw labels with white background for better visibility
    nx.draw_networkx_labels(G, pos, font_size=14, ax=ax1)

    # Add component labels with better positioning
    ax1.text(-0.5, 1.2, 'Component 1: {A,B,F}',
             horizontalalignment='center', fontsize=14,
             bbox=dict(facecolor=colors[0], edgecolor='none', alpha=0.2, pad=5))
    ax1.text(2.5, 1.2, 'Component 2: {C,D}',
             horizontalalignment='center', fontsize=14,
             bbox=dict(facecolor=colors[1], edgecolor='none', alpha=0.2, pad=5))
    ax1.text(4.5, 1.2, 'Component 3: {E}',
             horizontalalignment='center', fontsize=14,
             bbox=dict(facecolor=colors[2], edgecolor='none', alpha=0.2, pad=5))

    # Second subplot: Non-maximal vs Maximal subgraph example
    pos2 = {
        'A': (-1, 0), 'B': (0, 0), 'F': (-0.5, -1)
    }

    ax2.set_title('Non-maximal vs Maximal Subgraph', pad=20, fontsize=16)

    # Draw the complete subgraph structure first in light gray
    G2 = nx.Graph()
    G2.add_edges_from([('A', 'B'), ('B', 'F')])
    nx.draw_networkx_nodes(G2, pos2, node_color='#EEEEEE',
                         node_size=1200, ax=ax2)
    nx.draw_networkx_edges(G2, pos2, edge_color='#EEEEEE',
                         width=3, ax=ax2)

    # Draw non-maximal subgraph
    G2_non_maximal = nx.Graph()
    G2_non_maximal.add_edge('A', 'B')
    nx.draw_networkx_nodes(G2_non_maximal, pos2, nodelist=['A', 'B'],
                         node_color='#FFB6C1', node_size=1200, ax=ax2)
    nx.draw_networkx_edges(G2_non_maximal, pos2,
                         width=3, style='dashed',
                         edge_color='#FFB6C1', ax=ax2)

    # Draw the additional edge that makes it maximal with an arrow
    ax2.annotate('', xy=pos2['F'], xytext=pos2['B'],
                arrowprops=dict(arrowstyle='->',
                              color=colors[0],
                              lw=2,
                              ls='dotted'))

    # Draw labels
    nx.draw_networkx_labels(G2, pos2, font_size=14, ax=ax2)

    # Add explanatory text with better positioning and styling
    ax2.text(-0.5, -1.8, 'Non-maximal subgraph {A,B}\nMissing connection to F',
             horizontalalignment='center', fontsize=14,
             bbox=dict(facecolor='#FFB6C1', edgecolor='none', alpha=0.2, pad=5))
    ax2.text(-0.5, 1, 'Maximal subgraph {A,B,F}\nIncludes all possible connections',
             horizontalalignment='center', fontsize=14,
             bbox=dict(facecolor=colors[0], edgecolor='none', alpha=0.2, pad=5))

    # Set better axis limits for both subplots
    ax1.set_xlim(-2, 5.5)
    ax1.set_ylim(-1.5, 1.5)
    ax2.set_xlim(-2, 1)
    ax2.set_ylim(-2.2, 1.5)

    # Turn off axes for both subplots
    ax1.axis('off')
    ax2.axis('off')

    plt.tight_layout(w_pad=1)
    plt.savefig('images/maximal_subgraph_explanation.png',
                dpi=100, bbox_inches='tight', pad_inches=0.2)
    plt.close()

# Generate all images
if __name__ == "__main__":
    print("Generating connected components image...")
    generate_connected_components_example()

    print("Generating maximal subgraph explanation...")
    generate_maximal_subgraph_example()

    print("Generating articulation points image...")
    create_articulation_points_graph()

    print("Generating bridges image...")
    create_bridges_graph()

    print("Generating strongly connected components image...")
    create_strongly_connected_components()

    print("Generating critical node removal images...")
    create_critical_node_removal()

    print("All images generated successfully!")