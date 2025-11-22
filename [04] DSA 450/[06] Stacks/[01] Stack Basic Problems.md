## Basic Stack Problems

### 1. Valid Parentheses

```python
def isValid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0
```

**Time Complexity:** O(n)
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

### 3. Min Stack

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

**Time Complexity:** O(1) for all operations
**Space Complexity:** O(n)

---

### 4. Implement Queue using Stacks

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

OR

```python
class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)


    def pop(self):
        """
        :rtype: int
        """
        print(self.stack)
        popped = self.stack[0]
        for x in range(1, len(self.stack)):
            self.temp.append(self.stack[x])
        self.stack = self.temp
        self.temp = []
        return popped

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return False if len(self.stack) else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

**Time Complexity:** Push O(1), Pop/Peek amortized O(1)
**Space Complexity:** O(n)

---

### 5. Backspace String Compare

```python
def backspaceCompare(s, t):
    def build_string(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)

    return build_string(s) == build_string(t)
```

**Time Complexity:** O(n + m)
**Space Complexity:** O(n + m)

---

### 6. Baseball Game

```python
def calPoints(operations):
    stack = []

    for op in operations:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 7. Remove All Adjacent Duplicates

```python
def removeDuplicates(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)
