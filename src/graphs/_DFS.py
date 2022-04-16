
'''A Mixin class to extend features to the Graph class. Provides Depth-First Search algorithms for an adjacency-list graph.'''
class Mixin:

    '''Method to perform a recursive Depth-First Search traversal on a graph.
        
    Recursive backtracking is used to traverse all nodes in a graph, starting from a specified vertex.
    Algorithm continuously calls recursive_DFS on adjacent vertices (the key of every dictionary entry).
    Cycles may be found, and thus a 'visited' list of vertices is maintained to track what has already been seen.
    
    Returns the 'visited' vertex set, and (for the purpose of demonstration) a 'visit_order' ordered DFS traversal path.

    Time Complexity: O(V + E) - where V = cardinality of the vertex set, E = cardinality of the edge set. 
    Space Complexity: O(V) - as an extra list of len(V) must be maintained to track visited nodes.
    '''
    def DFS(self, v):
        #create a set to store visited vertices. The entry index corresponds to the vertex's label
        #**sets in Python utilize hashtables and therefore are ~ O(1) for checking set membership**
        visited = set()

        #also maintain an ordered vertex list to show the order of traversals that the DFS takes
        visit_order = []

        #perform recursive DFS on the graph object from a specific vertex
        self.recursive_DFS(v, visited, visit_order)
        return visited, visit_order


    '''The recursive DFS helper function.
    '''
    def recursive_DFS(self, v, visited, visit_order):
        #visit the node by adding it to the set
        visited.add(v)
        visit_order.append(v)

        #perform DFS on all branches adjacent to this vertex
        for a in self.graph[v]:

            #skip if the vertex was already traversed
            if a not in visited:
                self.recursive_DFS(a, visited, visit_order)



