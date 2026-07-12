"""
Problem: Remove Element

LeetCode: 27
Difficulty: Easy

Pattern:
Fast & Slow Pointers

Approach:
1. Use a fast pointer to scan every element.
2. Use a slow pointer to track where the next valid element should be placed.
3. Copy valid elements forward.
4. Return the new length.

Alternative Solution:
Swap the target element with the last element when order does not matter.

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Learning:
Fast & Slow Pointers are commonly used for in-place array modification.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


# ------------------------------------------------------------------
# Alternative Solution (Order Not Preserved)
# ------------------------------------------------------------------

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i = 0
#         n = len(nums)
#
#         while i < n:
#             if nums[i] == val:
#                 nums[i] = nums[n - 1]
#                 n -= 1
#             else:
#                 i += 1
#
#         return n
