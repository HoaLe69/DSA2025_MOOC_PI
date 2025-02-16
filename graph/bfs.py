class BFS:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def search(self, start_node):
        visited = set()

        queue = [start_node]

        visited.add(start_node)

        for node in queue:
            for next_node in self.graph[node]:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)

        return visited

    def find_distances(self, start_node):
        distances = {}
        queue = [start_node]
        distances[start_node] = 0

        for node in queue:
            distance = distances[node]

            for next_node in self.graph[node]:
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1

        return distances

    def find_path(self, start_node, end_node):
        distances = {}
        previous = {}
        queue = [start_node]
        distances[start_node] = 0
        previous[start_node] = None

        for node in queue:
            distance = distances[node]
            for next_node in self.graph[node]:
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1
                    previous[next_node] = node

        if end_node not in distances:
            return None

        node = end_node

        path = []
        while node:
            path.append(node)
            node = previous[node]

        path.reverse()
        return path


b = BFS([1, 2, 3, 4, 5])

b.add_edge(1, 2)
b.add_edge(1, 3)
b.add_edge(1, 4)
b.add_edge(2, 4)
b.add_edge(2, 5)
b.add_edge(3, 4)
b.add_edge(4, 5)
s = BFS([1, 2, 3, 4, 5])
s.add_edge(1, 2)
s.add_edge(1, 3)
s.add_edge(1, 4)
s.add_edge(2, 4)
s.add_edge(2, 5)
s.add_edge(3, 4)
s.add_edge(4, 5)

print(s.find_path(2, 4))  # [2, 4]
print(s.find_path(1, 5))  # [1, 2, 5]
print(s.find_path(5, 1))  # [5, 2, 1]

print(b.find_distances(1))

print(b.search(1))
