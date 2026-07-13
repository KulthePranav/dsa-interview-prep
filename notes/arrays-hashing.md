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

## 14. Longest Common Prefix

**Pattern:** Prefix Reduction

**Signal:**
- Multiple strings.
- Need the longest common starting substring.
- Prefix can only become shorter.

## Approach

1. Assume the first string is the common prefix.
2. Compare it with every other string.
3. While the current string doesn't start with the prefix:
   - Remove the last character from the prefix.
4. If the prefix becomes empty, return `""`.
5. Return the remaining prefix.


## Visualization

```
Input

["flower","flow","flight"]

prefix = "flower"

Compare with "flow"

flower ❌

Reduce

flowe ❌

flow ✅

prefix = "flow"

Compare with "flight"

flow ❌

flo ❌

fl ✅

Answer

"fl"
```


## Template

```python
prefix = strs[0]

for word in strs[1:]:

    while word.find(prefix) != 0:
        prefix = prefix[:-1]

        if prefix == "":
            return ""
```


## Actual Solution

```python
if len(strs) == 0:
    return ""

prefix = strs[0]

for i in range(1, len(strs)):
    while strs[i].find(prefix) != 0:
        prefix = prefix[:-1]

        if prefix == "":
            return ""

return prefix
```

## Alternative Solution 1 (Character-by-Character)

```python
prefix = ""

for chars in zip(*strs):
    if len(set(chars)) == 1:
        prefix += chars[0]
    else:
        break

return prefix
```

Uses `zip()` to compare the same index across all strings.


## Alternative Solution 2 (Sorting)

```python
strs.sort()

first = strs[0]
last = strs[-1]

i = 0

while i < len(first) and first[i] == last[i]:
    i += 1

return first[:i]
```

After sorting, only the first and last strings need to be compared.


## Comparison

| Approach | Time | Space |
|----------|------|-------|
| Prefix Reduction | O(n × m) | O(1) |
| Character Comparison | O(n × m) | O(1) |
| Sorting | O(n log n × m) | O(1) |

- `n` = number of strings
- `m` = length of the shortest string

## Pattern Recognition

```text
Multiple strings?

↓

Need common prefix?

↓

Start with first string

↓

Shrink prefix until all strings match
```

## Common Mistakes

❌ Forgetting to handle an empty input list.

❌ Comparing entire strings instead of only the prefix.

❌ Not stopping when the prefix becomes empty.


## Python Note: `find()`

```python
word.find(prefix)
```

Returns:

- `0` → prefix found at the beginning.
- Positive index → found elsewhere.
- `-1` → not found.

Example

```python
"flower".find("flo")      # 0
"flower".find("low")      # 1
"flower".find("abc")      # -1
```

Therefore,

```python
while word.find(prefix) != 0:
```

means

> "Keep reducing the prefix until the word starts with it."


**Time Complexity:** O(n × m)

**Space Complexity:** O(1)

**Key Learning:**
The common prefix can only become shorter. Start with the first string and continuously shrink it until every string starts with that prefix.

---

## 27. Remove Element

**Pattern:** Fast & Slow Pointers

**Signal:**
- Modify the array in-place.
- Remove specific elements.
- Preserve the order of remaining elements.
- Extra space is not allowed.

## Approach

1. Maintain two pointers:
   - `j` → scans every element (fast pointer).
   - `i` → points to the next position for a valid element (slow pointer).
2. If `nums[j]` is not equal to `val`, copy it to `nums[i]`.
3. Increment `i`.
4. Return `i` as the new length.

## Visualization

Input

```
nums = [3,2,2,3]
val = 3
```

```
i = 0

j = 0

3 == val

Skip

------------------

j = 1

2 != val

nums[0] = 2

[2,2,2,3]

i = 1

------------------

j = 2

2 != val

nums[1] = 2

[2,2,2,3]

i = 2

------------------

j = 3

3 == val

Skip
```

Result

```
Length = 2

Array

[2,2,...]
```

## Template

```python
i = 0

for j in range(len(nums)):
    if nums[j] != val:
        nums[i] = nums[j]
        i += 1

return i
```

## Actual Solution

```python
i = 0

for j in range(len(nums)):
    if nums[j] != val:
        nums[i] = nums[j]
        i += 1

return i
```

## Alternative Solution (Swap with Last Element)

> Order of elements is **not preserved**.

```python
i = 0
n = len(nums)

while i < n:
    if nums[i] == val:
        nums[i] = nums[n - 1]
        n -= 1
    else:
        i += 1

return n
```

Useful when preserving order is not required.

## Comparison

| Approach | Time | Space | Preserves Order |
|----------|------|-------|-----------------|
| Fast & Slow Pointers | O(n) | O(1) | ✅ |
| Swap with Last | O(n) | O(1) | ❌ |


## Pattern Recognition

```text
Modify array in-place?

↓

Need to remove elements?

↓

Preserve order?

↓

Fast & Slow Pointers
```

## Common Mistakes

❌ Using `remove()` repeatedly.

```
O(n²)
```

❌ Creating another list.

```
Extra O(n) space.
```

❌ Forgetting to return the new length.


**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Key Learning:**
The slow pointer always indicates where the next valid element should be placed, while the fast pointer scans the array exactly once.

---

## 169. Majority Element

**Pattern:** Boyer-Moore Voting Algorithm

**Signal:**
- One element appears more than half the time.
- Need O(1) extra space.
- Frequency counting is possible but not optimal.

## Approach

1. Maintain a candidate and a counter.
2. If the counter becomes zero, choose the current element as the new candidate.
3. If the current element equals the candidate, increment the counter.
4. Otherwise, decrement the counter.
5. After one pass, the candidate is the majority element.

## Visualization

Input

```
[2,2,1,1,1,2,2]
```

```
Candidate  Count

None       0

2          1
2          2
2          1
2          0

1          1
1          0

2          1
```

Answer

```
2
```

## Why It Works

Think of each different element as canceling one occurrence of the current candidate.

```
2 2 1 1 1 2 2

↓

Cancel

2 1
2 1
1 2

↓

Remaining

2
```

Since the majority element appears more than `n / 2` times, it can never be completely canceled.

## Template

```python
candidate = None
count = 0

for num in nums:

    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

return candidate
```

## Actual Solution

```python
candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

return candidate
```

## Alternative Solution 1 (Hash Map)

```python
count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

    if count[num] > len(nums) // 2:
        return num
```

## Alternative Solution 2 (Sorting)

```python
nums.sort()
return nums[len(nums) // 2]
```

## Alternative Solution 3 (Brute Force)

```python
majority = len(nums) // 2

for num in set(nums):
    if nums.count(num) > majority:
        return num
```

## Comparison

| Approach | Time | Space |
|----------|------|-------|
| Brute Force (`count`) | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |
| Sorting | O(n log n) | O(1) |
| Boyer-Moore Voting | **O(n)** | **O(1)** |

## Pattern Recognition

```text
Majority element (> n/2)?

↓

Need O(1) space?

↓

Boyer-Moore Voting Algorithm
```

## Common Mistakes

❌ Using `nums.count()` inside a loop.

This makes the solution O(n²).

❌ Forgetting that Boyer-Moore only works when a majority element is guaranteed.

If not guaranteed, verify the candidate with another pass.


**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Key Learning:**
Boyer-Moore Voting Algorithm uses pair cancellation to eliminate non-majority elements, leaving the majority element as the final candidate.

---

## 705. Design HashSet

**Pattern:** Hash Table (Separate Chaining)

**Signal:**
- Design a data structure.
- Fast lookup, insertion, and deletion.
- Built-in hash collections are not allowed.

## Approach

1. Create a fixed number of buckets.
2. Compute the bucket index using:

```python
index = key % size
```

3. Store keys inside the corresponding bucket.
4. Handle collisions using a list (Separate Chaining).

## Visualization

Suppose

```
size = 5
```

Keys

```
12
7
17
22
```

Bucket indices

```
12 % 5 = 2

7 % 5 = 2

17 % 5 = 2

22 % 5 = 2
```

Buckets

```
0 :

1 :

2 : [12, 7, 17, 22]

3 :

4 :
```

All keys share the same bucket because they produce the same hash value.

## Hash Function

```python
index = key % size
```

Maps every key to one of the available buckets.

## Template

```python
bucket = buckets[key % size]

if key not in bucket:
    bucket.append(key)
```

## Actual Solution

```python
self.size = 1000
self.buckets = [[] for _ in range(self.size)]
```

```python
bucket = self.buckets[key % self.size]
```

## Alternative Solution 1 (Boolean Array)

```python
self.hashset = [False] * 1000001

self.hashset[key] = True
```

### Pros

- O(1) operations
- Very simple

### Cons

- Wastes memory
- Only works when key range is known

## Alternative Solution 2 (Single List)

```python
self.hashset = []

if key not in self.hashset:
    self.hashset.append(key)
```

### Pros

Very easy to understand.

### Cons

Every lookup is O(n).

## Comparison

| Approach | Add | Remove | Contains | Space |
|----------|-----|---------|-----------|-------|
| List | O(n) | O(n) | O(n) | O(n) |
| Boolean Array | O(1) | O(1) | O(1) | O(maxKey) |
| Bucket Hashing | O(1) Average | O(1) Average | O(1) Average | O(n) |

## Pattern Recognition

```text
Need to design a hash data structure?

↓

Built-in HashSet not allowed?

↓

Use Hash Table

↓

Handle collisions

↓

Separate Chaining
```

## Collision

A collision occurs when two different keys map to the same bucket.

Example

```
12 % 5 = 2

17 % 5 = 2
```

Both keys are stored in the same bucket.

## Common Mistakes

❌ Using one large list.

```
Lookup becomes O(n).
```

❌ Forgetting collision handling.

Different keys can map to the same bucket.


❌ Choosing very few buckets.

This increases collisions and slows down operations.

**Time Complexity**

Average

- Add → O(1)
- Remove → O(1)
- Contains → O(1)

Worst Case

- O(n)

**Space Complexity**

O(n)

**Key Learning**

A HashSet stores values in buckets using a hash function. Collisions are handled using Separate Chaining, allowing average O(1) operations.

---

## 706. Design HashMap

**Pattern:** Hash Table (Separate Chaining)

**Signal:**
- Design a key-value data structure.
- Fast insertion, lookup, and deletion.
- Built-in dictionaries/maps are not allowed.

## Approach

1. Create a fixed number of buckets.
2. Compute the bucket index:

```python
index = key % size
```

3. Each bucket stores `(key, value)` pairs.
4. If the key already exists, update its value.
5. Otherwise, insert a new pair.
6. Handle collisions using Separate Chaining.

## Visualization

Suppose

```
size = 5
```

Operations

```
put(12, 100)
put(7, 200)
put(17, 300)
```

Bucket index

```
12 % 5 = 2
7 % 5 = 2
17 % 5 = 2
```

Buckets

```
0 :

1 :

2 : [(12,100), (7,200), (17,300)]

3 :

4 :
```

All three keys share the same bucket.

## Updating Existing Key

```
put(7, 500)
```

Bucket becomes

```
[(12,100), (7,500), (17,300)]
```

The old value is replaced.

## Hash Function

```python
index = key % size
```

Maps every key into a bucket.

## Template

```python
bucket = buckets[key % size]

for i, (k, v) in enumerate(bucket):
    if k == key:
        bucket[i] = (key, value)
        return

bucket.append((key, value))
```

## Actual Solution

```python
self.size = 1000
self.buckets = [[] for _ in range(self.size)]
```

## Alternative Solution 1 (Large Array)

```python
self.map = [-1] * 1000001

self.map[key] = value
```

### Pros

- O(1) operations
- Very simple

### Cons

- Very high memory usage
- Requires known key range


## Alternative Solution 2 (List of Pairs)

```python
self.map = []

for i, (k, v) in enumerate(self.map):
    if k == key:
        self.map[i] = (key, value)
```

### Pros

Simple implementation.

### Cons

Every operation is O(n).

## Comparison

| Approach | Put | Get | Remove | Space |
|----------|-----|-----|--------|-------|
| List | O(n) | O(n) | O(n) | O(n) |
| Large Array | O(1) | O(1) | O(1) | O(maxKey) |
| Bucket Hashing | O(1) Average | O(1) Average | O(1) Average | O(n) |

## Pattern Recognition

```text
Need key-value storage?

↓

Built-in HashMap not allowed?

↓

Hash Function

↓

Buckets

↓

Separate Chaining
```

## Collision

A collision occurs when multiple keys map to the same bucket.

Example

```
12 % 5 = 2
17 % 5 = 2
22 % 5 = 2
```

Store them together inside the bucket.

## Common Mistakes

❌ Appending duplicate keys instead of updating.

❌ Forgetting to search for the key before insertion.

❌ Removing the wrong element after a collision.

## Time Complexity

Average

- Put → O(1)
- Get → O(1)
- Remove → O(1)

Worst Case

- O(n)

## Space Complexity

O(n)

## Key Learning

A HashMap stores `(key, value)` pairs inside buckets. Collisions are resolved using Separate Chaining, providing average O(1) insertion, lookup, and deletion.

---
