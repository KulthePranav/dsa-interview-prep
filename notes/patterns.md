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
