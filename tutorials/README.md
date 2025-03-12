# Tutorials

This directory contains all tutorial materials for the Network Analysis course, presented as Jupyter notebooks.

## Structure

Tutorials are organized to complement the lecture materials, providing hands-on experience with network analysis concepts and tools.

## Running the Notebooks

### Requirements

Make sure you have the necessary Python packages installed.

#### Option 1: Using uv (Recommended)

[uv](https://docs.astral.sh/uv/) is a fast Python package installer and resolver.

```bash
# Install uv if you don't have it already
pip install uv

# Create a virtual environment in the project root
cd ..
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all requirements
uv pip install -r requirements.txt
```

#### Option 2: Using pip

```bash
# Create a virtual environment in the project root
cd ..
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install core packages
pip install jupyter networkx pandas numpy matplotlib seaborn scikit-learn plotly
```

### Launch Jupyter

From the activated virtual environment:

```bash
jupyter notebook
# or
jupyter lab
```

## Topics Covered

The tutorials cover practical implementations of the concepts discussed in lectures, including:

- Basic network creation and manipulation with NetworkX
- Computing network metrics and centrality measures
- Visualizing networks with different layouts and tools
- Implementing random graph models
- Community detection algorithms
- Network resilience analysis
- Temporal network analysis
- Real-world network data analysis