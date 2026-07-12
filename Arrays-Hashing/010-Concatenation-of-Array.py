"""
Problem: Concatenation of Array

LeetCode: 1929
Difficulty: Easy

Pattern:
Array Traversal

Approach:
1. Create a result array of size 2 * n.
2. Traverse the original array.
3. Copy each element to its original position and position + n.

Alternative Solutions:
1. nums + nums
2. nums * 2

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
Pre-allocate the result array and use index manipulation for efficient copying.
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + n] = num

        return ans


# ------------------------------------------------------------------
# Alternative Solution 1 (Pythonic)
# ------------------------------------------------------------------

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums


# ------------------------------------------------------------------
# Alternative Solution 2
# ------------------------------------------------------------------

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums * 2
