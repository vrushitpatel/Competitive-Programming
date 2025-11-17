## Common Interview Problems

### 1. Reverse Doubly Linked List

```python
def reverse(self):
    curr = self.head
    temp = None

    while curr:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev

    if temp:
        self.head = temp.prev
```

### 2. Find Pairs with Given Sum

```python
def find_pairs_with_sum(self, target):
    pairs = []
    first = self.head
    last = self.head

    # Find last node
    while last.next:
        last = last.next

    # Two pointer approach
    while first != last and last.next != first:
        curr_sum = first.data + last.data

        if curr_sum == target:
            pairs.append((first.data, last.data))
            first = first.next
            last = last.prev
        elif curr_sum < target:
            first = first.next
        else:
            last = last.prev

    return pairs
```

### 3. Remove Duplicates (Sorted)

```python
def remove_duplicates(self):
    curr = self.head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
            if curr.next:
                curr.next.prev = curr
        else:
            curr = curr.next
```

### 4. Rotate by N Nodes

```python
def rotate(self, n):
    if not self.head or n == 0:
        return

    # Find nth node
    curr = self.head
    count = 1
    while count < n and curr:
        curr = curr.next
        count += 1

    if not curr:
        return

    nth_node = curr

    # Go to last node
    while curr.next:
        curr = curr.next

    # Make circular
    curr.next = self.head
    self.head.prev = curr

    # Break link
    self.head = nth_node.next
    self.head.prev = None
    nth_node.next = None
```

### 5. LRU Cache Implementation

```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add_to_head(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

### 6. Clone List with Random Pointer

```python
def clone_list(head):
    if not head:
        return None

    # Step 1: Create copy nodes
    curr = head
    while curr:
        new_node = Node(curr.data)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next

    # Step 2: Set prev/random pointers
    curr = head
    while curr:
        if curr.prev:
            curr.next.prev = curr.prev.next
        curr = curr.next.next

    # Step 3: Separate lists
    curr = head
    new_head = head.next
    while curr:
        clone = curr.next
        curr.next = clone.next
        if clone.next:
            clone.next = clone.next.next
        curr = curr.next

    return new_head
```
