"""
Weighted Graph Implementation with Dijkstra's Algorithm and Minimum Spanning Tree (MST)

This script provides a `WeightedGraph` class that supports weighted edges and includes algorithms for finding shortest paths using Dijkstra's algorithm and computing Minimum Spanning Trees (MSTs).

Classes:
    - WeightedGraph: Extends the `Graph` class to include weighted edges and additional graph algorithms.
    - MST: Represents the Minimum Spanning Tree as a subclass of `Tree`.
    - ShortestPathTree: Represents the result of Dijkstra's algorithm as a subclass of `Tree`.

Key Methods in WeightedGraph:
    - addEdge(u, v, w): Adds a weighted edge between vertices `u` and `v` with weight `w`.
    - getWeight(u, v): Retrieves the weight of the edge between vertices `u` and `v`.
    - getMinimumSpanningTree(startingVertex): Computes the MST using Prim's algorithm.
    - getShortestPath(sourceVertex): Computes the shortest paths from a source vertex using Dijkstra's algorithm.

Usage Example:
    >>> vertices = ["A", "B", "C", "D"]
    >>> edges = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [0, 3, 8]]
    >>> graph = WeightedGraph(vertices, edges)
    >>> mst = graph.getMinimumSpanningTree(0)
    >>> print(mst.getTotalWeight())  # Outputs the total weight of the MST
    >>> shortest_path_tree = graph.getShortestPath(0)
    >>> shortest_path_tree.printAllPaths()  # Prints shortest paths from the source
"""

from Graph import Graph
from Graph import Tree
from WeightedEdge import WeightedEdge

INFINITY = 1e+308 # Infinity value

class WeightedGraph(Graph):
    def __init__(self, vertices = [], edges = []):
        super().__init__(vertices, edges)

    # Override this method in the Graph class
    def getAdjacnecyLists(self, edges):
        self.neighbors = []
        for i in range(len(self.vertices)):
            self.neighbors.append([]) # Each element is another list
            
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            w = edges[i][2]
            # Insert an edge (u, v, w)
            self.neighbors[u].append(WeightedEdge(u, v, w)) 

        return self.neighbors
    
    #Display edges with weights 
    def printWeightedEdges(self):
        for i in range(len(self.neighbors)):
            print(str(self.getVertex(i)) 
                + " (" + str(i), end = "): ")
            for edge in self.neighbors[i]:
                print("(" + str(edge.u) + ", " + str(edge.v) 
                      + ", "  + str(edge.weight), end = ") ")
            print()

    # Return the weight between two vertices
    def getWeight(self, u, v):
        for edge in self.neighbors[self.getIndex(u)]:
            if edge.v == self.getIndex(v):
                return edge.weight
  
    # Override the addEdge method to add a weighted edge 
    def addEdge(self, u, v, w):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            # Add an edge (u, v, w) to the graph
            self.neighbors[indexU].append(
                WeightedEdge(indexU, indexV, w))

    # Get a minimum spanning tree rooted at the specified vertex
    def getMinimumSpanningTree(self, startingVertex = 0):
        # cost[v] stores the cost by adding v to the tree
        cost = self.getSize() * [INFINITY]
        cost[startingVertex] = 0 # Cost of source is 0

        parent = self.getSize() * [-1] # Parent of a vertex
        totalWeight = 0; # Total weight of the tree thus far

        T = []
    
        # Expand T
        while len(T) < self.getSize():
            # Find smallest cost v in V - T 
            u = -1 # Vertex to be determined
            currentMinCost = INFINITY
            for i in range(self.getSize()):
                if i not in T and cost[i] < currentMinCost:
                    currentMinCost = cost[i]
                    u = i
                    
            if u == -1:
                break
            else:
                T.append(u) # Add a new vertex to T
            totalWeight += cost[u] # Add cost[u] to the tree

            # Adjust cost[v] for v that is adjacent to u and v in V - T
            for e in self.neighbors[u]:
                if e.v not in T and cost[e.v] > e.weight:
                    cost[e.v] = e.weight
                    parent[e.v] = u 

        return MST(startingVertex, parent, T, totalWeight, 
            self.vertices)

    def getShortestPath(self, sourceVertex):
        # cost[v] stores the cost of the path from v to the source
        cost = [INFINITY] * self.getSize()  # Initial cost to infinity
        cost[sourceVertex] = 0  # Cost of source is 0

        # parent[v] stores the previous vertex of v in the path
        parent = [-1] * self.getSize()

        # T stores the vertices whose path found so far
        T = [sourceVertex]

        # Initialize cost for vertices not in T to infinity
        for v in range(self.getSize()):
            if v != sourceVertex:
                cost[v] = INFINITY

        # Expand T
        while len(T) < self.getSize():
            # Find vertex v in V-T with the smallest cost[u] + w(u,v)
            minCost = INFINITY
            minVertex = -1
            for u in T:
                for e in self.neighbors[u]:
                    if e.v not in T and cost[u] + e.weight < minCost:
                        minCost = cost[u] + e.weight
                        minVertex = e.v
                        parent[minVertex] = u

            if minVertex == -1:
                break

            T.append(minVertex)  # Add v to T
            cost[minVertex] = minCost  # Update cost[v]

        # Create a ShortestPathTree
        return ShortestPathTree(sourceVertex, parent, T, cost, self.vertices)

# MST is a subclass of Tree, defined in the preceding chapter
class MST(Tree):
    def __init__(self, startingIndex, parent, T, 
                 totalWeight, vertices):
        super().__init__(startingIndex, parent, T, vertices)
        # Total weight of all edges in the tree
        self.totalWeight = totalWeight 

    def getTotalWeight(self):
        return self.totalWeight

# ShortestPathTree is an inner class in WeightedGraph 
class ShortestPathTree(Tree):
    def __init__(self, sourceIndex, parent, T, costs, vertices):
        super().__init__(sourceIndex, parent, T, vertices)
        self.costs = costs

    # Return the cost for a path from the root to vertex v 
    def getCost(self, v):
        return self.costs[v]

    # Print paths from all vertices to the source 
    def printAllPaths(self):
        print("All shortest paths from " 
            + str(self.vertices[self.root]) + " are:")
        for i in range(len(self.costs)):
            self.printPath(i) # Print a path from i to the source
            print("(cost: " + str(self.costs[i]) + ")") # Path cost


def test_shortest_path(): 

    # Create vertices
    vertices = ["Seattle", "San Francisco", "Los Angeles",
        "Denver", "Kansas City", "Chicago", "Boston", "New York",
        "Atlanta", "Miami", "Dallas", "Houston"]

    # Create edges
    edges = [
        [0, 1, 807], [0, 3, 1331], [0, 5, 2097],
        [1, 0, 807], [1, 2, 381], [1, 3, 1267],
        [2, 1, 381], [2, 3, 1015], [2, 4, 1663], [2, 10, 1435],
        [3, 0, 1331], [3, 1, 1267], [3, 2, 1015], [3, 4, 599], 
            [3, 5, 1003],
        [4, 2, 1663], [4, 3, 599], [4, 5, 533], [4, 7, 1260],
            [4, 8, 864], [4, 10, 496],
        [5, 0, 2097], [5, 3, 1003], [5, 4, 533], 
            [5, 6, 983], [5, 7, 787],
        [6, 5, 983], [6, 7, 214],
        [7, 4, 1260], [7, 5, 787], [7, 6, 214], [7, 8, 888],
        [8, 4, 864], [8, 7, 888], [8, 9, 661], 
            [8, 10, 781], [8, 11, 810],
        [9, 8, 661], [9, 11, 1187],
        [10, 2, 1435], [10, 4, 496], [10, 8, 781], [10, 11, 239],
        [11, 8, 810], [11, 9, 1187], [11, 10, 239]
        ]

    # Create a graph
    graph1 = WeightedGraph(vertices, edges)

    # Obtain a shortest path
    tree1 = graph1.getShortestPath(5) # Get shortest path from index 5
    tree1.printAllPaths()

    # Display shortest paths from Houston to Chicago
    print("Shortest path from Houston to Chicago: ")
    path = tree1.getPath(11)
    print(path)

    # Create vertices and edges
    vertices = [x for x in range(5)]
    edges = [
        [0, 1, 2], [0, 3, 8], 
        [1, 0, 2], [1, 2, 7], [1, 3, 3],
        [2, 1, 7], [2, 3, 4], [2, 4, 5],
        [3, 0, 8], [3, 1, 3], [3, 2, 4], [3, 4, 6],
        [4, 2, 5], [4, 3, 6]
        ]

    # Create a graph
    graph2 = WeightedGraph(vertices, edges)

    # Obtain a shortest path
    tree2 = graph2.getShortestPath(3)
    tree2.printAllPaths()

test_shortest_path()