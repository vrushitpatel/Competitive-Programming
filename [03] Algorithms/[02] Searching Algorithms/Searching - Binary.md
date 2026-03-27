# Binary Search — Complete Notes

---

## 1. Real-Life Example

Imagine searching for a word in a **dictionary**. You don't flip through every page one by one. Instead, you:

1. Open the book near the **middle**.
2. Check if your word comes **before or after** the current page.
3. Discard the half where the word **cannot** be, and repeat.

This is exactly how Binary Search works — cutting the search space in **half** at every step.

Other real-life analogies:

- **Phone contacts**: Contacts are sorted alphabetically; the search uses a binary-search-like approach to locate a name quickly.
- **Guessing a number game**: "Is it higher or lower?" — each answer eliminates half the possibilities.

---

## 2. Coding Problem (Problem Statement)

> Given a **sorted** array `arr[]` and a target value `key`, find the **index** of `key` in the array.  
> Return `-1` if the element is not present.

**Pre-conditions:**

- The array must be **sorted** (ascending or descending).
- Random access to any element must take **O(1)** time.

**Example:**

```
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 23
Output: Index 5
```

---

## 3. Iterative Solution

### How it works:

1. Maintain two pointers: `low = 0` and `high = n - 1`.
2. Calculate `mid = low + (high - low) / 2`.
   > ⚠️ Use `low + (high - low) / 2` instead of `(low + high) / 2` to **avoid integer overflow**.
3. Compare `arr[mid]` with `key`:
   - `arr[mid] == key` → return `mid` ✅
   - `key < arr[mid]` → search **left half**: `high = mid - 1`
   - `key > arr[mid]` → search **right half**: `low = mid + 1`
4. Repeat until `low > high`. If not found, return `-1`.

### Python Code:

```python
def binary_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid          # Element found
        elif arr[mid] > key:
            high = mid - 1      # Search left half
        else:
            low = mid + 1       # Search right half

    return -1                   # Element not found
```

---

## 4. Recursive Solution

### How it works:

- Same logic as iterative, but uses **function calls** instead of a loop.
- **Base case**: If `low > high`, the element is not found — return `-1`.
- At each call, compute `mid` and recursively search the appropriate half.

### Python Code:

```python
class Solution:
    def recursive_search(self, nums, low, high, target) -> int:
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.recursive_search(nums, mid + 1, high, target)
        else:
            return self.recursive_search(nums, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.recursive_search(nums, 0, len(nums) - 1, target)
```

---

## 5. Time and Space Complexity

### Why O(log n)?

At each step, the search space is **halved**:

| Iteration | Search Space |
| --------- | ------------ |
| Start     | n            |
| After 1st | n / 2        |
| After 2nd | n / 4        |
| After kth | n / 2^k      |

The search ends when the space reduces to 1: `n / 2^k = 1` → `k = log₂(n)`

### Complexity Table

|               | Time Complexity | Space Complexity |
| ------------- | --------------- | ---------------- |
| **Iterative** | O(log n)        | **O(1)**         |
| **Recursive** | O(log n)        | **O(log n)**     |

> The recursive approach uses extra **call stack** space — one stack frame per recursive call, up to a depth of log n.

### Case-wise Time Complexity

| Case        | Description                                     | Complexity |
| ----------- | ----------------------------------------------- | ---------- |
| **Best**    | Target is at the **middle** on the first check  | O(1)       |
| **Average** | Target found after halving a few times          | O(log n)   |
| **Worst**   | Target at the last possible position or missing | O(log n)   |

### Practical Insight

For an array of **1,000,000** elements:

- **Linear Search** → up to 1,000,000 comparisons
- **Binary Search** → at most **20 comparisons** (log₂ 1,000,000 ≈ 20)

---

## 6. Iterative vs Recursive — Quick Comparison

| Feature          | Iterative                 | Recursive                     |
| ---------------- | ------------------------- | ----------------------------- |
| Space Complexity | O(1) ✅ Better            | O(log n)                      |
| Readability      | Slightly verbose          | Cleaner, more elegant         |
| Risk             | None                      | Stack overflow on huge inputs |
| Preferred when   | Memory efficiency matters | Readability matters           |

---

## 7. Key Takeaways

- Binary Search only works on **sorted** arrays/data structures.
- Always compute mid as `low + (high - low) / 2` to **prevent overflow**.
- **Iterative** is generally preferred in production due to lower space usage.
- **Recursive** is preferred for clarity when input size is manageable.
- Binary Search is a **Divide and Conquer** algorithm.
- Time complexity: **O(log n)** — drastically better than linear search O(n) for large datasets.

---

## 8. Edge Cases to Handle

- **Empty array** → return `-1` immediately.
- **Single element** → check if it matches the key.
- **Target at boundaries** → first or last element.
- **Target not in array** → return `-1` after exhausting search space.
