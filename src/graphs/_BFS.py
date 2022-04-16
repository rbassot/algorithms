
'''A Mixin class to extend features to the Graph class. Provides Breadth-First Search algorithms for an adjacency-list graph.'''
class Mixin:

    '''Method to perform an iterative Breadth-First Search traversal on a graph.

    This algorithm iteratively adds all neighbours to a given vertex to the queue, where the neighbours at this depth
    are traversed first. The queue allows for FIFO traversal priority to be given to the earliest-seen neighbouring vertices.

    Time Complexity: O(V + E) - where V = cardinality of the vertex set, E = cardinality of the edge set. 
    Space Complexity: O(V) - as a queue of len(V) must be maintained to track visited nodes.
    '''
    def BFS(self, source):
        #create a set to store visited vertices. The entry index corresponds to the vertex's label
        #**sets in Python utilize hashtables and therefore are ~ O(1) for checking set membership**
        visited = set()

        #also maintain an ordered vertex list to show the order of traversals that the BFS takes
        visit_order = []

        #create a BFS queue
        queue = []

        #visit the source node by enqueuing it & adding it to the 'visited' set
        visited.add(source)
        visit_order.append(source)
        queue.append(source)


        #perform BFS by iterating through the enqueued neighbours
        while queue:

            #dequeue a vertex from the queue
            v = queue.pop(0)

            #iterate through the vertex's neighbours, and enqueue them all
            for a in self.graph[v]:

                #label unvisited vertixes as visited, and enqueue them
                if a not in visited:
                    visited.add(a)
                    visit_order.append(a)
                    queue.append(a)

        return visited, visit_order



