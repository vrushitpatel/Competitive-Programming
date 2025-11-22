# Queue Cheat Sheet

Queue is a linear data structure that follows the FIFO (First In First Out) principle. Elements are added at the rear and removed from the front. Think of it like a line of people waiting - first person in line is served first.

## Structure

Initializing a Queue Class

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()  # Initialize deque for O(1) operations
```

## Time & Space Complexity

| Operation | Time | Space |
| --------- | ---- | ----- |
| Enqueue   | O(1) | O(1)  |
| Dequeue   | O(1) | O(1)  |
| Peek      | O(1) | O(1)  |
| isEmpty   | O(1) | O(1)  |
| Search    | O(n) | O(1)  |

Note: Using `deque` is more efficient than list for queue operations.

## Core Operations

### 1. Enqueue (Insert)

```python
def enqueue(self, data):
    self.items.append(data)  # Add element to the right end
```

### 2. Dequeue (Remove)

```python
def dequeue(self):
    if self.is_empty():
        return None  # or raise exception
    return self.items.popleft()  # Remove from left end
```

### 3. Peek/Front

```python
def peek(self):
    if self.is_empty():
        return None  # or raise exception
    return self.items[0]  # Return leftmost element
```

### 4. isEmpty & Size

```python
def is_empty(self):
    return len(self.items) == 0

def size(self):
    return len(self.items)
```

## Queue Variations

### 1. Circular Queue

```python
class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.size = k
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            return False  # Queue is full
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        return True

    def dequeue(self):
        if self.front == -1:
            return None  # Queue is empty
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data
```

### 2. Priority Queue

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[1]
```

### 3. Deque (Double-ended Queue)

```python
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def add_front(self, data):
        self.items.appendleft(data)

    def add_rear(self, data):
        self.items.append(data)

    def remove_front(self):
        return self.items.popleft() if self.items else None

    def remove_rear(self):
        return self.items.pop() if self.items else None
```

## Common Queue Patterns

### 1. BFS Traversal (Tree/Graph)

```python
from collections import deque

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### 2. Sliding Window Maximum

```python
from collections import deque

def max_sliding_window(nums, k):
    result = []
    q = deque()  # Store indices
    for i in range(len(nums)):
        # Remove elements outside window
        if q and q[0] < i - k + 1:
            q.popleft()
        # Remove smaller elements
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            result.append(nums[q[0]])
    return result
```

### 3. Generate Binary Numbers

```python
from collections import deque

def generate_binary(n):
    queue = deque(['1'])
    result = []
    for _ in range(n):
        binary = queue.popleft()
        result.append(binary)
        queue.append(binary + '0')
        queue.append(binary + '1')
    return result
```

### 4. Level Order Traversal

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

## Key Patterns to Remember

1. **Level Order Traversal**: BFS in trees/graphs
2. **Sliding Window**: Using deque for efficient window operations
3. **Monotonic Queue**: Maintain increasing/decreasing order
4. **Producer-Consumer**: Task scheduling, buffering
5. **State Machines**: Game development, simulations

## Common Pitfalls

- Using list.pop(0) instead of deque.popleft() (O(n) vs O(1))
- Not checking for empty queue before dequeue/peek
- Forgetting to handle circular queue overflow
- Confusion between front and rear pointers

## Interview Tips

- Always prefer `deque` over list for queue operations
- Clarify: Is there a size limit? (circular queue)
- Consider: Priority queue for special ordering
- Think about: BFS applications
- Test: Empty queue, single element, full queue (circular)
- Common problems: Level order traversal, shortest path, task scheduling

## Real-world Applications

- BFS in graphs and trees
- Task scheduling (CPU, printer queues)
- Request handling in web servers
- Message queues in distributed systems
- Call center systems
- Playlist management
