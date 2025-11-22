## Easy Hash Table Problems

### 1. Two Sum

```python
def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 2. Contains Duplicate

```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

**Alternative:**
```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

### 3. Valid Anagram

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

**Using Hash Map (Better):**
```python
from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)
```

**Manual Count:**
```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) - at most 26 characters

---

### 4. Majority Element

```python
from collections import Counter

def majorityElement(nums):
    count = Counter(nums)
    return count.most_common(1)[0][0]
```

**Using Hash Map:**
```python
def majorityElement(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:
            return num
```

**Boyer-Moore Voting (O(1) space):**
```python
def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate
```

**Time Complexity:** O(n)
**Space Complexity:** O(n) for hash map, O(1) for Boyer-Moore

---

### 5. Single Number

```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

**Using Hash Set:**
```python
def singleNumber(nums):
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return seen.pop()
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) for XOR, O(n) for set

---

### 6. Intersection of Two Arrays

```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```

**Using Hash Set:**
```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()
    for num in nums2:
        if num in set1:
            result.add(num)
    return list(result)
```

**Time Complexity:** O(n + m)
**Space Complexity:** O(n + m)

---

### 7. First Unique Character

```python
from collections import Counter

def firstUniqChar(s):
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
```

**Using Hash Map:**
```python
def firstUniqChar(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) - at most 26 characters

---

### 8. Ransom Note

```python
from collections import Counter

def canConstruct(ransomNote, magazine):
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True
```

**Using Single Counter:**
```python
from collections import Counter

def canConstruct(ransomNote, magazine):
    magazine_count = Counter(magazine)
    for char in ransomNote:
        if magazine_count[char] <= 0:
            return False
        magazine_count[char] -= 1
    return True
```

**Time Complexity:** O(n + m)
**Space Complexity:** O(1) - at most 26 characters
