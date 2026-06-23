# Pattern Recognition

## 217. Contains Duplicate
→ Hash Set

**Signal:**
Need fast duplicate detection.

**Key Learning:**
Hash Set provides O(1) lookup.

---

## 242. Valid Anagram
→ Frequency Count / Hash Map

**Signal:**
Character occurrences matter more than order.

**Key Learning:**
Frequency counting is useful when counts matter.

---

## 1. Two Sum
→ Hash Map

**Signal:**
Need to find a pair efficiently.

**Key Learning:**
Store value → index for O(1) lookups.

---

## 49. Group Anagrams
→ Hash Map + Frequency Count

**Signal:**
Need to group words where order doesn't matter.

**Key Learning:**
Character frequency uniquely identifies an anagram.

---

## 347. Top K Frequent Elements
→ Bucket Sort

**Signal:**
Need highest frequency elements.

**Key Learning:**
Frequency can be used as an array index.

---

## 271. Encode and Decode Strings
→ Length Prefix Encoding

**Signal:**
Need reversible string serialization.

**Key Learning:**
Store length before data.

---

## 238. Product of Array Except Self
→ Prefix & Postfix Products

**Signal:**
Need left and right information.

**Key Learning:**
Prefix × Postfix = Answer.

---

## 36. Valid Sudoku
→ Hash Set Validation

**Signal:**
Need duplicate validation across multiple dimensions.

**Key Learning:**
Track rows, columns, and boxes independently.

---

## 128. Longest Consecutive Sequence
→ Hash Set

**Signal:**
Need O(1) neighbor lookup.

**Key Learning:**
Only start from sequence beginnings.

---

## 125. Valid Palindrome
→ Two Pointers

**Signal:**
- Need to compare characters from both ends.
- Palindrome or symmetry-based problem.
- Need O(1) extra space.

**Key Learning:**
Move two pointers inward while skipping unwanted characters.

---

## 167. Two Sum II - Input Array Is Sorted
→ Two Pointers

**Signal:**
Sorted array + pair search

**Rule:**
- sum < target  -> move left pointer
- sum > target  -> move right pointer
- sum = target  -> answer found

**Key Learning:**
Sorted arrays often allow replacing Hash Maps with Two Pointers.

---
