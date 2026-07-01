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

---

## `float("inf")` and `float("-inf")`

## Positive Infinity

```python
minimum = float("inf")
```

Used when searching for the **minimum** value.

Example:

```python
minimum = float("inf")

for num in nums:
    minimum = min(minimum, num)
```

## Negative Infinity

```python
maximum = float("-inf")
```

Used when searching for the **maximum** value.

Example:

```python
maximum = float("-inf")

for num in nums:
    maximum = max(maximum, num)
```

## Common Use Cases

| Expression | Used For |
|------------|----------|
| `float("inf")` | Initialize minimum value |
| `float("-inf")` | Initialize maximum value |

Examples:
- Minimum Window Substring
- Dijkstra's Algorithm
- Kadane's Algorithm
- Dynamic Programming

---

## `collections.deque`

A **deque (Double Ended Queue)** supports efficient insertion and deletion from **both ends**.

```python
from collections import deque

q = deque()
```

Unlike a list, operations at the front are **O(1)**.

## Common Operations

### Append to Right

```python
q.append(5)
```

```
[5]
```

### Append to Left

```python
q.appendleft(3)
```

```
[3, 5]
```

### Remove from Right

```python
q.pop()
```

---

### Remove from Left

```python
q.popleft()
```

### Front Element

```python
q[0]
```
### Back Element

```python
q[-1]
```


### Length

```python
len(q)
```

### Check if Empty

```python
if not q:
    ...
```

or

```python
if q:
    ...
```

## Why Use `deque` Instead of a List?

| Operation | List | Deque |
|-----------|------|--------|
| Append Right | O(1) | O(1) |
| Pop Right | O(1) | O(1) |
| Append Left | O(n) | O(1) |
| Pop Left | O(n) | O(1) |

Lists are inefficient for removing elements from the front because all remaining elements must be shifted.


## Common DSA Applications

- Sliding Window Maximum
- Monotonic Queue
- BFS (Breadth-First Search)
- Queue implementation
- LRU Cache

---

## Monotonic Deque Pattern

Used to maintain elements in increasing or decreasing order.

Example (decreasing deque):

```python
while q and nums[q[-1]] < nums[r]:
    q.pop()

q.append(r)
```

The front of the deque always stores the index of the maximum element in the current window.

### Why Store Indices Instead of Values?

Store indices so you can determine whether an element has moved outside the current window.

```python
if q[0] < left:
    q.popleft()
```

If only values were stored, you couldn't tell whether the maximum element was still inside the sliding window.

---
