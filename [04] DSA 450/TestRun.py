from collections import deque
class Queue:
  def __init__(self) -> None:
    self.items = deque()

  def enqueue(self, data):
    self.items.append(data)

  def dequeue(self):
    if self.isEmpty():
      return None
    return self.items.popleft()
  
  def peek(self):
    if self.isEmpty():
      return None
    return self.item[0]

  def isEmpty(self):
    return len(self.items) == 0
  
  def size(self):
    return len(self.items)


class CircularQueue:
  def __init__(self, k) -> None:
    self.items = [None] * k
    self.size = k
    self.front = self.rear = -1

  def enqueue(self, data):
    if (self.rear + 1) % self.size == self.front:
      return False
    if self.front == -1:
      self.front = 0
    self.rear = (self.rear + 1) % self.size
    self.items[self.rear] = data
    return True
  
  def deque(self):
    if self.front == -1:
      return None
    data = self.items[self.front]
    if self.front == self.rear:
      self.front = self.rear = -1
    else:
      self.front = (self.front + 1) % self.size
    return data
