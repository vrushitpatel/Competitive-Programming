class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_beginning(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      new_node.next = self.head
      return
    curr = self.head
    while curr.next != self.head:
      curr = curr.next
    curr.next = new_node
    new_node.next = self.head
    self.head = new_node