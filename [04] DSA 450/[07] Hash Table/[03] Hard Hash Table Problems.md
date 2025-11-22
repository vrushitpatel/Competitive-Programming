## Hard Hash Table Problems

### 1. Substring with Concatenation

```python
from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words)
    result = []

    for i in range(len(s) - total_len + 1):
        seen = {}
        for j in range(word_count):
            start = i + j * word_len
            word = s[start:start + word_len]

            if word not in word_freq:
                break

            seen[word] = seen.get(word, 0) + 1
            if seen[word] > word_freq[word]:
                break
        else:
            result.append(i)

    return result
```

**Optimized Sliding Window:**
```python
from collections import Counter, defaultdict

def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words)
    result = []

    for offset in range(word_len):
        left = offset
        seen = defaultdict(int)
        count = 0

        for right in range(offset, len(s) - word_len + 1, word_len):
            word = s[right:right + word_len]

            if word in word_freq:
                seen[word] += 1
                count += 1

                while seen[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == word_count:
                    result.append(left)

            else:
                seen.clear()
                count = 0
                left = right + word_len

    return result
```

**Time Complexity:** O(n * m * k) where n = len(s), m = len(words), k = word length
**Space Complexity:** O(m)

---

### 2. Minimum Window Substring

```python
from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    window_count = {}

    left = 0
    min_len = float('inf')
    min_left = 0

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                formed -= 1
            left += 1

    return "" if min_len == float('inf') else s[min_left:min_left + min_len]
```

**Time Complexity:** O(n + m)
**Space Complexity:** O(n + m)

---

### 3. LFU Cache

```python
from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size > 0:
            last = self.tail.prev
            self.remove(last)
            return last
        return None

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.cache = {}
        self.freq_map = defaultdict(DLinkedList)

    def _update(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)

        if self.min_freq == freq and self.freq_map[freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        self.freq_map[node.freq].add(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update(node)
        else:
            if len(self.cache) >= self.capacity:
                last = self.freq_map[self.min_freq].remove_last()
                del self.cache[last.key]

            node = Node(key, value)
            self.cache[key] = node
            self.freq_map[1].add(node)
            self.min_freq = 1
```

**Time Complexity:** O(1) for both get and put
**Space Complexity:** O(capacity)

---

### 4. First Missing Positive

```python
def firstMissingPositive(nums):
    n = len(nums)

    # Place each positive number at its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_pos = nums[i] - 1
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]

    # Find first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
```

**Using Hash Set:**
```python
def firstMissingPositive(nums):
    num_set = set(nums)
    i = 1
    while i in num_set:
        i += 1
    return i
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) for in-place, O(n) for set

---

### 5. Longest Duplicate Substring

```python
def longestDupSubstring(s):
    # Binary search on length
    def search(length):
        seen = set()
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr in seen:
                return substr
            seen.add(substr)
        return ""

    left, right = 0, len(s)
    result = ""

    while left < right:
        mid = (left + right + 1) // 2
        dup = search(mid)
        if dup:
            result = dup
            left = mid
        else:
            right = mid - 1

    return result
```

**Using Rabin-Karp (Rolling Hash):**
```python
def longestDupSubstring(s):
    def search(length):
        if length == 0:
            return ""

        MOD = 2**63 - 1
        base = 256
        h = 0
        power = pow(base, length, MOD)

        seen = {}
        for i in range(len(s)):
            if i >= length:
                h = (h * base - ord(s[i - length]) * power + ord(s[i])) % MOD
            else:
                h = (h * base + ord(s[i])) % MOD

            if i >= length - 1:
                if h in seen:
                    start = seen[h]
                    if s[start:start + length] == s[i - length + 1:i + 1]:
                        return s[i - length + 1:i + 1]
                seen[h] = i - length + 1

        return ""

    left, right = 0, len(s)
    result = ""

    while left < right:
        mid = (left + right + 1) // 2
        dup = search(mid)
        if dup:
            result = dup
            left = mid
        else:
            right = mid - 1

    return result
```

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

---

### 6. All O`one Data Structure

```python
class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_node = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key in self.key_count:
            count = self.key_count[key]
            self.key_count[key] = count + 1
            curr_node = self.count_node[count]
            curr_node.keys.remove(key)

            if count + 1 not in self.count_node:
                new_node = Node(count + 1)
                self.count_node[count + 1] = new_node
                self._add_node_after(new_node, curr_node)

            self.count_node[count + 1].keys.add(key)

            if not curr_node.keys:
                self._remove_node(curr_node)
                del self.count_node[count]
        else:
            self.key_count[key] = 1
            if 1 not in self.count_node:
                new_node = Node(1)
                self.count_node[1] = new_node
                self._add_node_after(new_node, self.head)
            self.count_node[1].keys.add(key)

    def dec(self, key):
        if key not in self.key_count:
            return

        count = self.key_count[key]
        curr_node = self.count_node[count]
        curr_node.keys.remove(key)

        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] = count - 1
            if count - 1 not in self.count_node:
                new_node = Node(count - 1)
                self.count_node[count - 1] = new_node
                self._add_node_after(new_node, curr_node.prev)
            self.count_node[count - 1].keys.add(key)

        if not curr_node.keys:
            self._remove_node(curr_node)
            del self.count_node[count]

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
```

**Time Complexity:** O(1) for all operations
**Space Complexity:** O(n) where n is number of unique keys
