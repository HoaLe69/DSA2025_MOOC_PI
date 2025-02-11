# Implementing a tree.
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        return str(self.value)


def traverse(node):
    print("enter", node.value)
    for child in node.children:
        traverse(child)
    print("leave", node.value)


def count_nodes(node):
    result = 1
    for child in node.children:
        result += count_nodes(child)
    print("substree of node", node, result, "nodes")
    return result


def count_height(node):
    result = 0
    for child in node.children:
        result = max(result, count_height(child) + 1)
    print("substree of node", node, result, "nodes")

    return result


def depth_of_node(node, depth):
    print("node", node, "depth", depth)
    for child in node.children:
        depth_of_node(child, depth + 1)


# def get_depths_helper(node, depth, depths):
#     depths.append(depth)
#
#     for child in node.children:
#         get_depths_helper(child, depth + 1, depths)
#
#
# def get_depths(node):
#     depths = []
#     get_depths_helper(node, 0, depths)
#     return sorted(depths)


def get_depths(node):
    return sorted(get_depths_helper(node, 0))


def get_depths_helper(node, depth):
    depths = [depth]
    for child in node.children:
        depths += get_depths_helper(child, depth + 1)
    return depths


# Define a tree by building the root node of the tree.
# tree = Node(1, [Node(4, [Node(3), Node(7)]), Node(5), Node(2, [Node(6)])])
#
# # traverse(tree)
# print("num of node", count_nodes(tree))
#
# print("count_height", count_height(tree))
#
# print("get_depths", get_depths(tree))
#
# depth_of_node(tree, 0)

node1 = Node(1)
node2 = Node(2)
node1.children.append(node2)

print(node1.children)
print(node2.children)
