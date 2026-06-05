"""
Problem: Product of Array Except Self

LeetCode: 238
Difficulty: Medium

Pattern:
Prefix & Postfix Products

Approach:
1. First pass:
   Store the product of all elements to the left of each index.
2. Second pass:
   Multiply each position by the product of all elements to the right.
3. The final value at each index represents the product of all
   elements except itself.

Example:
nums = [1, 2, 3, 4]

Prefix Pass:
res = [1, 1, 2, 6]

Postfix Pass:
res = [24, 12, 8, 6]

Time Complexity:
O(n)

Space Complexity:
O(1) extra space
(Output array is not counted)

Key Learning:
When a problem requires information from both the left and right sides
of an element, consider using Prefix and Postfix computations.
This avoids division and achieves optimal space complexity.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
