# Circular Linked List Cheat Sheet

## Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
```

## Key Difference

- Last node points back to head instead of None
- `last.next = head` (circular connection)

## Visual Representation

```
[1] → [2] → [3] → [4]
 ↑__________________|
```

## Time & Space Complexity

| Operation          | Time             | Space |
| ------------------ | ---------------- | ----- |
| Access             | O(n)             | O(1)  |
| Search             | O(n)             | O(1)  |
| Insert (beginning) | O(1)\*           | O(1)  |
| Insert (end)       | O(n) or O(1)\*\* | O(1)  |
| Delete             | O(n)             | O(1)  |

\*O(1) if we maintain tail pointer
\*\*O(1) with tail pointer, O(n) without

## Core Operations

### 1. Insertion at Beginning

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        new_node.next = self.head
        return

    curr = self.head
    while curr.next != self.head:
        curr = curr.next

    new_node.next = self.head
    curr.next = new_node
    self.head = new_node
```

### 2. Insertion at End

```python
def insert_at_end(self, data):
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
```

### 3. Deletion

```python
def delete_node(self, key):
    if not self.head:
        return

    # If head needs to be deleted
    if self.head.data == key:
        if self.head.next == self.head:  # Single node
            self.head = None
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = self.head.next
        self.head = self.head.next
        return

    # Delete other nodes
    curr = self.head
    while curr.next != self.head:
        if curr.next.data == key:
            curr.next = curr.next.next
            return
        curr = curr.next
```

### 4. Traversal

```python
def print_list(self):
    if not self.head:
        return
    curr = self.head
    while True:
        print(curr.data, end=" -> ")
        curr = curr.next
        if curr == self.head:
            break
    print("(back to head)")
```

### 5. Length Calculation

```python
def length(self):
    if not self.head:
        return 0
    count = 1
    curr = self.head.next
    while curr != self.head:
        count += 1
        curr = curr.next
    return count
```

## Optimized Version (with Tail Pointer)

### Structure with Tail

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Maintains reference to last node
```

### Insert at End - O(1)

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = self.tail = new_node
        new_node.next = self.head
        return

    self.tail.next = new_node
    new_node.next = self.head
    self.tail = new_node
```

### Insert at Beginning - O(1)

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = self.tail = new_node
        new_node.next = self.head
        return

    new_node.next = self.head
    self.tail.next = new_node
    self.head = new_node
```

## Advantages

1. Can traverse entire list from any node
2. Useful for round-robin scheduling
3. No need to track beginning/end separately
4. Useful in applications that need circular behavior

## Disadvantages

1. More complex to implement
2. Infinite loop risk if not careful
3. Cannot use NULL to detect end
4. Harder to debug

## Use Cases

- Round Robin scheduling (CPU, process)
- Multiplayer games (turn rotation)
- Music playlists (repeat mode)
- Browser tab cycling
- Undo/Redo with circular buffer

## Key Patterns

1. **Loop Termination**: Always use `curr.next != head`
2. **Empty Check**: `if not self.head`
3. **Single Node**: `if self.head.next == self.head`
4. **Maintain Tail**: For O(1) end operations

## Common Pitfalls

- Forgetting to make last node point to head
- Infinite loops in traversal
- Not handling single node case
- Breaking circular link during deletion

## Interview Tips

- Always clarify: Is it circular or singly?
- Ask: Can we use tail pointer?
- Check: Single node edge case
- Discuss: How to detect end of list
- Test: Empty, single, two nodes, multiple nodes

## Quick Comparison

| Feature             | Singly       | Circular          |
| ------------------- | ------------ | ----------------- |
| Last node points to | None         | Head              |
| Traversal end       | curr == None | curr.next == head |
| Can reach any node  | No           | Yes               |
| Memory              | Same         | Same              |
