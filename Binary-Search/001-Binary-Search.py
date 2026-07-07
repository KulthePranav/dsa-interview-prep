"""
Problem: Binary Search

LeetCode: 704
Difficulty: Easy

Pattern:
Binary Search

Approach:
1. Initialize left and right pointers.
2. Find the middle element.
3. Compare it with the target.
4. Search the appropriate half.
5. Repeat until found or pointers cross.

Alternative Solution:
Recursive Binary Search

Time Complexity:
O(log n)

Space Complexity:
Iterative: O(1)
Recursive: O(log n)

Key Learning:
Each comparison eliminates half of the search space.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            elif target < nums[middle]:
                right = middle - 1

            else:
                left = middle + 1

        return -1


# ------------------------------------------------------------------
# Alternative Solution: Recursive Binary Search
# ------------------------------------------------------------------

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#
#         def binary_search(left, right):
#
#             if left > right:
#                 return -1
#
#             mid = (left + right) // 2
#
#             if nums[mid] == target:
#                 return mid
#
#             if target < nums[mid]:
#                 return binary_search(left, mid - 1)
#
#             return binary_search(mid + 1, right)
#
#         return binary_search(0, len(nums) - 1)
