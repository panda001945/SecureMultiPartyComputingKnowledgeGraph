# Secure Multi-Party Computation Knowledge Graph

This project implements a knowledge graph for secure multi-party computation (SMPC), covering protocols, applications, and participants.

## Features
- **Data Extraction**: Extracts triples (Subject, Predicate, Object) from SMPC-related text.
- **Graph Construction**: Builds a Neo4j graph database.
- **Query Interface**: Provides REST API for querying the graph.
- **Visualization**: Displays the graph using NetworkX and Matplotlib.

## Installation
1. Install dependencies: `pip install -r requirements.txt`
2. Start Neo4j and configure it using `settings.json`.
3. Run the scripts.

## Usage
- **Data Extraction**: `python src/extraction/extract_triples.py`
- **Graph Construction**: `python src/graph_construction/build_graph.py`
- **API**: `python src/query_interface/api.py`
