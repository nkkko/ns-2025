Project Path: notebooks

Source Tree:

```
notebooks
├── 05-casestudies
│   ├── images
│   │   ├── got.png
│   │   └── pagerank.png
│   ├── 02-airport.ipynb
│   └── 01-gameofthrones.ipynb
├── css
│   ├── nb_mods.css
│   └── apidocs.css
├── 00-preface
│   ├── 02-prereqs.ipynb
│   ├── 03-goals.md
│   ├── 01-setup.md
│   └── preface.md
├── devdocs
│   └── style.md
├── 02-algorithms
│   ├── 02-paths.ipynb
│   ├── 01-hubs.ipynb
│   └── 03-structures.ipynb
├── 01-introduction
│   ├── 01-graphs.ipynb
│   ├── 02-networkx-intro.ipynb
│   └── 03-viz.ipynb
├── 04-advanced
│   ├── 02-linalg.ipynb
│   ├── 03-stats.ipynb
│   ├── 01-bipartite.ipynb
│   └── figures
│       └── bipartite-projection.svg
├── index.md
├── 03-practical
│   ├── 01-io.ipynb
│   └── 02-testing.ipynb
└── learn-more.md

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/05-casestudies/02-airport.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import networkx as nx\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import warnings\n",
    "\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction\n",
    "\n",
    "In this chapter, we will analyse the evolution of US Airport Network between 1990 and 2015. This dataset contains data for 25 years[1995-2015] of flights between various US airports and metadata about these routes. Taken from Bureau of Transportation Statistics, United States Department of Transportation.\n",
    "\n",
    "Let's see what can we make out of this!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "\n",
    "pass_air_data = cf.load_airports_data()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the `pass_air_data` dataframe we have the information of number of people that fly every year on a particular route on the list of airlines that fly that route."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pass_air_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Every row in this dataset is a unique route between 2 airports in United States territory in a particular year. Let's see how many people flew from New York JFK to Austin in 2006.\n",
    "\n",
    "NOTE: This will be a fun chapter if you are an aviation geek and like guessing airport IATA codes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "jfk_aus_2006 = pass_air_data.query(\"YEAR == 2006\").query(\n",
    "    \"ORIGIN == 'JFK' and DEST == 'AUS'\"\n",
    ")\n",
    "\n",
    "jfk_aus_2006.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the above pandas query we see that according to this dataset 105290 passengers travelled from JFK to AUS in the year 2006.\n",
    "\n",
    "But how does this dataset translate to an applied network analysis problem? In the previous chapter we created different graph objects for every book. Let's create a graph object which encompasses all the edges.\n",
    "\n",
    "NetworkX provides us with Multi(Di)Graphs to model networks with multiple edges between two nodes.\n",
    "\n",
    "In this case every row in the dataframe represents a directed edge between two airports, common sense suggests that if there is a flight from airport A to airport B there should definitely be a flight from airport B to airport A, i.e direction of the edge shouldn't matter. But in this dataset we have data for individual directions (A -> B and B -> A) so we create a MultiDiGraph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "passenger_graph = nx.from_pandas_edgelist(\n",
    "    pass_air_data,\n",
    "    source=\"ORIGIN\",\n",
    "    target=\"DEST\",\n",
    "    edge_key=\"YEAR\",\n",
    "    edge_attr=[\"PASSENGERS\", \"UNIQUE_CARRIER_NAME\"],\n",
    "    create_using=nx.MultiDiGraph(),\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have created a MultiDiGraph object `passenger_graph` which contains all the information from the dataframe `pass_air_data`. `ORIGIN` and `DEST` represent the column names in the dataframe `pass_air_data` used to construct the edge. As this is a `MultiDiGraph` we can also give a name/key to the multiple edges between two nodes and `edge_key` is used to represent that name and in this graph `YEAR` is used to distinguish between multiple edges between two nodes. `PASSENGERS` and `UNIQUE_CARRIER_NAME` are added as edge attributes which can be accessed using the nodes and the key form the MultiDiGraph object.\n",
    "\n",
    "Let's check if can access the same information (the 2006 route between JFK and AUS) using our `passenger_graph`.\n",
    "\n",
    "To check an edge between two nodes in a Graph we can use the syntax `GraphObject[source][target]` and further specify the edge attribute using `GraphObject[source][target][attribute]`.\n",
    "\n",
    "<!-- Let's see if `passenger_graph['JFK']['AUS'][2006]` works. -->"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "passenger_graph[\"JFK\"][\"AUS\"][2006]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's use our new constructed passenger graph to look at the evolution of passenger load over 25 years."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Route betweeen New York-JFK and SFO\n",
    "\n",
    "values = [\n",
    "    (year, attr[\"PASSENGERS\"]) for year, attr in passenger_graph[\"JFK\"][\"SFO\"].items()\n",
    "]\n",
    "x, y = zip(*values)\n",
    "plt.plot(x, y)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see some usual trends all across the datasets like steep drops in 2001 (after 9/11) and 2008 (recession)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Route betweeen SFO and Chicago-ORD\n",
    "\n",
    "values = [\n",
    "    (year, attr[\"PASSENGERS\"]) for year, attr in passenger_graph[\"SFO\"][\"ORD\"].items()\n",
    "]\n",
    "x, y = zip(*values)\n",
    "plt.plot(x, y)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To find the overall trend, we can use our `pass_air_data` dataframe to calculate total passengers flown in a year."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pass_air_data.groupby([\"YEAR\"]).sum()[\"PASSENGERS\"].plot()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise\n",
    "\n",
    "Find the busiest route in 1990 and in 2015 according to number of passengers, and plot the time series of number of passengers on these routes.\n",
    "\n",
    "You can use the DataFrame instead of working with the network. It will be faster :)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.airport import busiest_route, plot_time_series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "busiest_route(pass_air_data, 1990).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plot_time_series(pass_air_data, \"LAX\", \"HNL\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "busiest_route(pass_air_data, 2015).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plot_time_series(pass_air_data, \"LAX\", \"SFO\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Before moving to the next part of the chapter let's create a method to extract edges from `passenger_graph` for a particular year so we can better analyse the data on a granular scale."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def year_network(G, year):\n",
    "    \"\"\"Extract edges for a particular year from\n",
    "    a MultiGraph. The edge is also populated with\n",
    "    two attributes, weight and weight_inv where\n",
    "    weight is the number of passengers and\n",
    "    weight_inv the inverse of it.\n",
    "    \"\"\"\n",
    "    year_network = nx.DiGraph()\n",
    "    for edge in G.edges:\n",
    "        source, target, edge_year = edge\n",
    "        if edge_year == year:\n",
    "            attr = G[source][target][edge_year]\n",
    "            year_network.add_edge(\n",
    "                source,\n",
    "                target,\n",
    "                weight=attr[\"PASSENGERS\"],\n",
    "                weight_inv=1 / (attr[\"PASSENGERS\"] if attr[\"PASSENGERS\"] != 0.0 else 1),\n",
    "                airlines=attr[\"UNIQUE_CARRIER_NAME\"],\n",
    "            )\n",
    "    return year_network"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pass_2015_network = year_network(passenger_graph, 2015)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Extracted a Directed Graph from the Multi Directed Graph\n",
    "# Number of nodes = airports\n",
    "# Number of edges = routes\n",
    "\n",
    "print(pass_2015_network)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualise the airports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Loadin the GPS coordinates of all the airports\n",
    "from nams import load_data as cf\n",
    "\n",
    "lat_long = cf.load_airports_GPS_data()\n",
    "lat_long.columns = [\n",
    "    \"CODE4\",\n",
    "    \"CODE3\",\n",
    "    \"CITY\",\n",
    "    \"PROVINCE\",\n",
    "    \"COUNTRY\",\n",
    "    \"UNKNOWN1\",\n",
    "    \"UNKNOWN2\",\n",
    "    \"UNKNOWN3\",\n",
    "    \"UNKNOWN4\",\n",
    "    \"UNKNOWN5\",\n",
    "    \"UNKNOWN6\",\n",
    "    \"UNKNOWN7\",\n",
    "    \"UNKNOWN8\",\n",
    "    \"UNKNOWN9\",\n",
    "    \"LATITUDE\",\n",
    "    \"LONGITUDE\",\n",
    "]\n",
    "lat_long\n",
    "wanted_nodes = list(pass_2015_network.nodes())\n",
    "us_airports = (\n",
    "    lat_long.query(\"CODE3 in @wanted_nodes\")\n",
    "    .drop_duplicates(subset=[\"CODE3\"])\n",
    "    .set_index(\"CODE3\")\n",
    ")\n",
    "us_airports.head()\n",
    "# us_airports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Annotate graph with latitude and longitude\n",
    "no_gps = []\n",
    "for n, d in pass_2015_network.nodes(data=True):\n",
    "    try:\n",
    "        pass_2015_network.nodes[n][\"longitude\"] = us_airports.loc[n, \"LONGITUDE\"]\n",
    "        pass_2015_network.nodes[n][\"latitude\"] = us_airports.loc[n, \"LATITUDE\"]\n",
    "        pass_2015_network.nodes[n][\"degree\"] = pass_2015_network.degree(n)\n",
    "\n",
    "    # Some of the nodes are not represented\n",
    "    except KeyError:\n",
    "        no_gps.append(n)\n",
    "\n",
    "# Get subgraph of nodes that do have GPS coords\n",
    "has_gps = set(pass_2015_network.nodes()).difference(no_gps)\n",
    "g = pass_2015_network.subgraph(has_gps)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's first plot only the nodes, i.e airports. Places like Guam, US Virgin Islands are also included in this dataset as they are treated as domestic airports in this dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "from nxviz import nodes, plots, edges\n",
    "\n",
    "plt.figure(figsize=(20, 9))\n",
    "pos = nodes.geo(g, encodings_kwargs={\"size_scale\": 1})\n",
    "plots.aspect_equal()\n",
    "plots.despine()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's also plot the routes(edges)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "from nxviz import nodes, plots, edges, annotate\n",
    "\n",
    "plt.figure(figsize=(20, 9))\n",
    "pos = nodes.geo(g, color_by=\"degree\", encodings_kwargs={\"size_scale\": 1})\n",
    "edges.line(g, pos, encodings_kwargs={\"alpha_scale\": 0.1})\n",
    "annotate.node_colormapping(g, color_by=\"degree\")\n",
    "plots.aspect_equal()\n",
    "plots.despine()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Before we proceed further, let's take a detour to briefly discuss directed networks and PageRank."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Directed Graphs and PageRank\n",
    "\n",
    "The figure below explains the basic idea behind the PageRank algorithm. The \"importance\" of the node depends on the incoming links to the node, i.e if an \"important\" node A points towards a node B it will increase the PageRank score of node B, and this is run iteratively. In the given figure, even though node C is only connected to one node it is considered \"important\" as the connection is to node B, which is an \"important\" node.\n",
    "\n",
    "![](images/pagerank.png)\n",
    "<!-- <img src='images/pagerank.png' alt='pagerank' width='500'/> -->\n",
    "\n",
    "Source: Wikipedia\n",
    "\n",
    "To better understand this let's work through an example."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Create an empty directed graph object\n",
    "G = nx.DiGraph()\n",
    "# Add an edge from 1 to 2 with weight 4\n",
    "G.add_edge(1, 2, weight=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "print(G.edges(data=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Access edge from 1 to 2\n",
    "G[1][2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What happens when we try to access the edge from 2 to 1?\n",
    "\n",
    "``` python\n",
    "G[2][1]\n",
    "\n",
    "---------------------------------------------------------------------------\n",
    "KeyError                                  Traceback (most recent call last)\n",
    "<ipython-input-137-d6b8db3142ef> in <module>\n",
    "      1 # Access edge from 2 to 1\n",
    "----> 2 G[2][1]\n",
    "\n",
    "~/miniconda3/envs/nams/lib/python3.7/site-packages/networkx/classes/coreviews.py in __getitem__(self, key)\n",
    "     52 \n",
    "     53     def __getitem__(self, key):\n",
    "---> 54         return self._atlas[key]\n",
    "     55 \n",
    "     56     def copy(self):\n",
    "\n",
    "KeyError: 1\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As expected we get an error when we try to access the edge between 2 to 1 as this is a directed graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "G.add_edges_from([(1, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)])\n",
    "nx.draw_circular(G, with_labels=True)\n",
    "\n",
    "# nv.circos(G, node_enc_kwargs={\"size_scale\": 0.3})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Just by looking at the example above, we can conclude that node 2 should have the highest PageRank score as all the nodes are pointing towards it.\n",
    "\n",
    "This is confirmed by calculating the PageRank of this graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.pagerank(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What happens when we add an edge from node 5 to node 6."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "G.add_edge(5, 6)\n",
    "# nv.circos(G, node_enc_kwargs={\"size_scale\": 0.3})\n",
    "nx.draw_circular(G, with_labels=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.pagerank(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As expected there was some change in the scores (an increase for 6) but the overall trend stays the same, with node 2 leading the pack."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "G.add_edge(2, 8)\n",
    "nx.draw_circular(G, with_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we have an added an edge from 2 to a new node 8. As node 2 already has a high PageRank score, this should be passed on node 8. Let's see how much difference this can make."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.pagerank(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this example, node 8 is now even more \"important\" than node 2 even though node 8 has only incoming connection.\n",
    "\n",
    "Let's move back to Airports and use this knowledge to analyse the network."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importants Hubs in the Airport Network\n",
    "\n",
    "So let's have a look at the important nodes in this network, i.e. important airports in this network. We'll use centrality measures like pagerank, betweenness centrality and degree centrality which we gone through in this book."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's try to calculate the PageRank of `passenger_graph`.\n",
    "\n",
    "``` python\n",
    "nx.pagerank(passenger_graph)\n",
    "\n",
    "---------------------------------------------------------------------------\n",
    "NetworkXNotImplemented                    Traceback (most recent call last)\n",
    "<ipython-input-144-15a6f513bf9b> in <module>\n",
    "      1 # Let's try to calulate the PageRank measures of this graph.\n",
    "----> 2 nx.pagerank(passenger_graph)\n",
    "\n",
    "<decorator-gen-435> in pagerank(G, alpha, personalization, max_iter, tol, nstart, weight, dangling)\n",
    "\n",
    "~/miniconda3/envs/nams/lib/python3.7/site-packages/networkx/utils/decorators.py in _not_implemented_for(not_implement_for_func, *args, **kwargs)\n",
    "     78         if match:\n",
    "     79             msg = 'not implemented for %s type' % ' '.join(graph_types)\n",
    "---> 80             raise nx.NetworkXNotImplemented(msg)\n",
    "     81         else:\n",
    "     82             return not_implement_for_func(*args, **kwargs)\n",
    "\n",
    "NetworkXNotImplemented: not implemented for multigraph type\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As PageRank isn't defined for a MultiGraph in NetworkX we need to use our extracted yearly sub networks."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# As pagerank will take weighted measure\n",
    "# by default we pass in None to make this\n",
    "# calculation for unweighted network\n",
    "PR_2015_scores = nx.pagerank(pass_2015_network, weight=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Let's check the PageRank score for JFK\n",
    "PR_2015_scores[\"JFK\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# top 10 airports according to unweighted PageRank\n",
    "top_10_pr = sorted(PR_2015_scores.items(), key=lambda x: x[1], reverse=True)[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# top 10 airports according to unweighted betweenness centrality\n",
    "top_10_bc = sorted(\n",
    "    nx.betweenness_centrality(pass_2015_network, weight=None).items(),\n",
    "    key=lambda x: x[1],\n",
    "    reverse=True,\n",
    ")[0:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# top 10 airports according to degree centrality\n",
    "top_10_dc = sorted(\n",
    "    nx.degree_centrality(pass_2015_network).items(), key=lambda x: x[1], reverse=True\n",
    ")[0:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Before looking at the results do think about what we just calculated and try to guess which airports should come out at the top and be ready to be surprised :D"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# PageRank\n",
    "top_10_pr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Betweenness Centrality\n",
    "top_10_bc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Degree Centrality\n",
    "top_10_dc"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Degree Centrality results do make sense at first glance, ATL is Atlanta, ORD is Chicago, these are defintely airports one would expect to be at the top of a list which calculates \"importance\" of an airport. But when we look at PageRank and Betweenness Centrality we have an unexpected airport 'ANC'. Do think about measures like PageRank and Betweenness Centrality and what they calculate. Do note that currently we have used the core structure of the network, no other metadata like number of passengers. These are calculations on the unweighted network.\n",
    "\n",
    "'ANC' is the airport code of Anchorage airport, a place in Alaska, and according to pagerank and betweenness centrality it is the most important airport in this network. Isn't that weird? Thoughts?\n",
    "\n",
    "Looks like 'ANC' is essential to the core structure of the network, as it is the main airport connecting Alaska with other parts of US. This explains the high Betweenness Centrality score and there are flights from other major airports to 'ANC' which explains the high PageRank score.\n",
    "\n",
    "Related blog post: https://toreopsahl.com/2011/08/12/why-anchorage-is-not-that-important-binary-ties-and-sample-selection/\n",
    "\n",
    "Let's look at weighted version, i.e taking into account the number of people flying to these places."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Recall from the last chapter we use weight_inv\n",
    "# while calculating betweenness centrality\n",
    "sorted(\n",
    "    nx.betweenness_centrality(pass_2015_network, weight=\"weight_inv\").items(),\n",
    "    key=lambda x: x[1],\n",
    "    reverse=True,\n",
    ")[0:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "sorted(\n",
    "    nx.pagerank(pass_2015_network, weight=\"weight\").items(),\n",
    "    key=lambda x: x[1],\n",
    "    reverse=True,\n",
    ")[0:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When we adjust for number of passengers we see that we have a reshuffle in the \"importance\" rankings, and they do make a bit more sense now. According to weighted PageRank, Atlanta, Chicago, Seattle the top 3 airports while Anchorage is at 4th rank now.\n",
    "\n",
    "To get an even better picture of this we should do the analyse with more metadata about the routes not just the number of passengers."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How reachable is this network?\n",
    "\n",
    "Let's assume you are the Head of Data Science of an airline and your job is to make your airline network as \"connected\" as possible.\n",
    "\n",
    "To translate this problem statement to network science, we calculate the average shortest path length of this network, it gives us an idea about the number of jumps we need to make around the network to go from one airport to any other airport in this network on average."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use the inbuilt networkx method `average_shortest_path_length` to find the average shortest path length of a network.\n",
    "\n",
    "```python\n",
    "nx.average_shortest_path_length(pass_2015_network)\n",
    "\n",
    "---------------------------------------------------------------------------\n",
    "NetworkXError                             Traceback (most recent call last)\n",
    "<ipython-input-157-acfe9bf3572a> in <module>\n",
    "----> 1 nx.average_shortest_path_length(pass_2015_network)\n",
    "\n",
    "~/miniconda3/envs/nams/lib/python3.7/site-packages/networkx/algorithms/shortest_paths/generic.py in average_shortest_path_length(G, weight, method)\n",
    "    401     # Shortest path length is undefined if the graph is disconnected.\n",
    "    402     if G.is_directed() and not nx.is_weakly_connected(G):\n",
    "--> 403         raise nx.NetworkXError(\"Graph is not weakly connected.\")\n",
    "    404     if not G.is_directed() and not nx.is_connected(G):\n",
    "    405         raise nx.NetworkXError(\"Graph is not connected.\")\n",
    "\n",
    "NetworkXError: Graph is not weakly connected.\n",
    "    \n",
    "```\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Wait, What? This network is not \"connected\" (ignore the term weakly for the moment).\n",
    "That seems weird. It means that there are nodes which aren't reachable from other set of nodes, which isn't good news in especially a transporation network.\n",
    "\n",
    "Let's have a look at these far flung airports which aren't reachable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "components = list(nx.weakly_connected_components(pass_2015_network))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# There are 3 weakly connected components in the network.\n",
    "for c in components:\n",
    "    print(len(c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Let's look at the component with 2 and 1 airports respectively.\n",
    "print(components[1])\n",
    "print(components[2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The airports `SSB` and `SPB` are codes for Seaplanes airports and they have flights to each other so it makes sense that they aren't connected to the larger network of airports.\n",
    "\n",
    "The airport is even more weird as it is in a component in itself, i.e there is a flight from `AIK` to `AIK`. After investigating further it just seems like an anomaly in this dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "AIK_DEST_2015 = pass_air_data[\n",
    "    (pass_air_data[\"YEAR\"] == 2015) & (pass_air_data[\"DEST\"] == \"AIK\")\n",
    "]\n",
    "AIK_DEST_2015.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Let's get rid of them, we don't like them\n",
    "pass_2015_network.remove_nodes_from([\"SPB\", \"SSB\", \"AIK\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Our network is now weakly connected\n",
    "nx.is_weakly_connected(pass_2015_network)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# It's not strongly connected\n",
    "nx.is_strongly_connected(pass_2015_network)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Strongly vs weakly connected graphs.\n",
    "\n",
    "Let's go through an example to understand weakly and strongly connected directed graphs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# NOTE: The notion of strongly and weakly exists only for directed graphs.\n",
    "G = nx.DiGraph()\n",
    "\n",
    "# Let's create a cycle directed graph, 1 -> 2 -> 3 -> 1\n",
    "G.add_edge(1, 2)\n",
    "G.add_edge(2, 3)\n",
    "G.add_edge(3, 1)\n",
    "nx.draw(G, with_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the above example we can reach any node irrespective of where we start traversing the network, if we start from 2 we can reach 1 via 3. In this network every node is \"reachable\" from one another, i.e the network is strongly connected."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.is_strongly_connected(G)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Let's add a new connection\n",
    "G.add_edge(3, 4)\n",
    "nx.draw(G, with_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's evident from the example above that we *can't* traverse the network graph. If we start from node 4 we are stuck at the node, we don't have any way of leaving node 4. This is assuming we strictly follow the direction of edges. In this case the network isn't strongly connected but if we look at the structure and assume the directions of edges don't matter than we can go to any other node in the network even if we start from node 4.\n",
    "\n",
    "In the case an undirected copy of directed network is connected we call the directed network as weakly connected."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.is_strongly_connected(G)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.is_weakly_connected(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's go back to our airport network of 2015.\n",
    "\n",
    "After removing those 3 airports the network is weakly connected."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.is_weakly_connected(pass_2015_network)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.is_strongly_connected(pass_2015_network)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "But our network is still not strongly connected, which essentially means there are airports in the network where you can fly into but not fly back, which doesn't really seem okay"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "strongly_connected_components = list(\n",
    "    nx.strongly_connected_components(pass_2015_network)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Let's look at one of the examples of a strong connected component\n",
    "strongly_connected_components[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "bce_2015 = pass_air_data.query(\"YEAR == 2015\").query(\"ORIGIN == 'BCE' or DEST == 'BCE'\")\n",
    "bce_2015"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we can see above you can fly into `BCE` but can't fly out, weird indeed. These airport are small airports with one off schedules flights. For the purposes of our analyses we can ignore such airports."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Let's find the biggest strongly connected component\n",
    "pass_2015_strong_nodes = max(strongly_connected_components, key=len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Create a subgraph with the nodes in the\n",
    "# biggest strongly connected component\n",
    "pass_2015_strong = pass_2015_network.subgraph(nodes=pass_2015_strong_nodes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.is_strongly_connected(pass_2015_strong)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After removing multiple airports we now have a strongly connected airport network. We can now travel from one airport to any other airport in the network."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# We started with 1258 airports\n",
    "len(pass_2015_strong)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.average_shortest_path_length(pass_2015_strong)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The 3.17 number above represents the average length between 2 airports in the network which means that it's possible to go from one airport to another in this network under 3 layovers, which sounds nice. A more reachable network is better, not necessearily in terms of revenue for the airline but for social health of the air transport network."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise\n",
    "\n",
    "How can we decrease the average shortest path length of this network?\n",
    "\n",
    "Think of an effective way to add new edges to decrease the average shortest path length.\n",
    "Let's see if we can come up with a nice way to do this.\n",
    "\n",
    "The rules are simple:\n",
    "- You can't add more than 2% of the current edges( ~500 edges)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.airport import add_opinated_edges"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "new_routes_network = add_opinated_edges(pass_2015_strong)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.average_shortest_path_length(new_routes_network)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using an opinionated heuristic we were able to reduce the average shortest path length of the network. Check the solution below to understand the idea behind the heuristic, do try to come up with your own heuristics."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Can we find airline specific reachability?\n",
    "\n",
    "Let's see how we can use the airline metadata to calculate the reachability of a specific airline."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# We have access to the airlines that fly the route in the edge attribute airlines\n",
    "pass_2015_network[\"JFK\"][\"SFO\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# A helper function to extract the airlines names from the edge attribute\n",
    "def str_to_list(a):\n",
    "    return a[1:-1].split(\", \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for origin, dest in pass_2015_network.edges():\n",
    "    pass_2015_network[origin][dest][\"airlines_list\"] = str_to_list(\n",
    "        (pass_2015_network[origin][dest][\"airlines\"])\n",
    "    )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's extract the network of United Airlines from our airport network."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "united_network = nx.DiGraph()\n",
    "for origin, dest in pass_2015_network.edges():\n",
    "    if \"'United Air Lines Inc.'\" in pass_2015_network[origin][dest][\"airlines_list\"]:\n",
    "        united_network.add_edge(\n",
    "            origin, dest, weight=pass_2015_network[origin][dest][\"weight\"]\n",
    "        )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# number of nodes -> airports\n",
    "# number of edges -> routes\n",
    "print(united_network)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's find United Hubs according to PageRank\n",
    "sorted(\n",
    "    nx.pagerank(united_network, weight=\"weight\").items(),\n",
    "    key=lambda x: x[1],\n",
    "    reverse=True,\n",
    ")[0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's find United Hubs according to Degree Centrality\n",
    "sorted(nx.degree_centrality(united_network).items(), key=lambda x: x[1], reverse=True)[\n",
    "    0:5\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solutions\n",
    "\n",
    "Here are the solutions to the exercises above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions import airport\n",
    "import inspect\n",
    "\n",
    "print(inspect.getsource(airport))"
   ]
  }
 ],
 "metadata": {
  "jupytext": {
   "notebook_metadata_filter": "all"
  },
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/05-casestudies/01-gameofthrones.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import pandas as pd\n",
    "import networkx as nx\n",
    "import community\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction\n",
    "\n",
    "In this chapter, we will use Game of Thrones as a case study to practice our newly learnt skills of network analysis.\n",
    "\n",
    "It is suprising right? What is the relationship between a fatansy TV show/novel and network science or Python(not dragons).\n",
    "\n",
    "If you haven't heard of Game of Thrones, then you must be really good at hiding. Game of Thrones is a hugely popular television series by HBO based on the (also) hugely popular book series A Song of Ice and Fire by George R.R. Martin. In this notebook, we will analyze the co-occurrence network of the characters in the Game of Thrones books. Here, two characters are considered to co-occur if their names appear in the vicinity of 15 words from one another in the books.\n",
    "\n",
    "The figure below is a precusor of what we will analyse in this chapter.\n",
    "\n",
    "![](images/got.png)\n",
    "\n",
    "\n",
    "The dataset is publicly avaiable for the 5 books at https://github.com/mathbeveridge/asoiaf. This is an interaction network and were created by connecting two characters whenever their names (or nicknames) appeared within 15 words of one another in one of the books. The edge weight corresponds to the number of interactions. \n",
    "\n",
    "\n",
    "Blog: https://networkofthrones.wordpress.com"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "\n",
    "books = cf.load_game_of_thrones_data()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The resulting DataFrame books has 5 columns: Source, Target, Type, weight, and book. Source and target are the two nodes that are linked by an edge. As we know a network can have directed or undirected edges and in this network all the edges are undirected. The weight attribute of every edge tells us the number of interactions that the characters have had over the book, and the book column tells us the book number.\n",
    "\n",
    "Let's have a look at the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We also add this weight_inv to our dataset.\n",
    "# Why? we will discuss it in a later section.\n",
    "books[\"weight_inv\"] = 1 / books.weight"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the above data we can see that the characters Addam Marbrand and Tywin Lannister have interacted 6 times in the first book.\n",
    "\n",
    "We can investigate this data by using the pandas DataFrame. Let's find all the interactions of Robb Stark in the third book."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "robbstark = books.query(\"book == 3\").query(\n",
    "    \"Source == 'Robb-Stark' or Target == 'Robb-Stark'\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "robbstark.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see this data easily translates to a network problem. Now it's time to create a network.\n",
    "We create a graph for each book. It's possible to create one `MultiGraph`(Graph with multiple edges between nodes) instead of 5 graphs, but it is easier to analyse and manipulate individual `Graph` objects rather than a `MultiGraph`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# example of creating a MultiGraph\n",
    "\n",
    "# all_books_multigraph = nx.from_pandas_edgelist(\n",
    "#            books, source='Source', target='Target',\n",
    "#            edge_attr=['weight', 'book'],\n",
    "#            create_using=nx.MultiGraph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# we create a list of graph objects using\n",
    "# nx.from_pandas_edgelist and specifying\n",
    "# the edge attributes.\n",
    "\n",
    "graphs = [\n",
    "    nx.from_pandas_edgelist(\n",
    "        books[books.book == i],\n",
    "        source=\"Source\",\n",
    "        target=\"Target\",\n",
    "        edge_attr=[\"weight\", \"weight_inv\"],\n",
    "    )\n",
    "    for i in range(1, 6)\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The Graph object associated with the first book.\n",
    "graphs[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# To access the relationship edges in the graph with\n",
    "# the edge attribute weight data (data=True)\n",
    "relationships = list(graphs[0].edges(data=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "relationships[0:3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Finding the most important node i.e character in these networks.\n",
    "\n",
    "Let's use our network analysis knowledge to decrypt these Graphs that we have just created.\n",
    "\n",
    "Is it Jon Snow, Tyrion, Daenerys, or someone else? Let's see! Network Science offers us many different metrics to measure the importance of a node in a network as we saw in the first part of the tutorial. Note that there is no \"correct\" way of calculating the most important node in a network, every metric has a different meaning.\n",
    "\n",
    "First, let's measure the importance of a node in a network by looking at the number of neighbors it has, that is, the number of nodes it is connected to. For example, an influential account on Twitter, where the follower-followee relationship forms the network, is an account which has a high number of followers. This measure of importance is called degree centrality.\n",
    "\n",
    "Using this measure, let's extract the top ten important characters from the first book (`graphs[0]`) and the fifth book (`graphs[4]`).\n",
    "\n",
    "NOTE: We are using zero-indexing and that's why the graph of the first book is acceseed by `graphs[0]`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We use the in-built degree_centrality method\n",
    "deg_cen_book1 = nx.degree_centrality(graphs[0])\n",
    "deg_cen_book5 = nx.degree_centrality(graphs[4])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`degree_centrality` returns a dictionary and to access the results we can directly use the name of the character."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "deg_cen_book1[\"Daenerys-Targaryen\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Top 5 important characters in the first book according to degree centrality."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The following expression sorts the dictionary by\n",
    "# degree centrality and returns the top 5 from a graph\n",
    "\n",
    "sorted(deg_cen_book1.items(), key=lambda x: x[1], reverse=True)[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Top 5 important characters in the fifth book according to degree centrality."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sorted(deg_cen_book5.items(), key=lambda x: x[1], reverse=True)[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To visualize the distribution of degree centrality let's plot a histogram of degree centrality."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.hist(deg_cen_book1.values(), bins=30)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The above plot shows something that is expected, a high portion of characters aren't connected to lot of other characters while some characters are highly connected all through the network. A close real world example of this is a social network like Twitter where a few people have millions of connections(followers) but majority of users aren't connected to that many other users. This exponential decay like property resembles power law in real life networks."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A log-log plot to show the \"signature\" of power law in graphs.\n",
    "from collections import Counter\n",
    "\n",
    "hist = Counter(deg_cen_book1.values())\n",
    "plt.scatter(np.log2(list(hist.keys())), np.log2(list(hist.values())), alpha=0.9)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise\n",
    "\n",
    "Create a new centrality measure, weighted_degree(Graph, weight) which takes in Graph and the weight attribute and returns a weighted degree dictionary. Weighted degree is calculated by summing the weight of the all edges of a node and find the top five characters according to this measure."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.got import weighted_degree\n",
    "\n",
    "plt.hist(list(weighted_degree(graphs[0], \"weight\").values()), bins=30)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sorted(weighted_degree(graphs[0], \"weight\").items(), key=lambda x: x[1], reverse=True)[\n",
    "    0:5\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Betweeness centrality\n",
    "\n",
    "Let's do this for Betweeness centrality and check if this makes any difference. As different centrality method use different measures underneath, they find nodes which are important in the network. A centrality method like Betweeness centrality finds nodes which are structurally important to the network, which binds the network together and densely."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# First check unweighted (just the structure)\n",
    "\n",
    "sorted(nx.betweenness_centrality(graphs[0]).items(), key=lambda x: x[1], reverse=True)[\n",
    "    0:10\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's care about interactions now\n",
    "\n",
    "sorted(\n",
    "    nx.betweenness_centrality(graphs[0], weight=\"weight_inv\").items(),\n",
    "    key=lambda x: x[1],\n",
    "    reverse=True,\n",
    ")[0:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see there are some differences between the unweighted and weighted centrality measures. Another thing to note is that we are using the weight_inv attribute instead of weight(the number of interactions between characters). This decision is based on the way we want to assign the notion of \"importance\" of a character. The basic idea behind betweenness centrality is to find nodes which are essential to the structure of the network. As betweenness centrality computes shortest paths underneath, in the case of weighted betweenness centrality it will end up penalising characters with high number of interactions. By using weight_inv we will prop up the characters with high interactions with other characters."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PageRank\n",
    "The billion dollar algorithm, PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites.\n",
    "\n",
    "NOTE: We don't need to worry about weight and weight_inv in PageRank as the algorithm uses weights in the opposite sense (larger weights are better). This may seem confusing as different centrality measures have different definition of weights. So it is always better to have a look at documentation before using weights in a centrality measure."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# by default weight attribute in PageRank is weight\n",
    "# so we use weight=None to find the unweighted results\n",
    "sorted(nx.pagerank(graphs[0], weight=None).items(), key=lambda x: x[1], reverse=True)[\n",
    "    0:10\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sorted(\n",
    "    nx.pagerank(graphs[0], weight=\"weight\").items(), key=lambda x: x[1], reverse=True\n",
    ")[0:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise\n",
    "\n",
    "#### Is there a correlation between these techniques?\n",
    "\n",
    "\n",
    "Find the correlation between these four techniques.\n",
    "\n",
    "- pagerank (weight = 'weight')\n",
    "- betweenness_centrality (weight = 'weight_inv')\n",
    "- weighted_degree\n",
    "- degree centrality\n",
    "\n",
    "HINT: Use pandas correlation "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.got import correlation_centrality\n",
    "\n",
    "correlation_centrality(graphs[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Evolution of importance of characters over the books\n",
    "\n",
    "According to degree centrality the most important character in the first book is Eddard Stark but he is not even in the top 10 of the fifth book. The importance changes over the course of five books, because you know stuff happens ;)\n",
    "\n",
    "Let's look at the evolution of degree centrality of a couple of characters like Eddard Stark, Jon Snow, Tyrion which showed up in the top 10 of degree centrality in first book.\n",
    "\n",
    "We create a dataframe with character columns and index as books where every entry is the degree centrality of the character in that particular book and plot the evolution of degree centrality Eddard Stark, Jon Snow and Tyrion.\n",
    "We can see that the importance of Eddard Stark in the network dies off and with Jon Snow there is a drop in the fourth book but a sudden rise in the fifth book"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "evol = [nx.degree_centrality(graph) for graph in graphs]\n",
    "evol_df = pd.DataFrame.from_records(evol).fillna(0)\n",
    "evol_df[[\"Eddard-Stark\", \"Tyrion-Lannister\", \"Jon-Snow\"]].plot()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "set_of_char = set()\n",
    "for i in range(5):\n",
    "    set_of_char |= set(list(evol_df.T[i].sort_values(ascending=False)[0:5].index))\n",
    "set_of_char"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise\n",
    "\n",
    "Plot the evolution of betweenness centrality of the above mentioned characters over the 5 books."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.got import evol_betweenness"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "evol_betweenness(graphs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## So what's up with Stannis Baratheon?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sorted(nx.degree_centrality(graphs[4]).items(), key=lambda x: x[1], reverse=True)[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sorted(nx.betweenness_centrality(graphs[4]).items(), key=lambda x: x[1], reverse=True)[\n",
    "    :5\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nx.draw(nx.barbell_graph(5, 1), with_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we know the a higher betweenness centrality means that the node is crucial for the structure of the network, and in the case of Stannis Baratheon in the fifth book it seems like Stannis Baratheon has characterstics similar to that of node 5 in the above example as it seems to be the holding the network together.\n",
    "\n",
    "As evident from the betweenness centrality scores of the above example of barbell graph, node 5 is the most important node in this network."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nx.betweenness_centrality(nx.barbell_graph(5, 1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Community detection in Networks\n",
    "A network is said to have community structure if the nodes of the network can be easily grouped into (potentially overlapping) sets of nodes such that each set of nodes is densely connected internally. There are multiple algorithms and definitions to calculate these communites in a network.\n",
    "\n",
    "We will use louvain community detection algorithm to find the modules in our graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "from nxviz import annotate\n",
    "\n",
    "plt.figure(figsize=(8, 8))\n",
    "\n",
    "partition = community.best_partition(graphs[0], randomize=False)\n",
    "\n",
    "# Annotate nodes' partitions\n",
    "for n in graphs[0].nodes():\n",
    "    graphs[0].nodes[n][\"partition\"] = partition[n]\n",
    "    graphs[0].nodes[n][\"degree\"] = graphs[0].degree(n)\n",
    "\n",
    "nv.matrix(graphs[0], group_by=\"partition\", sort_by=\"degree\", node_color_by=\"partition\")\n",
    "annotate.matrix_block(graphs[0], group_by=\"partition\", color_by=\"partition\")\n",
    "annotate.matrix_group(graphs[0], group_by=\"partition\", offset=-8)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A common defining quality of a community is that\n",
    "the within-community edges are denser than the between-community edges."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# louvain community detection find us 8 different set of communities\n",
    "partition_dict = {}\n",
    "for character, par in partition.items():\n",
    "    if par in partition_dict:\n",
    "        partition_dict[par].append(character)\n",
    "    else:\n",
    "        partition_dict[par] = [character]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(partition_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "partition_dict[2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If we plot these communities of the network we see a denser network as compared to the original network which contains all the characters."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nx.draw(nx.subgraph(graphs[0], partition_dict[3]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nx.draw(nx.subgraph(graphs[0], partition_dict[1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can test this by calculating the density of the network and the community.\n",
    "\n",
    "Like in the following example the network between characters in a community is 5 times more dense than the original network."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.density(nx.subgraph(graphs[0], partition_dict[4])) / nx.density(graphs[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise \n",
    "\n",
    "Find the most important node in the partitions according to degree centrality of the nodes using the partition_dict we have already created."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.got import most_important_node_in_partition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "most_important_node_in_partition(graphs[0], partition_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solutions\n",
    "\n",
    "Here are the solutions to the exercises above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions import got\n",
    "import inspect\n",
    "\n",
    "print(inspect.getsource(got))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/css/nb_mods.css`:

```css
/*
Hide cell output overflow

Taken from: https://github.com/greenape/mknotebooks/issues/12
*/
.output pre {
    overflow: auto;
}


.output_html {
    overflow: auto;
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/css/apidocs.css`:

```css
div.doc-contents:not(.first) {
  padding-left: 25px;
  border-left: 4px solid rgba(230, 230, 230);
  margin-bottom: 80px;
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/00-preface/02-prereqs.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To get maximum benefit from this book, you should know how to program in Python.\n",
    "(Hint: it's an extremely useful skill to know!)\n",
    "In particular, knowing how to:\n",
    "\n",
    "1. use dictionaries,\n",
    "1. write list comprehensions, and\n",
    "1. handle `pandas` DataFrames,\n",
    "\n",
    "will help you a ton during the tutorial.\n",
    "\n",
    "## Exercises\n",
    "\n",
    "We have a few exercises below that should help you get warmed up."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise 1\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the following line of code:\n",
    "\n",
    "```python\n",
    "[s for s in my_fav_things if s[‘name’] == ‘raindrops on roses’]\n",
    "```\n",
    "\n",
    "What are plausible data structures for `s` and `my_fav_things`?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the following data:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "names = [\n",
    "    {\n",
    "        'name': 'Eric',\n",
    "         'surname': 'Ma'\n",
    "    },\n",
    "    {\n",
    "        'name': 'Jeffrey',\n",
    "        'surname': 'Elmer'\n",
    "    },\n",
    "    {\n",
    "        'name': 'Mike',\n",
    "        'surname': 'Lee'\n",
    "    },\n",
    "    {\n",
    "        'name': 'Jennifer',\n",
    "        'surname': 'Elmer'\n",
    "    }\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a function that takes in the `names` list of dictionaries\n",
    "and returns the dictionaries in which the `surname` value\n",
    "matches exactly some `query_surname`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_persons_with_surname(persons, query_surname):\n",
    "    # Assert that the persons parameter is a list. \n",
    "    # This is a good defensive programming practice.\n",
    "    assert isinstance(persons, list)   \n",
    "    \n",
    "    results = []\n",
    "    for ______ in ______:\n",
    "        if ___________ == __________:\n",
    "            results.append(________)\n",
    "    \n",
    "    return results"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To test your implementation, check it with the following code.\n",
    "No errors should be raised."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Test your result below.\n",
    "# results = find_persons_with_surname(names, 'Lee')\n",
    "# assert len(results) == 1\n",
    "\n",
    "# results = find_persons_with_surname(names, 'Elmer')\n",
    "# assert len(results) == 2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  },
  "toc": {
   "colors": {
    "hover_highlight": "#DAA520",
    "navigate_num": "#000000",
    "navigate_text": "#333333",
    "running_highlight": "#FF0000",
    "selected_highlight": "#FFD700",
    "sidebar_border": "#EEEEEE",
    "wrapper_background": "#FFFFFF"
   },
   "moveMenuLeft": true,
   "nav_menu": {
    "height": "30px",
    "width": "252px"
   },
   "navigate_menu": true,
   "number_sections": true,
   "sideBar": true,
   "threshold": 4,
   "toc_cell": false,
   "toc_section_display": "block",
   "toc_window_display": false,
   "widenNotebook": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/00-preface/03-goals.md`:

```md
Our learning goals for you with this book
can be split into the technical and the intellectual.

## Technical Takeaways

Firstly, we would like to equip you to be familiar
with the NetworkX application programming interface (API).
The reason for choosing NetworkX is because
it is extremely beginner-friendly,
and has an API that matches graph theory concepts very closely.

Secondly, we would like to show you how you can visualize graph data
in a fashion that doesn't involve showing mere hairballs.
Throughout the book, you will see examples of what we call
_rational graph visualizations_.
One of our authors, Eric Ma, has developed a companion package, `nxviz`,
that provides a declarative and convenient API
(in other words an attempt at a "grammar")
for graph visualization.

Thirdly, in this book, you will be introduced to basic graph algorithms,
such as finding special graph structures,
or finding paths in a graph.
Graph algorithms will show you how to "think on graphs",
and knowing how to do so will broaden your ability to interact with
graph data structures.

Fourthly, you will also be equipped with the connection between graph theory
and other areas of math and computing,
such as statistical inference and linear algebra.

## Intellectual Goals

Beyond the technical takeaways,
we hope to broaden how you think about data.

The first idea we hope to give you
the ability to think about your data
in terms of "relationships".
As you will learn,
relationships are what give rise to the interestingness of graphs.
That's where _relational insights_ can come to fore.

The second idea we hope to give you
is the ability to "think on graphs".
This comes with practice.
Once you master it, though,
you will find yourself becoming more and more familiar
with **algorithmic thinking**.
which is where you look at a problem
in terms of the **algorithm** that solves it.

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/00-preface/01-setup.md`:

```md
## Introduction

In order to get the most of this book,
you will want to be able to execute the examples in the notebooks,
modify them, break the code, and fix it.
Pedagogically, that is the best way for you to learn the concepts.
Here are the recommended ways in which you can get set up.

## Binder

We recommend the use of Binder!
This is because Binder will automagically setup
an isolated and ephemeral compute environment for you
with all of the packages needed to run the code in your notebooks.
As such, you won't have to wrestle with anything at the terminal.
To go there, click on the following button:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ericmjl/Network-Analysis-Made-Simple/master)

## VSCode Development Containers

Assuming that you're using Visual Studio Code
and have attempted to use development containers before,
you can run the Network Analysis Made Simple tutorial content
inside a development container.
After Binder, this is the second easiest way to get set up.
You need to have Docker installed on your computer
but don't worry -- you won't have to execute any Docker commands :).

### Install the Remote Containers extension

This is found in the Extensions marketplace.

![Remote Containers extension.](https://user-images.githubusercontent.com/2631566/164070556-7ca675bc-d700-4e1b-a8e4-f07bc77c79f8.png)

### Clone the repository to your local drive

```bash
git clone https://github.com/ericmjl/Network-Analysis-Made-Simple.git
```

### Open the repository in VSCode

Use `Cmd+Shift+P` (on macOS) or `Ctrl+Shift+P` (on Linux/Windows)
to open the command palette, and search for "Rebuild and Reopen in Container" as below:

![Search for "Rebuild and Reopen in Container"](https://user-images.githubusercontent.com/2631566/164071398-ff115bd0-02fc-4827-935a-2785a354360f.png)

Hit enter and wait for the container to build automagically. This may take around 10 minutes or so, depending on your system.

![Development container will be built.](https://user-images.githubusercontent.com/2631566/164071594-d3ddf3fa-9c78-48f3-be56-09a453f8eb0a.png)

## `conda` environments

We also recommend the use of `conda` environments!
Use this if you're not already using one of the options above.
If you are feeling confident enough to set up
a conda environment at the terminal,
then follow along.
(We'll be assuming you've already cloned the repository locally.)

### Leverage the Makefile

We've provided a Makefile with a single command:

```bash
make conda
```

On most \*nix systems, that should get you most of the way
to having the environment setup.

### Alternative: Execute individual commands

If you encounter errors, then you should know that the Makefile command
`make conda`
basically wraps the following steps.

Firstly, it creates the conda environment based on the `environment.yml` file:

```bash
conda env create -f environment.yml
```

Next, it activates the environment:

```bash
conda activate nams
```

We have a custom module for the project, which is called `nams`,
that you will have to install.

```bash
# In the root directory of the cloned repository
python setup.py develop
```

Finally, it runs a check on the environment
to make sure everything is installed correctly:

```bash
python checkenv.py
```

## `venv` environments

If you're not a `conda` user, then you can use `venv` to create your environment.


### Leverage the Makefile

As with the `conda` commands, you should be able
to execute a single Makefile command at your terminal:

```bash
make venv
```

Special heartfelt thanks goes out to GitHub user @matt-land
who contributed the `venv` script.

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/00-preface/preface.md`:

```md
Hey, thanks for picking up this e-Book.
We had a ton of fun making the material,
and we hope you have a ton of fun learning new things from it too.

Applied network analysis, and graph theory concepts,
are getting more and more relevant in our world.
Graph problems are abound.
Once you pick up how to use graphs in an applied setting,
you'll find your view of data problems change tremendously.
We hope this book can become part of your learning journey.

The act of purchasing this book means you've chosen to support us, the authors.
It means a ton to us, as this book is the culmination of 5 years
of learning and teaching applied network analysis
at conferences around the world.
The reason we went with LeanPub to publish this book is this:
For as long as we issue updates to the book,
you will also receive an updated copy of it.
And because the book is digital, it's easy for us to get updates out to you.

Just so you know, the full text of the book is available online too,
at the accompanying website, https://ericmjl.github.io/Network-Analysis-Made-Simple.
On there, you'll find a link to Binder so you can interact with the code,
and through the act of playing around with the code and breaking it yourself,
learn new things.
(Breaking code and fixing it is something you _should_ be doing -
it's one of the best ways to learn!)

If you have questions about the content,
or find an errata that you'd like to point out,
please head over to https://github.com/ericmjl/Network-Analysis-Made-Simple/,
and post an issue up there.
We'll be sure to address it and acknowledge it appropriately.

We hope that this book becomes a stepping stone in your learning journey.
Enjoy!

Eric & Mridul

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/devdocs/style.md`:

```md
This is the style guide for writing notebooks and markdown files for the book.

Intended as a guide when there is ambiguity in how to format something.
Updated it when new decisions are made for uncertain circumstances.

## Notebooks

### Headers

Jupyter notebook headers should begin at the 2nd level.
In other words:

```markdown
## Introdction (this is correct!)
```

should be the first header, and not:

```markdown
# Introdction (this is wrong!)
```

This allows `mkdocs` to insert the "Chapter X" heading
at the top of the compiled Markdown document.

### Exercises

Exercises should be at the 3rd level of headers.

For exercises that yield a plot, allow the exercise cell to be executed.

For exercises that modify an object that is used later, allow the exercise cell to be executed.

For exercises that are implementation-oriented, and do not affect notebook state,
it is recommended that the execution be commented out to save on execution time.

For exercises that require answering a question,
wrap the answer in a triple quote string,
use the `markdown` package to parse it into HTML,
and then use IPython's HTML display facility to show the answer
in beautiful HTML.
A convenience function called `render_html` is provided.
Here's an example:

```python
from nams.functions import render_html

def bipartite_degree_centrality_denominator():
    ans = """
Some answer goes here!
Written in **Markdown**.
"""
    return render_html(ans)
```

!!! warning "Indentation is super important!"
    Left indentation on the answer string cannot be present,
    otherwise the answer will not render correctly in HTML form!

### Solutions

Exercise solutions should be placed in the corresponding `nams.solutions.<notebook_name_without_extension>`
Python submodule.

Code solutions should always be present at the bottom of the notebook.

Use the following code block to help:

```python
import inspect
from nams.solutions import {{ notebook_name }}

print(inspect({{ notebook_name }}))
```

### Execution

Notebooks should run from top-to-bottom without erroring out.

Notebooks ideally should run in under 10 seconds.
However, if a notebook needs up to 30 seconds to finish execution,
that is acceptable.
No notebook should take on the order of minutes to finish.

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/02-algorithms/02-paths.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"JjpbztqP9_0\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Graph traversal is akin to walking along the graph, node by node,\n",
    "constrained by the edges that connect the nodes.\n",
    "Graph traversal is particularly useful for understanding \n",
    "the local structure of certain portions of the graph\n",
    "and for finding paths that connect two nodes in the network.\n",
    "\n",
    "In this chapter, we are going to learn how to perform pathfinding in a graph,\n",
    "specifically by looking for _shortest paths_ via the _breadth-first search_ algorithm."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Breadth-First Search\n",
    "\n",
    "The BFS algorithm is a staple of computer science curricula,\n",
    "and for good reason:\n",
    "it teaches learners how to \"think on\" a graph,\n",
    "putting one in the position of \n",
    "\"the dumb computer\" that can't use a visual cortex to \n",
    "\"_just know_\" how to trace a path from one node to another.\n",
    "As a topic, learning how to do BFS\n",
    "additionally imparts algorithmic thinking to the learner.\n",
    "\n",
    "### Exercise: Design the algorithm\n",
    "\n",
    "Try out this exercise to get some practice with algorithmic thinking.\n",
    "\n",
    "> 1. On a piece of paper, conjure up a graph that has 15-20 nodes. Connect them any way you like.\n",
    "> 1. Pick two nodes. Pretend that you're standing on one of the nodes, but you can't see any further beyond one neighbor away.\n",
    "> 1. Work out how you can find _a_ path from the node you're standing on to the other node, given that you can _only_ see nodes that are one neighbor away but have an infinitely good memory.\n",
    "\n",
    "If you are successful at designing the algorithm, you should get the answer below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "\n",
    "G = cf.load_sociopatterns_network()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.paths import bfs_algorithm\n",
    "\n",
    "# UNCOMMENT NEXT LINE TO GET THE ANSWER.\n",
    "# bfs_algorithm()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Implement the algorithm\n",
    "\n",
    "> Now that you've seen how the algorithm works, try implementing it!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# FILL IN THE BLANKS BELOW\n",
    "\n",
    "\n",
    "def path_exists(node1, node2, G):\n",
    "    \"\"\"\n",
    "    This function checks whether a path exists between two nodes (node1,\n",
    "    node2) in graph G.\n",
    "    \"\"\"\n",
    "    visited_nodes = _____\n",
    "    queue = [_____]\n",
    "\n",
    "    while len(queue) > 0:\n",
    "        node = ___________\n",
    "        neighbors = list(_________________)\n",
    "        if _____ in _________:\n",
    "            # print('Path exists between nodes {0} and {1}'.format(node1, node2))\n",
    "            return True\n",
    "        else:\n",
    "            visited_nodes.___(____)\n",
    "            nbrs = [_ for _ in _________ if _ not in _____________]\n",
    "            queue = ____ + _____\n",
    "\n",
    "    # print('Path does not exist between nodes {0} and {1}'.format(node1, node2))\n",
    "    return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# UNCOMMENT THE FOLLOWING TWO LINES TO SEE THE ANSWER\n",
    "from nams.solutions.paths import path_exists\n",
    "\n",
    "# path_exists??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# CHECK YOUR ANSWER AGAINST THE TEST FUNCTION BELOW\n",
    "from random import sample\n",
    "import networkx as nx\n",
    "\n",
    "\n",
    "def test_path_exists(N):\n",
    "    \"\"\"\n",
    "    N: The number of times to spot-check.\n",
    "    \"\"\"\n",
    "    for i in range(N):\n",
    "        n1, n2 = sample(list(G.nodes()), 2)\n",
    "        assert path_exists(n1, n2, G) == bool(nx.shortest_path(G, n1, n2))\n",
    "    return True\n",
    "\n",
    "\n",
    "assert test_path_exists(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualizing Paths\n",
    "\n",
    "One of the objectives of that exercise before was to help you \"think on graphs\".\n",
    "Now that you've learned how to do so, you might be wondering,\n",
    "\"How do I visualize that path through the graph?\"\n",
    "\n",
    "Well first off, if you inspect the `test_path_exists` function above,\n",
    "you'll notice that NetworkX provides a `shortest_path()` function\n",
    "that you can use. Here's what using `nx.shortest_path()` looks like."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "path = nx.shortest_path(G, 7, 400)\n",
    "path"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, it returns the nodes along the shortest path,\n",
    "incidentally in the exact order that you would traverse.\n",
    "\n",
    "One thing to note, though!\n",
    "If there are multiple shortest paths from one node to another,\n",
    "NetworkX will only return one of them.\n",
    "\n",
    "So how do you draw those nodes _only_?\n",
    "\n",
    "You can use the `G.subgraph(nodes)`\n",
    "to return a new graph that only has nodes in `nodes`\n",
    "and only the edges that exist between them.\n",
    "After that, you can use any plotting library you like.\n",
    "We will show an example here that uses nxviz's matrix plot.\n",
    "\n",
    "Let's see it in action:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "\n",
    "g = G.subgraph(path)\n",
    "nv.matrix(g, sort_by=\"order\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_Voila!_ Now we have the subgraph (1) extracted and (2) drawn to screen!\n",
    "In this case, the matrix plot is a suitable visualization for its compactness.\n",
    "The off-diagonals also show that each node is a neighbor to the next one.\n",
    "\n",
    "You'll also notice that if you try to modify the graph `g`, say by adding a node:\n",
    "\n",
    "```python\n",
    "g.add_node(2048)\n",
    "```\n",
    "\n",
    "you will get an error:\n",
    "\n",
    "```python\n",
    "---------------------------------------------------------------------------\n",
    "NetworkXError                             Traceback (most recent call last)\n",
    "<ipython-input-10-ca6aa4c26819> in <module>\n",
    "----> 1 g.add_node(2048)\n",
    "\n",
    "~/anaconda/envs/nams/lib/python3.7/site-packages/networkx/classes/function.py in frozen(*args, **kwargs)\n",
    "    156 def frozen(*args, **kwargs):\n",
    "    157     \"\"\"Dummy method for raising errors when trying to modify frozen graphs\"\"\"\n",
    "--> 158     raise nx.NetworkXError(\"Frozen graph can't be modified\")\n",
    "    159 \n",
    "    160 \n",
    "\n",
    "NetworkXError: Frozen graph can't be modified\n",
    "```\n",
    "\n",
    "From the perspective of semantics, this makes a ton of sense:\n",
    "the subgraph `g` is a perfect subset of the larger graph `G`,\n",
    "and should not be allowed to be modified\n",
    "unless the larger container graph is modified."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Draw path with neighbors one degree out\n",
    "\n",
    "Try out this next exercise:\n",
    "\n",
    "> Extend graph drawing with the neighbors of each of those nodes.\n",
    "> Use any of the nxviz plots (`nv.matrix`, `nv.arc`, `nv.circos`);\n",
    "> try to see which one helps you tell the best story."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.paths import plot_path_with_neighbors\n",
    "\n",
    "### YOUR SOLUTION BELOW"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "plot_path_with_neighbors(G, 7, 400)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this case, we opted for an Arc plot because we only have one grouping of nodes but have a logical way to order them.\n",
    "Because the path follows the order, the edges being highlighted automatically look like hops through the graph."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bottleneck nodes\n",
    "\n",
    "We're now going to revisit the concept of an \"important node\",\n",
    "this time now leveraging what we know about paths.\n",
    "\n",
    "In the \"hubs\" chapter, we saw how a node that is \"important\"\n",
    "could be so because it is connected to many other nodes.\n",
    "\n",
    "Paths give us an alternative definition.\n",
    "If we imagine that we have to pass a message on a graph\n",
    "from one node to another,\n",
    "then there may be \"bottleneck\" nodes\n",
    "for which if they are removed,\n",
    "then messages have a harder time flowing through the graph.\n",
    "\n",
    "One metric that measures this form of importance\n",
    "is the \"betweenness centrality\" metric.\n",
    "On a graph through which a generic \"message\" is flowing,\n",
    "a node with a high betweenness centrality\n",
    "is one that has a high proportion of shortest paths\n",
    "flowing through it.\n",
    "In other words, it behaves like a _bottleneck_."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Betweenness centrality in NetworkX\n",
    "\n",
    "NetworkX provides a \"betweenness centrality\" function\n",
    "that behaves consistently with the \"degree centrality\" function,\n",
    "in that it returns a mapping from node to metric:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "pd.Series(nx.betweenness_centrality(G))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: compare degree and betweenness centrality\n",
    "\n",
    "> Make a scatterplot of degree centrality on the x-axis\n",
    "> and betweenness centrality on the y-axis.\n",
    "> Do they correlate with one another?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# YOUR ANSWER HERE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.paths import plot_degree_betweenness\n",
    "\n",
    "plot_degree_betweenness(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Think about it...\n",
    "\n",
    "...does it make sense that degree centrality and betweenness centrality\n",
    "are not well-correlated?\n",
    "\n",
    "Can you think of a scenario where a node has a\n",
    "\"high\" betweenness centrality\n",
    "but a \"low\" degree centrality?\n",
    "Before peeking at the graph below,\n",
    "think about your answer for a moment."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nx.draw(nx.barbell_graph(5, 1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Recap\n",
    "\n",
    "In this chapter, you learned the following things:\n",
    "\n",
    "1. You figured out how to implement the breadth-first-search algorithm to find shortest paths.\n",
    "1. You learned how to extract subgraphs from a larger graph.\n",
    "1. You implemented visualizations of subgraphs, which should help you as you communicate with colleagues.\n",
    "1. You calculated betweenness centrality metrics for a graph, and visualized how they correlated with degree centrality."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solutions\n",
    "\n",
    "Here are the solutions to the exercises above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions import paths\n",
    "import inspect\n",
    "\n",
    "print(inspect.getsource(paths))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/02-algorithms/01-hubs.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"-oimHbVDdDA\", width=560, height=315)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Because of the relational structure in a graph,\n",
    "we can begin to think about \"importance\" of a node\n",
    "that is induced because of its relationships\n",
    "to the rest of the nodes in the graph.\n",
    "\n",
    "Before we go on, let's think about\n",
    "a pertinent and contemporary example.\n",
    "\n",
    "### An example: contact tracing\n",
    "\n",
    "At the time of writing (April 2020),\n",
    "finding important nodes in a graph has actually taken on a measure of importance\n",
    "that we might not have appreciated before.\n",
    "With the COVID-19 virus spreading,\n",
    "contact tracing has become quite important.\n",
    "In an infectious disease contact network,\n",
    "where individuals are nodes and\n",
    "contact between individuals of some kind are the edges,\n",
    "an \"important\" node in this contact network\n",
    "would be an individual who was infected\n",
    "who also was in contact with many people\n",
    "during the time that they were infected.\n",
    "\n",
    "### Our dataset: \"Sociopatterns\"\n",
    "\n",
    "The dataset that we will use in this chapter is the \"[sociopatterns network][sociopatterns]\" dataset.\n",
    "Incidentally, it's also about infectious diseases. \n",
    "\n",
    "[sociopatterns]: http://www.sociopatterns.org/datasets/infectious-sociopatterns-dynamic-contact-networks/\n",
    "\n",
    "Note to readers: We originally obtained the dataset in 2014\n",
    "from the Konect website.\n",
    "It is unfortunately no longer available.\n",
    "The sociopatterns.org website hosts an edge list of a slightly different format,\n",
    "so it will look different from what we have here.\n",
    "\n",
    "From the original description on Konect, here is the description of the dataset:\n",
    "\n",
    "> This network describes the face-to-face behavior of people\n",
    "> during the exhibition INFECTIOUS: STAY AWAY in 2009\n",
    "> at the Science Gallery in Dublin.\n",
    "> Nodes represent exhibition visitors;\n",
    "> edges represent face-to-face contacts that were active for at least 20 seconds.\n",
    "> Multiple edges between two nodes are possible and denote multiple contacts.\n",
    "> The network contains the data from the day with the most interactions.\n",
    "\n",
    "To simplify the network, we have represented only the last contact between individuals."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "\n",
    "G = cf.load_sociopatterns_network()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is loaded as an undirected graph object:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As usual, before proceeding with any analysis,\n",
    "we should know basic graph statistics."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(G.nodes()), len(G.edges())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## A Measure of Importance: \"Number of Neighbors\"\n",
    "\n",
    "One measure of importance of a node is\n",
    "the number of **neighbors** that the node has.\n",
    "What is a **neighbor**?\n",
    "We will work with the following definition:\n",
    "\n",
    "> The neighbor of a node is connected to that node by an edge.\n",
    "\n",
    "Let's explore this concept, using the NetworkX API.\n",
    "\n",
    "Every NetworkX graph provides a `G.neighbors(node)` class method,\n",
    "which lets us query a graph for the number of neighbors\n",
    "of a given node:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "G.neighbors(7)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It returns a generator that doesn't immediately return\n",
    "the exact neighbors list.\n",
    "This means we cannot know its exact length,\n",
    "as it is a generator.\n",
    "If you tried to do:\n",
    "\n",
    "```python\n",
    "len(G.neighbors(7))\n",
    "```\n",
    "\n",
    "you would get the following error:\n",
    "\n",
    "```python\n",
    "---------------------------------------------------------------------------\n",
    "TypeError                                 Traceback (most recent call last)\n",
    "<ipython-input-13-72c56971d077> in <module>\n",
    "----> 1 len(G.neighbors(7))\n",
    "\n",
    "TypeError: object of type 'dict_keyiterator' has no len()\n",
    "```\n",
    "\n",
    "Hence, we will need to cast it as a list in order to know\n",
    "both its length\n",
    "and its members:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(G.neighbors(7))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the event that some nodes have an extensive list of neighbors,\n",
    "then using the `dict_keyiterator` is potentially a good memory-saving technique,\n",
    "as it lazily yields the neighbors."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Rank-ordering the number of neighbors a node has\n",
    "\n",
    "Since we know how to get the list of nodes that are neighbors of a given node,\n",
    "try this following exercise:\n",
    "\n",
    "> Can you create a ranked list of the importance of each individual, based on the number of neighbors they have?\n",
    "\n",
    "Here are a few hints to help:\n",
    "\n",
    "- You could consider using a `pandas Series`. This would be a modern and idiomatic way of approaching the problem.\n",
    "- You could also consider using Python's `sorted` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.hubs import rank_ordered_neighbors\n",
    "\n",
    "#### REPLACE THE NEXT FEW LINES WITH YOUR ANSWER\n",
    "# answer = rank_ordered_neighbors(G)\n",
    "# answer"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The original implementation looked like the following"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.hubs import rank_ordered_neighbors_original\n",
    "\n",
    "# rank_ordered_neighbors_original??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And another implementation that uses generators:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.hubs import rank_ordered_neighbors_generator\n",
    "\n",
    "# rank_ordered_neighbors_generator??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generalizing \"neighbors\" to arbitrarily-sized graphs\n",
    "\n",
    "The concept of neighbors is simple and appealing,\n",
    "but it leaves us with a slight point of dissatisfaction:\n",
    "it is difficult to compare graphs of different sizes.\n",
    "Is a node more important solely because it has more neighbors?\n",
    "What if it were situated in an extremely large graph?\n",
    "Would we not expect it to have more neighbors?\n",
    "\n",
    "As such, we need a normalization factor.\n",
    "One reasonable one, in fact, is\n",
    "_the number of nodes that a given node could **possibly** be connected to._\n",
    "By taking the ratio of the number of neighbors a node has\n",
    "to the number of neighbors it could possibly have,\n",
    "we get the **degree centrality** metric.\n",
    "\n",
    "Formally defined, the degree centrality of a node (let's call it $d$)\n",
    "is the number of neighbors that a node has (let's call it $n$)\n",
    "divided by the number of neighbors it could _possibly_ have (let's call it $N$):\n",
    "\n",
    "$$d = \\frac{n}{N}$$\n",
    "\n",
    "NetworkX provides a function for us to calculate degree centrality conveniently:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "import pandas as pd\n",
    "\n",
    "dcs = pd.Series(nx.degree_centrality(G))\n",
    "dcs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`nx.degree_centrality(G)` returns to us a dictionary of key-value pairs,\n",
    "where the keys are node IDs\n",
    "and values are the degree centrality score.\n",
    "To save on output length, I took the liberty of casting it as a pandas Series\n",
    "to make it easier to display.\n",
    "\n",
    "Incidentally, we can also sort the series\n",
    "to find the nodes with the highest degree centralities:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dcs.sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Does the list order look familiar?\n",
    "It should, since the numerator of the degree centrality metric\n",
    "is identical to the number of neighbors,\n",
    "and the denominator is a constant.\n",
    "\n",
    "## Distribution of graph metrics\n",
    "\n",
    "One important concept that you should come to know\n",
    "is that the distribution of node-centric values\n",
    "can characterize classes of graphs.\n",
    "\n",
    "What do we mean by \"distribution of node-centric values\"?\n",
    "One would be the degree distribution,\n",
    "that is, the collection of node degree values in a graph.\n",
    "\n",
    "Generally, you might be familiar with plotting a histogram\n",
    "to visualize distributions of values,\n",
    "but in this book, we are going to avoid histograms like the plague.\n",
    "I detail a lot of reasons in a [blog post][ecdf] I wrote in 2018,\n",
    "but the main points are that:\n",
    "\n",
    "1. It's easier to lie with histograms.\n",
    "1. You get informative statistical information (median, IQR, extremes/outliers)\n",
    "more easily.\n",
    "\n",
    "[ecdf]: https://ericmjl.github.io/blog/2018/7/14/ecdfs/\n",
    "\n",
    "### Exercise: Degree distribution\n",
    "\n",
    "In this next exercise, we are going to get practice visualizing these values\n",
    "using empirical cumulative distribution function plots.\n",
    "\n",
    "I have written for you an ECDF function that you can use already.\n",
    "Its API looks like the following:\n",
    "\n",
    "```python\n",
    "x, y = ecdf(list_of_values)\n",
    "```\n",
    "\n",
    "giving you `x` and `y` values that you can directly plot.\n",
    "\n",
    "The exercise prompt is this:\n",
    "\n",
    "> Plot the ECDF of the degree centrality and degree distributions.\n",
    "\n",
    "First do it for **degree centrality**:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.functions import ecdf\n",
    "from nams.solutions.hubs import ecdf_degree_centrality\n",
    "\n",
    "#### REPLACE THE FUNCTION CALL WITH YOUR ANSWER\n",
    "ecdf_degree_centrality(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now do it for **degree**:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.hubs import ecdf_degree\n",
    "\n",
    "#### REPLACE THE FUNCTION CALL WITH YOUR ANSWER\n",
    "ecdf_degree(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The fact that they are identically-shaped\n",
    "should not surprise you!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: What about that denominator?\n",
    "\n",
    "The denominator $N$ in the degree centrality definition\n",
    "is \"the number of nodes that a node could _possibly_ be connected to\".\n",
    "Can you think of two ways $N$ be defined?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.hubs import num_possible_neighbors\n",
    "\n",
    "#### UNCOMMENT TO SEE MY ANSWER\n",
    "# print(num_possible_neighbors())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Circos Plotting\n",
    "\n",
    "Let's get some practice with the `nxviz` API.\n",
    "\n",
    "> Visualize the graph `G`, while ordering and colouring them by the 'order' node attribute."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.hubs import circos_plot\n",
    "\n",
    "#### REPLACE THE NEXT LINE WITH YOUR ANSWER\n",
    "circos_plot(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And here's an alternative view using an arc plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "\n",
    "nv.arc(G, sort_by=\"order\", node_color_by=\"order\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Visual insights\n",
    "\n",
    "Since we know that node colour and order\n",
    "are by the \"order\" in which the person entered into the exhibit,\n",
    "what does this visualization tell you?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.hubs import visual_insights\n",
    "\n",
    "#### UNCOMMENT THE NEXT LINE TO SEE MY ANSWER\n",
    "# print(visual_insights())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Investigating degree centrality and node order\n",
    "\n",
    "One of the insights that we might have gleaned from visualizing the graph\n",
    "is that the nodes that have a high degree centrality\n",
    "might also be responsible for the edges that criss-cross the Circos plot.\n",
    "To test this, plot the following:\n",
    "\n",
    "- x-axis: node degree centrality\n",
    "- y-axis: maximum difference between the neighbors' `order`s (a node attribute) and the node's `order`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.hubs import dc_node_order\n",
    "\n",
    "dc_node_order(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The somewhat positive correlation between the degree centrality might tell us that this trend holds true.\n",
    "A further applied question would be to ask what behaviour of these nodes would give rise to this pattern.\n",
    "Are these nodes actually exhibit staff?\n",
    "Or is there some other reason why they are staying so long?\n",
    "This, of course, would require joining in further information\n",
    "that we would overlay on top of the graph\n",
    "(by adding them as node or edge attributes)\n",
    "before we might make further statements."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reflections\n",
    "\n",
    "In this chapter, we defined a metric of node importance: the degree centrality metric.\n",
    "In the example we looked at, it could help us identify\n",
    "potential infectious agent superspreaders in a disease contact network.\n",
    "In other settings, it might help us spot:\n",
    "\n",
    "- message amplifiers/influencers in a social network, and \n",
    "- potentially crowded airports that have lots of connections into and out of it (still relevant to infectious disease spread!)\n",
    "- and many more!\n",
    "\n",
    "What other settings can you think of in which the number of neighbors that a node has can become\n",
    "a metric of importance for the node?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solutions\n",
    "\n",
    "Here are the solutions to the exercises above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions import hubs\n",
    "import inspect\n",
    "\n",
    "print(inspect.getsource(hubs))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/02-algorithms/03-structures.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"3DWSRCbPPJs\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you remember, at the beginning of this book,\n",
    "we saw a quote from John Quackenbush that essentially said\n",
    "that the reason a graph is interesting is because of its edges.\n",
    "In this chapter, we'll see this in action once again,\n",
    "as we are going to figure out how to leverage the edges\n",
    "to find special _structures_ in a graph.\n",
    "\n",
    "## Triangles\n",
    "\n",
    "The first structure that we are going to learn about is **triangles**.\n",
    "Triangles are super interesting!\n",
    "They are what one might consider to be\n",
    "\"the simplest complex structure\" in a graph.\n",
    "Triangles can also have semantically-rich meaning depending on the application.\n",
    "To borrow a bad example, love triangles in social networks are generally frowned upon,\n",
    "while on the other hand, when we connect two people that we know together,\n",
    "we instead _complete_ a triangle.\n",
    "\n",
    "### Load Data\n",
    "\n",
    "To learn about triangles,\n",
    "we are going to leverage a physician trust network.\n",
    "Here's the data description:\n",
    "\n",
    "> This directed network captures innovation spread among 246 physicians \n",
    "> for towns in Illinois, Peoria, Bloomington, Quincy and Galesburg.\n",
    "> The data was collected in 1966.\n",
    "> A node represents a physician and an edge between two physicians\n",
    "> shows that the left physician told that the right physician is his friend\n",
    "> or that he turns to the right physician if he needs advice\n",
    "> or is interested in a discussion.\n",
    "> There always only exists one edge between two nodes\n",
    "> even if more than one of the listed conditions are true."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "G = cf.load_physicians_network()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Finding triangles in a graph\n",
    "\n",
    "This exercise is going to flex your ability\n",
    "to \"think on a graph\", just as you did in the previous chapters.\n",
    "\n",
    "> Leveraging what you know, can you think of a few strategies\n",
    "> to find triangles in a graph?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.structures import triangle_finding_strategies\n",
    "\n",
    "# triangle_finding_strategies()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Identify whether a node is in a triangle relationship or not\n",
    "\n",
    "Let's now get down to implementing this next piece of code.\n",
    "\n",
    "> Write a function that identifies whether a node is or is not in a triangle relationship.\n",
    "> It should take in a graph `G` and a node `n`,\n",
    "> and return a boolean True if the node `n` is in any triangle relationship\n",
    "> and boolean False if the node `n` is not in any triangle relationship.\n",
    "\n",
    "A hint that may help you:\n",
    "\n",
    "> Every graph object `G` has a `G.has_edge(n1, n2)` method that you can use to identify whether a graph has an edge between `n1` and `n2`.\n",
    "\n",
    "Also:\n",
    "\n",
    "> `itertools.combinations` lets you iterate over every _K-combination_ of items in an iterable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def in_triangle(G, node):\n",
    "    # Your answer here\n",
    "    pass\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import in_triangle\n",
    "\n",
    "# UNCOMMENT THE NEXT LINE TO SEE MY ANSWER\n",
    "# in_triangle??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, test your implementation below!\n",
    "The code cell will not error out if your answer is correct."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import sample\n",
    "import networkx as nx\n",
    "\n",
    "def test_in_triangle():\n",
    "    nodes = sample(list(G.nodes()), 10)\n",
    "    for node in nodes:\n",
    "        assert in_triangle(G, 3) == bool(nx.triangles(G, 3))\n",
    "\n",
    "test_in_triangle()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see from the test function above,\n",
    "NetworkX provides an `nx.triangles(G, node)` function.\n",
    "It returns the number of triangles that a node is involved in.\n",
    "We convert it to boolean as a hack to check whether or not\n",
    "a node is involved in a triangle relationship\n",
    "because 0 is equivalent to boolean `False`,\n",
    "while any non-zero number is equivalent to boolean `True`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Extract triangles for plotting\n",
    "\n",
    "We're going to leverage another piece of knowledge that you already have:\n",
    "the ability to extract subgraphs.\n",
    "We'll be plotting all of the triangles that a node is involved in.\n",
    "\n",
    "> Given a node, write a function that extracts out\n",
    "> all of the neighbors that it is in a triangle relationship with.\n",
    "> Then, in a new function,\n",
    "> implement code that plots only the subgraph\n",
    "> that contains those nodes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_triangle_neighbors(G, n):\n",
    "    # Your answer here\n",
    "    pass\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import get_triangle_neighbors\n",
    "\n",
    "# UNCOMMENT THE NEXT LINE TO SEE MY ANSWER\n",
    "# get_triangle_neighbors??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_triangle_relations(G, n):\n",
    "    # Your answer here\n",
    "    pass\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import plot_triangle_relations\n",
    "\n",
    "plot_triangle_relations(G, 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Triadic Closure\n",
    "\n",
    "In professional circles, making connections between two people\n",
    "is one of the most valuable things you can do professionally.\n",
    "What you do in that moment is what we would call\n",
    "**triadic closure**.\n",
    "Algorithmically, we can do the same thing\n",
    "if we maintain a graph of connections!\n",
    "\n",
    "Essentially, what we are looking for\n",
    "are \"open\" or \"unfinished\" triangles\".\n",
    "\n",
    "In this section, we'll try our hand at implementing\n",
    "a rudimentary triadic closure system.\n",
    "\n",
    "### Exercise: Design the algorithm\n",
    "\n",
    "> What graph logic would you use to identify triadic closure opportunities?\n",
    "> Try writing out your general strategy, or discuss it with someone."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.structures import triadic_closure_algorithm\n",
    "\n",
    "# UNCOMMENT FOR MY ANSWER\n",
    "# triadic_closure_algorithm()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Implement triadic closure.\n",
    "\n",
    "Now, try your hand at implementing triadic closure.\n",
    "\n",
    "> Write a function that takes in a graph `G` and a node `n`,\n",
    "> and returns all of the neighbors that are potential triadic closures\n",
    "> with `n` being the center node.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_open_triangles_neighbors(G, n):\n",
    "    # Your answer here\n",
    "    pass\n",
    "\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import get_open_triangles_neighbors\n",
    "\n",
    "# UNCOMMENT THE NEXT LINE TO SEE MY ANSWER\n",
    "# get_open_triangles_neighbors??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Plot the open triangles\n",
    "\n",
    "> Now, write a function that takes in a graph `G` and a node `n`,\n",
    "> and plots out that node `n` and all of the neighbors\n",
    "> that it could help close triangles with.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_open_triangle_relations(G, n):\n",
    "    # Your answer here\n",
    "    pass\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import plot_open_triangle_relations\n",
    "\n",
    "plot_open_triangle_relations(G, 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Cliques\n",
    "\n",
    "Triangles are interesting in a graph theoretic setting\n",
    "because triangles are the simplest complex clique that exist.\n",
    "\n",
    "But wait!\n",
    "What is the definition of a \"clique\"?\n",
    "\n",
    "> A \"clique\" is a set of nodes in a graph\n",
    "> that are fully connected with one another\n",
    "> by edges between them.\n",
    "\n",
    "### Exercise: Simplest cliques\n",
    "\n",
    "Given this definition, what is the simplest \"clique\" possible?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.structures import simplest_clique\n",
    "\n",
    "# UNCOMMENT THE NEXT LINE TO SEE MY ANSWER\n",
    "# simplest_clique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### $k$-Cliques\n",
    "\n",
    "Cliques are identified by their size $k$,\n",
    "which is the number of nodes that are present in the clique.\n",
    "\n",
    "A triangle is what we would consider to be a $k$-clique where $k=3$.\n",
    "\n",
    "A square with cross-diagonal connections is what we would consider to be\n",
    "a $k$-clique where $k=4$.\n",
    "\n",
    "By now, you should get the gist of the idea.\n",
    "\n",
    "### Maximal Cliques\n",
    "\n",
    "Related to this idea of a $k$-clique is another idea called \"maximal cliques\".\n",
    "\n",
    "Maximal cliques are defined as follows:\n",
    "\n",
    "> A maximal clique is a subgraph of nodes in a graph\n",
    "> \n",
    "> 1. to which no other node can be added to it and \n",
    "> 2. still remain a clique.\n",
    "\n",
    "NetworkX provides a way to find all maximal cliques:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# I have truncated the output to the first 5 maximal cliques.\n",
    "list(nx.find_cliques(G))[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: finding sized-$k$ maximal cliques\n",
    "\n",
    "> Write a generator function that yields all maximal cliques of size $k$.\n",
    "\n",
    "I'm requesting a generator as a matter of good practice;\n",
    "you never know when the list you return might explode in memory consumption,\n",
    "so generators are a cheap and easy way to reduce memory usage."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def size_k_maximal_cliques(G, k):\n",
    "    # Your answer here\n",
    "    pass\n",
    "\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import size_k_maximal_cliques"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, test your implementation against the test function below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_size_k_maximal_cliques(G, k):\n",
    "    clique_generator = size_k_maximal_cliques(G, k)\n",
    "    for clique in clique_generator:\n",
    "        assert len(clique) == k\n",
    "\n",
    "test_size_k_maximal_cliques(G, 5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Clique Decomposition\n",
    "\n",
    "One _super_ neat property of cliques\n",
    "is that every clique of size $k$\n",
    "can be decomposed to the set of cliques of size $k-1$.\n",
    "\n",
    "Does this make sense to you?\n",
    "If not, think about triangles (3-cliques).\n",
    "They can be decomposed to three edges (2-cliques).\n",
    "\n",
    "Think again about 4-cliques.\n",
    "Housed within 4-cliques are four 3-cliques.\n",
    "_Draw it out if you're still not convinced!_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: finding all $k$-cliques in a graph\n",
    "\n",
    "> Knowing this property of $k$-cliques,\n",
    "> write a generator function that yields all $k$-cliques in a graph,\n",
    "> leveraging the `nx.find_cliques(G)` function.\n",
    "\n",
    "Some hints to help you along:\n",
    "\n",
    "> If a $k$-clique can be decomposed to its $k-1$ cliques,\n",
    "> it follows that the $k-1$ cliques can be decomposed into $k-2$ cliques,\n",
    "> and so on until you hit 2-cliques.\n",
    "> This implies that all cliques of size $k$\n",
    "> house cliques of size $n < k$, where $n >= 2$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_k_cliques(G, k):\n",
    "    # your answer here\n",
    "    pass\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import find_k_cliques\n",
    "\n",
    "def test_find_k_cliques(G, k):\n",
    "    for clique in find_k_cliques(G, k):\n",
    "        assert len(clique) == k\n",
    "\n",
    "test_find_k_cliques(G, 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Connected Components\n",
    "\n",
    "Now that we've explored a lot around cliques,\n",
    "we're now going to explore this idea of \"connected components\".\n",
    "To do so, I am going to have you draw the graph\n",
    "that we are working with.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "\n",
    "nv.circos(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Visual insights\n",
    "\n",
    "From this rendering of the CircosPlot,\n",
    "what visual insights do you have about the structure of the graph?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.structures import visual_insights\n",
    "\n",
    "# UNCOMMENT TO SEE MY ANSWER\n",
    "# visual_insights()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Defining connected components\n",
    "\n",
    "From [Wikipedia](https://en.wikipedia.org/wiki/Connected_component_%28graph_theory%29):\n",
    "\n",
    "> In graph theory, a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.\n",
    "\n",
    "NetworkX provides a function to let us find all of the connected components:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "ccsubgraph_nodes = list(nx.connected_components(G))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's see how many connected component subgraphs are present:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "len(ccsubgraph_nodes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: visualizing connected component subgraphs\n",
    "\n",
    "In this exercise, we're going to draw a circos plot of the graph, \n",
    "but colour and order the nodes by their connected component subgraph.\n",
    "\n",
    "Recall Circos API:\n",
    "\n",
    "```python\n",
    "c = CircosPlot(G, node_order='node_attribute', node_color='node_attribute')\n",
    "c.draw()\n",
    "plt.show()  # or plt.savefig(...)\n",
    "```\n",
    "\n",
    "Follow the steps along here to accomplish this.\n",
    "\n",
    "> Firstly, label the nodes with a unique identifier for connected component subgraph\n",
    "> that it resides in.\n",
    "> Use `subgraph` to store this piece of metadata."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def label_connected_component_subgraphs(G):\n",
    "    # Your answer here\n",
    "    return G\n",
    "\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import label_connected_component_subgraphs\n",
    "G_labelled = label_connected_component_subgraphs(G)\n",
    "\n",
    "# UNCOMMENT TO SEE THE ANSWER\n",
    "# label_connected_component_subgraphs??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Now, draw a CircosPlot with the node order and colouring\n",
    "> dictated by the `subgraph` key."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def plot_cc_subgraph(G):\n",
    "    # Your answer here\n",
    "    pass\n",
    "\n",
    "\n",
    "# COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER\n",
    "from nams.solutions.structures import plot_cc_subgraph\n",
    "from nxviz import annotate\n",
    "\n",
    "plot_cc_subgraph(G_labelled)\n",
    "annotate.circos_group(G_labelled, group_by=\"subgraph\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using an arc plot will also clearly illuminate for us\n",
    "that there are no inter-group connections."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nv.arc(G_labelled, group_by=\"subgraph\", node_color_by=\"subgraph\")\n",
    "annotate.arc_group(G_labelled, group_by=\"subgraph\", rotation=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_Voila!_ It looks quite clear that there are indeed four disjoint group of physicians."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solutions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions import structures\n",
    "import inspect\n",
    "\n",
    "print(inspect.getsource(structures))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/01-introduction/01-graphs.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"k4KHoLC7TFE\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In our world, networks are an immensely useful _data modelling tool_\n",
    "to model complex _relational_ problems.\n",
    "Building on top of a network-oriented data model,\n",
    "they have been put to great use in a wide variety of settings."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## A _formal_ definition of networks\n",
    "\n",
    "Before we explore examples of networks,\n",
    "we want to first give you a more formal definition\n",
    "of what networks are.\n",
    "The reason is that knowing a _formal_ definition\n",
    "helps us refine our application of networks.\n",
    "So bear with me for a moment.\n",
    "\n",
    "In the slightly more academic literature,\n",
    "networks are more formally referred to as **graphs**.\n",
    "\n",
    "Graphs are comprised of two _sets_ of objects:\n",
    "\n",
    "- A **node set**: the \"entities\" in a graph.\n",
    "- An **edge set**: the record of \"relationships\" between the entities in the graph.\n",
    "\n",
    "For example, if a **node set** $n$ is comprised of elements:\n",
    "\n",
    "$$n = \\{a, b, c, d, ...\\}$$\n",
    "\n",
    "Then, the **edge set** $e$ would be represented as tuples of _pairs_ of elements:\n",
    "\n",
    "$$e = \\{(a, b), (a, c), (c, d), ...\\}$$\n",
    "\n",
    "If you extracted every node from the edge set $e$,\n",
    "it should form _at least a subset_ of the node set $n$.\n",
    "(It is at least a subset because not every node in $n$ might participate in an edge.)\n",
    "\n",
    "If you draw out a network, the \"nodes\" are commonly represented as shapes, such as circles,\n",
    "while the \"edges\" are the lines between the shapes."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Examples of Networks\n",
    "\n",
    "Now that we have a proper definition of a graph,\n",
    "let's move on to explore examples of graphs.\n",
    "\n",
    "One example I (Eric Ma) am fond of, based on my background as a biologist,\n",
    "is a protein-protein interaction network.\n",
    "Here, the graph can be defined in the following way:\n",
    "\n",
    "- nodes/entities are the proteins,\n",
    "- edges/relationships are defined as \"one protein is known to bind with another\".\n",
    "\n",
    "A more colloquial example of networks is an air transportation network.\n",
    "Here, the graph can be defined in the following way:\n",
    "\n",
    "- nodes/entities are airports\n",
    "- edges/relationships are defined as \"at least one flight carrier flies between the airports\".\n",
    "\n",
    "And another even more relatable example would be our ever-prevalent social networks!\n",
    "With Twitter, the graph can be defined in the following way:\n",
    "\n",
    "- nodes/entities are individual users\n",
    "- edges/relationships are defined as \"one user has decided to follow another\".\n",
    "\n",
    "Now that you've seen the framework for defining a graph,\n",
    "we'd like to invite you to answer the following question:\n",
    "**What examples of networks have _you_ seen before in your profession?**\n",
    "\n",
    "Go ahead and list it out."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Types of Graphs\n",
    "\n",
    "As you probably can see, graphs are a really flexible data model\n",
    "for modelling the world,\n",
    "as long as the nodes and edges are strictly defined.\n",
    "(If the nodes and edges are _sloppily_ defined,\n",
    "well, we run into a lot of interpretability problems later on.)\n",
    "\n",
    "If you are a member of both LinkedIn and Twitter,\n",
    "you might intuitively think that there's a _slight_ difference\n",
    "in the structure of the two \"social graphs\".\n",
    "You'd be absolutely correct on that count!\n",
    "\n",
    "Twitter is an example of what we would intuitively call a **directed** graph.\n",
    "Why is this so?\n",
    "The key here lies in how interactions are modelled.\n",
    "One user can follow another, but the other need not necessarily follow back.\n",
    "As such, there is a _directionality_ to the relationship.\n",
    "\n",
    "LinkedIn is an example of what we would intuitively call an **undirected** graph.\n",
    "Why is this so?\n",
    "The key here is that when two users are LinkedIn connections,\n",
    "we _automatically_ assign a bi-directional edge between them.\n",
    "As such, for convenience, we can collapse the bi-directional edge\n",
    "into an _undirected_ edge,\n",
    "thus yielding an undirected graph.\n",
    "\n",
    "If we wanted to turn LinkedIn into a directed graph,\n",
    "we might want to keep information on who initiated the invitation.\n",
    "In that way, the relationship is automatically bi-directional."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Edges define the interesting part of a graph\n",
    "\n",
    "While in graduate school, I (Eric Ma) once sat in a seminar\n",
    "organized by one of the professors on my thesis committee.\n",
    "The speaker that day was John Quackenbush,\n",
    "a faculty member of the Harvard School of Public Health.\n",
    "While the topic of the day remained fuzzy in my memory,\n",
    "one quote stood out:\n",
    "\n",
    "> The heart of a graph lies in its edges, not in its nodes.\n",
    "> (John Quackenbush, Harvard School of Public Health)\n",
    "\n",
    "Indeed, this is a key point to remember!\n",
    "Without edges, the nodes are merely collections of entities.\n",
    "In a data table, they would correspond to the rows.\n",
    "That alone can be interesting,\n",
    "but doesn't yield _relational insights_ between the entities."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/01-introduction/02-networkx-intro.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id='sdF0uJo2KdU', width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "In this chapter, we will introduce you to the NetworkX API.\n",
    "This will allow you to create and manipulate graphs in your computer memory,\n",
    "thus giving you a language \n",
    "to more concretely explore graph theory ideas.\n",
    "\n",
    "Throughout the book, we will be using different graph datasets\n",
    "to help us anchor ideas.\n",
    "In this section, we will work with a social network of seventh graders.\n",
    "Here, nodes are individual students,\n",
    "and edges represent their relationships.\n",
    "Edges between individuals show how often\n",
    "the seventh graders indicated other seventh graders as their favourite.\n",
    "\n",
    "The data are taken from the [Konect] graph data repository\n",
    "\n",
    "[Konect]: http://konect.cc/networks/moreno_seventh"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Data Model\n",
    "\n",
    "In NetworkX, graph data are stored in a dictionary-like fashion.\n",
    "They are placed under a `Graph` object,\n",
    "canonically instantiated with the variable `G` as follows:\n",
    "\n",
    "```python\n",
    "G = nx.Graph()\n",
    "```\n",
    "\n",
    "Of course, you are free to name the graph anything you want!\n",
    "\n",
    "Nodes are part of the attribute `G.nodes`.\n",
    "There, the node data are housed in a dictionary-like container,\n",
    "where the key is the node itself\n",
    "and the values are a dictionary of attributes. \n",
    "Node data are accessible using syntax that looks like:\n",
    "\n",
    "```python\n",
    "G.nodes[node1]\n",
    "```\n",
    "\n",
    "Edges are part of the attribute `G.edges`,\n",
    "which is also stored in a dictionary-like container.\n",
    "Edge data are accessible using syntax that looks like: \n",
    "\n",
    "```python\n",
    "G.edges[node1, node2]\n",
    "```\n",
    "Because of the dictionary-like implementation of the graph,\n",
    "any hashable object can be a node.\n",
    "This means strings and tuples, but not lists and sets."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Load Data\n",
    "\n",
    "Let's load some real network data to get a feel for the NetworkX API. This [dataset](http://konect.cc/networks/moreno_seventh) comes from a study of 7th grade students.\n",
    "\n",
    "> This directed network contains proximity ratings between students\n",
    "> from 29 seventh grade students from a school in Victoria.\n",
    "> Among other questions the students were asked\n",
    "> to nominate their preferred classmates for three different activities.\n",
    "> A node represents a student.\n",
    "> An edge between two nodes shows that\n",
    "> the left student picked the right student as his or her answer.\n",
    "> The edge weights are between 1 and 3 \n",
    "> and show how often the left student chose the right student as his/her favourite.\n",
    "\n",
    "In the original dataset, students were from an all-boys school.\n",
    "However, I have modified the dataset to instead be a mixed-gender school."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "from datetime import datetime\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import warnings\n",
    "from nams import load_data as cf\n",
    "\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "G = cf.load_seventh_grader_network()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Understanding a graph's basic statistics\n",
    "\n",
    "When you get graph data,\n",
    "one of the first things you'll want to do is to\n",
    "check its basic graph statistics:\n",
    "the number of nodes\n",
    "and the number of edges\n",
    "that are represented in the graph.\n",
    "This is a basic sanity-check on your data\n",
    "that you don't want to skip out on.\n",
    "\n",
    "### Querying graph type\n",
    "\n",
    "The first thing you need to know is the `type` of the graph:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Because the graph is a `DiGraph`,\n",
    "this tells us that the graph is a **directed** one.\n",
    "\n",
    "If it were undirected, the type would change:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "H = nx.Graph()\n",
    "type(H)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Querying node information\n",
    "\n",
    "Let's now query for the nodeset:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(G.nodes())[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`G.nodes()` returns a \"view\" on the nodes.\n",
    "We can't actually slice into the view and grab out a sub-selection,\n",
    "but we can _at least_ see what nodes are present.\n",
    "For brevity, we have sliced into `G.nodes()` passed into a `list()` constructor,\n",
    "so that we don't pollute the output.\n",
    "Because a `NodeView` is iterable, though,\n",
    "we can query it for its length:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(G.nodes())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If our nodes have metadata attached to them,\n",
    "we can view the metadata at the same time\n",
    "by passing in `data=True`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(G.nodes(data=True))[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "G.nodes(data=True) returns a `NodeDataView`,\n",
    "which you can see is dictionary-like.\n",
    "\n",
    "Additionally, we can select out individual nodes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "G.nodes[1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, because a `NodeDataView` is dictionary-like,\n",
    "looping over `G.nodes(data=True)`\n",
    "is very much like looping over key-value pairs of a dictionary.\n",
    "As such, we can write things like:\n",
    "\n",
    "```python\n",
    "for n, d in G.nodes(data=True):\n",
    "    # n is the node\n",
    "    # d is the metadata dictionary\n",
    "    ...\n",
    "```\n",
    "\n",
    "This is analogous to how we would loop over a dictionary:\n",
    "\n",
    "```python\n",
    "for k, v in dictionary.items():\n",
    "    # do stuff in the loop\n",
    "```\n",
    "\n",
    "Naturally, this leads us to our first exercise.\n",
    "\n",
    "### Exercise: Summarizing node metadata\n",
    "\n",
    "> Can you count how many males and females are represented in the graph?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.intro import node_metadata\n",
    "\n",
    "#### REPLACE THE NEXT LINE WITH YOUR ANSWER\n",
    "mf_counts = node_metadata(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Test your implementation by checking it against the `test_answer` function below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "from typing import Dict\n",
    "\n",
    "def test_answer(mf_counts: Dict):\n",
    "    assert mf_counts['female'] == 17\n",
    "    assert mf_counts['male'] == 12\n",
    "    \n",
    "test_answer(mf_counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "With this dictionary-like syntax,\n",
    "we can query back the metadata that's associated with any node."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Querying edge information\n",
    "\n",
    "Now that you've learned how to query for node information,\n",
    "let's now see how to query for all of the edges in the graph:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(G.edges())[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similar to the `NodeView`, `G.edges()` returns an `EdgeView` that is also iterable.\n",
    "As with above, we have abbreviated the output inside a sliced list\n",
    "to keep things readable.\n",
    "Because `G.edges()` is iterable, we can get its length to see the number of edges\n",
    "that are present in a graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(G.edges())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Likewise, we can also query for all of the edge's metadata:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(G.edges(data=True))[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Additionally, it is possible for us to select out individual edges, as long as they exist in the graph:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "G.edges[15, 10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This yields the metadata dictionary for that edge.\n",
    "\n",
    "If the edge does not exist, then we get an error:\n",
    "\n",
    "```python\n",
    ">>> G.edges[15, 16]\n",
    "```\n",
    "\n",
    "```python\n",
    "---------------------------------------------------------------------------\n",
    "KeyError                                  Traceback (most recent call last)\n",
    "<ipython-input-21-ce014cab875a> in <module>\n",
    "----> 1 G.edges[15, 16]\n",
    "\n",
    "~/anaconda/envs/nams/lib/python3.7/site-packages/networkx/classes/reportviews.py in __getitem__(self, e)\n",
    "    928     def __getitem__(self, e):\n",
    "    929         u, v = e\n",
    "--> 930         return self._adjdict[u][v]\n",
    "    931 \n",
    "    932     # EdgeDataView methods\n",
    "\n",
    "KeyError: 16\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As with the `NodeDataView`, the `EdgeDataView` is dictionary-like,\n",
    "with the difference being that the keys are 2-tuple-like\n",
    "instead of being single hashable objects.\n",
    "Thus, we can write syntax like the following to loop over the edgelist:\n",
    "\n",
    "```python\n",
    "for n1, n2, d in G.edges(data=True):\n",
    "    # n1, n2 are the nodes\n",
    "    # d is the metadata dictionary\n",
    "    ...\n",
    "```\n",
    "\n",
    "Naturally, this leads us to our next exercise."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Summarizing edge metadata\n",
    "\n",
    "> Can you write code to verify\n",
    "> that the maximum times any student rated another student as their favourite\n",
    "> is 3 times?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.intro import edge_metadata\n",
    "\n",
    "#### REPLACE THE NEXT LINE WITH YOUR ANSWER\n",
    "maxcount = edge_metadata(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Likewise, you can test your answer using the test function below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_maxcount(maxcount):\n",
    "    assert maxcount == 3\n",
    "    \n",
    "test_maxcount(maxcount)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Manipulating the graph\n",
    "\n",
    "Great stuff! You now know how to query a graph for:\n",
    "\n",
    "- its node set, optionally including metadata\n",
    "- individual node metadata\n",
    "- its edge set, optionally including metadata, and \n",
    "- individual edges' metadata\n",
    "\n",
    "Now, let's learn how to manipulate the graph.\n",
    "Specifically, we'll learn how to add nodes and edges to a graph.\n",
    "\n",
    "### Adding Nodes\n",
    "\n",
    "The NetworkX graph API lets you add a node easily:\n",
    "\n",
    "```python\n",
    "G.add_node(node, node_data1=some_value, node_data2=some_value)\n",
    "```\n",
    "\n",
    "### Adding Edges\n",
    "\n",
    "It also allows you to add an edge easily:\n",
    "\n",
    "```python\n",
    "G.add_edge(node1, node2, edge_data1=some_value, edge_data2=some_value)\n",
    "```\n",
    "\n",
    "### Metadata by Keyword Arguments\n",
    "\n",
    "In both cases, the keyword arguments that are passed into `.add_node()`\n",
    "are automatically collected into the metadata dictionary.\n",
    "\n",
    "Knowing this gives you enough knowledge to tackle the next exercise.\n",
    "\n",
    "### Exercise: adding students to the graph\n",
    "\n",
    "> We found out that there are two students that we left out of the network,\n",
    "> student no. 30 and 31. \n",
    "> They are one male (30) and one female (31), \n",
    "> and they are a pair that just love hanging out with one another \n",
    "> and with individual 7 (i.e. `count=3`), in both directions per pair. \n",
    "> Add this information to the graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.intro import adding_students\n",
    "\n",
    "#### REPLACE THE NEXT LINE WITH YOUR ANSWER\n",
    "G = adding_students(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "You can verify that the graph has been correctly created\n",
    "by executing the test function below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "def test_graph_integrity(G):\n",
    "    assert 30 in G.nodes()\n",
    "    assert 31 in G.nodes()\n",
    "    assert G.nodes[30]['gender'] == 'male'\n",
    "    assert G.nodes[31]['gender'] == 'female'\n",
    "    assert G.has_edge(30, 31)\n",
    "    assert G.has_edge(30, 7)\n",
    "    assert G.has_edge(31, 7)\n",
    "    assert G.edges[30, 7]['count'] == 3\n",
    "    assert G.edges[7, 30]['count'] == 3\n",
    "    assert G.edges[31, 7]['count'] == 3\n",
    "    assert G.edges[7, 31]['count'] == 3\n",
    "    assert G.edges[30, 31]['count'] == 3\n",
    "    assert G.edges[31, 30]['count'] == 3\n",
    "    print('All tests passed.')\n",
    "    \n",
    "test_graph_integrity(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Coding Patterns\n",
    "\n",
    "These are some recommended coding patterns when doing network analysis using NetworkX,\n",
    "which stem from my personal experience with the package."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### Iterating using List Comprehensions\n",
    "I would recommend that you use the following for compactness: \n",
    "\n",
    "```python\n",
    "[d['attr'] for n, d in G.nodes(data=True)]\n",
    "```\n",
    "\n",
    "And if the node is unimportant, you can do:\n",
    "\n",
    "```python\n",
    "[d['attr'] for _, d in G.nodes(data=True)]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### Iterating over Edges using List Comprehensions\n",
    "\n",
    "A similar pattern can be used for edges:\n",
    "\n",
    "```python\n",
    "[n2 for n1, n2, d in G.edges(data=True)]\n",
    "```\n",
    "\n",
    "or\n",
    "\n",
    "```python\n",
    "[n2 for _, n2, d in G.edges(data=True)]\n",
    "```\n",
    "\n",
    "If the graph you are constructing is a directed graph,\n",
    "with a \"source\" and \"sink\" available,\n",
    "then I would recommend the following naming of variables instead:\n",
    "\n",
    "```python\n",
    "[(sc, sk) for sc, sk, d in G.edges(data=True)]\n",
    "```\n",
    "\n",
    "or \n",
    "\n",
    "```python\n",
    "[d['attr'] for sc, sk, d in G.edges(data=True)]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Further Reading\n",
    "\n",
    "For a deeper look at the NetworkX API,\n",
    "be sure to check out the [NetworkX docs][nxdocs].\n",
    "\n",
    "[nxdocs]: https://networkx.readthedocs.io"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Further Exercises\n",
    "\n",
    "Here's some further exercises that you can use to get some practice.\n",
    "\n",
    "### Exercise: Unrequited Friendships\n",
    "\n",
    "> Try figuring out which students have \"unrequited\" friendships, that is, \n",
    "> they have rated another student as their favourite at least once, \n",
    "> but that other student has not rated them as their favourite at least once.\n",
    "\n",
    "_Hint: the goal here is to get a list of edges for which the reverse edge is not present._\n",
    "\n",
    "_Hint: You may need the class method `G.has_edge(n1, n2)`. This returns whether a graph has an edge between the nodes `n1` and `n2`._"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.intro import unrequitted_friendships_v1\n",
    "#### REPLACE THE NEXT LINE WITH YOUR ANSWER\n",
    "unrequitted_friendships = unrequitted_friendships_v1(G)\n",
    "assert len(unrequitted_friendships) == 124"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In a previous session at ODSC East 2018, a few other class participants provided the following solutions,\n",
    "which you can take a look at by uncommenting the following cells."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This first one by [@schwanne](https://github.com/schwanne) is the list comprehension version of the above solution:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.intro import unrequitted_friendships_v2\n",
    "# unrequitted_friendships_v2??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This one by [@end0](https://github.com/end0) is a unique one involving sets."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams.solutions.intro import unrequitted_friendships_v3\n",
    "# unrequitted_friendships_v3??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solution Answers\n",
    "\n",
    "Here are the answers to the exercises above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nams.solutions.intro as solutions\n",
    "import inspect\n",
    "\n",
    "print(inspect.getsource(solutions))"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "toc": {
   "colors": {
    "hover_highlight": "#DAA520",
    "navigate_num": "#000000",
    "navigate_text": "#333333",
    "running_highlight": "#FF0000",
    "selected_highlight": "#FFD700",
    "sidebar_border": "#EEEEEE",
    "wrapper_background": "#FFFFFF"
   },
   "moveMenuLeft": true,
   "nav_menu": {
    "height": "297px",
    "width": "252px"
   },
   "navigate_menu": true,
   "number_sections": true,
   "sideBar": true,
   "threshold": 4,
   "toc_cell": false,
   "toc_position": {
    "height": "530px",
    "left": "0px",
    "right": "1068px",
    "top": "33px",
    "width": "212px"
   },
   "toc_section_display": "block",
   "toc_window_display": true,
   "widenNotebook": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/01-introduction/03-viz.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"v9HrR_AF5Zc\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "In this chapter, We want to introduce you to the wonderful world of graph visualization.\n",
    "\n",
    "You probably have seen graphs that are visualized as hairballs.\n",
    "Apart from communicating how complex the graph is,\n",
    "hairballs don't really communicate much else.\n",
    "As such, my goal by the end of this chapter is \n",
    "to introduce you to what I call _rational graph visualization_.\n",
    "\n",
    "But before we can do that, let's first make sure we understand\n",
    "how to use NetworkX's drawing facilities to draw graphs to the screen.\n",
    "In a pinch, and for small graphs, it's very handy to have."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hairballs\n",
    "\n",
    "The node-link diagram is the canonical diagram we will see in publications.\n",
    "Nodes are commonly drawn as circles, while edges are drawn s lines.\n",
    "\n",
    "Node-link diagrams are common,\n",
    "and there's a good reason for this: it's convenient to draw!\n",
    "In NetworkX, we can draw node-link diagrams using:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "import networkx as nx\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "G = cf.load_seventh_grader_network()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "nx.draw(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Nodes more tightly connected with one another are clustered together. \n",
    "Initial node placement is done typically at random,\n",
    "so really it's tough to deterministically generate the same figure.\n",
    "If the network is small enough to visualize,\n",
    "and the node labels are small enough to fit in a circle,\n",
    "then you can use the `with_labels=True` argument\n",
    "to bring some degree of informativeness to the drawing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "G.is_directed()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "nx.draw(G, with_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "The downside to drawing graphs this way is that\n",
    "large graphs end up looking like hairballs.\n",
    "Can you imagine a graph with more than the 28 nodes that we have?\n",
    "As you probably can imagine, the default `nx.draw(G)`\n",
    "is probably not suitable for generating visual insights.\n",
    "\n",
    "## Matrix Plot\n",
    "\n",
    "A different way that we can visualize a graph is by visualizing it in its matrix form.\n",
    "The nodes are on the x- and y- axes, and a filled square represent an edge between the nodes.\n",
    "\n",
    "We can draw a graph's matrix form conveniently by using `nxviz.MatrixPlot`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv \n",
    "from nxviz import annotate\n",
    "\n",
    "\n",
    "nv.matrix(G, group_by=\"gender\", node_color_by=\"gender\")\n",
    "annotate.matrix_group(G, group_by=\"gender\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What can you tell from the graph visualization?\n",
    "A few things are immediately obvious:\n",
    "\n",
    "- The diagonal is empty: no student voted for themselves as their favourite.\n",
    "- The matrix is asymmetric about the diagonal: this is a directed graph!\n",
    "\n",
    "(An undirected graph would be symmetric about the diagonal.)\n",
    "\n",
    "You might go on to suggest that there is some clustering happening,\n",
    "but without applying a proper clustering algorithm on the adjacency matrix,\n",
    "we would be hard-pressed to know for sure.\n",
    "After all, we can simply re-order the node ordering along the axes\n",
    "to produce a seemingly-random matrix."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Arc Plot\n",
    "\n",
    "The Arc Plot is another rational graph visualization.\n",
    "Here, we line up the nodes along a horizontal axis,\n",
    "and draw _arcs_ between nodes if they are connected by an edge.\n",
    "We can also optionally group and colour them by some metadata.\n",
    "In the case of this student graph,\n",
    "we group and colour them by \"gender\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# a = ArcPlot(G, node_color='gender', node_grouping='gender')\n",
    "nv.arc(G, node_color_by=\"gender\", group_by=\"gender\")\n",
    "annotate.arc_group(G, group_by=\"gender\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Arc Plot forms the basis of the next visualization,\n",
    "the highly popular Circos plot."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "## Circos Plot\n",
    "\n",
    "The Circos Plot was developed by [Martin Krzywinski][bccrc] at the BC Cancer Research Center. The `nxviz.CircosPlot` takes inspiration from the original by joining the two ends of the Arc Plot into a circle. Likewise, we can colour and order nodes by node metadata:\n",
    "\n",
    "[bccrc]: http://circos.ca/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "nv.circos(G, group_by=\"gender\", node_color_by=\"gender\")\n",
    "annotate.circos_group(G, group_by=\"gender\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "Generally speaking, you can think of a Circos Plot as being\n",
    "a more compact and aesthetically pleasing version of Arc Plots."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "## Hive Plot\n",
    "\n",
    "The final plot we'll show is, Hive Plots."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nxviz import plots\n",
    "import matplotlib.pyplot as plt \n",
    "\n",
    "nv.hive(G, group_by=\"gender\", node_color_by=\"gender\")\n",
    "annotate.hive_group(G, group_by=\"gender\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "As you can see, with Hive Plots,\n",
    "we first group nodes along two or three radial axes.\n",
    "In this case, we have the boys along one radial axis\n",
    "and the girls along the other.\n",
    "We can also order the nodes along each axis if we so choose to.\n",
    "In this case, no particular ordering is chosen.\n",
    "\n",
    "Next, we draw edges.\n",
    "We start first with edges _between_ groups.\n",
    "That is shown on the left side of the figure,\n",
    "joining nodes in the \"yellow\" and \"green\" (boys/girls) groups.\n",
    "We then proceed to edges _within_ groups.\n",
    "This is done by cloning the node radial axis\n",
    "before drawing edges."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Principles of Rational Graph Viz\n",
    "\n",
    "While I was implementing these visualizations in `nxviz`,\n",
    "I learned an important lesson in implementing graph visualizations in general:\n",
    "\n",
    "> To be most informative and communicative,\n",
    "> a graph visualization should first prioritize node placement\n",
    "> in a fashion that makes sense.\n",
    "\n",
    "In some ways, this makes a ton of sense.\n",
    "The nodes are the \"entities\" in a graph,\n",
    "corresponding to people, proteins, and ports.\n",
    "For \"entities\", we have natural ways to group, order and summarize (reduce).\n",
    "(An example of a \"reduction\" is counting the number of things.)\n",
    "Prioritizing node placement allows us\n",
    "to appeal to our audience's natural sense of grouping, ordering and reduction.\n",
    "\n",
    "So the next time you see a hairball,\n",
    "I hope you're able to critique it for what it doesn't communicate,\n",
    "and possibly use the same principle to design a better visualization!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/04-advanced/02-linalg.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import warnings\n",
    "\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"uTHihJiRELc\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this chapter, we will look at the relationship between graphs and linear algebra.\n",
    "\n",
    "The deep connection between these two topics is super interesting,\n",
    "and I'd like to show it to you through an exploration of three topics:\n",
    "\n",
    "1. Path finding\n",
    "1. Message passing\n",
    "1. Bipartite projections\n",
    "\n",
    "## Preliminaries\n",
    "\n",
    "Before we go deep into the linear algebra piece though,\n",
    "we have to first make sure some ideas are clear.\n",
    "\n",
    "The most important thing that we need\n",
    "when treating graphs in linear algebra form\n",
    "is the **adjacency matrix**.\n",
    "For example, for four nodes joined in a chain:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "\n",
    "nodes = list(range(4))\n",
    "G1 = nx.Graph()\n",
    "G1.add_nodes_from(nodes)\n",
    "G1.add_edges_from(zip(nodes, nodes[1:]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "we can visualize the graph:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nx.draw(G1, with_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "and we can visualize its adjacency matrix:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "\n",
    "m = nv.matrix(G1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "and we can obtain the adjacency matrix as a NumPy array:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "A1 = nx.to_numpy_array(G1, nodelist=sorted(G1.nodes()))\n",
    "A1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Symmetry\n",
    "\n",
    "Remember that for an undirected graph,\n",
    "the adjacency matrix will be symmetric about the diagonal,\n",
    "while for a directed graph,\n",
    "the adjacency matrix will be _asymmetric_."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Path finding\n",
    "\n",
    "In the Paths chapter, we can use the breadth-first search algorithm\n",
    "_to find a shortest path between any two nodes_.\n",
    "\n",
    "As it turns out, using adjacency matrices, we can answer a related question,\n",
    "which is _how many paths exist of length K between two nodes_.\n",
    "\n",
    "To see how, we need to see the relationship between matrix powers and graph path lengths.\n",
    "\n",
    "Let's take the adjacency matrix above,\n",
    "raise it to the second power,\n",
    "and see what it tells us."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "np.linalg.matrix_power(A1, 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: adjacency matrix power?\n",
    "\n",
    "> What do you think the values in the adjacency matrix are related to?\n",
    "> If studying in a group, discuss with your neighbors;\n",
    "> if working on this alone, write down your thoughts."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.linalg import adjacency_matrix_power\n",
    "from nams.functions import render_html\n",
    "\n",
    "render_html(adjacency_matrix_power())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Higher matrix powers\n",
    "\n",
    "The semantic meaning of adjacency matrix powers\n",
    "is preserved even if we go to higher powers.\n",
    "For example, if we go to the 3rd matrix power:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "np.linalg.matrix_power(A1, 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You should be able to convince yourself that:\n",
    "\n",
    "1. There's no way to go from a node back to itself in 3 steps, thus explaining the diagonals, and \n",
    "1. The off-diagonals take on the correct values when you think about them in terms of \"ways to go from one node to another\"."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### With directed graphs?\n",
    "\n",
    "Does the \"number of steps\" interpretation hold\n",
    "with directed graphs?\n",
    "Yes it does!\n",
    "Let's see it in action."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "G2 = nx.DiGraph()\n",
    "G2.add_nodes_from(nodes)\n",
    "G2.add_edges_from(zip(nodes, nodes[1:]))\n",
    "nx.draw(G2, with_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: directed graph matrix power\n",
    "\n",
    "> Convince yourself that the resulting adjacency matrix power\n",
    "> contains the same semantic meaning\n",
    "> as that for an undirected graph,\n",
    "> that is,\n",
    "> _the number of ways to go from \"row\" node to \"column\" node\n",
    "> in K steps_.\n",
    "> (I have provided three different matrix powers for you.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "A2 = nx.to_numpy_array(G2)\n",
    "np.linalg.matrix_power(A2, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "np.linalg.matrix_power(A2, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "np.linalg.matrix_power(A2, 4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Message Passing\n",
    "\n",
    "Let's now dive into the second topic here,\n",
    "that of message passing.\n",
    "\n",
    "To show how message passing works on a graph,\n",
    "let's start with the directed linear chain,\n",
    "as this will make things easier to understand.\n",
    "\n",
    "### \"Message\" representation in matrix form\n",
    "\n",
    "Our graph adjacency matrix contains nodes ordered in a particular fashion\n",
    "along the rows and columns.\n",
    "We can also create a \"message\" matrix $M$,\n",
    "using the same ordering of nodes along the rows,\n",
    "with columns instead representing a \"message\"\n",
    "that is intended to be \"passed\" from one node to another:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "M = np.array([1, 0, 0, 0])\n",
    "M"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice where the position of the value `1` is - at the first node.\n",
    "\n",
    "If we take M and matrix multiply it against A2, let's see what we get:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "M @ A2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The message has been passed onto the next node!\n",
    "And if we pass the message one more time:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "M @ A2 @ A2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, the message lies on the 3rd node!\n",
    "\n",
    "We can make an animation to visualize this more clearly. \n",
    "_There are comments in the code to explain what's going on!_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def propagate(G, msg, n_frames):\n",
    "    \"\"\"\n",
    "    Computes the node values based on propagation.\n",
    "\n",
    "    Intended to be used before or when being passed into the\n",
    "    anim() function (defined below).\n",
    "\n",
    "    :param G: A NetworkX Graph.\n",
    "    :param msg: The initial state of the message.\n",
    "    :returns: A list of 1/0 representing message status at\n",
    "        each node.\n",
    "    \"\"\"\n",
    "    # Initialize a list to store message states at each timestep.\n",
    "    msg_states = []\n",
    "\n",
    "    # Set a variable `new_msg` to be the initial message state.\n",
    "    new_msg = msg\n",
    "\n",
    "    # Get the adjacency matrix of the graph G.\n",
    "    A = nx.to_numpy_array(G)\n",
    "\n",
    "    # Perform message passing at each time step\n",
    "    for i in range(n_frames):\n",
    "        msg_states.append(new_msg)\n",
    "        new_msg = new_msg @ A\n",
    "\n",
    "    # Return the message states.\n",
    "    return msg_states"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from IPython.display import HTML\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib import animation\n",
    "\n",
    "\n",
    "def update_func(step, nodes, colors):\n",
    "    \"\"\"\n",
    "    The update function for each animation time step.\n",
    "\n",
    "    :param step: Passed in from matplotlib's FuncAnimation. Must\n",
    "        be present in the function signature.\n",
    "    :param nodes: Returned from nx.draw_networkx_edges(). Is an\n",
    "        array of colors.\n",
    "    :param colors: A list of pre-computed colors.\n",
    "    \"\"\"\n",
    "    nodes.set_array(colors[step].ravel())\n",
    "    return nodes\n",
    "\n",
    "\n",
    "def anim(G, initial_state, n_frames=4):\n",
    "    \"\"\"\n",
    "    Animation function!\n",
    "    \"\"\"\n",
    "    # First, pre-compute the message passing states over all frames.\n",
    "    colors = propagate(G, initial_state, n_frames)\n",
    "    # Instantiate a figure\n",
    "    fig = plt.figure()\n",
    "    # Precompute node positions so that they stay fixed over the entire animation\n",
    "    pos = nx.kamada_kawai_layout(G)\n",
    "    # Draw nodes to screen\n",
    "    nodes = nx.draw_networkx_nodes(\n",
    "        G, pos=pos, node_color=colors[0].ravel(), node_size=20\n",
    "    )\n",
    "    # Draw edges to screen\n",
    "    ax = nx.draw_networkx_edges(G, pos)\n",
    "    # Finally, return the animation through matplotlib.\n",
    "    return animation.FuncAnimation(\n",
    "        fig, update_func, frames=range(n_frames), fargs=(nodes, colors)\n",
    "    )\n",
    "\n",
    "\n",
    "# Initialize the message\n",
    "msg = np.zeros(len(G2))\n",
    "msg[0] = 1\n",
    "\n",
    "# Animate the graph with message propagation.\n",
    "HTML(anim(G2, msg, n_frames=4).to_html5_video())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bipartite Graphs & Matrices\n",
    "\n",
    "The section on message passing above assumed unipartite graphs, or at least graphs for which messages can be meaningfully passed between nodes. \n",
    "\n",
    "In this section, we will look at bipartite graphs. \n",
    "\n",
    "Recall from before the definition of a bipartite graph:\n",
    "\n",
    "- Nodes are separated into two partitions (hence 'bi'-'partite').\n",
    "- Edges can only occur between nodes of different partitions.\n",
    "\n",
    "Bipartite graphs have a natural matrix representation, known as the **biadjacency matrix**. Nodes on one partition are the rows, and nodes on the other partition are the columns.\n",
    "\n",
    "NetworkX's `bipartite` module provides a function for computing the biadjacency matrix of a bipartite graph."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's start by looking at a toy bipartite graph, a \"customer-product\" purchase record graph, with 4 products and 3 customers. The matrix representation might be as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Rows = customers, columns = products, 1 = customer purchased product, 0 = customer did not purchase product.\n",
    "cp_mat = np.array([[0, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From this \"bi-adjacency\" matrix, one can compute the projection onto the customers, matrix multiplying the matrix with its transpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "c_mat = cp_mat @ cp_mat.T  # c_mat means \"customer matrix\"\n",
    "c_mat"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What we get is the connectivity matrix of the customers, based on shared purchases. \n",
    "The diagonals are the degree of the customers in the original graph, \n",
    "i.e. the number of purchases they originally made, \n",
    "and the off-diagonals are the connectivity matrix, based on shared products."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To get the products matrix, we make the transposed matrix the left side of the matrix multiplication."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "p_mat = cp_mat.T @ cp_mat  # p_mat means \"product matrix\"\n",
    "p_mat"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You may now try to convince yourself that the diagonals are the number of times a customer purchased that product, and the off-diagonals are the connectivity matrix of the products, weighted by how similar two customers are."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercises \n",
    "\n",
    "In the following exercises, you will now play with a customer-product graph from Amazon. This dataset was downloaded from [UCSD's Julian McAuley's website](http://jmcauley.ucsd.edu/data/amazon/), and corresponds to the digital music dataset.\n",
    "\n",
    "This is a bipartite graph. The two partitions are:\n",
    "\n",
    "- `customers`: The customers that were doing the reviews.\n",
    "- `products`: The music that was being reviewed.\n",
    "\n",
    "In the original dataset (see the original JSON in the `datasets/` directory), they are referred to as:\n",
    "\n",
    "- `customers`: `reviewerID`\n",
    "- `products`: `asin`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "\n",
    "G_amzn = cf.load_amazon_reviews()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Remember that with bipartite graphs, it is useful to obtain nodes from one of the partitions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.bipartite import extract_partition_nodes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "customer_nodes = extract_partition_nodes(G_amzn, \"customer\")\n",
    "mat = nx.bipartite.biadjacency_matrix(G_amzn, row_order=customer_nodes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You'll notice that this matrix is extremely large! There are 5541 customers and 3568 products,\n",
    "for a total matrix size of $5541 \\times 3568 = 19770288$, but it is stored in a sparse format because only 64706 elements are filled in."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "mat"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Example: finding customers who reviewed the most number of music items.\n",
    "\n",
    "Let's find out which customers reviewed the most number of music items.\n",
    "\n",
    "To do so, you can break the problem into a few steps.\n",
    "\n",
    "First off, we compute the customer projection using matrix operations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "customer_mat = mat @ mat.T"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, get the diagonals of the customer-customer matrix. Recall here that in `customer_mat`, the diagonals correspond to the degree of the customer nodes in the bipartite matrix.\n",
    "\n",
    "SciPy sparse matrices provide a `.diagonal()` method that returns the diagonal elements."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Get the diagonal.\n",
    "degrees = customer_mat.diagonal()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, find the index of the customer that has the highest degree."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "cust_idx = np.argmax(degrees)\n",
    "cust_idx"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can verify this independently by sorting the customer nodes by degree."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import janitor\n",
    "\n",
    "# There's some pandas-fu we need to use to get this correct.\n",
    "deg = (\n",
    "    pd.Series(dict(nx.degree(G_amzn, customer_nodes)))\n",
    "    .to_frame()\n",
    "    .reset_index()\n",
    "    .rename_column(\"index\", \"customer\")\n",
    "    .rename_column(0, \"num_reviews\")\n",
    "    .sort_values(\"num_reviews\", ascending=False)\n",
    ")\n",
    "deg.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Indeed, customer 294 was the one who had the most number of reviews!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Example: finding similar customers\n",
    "\n",
    "Let's now also compute which two customers are similar, based on shared reviews. To do so involves the following steps:\n",
    "\n",
    "1. We construct a sparse matrix consisting of only the diagonals. `scipy.sparse.diags(elements)` will construct a sparse diagonal matrix based on the elements inside `elements`.\n",
    "1. Subtract the diagonals from the customer matrix projection. This yields the customer-customer similarity matrix, which should only consist of the off-diagonal elements of the customer matrix projection.\n",
    "1. Finally, get the indices where the weight (shared number of between the customers is highest. (*This code is provided for you.*)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import scipy.sparse as sp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Construct diagonal elements.\n",
    "customer_diags = sp.diags(degrees)\n",
    "# Subtract off-diagonals.\n",
    "off_diagonals = customer_mat - customer_diags\n",
    "# Compute index of most similar individuals.\n",
    "np.unravel_index(np.argmax(off_diagonals), customer_mat.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Performance: Object vs. Matrices\n",
    "\n",
    "Finally, to motivate why you might want to use matrices rather than graph objects to compute some of these statistics, let's time the two ways of getting to the same answer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Objects\n",
    "\n",
    "Let's first use NetworkX's built-in machinery to find customers that are most similar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from time import time\n",
    "\n",
    "start = time()\n",
    "\n",
    "# Compute the projection\n",
    "G_cust = nx.bipartite.weighted_projected_graph(G_amzn, customer_nodes)\n",
    "\n",
    "# Identify the most similar customers\n",
    "most_similar_customers = sorted(\n",
    "    G_cust.edges(data=True), key=lambda x: x[2][\"weight\"], reverse=True\n",
    ")[0]\n",
    "\n",
    "end = time()\n",
    "print(f\"{end - start:.3f} seconds\")\n",
    "print(f\"Most similar customers: {most_similar_customers}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Matrices\n",
    "\n",
    "Now, let's implement the same thing in matrix form."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "start = time()\n",
    "\n",
    "# Compute the projection using matrices\n",
    "mat = nx.bipartite.matrix.biadjacency_matrix(G_amzn, customer_nodes)\n",
    "cust_mat = mat @ mat.T\n",
    "\n",
    "# Identify the most similar customers\n",
    "degrees = customer_mat.diagonal()\n",
    "customer_diags = sp.diags(degrees)\n",
    "off_diagonals = customer_mat - customer_diags\n",
    "c1, c2 = np.unravel_index(np.argmax(off_diagonals), customer_mat.shape)\n",
    "\n",
    "end = time()\n",
    "print(f\"{end - start:.3f} seconds\")\n",
    "print(\n",
    "    f\"Most similar customers: {customer_nodes[c1]}, {customer_nodes[c2]}, {cust_mat[c1, c2]}\"\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "On a modern PC, the matrix computation should be about 10-50X faster\n",
    "using the matrix form compared to the object-oriented form.\n",
    "(The web server that is used to build the book\n",
    "might not necessarily have the software stack to do this though,\n",
    "so the time you see reported might not reflect the expected speedups.)\n",
    "I'd encourage you to fire up a Binder session or clone the book locally \n",
    "to test out the code yourself.\n",
    "\n",
    "You may notice that it's much easier to read the \"objects\" code, \n",
    "but the matrix code way outperforms the object code. \n",
    "This tradeoff is common in computing, and shouldn't surprise you.\n",
    "That said, the speed gain alone is a great reason to use matrices!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Acceleration on a GPU\n",
    "\n",
    "If your appetite has been whipped up for even more acceleration\n",
    "and you have a GPU on your daily compute,\n",
    "then you're very much in luck!\n",
    "\n",
    "The [RAPIDS.AI](https://rapids.ai) project has a package called [cuGraph](https://github.com/rapidsai/cugraph),\n",
    "which provides GPU-accelerated graph algorithms.\n",
    "As over release 0.16.0, all cuGraph algorithms will be able to accept NetworkX graph objects!\n",
    "This came about through online conversations on GitHub and Twitter,\n",
    "which for us, personally, speaks volumes to the power of open source projects!\n",
    "\n",
    "Because cuGraph does presume that you have access to a GPU,\n",
    "and because we assume most readers of this book might not have access to one easily,\n",
    "we'll delegate teaching how to install and use cuGraph to the cuGraph devs and [their documentation][docs].\n",
    "Nonetheless, if you do have the ability to install and use the RAPIDS stack,\n",
    "definitely check it out!\n",
    "\n",
    "[docs]: https://docs.rapids.ai/api/cugraph/stable/api.html"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/04-advanced/03-stats.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"P-0CJpO3spg\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this chapter, we are going to take a look at how to perform statistical inference on graphs."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Statistics refresher\n",
    "\n",
    "Before we can proceed with statistical inference on graphs,\n",
    "we must first refresh ourselves with some ideas from the world of statistics.\n",
    "Otherwise, the methods that we will end up using\n",
    "may seem a tad _weird_, and hence difficult to follow along.\n",
    "\n",
    "To review statistical ideas,\n",
    "let's set up a few statements and explore what they mean."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## We are concerned with models of randomness\n",
    "\n",
    "As with all things statistics, we are concerned with models of randomness.\n",
    "Here, probability distributions give us a way to think about random events\n",
    "and how to assign credibility points to them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### In an abstract fashion...\n",
    "\n",
    "The supremely abstract way of thinking about a probability distribution\n",
    "is that it is the space of all possibilities of \"stuff\"\n",
    "with different credibility points _distributed_ amongst each possible \"thing\"."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### More concretely: the coin flip\n",
    "\n",
    "A more concrete example is to consider the coin flip.\n",
    "Here, the space of all possibilities of \"stuff\" is the set of \"heads\" and \"tails\".\n",
    "If we have a fair coin, then we have 0.5 credibility points _distributed_\n",
    "to each of \"heads\" and \"tails\"."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Another example: dice rolls\n",
    "\n",
    "Another concrete example is to consider the six-sided dice.\n",
    "Here, the space of all possibilities of \"stuff\" is the set of numbers in the range $[1, 6]$.\n",
    "If we have a fair dice, then we have 1/6 credibility points assigned\n",
    "to each of the numbers.\n",
    "(Unfair dice will have an unequal _distribution_ of credibility points across each face.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### A graph-based example: social networks\n",
    "\n",
    "If we receive an undirected social network graph with 5 nodes and 6 edges,\n",
    "we have to keep in mind that this graph with 6 edges\n",
    "was merely one of $15 \\choose 6$ ways to construct 5 node, 6 edge graphs.\n",
    "(15 comes up because there are 15 edges that can be constructed in a 5-node undirected graph.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hypothesis Testing\n",
    "\n",
    "A commonplace task in statistical inferences\n",
    "is calculating the probability of observing a value or something more extreme\n",
    "under an assumed \"null\" model of reality.\n",
    "This is what we commonly call \"hypothesis testing\",\n",
    "and where the oft-misunderstood term \"p-value\" shows up."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hypothesis testing in coin flips, by simulation\n",
    "\n",
    "As an example, hypothesis testing in coin flips follows this logic:\n",
    "\n",
    "- I observe that 8 out of 10 coin tosses give me heads, giving me a probability of heads $p=0.8$ (a summary statistic).\n",
    "- Under a \"null distribution\" of a fair coin, I simulate the distribution of probability of heads (the summary statistic) that I would get from 10 coin tosses.\n",
    "- Finally, I use that distribution to calculate the probability of observing $p=0.8$ or more extreme."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hypothesis testing in graphs\n",
    "\n",
    "The same protocol applies when we perform hypothesis testing on graphs.\n",
    "\n",
    "Firstly, we calculate a _summary statistic_ that describes our graph.\n",
    "\n",
    "Secondly, we propose a _null graph model_, and calculate our summary statistic under simulated versions of that null graph model.\n",
    "\n",
    "Thirdly, we look at the probability of observing the summary statistic value that we calculated in step 1 or more extreme, under the assumed graph null model distribution."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Stochastic graph creation models\n",
    "\n",
    "Since we are going to be dealing with models of randomness in graphs,\n",
    "let's take a look at some examples."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Erdos-Renyi (a.k.a. \"binomial\") graph\n",
    "\n",
    "On easy one to study is the Erdos-Renyi graph, also known as the \"binomial\" graph.\n",
    "\n",
    "The data generation story here is that we instantiate an undirected graph with $n$ nodes,\n",
    "giving $\\frac{n^2 - n}{2}$ possible edges.\n",
    "Each edge has a probability $p$ of being created."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "\n",
    "\n",
    "G_er = nx.erdos_renyi_graph(n=30, p=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nx.draw(G_er)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can verify that there's approximately 20% of $\\frac{30^2 - 30}{2} = 435$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(G_er.edges())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(G_er.edges()) / 435"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also look at the degree distribution:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from nams.functions import ecdf\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "x, y = ecdf(pd.Series(dict(nx.degree(G_er))))\n",
    "plt.scatter(x, y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Barabasi-Albert Graph\n",
    "\n",
    "The data generating story of this graph generator is essentially that nodes that have lots of edges preferentially get new edges attached onto them. \n",
    "This is what we call a \"preferential attachment\" process."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "G_ba = nx.barabasi_albert_graph(n=30, m=3)\n",
    "nx.draw(G_ba)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(G_ba.edges())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And the degree distribution:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x, y = ecdf(pd.Series(dict(nx.degree(G_ba))))\n",
    "plt.scatter(x, y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can see that even though the number of edges between the two graphs are similar,\n",
    "their degree distribution is wildly different."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Load Data\n",
    "\n",
    "For this notebook, we are going to look at a protein-protein interaction network,\n",
    "and test the hypothesis that this network was _not_ generated by the data generating process\n",
    "described by an Erdos-Renyi graph.\n",
    "\n",
    "Let's load a [protein-protein interaction network dataset](http://konect.cc/networks/moreno_propro).\n",
    "\n",
    "> This undirected network contains protein interactions contained in yeast.\n",
    "> Research showed that proteins with a high degree\n",
    "> were more important for the surivial of the yeast than others.\n",
    "> A node represents a protein and an edge represents a metabolic interaction between two proteins. \n",
    "> The network contains loops."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "\n",
    "G = cf.load_propro_network()\n",
    "for n, d in G.nodes(data=True):\n",
    "    G.nodes[n][\"degree\"] = G.degree(n)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As is always the case, let's make sure we know some basic stats of the graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "len(G.nodes())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "len(G.edges())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's also examine the degree distribution of the graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x, y = ecdf(pd.Series(dict(nx.degree(G))))\n",
    "plt.scatter(x, y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, we should visualize the graph to get a feel for it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "from nxviz import annotate\n",
    "\n",
    "nv.circos(\n",
    "    G, sort_by=\"degree\", node_color_by=\"degree\", node_enc_kwargs={\"size_scale\": 10}\n",
    ")\n",
    "annotate.node_colormapping(G, color_by=\"degree\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "One thing we might infer from this visualization\n",
    "is that the vast majority of nodes have a very small degree,\n",
    "while a very small number of nodes have a high degree.\n",
    "That would prompt us to think:\n",
    "what process could be responsible for generating this graph?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Inferring Graph Generating Model\n",
    "\n",
    "Given a graph dataset, how do we identify which data generating model provides the best fit?\n",
    "\n",
    "One way to do this is to compare characteristics of a graph generating model against the characteristics of the graph.\n",
    "The logic here is that if we have a good graph generating model for the data,\n",
    "we should, in theory, observe the observed graph's characteristics\n",
    "in the graphs generated by the graph generating model."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Comparison of degree distribution\n",
    "\n",
    "Let's compare the degree distribution between the data, a few Erdos-Renyi graphs, and a few Barabasi-Albert graphs."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Comparison with Barabasi-Albert graphs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from ipywidgets import interact, IntSlider\n",
    "\n",
    "m = IntSlider(value=2, min=1, max=10)\n",
    "\n",
    "\n",
    "@interact(m=m)\n",
    "def compare_barabasi_albert_graph(m):\n",
    "    fig, ax = plt.subplots()\n",
    "    G_ba = nx.barabasi_albert_graph(n=len(G.nodes()), m=m)\n",
    "    x, y = ecdf(pd.Series(dict(nx.degree(G_ba))))\n",
    "    ax.scatter(x, y, label=\"Barabasi-Albert Graph\")\n",
    "\n",
    "    x, y = ecdf(pd.Series(dict(nx.degree(G))))\n",
    "    ax.scatter(x, y, label=\"Protein Interaction Network\")\n",
    "    ax.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Comparison with Erdos-Renyi graphs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from ipywidgets import FloatSlider\n",
    "\n",
    "p = FloatSlider(value=0.6, min=0, max=0.1, step=0.001)\n",
    "\n",
    "\n",
    "@interact(p=p)\n",
    "def compare_erdos_renyi_graph(p):\n",
    "    fig, ax = plt.subplots()\n",
    "    G_er = nx.erdos_renyi_graph(n=len(G.nodes()), p=p)\n",
    "    x, y = ecdf(pd.Series(dict(nx.degree(G_er))))\n",
    "    ax.scatter(x, y, label=\"Erdos-Renyi Graph\")\n",
    "\n",
    "    x, y = ecdf(pd.Series(dict(nx.degree(G))))\n",
    "    ax.scatter(x, y, label=\"Protein Interaction Network\")\n",
    "    ax.legend()\n",
    "    ax.set_title(f\"p={p}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the degree distribution only, which model do you think better describes the generation of a protein-protein interaction network?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Quantitative Model Comparison\n",
    "\n",
    "Each time we plug in a value of $m$ for the Barabasi-Albert graph model, we are using one of many possible Barabasi-Albert graph models, each with a different $m$.\n",
    "Similarly, each time we choose a different $p$ for the Erdos-Renyi model, we are using one of many possible Erdos-Renyi graph models, each with a different $p$.\n",
    "\n",
    "To quantitatively compare degree distributions, we can use the [Wasserstein distance][wasd] between the data.\n",
    "Let's see how to implement this.\n",
    "\n",
    "[wasd]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import wasserstein_distance\n",
    "\n",
    "\n",
    "def erdos_renyi_degdist(n, p):\n",
    "    \"\"\"Return a Pandas series of degree distribution of an Erdos-Renyi graph.\"\"\"\n",
    "    G = nx.erdos_renyi_graph(n=n, p=p)\n",
    "    return pd.Series(dict(nx.degree(G)))\n",
    "\n",
    "\n",
    "def barabasi_albert_degdist(n, m):\n",
    "    \"\"\"Return a Pandas series of degree distribution of an Barabasi-Albert graph.\"\"\"\n",
    "    G = nx.barabasi_albert_graph(n=n, m=m)\n",
    "    return pd.Series(dict(nx.degree(G)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "deg = pd.Series(dict(nx.degree(G)))\n",
    "\n",
    "er_deg = erdos_renyi_degdist(n=len(G.nodes()), p=0.001)\n",
    "ba_deg = barabasi_albert_degdist(n=len(G.nodes()), m=1)\n",
    "wasserstein_distance(deg, er_deg), wasserstein_distance(deg, ba_deg)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that because the graphs are instantiated in a non-deterministic fashion, re-running the cell above will give you different values for each new graph generated.\n",
    "\n",
    "Let's now plot the wasserstein distance to our graph data for the two particular Erdos-Renyi and Barabasi-Albert graph models shown above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from tqdm.autonotebook import tqdm\n",
    "\n",
    "er_dist = []\n",
    "ba_dist = []\n",
    "for _ in tqdm(range(100)):\n",
    "    er_deg = erdos_renyi_degdist(n=len(G.nodes()), p=0.001)\n",
    "    er_dist.append(wasserstein_distance(deg, er_deg))\n",
    "\n",
    "    ba_deg = barabasi_albert_degdist(n=len(G.nodes()), m=1)\n",
    "    ba_dist.append(wasserstein_distance(deg, ba_deg))\n",
    "\n",
    "# er_degs = [erdos_renyi_degdist(n=len(G.nodes()), p=0.001) for _ in range(100)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "import janitor\n",
    "\n",
    "\n",
    "data = (\n",
    "    pd.DataFrame(\n",
    "        {\n",
    "            \"Erdos-Renyi\": er_dist,\n",
    "            \"Barabasi-Albert\": ba_dist,\n",
    "        }\n",
    "    )\n",
    "    .melt(value_vars=[\"Erdos-Renyi\", \"Barabasi-Albert\"])\n",
    "    .rename_columns({\"variable\": \"Graph Model\", \"value\": \"Wasserstein Distance\"})\n",
    ")\n",
    "sns.swarmplot(data=data, x=\"Graph Model\", y=\"Wasserstein Distance\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From this, we might conclude that the Barabasi-Albert graph with $m=1$ has the better fit to the protein-protein interaction network graph."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Interpretation\n",
    "\n",
    "That statement, accurate as it might be, still does not connect the dots to _biology_.\n",
    "\n",
    "Let's think about the generative model for this graph.\n",
    "The Barabasi-Albert graph gives us a model for \"rich gets richer\".\n",
    "Given the current state of the graph,\n",
    "if we want to add a new edge, we first pick a node with probability proportional to\n",
    "the number of edges it already has.\n",
    "Then, we pick another node with probability proportional to the number of edges that it has too.\n",
    "Finally, we add an edge there.\n",
    "This has the effect of \"enriching\" nodes that have a large number of edges with more edges.\n",
    "\n",
    "How might this connect to biology?\n",
    "\n",
    "We can't necessarily provide a concrete answer, but this model might help raise new hypotheses.\n",
    "\n",
    "For example, if protein-protein interactions of the \"binding\" kind\n",
    "are driven by subdomains, then proteins that acquire a domain through recombination\n",
    "may end up being able to bind to everything else that the domain was able to.\n",
    "In this fashion, proteins with that particular binding domain\n",
    "gain new edges more readily.\n",
    "\n",
    "Testing these hypotheses would be a totally different matter, and at this point,\n",
    "I submit the above hypothesis with a large amount of salt thrown over my shoulder.\n",
    "In other words, the hypothesized mechanism could be completely wrong.\n",
    "However, I hope that this example illustrated that\n",
    "the usage of a \"graph generative model\" can help us narrow down hypotheses about the observed world."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/04-advanced/01-bipartite.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import warnings\n",
    "\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"BYOK12I9vgI\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this chapter, we will look at bipartite graphs and their applications.\n",
    "\n",
    "## What are bipartite graphs?\n",
    "\n",
    "As the name suggests,\n",
    "bipartite have two (bi) node partitions (partite).\n",
    "In other words, we can assign nodes to one of the two partitions.\n",
    "(By contrast, all of the graphs that we have seen before are _unipartite_:\n",
    "they only have a single partition.)\n",
    "\n",
    "### Rules for bipartite graphs\n",
    "\n",
    "With unipartite graphs, you might remember a few rules that apply.\n",
    "\n",
    "Firstly, nodes and edges belong to a _set_.\n",
    "This means the node set contains only unique members,\n",
    "i.e. no node can be duplicated.\n",
    "The same applies for the edge set.\n",
    "\n",
    "On top of those two basic rules, bipartite graphs add an additional rule:\n",
    "Edges can only occur between nodes of **different** partitions.\n",
    "In other words, nodes within the same partition \n",
    "are not allowed to be connected to one another.\n",
    "\n",
    "### Applications of bipartite graphs\n",
    "\n",
    "Where do we see bipartite graphs being used?\n",
    "Here's one that is very relevant to e-commerce,\n",
    "which touches our daily lives:\n",
    "\n",
    "> We can model customer purchases of products using a bipartite graph.\n",
    "> Here, the two node sets are **customer** nodes and **product** nodes,\n",
    "> and edges indicate that a customer $C$ purchased a product $P$.\n",
    "\n",
    "On the basis of this graph, we can do interesting analyses,\n",
    "such as finding customers that are similar to one another\n",
    "on the basis of their shared product purchases.\n",
    "\n",
    "Can you think of other situations\n",
    "where a bipartite graph model can be useful?\n",
    "\n",
    "## Dataset\n",
    "\n",
    "Here's another application in crime analysis,\n",
    "which is relevant to the example that we will use in this chapter:\n",
    "\n",
    "> This bipartite network contains persons\n",
    "> who appeared in at least one crime case \n",
    "> as either a suspect, a victim, a witness \n",
    "> or both a suspect and victim at the same time. \n",
    "> A left node represents a person and a right node represents a crime. \n",
    "> An edge between two nodes shows that \n",
    "> the left node was involved in the crime \n",
    "> represented by the right node.\n",
    "\n",
    "This crime dataset was also sourced from Konect."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams import load_data as cf\n",
    "\n",
    "G = cf.load_crime_network()\n",
    "for n, d in G.nodes(data=True):\n",
    "    G.nodes[n][\"degree\"] = G.degree(n)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you inspect the nodes,\n",
    "you will see that they contain a special metadata keyword: `bipartite`.\n",
    "This is a special keyword that NetworkX can use \n",
    "to identify nodes of a given partition."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Visualize the crime network\n",
    "\n",
    "To help us get our bearings right, let's visualize the crime network."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(7, 7))\n",
    "nv.circos(\n",
    "    G,\n",
    "    sort_by=\"degree\",\n",
    "    group_by=\"bipartite\",\n",
    "    node_color_by=\"bipartite\",\n",
    "    node_enc_kwargs={\"size_scale\": 3},\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Extract each node set\n",
    "\n",
    "A useful thing to be able to do\n",
    "is to extract each partition's node set.\n",
    "This will become handy when interacting with\n",
    "NetworkX's bipartite algorithms later on.\n",
    "\n",
    "> Write a function that extracts all of the nodes \n",
    "> from specified node partition.\n",
    "> It should also raise a plain Exception\n",
    "> if no nodes exist in that specified partition.\n",
    "> (as a precuation against users putting in invalid partition names)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "\n",
    "\n",
    "def extract_partition_nodes(G: nx.Graph, partition: str):\n",
    "    nodeset = [_ for _, _ in _______ if ____________]\n",
    "    if _____________:\n",
    "        raise Exception(f\"No nodes exist in the partition {partition}!\")\n",
    "    return nodeset\n",
    "\n",
    "\n",
    "from nams.solutions.bipartite import extract_partition_nodes\n",
    "\n",
    "# Uncomment the next line to see the answer.\n",
    "# extract_partition_nodes??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bipartite Graph Projections\n",
    "\n",
    "In a bipartite graph, one task that can be useful to do\n",
    "is to calculate the projection of a graph onto one of its nodes.\n",
    "\n",
    "What do we mean by the \"projection of a graph\"?\n",
    "It is best visualized using this figure:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.bipartite import (\n",
    "    draw_bipartite_graph_example,\n",
    "    bipartite_example_graph,\n",
    ")\n",
    "from nxviz import annotate\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "bG = bipartite_example_graph()\n",
    "pG = nx.bipartite.projection.projected_graph(bG, \"abcd\")\n",
    "ax = draw_bipartite_graph_example()\n",
    "plt.sca(ax[0])\n",
    "annotate.parallel_labels(bG, group_by=\"bipartite\")\n",
    "plt.sca(ax[1])\n",
    "annotate.arc_labels(pG)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As shown in the figure above, we start first with a bipartite graph with two node sets,\n",
    "the \"alphabet\" set and the \"numeric\" set.\n",
    "The projection of this bipartite graph onto the \"alphabet\" node set\n",
    "is a graph that is constructed such that it only contains the \"alphabet\" nodes,\n",
    "and edges join the \"alphabet\" nodes because they share a connection to a \"numeric\" node.\n",
    "The red edge on the right\n",
    "is basically the red path traced on the left."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Computing graph projections\n",
    "\n",
    "How does one compute graph projections using NetworkX?\n",
    "Turns out, NetworkX has a `bipartite` submodule,\n",
    "which gives us all of the facilities that we need\n",
    "to interact with bipartite algorithms.\n",
    "\n",
    "First of all, we need to check that the graph\n",
    "is indeed a bipartite graph.\n",
    "NetworkX provides a function for us to do so:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from networkx.algorithms import bipartite\n",
    "\n",
    "bipartite.is_bipartite(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we've confirmed that the graph is indeed bipartite,\n",
    "we can use the NetworkX bipartite submodule functions\n",
    "to generate the bipartite projection onto one of the node partitions.\n",
    "\n",
    "First off, we need to extract nodes from a particular partition."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "person_nodes = extract_partition_nodes(G, \"person\")\n",
    "crime_nodes = extract_partition_nodes(G, \"crime\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we can compute the projection:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "person_graph = bipartite.projected_graph(G, person_nodes)\n",
    "crime_graph = bipartite.projected_graph(G, crime_nodes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And with that, we have our projected graphs!\n",
    "\n",
    "Go ahead and inspect them:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "list(person_graph.edges(data=True))[0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "list(crime_graph.edges(data=True))[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, what is the _interpretation_ of these projected graphs?\n",
    "\n",
    "- For `person_graph`, we have found _individuals who are linked by shared participation (whether witness or suspect) in a crime._\n",
    "- For `crime_graph`, we have found _crimes that are linked by shared involvement by people._\n",
    "\n",
    "Just by this graph, we already can find out pretty useful information.\n",
    "Let's use an exercise that leverages what you already know\n",
    "to extract useful information from the projected graph."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: find the crime(s) that have the most shared connections with other crimes\n",
    "\n",
    "> Find crimes that are most similar to one another\n",
    "> on the basis of the number of shared connections to individuals.\n",
    "\n",
    "_Hint: This is a degree centrality problem!_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "def find_most_similar_crimes(cG: nx.Graph):\n",
    "    \"\"\"\n",
    "    Find the crimes that are most similar to other crimes.\n",
    "    \"\"\"\n",
    "    dcs = ______________\n",
    "    return ___________________\n",
    "\n",
    "\n",
    "from nams.solutions.bipartite import find_most_similar_crimes\n",
    "\n",
    "find_most_similar_crimes(crime_graph)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: find the individual(s) that have the most shared connections with other individuals\n",
    "\n",
    "> Now do the analogous thing for individuals!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def find_most_similar_people(pG: nx.Graph):\n",
    "    \"\"\"\n",
    "    Find the persons that are most similar to other persons.\n",
    "    \"\"\"\n",
    "    dcs = ______________\n",
    "    return ___________________\n",
    "\n",
    "\n",
    "from nams.solutions.bipartite import find_most_similar_people\n",
    "\n",
    "find_most_similar_people(person_graph)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Weighted Projection\n",
    "\n",
    "Though we were able to find out which graphs were connected with one another,\n",
    "we did not record in the resulting projected graph\n",
    "the **strength** by which the two nodes were connected.\n",
    "To preserve this information, we need another function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "weighted_person_graph = bipartite.weighted_projected_graph(G, person_nodes)\n",
    "list(weighted_person_graph.edges(data=True))[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Find the people that can help with investigating a `crime`'s `person`.\n",
    "\n",
    "Let's pretend that we are a detective trying to solve a crime,\n",
    "and that we right now need to find other individuals\n",
    "who were not implicated in the same _exact_ crime as an individual was,\n",
    "but who might be able to give us information about that individual\n",
    "because they were implicated in other crimes with that individual.\n",
    "\n",
    "> Implement a function that takes in a bipartite graph `G`, a string `person` and a string `crime`,\n",
    "> and returns a list of other `person`s that were **not** implicated in the `crime`,\n",
    "> but were connected to the `person` via other crimes.\n",
    "> It should return a _ranked list_,\n",
    "> based on the **number of shared crimes** (from highest to lowest)\n",
    "> because the ranking will help with triage."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "list(G.neighbors(\"p1\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def find_connected_persons(G, person, crime):\n",
    "    # Step 0: Check that the given \"person\" and \"crime\" are connected.\n",
    "    if _____________________________:\n",
    "        raise ValueError(\n",
    "            f\"Graph does not have a connection between {person} and {crime}!\"\n",
    "        )\n",
    "\n",
    "    # Step 1: calculate weighted projection for person nodes.\n",
    "    person_nodes = ____________________________________\n",
    "    person_graph = bipartite.________________________(_, ____________)\n",
    "\n",
    "    # Step 2: Find neighbors of the given `person` node in projected graph.\n",
    "    candidate_neighbors = ___________________________________\n",
    "\n",
    "    # Step 3: Remove candidate neighbors from the set if they are implicated in the given crime.\n",
    "    for p in G.neighbors(crime):\n",
    "        if ________________________:\n",
    "            _____________________________\n",
    "\n",
    "    # Step 4: Rank-order the candidate neighbors by number of shared connections.\n",
    "    _________ = []\n",
    "    ## You might need a for-loop here\n",
    "    return pd.DataFrame(__________).sort_values(\"________\", ascending=False)\n",
    "\n",
    "\n",
    "from nams.solutions.bipartite import find_connected_persons\n",
    "\n",
    "find_connected_persons(G, \"p2\", \"c10\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Degree Centrality\n",
    "\n",
    "The degree centrality metric is something we can calculate for bipartite graphs.\n",
    "Recall that the degree centrality metric is the number of neighbors of a node\n",
    "divided by the total number of _possible_ neighbors.\n",
    "\n",
    "In a unipartite graph, the denominator can be the total number of nodes less one\n",
    "(if self-loops are not allowed)\n",
    "or simply the total number of nodes (if self loops _are_ allowed).\n",
    "\n",
    "### Exercise: What is the denominator for bipartite graphs?\n",
    "\n",
    "Think about it for a moment, then write down your answer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions.bipartite import bipartite_degree_centrality_denominator\n",
    "from nams.functions import render_html\n",
    "\n",
    "render_html(bipartite_degree_centrality_denominator())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: Which `persons` are implicated in the most number of crimes?\n",
    "\n",
    "> Find the `persons` (singular or plural) who are connected to the most number of crimes.\n",
    "\n",
    "To do so, you will need to use `nx.bipartite.degree_centrality`,\n",
    "rather than the regular `nx.degree_centrality` function.\n",
    "\n",
    "`nx.bipartite.degree_centrality` requires that you pass in\n",
    "a node set from one of the partitions\n",
    "so that it can correctly partition nodes on the other set.\n",
    "What is returned, though, is the degree centrality\n",
    "for nodes in both sets.\n",
    "Here is an example to show you how the function is used:\n",
    "\n",
    "```python\n",
    "dcs = nx.bipartite.degree_centrality(my_graph, nodes_from_one_partition)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def find_most_crime_person(G, person_nodes):\n",
    "    dcs = __________________________\n",
    "    return ___________________________\n",
    "\n",
    "\n",
    "from nams.solutions.bipartite import find_most_crime_person\n",
    "\n",
    "find_most_crime_person(G, person_nodes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solutions\n",
    "\n",
    "Here are the solutions to the exercises above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions import bipartite\n",
    "import inspect\n",
    "\n",
    "print(inspect.getsource(bipartite))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/04-advanced/figures/bipartite-projection.svg`:

```svg
<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.2" baseProfile="tiny" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 612 415" xml:space="preserve">
<g>
	<line fill="none" stroke="#ED1C24" stroke-miterlimit="10" x1="89.6" y1="62.3" x2="266.7" y2="62.3"/>
	<line fill="none" stroke="#ED1C24" stroke-miterlimit="10" x1="89.6" y1="103.5" x2="266.7" y2="62.3"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="89.6" y1="144.6" x2="266.7" y2="103.5"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="89.6" y1="144.6" x2="266.7" y2="144.6"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="89.6" y1="185.8" x2="266.7" y2="62.3"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="89.6" y1="103.5" x2="266.7" y2="144.6"/>
	<g>
		<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="89.6" cy="144.6" r="15.4"/>
	</g>
	<g>
		<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="89.6" cy="62.3" r="15.4"/>
		<text transform="matrix(1 0 0 1 86.7242 65.8196)" font-family="'MyriadPro-Regular'" font-size="12px">a</text>
	</g>
	<g>
		<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="89.6" cy="103.5" r="15.4"/>
		<text transform="matrix(1 0 0 1 86.2022 106.9816)" font-family="'MyriadPro-Regular'" font-size="12px">b</text>
	</g>
	<text transform="matrix(1 0 0 1 86.9281 148.1436)" font-family="'MyriadPro-Regular'" font-size="12px">c</text>
	<g>
		<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="89.6" cy="185.8" r="15.4"/>
		<text transform="matrix(1 0 0 1 86.232 189.3056)" font-family="'MyriadPro-Regular'" font-size="12px">d</text>
	</g>
	<g>
		<rect x="251.3" y="46.9" fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" width="30.8" height="30.8"/>
		<text transform="matrix(1 0 0 1 263.6331 65.8196)" font-family="'MyriadPro-Regular'" font-size="12px">1</text>
	</g>
	<g>
		<rect x="251.3" y="88.1" fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" width="30.8" height="30.8"/>
		<text transform="matrix(1 0 0 1 263.6331 106.9816)" font-family="'MyriadPro-Regular'" font-size="12px">2</text>
	</g>
	<g>
		<rect x="251.3" y="129.2" fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" width="30.8" height="30.8"/>
		<text transform="matrix(1 0 0 1 263.6331 148.1436)" font-family="'MyriadPro-Regular'" font-size="12px">3</text>
	</g>
</g>
<g>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="405.2" y1="62.3" x2="479.8" y2="136.9"/>
	<line fill="none" stroke="#ED1C24" stroke-miterlimit="10" x1="405.2" y1="62.3" x2="479.8" y2="62.3"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="405.2" y1="136.9" x2="479.8" y2="62.3"/>
	<g>
		<g>
			<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="405.2" cy="62.3" r="15.4"/>
			<text transform="matrix(1 0 0 1 402.3443 65.8196)" font-family="'MyriadPro-Regular'" font-size="12px">a</text>
		</g>
		<g>
			<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="479.8" cy="62.3" r="15.4"/>
			<text transform="matrix(1 0 0 1 476.3851 65.8196)" font-family="'MyriadPro-Regular'" font-size="12px">b</text>
		</g>
		<g>
			<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="405.2" cy="136.9" r="15.4"/>
			<text transform="matrix(1 0 0 1 402.5482 140.3823)" font-family="'MyriadPro-Regular'" font-size="12px">c</text>
		</g>
		<g>
			<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="479.8" cy="136.9" r="15.4"/>
			<text transform="matrix(1 0 0 1 476.4149 140.3823)" font-family="'MyriadPro-Regular'" font-size="12px">d</text>
		</g>
	</g>
</g>
<text transform="matrix(1 0 0 1 156.7497 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">B</text>
<text transform="matrix(1 0 0 1 163.2536 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">i</text>
<text transform="matrix(1 0 0 1 166.0618 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">p</text>
<text transform="matrix(1 0 0 1 172.8894 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">a</text>
<text transform="matrix(1 0 0 1 178.6731 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">r</text>
<text transform="matrix(1 0 0 1 182.885 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">t</text>
<text transform="matrix(1 0 0 1 186.8572 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">i</text>
<text transform="matrix(1 0 0 1 189.6648 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">t</text>
<text transform="matrix(1 0 0 1 193.5647 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">e</text>
<text transform="matrix(1 0 0 1 416.9817 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">P</text>
<text transform="matrix(1 0 0 1 423.1736 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">r</text>
<text transform="matrix(1 0 0 1 426.9778 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">o</text>
<text transform="matrix(1 0 0 1 433.5657 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">j</text>
<text transform="matrix(1 0 0 1 436.4817 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">e</text>
<text transform="matrix(1 0 0 1 442.4934 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">c</text>
<text transform="matrix(1 0 0 1 448.0251 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">t</text>
<text transform="matrix(1 0 0 1 451.9973 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">i</text>
<text transform="matrix(1 0 0 1 454.8054 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">o</text>
<text transform="matrix(1 0 0 1 461.3933 30.5137)" font-family="'MyriadPro-Regular'" font-size="12px">n</text>
<g>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="89.6" y1="257.2" x2="266.7" y2="257.2"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="89.6" y1="298.3" x2="266.7" y2="257.2"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="89.6" y1="339.5" x2="266.7" y2="298.3"/>
	<line fill="none" stroke="#ED1C24" stroke-miterlimit="10" x1="89.6" y1="339.5" x2="266.7" y2="339.5"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="89.6" y1="380.6" x2="266.7" y2="257.2"/>
	<line fill="none" stroke="#ED1C24" stroke-miterlimit="10" x1="89.6" y1="298.3" x2="266.7" y2="339.5"/>
	<g>
		<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="89.6" cy="339.5" r="15.4"/>
	</g>
	<g>
		<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="89.6" cy="257.2" r="15.4"/>
		<text transform="matrix(1 0 0 1 86.7242 260.6728)" font-family="'MyriadPro-Regular'" font-size="12px">a</text>
	</g>
	<g>
		<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="89.6" cy="298.3" r="15.4"/>
		<text transform="matrix(1 0 0 1 86.2022 301.8348)" font-family="'MyriadPro-Regular'" font-size="12px">b</text>
	</g>
	<text transform="matrix(1 0 0 1 86.9281 342.9968)" font-family="'MyriadPro-Regular'" font-size="12px">c</text>
	<g>
		<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="89.6" cy="380.6" r="15.4"/>
		<text transform="matrix(1 0 0 1 86.232 384.1588)" font-family="'MyriadPro-Regular'" font-size="12px">d</text>
	</g>
	<g>
		<rect x="251.3" y="241.7" fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" width="30.8" height="30.8"/>
		<text transform="matrix(1 0 0 1 263.6331 260.6728)" font-family="'MyriadPro-Regular'" font-size="12px">1</text>
	</g>
	<g>
		<rect x="251.3" y="282.9" fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" width="30.8" height="30.8"/>
		<text transform="matrix(1 0 0 1 263.6331 301.8348)" font-family="'MyriadPro-Regular'" font-size="12px">2</text>
	</g>
	<g>
		<rect x="251.3" y="324.1" fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" width="30.8" height="30.8"/>
		<text transform="matrix(1 0 0 1 263.6331 342.9968)" font-family="'MyriadPro-Regular'" font-size="12px">3</text>
	</g>
</g>
<g>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="405.2" y1="257.2" x2="479.8" y2="331.7"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="405.2" y1="257.2" x2="479.8" y2="257.2"/>
	<line fill="none" stroke="#ED1C24" stroke-miterlimit="10" x1="405.2" y1="331.7" x2="479.8" y2="257.2"/>
	<g>
		<g>
			<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="405.2" cy="257.2" r="15.4"/>
			<text transform="matrix(1 0 0 1 402.3443 260.6728)" font-family="'MyriadPro-Regular'" font-size="12px">a</text>
		</g>
		<g>
			<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="479.8" cy="257.2" r="15.4"/>
			<text transform="matrix(1 0 0 1 476.3851 260.6728)" font-family="'MyriadPro-Regular'" font-size="12px">b</text>
		</g>
		<g>
			<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="405.2" cy="331.7" r="15.4"/>
			<text transform="matrix(1 0 0 1 402.5482 335.2355)" font-family="'MyriadPro-Regular'" font-size="12px">c</text>
		</g>
		<g>
			<circle fill="#FFFFFF" stroke="#000000" stroke-miterlimit="10" cx="479.8" cy="331.7" r="15.4"/>
			<text transform="matrix(1 0 0 1 476.4149 335.2355)" font-family="'MyriadPro-Regular'" font-size="12px">d</text>
		</g>
	</g>
</g>
<g>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="23.9" y1="221.5" x2="24.9" y2="221.5"/>

		<line fill="none" stroke="#000000" stroke-miterlimit="10" stroke-dasharray="1.9952,1.9952" x1="26.9" y1="221.5" x2="580.6" y2="221.5"/>
	<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="581.6" y1="221.5" x2="582.6" y2="221.5"/>
</g>
</svg>

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/index.md`:

```md
Hey, thanks for stopping by!

Network Analysis Made Simple is a collection of Jupyter notebooks
designed to help you get up and running with the NetworkX package
in the Python programming langauge.
It's written by programmers for programmers,
and will give you a basic introduction to
graph theory, applied network science,
and advanced topics to help kickstart your learning journey.
There's even case studies to help those of you
for whom example narratives help a ton!

We hope you enjoy learning from it.

## Introduction Videos

At the beginning of each "chapter",
there's an introduction video just like the one you'll see embedded below.
Those videos will give you an overview of the chapter,
particularly what to look out for and what the learning goals are,
and are designed to orient you on the right path.
If you're not the audio/visual kind,
feel free to skip past them :).
Because they're hosted on YouTube,
if you need captions,
hit the captions button to get access to them.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JdcFLuZLJ3Y" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Using the book

There are three ways to use this website/web book.

Firstly, you can view everything online at this site.
Use the navigation to help you get around,
or search for a specific topic that you're interested in.

Secondly, you can [launch a binder session][binder].
Binder lets you execute the notebook code inside the book.
Click on the Binder button below to get started!

[![Binder](https://mybinder.org/badge.svg)][binder]

Finally, you can pick up the official EPUB/MOBI/PDF version of the book
[on LeanPub][leanpub]!
Purchasing a copy helps support the authors,
and funds future improvements and updates to the book,
which you will continue to receive as we make updates!

## Feedback

If you have feedback for the eBook,
please head over to our [GitHub repository][repo] and raise an issue there.

## Support us!

If you find the book useful,
you can support the creators in the following ways:

1. [Star the repository][repo]! It costs you nothing,
and helps raise the profile of the book.
1. Share the website with your colleagues! It also costs you nothing,
and helps share _the good stuff_ with those you think might benefit from it.
1. Take the official companion courses and projects on DataCamp!
It does cost some money, so we totally understand if you'd prefer not to, but it does buy us coffee :).
1. Support [Eric Ma on Patreon](https://www.patreon.com/ericmjl) with a monthly coffee pledge
to keep him caffeinated, which helps him make other good material to share.
1. Follow Eric and Mridul on Twitter at [@ericmjl](https://twitter.com/ericmjl) and [@Mridul_Seth](https://twitter.com/Mridul_Seth)
1. Purchase [the companion book on LeanPub][leanpub] and fund coffee that way too!

[binder]: https://mybinder.org/v2/gh/ericmjl/Network-Analysis-Made-Simple/master
[leanpub]: https://leanpub.com/nams
[repo]: https://github.com/ericmjl/Network-Analysis-Made-Simple

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/03-practical/01-io.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "%matplotlib inline\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "import warnings\n",
    "\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"3sJnTpeFXZ4\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to get you familiar with graph ideas,\n",
    "I have deliberately chosen to steer away from\n",
    "the more pedantic matters\n",
    "of loading graph data to and from disk.\n",
    "That said, the following scenario will eventually happen,\n",
    "where a graph dataset lands on your lap,\n",
    "and you'll need to load it in memory \n",
    "and start analyzing it.\n",
    "\n",
    "Thus, we're going to go through graph I/O,\n",
    "specifically the APIs on how to convert\n",
    "graph data that comes to you\n",
    "into that magical NetworkX object `G`.\n",
    "\n",
    "Let's get going!\n",
    "\n",
    "## Graph Data as Tables\n",
    "\n",
    "Let's recall what we've learned in the introductory chapters.\n",
    "Graphs can be represented using two **sets**:\n",
    "\n",
    "- Node set\n",
    "- Edge set\n",
    "\n",
    "### Node set as tables\n",
    "\n",
    "Let's say we had a graph with 3 nodes in it: `A, B, C`.\n",
    "We could represent it in plain text, computer-readable format:\n",
    "\n",
    "```csv\n",
    "A\n",
    "B\n",
    "C\n",
    "```\n",
    "\n",
    "Suppose the nodes also had metadata.\n",
    "Then, we could tag on metadata as well:\n",
    "\n",
    "```csv\n",
    "A, circle, 5\n",
    "B, circle, 7\n",
    "C, square, 9\n",
    "```\n",
    "\n",
    "Does this look familiar to you?\n",
    "Yes, node sets can be stored in CSV format,\n",
    "with one of the columns being node ID,\n",
    "and the rest of the columns being metadata.\n",
    "\n",
    "### Edge set as tables\n",
    "\n",
    "If, between the nodes, we had 4 edges (this is a directed graph),\n",
    "we can also represent those edges in plain text, computer-readable format:\n",
    "\n",
    "```csv\n",
    "A, C\n",
    "B, C\n",
    "A, B\n",
    "C, A\n",
    "```\n",
    "\n",
    "And let's say we also had other metadata,\n",
    "we can represent it in the same CSV format:\n",
    "\n",
    "```csv\n",
    "A, C, red\n",
    "B, C, orange\n",
    "A, B, yellow\n",
    "C, A, green\n",
    "```\n",
    "\n",
    "If you've been in the data world for a while,\n",
    "this should not look foreign to you.\n",
    "Yes, edge sets can be stored in CSV format too!\n",
    "Two of the columns represent the nodes involved in an edge,\n",
    "and the rest of the columns represent the metadata.\n",
    "\n",
    "### Combined Representation\n",
    "\n",
    "In fact, one might also choose to combine\n",
    "the node set and edge set tables together in a merged format:\n",
    "\n",
    "```\n",
    "n1, n2, colour, shape1, num1, shape2, num2\n",
    "A,  C,  red,    circle, 5,    square, 9\n",
    "B,  C,  orange, circle, 7,    square, 9\n",
    "A,  B,  yellow, circle, 5,    circle, 7\n",
    "C,  A,  green,  square, 9,    circle, 5\n",
    "```\n",
    "\n",
    "In this chapter, the datasets that we will be looking at\n",
    "are going to be formatted in both ways.\n",
    "Let's get going."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Dataset\n",
    "\n",
    "We will be working with the Divvy bike sharing dataset.\n",
    "\n",
    "> Divvy is a bike sharing service in Chicago.\n",
    "> Since 2013, Divvy has released their bike sharing dataset to the public.\n",
    "> The 2013 dataset is comprised of two files: \n",
    "> - `Divvy_Stations_2013.csv`, containing the stations in the system, and\n",
    "> - `DivvyTrips_2013.csv`, containing the trips.\n",
    "\n",
    "Let's dig into the data!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyprojroot import here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Firstly, we need to unzip the dataset:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import zipfile\n",
    "import os\n",
    "from nams.load_data import datasets\n",
    "\n",
    "# This block of code checks to make sure that a particular directory is present.\n",
    "if \"divvy_2013\" not in os.listdir(datasets):\n",
    "    print(\"Unzipping the divvy_2013.zip file in the datasets folder.\")\n",
    "    with zipfile.ZipFile(datasets / \"divvy_2013.zip\", \"r\") as zip_ref:\n",
    "        zip_ref.extractall(datasets)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's load in both tables.\n",
    "\n",
    "First is the `stations` table:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "stations = pd.read_csv(\n",
    "    datasets / \"divvy_2013/Divvy_Stations_2013.csv\",\n",
    "    parse_dates=[\"online date\"],\n",
    "    encoding=\"utf-8\",\n",
    ")\n",
    "stations.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stations.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's load in the `trips` table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "trips = pd.read_csv(\n",
    "    datasets / \"divvy_2013/Divvy_Trips_2013.csv\", parse_dates=[\"starttime\", \"stoptime\"]\n",
    ")\n",
    "trips.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import janitor\n",
    "\n",
    "trips_summary = (\n",
    "    trips.groupby([\"from_station_id\", \"to_station_id\"])\n",
    "    .count()\n",
    "    .reset_index()\n",
    "    .select_columns([\"from_station_id\", \"to_station_id\", \"trip_id\"])\n",
    "    .rename_column(\"trip_id\", \"num_trips\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "trips_summary.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Model\n",
    "\n",
    "Given the data, if we wished to use a graph as a data model\n",
    "for the number of trips between stations,\n",
    "then naturally, nodes would be the stations,\n",
    "and edges would be trips between them.\n",
    "\n",
    "This graph would be directed,\n",
    "as one could have more trips from station A to B\n",
    "and less in the reverse.\n",
    "\n",
    "With this definition,\n",
    "we can begin graph construction!\n",
    "\n",
    "### Create NetworkX graph from pandas edgelist\n",
    "\n",
    "NetworkX provides an extremely convenient way\n",
    "to load data from a pandas DataFrame:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "\n",
    "G = nx.from_pandas_edgelist(\n",
    "    df=trips_summary,\n",
    "    source=\"from_station_id\",\n",
    "    target=\"to_station_id\",\n",
    "    edge_attr=[\"num_trips\"],\n",
    "    create_using=nx.DiGraph,\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Inspect the graph\n",
    "\n",
    "Once the graph is in memory,\n",
    "we can inspect it to get out summary graph statistics."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You'll notice that the edge metadata have been added correctly: we have recorded in there the number of trips between stations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(G.edges(data=True))[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "However, the node metadata is not present:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(G.nodes(data=True))[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Annotate node metadata\n",
    "\n",
    "We have rich station data on hand,\n",
    "such as the longitude and latitude of each station,\n",
    "and it would be a pity to discard it,\n",
    "especially when we can potentially use it as part of the analysis\n",
    "or for visualization purposes.\n",
    "Let's see how we can add this information in.\n",
    "\n",
    "Firstly, recall what the `stations` dataframe looked like:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stations.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `id` column gives us the node ID in the graph,\n",
    "so if we set `id` to be the index,\n",
    "if we then also loop over each row,\n",
    "we can treat the rest of the columns as dictionary keys\n",
    "and values as dictionary values,\n",
    "and add the information into the graph.\n",
    "\n",
    "Let's see this in action."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for node, metadata in stations.set_index(\"id\").iterrows():\n",
    "    for key, val in metadata.items():\n",
    "        G.nodes[node][key] = val"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, our node metadata should be populated."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(G.nodes(data=True))[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In `nxviz`, a `GeoPlot` object is available\n",
    "that allows you to quickly visualize\n",
    "a graph that has geographic data.\n",
    "However, being `matplotlib`-based,\n",
    "it is going to be quickly overwhelmed\n",
    "by the sheer number of edges.\n",
    "\n",
    "As such, we are going to first filter the edges.\n",
    "\n",
    "### Exercise: Filter graph edges\n",
    "\n",
    "> Leveraging what you know about how to manipulate graphs,\n",
    "> now try _filtering_ edges.\n",
    ">\n",
    "\n",
    "_Hint: NetworkX graph objects can be deep-copied using `G.copy()`:_\n",
    "\n",
    "```python\n",
    "G_copy = G.copy()\n",
    "```\n",
    "\n",
    "_Hint: NetworkX graph objects also let you remove edges:_\n",
    "\n",
    "```python\n",
    "G.remove_edge(node1, node2)  # does not return anything\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def filter_graph(G, minimum_num_trips):\n",
    "    \"\"\"\n",
    "    Filter the graph such that\n",
    "    only edges that have minimum_num_trips or more\n",
    "    are present.\n",
    "    \"\"\"\n",
    "    G_filtered = G.____()\n",
    "    for _, _, _ in G._____(data=____):\n",
    "        if d[___________] < ___:\n",
    "            G_________.___________(_, _)\n",
    "    return G_filtered\n",
    "\n",
    "\n",
    "from nams.solutions.io import filter_graph\n",
    "\n",
    "G_filtered = filter_graph(G, 50)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Visualize using GeoPlot\n",
    "\n",
    "`nxviz` provides a GeoPlot object\n",
    "that lets you quickly visualize geospatial graph data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A note on geospatial visualizations:\n",
    "\n",
    "> As the creator of `nxviz`,\n",
    "> I would recommend using proper geospatial packages\n",
    "> to build custom geospatial graph viz,\n",
    "> such as [`pysal`](http://pysal.org/).)\n",
    "> \n",
    "> That said, `nxviz` can probably do what you need\n",
    "> for a quick-and-dirty view of the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import nxviz as nv\n",
    "\n",
    "c = nv.geo(G_filtered, node_color_by=\"dpcapacity\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Does that look familiar to you? Looks quite a bit like Chicago, I'd say :)\n",
    "\n",
    "Jesting aside, this visualization does help illustrate\n",
    "that the majority of trips occur between stations that are\n",
    "near the city center."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Pickling Graphs\n",
    "\n",
    "Since NetworkX graphs are Python objects,\n",
    "the canonical way to save them is by pickling them.\n",
    "\n",
    "Here's an example in action:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "\n",
    "with open(\"/tmp/divvy.pkl\", \"wb\") as f:\n",
    "    pickle.dump(G, f, pickle.HIGHEST_PROTOCOL)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And just to show that it can be loaded back into memory:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"/tmp/divvy.pkl\", \"rb\") as f:\n",
    "    G_loaded = pickle.load(f)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise: checking graph integrity\n",
    "\n",
    "If you get a graph dataset as a pickle,\n",
    "you should always check it against reference properties\n",
    "to make sure of its data integrity.\n",
    "\n",
    "> Write a function that tests that the graph\n",
    "> has the correct number of nodes and edges inside it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_graph_integrity(G):\n",
    "    \"\"\"Test integrity of raw Divvy graph.\"\"\"\n",
    "    # Your solution here\n",
    "    pass\n",
    "\n",
    "\n",
    "from nams.solutions.io import test_graph_integrity\n",
    "\n",
    "test_graph_integrity(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Other text formats\n",
    "\n",
    "CSV files and `pandas` DataFrames\n",
    "give us a convenient way to store graph data,\n",
    "and if possible, do insist with your data collaborators\n",
    "that they provide you with graph data that are in this format.\n",
    "If they don't, however, no sweat!\n",
    "After all, Python is super versatile.\n",
    "\n",
    "In this ebook, we have loaded data in\n",
    "from non-CSV sources,\n",
    "sometimes by parsing text files raw,\n",
    "sometimes by treating special characters as delimiters in a CSV-like file,\n",
    "and sometimes by resorting to parsing JSON.\n",
    "\n",
    "You can see other examples of how we load data\n",
    "by browsing through the source file of `load_data.py`\n",
    "and studying how we construct graph objects."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solutions\n",
    "\n",
    "The solutions to this chapter's exercises are below"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from nams.solutions import io\n",
    "import inspect\n",
    "\n",
    "print(inspect.getsource(io))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/03-practical/02-testing.ipynb`:

```ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import YouTubeVideo\n",
    "\n",
    "YouTubeVideo(id=\"SdbKs-crm-g\", width=\"100%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "By this point in the book, you should have observed\n",
    "that we have written a number of _tests_ for our data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Why test?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### If you like it, put a ring on it...\n",
    "\n",
    "...and if you rely on it, test it.\n",
    "\n",
    "I am personally a proponent of writing tests for our data\n",
    "because as data scientists,\n",
    "the fields of our data, and their correct values,\n",
    "form the \"data programming interface\" (DPI)\n",
    "much like function signatures form\n",
    "the \"application programming interface\" (API).\n",
    "Since we test the APIs that we rely on,\n",
    "we probably should test the DPIs that we rely on too."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What to test\n",
    "\n",
    "When thinking about what part of the data to test,\n",
    "it can be confusing.\n",
    "After all, data are seemingly generated\n",
    "from random processes\n",
    "(my Bayesian foxtail has been revealed),\n",
    "and it seems difficult to test random processes.\n",
    "\n",
    "That said, from my experience handling data,\n",
    "I can suggest a few principles."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Test invariants\n",
    "\n",
    "Firstly, we test __invariant properties__ of the data.\n",
    "Put in plain language, things we know _ought_ to be true.\n",
    "\n",
    "Using the Divvy bike dataset example,\n",
    "we know that every node ought to have a station name.\n",
    "Thus, the minimum that we can test\n",
    "is that the `station_name` attribute is present on every node.\n",
    "As an example:\n",
    "\n",
    "```python\n",
    "def test_divvy_nodes(G):\n",
    "    \"\"\"Test node metadata on Divvy dataset.\"\"\"\n",
    "    for n, d in G.nodes(data=True):\n",
    "        assert \"station_name\" in d.keys()\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Test nullity\n",
    "\n",
    "Secondly, we can test that values that ought **not** to be null\n",
    "should not be null.\n",
    "\n",
    "Using the Divvy bike dataset example again,\n",
    "if we _also_ know that the station name\n",
    "cannot be null or an empty string,\n",
    "then we can bake that into the test.\n",
    "\n",
    "```python\n",
    "def test_divvy_nodes(G):\n",
    "    \"\"\"Test node metadata on Divvy dataset.\"\"\"\n",
    "    for n, d in G.nodes(data=True):\n",
    "        assert \"station_name\" in d.keys()\n",
    "        assert bool(d[\"station_name\"])\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Test boundaries\n",
    "\n",
    "We can also test boundary values.\n",
    "For example, within the city of Chicago,\n",
    "we know that latitude and longitude values\n",
    "ought to be within the vicinity of\n",
    "`41.85003, -87.65005`.\n",
    "If we get data values that are, say,\n",
    "outside the range of `[41, 42]; [-88, -87]`,\n",
    "then we know that we have data issues as well.\n",
    "\n",
    "Here's an example:\n",
    "\n",
    "```python\n",
    "def test_divvy_nodes(G):\n",
    "    \"\"\"Test node metadata on Divvy dataset.\"\"\"\n",
    "    for n, d in G.nodes(data=True):\n",
    "        # Test for station names.\n",
    "        assert \"station_name\" in d.keys()\n",
    "        assert bool(d[\"station_name\"])\n",
    "\n",
    "        # Test for longitude/latitude\n",
    "        assert d[\"latitude\"] >= 41 and d[\"latitude\"] <= 42\n",
    "        assert d[\"longitude\"] >= -88 and d[\"longitude\"] <= -87\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "An apology to geospatial experts: \n",
    "_I genuinely don't know the bounding box lat/lon coordinates of Chicago,\n",
    "so if you know those coordinates, please reach out\n",
    "so I can update the test._"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Continuous data testing\n",
    "\n",
    "The key idea with testing is to have tests that continuously run\n",
    "all the time in the background\n",
    "without you ever needing to intervene to kickstart it off.\n",
    "It's like having a bot in the background always running checks for you\n",
    "so you don't have to kickstart them.\n",
    "\n",
    "To do so, you should be equipped with a few tools.\n",
    "I won't go into them in-depth here,\n",
    "as I will be writing\n",
    "a \"continuous data testing\" essay in the near future.\n",
    "That said, here is the gist.\n",
    "\n",
    "Firstly, **use `pytest` to get set up with testing.**\n",
    "You essentially write a `test_something.py` file\n",
    "in which you write your test suite,\n",
    "and your test functions are all nothinng more than simple functions.\n",
    "\n",
    "```python\n",
    "# test_data.py\n",
    "def test_divvy_nodes(G):\n",
    "    \"\"\"Test node metadata on Divvy dataset.\"\"\"\n",
    "    for n, d in G.nodes(data=True):\n",
    "        # Test for station names.\n",
    "        assert \"station_name\" in d.keys()\n",
    "        assert bool(d[\"station_name\"])\n",
    "\n",
    "        # Test for longitude/latitude\n",
    "        assert d[\"latitude\"] >= 41 and d[\"latitude\"] <= 42\n",
    "        assert d[\"longitude\"] >= -88 and d[\"longitude\"] <= -87\n",
    "```\n",
    "\n",
    "At the command line, if you ran `pytest`,\n",
    "it will automatically discover all functions prefixed with `test_`\n",
    "in all `.py` files underneath the current working directory.\n",
    "\n",
    "Secondly, **set up a continuous pipelining system**\n",
    "to continuously run data tests.\n",
    "For example, you can set up\n",
    "[Jenkins](https://www.jenkins.io/),\n",
    "[Travis](https://travis-ci.org/),\n",
    "[Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/),\n",
    "[Prefect](https://www.prefect.io/),\n",
    "and more,\n",
    "depending on what your organization has bought into.\n",
    "\n",
    "Sometimes data tests take longer than software tests,\n",
    "especially if you are pulling dumps from a database,\n",
    "so you might want to run this portion of tests\n",
    "in a separate pipeline instead."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Further reading\n",
    "\n",
    "- In my essays collection, I wrote about [testing data](https://ericmjl.github.io/essays-on-data-science/software-skills/testing/#tests-for-data).\n",
    "- Itamar Turner-Trauring has written about [keeping tests quick and speedy](https://pythonspeed.com/articles/slow-tests-fast-feedback/), which is extremely crucial to keeping yourself motivated to write tests."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nams",
   "language": "python",
   "name": "nams"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```

`/Users/nikola/dev/Network-Analysis-Made-Simple/notebooks/learn-more.md`:

```md
Thank you for making it this far!
We hope you've enjoyed the book.
If you want to further your learning,
here's a few resources to keep you going.

<!--
## DataCamp

I have a course on DataCamp that you can use
to get further practice.
Signing up also supports me financially
(that's my disclaimer),
though the financial support also helps me make more
programmer-oriented data science content for you!
You can sign up at [DataCamp.com](https://www.datacamp.com/?tap_a=5644-dce66f&tap_s=883155-2f8036&utm_medium=affiliate&utm_source=ericma1)

Here's an overview of what's available

=== "Introduction"

    I created "Introduction to Network Analysis with Python" in 2017,
    and have been continually updating it with the latest API.
    It will give you complementary extra practice to the exercises in this book.

    You can find the course [here](https://learn.datacamp.com/courses/introduction-to-network-analysis-in-python).

=== "Intermediate"

    This is the next step up from "Introduction to Network Analysis".
    You will explore some of the advanced topics in this book,
    with different exercises in there to help you reinforce the ideas.

    The link to this course is [here](https://learn.datacamp.com/courses/intermediate-network-analysis-in-python).

=== "Project"

    Mridul's project is up on DataCamp as a continuation of the series
    of network analysis courses.
    The online learning environment should help you with reinforcing
    the ideas in there.

    The link to his "project course" is [here](https://learn.datacamp.com/projects/76).

-->

## Academic Books

=== "Statistics"

    "Statistical Analysis of Network Data" is an incredible resource for learning
    how to analyze graph data from a statistical viewpoint.
    It is written by Boston University's professor of mathematics
    Eric D. Kolaczyck.
    I used it during graduate school
    as part of my personnal learning journey.
    The book's website can be found [here](http://math.bu.edu/people/kolaczyk/SAND.html),
    and is available on Amazon (click on the book link below).

    <a target="_blank"  href="https://www.amazon.com/gp/product/038788145X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=038788145X&linkCode=as2&tag=ericmjl-20&linkId=489e360e1beb1e46ab19a76214deaa77"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=038788145X&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=ericmjl-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=ericmjl-20&l=am2&o=1&a=038788145X" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

=== "Network Science"

    This is a book by Prof. Albert-Laszlo Barabasi, and is freely available [online].
    In it, he explores network analysis from the perspective of an applied academic discipline,
    showing universal properties and processes that underly networks.

    [online]: http://networksciencebook.com/

=== "Think Complexity"

    This is a book by Prof. Allen Downey at the Olin College of Engineering.
    In fact, this was the first book that exposed me (Eric Ma)
    to network science and its ideas, which thus inspired my thesis topic,
    which then gave me the impetus to learn graph theory and make this tutorial.
    I hope it becomes a useful thing for you too.
    You can find the book [at Green Tea Press][thinkcomp] for free,
    but do consider purchasing a copy to support Allen's work!

    [thinkcomp]: https://greenteapress.com/wp/think-complexity-2e/


=== "Spectral Graph Theory"

    This is a book by UCSD Prof. Fan Chung.
    It is being partially revised, with chapters available [online][fanchung].
    Contains valuable information on the connections between graphs and linear algebra.

    [fanchung]: https://mathweb.ucsd.edu/~fan/research/revised.html

## Online Resources

=== "Snacks"

    Snacks is a repository of network analysis learning tools
    curated in the same spirit as the "Awesome-X" repositories
    that show up on GitHub.
    You can find it [here](https://github.com/alonnir/snacks/).

```