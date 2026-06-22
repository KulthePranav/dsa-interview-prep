# Python DSA Utilities

## defaultdict(list)

```python
from collections import defaultdict

groups = defaultdict(list)
groups["a"].append(1)
```

### Benefit

Automatically creates an empty list for missing keys.

Instead of:

```python
if key not in groups:
    groups[key] = []

groups[key].append(value)
```

### Common Uses

- Group Anagrams
- Graph Adjacency Lists
- BFS / DFS

---

## defaultdict(set)

```python
from collections import defaultdict

rows = defaultdict(set)
rows[0].add("5")
```

### Benefit

Automatically creates an empty `set` for missing keys.

Instead of:

```python
if key not in rows:
    rows[key] = set()

rows[key].add(value)
```

### Common Uses

- Valid Sudoku
- Graph Problems
- Unique Value Tracking

---

## defaultdict(int)

```python
from collections import defaultdict

freq = defaultdict(int)

for num in nums:
    freq[num] += 1
```

### Benefit

Automatically initializes missing keys to `0`.

Instead of:

```python
freq[num] = freq.get(num, 0) + 1
```

### Common Uses

- Frequency Counting
- Top K Frequent Elements
- Sliding Window

---

## ord()

Returns ASCII/Unicode value of a character.

```python
ord("a")
# 97

ord("z")
# 122
```

### Common Uses

Convert characters into array indices.

```python
index = ord(char) - ord("a")
```

Example:

```python
ord("c") - ord("a")
# 2
```

### Used In

- Group Anagrams
- Character Frequency Problems

---

## chr()

Converts ASCII value back to a character.

```python
chr(97)
# 'a'

chr(122)
# 'z'
```

### Reverse of

```python
ord()
```

---

## enumerate()

Returns index and value together.

```python
for i, num in enumerate(nums):
    print(i, num)
```

Output:

```python
0 10
1 20
2 30
```

### Used In

- Two Sum
- Array Traversal

Instead of:

```python
for i in range(len(nums)):
    num = nums[i]
```

---

## set()

Stores unique values.

```python
seen = set()

seen.add(1)
seen.add(1)

print(seen)
# {1}
```

### Time Complexity

```text
Add       O(1)
Lookup    O(1)
Delete    O(1)
```

### Used In

- Contains Duplicate
- Longest Consecutive Sequence

---

## tuple()

Immutable and hashable.

```python
count = [1, 0, 2]

key = tuple(count)
```

Output:

```python
(1, 0, 2)
```

### Why?

Lists cannot be dictionary keys.

```python
d[[1,2,3]] = value  ❌
```

But tuples can.

```python
d[(1,2,3)] = value  ✅
```

### Used In

- Group Anagrams

---

## list[::-1]

Reverse a sequence.

```python
s = "abc"

s[::-1]
```

Output:

```python
"cba"
```

### Used In

- Valid Palindrome (alternative solution)

---

## get()

Safely fetch dictionary values.

```python
count[num] = count.get(num, 0) + 1
```

### Benefit

Avoids:

```python
if num not in count:
    count[num] = 0

count[num] += 1
```

### Used In

- Valid Anagram
- Top K Frequent Elements

---

## isalnum()

Checks if a character is alphanumeric.

```python
"a".isalnum()   # True
"1".isalnum()   # True
"#".isalnum()   # False
```

### Used In

- Valid Palindrome

---

## lower()

Converts character/string to lowercase.

```python
"A".lower()

# 'a'
```

### Used In

- Valid Palindrome
- Valid Anagram
