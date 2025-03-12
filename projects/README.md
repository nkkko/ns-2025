# Dataset and project ideas for Network Analysis 2024/2025

## A word on data preparation

For all datasets, some degree of pre-processing is needed before obtaining usable data.
That is inherent to the work of a data scientist, and will mostly involve the following steps.

1. **Data acquisition.**
   Raw data may need to be (i) collected via a web API, (ii) collected by scraping a website, or (iii) already collected and packaged (for example in a CSV file).
2. **Data importation.**
   Raw data needs to be imported in a pandas DataFrame, where rows will be nodes of the network, and columns will be features (or characteristics or attributes) of those nodes.
3. **Data cleaning.**
   This step varies a lot from dataset to dataset.
   In the context of the course, it will mostly consist in reducing the size of the network so that it can be processed in a reasonable amount of time.
   The less packaged the raw data, the more cleaning will be necessary.
4. **Network creation.**
   The network structure may either be (i) given to you as an adjacency matrix, (ii) given to you as an edge list, or (iii) inferred from raw data.

While those steps are necessary for every dataset, the amount of pre-processing will however vary.
If a dataset requires raw data to be collected or the network to be created, that will be indicated in the datset description.
So if you are a beginner and do not feel confident, choose a dataset that requires little pre-processing.
If you feel confident, be adventurous!
Keep in mind that the amount of work generally trades with flexibility: well packaged data usually serves a single task and may restrict your creativity.

## Selecting a dataset

We encourage teams to choose a dataset and problematic that inspire them.
While we provide a [list of datasets](#proposed-datasets), we encourage motivated teams to look for their own data.
That is especially relevant to PhD students who want to apply the knowledge acquired in this course to their research problems.

### Where to find (network) datasets?

There are plenty of sources to search for data. Here are some links:
* <https://www.kaggle.com/datasets>
* <https://toolbox.google.com/datasetsearch>
* <https://networkrepository.com>
* <https://github.com/awesomedata/awesome-public-datasets>
* <https://opendata.swiss/en>

### What are the requirements for the dataset?

You need to choose a dataset that can be represented by a network.
The network structure can either be given or can be constructed from features.
To give you an idea of network representations, go through the [list of proposed datasets](#proposed-datasets).
Please discuss with the TAs during lab sessions for guidance.

### How to determine the task to be addressed?

Keep in mind that while necessary, it is not enough to create a network and give some statistical facts about it.
You should determine a task, which is usually based on the inference of latent information.
You can address it with network science tools, such as community detection, or by machine learning tools, such as classification or semi-supervised learning.
Check beforehand if you can justify your results with a ground-truth, or alternatively, with a qualitative or visual assessment.
The tasks that can be addressed depend on the information provided by the dataset such as features, labels, signals, etc.
Some datasets, like the ones on [Kaggle](https://www.kaggle.com/datasets), were created to address one such task.

## Proposed datasets

* [Free Music Archive](#free-music-archive)
* [US Senators](#us-senators)
* [Wikipedia](#wikipedia)
* [Researchers on Twitter](#researchers-on-twitter)
* [Scientific co-Authorship](#scientific-co-authorship)
* [Spammers on Social Networks](#spammers-on-social-networks)
* [Terrorist Attacks and Relations](#terrorist-attacks-and-relations)
* [IMDb Films and Crew](#imdb-films-and-crew)
* [Flight Routes](#flight-routes)
* [Recipes 1M](#recipes-1m)
* [Genetics](#genetics)
* [Movielens 100k](#movielens-100k)

Look also at the list of [past Network Analysis projects](#past-projects).

## Free Music Archive
By Michaël

The [Free Music Archive](https://freemusicarchive.org/) (FMA) is a free and open library directed by [WFMU](https://wfmu.org/), the longest-running freeform radio station in the United States.
Inspired by [Creative Commons](https://creativecommons.org/) and the open-source software movement, the FMA provides a platform for curators, artists, and listeners to harness the potential of music sharing.
The website provides a large catalog of artists and tracks, hand-picked by established audio curators. Each track is legally free to download as artists decided to release their works under permissive licenses.

The goal of this project is to analyze the content created by an open community.
Through the light of networks, it is possible to examine how music tracks relate to each other.
Does genre structure the music?
Do we observe groups of similar artists?
Can we build a playlist that links two tracks through a smooth transition?
To answer those questions, we will build a similarity graph between music tracks.

The packaged data consists of music tracks with associated metadata.
Metadata exists at the level of tracks (e.g., title, creation date), albums (e.g., track number), and artists (e.g, artist name).
A full-length audio recording is available for each track.
Additionally, a fixed length feature vector (audio descriptors computed from the waveform) describes the track.
Relations between tracks can be studied by constructing a similarity graph.
The similarity graph can be computed from audio features and metadata (at the level of tracks, albums, or artists).
A subset of 2,000 tracks can be built by choosing tracks that belong to the Hip-Hop and Rock genres of the dataset "FMA small".

It is also feasible to work with other graphs, such as relations between artists or listeners.
The latter requires to scrap the website.

|          | Description                                | Amount |
| -------- | ------------------------------------------ | ------:|
| nodes    | audio tracks                               | 25,000 |
| edges    | similarity between tracks                  |    N/A |
| features | audio features pre-extracted from waveform |    518 |
| labels   | musical genre (e.g., Rock, Pop)            |     16 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: up to the students
* **Network creation**: needs to be built from features

Resources:
* Paper: <https://arxiv.org/abs/1612.01840>
* Code and data: <https://github.com/mdeff/fma>

## US Senators
By Michaël

The goal of this project is to understand the [community structure](https://en.wikipedia.org/wiki/Community_structure) and voting pattern of US senators.
Will we observe a divide between democrats and republicans?
Are there sub-communities or moderate members?
Can we predict what a senator will vote knowing what some senators voted?
To answer those questions, we will build a similarity graph between senators.

For each senator, we know (i) their political party (i.e., republican, democrat, independent), (ii) their voting activity (i.e., what they voted on a list of issues), and (iii) the groups they belong to (e.g., the bills they sponsored, the committees they are member of).
We propose to first build the similarity graph from the votes, i.e., measure the distance between voting vectors.
Going further, similarity might be measured from the other features, such as bill sponsoring or committee membership.

|          | Description                                              | Amount |
| -------- | -------------------------------------------------------- | ------:|
| nodes    | US senators                                              |   ~100 |
| edges    | similarity between senators                              |    N/A |
| features | votes, bill sponsoring, committee membership, statements |    N/A |
| labels   | political party: democrat, republican, independent       |      3 |

* **Data acquisition**: need to be collected from a web API
* **Requires down-sampling**: no
* **Network creation**: needs to be built from features

Resources:
* [ProPublica Congress API](https://projects.propublica.org/api-docs/congress-api/)
* [Blog post on using the API](https://www.storybench.org/use-propublicas-congress-api-see-senators-stand-issues/)

## Wikipedia
By Benjamin and Nicolas

Wikipedia is an enormous source of information visited daily by millions of users. We can understand human behavior by looking at how it is built and accessed. In this project you will investigate the Wikipedia structure and learn more about our use, as humans, of the largest encyclopedia ever.
Using the [Wikipedia API], a network can be built where pages are nodes and hyperlinks are edges. The students exploring this dataset can focus on a (or several) particular subset(s) of pages. (The entire Wikipedia is too large for a NTDS project and cannot be retrieved from the API.)
In addition, numerous attributes about the pages can be retrieved through the API. For example, similarly to the Cora dataset, from the text of the page one can build a feature vector for each page related to the keywords it contains. The category of a page can be a label. Furthermore, the number of visits per page per day can be obtained from the [Pageview API]. It gives the possibility to the students of analyzing the popularity of the articles over time. For example, one can check if the popularity of a page influences the popularity of the neighboring pages or if the popularity of a group of pages is related to a particular event.
It is also possible to study and compare pages, networks and features in different languages. This dataset is rich, be creative!
A reduced dataset, extracted from the API, will be collected by the students. We suggest to build a graph having 100 to 1000 nodes.

|          | Description                                    |      Amount |
| -------- | ---------------------------------------------- | -----------:|
| nodes    | Wikipedia pages                                | 100 to 1000 |
| edges    | hyperlinks                                     |         N/A |
| features | number of visits per day, keywords in the text |         >10 |
| labels   | category                                       |         3-5 |

* **Data acquisition**: to be collected from the Wikipedia API
* **Requires down-sampling**: yes, during collection
* **Network creation**: given

Resources:
* [Wikipedia API]
* [Pageview API]
* Python packages to access the APIs: [`wikipedia`](https://pypi.org/project/wikipedia), [`Wikipedia-API`](https://pypi.org/project/Wikipedia-API), [`pageviewapi`](https://pypi.org/project/pageviewapi)

[Wikipedia API]: https://www.mediawiki.org/wiki/API:Main_page
[Pageview API]: https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews

## Researchers on Twitter
by Ersi

The goal of this project is to analyze the interactions of a sub-network of Twitter.
The Twitter accounts in this project are Computer Science researchers or other accounts "related" to Computer Science.
The [dataset](https://github.com/l3s/twitter-researcher) consists of the activity of 52,678 Twitter users.
Of those, 170 are Twitter screen names of 98 Computer Science Conferences.
These 170 Twitter accounts are set as seeds and more Twitter nodes have been collected if they are (i) following a seed, (ii) being followed by a seed, or (iii) have re-tweeted a seed's tweet.
Out of the 52,678 Twitter users, 9,191 are verified to be researchers (they have been matched to a DBLP author profile).
22 features are given for each Twitter user, including for instance a boolean feature demonstrating if the bio description includes words that are usually being used to describe researchers.
You can find a detailed description of the data in [this paper](https://dx.doi.org/10.1145/2615569.2615676).
Keep in mind that the labels for this project are noisy as they are the results of classification.

|          | Description                                                | Amount |
| -------- | ---------------------------------------------------------- | ------:|
| nodes    | Twitter accounts                                           | 52,678 |
| edges    | similarity (or connection) between Twitter accounts        |    N/A |
| features | numerical and boolean features describing Twitter accounts |     22 |
| labels   | researcher or non-researcher (noisy label)                 |      2 |

* **Data acquisition**: already collected and packaged (load tsv files). Some data cleaning will be needed.
* **Requires down-sampling**: up to the students
* **Network creation**: If you chose to create a similarity graph between the Twitter users, it needs to be built from features.
  If you chose to build a graph with the connections between users, you must collect information using the Twitter API (with [tweepy](https://github.com/tweepy/tweepy)).
  As this can be time consuming, we recommend to build a feature graph first, and to explore the connections graph later.

Resources:
* Paper: <https://dx.doi.org/10.1145/2615569.2615676>
* Data: <https://github.com/l3s/twitter-researcher>

## Scientific co-Authorship
by Ersi

This project aims to explore the co-authorship behaviour of scientific authors.
The [dataset](https://perso.liris.cnrs.fr/marc.plantevit/doku/doku.php?id=data_sets) is a co-authorship graph built from the DBLP digital library. Each vertex represents an author that has published at least one paper in one of the major conferences and journals of the Data Mining and Database communities between January 1990 and February 2011. Each edge links two authors who co-authored at least one paper (no matter the conference or journal). The vertex properties are the number of publications in each of the 29 selected conferences or journals and 9 topological properties (Degree Cent., Closeness Cent., Betweenness Cent., EigenVector Cent., PageRank, Clustering Coeff., Size of Max. Quasi-Clique, Number of Quasi-Cliques, Size of Community).

|          | Description                                                    |  Amount |
| -------- | -------------------------------------------------------------- | -------:|
| nodes    | scientific authors                                             |  42,252 |
| edges    | authors are linked if they wrote a paper together              | 210,320 |
| features | number of publications in conferences and topological features |      38 |
| labels   | N/A                                                            |     N/A |

* **Data acquisition**: already collected and packaged (load txt files)
* **Requires down-sampling**: up to the students
* **Network creation**: The connections between the nodes are already provided.

Remark 1: There are no labels given for the nodes in this dataset. You can chose as your labels two subsets of the conferences (e.g., KDD and AAAI).

Remark 2: The creator of this dataset has agreed to provide the data for this project. However, they will be given to you through a private channel and you should not re-distribute it.

## Spammers on Social Networks
by Eda

The dataset contains 5.6 million users, which are described by 4 features; "user id", "gender", "age group", "spammer label". There are 7 different type of relations between the users indicating the action between them such as profile view, message, poke, etc., which may lead to 7 different directed graph. In total, there are 858 million link between the users. The original task associated with this dataset is to identify the spammers based on their features and links in the network.

Since this dataset is very big, it requires subsampling even during the loading of the data and cleaning the network accordingly. We warn the students that the size of the dataset add more difficulties (for example you can't create a 5.6x5.6 million adjacency matrix). So be sure you can make a smaller, meaningful subset for the project if you choose it.

|          | Description                                                   |      Amount |
| -------- | ------------------------------------------------------------- | -----------:|
| nodes    | users of tagged.com                                           |   5,607,447 |
| edges    | action between users: includes a timestamp and one of 7 types | 858,247,099 |
| features | sex, timePassedValidation, ageGroup                           |           3 |
| labels   | spammer or not spammer                                        |           2 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: yes
* **Network creation**: network is given as a list of edges

Resources:
* <https://linqs.soe.ucsc.edu/node/236>
* <https://linqs-data.soe.ucsc.edu/public/social_spammer>
* Paper: <https://www.cs.umd.edu/~shobeir/papers/fakhraei_kdd_2015.pdf>
* Code: <https://github.com/shobeir/fakhraei_kdd2015>
* Data: <https://linqs-data.soe.ucsc.edu/public/social_spammer/usersdata.csv.gz>, <https://linqs-data.soe.ucsc.edu/public/social_spammer/relations.csv.gz>


## Terrorist Attacks and Relations
by Eda

The first dataset consists of 1293 terrorist attacks (nodes), each of which is assigned to one of 6 labels indicating the type of the attack. Each attack is described by a 0/1-valued vector of attributes whose entries indicate the absence/presence of a feature. There are a total of 106 distinct features. The files in the dataset can be used to create two distinct graphs. In one of them edges of the graph connect the colocated attacks. On the other one, edges connect co-located terrorist attacks performed by the same terrorist organization.

The second dataset is designed for the classification of the relationships between the terrorists. The dataset contains 851 relations (aka; nodes of the graph). Each node is assigned to least one label (multiple labeling is also possible) among 4 labels; "Colleague", "Congregate", "Contact", "Family", and is described with 0/1 valued feature vector indicating absence/presence of the attributes, which are 1224 in total. There are 8592 edges on the graph, which connects the nodes involving the same terrorist group.
As the goal is the classification of links, we will here build the [line graph](https://en.wikipedia.org/wiki/Line_graph) of the social network between terrorists.
That is, instead of having terrorists as nodes and relationships between them as edges, relationships will be nodes and terrorists will be edges.

We warn the students that the 106 features given in this dataset are undocumented so that it can not be used for interpreting the data or doing anything meaningful. The students who choose this project will have to increase the dataset by collecting data from other source of information about terrorism.

|          | Description                                                                  | Amount |
| -------- | ---------------------------------------------------------------------------- | ------:|
| nodes    | relationships                                                                |    851 |
| edges    | terrorists                                                                   |  8,592 |
| features | 0-1 vector of attribute values                                               |  1,224 |
| labels   | type of relationship (non exclusive): colleague, congregate, contact, family |      4 |

|          | Description                                                     | Amount |
| -------- | --------------------------------------------------------------- | ------:|
| nodes    | terrorist attacks                                               |  1,293 |
| edges    | connect co-located attacks                                      |  3,172 |
| features | 0-1 vector of attribute values                                  |    106 |
| labels   | kind of attack: arson, bombing, kidnapping, weapon, nbcr, other |      6 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: network is given as a list of edges

Resources:
* <https://linqs.soe.ucsc.edu/node/236>
* <https://www.cs.umd.edu/~sen/lbc-proj/LBC.html>
* Paper: <https://pdfs.semanticscholar.org/c047/f91ece3e9ec74bf42b8f69f375e27498a54a.pdf>
* Data: <https://linqs-data.soe.ucsc.edu/public/lbc/TerrorAttack.tgz>
* Data: <https://linqs-data.soe.ucsc.edu/public/lbc/TerroristRel.tgz>

## IMDb Films and Crew
By Rodrigo, taken over by Nikolaos

The IMDb datasets contain information such as crew, rating, and genre for every entertainment product in its database. The Kaggle dataset linked above is a smaller, but similar dataset, and could be used instead of the IMDb one, which is much larger. The goal of this project is to analyze this database in graph form, and attempt to recover missing information from data on cast/crew co-appearance in movies. The graphical analysis requires network creation, for which two possible paths are possible, according to which instances one wishes to consider as the nodes of the network.

The first approach could be to construct a social network of cast/crew members, where the edges are weighted according to co-appearance For example, actor_1 becomes strongly connected to actor_2 if they have appeared in a lot of movies together. The edges of the graph could be weighted according to a count on the number of entertainment products in which the two corresponding people participated together. We can take as a signal on this constructed graph the aggregate ratings of movies each person has participated in.

|          | Description                            |                          Amount |
| -------- | -------------------------------------- | ------------------------------: |
| nodes    | cast/crew                              | millions (IMDb), ~8500 (Kaggle) |
| edges    | co-apearance in movies/TV/etc.         |                  O(10) per node |
| features | ratings of movies taken part in        |                  O(10) per node |
| labels   | movie genre                            |       unknown (IMDb), 3 (Kaggle)|

A second approach could be to create a movie-network, in which movies are strongly connected if they share a lot of crew/cast members (or some other similarity measure combining this and genres, running times, release years, etc.). There are more options for the signal the students could consider on this graph, as they could use either the movie ratings, or the genre labels.

|          | Description                                           |                          Amount |
| -------- | ----------------------------------------------------- | ------------------------------: |
| nodes    | movies                                                | millions (IMDb), ~5000 (Kaggle) |
| edges    | count of common cast/crew + other feature similarity. |                  O(10) per node |
| features | average rating                                        |                               1 |
| labels   | movie genre                                           |      unknown (IMDb), 3 (Kaggle) |

For the extra work, there is plenty of extra information. For instance, the students could try to predict the revenue of movies by potentially including extra metadata. Note however that the number of instances in the original dataset is of the order of **millions**, so a smaller subset of those should be used.

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: yes if using the original datasets from IMDb, no if using the subsampled dataset from Kaggle
* **Network creation**: needs to be built from features

Resources:
* <https://www.imdb.com/interfaces>
* <https://www.kaggle.com/tmdb/tmdb-movie-metadata/home>

## Flight Routes
By Rodrigo, taken over by Guillermo

This OpenFlights/Airline Route Mapper Route Database contains 67,663 routes (EDGES) between 3,321 airports (NODES) on 548 airlines spanning the globe.

The construction of the graph is facilitated by the source and destination airports of each flight, which gives essentially an edge list for the airport graph. Students could complement the graph construction by providing weigths to the edges, proportional to the number of flights connecting the corresponding pair of airports. The visualization of the graph embedded on the globe can be achieved by using the supplemented data in https://openflights.org/data.html, which contains, among others, information on latitute/longitude of each airport. A potential goal of the extra work could then be comparing the embedding produced by the Laplacian eigenmaps algorithm seen in the course and the "natural" embedding given by the terrestrial coordinates. The most sensitive part of the project (which could be examined in the extra work) would be to find a label signal on the graph that could be recovered via a label propagation algorithm on the graph. In principle, the average number of stops of flights leaving each airport could fulfill this purpose, but it remains a metter of study whether a subsampled version of this information can be recovered from the topological information of the graph alone or not.

|          | Description                                 | Amount |
| -------- | ------------------------------------------- | -----: |
| nodes    | airports                                    |  3,321 |
| edges    | count of flights connecting airports        | 67,663 |
| features | average number of stops of outbound flights |      1 |
| labels   | N/A                                         |    N/A |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: network is essentially given (list of edges)

Resources:
* <https://openflights.org/data.html#route>
* <https://openflights.org/data.html>

## Recipes 1M
By Nicolas

This database contains circa 1 million cooking recipes retrieved from several websites, along with one or more images for each recipe (13 million images available).
Its original use is to train models to perform a "im2recipe", i.e., get recipe instructions from an image.
For every recipe in this dataset, you can retrieve the full-text of instructions, ingredients contained in the file available under the "layers" link (and after you unpack the file, in the "layer1.json" file).
For each ingredient line inside a recipe, the name of the ingredient has been extracted ("ingredient detection" link).
Ingredient name detection from text is a non-trivial task, so expect the results to be noisy.
Quantity detection has not been performed, but might be an interesting feature to study (requires extra work).
If you intend to work with images, they require more than 100 GB of download and a matching storage space.

You can, for instance, construct an ingredient graph (linking ingredients when they appear simultaneously in a recipe).

|          | Description                      |         Amount |
| -------- | -------------------------------- | -------------: |
| nodes    | ingredients                      |          18253 |
| edges    | connect co-appearing ingredients | O(10) per node |
| features | recipes                          |              1 |
| labels   | N/A                              |            N/A |

Another approach could be to create a graph from recipes having several ingredients in common.
Given the size of the dataset, it might be a good idea to try out a smaller subset of the dataset, for instance by filtering recipes that contain a particular ingredient (e.g., 'beef', 'vanilla', etc.).
In order for the students to get started more easily, [two smaller subsets](https://drive.switch.ch/index.php/s/fjjqqaRznah6PKp) (with circa 10,000 and 23,000 recipes) are supplied.

|          | Description                             |                         Amount |
| -------- | --------------------------------------- | -----------------------------: |
| nodes    | recipes                                 |                             1M |
| edges    | connect recipes with common ingredients | depends how the graph is built |
| features | images / ingredient quantities          |                           1-10 |
| labels   | N/A                                     |                            N/A |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: yes
* **Network creation**: to be created from co-appearing ingredients or from recipes

Resources:
* <http://pic2recipe.csail.mit.edu/>
* <http://im2recipe.csail.mit.edu/dataset/download/> (requires free registration prior download)
* subsets: <https://drive.switch.ch/index.php/s/fjjqqaRznah6PKp>

## Genetics
By Benjamin

This dataset contains genes, protein expressions and phenotypes of a "family" of mice.
It is a subset of the open dataset available at <http://www.genenetwork.org>.
The goal is to explore the data using graphs and discover connections between genes, protein expression, and phenotypes.
This data has been collected by different laboratories all over the world during several decades.
The [EPFL's LISP](https://www.epfl.ch/labs/auwerx-lab) is part of the group.
More details about the project and dataset can be found on this [EPFL mediacom article](https://actu.epfl.ch/news/a-big-data-tool-begins-new-era-for-biology-and-per/).

This dataset is a collection of matrices.
Each column is a single BXD strain (a mouse) whose genome is a unique combination of the C57BL/6J and DBA/2J parental strains.
They have been saved as CSV files (with a `txt` extension).
The `genotype_BXD.txt` file is a binary matrix that describes the contribution of each of the parental strains for a list of selected genes (rows).
Each row of the genotype data indicates whether a certain position in the genome is inherited from the C57BL/6J or DBA/2J parent.
Phenotype data contained in `Phenotype.txt` are also matrices indicating the values of each phenotype for each strain.
In addition, multiomic molecular phenotypes from different mouse organs are represented as one matrix per organ (e.g., brain, bone, muscle, liver, etc.), in the `expression_data` folder.

It is important to note that protein or phenotype information is not available for all the mice.
Depending on the research team gathering the data or the protocols, only a subset of mice have been tested for each phenotype, or different organs have been analyzed.
Hence, the combination of several matrices will result in missing entries.
These missing entries, along with the variety of the data, are a real challenge for a data science approach, but mimic the real life situation encountered with human medical records.

The dataset for the NTDS project can be found [here](https://drive.switch.ch/index.php/s/mtQ2F0dYc7dHOtQ).
The students are expected to:
* use the different matrices of data to build one or more graphs (for example a graph of mice),
* explore these graphs,
* associate values to the nodes of the graphs using the other matrices,
* apply graph signal processing approaches,
* discover new relations between the genome, protein expressions in tissues and phenotypes (optional but that would be great!).

|          | Description                                                  |         Amount |
| -------- | ------------------------------------------------------------ | -------------: |
| nodes    | mice                                                         |      100 - 200 |
| edges    | similar genes, protein expressions, or phenotypes            | O(10) per node |
| features | genes, protein expressions in tissues, or phenotypes         |          1000s |
| labels   | depends: a particular gene, phenotype, or protein expression |            N/A |

Resources:
* [EPFL mediacom article](https://actu.epfl.ch/news/a-big-data-tool-begins-new-era-for-biology-and-per/)
* [Info on the BXD mice](https://www.biorxiv.org/content/10.1101/672097v3.full)
* [Official dataset website](http://www.genenetwork.org/)
* [Subset for NTDS](https://drive.switch.ch/index.php/s/mtQ2F0dYc7dHOtQ)

## Movielens 100k
By Clément

[Movielens](https://movielens.org) is a personalized movie recommendation system.
Several datasets have been built using this database, the smallest being Movielens 100k.
It contains 100,000 ratings from 1000 users on 1700 movies.
Various information is available about the users (e.g., age, gender, occupation, zip code) and the movies (e.g., release date, genre).
Additional features can be retrieved as movie titles are available.
Two graphs can be built out of this dataset, and they can be connected using the ratings.

The main purpose of this data is to build a recommender system that can be formulated as a semi-supervised learning problem: given a user, can you predict the ratings that they will give to a new movie?
Graph neural networks can be used for this purpose, but other graph based approaches can be explored as well.

| Users graph | Description                       |                         Amount |
| ----------- | --------------------------------- | -----------------------------: |
| nodes       | users                             |                           1000 |
| edges       | similar features                  | depends how the graph is built |
| features    | age, gender, occupation, zip code |                              4 |
| labels      | ratings of the movies             |                           100k |

| Movies graph | Description               |                         Amount |
| ------------ | ------------------------- | -----------------------------: |
| nodes        | movies                    |                           1700 |
| edges        | similar features          | depends how the graph is built |
| features     | name, release date, genre |                  2 + 19 genres |
| labels       | ratings given by users    |                           100k |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: needs to be built from features

Resources:
* [Data](https://grouplens.org/datasets/movielens/)
* Papers using graph neural networks:
  * [Geometric Matrix Completion with Recurrent Multi-Graph Neural Networks](https://arxiv.org/abs/1704.06803)
  * [Graph Convolutional Matrix Completion](https://arxiv.org/abs/1706.02263)
