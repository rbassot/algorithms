
import _DFS
import _BFS

'''
A basic undirected graph class in adjacency list representation.
    A dictionary is used to maintain vertex/adjacent edge pairs.'''
class Graph(_DFS.Mixin, _BFS.Mixin):

    def __init__(self):
        self.V = []
        self.graph = dict()

    #method to add a vertex to the graph.
    #added vertices have degree = 0 initially.
    def add_vertex(self, v):
        if v not in self.graph:
            self.V.append(v)
            self.graph[v] = []


    #method to add an edge to the graph between two vertices: u & v.
    #as the graph is undirected, this adds the edge to both adjacency lists for vertices u & v
    def add_edge(self, u, v):
        for vertex1, vertex2 in [(u, v), (v, u)]:
            #append to an existing adjacency list
            if vertex1 in self.graph:
                self.graph[vertex1].append(vertex2)

            #otherwise, create a new list
            else:
                self.graph[vertex1] = [vertex2]

    #method to print the graph representation.
    def print_graph(self):
        for v in self.V:
            print("Vertex " + str(v) + ":", end="")

            #print out the vertex's adjacency list
            for x in self.graph[v]:
                print("-> {}".format(x), end="")
            print(" \n")