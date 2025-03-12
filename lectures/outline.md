# Lecture Outline

## 1. Introduction to Complex Networks

### Section 1:
- Definitions of networks, nodes, edges, and graphs
- Types of networks: social, technological, biological, etc.
- Examples of real-world complex systems
- Basic graph theory concepts: directed vs. undirected graphs, degree of a vertex
- Representing graphs: adjacency matrices, edge lists

### Section 2:
- Constructing simple networks using NetworkX
- **Coding Task:** Create a graph representing a social network of friends and visualize it
- **Natural Language Task:** Describe a transportation network as a graph on a whiteboard
- Visualization of networks using Matplotlib
- Adding node and edge attributes

---

## 2. Network Properties and Measures

### Section 1:
- Degree distribution
- Average degree of a graph
- Paths, distances, and connectivity
- Complete graphs, regular graphs, and bipartite graphs

### Section 2:
- Calculating degree distribution and average degree using NetworkX
- **Coding Task:** Compute the average path length in a collaboration network
- **Natural Language Task:** Explain the difference between a complete graph and a regular graph
- Visualizing degree distributions

---

## 3. Centrality Measures

### Section 1:
- Degree centrality, betweenness centrality, closeness centrality
- Eigenvector centrality, PageRank
- Hubs and authorities

### Section 2:
- Implementing centrality measures using NetworkX
- **Coding Task:** Identify the most influential nodes in a social network using different centrality measures
- **Natural Language Task:** Discuss the implications of high betweenness centrality in a communication network
- Comparing different centrality measures

---

## 4. Network Connectivity and Components

### Section 1:
- Connected components, giant connected component (GCC)
- Strongly and weakly connected components in directed graphs
- Articulation vertices and bridges

### Section 2:
- Finding connected components and articulation vertices using NetworkX
- **Coding Task:** Analyze the connectivity of a transportation network after removing a critical node
- **Natural Language Task:** Explain the importance of identifying articulation points in a network
- Visualizing network components

---

## 5. Community Detection

### Section 1:
- Definition of community structure and modularity
- Louvain algorithm for community detection
- Other community detection methods: clique-based methods, spectral clustering

### Section 2:
- Implementing the Louvain algorithm using the community module in Python
- **Coding Task:** Detect communities in a social network and visualize the community structure
- **Natural Language Task:** Discuss how community detection can be used to identify interest groups in a social media network
- Comparing different community detection algorithms

---

## 6. Network Assortativity and Homophily

### Section 1:
- Assortativity and disassortativity
- Measuring assortativity coefficient
- Homophily in social networks

### Section 2:
- Calculating assortativity using NetworkX
- **Coding Task:** Investigate the assortativity of a co-authorship network based on researcher attributes
- **Natural Language Task:** Explain how homophily affects the formation of social networks
- Visualizing assortativity patterns

---

## 7. Path Analysis and Network Efficiency

### Section 1:
- Shortest paths and average path length
- Network diameter and radius
- Network efficiency and robustness

### Section 2:
- Computing shortest paths and network diameter using NetworkX
- **Coding Task:** Evaluate the efficiency of a transportation network by calculating average path lengths
- **Natural Language Task:** Discuss how network efficiency is related to network robustness
- Visualizing paths and distances

---

## 8. Random Graph Models

### Section 1:
- Erdős-Rényi model
- Configuration model
- Comparing random graph models with real-world networks

### Section 2:
- Generating random graphs using NetworkX
- **Coding Task:** Create an Erdős-Rényi graph with the same number of nodes and edges as a real-world network and compare their properties
- **Natural Language Task:** Explain the differences between random graph models and real-world networks
- Analyzing the properties of random graphs

---

## 9. Scale-Free Networks and Preferential Attachment

### Section 1:
- Power-law degree distribution
- Barabási-Albert model for generating scale-free networks
- Properties of scale-free networks: robustness and vulnerability

### Section 2:
- Generating scale-free networks using NetworkX
- **Coding Task:** Construct a scale-free network using the preferential attachment model and analyze its degree distribution
- **Natural Language Task:** Discuss the implications of scale-free networks for information diffusion
- Visualizing power-law degree distributions

---

## 10. Network Dynamics and Epidemic Modelling

### Section 1:
- Basic epidemic models: SI, SIR, SIS
- Threshold models and influence
- Modelling diffusion and contagion on networks

### Section 2:
- Simulating epidemic spreading using Python
- **Coding Task:** Implement the SIR model on a social network and analyze the spread of an infection
- **Natural Language Task:** Discuss how network structure affects the spread of a disease
- Visualizing the spread of epidemics on networks

---

## 11. Temporal Networks

### Section 1:
- Definition of temporal networks and their properties
- Representing temporal networks: edge lists with timestamps, time-aggregated graphs
- Analyzing network evolution over time

### Section 2:
- Constructing and analyzing temporal networks using Python
- **Coding Task:** Analyze the evolution of a social network over time by examining changes in connectivity and community structure
- **Natural Language Task:** Discuss how temporal network analysis can be used to study the dynamics of online social interactions
- Visualizing network evolution

---

## 12. Bipartite Networks and Recommendation Systems

### Section 1:
- Definition of bipartite networks and their properties
- Projecting bipartite networks into unipartite networks
- Applications to recommendation systems

### Section 2:
- Constructing and analyzing bipartite networks using Python
- **Coding Task:** Build a recommendation system based on a user-item bipartite network
- **Natural Language Task:** Explain how bipartite networks can be used to model user preferences and product recommendations
- Visualizing bipartite networks and their projections

---

## 13. Network Visualization and Interpretation

### Section 1:
- Advanced network visualization techniques using Gephi
- Layout algorithms: force-directed layouts, circular layouts, etc.
- Customizing node and edge attributes for visualization

### Section 2:
- Using Gephi to visualize and explore complex networks
- **Coding Task:** Import a network into Gephi and create a presentation-quality visualization
- **Natural Language Task:** Discuss how network visualization can aid in interpreting network structure and properties
- Interpreting network visualizations

---

## 14. Advanced Topics and Case Studies

### Section 1:
- Graph Neural Networks: Concepts, Architectures, and Applications
- Representation Learning on Graphs: Node Embeddings and Deep Learning Techniques
- Applications of network analysis in various domains: social sciences, biology, technology

### Section 2:
- **Coding Task:** Apply network analysis techniques to a real-world dataset and present the findings
- **Natural Language Task:** Discuss ethical considerations in network analysis
- Review of key concepts and future directions
- Implementing Representation Learning on Graphs