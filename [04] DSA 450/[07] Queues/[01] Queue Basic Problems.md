## Basic Queue Problems

### 1. Implement Queue using Stacks

```python
class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        self.input_stack.append(x)

    def pop(self):
        self._transfer()
        return self.output_stack.pop()

    def peek(self):
        self._transfer()
        return self.output_stack[-1]

    def empty(self):
        return not self.input_stack and not self.output_stack

    def _transfer(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
```

**Time Complexity:** Push O(1), Pop/Peek amortized O(1)
**Space Complexity:** O(n)

---

### 2. Implement Stack using Queues

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        # Rotate queue to make last element first
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
```

**Time Complexity:** Push O(n), Pop/Top O(1)
**Space Complexity:** O(n)

---

### 3. Number of Recent Calls

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)
        # Remove calls older than 3000ms
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
```

**Time Complexity:** O(1) amortized
**Space Complexity:** O(n)

---

### 4. First Unique Character in String

```python
from collections import Counter

def firstUniqChar(s):
    count = Counter(s)

    for i, char in enumerate(s):
        if count[char] == 1:
            return i

    return -1
```

**Alternative using Queue:**
```python
from collections import deque, defaultdict

def firstUniqChar(s):
    count = defaultdict(int)
    queue = deque()

    for i, char in enumerate(s):
        count[char] += 1
        queue.append((char, i))

        while queue and count[queue[0][0]] > 1:
            queue.popleft()

    return queue[0][1] if queue else -1
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) - max 26 characters

---

### 5. Design Circular Queue

```python
class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] * k
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self):
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
```

**Time Complexity:** O(1) for all operations
**Space Complexity:** O(k)

---

### 6. Time Needed to Buy Tickets

```python
def timeRequiredToBuy(tickets, k):
    time = 0

    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[i], tickets[k])
        else:
            time += min(tickets[i], tickets[k] - 1)

    return time
```

**Alternative using Queue:**
```python
from collections import deque

def timeRequiredToBuy(tickets, k):
    queue = deque([(tickets[i], i) for i in range(len(tickets))])
    time = 0

    while queue:
        tickets_left, index = queue.popleft()
        time += 1
        tickets_left -= 1

        if index == k and tickets_left == 0:
            return time

        if tickets_left > 0:
            queue.append((tickets_left, index))

    return time
```

**Time Complexity:** O(n * max(tickets))
**Space Complexity:** O(n)
