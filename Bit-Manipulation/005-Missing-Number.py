"""
Problem: Missing Number

LeetCode: 268
Difficulty: Easy

Pattern:
Bit Manipulation (XOR)

Approach:
1. Initialize the result with n.
2. XOR every index.
3. XOR every value in the array.
4. Matching values cancel out.
5. The remaining value is the missing number.

Alternative Solution:
Use the sum formula:
n * (n + 1) // 2 - sum(nums)

Example:

Input:
[3, 0, 1]

Output:
2

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Complexity:
Time: O(n)
Space: O(1)

Key Learning:
XOR cancels identical values, making it ideal for finding a missing element.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = len(nums)

        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]

        return res


# ------------------------------------------------------------------
# Alternative Solution: Math Formula
# ------------------------------------------------------------------

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#
#         n = len(nums)
#
#         return (n * (n + 1) // 2) - sum(nums)
