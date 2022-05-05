import SinglyLinkedNode

'''
A basic singly-linked list implementation Uses SinglyLinkedNode type.
Contains only the head (SinglyLinkedNode) of the list'''
class SinglyLinkedList:
    def __init__(self, node):
        self.head = node


    '''Method to insert a node into the singly-linked list at the back of the list.'''
    def insert_to_back(self, node):
        #edge case - the list does not have a head, so insert it as the new head
        if(self.head == None):
            self.head = node
            return

        #iterate through the list until the tail is reached
        temp_node = self.head

        while temp_node.next != None:
            temp_node = temp_node.next

        #insert the node at the back of the list
        temp_node.next = node
        return


    '''Method to insert a node into the singly-linked list at the front of the list.
        the new node becomes the new head of the list.'''
    def insert_to_front(self, node):
        #edge case - the list does not have a head, so insert it as the new head
        if(self.head == None):
            self.head = node
            return

        #reassign pointers to insert the node as the new head
        node.next = self.head
        self.head = node     
        return

    
    '''Method to remove a specific node from the singly-linked list.
        the node is searched for by its data value, and the list is cleaned up.'''
    def remove_node(self, value):
        #edge case - the list does not have a head, so the node cannot be removed
        if(self.head == None):
            print("The list is empty!")
            return

        #iterate through the list from the head, searching for the node to be removed
        current_node = self.head
        prev_node = self.head

        while current_node != None:
            #check if the current node is the node to remove
            if current_node.data == value:
                break

            prev_node = current_node
            current_node = current_node.next

        #we found the correct node, and must remove it from the list by pointing prev --> current.next
        if current_node.data == value:
            prev_node.next = current_node.next

        return


    '''Method to return the head node of the list.'''
    def get_head(self):
        return self.head

    
    '''Method to print the data values of all nodes in the list, in order.'''
    def print_list(self):
        if(self.head == None):
            print("The list is empty!")
            return

        #iterate through the list from the head, printing node values
        temp_node = self.head
        print("Node values: ", end='')

        while temp_node != None:
            print(temp_node.data, " ", end='')
            temp_node = temp_node.next
        
        print()
        return
