"""
Problem: Longest Consecutive Sequence

LeetCode: 128
Difficulty: Medium

Pattern:
Hash Set

Approach:
1. Store all numbers in a hash set for O(1) lookups.
2. A number is the start of a sequence if (num - 1) is not in the set.
3. For each sequence start:
   - Count consecutive numbers.
   - Track the maximum sequence length.
4. Return the longest length found.

Example:
nums = [100, 4, 200, 1, 3, 2]

Sequence:
1 -> 2 -> 3 -> 4

Answer:
4

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
Only start counting from the beginning of a sequence.
This prevents revisiting elements and achieves O(n).
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1

                while num + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest
