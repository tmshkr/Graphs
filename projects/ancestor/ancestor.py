class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_parent(self, parent, child):
        if parent in self.vertices and child in self.vertices:
            self.vertices[child].add(parent)
        else:
            raise IndexError(
                "Both vertices must exist in order to add an edge")


def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for (parent, child) in ancestors:
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_parent(parent, child)

    visited = set()
    paths = []

    def dft(node, path=[]):
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if len(g.vertices[node]) > 0:
                for p in g.vertices[node]:
                    dft(p, path)
            else:
                paths.append(path)

    dft(starting_node)

    longest_path = (1, -1)
    for p in paths:
        if len(p) > longest_path[0]:
            longest_path = (len(p), p[-1])
        elif len(p) == longest_path[0]:
            if p[-1] < longest_path[1]:
                longest_path = (len(p), p[-1])

    return longest_path[1]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(ancestors, 8)
