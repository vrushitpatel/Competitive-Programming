# Hash Table Cheat Sheet

Hash Table (Hash Map) is a data structure that stores key-value pairs and provides fast access to values based on keys. It uses a hash function to compute an index into an array of buckets/slots, from which the desired value can be found.

## Structure

Initializing Hash Table and Hash Set

```python
# Hash Table (Dictionary)
hash_map = {}
hash_map = dict()

# Hash Set
hash_set = set()

# With initial values
hash_map = {'key1': 'value1', 'key2': 'value2'}
hash_set = {1, 2, 3, 4}

# From lists
hash_map = dict(zip(keys, values))
hash_set = set([1, 2, 3])
```

## Time & Space Complexity

| Operation | Average | Worst Case | Space |
| --------- | ------- | ---------- | ----- |
| Insert    | O(1)    | O(n)       | O(1)  |
| Delete    | O(1)    | O(n)       | O(1)  |
| Search    | O(1)    | O(n)       | O(1)  |
| Update    | O(1)    | O(n)       | O(1)  |

Note: Worst case O(n) occurs when all keys hash to the same bucket (collision).

## Hash Map Operations

### 1. Insert/Update

```python
# Insert or update
hash_map[key] = value

# Using setdefault (insert only if key doesn't exist)
hash_map.setdefault(key, default_value)

# Using update
hash_map.update({key1: value1, key2: value2})
```

### 2. Access/Search

```python
# Direct access (raises KeyError if not found)
value = hash_map[key]

# Safe access with default
value = hash_map.get(key, default_value)

# Check if key exists
if key in hash_map:
    value = hash_map[key]
```

### 3. Delete

```python
# Delete key (raises KeyError if not found)
del hash_map[key]

# Safe delete with pop
value = hash_map.pop(key, default_value)

# Remove and return arbitrary item
key, value = hash_map.popitem()

# Clear all items
hash_map.clear()
```

### 4. Iteration

```python
# Iterate over keys
for key in hash_map:
    print(key)

# Iterate over values
for value in hash_map.values():
    print(value)

# Iterate over key-value pairs
for key, value in hash_map.items():
    print(key, value)

# Get all keys/values as list
keys = list(hash_map.keys())
values = list(hash_map.values())
```

## Hash Set Operations

### 1. Add/Remove

```python
# Add element
hash_set.add(element)

# Remove element (raises KeyError if not found)
hash_set.remove(element)

# Safe remove
hash_set.discard(element)

# Remove and return arbitrary element
element = hash_set.pop()

# Clear all elements
hash_set.clear()
```

### 2. Set Operations

```python
# Union
set1 | set2
set1.union(set2)

# Intersection
set1 & set2
set1.intersection(set2)

# Difference
set1 - set2
set1.difference(set2)

# Symmetric Difference (XOR)
set1 ^ set2
set1.symmetric_difference(set2)

# Subset check
set1.issubset(set2)
set1 <= set2

# Superset check
set1.issuperset(set2)
set1 >= set2
```

## Common Hash Table Patterns

### 1. Two Sum

```python
def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []
```

### 2. Frequency Counter

```python
from collections import Counter

def frequency_count(arr):
    # Using dict
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Using Counter (preferred)
    freq = Counter(arr)
    return freq

# Get most common elements
counter = Counter(arr)
top_k = counter.most_common(k)
```

### 3. Group Anagrams

```python
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
```

### 4. Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s):
    char_map = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

### 5. First Non-Repeating Character

```python
def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1
```

### 6. Subarray Sum Equals K

```python
def subarray_sum(nums, k):
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

## Advanced Collections

### 1. defaultdict

```python
from collections import defaultdict

# Auto-initialize missing keys
graph = defaultdict(list)
graph[1].append(2)  # No KeyError

freq = defaultdict(int)
freq['a'] += 1  # Auto-initializes to 0

groups = defaultdict(set)
groups['group1'].add(1)
```

### 2. Counter

```python
from collections import Counter

# Frequency counter
counter = Counter([1, 2, 2, 3, 3, 3])
# Counter({3: 3, 2: 2, 1: 1})

# Most common elements
counter.most_common(2)  # [(3, 3), (2, 2)]

# Arithmetic operations
c1 + c2  # Add counts
c1 - c2  # Subtract (keep only positive)
c1 & c2  # Intersection (min)
c1 | c2  # Union (max)
```

### 3. OrderedDict

```python
from collections import OrderedDict

# Maintains insertion order (dict also does this in Python 3.7+)
ordered = OrderedDict()
ordered['a'] = 1
ordered['b'] = 2

# Move to end
ordered.move_to_end('a')  # Move 'a' to end

# LRU Cache implementation
ordered.move_to_end(key)  # Update access time
ordered.popitem(last=False)  # Remove oldest
```

## Hash Function Implementation

```python
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False
```

## Key Patterns to Remember

1. **Two Pointer + Hash**: Two sum, three sum variations
2. **Frequency Counting**: Anagrams, character frequency
3. **Prefix Sum + Hash**: Subarray sum problems
4. **Sliding Window + Hash**: Longest substring problems
5. **Graph Representation**: Adjacency list using dict
6. **Caching/Memoization**: DP optimization

## Common Pitfalls

- Modifying dictionary while iterating (use list(dict.keys()))
- Using mutable objects as keys (lists, dicts)
- Not handling KeyError (use .get() or check with 'in')
- Forgetting that sets are unordered
- Hash collisions in worst case scenarios

## Interview Tips

- Ask: Can we use extra space? (Hash tables require O(n) space)
- Clarify: What should happen with duplicate keys?
- Consider: Trade-off between time and space
- Think about: Dictionary vs set vs Counter vs defaultdict
- Test: Empty input, single element, duplicates, no solution
- Common problems: Two sum, group anagrams, frequency count

## When to Use Hash Table

✅ **Use when:**
- Need O(1) lookup/insert/delete
- Checking for existence/duplicates
- Counting frequencies
- Grouping/categorizing data
- Caching results

❌ **Don't use when:**
- Need ordered data (use list or OrderedDict)
- Need range queries (use trees)
- Memory is constrained
- Need to iterate in sorted order (use sorted containers)

## Real-world Applications

- Database indexing
- Caching (LRU cache, memoization)
- Symbol tables in compilers
- Password verification
- Blockchain (hash functions)
- File systems (duplicate detection)
- DNS resolution
