# Sorting Algorithms

Comparing the Sorting Algorithms

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

# Sorting Algorithms — Time Complexity Notes

---

## Complexity Table

| Algorithm      | Best Case  | Average Case | Worst Case | Space    | Stable? |
| -------------- | ---------- | ------------ | ---------- | -------- | ------- |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)     | ❌ No   |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅ Yes  |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅ Yes  |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)     | ✅ Yes  |
| Heap Sort      | O(n log n) | O(n log n)   | O(n log n) | O(1)     | ❌ No   |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n) | ❌ No   |

> `n` = number of elements, `k` = range of values, `d` = number of digits

---

## Algorithm-by-Algorithm Breakdown

### 1. Selection Sort — O(n²) always

- Finds the minimum element and places it at the front, repeating for each position.
- **Always scans the entire unsorted portion**, regardless of input order.
- No best-case improvement — even a sorted array costs O(n²).
- **Use when:** Number of swaps must be minimised (at most n–1 swaps).

---

### 2. Bubble Sort — Best: O(n) | Worst: O(n²)

- Repeatedly swaps adjacent elements that are out of order.
- **Optimised version** adds an early-exit flag: if no swap occurs in a pass, the array is sorted → **O(n) best case**.
- Naive version (no flag) is always O(n²).
- **Use when:** Array is nearly sorted or for educational purposes.

---

### 3. Insertion Sort — Best: O(n) | Worst: O(n²)

- Builds a sorted subarray one element at a time by inserting each new element into its correct position.
- On an **already sorted** array, each element is already in place → only n–1 comparisons → **O(n)**.
- Worst case: reverse-sorted input.
- **Use when:** Dataset is small or almost sorted. (Used internally by Timsort for small subarrays.)

---

### 4. Merge Sort — O(n log n) always

- Divides array into two halves, recursively sorts each, then merges them.
- **Guaranteed O(n log n) in all cases** — does not depend on input order.
- Requires **O(n) extra space** for the auxiliary merge array.
- **Use when:** Stability is required or sorting linked lists (no extra space needed for lists).

---

### 5. Heap Sort — O(n log n) always

- Builds a **max-heap**, then repeatedly extracts the maximum to build the sorted array.
- Consistent O(n log n) performance with **O(1) extra space** (in-place).
- Slower in practice than Quick Sort due to poor cache locality.
- **Use when:** Memory is constrained and worst-case guarantee is needed.

---

### 6. Quick Sort — Best/Avg: O(n log n) | Worst: O(n²)

- Picks a **pivot**, partitions elements around it, then recursively sorts partitions.
- **Best/Average:** Pivot splits array roughly in half → O(n log n).
- **Worst case:** Pivot is always the smallest/largest element (already sorted input with bad pivot choice) → O(n²).
- Mitigated by **random pivot** or **median-of-three** selection.
- **Use when:** General-purpose sorting where average performance matters most. (Default in most standard libraries.)

---

## Key Takeaways

| Category                | Algorithms                                |
| ----------------------- | ----------------------------------------- |
| Always O(n²)            | Selection Sort                            |
| O(n) best case          | Bubble Sort _(optimised)_, Insertion Sort |
| Always O(n log n)       | Merge Sort, Heap Sort                     |
| O(n²) worst case risk   | Quick Sort, Tree Sort, Bucket Sort        |
| Linear (non-comparison) | Radix Sort, Counting Sort, Bucket Sort    |

- **Stable** algorithms preserve the relative order of equal elements.
- **In-place** algorithms use O(1) extra space (Selection, Bubble, Insertion, Heap, Quick Sort).
- No comparison-based sort can do better than **O(n log n)** on average.
- Quick Sort is fastest in practice; Merge Sort is safest for guaranteed performance.
