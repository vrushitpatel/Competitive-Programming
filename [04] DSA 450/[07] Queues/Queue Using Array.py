# https://www.geeksforgeeks.org/problems/implement-queue-using-array/1
class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.queue = [None] * n
        self.size = n
        self.front = self.rear = -1
    
    def isEmpty(self):
        # Check if queue is empty
        return True if self.front == -1 else False
    
    def isFull(self):
        # Check if queue is full
        return True if ((self.rear + 1) % self.size == self.front) else False
    
    def enqueue(self, x):
        # Enqueue
        if self.isFull():
            return False
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = x
    
    def dequeue(self):
        # Dequeue
        if self.isEmpty():
            return False
        data = self.front
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data
    
    def getFront(self):
        # Get front element
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def getRear(self):
        # Get rear element 
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        
        