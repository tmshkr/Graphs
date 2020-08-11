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
    longest = [1, -1]

    def dft(node, path=[]):
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if len(g.vertices[node]) > 0:
                for p in g.vertices[node]:
                    dft(p, path)
            # if there are no parent nodes
            # determine the longest path
            elif len(path) > longest[0]:
                longest[0] = len(path)
                longest[1] = path[-1]
            elif len(path) == longest[0]:
                if path[-1] < longest[1]:
                    longest[1] = path[-1]

    dft(starting_node)

    return longest[1]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(ancestors, 8)
