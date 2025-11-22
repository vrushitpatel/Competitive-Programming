## BFS & Level Order Problems

### 1. Binary Tree Level Order Traversal

```python
from collections import deque

def levelOrder(root):
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

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 2. Binary Tree Zigzag Level Order

```python
from collections import deque

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 3. Binary Tree Right Side View

```python
from collections import deque

def rightSideView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # Add rightmost element of each level
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 4. Average of Levels in Binary Tree

```python
from collections import deque

def averageOfLevels(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_size)

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 5. Rotting Oranges

```python
from collections import deque

def orangesRotting(grid):
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Find all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_count += 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0

    while queue:
        r, c, time = queue.popleft()
        max_time = max(max_time, time)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_count -= 1
                queue.append((nr, nc, time + 1))

    return max_time if fresh_count == 0 else -1
```

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n)

---

### 6. Walls and Gates

```python
from collections import deque

def wallsAndGates(rooms):
    if not rooms:
        return

    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    # Find all gates
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                rooms[nr][nc] == 2147483647):
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))
```

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n)

---

### 7. Number of Islands

```python
from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == '1'):
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                bfs(r, c)
                count += 1

    return count
```

**Time Complexity:** O(m * n)
**Space Complexity:** O(min(m, n))
