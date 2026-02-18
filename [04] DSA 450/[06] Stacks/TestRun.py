class Node:
  def _init_(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def _init_(self):
    self.head = None
  
  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head.next
    self.head = new_node.next

  def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = new_node

  def insert_at_position(self, data, pos):
    new_node = Node(data)
    if pos == 0:
      new_node.next = self.head.next
      self.head = new_node
      return
    curr = self.head
    for _ in range(pos - 1):
      curr = curr.next
    new_node.next = curr.next
    curr.next = new_node

  def delete_node(self, key):
    if self.head and self.head.data == key:
      self.head = self.head.next
      return
    curr = self.head
    while curr:
      if curr.data == key:
        curr.next = curr.next.next
        return
      curr = curr.next

  def delete_at_position(self, pos):
    if self.head and pos == 0:
      self.head = self.head.next
      return
    curr = self.head
    for _ in range(pos-1):
      if not curr:
        return
      curr = curr.next
    if curr and curr.next:
      curr.next = curr.next.next

  def print_list(self):
    curr = self.head
    while curr:
      print(curr.data, "-->")
      curr = curr.next
    if curr == None:
      print("None")
