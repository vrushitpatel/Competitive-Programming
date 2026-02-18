# https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1
# Node class
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        # Initialize your data members
        self.head = None
        self._size = 0
    
    def isEmpty(self):
        # Check if the stack is empty
        return self.head is None

    def push(self, x):
        # Adds element x to the top of the stack
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self._size -= 1
        return temp

    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.isEmpty():
            return -1
        return self.head.data


    def size(self):
        # Returns the current size of the stack
        return self._size