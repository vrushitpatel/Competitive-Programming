# Doubly Linked List Cheat Sheet

## Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
```

## Visual Representation

```
None ← [1] ⇄ [2] ⇄ [3] ⇄ [4] → None
```

## Time & Space Complexity

| Operation             | Time           | Space |
| --------------------- | -------------- | ----- |
| Access                | O(n)           | O(1)  |
| Search                | O(n)           | O(1)  |
| Insert (beginning)    | O(1)           | O(1)  |
| Insert (end)          | O(n) or O(1)\* | O(1)  |
| Delete (node given)   | O(1)           | O(1)  |
| Delete (value search) | O(n)           | O(1)  |
| Reverse               | O(n)           | O(1)  |

\*O(1) with tail pointer

## Core Operations

### 1. Insertion at Beginning

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    if self.head:
        self.head.prev = new_node
    self.head = new_node
```

### 2. Insertion at End

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return

    curr = self.head
    while curr.next:
        curr = curr.next

    curr.next = new_node
    new_node.prev = curr
```

### 3. Insertion After Node

```python
def insert_after(self, node, data):
    if not node:
        return
    new_node = Node(data)
    new_node.next = node.next
    new_node.prev = node
    node.next = new_node
    if new_node.next:
        new_node.next.prev = new_node
```

### 4. Insertion Before Node

```python
def insert_before(self, node, data):
    if not node:
        return
    new_node = Node(data)
    new_node.prev = node.prev
    new_node.next = node
    node.prev = new_node
    if new_node.prev:
        new_node.prev.next = new_node
    else:
        self.head = new_node
```

### 5. Delete Node (Given Reference)

```python
def delete_node(self, node):
    if not node:
        return

    # If node is head
    if node == self.head:
        self.head = node.next

    # Change next only if node is not last
    if node.next:
        node.next.prev = node.prev

    # Change prev only if node is not first
    if node.prev:
        node.prev.next = node.next
```

### 6. Delete by Value

```python
def delete_by_value(self, key):
    curr = self.head

    # Find the node
    while curr and curr.data != key:
        curr = curr.next

    if not curr:
        return

    # Delete the node
    if curr.prev:
        curr.prev.next = curr.next
    else:
        self.head = curr.next

    if curr.next:
        curr.next.prev = curr.prev
    else:
        self.tail = curr.prev
```

### 7. Traversal (Forward & Backward)

```python
# Forward
def print_forward(self):
    curr = self.head
    while curr:
        print(curr.data, end=" ⇄ ")
        curr = curr.next
    print("None")

# Backward
def print_backward(self):
    curr = self.head
    if not curr:
        return

    # Go to end
    while curr.next:
        curr = curr.next

    # Print backwards
    while curr:
        print(curr.data, end=" ⇄ ")
        curr = curr.prev
    print("None")
```

## Optimized Version (with Tail Pointer)

### Structure with Tail

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

### Insert at End - O(1)

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = self.tail = new_node
        return

    self.tail.next = new_node
    new_node.prev = self.tail
    self.tail = new_node
```

### Delete from End - O(1)

```python
def delete_from_end(self):
    if not self.tail:
        return

    if self.head == self.tail:  # Single node
        self.head = self.tail = None
        return

    self.tail = self.tail.prev
    self.tail.next = None
```

## Advantages over Singly Linked List

1. **Bidirectional traversal** possible
2. **Deletion is O(1)** when node reference is given
3. **Insert before** a node easily
4. **Reverse traversal** without recursion
5. Better for **navigation** (back/forward)

## Disadvantages

1. **Extra memory** for prev pointer
2. **More complex** operations
3. **More pointers** to maintain
4. Higher **space overhead**

## Use Cases

- Browser history (back/forward)
- Undo/Redo functionality
- LRU Cache implementation
- Music/video players (playlist navigation)
- OS thread scheduler

## Key Patterns

1. **Always update both pointers**: prev and next
2. **Check boundary conditions**: head and tail
3. **Use dummy nodes**: Simplifies edge cases
4. **Two-pointer technique**: Works better than singly

## Common Pitfalls

- Forgetting to update prev pointer
- Not handling head/tail separately
- Breaking links before saving references
- Memory leaks from circular references
- Not checking for None before accessing prev/next

## Interview Tips

- Ask: Can we use extra space?
- Clarify: Is tail pointer available?
- Discuss: Trade-off between time and space
- Check: NULL pointers before operations
- Test: Empty, single node, two nodes

## Quick Comparison

| Feature                 | Singly   | Doubly         |
| ----------------------- | -------- | -------------- |
| Pointers per node       | 1 (next) | 2 (prev, next) |
| Space                   | O(n)     | O(2n)          |
| Delete node (ref given) | O(n)     | O(1)           |
| Reverse traversal       | Hard     | Easy           |
| Memory overhead         | Lower    | Higher         |
| Implementation          | Simpler  | Complex        |

## Memory Footprint

```
Singly:  Node = data + 1 pointer
Doubly:  Node = data + 2 pointers (2x overhead)
```

## Circular Doubly Linked List

```python
# Last node's next points to head
# Head's prev points to last node
tail.next = head
head.prev = tail
```

### Benefits of Circular Doubly

- Access both ends in O(1)
- Continuous circular navigation
- Used in deque implementations
