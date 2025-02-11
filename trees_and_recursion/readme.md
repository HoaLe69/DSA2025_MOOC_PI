# Trees and recursion.

- A tree is a data structures that consists of _nodes_ at different levels.
- The _subtree_ of a node consists of all nodes that can be reached by following connections downwards from the node.
- The depth of a node tells how low the node is in the tree.
- The height o a tree is the maximum depth of any node in the tree.

# Implementing a tree.

```python
class Node:
  # the nodes will refer to the same empty list and any additions to the list are seen by all nodes
  def __init__(self, value , children=[]):
    self.value = value
    self.children = children
  def __repr__(self):
    return str(self.value)
  # improving
  def __init__(self, value , children=None):
    self.value = value
    self.children = children if children else []
  def __repr__(self):
    if self.children == []:
      return f"Node({self.value})"
    else:
      return f"Node({self.value}, {self.children})"


node2 = Node(2)
node3 = Node(3)
node1 = Node(1, [node2, node3])

print(node1)

tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])
```

# Traversing a tree.

- A natural way to process a tree is using recursion.

```python
def traversing(node):
  print("enter", node.value)
  for child in node.children:
    traversing(child)
  print("leave", node.value)

traversing(tree)
"""
enter 1
enter 4
enter 3
leave 3
enter 7
leave 7
leave 4
enter 5
leave 5
enter 2
enter 6
leave 6
leave 2
leave 1
"""
```

# Computing information from a tree.

- Trees are often processed using recursive functions that compute some value related to the tree.

1. How many nodes in tree ?

```python
def count_nodes(node):
  result = 1
  for child in  node.children:
    result += count_nodes(child)
    print("subtree of node", node , "has" , result, "nodes")
  return result

print(count_nodes(tree)) #7
"""
subtree of node 3 has 1 nodes
subtree of node 7 has 1 nodes
subtree of node 4 has 3 nodes
subtree of node 5 has 1 nodes
subtree of node 6 has 1 nodes
subtree of node 2 has 2 nodes
subtree of node 1 has 7 nodes
"""
```

2. How tall is the tree ?

```python
def count_height(node):
  result = 0
  for child in node.children:
    result = max(result, count_height(child) + 1)
  return result

print(count_height(tree)) #2
```

# Computing depths.

1. prints out depth of every node.

```python
def depth_of_node(node, depth):
  print("node", node, "depth" , depth)
  for child in node.children:
    depth_of_node(child, depth+1)

depth_of_node(tree)
"""
node 1 depth 0
node 4 depth 1
node 3 depth 2
node 7 depth 2
node 5 depth 1
node 2 depth 1
node 6 depth 2
"""
```

3. get depth

- returns the node depths as a list ordered from the smallest to the biggest depth.

```python
def get_depths_helper(node , depth,depths):
  depths.append(depth)

  for child in node.children:
    get_depths_helper(node, depth+1, depths)

def get_depths(node):
  depths = []
  get_depths_helper(node, 0 , depths)
  return sorted(depths)

print(get_depths(tree))# [0, 1, 1, 1, 2, 2, 2]
```
