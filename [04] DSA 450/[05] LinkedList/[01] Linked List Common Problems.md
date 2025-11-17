## Common Interview Problems

### 1. Reverse Linked List

```python
# Iterative
def reverse_iterative(self):
    prev = None
    curr = self.head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    self.head = prev

# Recursive
def reverse_recursive(self, node):
    if not node or not node.next:
        return node
    new_head = self.reverse_recursive(node.next)
    node.next.next = node
    node.next = None
    return new_head
```

### 2. Merge Two Sorted Lists

```python
def merge_sorted(self, l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

### 3. Remove Duplicates (Sorted)

```python
def remove_duplicates(self):
    curr = self.head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
```

### 4. Palindrome Check

```python
def is_palindrome(self):
    # Find middle
    slow = fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Compare
    left, right = self.head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    return True
```

### 5. Intersection of Two Lists

```python
def get_intersection(self, head1, head2):
    if not head1 or not head2:
        return None
    a, b = head1, head2
    while a != b:
        a = a.next if a else head2
        b = b.next if b else head1
    return a
```
