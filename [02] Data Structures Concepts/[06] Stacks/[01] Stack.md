# Stack Cheat Sheet

Stack is a linear data structure that follows the LIFO (Last In First Out) principle. Elements are added and removed from the same end, called the top. Think of it like a stack of plates - you can only add or remove from the top.

## Structure

Initializing a Stack Class

```python
class Stack:
    def __init__(self):
        self.items = []  # Initialize empty list to store stack elements
```

## Time & Space Complexity

| Operation | Time | Space |
| --------- | ---- | ----- |
| Push      | O(1) | O(1)  |
| Pop       | O(1) | O(1)  |
| Peek/Top  | O(1) | O(1)  |
| Search    | O(n) | O(1)  |
| isEmpty   | O(1) | O(1)  |

## Core Operations

### 1. Push (Insert)

```python
def push(self, data):
    self.items.append(data)
```

### 2. Pop (Remove)

```python
def pop(self):
    if self.is_empty():
        return None  # or raise exception
    return self.items.pop()
```

### 3. Peek/Top

```python
def peek(self):
    if self.is_empty():
        return None  # or raise exception
    return self.items[-1]
```

### 4. isEmpty & Size

```python
def is_empty(self):
    return len(self.items) == 0

def size(self):
    return len(self.items)
```

## Common Stack Patterns

### 1. Evaluate Postfix Expression

```python
def evaluate_postfix(expression):
    stack = []
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+': stack.append(a + b)
            elif char == '-': stack.append(a - b)
            elif char == '*': stack.append(a * b)
            elif char == '/': stack.append(a // b)
    return stack.pop()
```

## Key Patterns to Remember

1. **Monotonic Stack**: Maintain increasing/decreasing order
2. **Expression Evaluation**: Infix, prefix, postfix conversions
3. **Backtracking**: DFS, path finding, undo operations
4. **Function Call Stack**: Recursion simulation
5. **Min/Max Stack**: Track minimum/maximum with each push

## Common Pitfalls

- Not checking for empty stack before pop/peek
- Confusion between stack.pop() (removes) and stack[-1] (peeks)
- Off-by-one errors when iterating
- Forgetting to handle edge cases (empty/single element)

## Interview Tips

- Always ask: What should happen on empty stack?
- Clarify: Is there a size limit?
- Consider: Can we use extra space?
- Think about: Auxiliary stack for optimization
- Test: Empty stack, single element, multiple elements
- Common problems: Expression parsing, browser history, undo/redo

## Real-world Applications

- Function call stack (recursion)
- Browser back button
- Undo/Redo operations
- Expression evaluation
- DFS traversal
- Syntax parsing in compilers
