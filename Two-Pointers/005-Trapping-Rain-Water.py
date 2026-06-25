"""
Problem: Trapping Rain Water

LeetCode: 42
Difficulty: Hard

Pattern:
Two Pointers

Approach:
1. Maintain left and right pointers.
2. Track left_max and right_max.
3. The smaller boundary determines trapped water.
4. Move the pointer with the smaller maximum.
5. Accumulate trapped water.

Example:
height = [4,2,0,3,2,5]

Water trapped:
2 + 4 + 1 + 2 = 9

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Solution:
Prefix & Postfix Maximum Arrays

Alternative Complexity:

Prefix Arrays:
Time: O(n)
Space: O(n)

Brute Force:
Time: O(n²)
Space: O(1)

Key Learning:
The smaller boundary determines how much water
can be trapped at a position.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        left_max = height[l]
        right_max = height[r]

        res = 0

        while l < r:

            if left_max < right_max:
                l += 1

                left_max = max(left_max, height[l])

                res += left_max - height[l]

            else:
                r -= 1

                right_max = max(right_max, height[r])

                res += right_max - height[r]

        return res


# Alternative Solution: Prefix & Postfix Maximum Arrays

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#
#         max_left = [0] * n
#         max_right = [0] * n
#
#         curr_max = 0
#         for i in range(n):
#             max_left[i] = curr_max
#             curr_max = max(curr_max, height[i])
#
#         curr_max = 0
#         for i in range(n - 1, -1, -1):
#             max_right[i] = curr_max
#             curr_max = max(curr_max, height[i])
#
#         trapped = 0
#
#         for i in range(n):
#             water_level = min(max_left[i], max_right[i])
#
#             if water_level > height[i]:
#                 trapped += water_level - height[i]
#
#         return trapped


# Alternative Solution: Brute Force

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         trapped = 0
#
#         for i in range(len(height)):
#             left_max = max(height[: i + 1])
#             right_max = max(height[i:])
#
#             trapped += min(left_max, right_max) - height[i]
#
#         return trapped
