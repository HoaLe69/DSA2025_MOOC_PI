# Graph algorithms.

- A _graph_ is a data structure that consists of _nodes_ and _edges_. Each edge connects two nodes.
- A _neighbor_ of node is another node connected to it by an edge.
- A _degree_ of a node is the number of its neighbors.
- A path between two nodes is a route along the edges of the graph.

1 → 2 → 5
1 → 4 → 5
1 → 3 → 4 → 5
1 → 3 → 4 → 2 → 5

- Examples of applications of graphs:

  1. Road network: The nodes are cities and the edges are roads. A path between two nodes is a route between two cities.
  2. Contact network: The nodes are people and the edges are contacts. A path between two nodes describes how people know each other.
  3. Communication network: The nodes are computers and the edges are connections. A path between two nodes describes how data can be transmitted.

# Programming with graphs.

- A common way to represent a graph in programming is to have an adjacency list for each node.
- In python, we can store a graph using a dictionary. Where the keys are nodes and the values are adjacency lists.

```python
graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 5],
    5: [2, 4]
}
```

- It useful to define a class for graph with a method adding edges.

```python
class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = {node : [] for node in nodes}
  def add_edge(self, a, b):
    self.graph[a].append(b)
    self.graph[b].append(a)
```

# Depth-First search.

- DFS is a technique for iterating through all nodes of a graph that can be reached from a given initial node by following edges.

# Components and connectivity.

- A _component_ of a graph contains nodes that are reachable from each other using the edges of the graph.
- A graph is _connected_ if it has exactly one component. If there is a path between any two nodes.

- Using depth-first search we can compute the components of a graph by iterating through all nodes.

# Breadth-first search.

- _Breadth-first search_ or BFS is another technique for iterating through the nodes a graph.
- The difference between the two techniques is the order in which the nodes are visited.

# Shortest paths and distances.

- The _shortest path_ between two nodes in a graph is a path connecting the nodes with the smallest number of edges.
- The _distance_ of two nodes is the length of the shortest path between them.
- We can use BFS to determine the distance of each node to the start node, and to find a shortest path between two nodes.
