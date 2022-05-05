import sorting.bubblesort as bs
import sorting.insertionsort as ins
import sorting.quicksort as qs

import searching.iter_binarysearch as i_bs
import graphs.Graph as g

from src.linkedlists.SinglyLinkedList import SinglyLinkedList
from src.linkedlists.SinglyLinkedNode import SinglyLinkedNode

def main():

    #initialize a test list
    l = [1, 6, 8, -3, 12, 2, -8, 0, 17, 9, -20, 32, 5]
    print("Initial test list: ", l)
    print()

    '''Sorting Algorithms'''
    #perform sorting operations, and print the sorted result
    l = [1, 6, 8, -3, 12, 2, -8, 0, 17, 9, -20, 32, 5]
    sorted_list = bs.bubblesort(l)
    print("Bubblesort result: ", sorted_list)

    #TODO: FIX INSERTION SORT!
    l = [1, 6, 8, -3, 12, 2, -8, 0, 17, 9, -20, 32, 5]
    ins.insertionsort(l)
    print("Insertionsort result: ", l)

    l = [1, 6, 8, -3, 12, 2, -8, 0, 17, 9, -20, 32, 5]
    qs.quicksort(l, 0, len(l) - 1)
    print("Quicksort result: ", l)


    '''Searching Algorithms'''
    #sort the list first, perform search, and print index
    print()
    l = [1, 6, 8, -3, 12, 2, -8, 0, 17, 9, -20, 32]
    l.sort()
    value = 12
    index = i_bs.iter_binarysearch(l, value)
    print("Iterative Binary Search index for target value " +  str(value) + ": " +  str(index),
         "; value at index: " +  str(sorted_list[index]))


    '''Graphing'''
    #build a graph
    print()
    graph = g.Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(3,5)
    graph.add_edge(4,0)
    graph.add_edge(5,1)
    graph.add_edge(4,1)
    graph.add_edge(2,3)
    graph.add_edge(2,5)

    #show the created graph
    graph.print_graph()

    #perform a recursive DFS traversal on the graph from a chosen vertex, and print the final 'visited' list
    vertex = 1
    visited, visit_order = graph.DFS(vertex)
    print("Vertices visited: ", visited)
    print("DFS traversal order from vertex " + str(vertex) + ": ", visit_order)

    #perform an iterative BFS traversal on the graph from a chosen vertex, and print the final 'visited' list
    visited, visit_order = graph.BFS(vertex)
    print("Vertices visited: ", visited)
    print("BFS traversal order from vertex " + str(vertex) + ": ", visit_order)


    '''Linked Lists'''
    #instantiating a linked list
    print()
    nodelist = SinglyLinkedList( SinglyLinkedNode(2) )

    #add some nodes to the list
    node1 = SinglyLinkedNode(5)
    node2 = SinglyLinkedNode(7)
    node3 = SinglyLinkedNode(13)
    node4 = SinglyLinkedNode(-6)
    node5 = SinglyLinkedNode(0)
    nodelist.insert_to_back(node1)
    nodelist.insert_to_back(node2)
    nodelist.insert_to_back(node3)
    nodelist.insert_to_front(node4)
    nodelist.insert_to_front(node5)

    #print the contents of the list
    nodelist.print_list()

    #get the list head
    print("Current head of the list: ", nodelist.get_head().data)

    #remove a specific node from the list
    nodelist.remove_node(7)
    print("Removing node with data = 7: ", end='')
    nodelist.print_list()



if __name__ == "__main__":
    main()