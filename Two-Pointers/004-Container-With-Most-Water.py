"""
Problem: Container With Most Water

LeetCode: 11
Difficulty: Medium

Pattern:
Greedy + Two Pointers

Approach:
1. Place pointers at both ends.
2. Calculate the area.
3. Update maximum area.
4. Move the pointer with the smaller height.
5. Continue until pointers meet.

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Solution:
Brute Force by checking every pair.

Alternative Complexity:
Time: O(n²)
Space: O(1)

Key Learning:
The smaller height determines the area.
Always move the limiting height.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])

            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
