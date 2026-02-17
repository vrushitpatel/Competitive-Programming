# Sliding Window Cheat Sheet

Sliding Window is an algorithmic technique used to solve problems involving arrays or strings by maintaining a window (subarray/substring) that slides through the data structure. This technique efficiently reduces time complexity from O(n²) to O(n) for many problems.

## Core Concept

The sliding window technique involves:

1. Creating a window (subarray) from start to end index
2. Expanding or contracting the window based on conditions
3. Processing elements as they enter/exit the window
4. Maintaining window state efficiently

## Types of Sliding Window

### 1. Fixed Size Window

```python
def fixed_window(arr, k):
    """Window size is constant throughout"""
    n = len(arr)
    window_sum = sum(arr[:k])  # Initial window
    max_sum = window_sum

    # Slide window
    for i in range(k, n):
        window_sum += arr[i] - arr[i-k]  # Add new, remove old
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### 2. Dynamic/Variable Size Window

```python
def variable_window(arr, target):
    """Window size changes based on condition"""
    left = 0
    window_sum = 0
    result = 0

    for right in range(len(arr)):
        # Expand window
        window_sum += arr[right]

        # Contract window while condition is violated
        while window_sum > target:
            window_sum -= arr[left]
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result
```

## Time & Space Complexity

| Type            | Time | Space        | Use Case                        |
| --------------- | ---- | ------------ | ------------------------------- |
| Fixed Window    | O(n) | O(1)         | Fixed size subarray problems    |
| Variable Window | O(n) | O(1) to O(k) | Dynamic size based on condition |
| With Hash Map   | O(n) | O(k)         | Substring with unique chars     |

Note: Each element is visited at most twice (once by right, once by left pointer).

## Common Patterns

### Pattern 1: Maximum/Minimum Sum of Fixed Size Subarray

```python
def max_sum_subarray(arr, k):
    """Find maximum sum of subarray of size k"""
    if len(arr) < k:
        return -1

    # Calculate first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Time: O(n), Space: O(1)
```

### Pattern 2: Longest Substring with K Distinct Characters

```python
def longest_substring_k_distinct(s, k):
    """Find longest substring with at most k distinct characters"""
    char_freq = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Add character to window
        char_freq[s[right]] = char_freq.get(s[right], 0) + 1

        # Shrink window if more than k distinct
        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Time: O(n), Space: O(k)
```

### Pattern 3: Minimum Window Substring (Template)

```python
def min_window_substring(s, t):
    """Find minimum window containing all characters of t"""
    n = len(str)


    # to store all distinct characters
    visited = [False] * 26
    distinct = 0

    for i in range(n):
        if visited[ord(str[i]) - ord('a')] == False:
            visited[ord(str[i]) - ord('a')] = True
            distinct += 1


    # to store the visited of characters

    # in the current window
    cur = [0] * 26
    cnt = 0

    ans = n
    start = 0
    for i in range(n):
        cur[ord(str[i]) - ord('a')] += 1

        if cur[ord(str[i]) - ord('a')] == 1:
            cnt += 1
        while cnt == distinct:
            ans = min(ans, i - start + 1)
            cur[ord(str[start]) - ord('a')] -= 1
            if cur[ord(str[start]) - ord('a')] == 0:
                cnt -= 1
            start += 1
    return ans

# Time: O(n + m), Space: O(n + m)
```

### Pattern 4: Longest Substring Without Repeating Characters

```python
def length_longest_substring(s):
    """Find length of longest substring without repeating characters"""
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If character seen and in current window
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Time: O(n), Space: O(min(n, m)) where m is charset size
```

### Pattern 5: Count Subarrays with Product Less Than K

```python
def num_subarray_product_less_than_k(nums, k):
    """Count subarrays where product is less than k"""
    if k <= 1:
        return 0

    product = 1
    left = 0
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        # All subarrays ending at right
        count += right - left + 1

    return count

# Time: O(n), Space: O(1)
```

### Pattern 6: Maximum of All Subarrays of Size K

```python
from collections import deque

def max_sliding_window(nums, k):
    """Find maximum element in each window of size k"""
    if not nums:
        return []

    result = []
    deq = deque()  # Store indices

    for i in range(len(nums)):
        # Remove indices outside window
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove smaller elements (not useful)
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        # Add to result when window is full
        if i >= k - 1:
            result.append(nums[deq[0]])

    return result

# Time: O(n), Space: O(k)
```

### Pattern 7: Fruits Into Baskets (At Most 2 Types)

```python
def total_fruit(fruits):
    """Maximum fruits with at most 2 types"""
    basket = {}
    left = 0
    max_fruits = 0

    for right in range(len(fruits)):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1

        # More than 2 types
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

# Time: O(n), Space: O(1) - at most 3 types in basket
```

## Sliding Window Template

```python
def sliding_window_template(arr, condition):
    """Generic sliding window template"""
    left = 0
    state = initialize_state()  # Hash map, counter, sum, etc.
    result = initialize_result()

    for right in range(len(arr)):
        # 1. Add arr[right] to window
        update_state_with_right(state, arr[right])

        # 2. Shrink window if condition violated
        while window_condition_violated(state, condition):
            remove_from_state(state, arr[left])
            left += 1

        # 3. Update result
        result = update_result(result, left, right, state)

    return result
```

## Step-by-Step Approach

1. **Identify if sliding window applies:**

   - Contiguous subarray/substring problem
   - Asks for longest/shortest/count
   - Has optimization from O(n²) to O(n) potential

2. **Choose window type:**

   - Fixed size: Window length is given
   - Variable size: Find optimal window based on condition

3. **Track window state:**

   - Use variables for sum, product, count
   - Use hash map for character/element frequency
   - Use deque for maintaining max/min

4. **Define window validity:**

   - What makes a window valid?
   - When to expand? When to shrink?

5. **Update result:**
   - After expansion? After contraction? Both?

## Common Variations

### With Hash Map (Character Frequency)

```python
def character_frequency_window(s, pattern):
    from collections import Counter

    pattern_count = Counter(pattern)
    window_count = {}
    matched = 0
    left = 0

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in pattern_count and window_count[char] == pattern_count[char]:
            matched += 1

        # Process window when all matched
        while matched == len(pattern_count):
            # Update result here

            # Shrink window
            left_char = s[left]
            if left_char in pattern_count and window_count[left_char] == pattern_count[left_char]:
                matched -= 1
            window_count[left_char] -= 1
            left += 1

    return result
```

### With Deque (Monotonic Queue)

```python
from collections import deque

def sliding_window_maximum(nums, k):
    """Maintain decreasing deque for max"""
    deq = deque()
    result = []

    for i in range(len(nums)):
        # Remove out of window
        if deq and deq[0] <= i - k:
            deq.popleft()

        # Maintain decreasing order
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(nums[deq[0]])

    return result
```

## Key Patterns to Remember

1. **Fixed Window**: Sum/avg of k elements
2. **Variable Window**: Longest/shortest with condition
3. **Two Distinct**: At most k distinct elements
4. **Anagram/Permutation**: Pattern matching in string
5. **Monotonic Deque**: Max/min in sliding window
6. **Count Subarrays**: Product/sum with condition

## Common Pitfalls

- Forgetting to handle empty input
- Not initializing first window correctly for fixed size
- Off-by-one errors in window size calculation
- Not updating state when removing left element
- Infinite loop when shrinking condition never met
- Using wrong comparison (< vs <=) for window validity

## Interview Tips

- Ask: Is the window size fixed or variable?
- Clarify: What defines a valid window?
- Consider: What to track (sum, count, frequency)?
- Think about: When to expand vs when to contract
- Edge cases: Empty array, k > n, all same elements
- Optimization: Can we avoid recalculating entire window?

## When to Use Sliding Window

✅ **Use when:**

- Finding subarray/substring with specific properties
- Contiguous elements are required
- Problem asks for longest/shortest/count
- Can optimize from O(n²) to O(n)
- Window state can be efficiently maintained

❌ **Don't use when:**

- Elements need not be contiguous
- Need to find all subarrays (might need different approach)
- Problem requires sorting
- Random access to all elements needed

## Problem Recognition Checklist

- [ ] Involves array/string
- [ ] Asks for contiguous subarray/substring
- [ ] Contains keywords: longest, shortest, maximum, minimum, count
- [ ] Condition involves window elements (sum, product, distinct)
- [ ] Current O(n²) brute force can be optimized

## Real-world Applications

- Network packet analysis (detecting patterns)
- Stock market (moving averages)
- String matching algorithms
- Real-time data stream processing
- Image processing (convolution)
- Rate limiting (request windows)
- Time series analysis
- DNA sequence analysis

## LeetCode Problems by Pattern

**Fixed Window:**

- Maximum Average Subarray I (643)
- Find All Anagrams in a String (438)
- Permutation in String (567)

**Variable Window:**

- Longest Substring Without Repeating Characters (3)
- Minimum Window Substring (76)
- Longest Substring with At Most K Distinct Characters (340)
- Subarrays with K Different Integers (992)

**Monotonic Deque:**

- Sliding Window Maximum (239)
- Shortest Subarray with Sum at Least K (862)

**Count Subarrays:**

- Subarray Product Less Than K (713)
- Count Number of Nice Subarrays (1248)
