## Medium Hash Table Problems

### 1. Group Anagrams

```python
from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
```

**Using Character Count as Key:**
```python
from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        anagrams[tuple(count)].append(s)
    return list(anagrams.values())
```

**Time Complexity:** O(n * k log k) for sorting, O(n * k) for counting
**Space Complexity:** O(n * k)

---

### 2. Top K Frequent Elements

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]
```

**Using Heap:**
```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

**Using Bucket Sort:**
```python
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]
```

**Time Complexity:** O(n log k) for heap, O(n) for bucket sort
**Space Complexity:** O(n)

---

### 3. Longest Consecutive Sequence

```python
def longestConsecutive(nums):
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 4. Subarray Sum Equals K

```python
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum - k]
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 5. Longest Substring Without Repeating

```python
def lengthOfLongestSubstring(s):
    char_map = {}
    left = max_len = 0

    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```

**Using Set:**
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
```

**Time Complexity:** O(n)
**Space Complexity:** O(min(n, m)) where m is charset size

---

### 6. 4Sum II

```python
from collections import defaultdict

def fourSumCount(nums1, nums2, nums3, nums4):
    sum_count = defaultdict(int)

    # Store all possible sums of nums1 and nums2
    for a in nums1:
        for b in nums2:
            sum_count[a + b] += 1

    count = 0
    # Check if -(c + d) exists in sum_count
    for c in nums3:
        for d in nums4:
            count += sum_count[-(c + d)]

    return count
```

**Time Complexity:** O(n²)
**Space Complexity:** O(n²)

---

### 7. Valid Sudoku

```python
def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue

            num = board[r][c]
            box_idx = (r // 3) * 3 + (c // 3)

            if num in rows[r] or num in cols[c] or num in boxes[box_idx]:
                return False

            rows[r].add(num)
            cols[c].add(num)
            boxes[box_idx].add(num)

    return True
```

**Using Single Set:**
```python
def isValidSudoku(board):
    seen = set()

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue

            num = board[r][c]
            row_key = f"{num} in row {r}"
            col_key = f"{num} in col {c}"
            box_key = f"{num} in box {r // 3}-{c // 3}"

            if row_key in seen or col_key in seen or box_key in seen:
                return False

            seen.add(row_key)
            seen.add(col_key)
            seen.add(box_key)

    return True
```

**Time Complexity:** O(1) - fixed 9x9 board
**Space Complexity:** O(1)

---

### 8. Find All Anagrams in String

```python
from collections import Counter

def findAnagrams(s, p):
    if len(p) > len(s):
        return []

    result = []
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])

    if window_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        # Add new character to window
        window_count[s[i]] += 1

        # Remove old character from window
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

        if window_count == p_count:
            result.append(i - len(p) + 1)

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) - at most 26 characters

---

### 9. Sort Characters by Frequency

```python
from collections import Counter

def frequencySort(s):
    count = Counter(s)
    return ''.join(char * freq for char, freq in count.most_common())
```

**Using Bucket Sort:**
```python
from collections import Counter

def frequencySort(s):
    count = Counter(s)
    buckets = [[] for _ in range(len(s) + 1)]

    for char, freq in count.items():
        buckets[freq].append(char)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for char in buckets[i]:
            result.append(char * i)

    return ''.join(result)
```

**Time Complexity:** O(n log n) for sorting, O(n) for bucket sort
**Space Complexity:** O(n)

---

### 10. LRU Cache

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

**Using HashMap + Doubly Linked List:**
```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_head(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

**Time Complexity:** O(1) for both get and put
**Space Complexity:** O(capacity)
