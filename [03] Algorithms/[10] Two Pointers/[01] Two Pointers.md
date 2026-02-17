# Two Pointers Cheat Sheet

Two Pointers is an algorithmic technique that uses two pointers to iterate through a data structure (usually an array or linked list) to solve problems efficiently. This technique often reduces time complexity from O(n²) to O(n) and is commonly used in sorted arrays.

## Core Concept

The two pointers technique involves:
1. Using two pointers that move through the data structure
2. Pointers can move in same or opposite directions
3. Decision on pointer movement based on comparison or condition
4. Efficiently solving problems without nested loops

## Types of Two Pointers

### 1. Opposite Direction (Convergent)

```python
def opposite_pointers(arr):
    """Pointers start at opposite ends and move toward each other"""
    left = 0
    right = len(arr) - 1

    while left < right:
        # Process arr[left] and arr[right]
        if condition_met:
            return result
        elif move_left:
            left += 1
        else:
            right -= 1

    return result
```

### 2. Same Direction (Parallel/Fast-Slow)

```python
def same_direction_pointers(arr):
    """Both pointers start at same end and move in same direction"""
    slow = 0
    fast = 0

    while fast < len(arr):
        # Process arr[fast]
        if condition:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1

    return slow
```

### 3. Fast and Slow (Floyd's Cycle Detection)

```python
def fast_slow_pointers(head):
    """Fast moves twice as fast as slow - for cycle detection"""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # Cycle detected

    return False
```

## Time & Space Complexity

| Pattern | Time | Space | Use Case |
| ------- | ---- | ----- | -------- |
| Opposite Direction | O(n) | O(1) | Sorted array, palindrome |
| Same Direction | O(n) | O(1) | Remove duplicates, partition |
| Fast-Slow | O(n) | O(1) | Cycle detection, middle element |
| Three Pointers | O(n²) or O(n) | O(1) | 3Sum, partition |

Note: Usually achieves O(n) with O(1) extra space, better than nested loops O(n²).

## Common Patterns

### Pattern 1: Two Sum (Sorted Array)

```python
def two_sum_sorted(arr, target):
    """Find two numbers that sum to target in sorted array"""
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Time: O(n), Space: O(1)
```

### Pattern 2: Remove Duplicates from Sorted Array

```python
def remove_duplicates(nums):
    """Remove duplicates in-place, return new length"""
    if not nums:
        return 0

    slow = 0  # Position for next unique element

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

# Time: O(n), Space: O(1)
```

### Pattern 3: Valid Palindrome

```python
def is_palindrome(s):
    """Check if string is palindrome ignoring non-alphanumeric"""
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# Time: O(n), Space: O(1)
```

### Pattern 4: Container With Most Water

```python
def max_area(height):
    """Find two lines that form container with most water"""
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Calculate current area
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_water = max(max_water, current_area)

        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Time: O(n), Space: O(1)
```

### Pattern 5: Three Sum

```python
def three_sum(nums):
    """Find all triplets that sum to zero"""
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Two pointers for remaining two numbers
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result

# Time: O(n²), Space: O(1) excluding result
```

### Pattern 6: Move Zeros to End

```python
def move_zeros(nums):
    """Move all zeros to end while maintaining relative order"""
    slow = 0  # Position for next non-zero

    # Move all non-zeros to front
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums

# Time: O(n), Space: O(1)
```

### Pattern 7: Partition Array

```python
def partition(nums, pivot):
    """Partition array around pivot (like QuickSort)"""
    left = 0
    right = len(nums) - 1

    i = 0
    while i <= right:
        if nums[i] < pivot:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] > pivot:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1

    return nums

# Time: O(n), Space: O(1)
```

### Pattern 8: Linked List Cycle Detection (Floyd's)

```python
def has_cycle(head):
    """Detect cycle in linked list using fast-slow pointers"""
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Time: O(n), Space: O(1)
```

### Pattern 9: Find Cycle Start

```python
def detect_cycle(head):
    """Find the node where cycle begins"""
    if not head or not head.next:
        return None

    # Detect cycle
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# Time: O(n), Space: O(1)
```

### Pattern 10: Middle of Linked List

```python
def middle_node(head):
    """Find middle node of linked list"""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Time: O(n), Space: O(1)
```

### Pattern 11: Remove Nth Node From End

```python
def remove_nth_from_end(head, n):
    """Remove nth node from end of linked list"""
    dummy = ListNode(0)
    dummy.next = head

    slow = fast = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both until fast reaches end
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove node
    slow.next = slow.next.next

    return dummy.next

# Time: O(n), Space: O(1)
```

### Pattern 12: Dutch National Flag

```python
def sort_colors(nums):
    """Sort array of 0s, 1s, 2s in one pass"""
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

# Time: O(n), Space: O(1)
```

## Two Pointers Templates

### Template 1: Opposite Direction

```python
def opposite_direction_template(arr, target):
    """Start from both ends, move toward center"""
    left = 0
    right = len(arr) - 1

    while left < right:
        # Calculate current value
        current = process(arr[left], arr[right])

        # Check condition
        if current == target:
            return [left, right]
        elif current < target:
            left += 1  # Need larger value
        else:
            right -= 1  # Need smaller value

    return []
```

### Template 2: Same Direction (Slow-Fast)

```python
def same_direction_template(arr):
    """Slow for placement, fast for exploration"""
    slow = 0

    for fast in range(len(arr)):
        if condition(arr[fast]):
            arr[slow] = arr[fast]
            slow += 1

    return slow
```

### Template 3: Fast-Slow for Linked List

```python
def fast_slow_template(head):
    """Fast moves 2x speed of slow"""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if meets_condition(slow, fast):
            return result

    return None
```

### Template 4: Three Pointers

```python
def three_pointers_template(arr):
    """One fixed, two moving (for 3Sum variations)"""
    arr.sort()
    result = []

    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current = arr[i] + arr[left] + arr[right]

            if current == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif current < target:
                left += 1
            else:
                right -= 1

    return result
```

## Step-by-Step Approach

1. **Identify if two pointers applies:**
   - Array/list problem with linear scan
   - Needs to find pair/triplet
   - Can be optimized from O(n²) to O(n)
   - For linked list: cycle, middle, nth from end

2. **Choose pointer direction:**
   - Opposite: Sorted array, palindrome, pair sum
   - Same: Remove duplicates, partition, in-place modification
   - Fast-slow: Linked list problems, cycle detection

3. **Determine movement logic:**
   - When to move left? When to move right?
   - What condition triggers movement?
   - When do both move together?

4. **Handle edge cases:**
   - Empty array/list
   - Single element
   - All same elements
   - No valid answer exists

## Pointer Movement Decision Tree

```
Is array sorted?
├── Yes
│   ├── Finding pair sum? → Opposite direction
│   ├── Finding triplet? → Fixed + Two pointers
│   └── Remove duplicates? → Same direction
└── No
    ├── Linked list? → Fast-slow
    ├── Partition/rearrange? → Same direction or three pointers
    └── Palindrome check? → Opposite direction
```

## Key Patterns to Remember

1. **Sorted Array + Target Sum**: Opposite direction
2. **Remove/Modify In-Place**: Same direction (slow-fast)
3. **Linked List Cycle**: Fast-slow (Floyd's)
4. **Find Middle**: Fast-slow
5. **3Sum/4Sum**: Fixed pointer + two pointers
6. **Dutch Flag**: Three pointers (low, mid, high)
7. **Partition**: Same direction or opposite

## Common Pitfalls

- Forgetting to handle empty input
- Not checking array bounds (left < right)
- Moving wrong pointer in opposite direction
- Not skipping duplicates in 3Sum
- Incorrect loop condition (< vs <=)
- Forgetting to check fast.next for linked lists
- Not using dummy node for linked list removal
- Modifying array while iterating without care

## Interview Tips

- Ask: Is the array sorted? (Affects pointer strategy)
- Clarify: In-place modification allowed?
- Consider: Can we sort first? (Time trade-off)
- Think about: Which direction should pointers move?
- Edge cases: Empty, single element, no solution, duplicates
- Optimization: Better than O(n²)? Usually yes with two pointers
- Variation: Can extend to three/four pointers?

## When to Use Two Pointers

✅ **Use when:**

- Finding pairs/triplets in array
- Array is sorted or can be sorted
- Need O(1) space solution
- Removing/rearranging elements in-place
- Linked list problems (cycle, middle, nth from end)
- Palindrome checking
- Partition/Dutch flag problems

❌ **Don't use when:**

- Need to maintain original order (and can't sort)
- Random access to all elements needed
- Subarray/substring problems (use sliding window)
- Need to track all elements (use hash map)
- Problem requires backtracking

## Problem Recognition Checklist

- [ ] Involves array or linked list
- [ ] Finding pairs, triplets, or partitions
- [ ] Array is sorted or can be sorted
- [ ] Asks for in-place modification
- [ ] Linked list cycle/middle/palindrome
- [ ] Can optimize from O(n²) to O(n)

## Two Pointers vs Other Techniques

| Two Pointers | Sliding Window | Hash Map |
| ------------ | -------------- | -------- |
| Pairs/triplets | Contiguous subarray | Any elements |
| Often sorted | Order matters | Order doesn't matter |
| O(1) space | O(1) to O(k) space | O(n) space |
| Move based on comparison | Move based on window | Direct lookup |

## Real-world Applications

- Merge operations (merge sort, merge arrays)
- Collision detection in physics engines
- Stream processing (finding patterns)
- Database query optimization
- Network packet inspection
- File comparison and diff tools
- String matching algorithms
- Memory management (garbage collection)

## LeetCode Problems by Pattern

**Opposite Direction:**
- Two Sum II (167)
- Container With Most Water (11)
- Valid Palindrome (125)
- Trapping Rain Water (42)

**Same Direction:**
- Remove Duplicates from Sorted Array (26)
- Move Zeroes (283)
- Remove Element (27)
- Sort Colors (75)

**Fast-Slow:**
- Linked List Cycle (141)
- Linked List Cycle II (142)
- Middle of Linked List (876)
- Happy Number (202)

**Three Pointers:**
- 3Sum (15)
- 3Sum Closest (16)
- 4Sum (18)
- Sort Colors (75)

**Advanced:**
- Trapping Rain Water (42)
- Remove Nth Node From End (19)
- Rotate List (61)
- Partition List (86)

## Advanced Techniques

### Squaring Sorted Array with Negatives

```python
def sorted_squares(nums):
    """Square elements of sorted array (with negatives)"""
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1

    return result

# Time: O(n), Space: O(n)
```

### Merge Sorted Arrays

```python
def merge(nums1, m, nums2, n):
    """Merge nums2 into nums1 in-place"""
    # Start from end to avoid overwriting
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Copy remaining from nums2
    nums1[:p2+1] = nums2[:p2+1]

# Time: O(m + n), Space: O(1)
```
