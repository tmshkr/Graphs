"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            raise IndexError("Vertex already exists")

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError(
                "Both vertices must exist in order to add an edge")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = deque()
        q.append(starting_vertex)

        visited = set()
        path = []

        while len(q) > 0:
            v = q.popleft()

            if v not in visited:
                visited.add(v)
                path.append(v)
                print(v)

                for neighbor in self.get_neighbors(v):
                    q.append(neighbor)

        return path

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = []
        s.append(starting_vertex)

        visited = set()
        path = []

        while len(s) > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                path.append(v)
                print(v)

                for neighbor in self.get_neighbors(v):
                    s.append(neighbor)

        return path

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order.

        This should be done using recursion.
        """
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for neighbor in self.get_neighbors(vertex):
                self.dft_recursive(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = deque()
        q.append([starting_vertex])

        visited = set()

        while len(q) > 0:
            path = q.popleft()
            v = path.pop()

            if v not in visited:
                visited.add(v)
                path.append(v)
                if v == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(v):
                    q.append(path + [neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = []
        s.append([starting_vertex])

        visited = set()
        path = []

        while len(s) > 0:
            path = s.pop()
            v = path.pop()

            if v not in visited:
                visited.add(v)
                path.append(v)
                if v == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(v):
                    s.append(path + [neighbor])

        return path

    def dfs_recursive(self, v, destination_vertex, path=[], visited=None, solution=None):
        """
        Return a list containing a path from
        v to destination_vertex in depth-first order.

        This should be done using recursion.
        """
        if len(path) == 0:
            solution = []
            visited = set()

        visited.add(v)
        path = path + [v]

        if v == destination_vertex:
            solution.extend(path)
            return

        for neighbor in self.get_neighbors(v):
            if neighbor not in visited:
                self.dfs_recursive(
                    neighbor, destination_vertex, path, visited, solution)

        return solution


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("graph.bft(1)", graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("graph.dft(1)", graph.dft(1))
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("graph.bfs(1, 6)", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("graph.dfs(1, 6)", graph.dfs(1, 6))
    print("graph.dfs_recursive(1, 6)", graph.dfs_recursive(1, 6))
