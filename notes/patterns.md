# Pattern Recognition

## 217. Contains Duplicate

**Pattern:** Hash Set

**Approach:**
Store seen numbers in a hash set.
If a number already exists in the set, return `True`.

**Time:** O(n)  
**Space:** O(n)

**Key Learning:**
Hash Set = O(1) lookup for duplicate detection.


## 242. Valid Anagram

**Pattern:** Frequency Count / Hash Map

**Approach:**
1. Check if lengths are equal.
2. Count character frequencies in the first string.
3. Decrement frequencies using the second string.
4. If a character is missing or count becomes negative, return False.
5. Otherwise, the strings are anagrams.

**Time:** O(n)

**Space:** O(1) for fixed alphabet
O(n) in general

**Key Learning:**
Use frequency counting when occurrence counts matter more than order.

## 1. Two Sum

**Pattern:** Hash Map

**Approach:**
1. Store previously seen numbers and their indices in a hash map.
2. For each number, calculate the complement.
3. Check if the complement exists in the map.
4. If found, return both indices.

**Time:** O(n)

**Space:** O(n)

**Key Learning:**
Hash Maps allow constant-time lookups, converting a brute-force O(n²) search into O(n).

## 49. Group Anagrams

**Pattern:** Hash Map + Frequency Count

**Approach:**
1. Build a frequency count array for each string.
2. Convert the count array into a tuple.
3. Use the tuple as a key in a hash map.
4. Group all strings with identical frequency counts.

**Time:** O(n × k)

**Space:** O(n × k)

- n = number of strings
- k = average length of string

**Key Learning:**
A tuple is hashable and can represent a character frequency signature.

**Recognition:**
- Need to group words.
- Order of characters doesn't matter.
- Character frequency uniquely identifies an anagram.

**Template:**

```python
count = [0] * 26

for c in word:
    count[ord(c) - ord('a')] += 1

hashmap[tuple(count)].append(word)
```

**defaultdict Note:**

```python
from collections import defaultdict

groups = defaultdict(list)
groups[key].append(value)
```

Without `defaultdict`:

```python
if key not in groups:
    groups[key] = []

groups[key].append(value)
```

**Why use defaultdict?**
- Automatically initializes missing keys.
- Avoids explicit existence checks.
- Makes grouping and graph problems cleaner.

**Common Usage:**

```python
defaultdict(list)   # Grouping values
defaultdict(set)    # Unique values
defaultdict(int)    # Frequency counting
```

**Key Learning:**
A frequency count tuple can be used as a hashable signature for anagrams.
