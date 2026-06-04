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
