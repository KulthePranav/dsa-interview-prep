"""
Problem: Find Minimum in Rotated Sorted Array

LeetCode: 153
Difficulty: Medium

Pattern:
Modified Binary Search

Approach:
1. Track the current minimum.
2. If the current range is already sorted, the leftmost element is the minimum.
3. Find the middle element.
4. Identify the sorted half.
5. Search the unsorted half.

Alternative Solution:
Compare the middle element with the right boundary.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Key Learning:
In a rotated sorted array, one half is always sorted. Use this property to eliminate half of the search space.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res


# ------------------------------------------------------------------
# Alternative Solution (Preferred in Interviews)
# ------------------------------------------------------------------

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#
#         while left < right:
#             mid = (left + right) // 2
#
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
#
#         return nums[left]
