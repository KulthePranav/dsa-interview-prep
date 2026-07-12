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

## 15. 3Sum
→ Sorting + Two Pointers

**Signal:**
- Need triplets instead of pairs.
- Array can be sorted.
- Need to avoid duplicate results.

**Key Learning:**
Fix one element and use Two Pointers to find the remaining pair.

---

## 11. Container With Most Water
→ Greedy + Two Pointers

**Signal:**
- Need maximum area between two boundaries.
- Width decreases as pointers move.
- Need optimal pair, not all pairs.

**Key Learning:**
Always move the smaller height because the larger height is not the limiting factor.

---
## 42. Trapping Rain Water
→ Two Pointers

**Signal:**
- Need left maximum and right maximum.
- Water depends on boundaries from both sides.
- Looking for O(1) extra space.

**Key Learning:**
The smaller boundary determines how much water can be trapped.

---
## 344. Reverse String
→ Two Pointers (In-place Swapping)

**Signal:**
- Reverse an array/string in-place.
- Extra space is not allowed.

**Key Learning:**
Use two pointers from both ends and swap elements until they meet.

---

## 121. Best Time to Buy and Sell Stock
→ Sliding Window

**Signal:**
- Need to maximize profit between two positions.
- Buy must happen before sell.
- Looking for O(n) solution.

**Key Learning:**
Track the minimum buying price while scanning, or use a sliding window to maintain buy and sell days.

---

## 3. Longest Substring Without Repeating Characters
→ Variable Sliding Window + Hash Set

**Signal:**
- Need the longest/shortest contiguous substring.
- Window validity depends on unique characters.
- Expand and shrink the window dynamically.

**Key Learning:**
Use a Hash Set to maintain unique characters and shrink the window whenever a duplicate is encountered.

---

## 424. Longest Repeating Character Replacement
→ Variable Sliding Window + Frequency Count

**Signal:**
- Need the longest valid substring.
- Allowed to modify up to `k` characters.
- Window validity depends on character frequencies.

**Key Learning:**
Maintain the frequency of characters in the current window. Shrink the window only when the number of replacements needed exceeds `k`.

---

## 567. Permutation in String
→ Fixed Sliding Window + Frequency Count

**Signal:**
- Need to check every substring of fixed length.
- Order doesn't matter.
- Character frequencies determine a match.

**Key Learning:**
Use a fixed-size sliding window and compare frequency counts instead of sorting every substring.

---

## 76. Minimum Window Substring
→ Variable Sliding Window + Frequency Count

**Signal:**
- Need the smallest valid substring.
- Window must contain all required characters.
- Expand to satisfy the condition, shrink to minimize the answer.

**Key Learning:**
Maintain character frequencies and shrink the window whenever all required characters are present.

---

## 239. Sliding Window Maximum
→ Monotonic Deque

**Signal:**
- Need the maximum/minimum of every fixed-size window.
- Brute force scans each window repeatedly.
- Looking for an O(n) solution.

**Key Learning:**
Maintain a decreasing deque of indices so the front always stores the maximum element of the current window.

---

## 20. Valid Parentheses
→ Stack

**Signal:**
- Need to match opening and closing symbols.
- Nested structures.
- Last opened item must be closed first.

**Key Learning:**
Use a stack to store opening brackets. Every closing bracket must match the top of the stack.

---

## 155. Min Stack
→ Stack + Auxiliary Stack

**Signal:**
- Need constant-time minimum/maximum retrieval.
- Stack operations with additional state.

**Key Learning:**
Maintain an auxiliary stack that stores the minimum value corresponding to each element in the main stack.

---

## 150. Evaluate Reverse Polish Notation
→ Stack

**Signal:**
- Expression evaluation.
- Operators appear after operands.
- Process tokens from left to right.

**Key Learning:**
Use a stack to store operands. When an operator is encountered, pop two operands, evaluate, and push the result back.

---

## 739. Daily Temperatures
→ Monotonic Stack (Next Greater Element)

**Signal:**
- Need the next greater/smaller element.
- Looking for the first future element satisfying a condition.
- Brute force compares every element with future elements.

**Key Learning:**
Maintain a monotonic stack of indices. When a larger element appears, resolve all smaller elements waiting in the stack.

---

## 853. Car Fleet
→ Monotonic Stack (Arrival Time)

**Signal:**
- Objects move toward the same destination.
- Faster objects cannot pass slower ones.
- Need to merge groups based on arrival time.

**Key Learning:**
Sort by position (closest to target first) and use a monotonic stack of arrival times to determine fleet formation.

---

## 84. Largest Rectangle in Histogram
→ Monotonic Increasing Stack

**Signal:**
- Need the largest area over contiguous bars.
- Previous taller bars become invalid when a shorter bar appears.

**Key Learning:**
Maintain a monotonic increasing stack to efficiently determine the width of each rectangle.

---

## 136. Single Number
→ Bit Manipulation (XOR)

**Signal:**
- Every element appears twice except one.
- Need O(n) time and O(1) extra space.

**Key Learning:**
XOR cancels duplicate values (`a ^ a = 0`), leaving only the unique element.

---

## 191. Number of 1 Bits
→ Bit Manipulation (Brian Kernighan's Algorithm)

**Signal:**
- Count set bits (1s) in a binary number.
- Need a solution faster than checking every bit.

**Key Learning:**
`n & (n - 1)` removes the rightmost set bit in each iteration.

---

## 338. Counting Bits
→ Dynamic Programming + Bit Manipulation

**Signal:**
- Compute results for every number from 0 to n.
- Previous answers can help compute the current answer.

**Key Learning:**
Use DP with the nearest power of 2 (`offset`) to build answers in O(n).

---

## 190. Reverse Bits
→ Bit Manipulation (Bit Shifting)

**Signal:**
- Reverse the binary representation of a number.
- Extract and reposition individual bits.

**Key Learning:**
Extract each bit using right shift and place it in the reversed position using left shift.

---

## 268. Missing Number
→ Bit Manipulation (XOR)

**Signal:**
- Numbers range from 0 to n.
- Exactly one number is missing.
- Need O(n) time and O(1) extra space.

**Key Learning:**
XOR all indices and numbers. Matching values cancel out, leaving the missing number.

---

## 704. Binary Search
→ Binary Search

**Signal:**
- Input array is sorted.
- Need efficient searching.
- Looking for O(log n) solution.

**Key Learning:**
Repeatedly eliminate half of the search space by comparing the target with the middle element.

---

## 74. Search a 2D Matrix
→ Binary Search (Two Binary Searches)

**Signal:**
- Matrix rows are sorted.
- First element of each row is greater than the last element of the previous row.
- Need O(log(m × n)) or O(log m + log n) solution.

**Key Learning:**
First locate the candidate row, then perform Binary Search within that row.

---

## 875. Koko Eating Bananas
→ Binary Search on Answer

**Signal:**
- Need to minimize/maximize a value.
- Can validate whether a candidate answer is feasible.
- Search space is a range of possible answers.

**Key Learning:**
Binary Search can be applied to the answer itself when the feasibility is monotonic.

---

## 153. Find Minimum in Rotated Sorted Array
→ Modified Binary Search

**Signal:**
- Sorted array has been rotated.
- Need minimum/rotation point.
- Half of the array is always sorted.

**Key Learning:**
Use the sorted half to determine which side contains the minimum.

---

## 33. Search in Rotated Sorted Array
→ Modified Binary Search

**Signal:**
- Sorted array has been rotated.
- Need O(log n) search.
- One half of the array is always sorted.

**Key Learning:**
Identify the sorted half, determine whether the target lies within it, and discard the other half.

---

## 981. Time Based Key-Value Store
→ Hash Map + Binary Search

**Signal:**
- Store historical values.
- Retrieve the latest value before or at a given timestamp.
- Data is inserted in increasing timestamp order.

**Key Learning:**
Use a Hash Map to group values by key and Binary Search to efficiently find the latest valid timestamp.

---

## 4. Median of Two Sorted Arrays
→ Binary Search on Partition

**Signal:**
- Two sorted arrays.
- Need the median.
- O(log(min(m, n))) solution expected.

**Key Learning:**
Partition both arrays so that the left half contains half of the total elements and every element on the left is less than or equal to every element on the right.

---

## 1929. Concatenation of Array
→ Array Traversal

**Signal:**
- Create a new array from an existing array.
- Traverse each element once.
- Use index manipulation.

**Key Learning:**
Pre-allocate the result array and fill it using calculated indices.

---
