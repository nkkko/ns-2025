# Lectures

This directory contains all lecture materials for the Network Analysis course, presented as MARP slide decks.

## Structure

Each lecture is organized in its own numbered directory:

- `01/` - Introduction to Network Science
- `02/` - Graph Theory Fundamentals
- `03/` - Network Measures and Metrics
- `04/` - Network Visualization
- `05/` - Random Graph Models
- `06/` - Small World Networks
- `07/` - Scale-Free Networks
- `08/` - Community Detection
- `09/` - Network Resilience
- `10/` - Dynamics on Networks
- `11/` - Network Analysis Tools
- `12/` - Temporal Networks
- `13/` - Multilayer Networks
- `14/` - Applications and Case Studies
- `15/` - Project Review

## Using MARP

Each lecture directory contains a MARP markdown file (`lecture.md`) that can be compiled into presentations.

### Install MARP CLI

```bash
npm install -g @marp-team/marp-cli
```

### Convert to PDF

```bash
marp --pdf lecture.md
```

### Convert to PPTX

```bash
marp --pptx lecture.md
```

### Preview with live reload

```bash
marp -p lecture.md
```