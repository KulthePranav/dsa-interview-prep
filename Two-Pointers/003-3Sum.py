"""
Problem: 3Sum

LeetCode: 15
Difficulty: Medium

Pattern:
Sorting + Two Pointers

Approach:
1. Sort the array.
2. Fix one number.
3. Use two pointers to find the remaining two numbers.
4. Skip duplicates to avoid repeated triplets.

Time Complexity:
O(n²)

Space Complexity:
O(1) extra space
(ignoring output array)

Alternative Solution:
Brute Force using three nested loops.

Alternative Complexity:
Time: O(n³)
Space: O(1)

Key Learning:
Sort first, then reduce the problem into multiple
Two Sum searches using Two Pointers.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, n in enumerate(nums):

            if i > 0 and nums[i - 1] == n:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = n + nums[l] + nums[r]

                if three_sum == 0:
                    res.append([n, nums[l], nums[r]])

                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif three_sum < 0:
                    l += 1

                else:
                    r -= 1

        return res
