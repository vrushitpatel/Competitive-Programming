## Advanced Stack Problems

### 1. Evaluate Reverse Polish Notation

```python
def evalRPN(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Truncate towards zero
        else:
            stack.append(int(token))

    return stack[0]
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 2. Basic Calculator

```python
def calculate(s):
    stack = []
    num = 0
    sign = 1
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  # pop sign
            result += stack.pop()  # pop result

    result += sign * num
    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 3. Basic Calculator II

```python
def calculate(s):
    stack = []
    num = 0
    operator = '+'

    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)

        if char in '+-*/' or i == len(s) - 1:
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                stack.append(int(stack.pop() / num))

            if i < len(s) - 1:
                operator = char
                num = 0

    return sum(stack)
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 4. Decode String

```python
def decodeString(s):
    stack = []
    curr_num = 0
    curr_str = ''

    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str = ''
            curr_num = 0
        elif char == ']':
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += char

    return curr_str
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 5. Asteroid Collision

```python
def asteroidCollision(asteroids):
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)

    return stack
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 6. Simplify Path

```python
def simplifyPath(path):
    stack = []
    parts = path.split('/')

    for part in parts:
        if part == '..' and stack:
            stack.pop()
        elif part and part != '.' and part != '..':
            stack.append(part)

    return '/' + '/'.join(stack)
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 7. Remove K Digits

```python
def removeKdigits(num, k):
    stack = []

    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # Remove remaining k digits from end
    stack = stack[:len(stack) - k]

    # Remove leading zeros and return
    result = ''.join(stack).lstrip('0')
    return result if result else '0'
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)
