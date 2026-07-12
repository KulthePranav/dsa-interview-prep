# Arrays & Hashing

## 217. Contains Duplicate

**Pattern:** Hash Set

**Approach:**
Store seen numbers in a hash set.
If a number already exists in the set, return `True`.

**Time:** O(n)  
**Space:** O(n)

**Key Learning:**
Hash Set = O(1) lookup for duplicate detection.

---

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

---

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

---

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

---

## 347. Top K Frequent Elements

**Pattern:** Bucket Sort + Frequency Count

**Signal:**
- Need top K frequent items.
- Frequency is more important than ordering.
- Better than sorting all elements.

**Approach:**
1. Count frequencies using a hash map.
2. Create frequency buckets.
3. Store numbers in buckets according to frequency.
4. Iterate buckets in reverse order.
5. Collect first k elements.

**Template:**

```python
count = {}

for n in nums:
    count[n] = count.get(n, 0) + 1

freq = [[] for _ in range(len(nums) + 1)]

for n, c in count.items():
    freq[c].append(n)

for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
        result.append(n)
```

**Time:** O(n)

**Space:** O(n)

**Key Learning:**
Bucket Sort is useful when values represent frequencies within a limited range.

---

## 271. Encode and Decode Strings

**Pattern:** String Encoding / Length Prefix

**Signal:**
- Need to serialize and deserialize strings.
- Strings may contain special characters.
- Need a lossless conversion.

**Approach:**
1. Encode each string as:
   length#string
2. During decoding:
   - Read digits until '#'
   - Extract the length
   - Read exactly that many characters
3. Repeat until the entire encoded string is processed.

**Template:**

```python
# Encode
encoded += str(len(word)) + "#" + word

# Decode
length = int(encoded[i:j])
word = encoded[j+1:j+1+length]
```

**Time:** O(n)

**Space:** O(n)

**Key Learning:**
Store metadata (length) before the data itself.
This avoids delimiter collision issues.

---

## 238. Product of Array Except Self

**Pattern:** Prefix & Postfix Products

**Signal:**
- Need values from both left and right sides.
- Division is not allowed.
- Looking for O(n) solution.

**Approach:**
1. Store prefix products in the result array.
2. Traverse backwards while maintaining a postfix product.
3. Multiply prefix and postfix products together.

**Template:**

```python
res = [1] * n

prefix = 1
for i in range(n):
    res[i] = prefix
    prefix *= nums[i]

postfix = 1
for i in range(n - 1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]
```

**Time:** O(n)

**Space:** O(1) extra space

**Key Learning:**
Use Prefix & Postfix Products when each position depends on elements on both sides.

---

## 36. Valid Sudoku

**Pattern:** Hash Set Validation

**Signal:**
- Need to detect duplicates across multiple dimensions.
- Validation problem rather than construction problem.

**Approach:**
1. Track seen values for each row.
2. Track seen values for each column.
3. Track seen values for each 3×3 box.
4. If a value already exists in any of them, return False.

**Template:**

```python
rows = defaultdict(set)
cols = defaultdict(set)
boxes = defaultdict(set)

box = (r // 3, c // 3)
```
### Sudoku Box Identification

```python
box = (r // 3, c // 3)
```

Examples:
```
(0,0) -> (0,0)
(1,2) -> (0,0)
(4,7) -> (1,2)
(8,8) -> (2,2)
```

This uniquely identifies each of the 9 sub-boxes.

**Time:** O(81)

**Space:** O(81)

**Key Learning:**
Multiple constraints can often be validated independently using separate hash sets

---

## 128. Longest Consecutive Sequence

**Pattern:** Hash Set

**Signal:**
- Need O(n) lookup.
- Consecutive values matter.
- Array is unsorted.

**Approach:**
1. Insert all numbers into a hash set.
2. Identify sequence starts:
   - num - 1 is not present.
3. Expand the sequence forward.
4. Track the maximum length.

**Template:**

```python
num_set = set(nums)

for num in num_set:
    if num - 1 not in num_set:
        length = 1

        while num + length in num_set:
            length += 1
```

**Time:** O(n)

**Space:** O(n)

**Key Learning:**
Only begin counting from sequence starts.
This guarantees each number is processed once.

---

## 1929. Concatenation of Array

**Pattern:** Array Traversal

**Signal:**
- Need to create a new array.
- Elements are copied in a fixed pattern.
- No extra computation per element.

## Approach

1. Create an array of size `2 * n`.
2. Traverse the original array.
3. Place each element at:
   - Current index
   - Current index + n

## Visualization

```
nums

[1,2,1]

n = 3

ans

[_,_,_,_,_,_]

i = 0

[1,_,_,1,_,_]

i = 1

[1,2,_,1,2,_]

i = 2

[1,2,1,1,2,1]
```

## Template

```python
n = len(nums)
ans = [0] * (2 * n)

for i, num in enumerate(nums):
    ans[i] = num
    ans[i + n] = num
```

## Actual Solution

```python
n = len(nums)
ans = [0] * (2 * n)

for i, num in enumerate(nums):
    ans[i] = num
    ans[i + n] = num

return ans
```

## Alternative Solution 1 (Pythonic)

```python
return nums + nums
```

## Alternative Solution 2

```python
return nums * 2
```

Since list multiplication duplicates the list.

## Comparison

| Approach | Time | Space |
|----------|------|-------|
| Pre-allocated Array | O(n) | O(n) |
| `nums + nums` | O(n) | O(n) |
| `nums * 2` | O(n) | O(n) |

## Pattern Recognition

```text
Need duplicate array?

↓

Traverse once

↓

Copy using indices
```

## Common Mistakes

❌ Appending twice inside the loop without pre-allocation (less efficient due to dynamic resizing).

❌ Modifying the original list when a new list is expected.

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Key Learning:**
Pre-allocating the result array avoids repeated resizing and makes index-based problems easier to solve.

---
