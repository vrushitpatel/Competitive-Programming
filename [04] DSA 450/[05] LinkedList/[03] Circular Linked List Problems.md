## Common Interview Problems

### 1. Check if List is Circular

```python
def is_circular(head):
    if not head:
        return False
    curr = head.next
    while curr and curr != head:
        curr = curr.next
    return curr == head
```

### 2. Split Circular List into Two Halves

```python
def split_list(self):
    if not self.head or self.head.next == self.head:
        return None, None

    slow = fast = self.head
    while fast.next != self.head and fast.next.next != self.head:
        slow = slow.next
        fast = fast.next.next

    # If even number of nodes
    if fast.next.next == self.head:
        fast = fast.next

    head1 = self.head
    head2 = slow.next

    # Make first half circular
    slow.next = head1

    # Make second half circular
    fast.next = head2

    return head1, head2
```

### 3. Josephus Problem

```python
def josephus(n, k):
    # Create circular list with n nodes
    head = Node(1)
    prev = head
    for i in range(2, n + 1):
        prev.next = Node(i)
        prev = prev.next
    prev.next = head  # Make circular

    # Eliminate every k-th person
    curr = head
    while curr.next != curr:
        for _ in range(k - 1):
            curr = curr.next
        # Remove next node
        curr.next = curr.next.next

    return curr.data  # Last survivor
```

### 4. Convert Singly to Circular

```python
def make_circular(head):
    if not head:
        return head
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = head
    return head
```

### 5. Sorted Insert in Circular List

```python
def sorted_insert(self, data):
    new_node = Node(data)

    # Empty list
    if not self.head:
        self.head = new_node
        new_node.next = self.head
        return

    curr = self.head

    # Insert at beginning
    if data < self.head.data:
        while curr.next != self.head:
            curr = curr.next
        new_node.next = self.head
        curr.next = new_node
        self.head = new_node
        return

    # Find position to insert
    while curr.next != self.head and curr.next.data < data:
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node
```
