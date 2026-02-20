# https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1
# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.front = None
        self.rear = None
        self._size = 0

    def isEmpty(self):
        # Return True if queue is empty, else False
        return True if self.size() == 0 else False
        

    def enqueue(self, x):
        # Add element x to the rear
        new_node = Node(x)
        self._size += 1
        if self.front == None:
            self.front = new_node
        if self.rear == None:
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        

    def dequeue(self):
        # Remove the front element
        if self.isEmpty():
            return False
        self._size -=1
        self.front = self.front.next

    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.isEmpty():
            return -1
        return self.front.data


    def size(self):
        # Return current size
        return self._size
        