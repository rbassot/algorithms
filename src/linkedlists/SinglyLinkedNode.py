'''
A basic node class to be used in singly-linked-list implementations.
    Nodes contain a data value, and a pointer to the next node.'''
class SinglyLinkedNode:
   def __init__(self, data=None):
      self.data = data
      self.next = None