## Monotonic Stack Problems

### 1. Next Greater Element I

```python
def nextGreaterElement(nums1, nums2):
    # Build next greater mapping for nums2
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    # For remaining elements, no greater element exists
    while stack:
        next_greater[stack.pop()] = -1

    return [next_greater[num] for num in nums1]
```

**Time Complexity:** O(n + m)
**Space Complexity:** O(n)

---

### 2. Next Greater Element II

```python
def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    # Traverse twice for circular array
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 3. Daily Temperatures

```python
def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 4. Largest Rectangle in Histogram

```python
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel value

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 5. Trapping Rain Water

```python
def trap(height):
    if not height:
        return 0

    stack = []
    water = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()
            if not stack:
                break

            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[bottom]
            water += distance * bounded_height

        stack.append(i)

    return water
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 6. Sum of Subarray Minimums

```python
def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    n = len(arr)

    # Find previous less element
    left = [0] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    # Find next less element
    right = [0] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    # Calculate sum
    result = 0
    for i in range(n):
        result += arr[i] * (i - left[i]) * (right[i] - i)
        result %= MOD

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 7. Online Stock Span

```python
class StockSpanner:
    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
```

**Time Complexity:** Amortized O(1)
**Space Complexity:** O(n)
