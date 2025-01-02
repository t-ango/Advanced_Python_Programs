# Weighted Graph with Dijkstra's and Minimum Spanning Tree (MST)

This repository contains an implementation of a weighted graph using adjacency lists. It supports graph operations such as adding edges, retrieving weights, and applying algorithms like Dijkstra's for shortest paths and Prim's for Minimum Spanning Trees (MSTs).

## Features

### Core Graph Operations
- **Weighted Edges**: Represents graphs with weights on edges.
- **Adjacency List Representation**: Efficient for storing and traversing sparse graphs.
- **Custom Edge Class**: Encapsulates edge properties for flexibility.

### Algorithms Implemented
1. **Dijkstra's Algorithm**:
   - Computes the shortest path from a specified source vertex to all other vertices.
   - Returns a `ShortestPathTree` containing paths and costs.

2. **Prim's Algorithm**:
   - Computes the Minimum Spanning Tree (MST) of the graph.
   - Returns an `MST` object with total weight and structure.

### Utilities
- Display graph structure with weighted edges.
- Retrieve weights for specific edges.
- Extendable to new features and algorithms.

## Usage Example

### Graph Initialization
```python
from WeightedGraph import WeightedGraph

# Define vertices and edges
vertices = ["A", "B", "C", "D"]
edges = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [0, 3, 8]]

# Create a graph
graph = WeightedGraph(vertices, edges)
Compute Minimum Spanning Tree (MST)
mst = graph.getMinimumSpanningTree(0)  # Root MST at vertex 0
print("MST Total Weight:", mst.getTotalWeight())
Compute Shortest Paths with Dijkstra's Algorithm
shortest_path_tree = graph.getShortestPath(0)  # Shortest paths from vertex 0
shortest_path_tree.printAllPaths()
Print Weighted Edges
graph.printWeightedEdges()
Example Output

For a graph with vertices ["A", "B", "C", "D"] and edges [[0, 1, 5], [1, 2, 3], [2, 3, 2], [0, 3, 8]]:

MST Total Weight: 10
Shortest Paths (from vertex A):
A -> A (cost: 0)
A -> B (cost: 5)
A -> B -> C (cost: 8)
A -> B -> C -> D (cost: 10)
Testing

Run the script to test the graph and its algorithms:

python Dijkstras_list.py
Why Adjacency Lists?

The adjacency list representation is memory-efficient for sparse graphs, supports fast traversal, and is widely used in real-world applications.
