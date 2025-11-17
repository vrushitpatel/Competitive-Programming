# Linked List Cheat Sheet

Linked List is a simple data structure that is made up of nodes. Each node has two components. One is the value and another is a pointer to the address of the next node. The next pointer of the last node of Linked List is NULL. Head is a pointer that points to the first node of Linked List.

## Structure

Initializing a Node Class & LinkedList Class

```python
class Node:
    def __init__(self, data):
        self.data = data # Assigns the given data to the node
        self.next = None # Initialize the next attribute to null

class LinkedList:
    def __init__(self):
        self.head = None # Initialize head as None
```

## Time & Space Complexity

| Operation          | Time | Space |
| ------------------ | ---- | ----- |
| Access             | O(n) | O(1)  |
| Search             | O(n) | O(1)  |
| Insert (beginning) | O(1) | O(1)  |
| Insert (end)       | O(n) | O(1)  |
| Insert (middle)    | O(n) | O(1)  |
| Delete (beginning) | O(1) | O(1)  |
| Delete (end)       | O(n) | O(1)  |
| Delete (middle)    | O(n) | O(1)  |

## Core Operations

### 1. Insertion

```python
# At beginning
def insert_at_beginning(self, data):
    new_node = Node(data) # Create a new node
    new_node.next = self.head # Next for new node becomes the current head
    self.head = new_node # Head now points to the new node

# At end
def insert_at_end(self, data):
    new_node = Node(data) # Create a new node
    if not self.head:
        self.head = new_node # If the list is empty, make the new node the head
        return
    curr = self.head
    while curr.next: # Otherwise, traverse the list to find the last node
        curr = curr.next
    curr.next = new_node # Make the new node the next node of the last node

# At position
def insert_at_position(self, data, pos):
    new_node = Node(data) # Create a new node
    if pos == 0: # If the list is empty, make the new node the head
        new_node.next = self.head
        self.head = new_node
        return
    curr = self.head
    for _ in range(pos - 1): # Otherwise, traverse the list till the position
        if not curr:
            return
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node # Make the new node in the list at the position pos
```

### 2. Deletion

```python
# Delete by value
def delete_node(self, key):
    curr = self.head
    if curr and curr.data == key: # If the node is the beginning node
        self.head = curr.next
        return
    prev = None  # Creating a Temp Previous Node Variable
    while curr and curr.data != key:
        prev = curr
        curr = curr.next
    if curr:
        prev.next = curr.next # Connect the previous and the next node, skipping the current node.

# Delete at position
def delete_at_position(self, pos):
    if not self.head: # If the list is empty, return this string
        return "The List is Empty"
    if pos == 0: # For the Beginning Node: Remove the head by making the next node the new head
        self.head = self.head.next
        return
    curr = self.head
    for _ in range(pos - 1): # Otherwise, go to the previous position
        if not curr:
            return
        curr = curr.next
    if curr and curr.next: # Remove the node by setting the "n"ext" pointer of the next node
        curr.next = curr.next.next
```

### 3. Traversal

```python
def print_list(self):
    curr = self.head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
```

## Two Pointer Techniques

### Fast & Slow Pointer (Floyd's Cycle Detection)

One pointer, the "tortoise," moves one step at a time, while the other, the "hare," moves two steps at a time.

**Problem:**

- If there's a cycle, the fast pointer will eventually catch up with the slow pointer within the cycle because it's moving faster.
- If there's no cycle, the fast pointer will reach the end of the list (i.e., it will become NULL).
- It Returns TRUE if Cycle or Loop Exists.

```python
def detect_cycle(self):
    slow = fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Find Middle Element

```python
def find_middle(self):
    slow = fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data
```

### Nth Node from End

```python
def nth_from_end(self, n):
    first = second = self.head
    for _ in range(n):
        if not first:
            return None
        first = first.next
    while first:
        first = first.next
        second = second.next
    return second.data
```

## Key Patterns to Remember

1. **Dummy Node**: Use for merge/partition operations
2. **Two Pointers**: Fast-slow, previous-current
3. **Recursion**: For reversal, merging
4. **Runner Technique**: One pointer k steps ahead
5. **In-place Operations**: Avoid extra space

## Common Pitfalls

- Forgetting to check `head == None`
- Not updating `head` after operations
- Losing reference to next node during deletion
- Off-by-one errors in position-based operations
- Not handling single node edge case

## Interview Tips

- Always ask: Singly or doubly linked?
- Clarify: Can we modify the original list?
- Check: Are there cycles?
- Discuss: Time vs Space tradeoffs
- Test: Empty list, single node, two nodes
