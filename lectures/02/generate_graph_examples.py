import networkx as nx
import matplotlib.pyplot as plt
import os

# Create the images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Create the default graph
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
G.add_nodes_from(nodes)

# Add edges
edges = [
    # Top cluster (a-g)
    ('a', 'b'), ('a', 'd'), ('a', 'f'),
    ('b', 'd'), ('b', 'e'), ('b', 'g'),
    ('c', 'f'), ('c', 'h'),
    ('d', 'f'), ('d', 'e'),
    ('e', 'g'),
    ('f', 'g'), ('f', 'h'),
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

# Use the same layout for all visualizations
pos = nx.spring_layout(G, seed=3)  # Using a seed for reproducibility

# 1. Default Graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=1000,
        width=2,
        with_labels=True,
        font_size=18)
plt.title('Default Network Graph', fontsize=16)
plt.axis('off')
plt.savefig('images/default_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Graph Construction Example
plt.figure(figsize=(12, 8))
# First show only nodes
nx.draw_networkx_nodes(G, pos,
                      nodelist=nodes,
                      node_color='#a6dcef',
                      node_size=800)
nx.draw_networkx_labels(G, pos, font_size=18)
plt.title('Step 1: Adding Nodes to a Graph', fontsize=16)
plt.axis('off')
plt.savefig('images/graph_construction_nodes.png', dpi=300, bbox_inches='tight')
plt.close()

# Then show nodes and edges
plt.figure(figsize=(12, 8))
nx.draw(G, pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=800,
        width=1,
        with_labels=True,
        font_size=18)
plt.title('Step 2: Adding Edges to Connect Nodes', fontsize=16)
plt.axis('off')
plt.savefig('images/graph_construction_complete.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Vertex Degree Example
plt.figure(figsize=(12, 8))
# Highlight node j and its connections
node_colors = ['red' if node == 'j' else '#a6dcef' for node in G.nodes()]
edge_colors = ['red' if 'j' in edge else 'gray' for edge in G.edges()]
nx.draw(G, pos,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=800,
        width=2,
        with_labels=True,
        font_size=18)
plt.title('Vertex Degree Example: Node j has degree 5', fontsize=16)
plt.axis('off')
plt.savefig('images/vertex_degree.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Path Example
plt.figure(figsize=(12, 8))
# Highlight a path from a to m
path = ['a', 'f', 'h', 'i', 'j', 'l', 'm']
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]

# Draw the graph
nx.draw_networkx_nodes(G, pos,
                      node_color='#a6dcef',
                      node_size=800)
nx.draw_networkx_edges(G, pos,
                      edge_color='gray',
                      width=1)

# Highlight the path
nx.draw_networkx_nodes(G, pos,
                      nodelist=path,
                      node_color='lightgreen',
                      node_size=800)
nx.draw_networkx_edges(G, pos,
                      edgelist=path_edges,
                      edge_color='green',
                      width=3)
nx.draw_networkx_labels(G, pos, font_size=18)

plt.title('Path Example: a → f → h → i → j → l → m', fontsize=16)
plt.axis('off')
plt.savefig('images/path_example.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Cycle Example
plt.figure(figsize=(12, 8))
# Highlight a cycle
cycle = ['e', 'g', 'h', 'i', 'j', 'p', 'k', 'l', 'j', 'n', 'i', 'h', 'f', 'd', 'e']
cycle_edges = [(cycle[i], cycle[i+1]) for i in range(len(cycle)-1)]

# Draw the graph
nx.draw_networkx_nodes(G, pos,
                      node_color='#a6dcef',
                      node_size=800)
nx.draw_networkx_edges(G, pos,
                      edge_color='gray',
                      width=1)

# Highlight the cycle
nx.draw_networkx_nodes(G, pos,
                      nodelist=set(cycle),  # Use set to avoid duplicate nodes
                      node_color='#ffcccb',  # light red
                      node_size=800)
nx.draw_networkx_edges(G, pos,
                      edgelist=cycle_edges,
                      edge_color='red',
                      width=3)
nx.draw_networkx_labels(G, pos, font_size=18)

plt.title('Cycle Example: A path that starts and ends at the same vertex', fontsize=16)
plt.axis('off')
plt.savefig('images/cycle_example.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Undirected vs Directed Graph
# Create a directed version of part of the graph
DG = nx.DiGraph()
subgraph_nodes = ['a', 'b', 'c', 'd', 'e', 'f']
DG.add_nodes_from(subgraph_nodes)
directed_edges = [('a', 'b'), ('a', 'd'), ('a', 'f'),
                 ('b', 'd'), ('d', 'f'), ('c', 'f'),
                 ('e', 'd'), ('e', 'b')]
DG.add_edges_from(directed_edges)

# Undirected subgraph
plt.figure(figsize=(12, 8))
subgraph = G.subgraph(subgraph_nodes)
nx.draw(subgraph, pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=1400,
        width=2,
        with_labels=True,
        font_size=18)
plt.title('Undirected Graph: Edges have no direction', fontsize=16)
plt.axis('off')
plt.savefig('images/undirected_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# Directed subgraph
plt.figure(figsize=(12, 8))
nx.draw(DG, pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=1400,
        width=2,
        with_labels=True,
        font_size=18,
        arrows=True,
        arrowsize=20)
plt.title('Directed Graph: Edges have direction', fontsize=16)
plt.axis('off')
plt.savefig('images/directed_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. Weighted Graph Example
WG = nx.Graph()
WG.add_nodes_from(subgraph_nodes)
weighted_edges = [('a', 'b', 3), ('a', 'd', 2), ('a', 'f', 5),
                 ('b', 'd', 1), ('d', 'f', 4), ('c', 'f', 2),
                 ('e', 'd', 3), ('e', 'b', 2)]
WG.add_weighted_edges_from(weighted_edges)

plt.figure(figsize=(12, 8))
nx.draw(WG, pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=1400,
        width=2,
        with_labels=True,
        font_size=18)

# Add edge labels (weights)
edge_labels = {(u, v): d['weight'] for u, v, d in WG.edges(data=True)}
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels, font_size=10)

plt.title('Weighted Graph: Edges have associated values', fontsize=16)
plt.axis('off')
plt.savefig('images/weighted_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. Graph Representations - Adjacency Matrix
plt.figure(figsize=(10, 8))
subgraph = G.subgraph(['a', 'b', 'c', 'd'])
A = nx.adjacency_matrix(subgraph).todense()

plt.imshow(A, cmap='YlGn', vmin=0, vmax=2)  # Increased vmax to make green lighter
plt.colorbar(label='Connection')
plt.title('Adjacency Matrix Representation', fontsize=16)
plt.xticks(range(4), ['a', 'b', 'c', 'd'])
plt.yticks(range(4), ['a', 'b', 'c', 'd'])

for i in range(4):
    for j in range(4):
        plt.text(j, i, int(A[i, j]), ha='center', va='center', color='#8B0000')

plt.savefig('images/adjacency_matrix.png', dpi=300, bbox_inches='tight')
plt.close()

# 9. Connected Components Example
# Create a disconnected graph by removing some edges
CG = G.copy()
CG.remove_edge('h', 'i')
CG.remove_edge('h', 'r')

plt.figure(figsize=(12, 8))
# Get connected components
components = list(nx.connected_components(CG))
colors = ['#a6dcef', '#ffcccb', '#90ee90']  # Different colors for different components

# Color nodes by component
node_colors = []
for node in CG.nodes():
    for i, component in enumerate(components):
        if node in component:
            node_colors.append(colors[i % len(colors)])
            break

nx.draw(CG, pos,
        node_color=node_colors,
        edge_color='gray',
        node_size=800,
        width=1,
        with_labels=True,
        font_size=18)
plt.title('Connected Components: Disconnected Graph', fontsize=16)
plt.axis('off')
plt.savefig('images/connected_components.png', dpi=300, bbox_inches='tight')
plt.close()

# 10. Multigraph Example
MG = nx.MultiGraph()
multigraph_nodes = ['a', 'b', 'c', 'd']
MG.add_nodes_from(multigraph_nodes)
multigraph_edges = [
    ('a', 'b'), ('a', 'b'),  # Multiple edges between a and b
    ('b', 'c'), ('b', 'd'),
    ('c', 'd'), ('c', 'd'), ('c', 'd')  # Multiple edges between c and d
]
MG.add_edges_from(multigraph_edges)

# Create a custom layout for the multigraph
mg_pos = {
    'a': (0, 0),
    'b': (1, 0),
    'c': (1, 1),
    'd': (0, 1)
}

plt.figure(figsize=(10, 8))
nx.draw(MG, mg_pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=1600,
        width=2,
        with_labels=True,
        font_size=14)
plt.title('Multigraph: Allows Multiple Edges Between Vertices', fontsize=16)
plt.axis('off')
plt.savefig('images/multigraph.png', dpi=300, bbox_inches='tight')
plt.close()

# 11. Complete Graph Example
KG = nx.complete_graph(5)
# Relabel nodes to match our naming convention
mapping = {i: chr(97 + i) for i in range(5)}  # 0->a, 1->b, etc.
KG = nx.relabel_nodes(KG, mapping)

# Create a circular layout for the complete graph
kg_pos = nx.circular_layout(KG)

plt.figure(figsize=(10, 8))
nx.draw(KG, kg_pos,
        node_color='#a6dcef',
        edge_color='gray',
        node_size=1600,
        width=2,
        with_labels=True,
        font_size=14)
plt.title('Complete Graph: Every Vertex Connected to Every Other Vertex', fontsize=16)
plt.axis('off')
plt.savefig('images/complete_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# 12. Bipartite Graph Example
BG = nx.Graph()
# Two sets of nodes
set1 = ['a', 'b', 'c']
set2 = ['d', 'e', 'f', 'g']
BG.add_nodes_from(set1, bipartite=0)
BG.add_nodes_from(set2, bipartite=1)
# Edges only between sets, not within
bipartite_edges = [
    ('a', 'd'), ('a', 'e'), ('a', 'g'),
    ('b', 'd'), ('b', 'f'),
    ('c', 'e'), ('c', 'f'), ('c', 'g')
]
BG.add_edges_from(bipartite_edges)

# Create a custom layout for the bipartite graph
bg_pos = {}
for i, node in enumerate(set1):
    bg_pos[node] = (0, i - (len(set1) - 1) / 2)
for i, node in enumerate(set2):
    bg_pos[node] = (1, i - (len(set2) - 1) / 2)

plt.figure(figsize=(10, 8))
# Color nodes by set
node_colors = ['#a6dcef' if node in set1 else '#ffcccb' for node in BG.nodes()]
nx.draw(BG, bg_pos,
        node_color=node_colors,
        edge_color='gray',
        node_size=1600,
        width=2,
        with_labels=True,
        font_size=14)
plt.title('Bipartite Graph: Nodes Divided into Two Disjoint Sets', fontsize=16)
plt.axis('off')
plt.savefig('images/bipartite_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# 13. Tree Example - FIXED LAYOUT
# Create a simpler tree with fewer nodes to avoid cutoff
TG = nx.Graph()
tree_nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
TG.add_nodes_from(tree_nodes)
tree_edges = [
    ('a', 'b'), ('a', 'c'),
    ('b', 'd'), ('b', 'e'),
    ('c', 'f'), ('c', 'g')
]
TG.add_edges_from(tree_edges)

# Use a better layout for the tree with more vertical space
plt.figure(figsize=(8, 6))  # Adjusted figure size
# Create a hierarchical layout manually
tg_pos = {
    'a': (0.5, 0.9),  # Root at the top
    'b': (0.3, 0.6),  # Left branch
    'c': (0.7, 0.6),  # Right branch
    'd': (0.2, 0.3),  # Left-left leaf
    'e': (0.4, 0.3),  # Left-right leaf
    'f': (0.6, 0.3),  # Right-left leaf
    'g': (0.8, 0.3)   # Right-right leaf
}

nx.draw(TG, tg_pos,
        node_color='#90ee90',  # light green
        edge_color='gray',
        node_size=1600,
        width=2,
        with_labels=True,
        font_size=14)
plt.title('Tree: Connected Graph with No Cycles', fontsize=16)
plt.axis('off')
# Add more margin at the bottom
plt.savefig('images/tree_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# 14. Planar Graph Example - FIXED LAYOUT
PG = nx.Graph()
planar_nodes = ['a', 'b', 'c', 'd', 'e']
PG.add_nodes_from(planar_nodes)
planar_edges = [
    ('a', 'b'), ('a', 'c'), ('a', 'e'),
    ('b', 'c'), ('b', 'd'),
    ('c', 'd'), ('c', 'e'),
    ('d', 'e')
]
PG.add_edges_from(planar_edges)

# Use a better planar layout with more vertical space
plt.figure(figsize=(8, 6))  # Adjusted figure size
pg_pos = {
    'a': (0.2, 0.2),  # Bottom left
    'b': (0.8, 0.2),  # Bottom right
    'c': (0.5, 0.5),  # Center
    'd': (0.8, 0.8),  # Top right
    'e': (0.2, 0.8)   # Top left
}

nx.draw(PG, pg_pos,
        node_color='#d8bfd8',  # light purple
        edge_color='gray',
        node_size=1600,
        width=2,
        with_labels=True,
        font_size=14)
plt.title('Planar Graph: Can Be Drawn Without Edge Crossings', fontsize=16)
plt.axis('off')
plt.savefig('images/planar_graph.png', dpi=300)
plt.close()

print("All graph example images have been generated in the 'images' directory.")