# Lower Bound, Upper Bound & First/Last Position

---

## 1. Definitions

| Term            | Definition                                                                          |
| --------------- | ----------------------------------------------------------------------------------- |
| **Lower Bound** | Smallest index where `arr[i] >= target` (first position target _could_ be inserted) |
| **Upper Bound** | Smallest index where `arr[i] > target` (first position _after_ all occurrences)     |

**Example:**

```
arr = [1, 2, 2, 2, 3, 4]
         0  1  2  3  4  5

target = 2
Lower Bound → index 1  (first element >= 2)
Upper Bound → index 4  (first element >  2, which is 3)
```

> If the target is absent, both lower and upper bound return the same insertion point.

---

## 2. Lower Bound Implementation

**Logic:** When `arr[mid] >= target`, store `mid` as a candidate and search **left**. Otherwise search **right**.

```python
def lower_bound(arr, target):
    low, high = 0, len(arr) - 1
    lb = len(arr)             # default: not found

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:
            lb = mid          # potential answer
            high = mid - 1    # look further left
        else:
            low = mid + 1

    return lb
```

---

## 3. Upper Bound Implementation

**Logic:** When `arr[mid] > target`, store `mid` as a candidate and search **left**. Otherwise search **right**.

```python
def upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    ub = len(arr)             # default: not found

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            ub = mid          # potential answer
            high = mid - 1    # look further left
        else:
            low = mid + 1

    return ub
```

> **Key difference:** Lower Bound uses `>=`, Upper Bound uses `>`.

---

## 4. Find First and Last Position (LeetCode #34)

**Problem:** Given a sorted array with duplicates, find the `[first, last]` index of `target`. Return `[-1, -1]` if not found.

```
nums = [5, 7, 7, 8, 8, 10],  target = 8
Output: [3, 4]
```

### Approach: Use Lower & Upper Bound

- **First occurrence** = `lower_bound(target)`
- **Last occurrence** = `upper_bound(target) - 1`

```python
def search_range(nums, target):
    first = lower_bound(nums, target)

    # Check if target actually exists
    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    last = upper_bound(nums, target) - 1
    return [first, last]
```

### Walkthrough

```
nums = [5, 7, 7, 8, 8, 10]
          0  1  2  3  4   5

lower_bound(8) → index 3   ← first occurrence
upper_bound(8) → index 5   ← first element > 8 (which is 10)
last = 5 - 1  → index 4   ← last occurrence

Output: [3, 4] ✅
```

---

## 5. Complexity

| Operation    | Time     | Space |
| ------------ | -------- | ----- |
| Lower Bound  | O(log n) | O(1)  |
| Upper Bound  | O(log n) | O(1)  |
| First & Last | O(log n) | O(1)  |

---

## 6. Quick Recap

- `lower_bound` → index of **first element ≥ target**
- `upper_bound` → index of **first element > target**
- `last occurrence = upper_bound(target) - 1`
- Always validate: check `nums[first] == target` before returning results
- Both bounds use `high = len(arr)` (not `len - 1`) to handle edge cases where target is beyond all elements
