"""
Problem: Search in Rotated Sorted Array

LeetCode: 33
Difficulty: Medium

Pattern:
Modified Binary Search

Approach:
1. Find the middle element.
2. Determine which half is sorted.
3. Check whether the target lies inside the sorted half.
4. Discard the other half.
5. Repeat until found.

Alternative Solution:
Use cleaner conditions that check whether the target lies inside the sorted half.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Key Learning:
A rotated sorted array always has one sorted half. Use that property to eliminate half of the search space.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


# ------------------------------------------------------------------
# Alternative Solution (Cleaner Conditions)
# ------------------------------------------------------------------

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#
#             if nums[mid] == target:
#                 return mid
#
#             if nums[left] <= nums[mid]:
#
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#
#             else:
#
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#
#         return -1
