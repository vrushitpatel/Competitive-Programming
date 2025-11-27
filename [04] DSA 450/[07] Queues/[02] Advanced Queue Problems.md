## Advanced Queue Problems

### 1. Sliding Window Maximum

```python
from collections import deque

def maxSlidingWindow(nums, k):
    result = []
    queue = deque()  # Store indices

    for i in range(len(nums)):
        # Remove elements outside window
        if queue and queue[0] < i - k + 1:
            queue.popleft()

        # Remove smaller elements from rear
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()

        queue.append(i)

        # Add to result after first window
        if i >= k - 1:
            result.append(nums[queue[0]])

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(k)

---

### 2. Task Scheduler

```python
from collections import Counter
import heapq

def leastInterval(tasks, n):
    count = Counter(tasks)
    max_heap = [-freq for freq in count.values()]
    heapq.heapify(max_heap)

    time = 0
    queue = deque()  # (freq, available_time)

    while max_heap or queue:
        time += 1

        if max_heap:
            freq = heapq.heappop(max_heap) + 1
            if freq < 0:
                queue.append((freq, time + n))

        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.popleft()[0])

    return time
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) - at most 26 tasks

---

### 3. Design Hit Counter

```python
from collections import deque

class HitCounter:
    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp):
        self.queue.append(timestamp)

    def getHits(self, timestamp):
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        return len(self.queue)
```

**Time Complexity:** hit O(1), getHits O(n)
**Space Complexity:** O(n)

---

### 4. Shortest Path in Binary Matrix

```python
from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    if n == 1:
        return 1

    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # Mark visited

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]

    while queue:
        r, c, dist = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if nr == n - 1 and nc == n - 1:
                return dist + 1

            if (0 <= nr < n and 0 <= nc < n and
                grid[nr][nc] == 0):
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))

    return -1
```

**Time Complexity:** O(n²)
**Space Complexity:** O(n²)

---

### 5. Open the Lock

```python
from collections import deque

def openLock(deadends, target):
    dead = set(deadends)
    if "0000" in dead:
        return -1

    queue = deque([("0000", 0)])
    visited = {"0000"}

    def get_neighbors(code):
        neighbors = []
        for i in range(4):
            digit = int(code[i])
            for move in [-1, 1]:
                new_digit = (digit + move) % 10
                neighbor = code[:i] + str(new_digit) + code[i+1:]
                neighbors.append(neighbor)
        return neighbors

    while queue:
        code, steps = queue.popleft()

        if code == target:
            return steps

        for neighbor in get_neighbors(code):
            if neighbor not in visited and neighbor not in dead:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))

    return -1
```

**Time Complexity:** O(10^4) - 10000 possible combinations
**Space Complexity:** O(10^4)

---

### 6. Snakes and Ladders

```python
from collections import deque

def snakesAndLadders(board):
    n = len(board)

    def get_position(square):
        row = (square - 1) // n
        col = (square - 1) % n
        if row % 2 == 1:
            col = n - 1 - col
        return n - 1 - row, col

    queue = deque([(1, 0)])  # (square, moves)
    visited = {1}

    while queue:
        square, moves = queue.popleft()

        if square == n * n:
            return moves

        for next_square in range(square + 1, min(square + 6, n * n) + 1):
            r, c = get_position(next_square)
            destination = board[r][c] if board[r][c] != -1 else next_square

            if destination not in visited:
                visited.add(destination)
                queue.append((destination, moves + 1))

    return -1
```

**Time Complexity:** O(n²)
**Space Complexity:** O(n²)

---

### 7. Jump Game III

```python
from collections import deque

def canReach(arr, start):
    n = len(arr)
    queue = deque([start])
    visited = {start}

    while queue:
        idx = queue.popleft()

        if arr[idx] == 0:
            return True

        for next_idx in [idx + arr[idx], idx - arr[idx]]:
            if 0 <= next_idx < n and next_idx not in visited:
                visited.add(next_idx)
                queue.append(next_idx)

    return False
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)
